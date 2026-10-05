"""Shared helpers for the Ab Initio India site generator (content loading, images, writers).
Build the site with:  python _build/gen2.py   (see README.md)."""
import json, os, re, sys, glob, shutil, html, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root = the website
CONTENT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
sys.path.insert(0, CONTENT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import *  # noqa

# Absolute address of the site (canonical, og:url, og:image, JSON-LD, form redirect). Always the
# live domain, also on the GitHub Pages preview, so search engines treat abinitioindia.com as the original.
BASE_URL = "https://abinitioindia.com/"
MANIFEST = json.load(open(os.path.join(CONTENT, "img-manifest.json")))
esc = lambda s: html.escape(s, quote=True)


def lp(path):
    """Extended-length path so slugs longer than MAX_PATH can be written on Windows."""
    return "\\\\?\\" + os.path.abspath(path)


def write(path, text):
    os.makedirs(lp(os.path.dirname(path)), exist_ok=True)
    with open(lp(path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def fmt_date(d):
    d = datetime.date.fromisoformat(d)
    return f"{d.day} {d:%B %Y}"


# ------------------------------------------------------------------ posts
def load_posts():
    posts = []
    for f in glob.glob(os.path.join(CONTENT, "posts", "*.json")):
        p = json.load(open(f, encoding="utf-8"))
        p["title"] = fix(p["title"])
        p["cat"] = CATEGORY_LABEL.get(p["categories"][0], p["categories"][0])
        p["cats"] = [CATEGORY_LABEL.get(c, c) for c in p["categories"]]
        body = p["body_html"]
        # WordPress tag archives do not exist on the new site: keep the words, drop the link
        body = re.sub(r'<a href="https://abinitioindia\.com/tag/[^"]*">(.*?)</a>', r"\1", body, flags=re.S)
        for a in re.findall(r'<a href="(http[^"]+)"', body):
            body = body.replace(f'<a href="{a}"', f'<a href="{a}" target="_blank" rel="noopener"', 1)
        # endnote anchors whose targets were not part of the article
        body = re.sub(r'<a href="#_edn\d+">(.*?)</a>', r"\1", body, flags=re.S)
        # article h1 lives in the banner, so the body's top heading level becomes h2
        # and no heading skips a level (each is at most one deeper than the previous)
        levels = [int(x) for x in re.findall(r"<h([2-6])\b", body)]
        if levels:
            shift, prev, out = min(levels) - 2, 1, []
            for lv in levels:
                prev = min(lv - shift, prev + 1); out.append(prev)
            it = iter(out); cur = [0]
            def heading(m):
                if not m.group(1):
                    cur[0] = next(it)
                return f"<{m.group(1)}h{cur[0]}"
            body = re.sub(r"<(/?)h[2-6]\b", heading, body)
        # wide tables scroll sideways on phones (.prose table is overflow-x:auto): keyboard users need to reach them
        body = body.replace("<table>", '<table tabindex="0">')
        before = body
        body = fix(body)
        p["typo_fixed"] = before != body
        p["body"] = body
        p["desc"] = (p.get("meta_description") or p["excerpt"]).strip()
        p["desc"] = fix(re.sub(r"\s+", " ", html.unescape(p["desc"])))[:300]
        posts.append(p)
    posts.sort(key=lambda p: (p["date"], p["id"]), reverse=True)
    return posts


POSTS = load_posts()
LEGAL_HTML = {k: fix(v) for k, v in json.load(open(os.path.join(CONTENT, "legal.json"), encoding="utf-8")).items()}


# ------------------------------------------------------------------ images
class Images:
    def __init__(self, theme_dir):
        self.dir = theme_dir; self.used = set()

    def __call__(self, key, R=""):
        m = MANIFEST[key]; self.used.add(m["file"])
        return f'{R}assets/img/{m["file"]}', m["w"], m["h"]

    def tag(self, key, R, alt, cls=None, eager=False, extra=""):
        src, w, h = self(key, R)
        c = f' class="{cls}"' if cls else ""
        return f'<img{c} src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="{"eager" if eager else "lazy"}"{extra}>'

    def copy(self):
        for f in self.used:
            dst = os.path.join(self.dir, "assets", "img", f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(os.path.join(CONTENT, "img", f), dst)


FIGURE_SIZES = "(min-width: 1400px) 760px, (min-width: 992px) 66vw, (min-width: 576px) 85vw, 76vw"


def post_body(p, R, img):
    """Article body with local image paths; returns (body_html, featured_in_body)."""
    body = p["body"]; featured_in_body = False
    for src, key in p["body_img_keys"]:
        if key == p["img_key"]:
            featured_in_body = True
        if hasattr(img, "srcset_tag"):  # responsive WebP variants; the featured image is the page's LCP
            lead = key == p["img_key"]
            tag = lambda m: img.srcset_tag(key, R, m.group(1) or p["title"], (480, 800, 1200), FIGURE_SIZES,
                                           eager=lead, extra=' fetchpriority="high"' if lead else "")
        else:
            local, w, h = img(key, R)
            tag = lambda m: f'<img src="{local}" alt="{esc(m.group(1) or p["title"])}" width="{w}" height="{h}" loading="lazy">'
        body = re.sub(r'<img alt="([^"]*)" src="' + re.escape(src) + '"/?>', tag, body)
    return body, featured_in_body
