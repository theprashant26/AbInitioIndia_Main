"""Logo and favicons, generated from the client's logo file (content/img/brand/logo-source.png).

The source is the logo on a white background. The white is turned into transparency (GIMP's
"colour to alpha", so anti-aliased edges and the grey chevron stay smooth on any background),
the margin is trimmed, and these are written:
  assets/img/logo.png, logo.webp    header/footer logo, 4x the 46 px display height (sharp on retina)
  assets/img/favicon-192.png        the pen-and-sword "A" mark, square, for browser tabs
  assets/img/apple-touch-icon.png   the mark on white, 180x180, for iOS home screens
  favicon.ico                       16/32/48 px, at the web root (browsers request /favicon.ico)
Run by gen2.py; to replace the logo, overwrite logo-source.png and rebuild."""
import os
from PIL import Image, ImageChops, ImageMath

S = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(S, "content", "img", "brand", "logo-source.png")
DISPLAY_H = 46          # .brand img height in style.css
_eval = getattr(ImageMath, "unsafe_eval", None) or ImageMath.eval


def transparent_logo():
    rgb = Image.open(SOURCE).convert("RGB")
    r, g, b = rgb.split()
    alpha = ImageChops.invert(ImageChops.darker(ImageChops.darker(r, g), b))  # 255 - min(r, g, b)
    alpha = alpha.point(lambda v: 0 if v < 5 else v)                          # the off-white paper
    unmix = lambda c: _eval("convert(min(max((float(c) - 255 + a) * 255 / max(float(a), 1), 0), 255), 'L')", c=c, a=alpha)
    logo = Image.merge("RGBA", (unmix(r), unmix(g), unmix(b), alpha))
    return logo.crop(alpha.point(lambda v: 255 if v > 8 else 0).getbbox())


def mark(logo):
    """The "A" mark alone (pen, sword, chevron), padded to a square. The sword's guard overlaps the
    lettering horizontally, so the mark is taken as the shapes that start in the left quarter."""
    top = round(logo.height * 0.88)                     # above the tagline
    k = 2                                               # label shapes on a half-size mask (fast)
    small = logo.getchannel("A").crop((0, 0, logo.width, top)).resize((logo.width // k, top // k))
    w, h = small.size; px = small.load(); seen = [[False] * w for _ in range(h)]
    keep = Image.new("L", (w, h), 0); kp = keep.load()
    for y0 in range(h):
        for x0 in range(w):
            if seen[y0][x0] or px[x0, y0] <= 8:
                continue
            stack, comp = [(x0, y0)], []; seen[y0][x0] = True
            while stack:
                x, y = stack.pop(); comp.append((x, y))
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and px[nx, ny] > 8:
                        seen[ny][nx] = True; stack.append((nx, ny))
            if min(x for x, _ in comp) < w * 0.27:
                for x, y in comp: kp[x, y] = 255
    keep = keep.resize((logo.width, top), Image.NEAREST)
    part = logo.crop((0, 0, logo.width, top))
    part.putalpha(ImageChops.multiply(part.getchannel("A"), keep))
    part = part.crop(part.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
    side = round(max(part.size) * 1.08)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(part, ((side - part.width) // 2, (side - part.height) // 2), part)
    return sq


def build(site_dir):
    logo = transparent_logo()
    h = DISPLAY_H * 4
    big = logo.resize((round(logo.width * h / logo.height), h), Image.LANCZOS)
    img = os.path.join(site_dir, "assets", "img")
    big.save(os.path.join(img, "logo.png"), optimize=True)
    big.save(os.path.join(img, "logo.webp"), "WEBP", quality=90, method=6)
    m = mark(logo)
    m.resize((192, 192), Image.LANCZOS).save(os.path.join(img, "favicon-192.png"), optimize=True)
    touch = Image.new("RGB", (180, 180), "white")
    inner = m.resize((150, 150), Image.LANCZOS); touch.paste(inner, (15, 15), inner)
    touch.save(os.path.join(img, "apple-touch-icon.png"), optimize=True)
    m.resize((256, 256), Image.LANCZOS).save(os.path.join(site_dir, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    return big.size
