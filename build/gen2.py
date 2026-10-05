"""Site build. Usage: python build/gen2.py
Every page (including index.html) is rendered by skin_<x>_glass.py; sitemap.xml/robots.txt are left untouched."""
import os, sys, json, shutil, importlib, html
import gen  # content loading, image helper, writers
import redirects
from gen import POSTS, LEGAL_HTML, post_body, Images, write, fmt_date, esc, SITE, FOLDERS, MANIFEST, REPO

S = os.path.dirname(os.path.abspath(__file__))
STOCK = os.path.join(S, "stock")
CREDITS = json.load(open(os.path.join(STOCK, "credits.json")))
for name, c in CREDITS.items():  # stock photos join the manifest
    MANIFEST["stock/" + name] = {"file": f"stock/{name}.webp", "w": c["size"][0], "h": c["size"][1], "stock": True}

HOME_META = {
    "A": "Ab Initio India | Business Consultants – Theme A",
    "B": "Ab Initio India | Business Consultants – Theme B",
    "C": "Ab Initio India | Business Consultants – Theme C",
}
HOME_DESC = "Ab Initio India LLP – business consultants in New Delhi offering strategic, transaction, regulatory and India entry advisory."


class GlassImages(Images):
    """Adds WebP thumbnails / responsive variants generated at build time."""
    def __init__(self, d):
        super().__init__(d); self.variants = {}

    def variant(self, key, width, R=""):
        m = MANIFEST[key]
        base = os.path.splitext(m["file"])[0]
        rel = f"v/{base}-{width}.webp"
        self.variants[rel] = (m, width)
        h = round(m["h"] * min(width, m["w"]) / m["w"])
        return f"{R}assets/img/{rel}", min(width, m["w"]), h

    def thumb_tag(self, key, R, alt="", cls=None, width=640):
        src, w, h = self.variant(key, width, R)
        c = f' class="{cls}"' if cls else ""
        return f'<img{c} src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy">'

    def srcset_tag(self, key, R, alt, widths=(640, 960, 1400), sizes="100vw", cls=None, eager=False, extra=""):
        parts = []
        for wd in widths:
            src, w, h = self.variant(key, wd, R); parts.append(f"{src} {w}w")
        src, w, h = self.variant(key, widths[-1], R)
        c = f' class="{cls}"' if cls else ""
        return f'<img{c} src="{src}" srcset="{", ".join(parts)}" sizes="{sizes}" alt="{esc(alt)}" width="{w}" height="{h}" loading="{"eager" if eager else "lazy"}"{extra}>'

    def copy_variants(self):
        from PIL import Image as PI
        for rel, (m, width) in self.variants.items():
            dst = os.path.join(self.dir, "assets", "img", rel)
            if os.path.exists(dst):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            src = os.path.join(STOCK, os.path.basename(m["file"])) if m.get("stock") else os.path.join(gen.CONTENT, "img", m["file"])
            im = PI.open(src).convert("RGB")
            if im.width > width:
                im = im.resize((width, round(im.height * width / im.width)), PI.LANCZOS)
            im.save(dst, "WEBP", quality=78, method=6)

    def copy(self):
        for f in self.used:
            dst = os.path.join(self.dir, "assets", "img", f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            src = os.path.join(STOCK, os.path.basename(f)) if f.startswith("stock/") else os.path.join(gen.CONTENT, "img", f)
            shutil.copyfile(src, dst)


def skin_head(skin, R, page):
    return skin.head_assets(R, page) if hasattr(skin, "head_assets") else ""


def default_assets(skin, R, preload):
    if hasattr(skin, "head_assets"):
        return ""
    return DEFAULT_ASSETS.replace("{R}", R).replace("{FONTS}", skin.FONTS) + preload.replace("{R}", R)


def shell(T, skin, page):
    R = page.get("root") or ("../" if "/" in page["path"] else "")
    site = getattr(skin, "CANONICAL_BASE", T.base)  # one constant: preview vs live domain
    url = site if page["path"] == "index.html" else site + page["path"]
    og = site + (page.get("og_image") or "assets/img/logo.png")
    robots = '\n<meta name="robots" content="noindex">' if page.get("noindex") else ""
    preload = page.get("preload", "")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page['title'])}</title>
<meta name="description" content="{esc(page['desc'])}">{robots}
<meta name="theme-color" content="{skin.THEME_COLOR}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="{page.get('og_type', 'website')}">
<meta property="og:site_name" content="Ab Initio India">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['desc'])}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(og)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}assets/img/logo.png">{skin_head(skin, R, page)}
{default_assets(skin, R, preload)}
</head>
<body class="{page.get('body_cls', 'page-inner')}">
{skin.backdrop(R, page)}
{skin.header(R, page.get('nav', page['path']))}
<main id="main">
{page['body'].strip()}
</main>
{skin.footer(R)}
{getattr(skin, "body_end", lambda R, p: "")(R, page)}<script src="{R}assets/vendor/bootstrap.bundle.min.js" defer></script>
<script src="{R}assets/js/main.js" defer></script>
</body></html>
"""


def client_logos(T):
    """Small WebP copies of the client logos (the originals include a 125 KB PNG)."""
    from PIL import Image as PI
    from site_data import CLIENTS
    import glob as _g
    for old in _g.glob(os.path.join(T.dir, "assets", "img", "clients", "c-*")):
        os.remove(old)  # brand-named files can be caught by content blockers
    for i, (f, _) in enumerate(CLIENTS, 1):
        base = os.path.join(T.dir, "assets", "img", "clients", f"client-{i:02d}")
        os.makedirs(os.path.dirname(base), exist_ok=True)
        im = PI.open(os.path.join(S, "clients_src", f))
        alpha = im.mode in ("RGBA", "P", "LA")
        im = im.convert("RGBA" if alpha else "RGB")
        im.thumbnail((240, 96), PI.LANCZOS)
        im.save(base + ".webp", "WEBP", quality=82, method=6)
        if f.endswith(".png"): im.save(base + ".png", optimize=True)
        else: im.save(base + ".jpg", quality=85, optimize=True)


DEFAULT_ASSETS = """<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="{FONTS}" as="style" onload="this.onload=null;this.rel='stylesheet'">
<link rel="preload" href="{R}assets/vendor/bootstrap-icons/bootstrap-icons.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link href="{FONTS}" rel="stylesheet"><link rel="stylesheet" href="{R}assets/vendor/bootstrap-icons/bootstrap-icons.min.css"></noscript>
<link rel="stylesheet" href="{R}assets/vendor/bootstrap.subset.min.css">
<link rel="stylesheet" href="{R}assets/css/style.css">
<script>(function(d){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;d.classList.add('motion');setTimeout(function(){d.classList.add('reveal-done')},1500)})(document.documentElement)</script>"""


class Theme:
    def __init__(self, key):
        self.key = key; self.folder = FOLDERS[key]; self.dir = os.path.join(REPO, self.folder); self.base = gen.BASE_URL


def build(key):
    T = Theme(key)
    skin = importlib.import_module(f"skin_{key.lower()}_glass")
    img = GlassImages(T.dir)
    ctx = dict(T=T, img=img, posts=POSTS, legal=LEGAL_HTML, post_body=post_body, fmt_date=fmt_date, esc=esc, base=T.base, key=key)
    import pagespec
    pages = [dict(path="index.html", title=HOME_META[key], desc=HOME_DESC, body_cls="page-home", body=skin.home(ctx, ""),
                  preload=getattr(skin, "HOME_PRELOAD", ""))]
    pages += pagespec.pages(ctx, skin)
    for p in pages:
        if p["path"] == "404.html" or p["path"] == "thank-you.html":
            p["body_cls"] = "page-center"
        write(os.path.join(T.dir, p["path"]), shell(T, skin, p))
    img.copy(); img.copy_variants(); client_logos(T)
    shutil.copyfile(os.path.join(S, "ScrollTrigger.min.js"), os.path.join(T.dir, "assets", "vendor", "ScrollTrigger.min.js"))
    shutil.copyfile(os.path.join(S, getattr(skin, "MAIN_JS", "main_glass.js")), os.path.join(T.dir, "assets", "js", "main.js"))
    if hasattr(skin, "post_build"):
        skin.post_build(T, pages)
    redirects.build(T.dir)
    print(key, len(pages), "pages,", len(img.used), "images")


if __name__ == "__main__":
    for k in ["B"]:
        build(k)
