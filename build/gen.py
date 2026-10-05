"""Shared helpers for the Ab Initio India site generator (content loading, images, writers).
Build the site with:  python build/gen2.py   (see README.md)."""
import json, os, re, sys, glob, shutil, html, datetime, importlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root; pages go to REPO/site
CONTENT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
sys.path.insert(0, CONTENT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import *  # noqa

SITE = "https://theprashant26.github.io/AbInitioIndia_Themes/"
FOLDERS = {"B": "site"}
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


# ------------------------------------------------------------------ link mapping shared by index + inner pages
TEXT_MAP = {"about us": "about.html", "about": "about.html", "our team": "team.html", "our mentors": "mentors.html",
            "our services": "services.html", "services": "services.html", "insights": "insights.html",
            "contact us": "contact.html", "faq": "faq.html", "privacy policy": "privacy-policy.html",
            "disclaimer": "disclaimer.html", "terms of use": "terms-of-use.html", "cookie policy": "cookie-policy.html"}
HREF_MAP = {"#services": "services.html", "#about": "about.html", "#insights": "insights.html", "#contact": "contact.html", "#top": "index.html"}
A_RE = re.compile(r'<a\b([^>]*?)href="(#[a-z-]+)"([^>]*)>(.*?)</a>', re.S)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def relink_home(src):
    """Turn the homepage #anchor links into real page links (idempotent)."""
    # insight cards: every #insights link inside the n-th <article> goes to the n-th newest post
    n = [0]
    def art(m):
        slug = POSTS[n[0]]["slug"]; n[0] += 1
        return m.group(0).replace('href="#insights"', f'href="insights/{slug}.html"')
    src = re.sub(r"<article\b.*?</article>", art, src, flags=re.S)

    def a(m):
        pre, href, post, inner = m.groups()
        text = strip_tags(inner)
        target = None
        for s in SERVICES:  # service cards (text starts with the card title)
            if text.startswith(html.unescape(s["card_title"])) and len(text) > len(html.unescape(s["card_title"])) + 5:
                target = f"services/{s['slug']}.html"
        target = target or TEXT_MAP.get(text.lower()) or HREF_MAP.get(href)
        return f'<a{pre}href="{target}"{post}>{inner}</a>' if target else m.group(0)
    return A_RE.sub(a, src)


def prefix(fragment, R):
    if not R:
        return fragment
    return re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|data:|/)([^"]+)"', lambda m: f'{m.group(1)}="{R}{m.group(2)}"', fragment)


class Chrome:
    def __init__(self, folder):
        s = open(os.path.join(REPO, folder, "index.html"), encoding="utf-8").read()
        self.head_extra = s[s.index('<link rel="icon"'):s.index("</head>")]
        self.header = s[s.index('<a class="skip-link"'):s.index("</header>") + len("</header>")]
        self.footer = s[s.index("<footer"):s.index("<script src=")]
        self.scripts = s[s.index("<script src="):s.index("</body>")]

    def nav(self, current):
        h = self.header
        group = current.split("/")[0] if "/" in current else None
        def mark(m):
            cls, href = m.group(1), m.group(2)
            if "dropdown-toggle" in cls:
                return f'<a class="{cls} active" href="{href}"' if current in ("about.html", "team.html", "mentors.html") else m.group(0)
            if href == current:
                return f'<a class="{cls} active" aria-current="page" href="{href}"'
            if (group == "services" and href == "services.html") or (group == "insights" and href == "insights.html"):
                return f'<a class="{cls} active" href="{href}"'
            return m.group(0)
        return re.sub(r'<a class="((?:nav-link|dropdown-item)[^"]*)" href="([^"]+)"', mark, h)


# ------------------------------------------------------------------ page shell
def shell(T, page):
    R = "../" if "/" in page["path"] else ""
    url = SITE + T.folder + "/" + page["path"]
    if page["path"] == "index.html":
        url = SITE + T.folder + "/"
    img = page.get("og_image") or "assets/img/logo.png"
    og = SITE + T.folder + "/" + img
    robots = '\n<meta name="robots" content="noindex">' if page.get("noindex") else ""
    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page['title'])}</title>
<meta name="description" content="{esc(page['desc'])}">{robots}
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="{page.get('og_type', 'website')}">
<meta property="og:site_name" content="Ab Initio India">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['desc'])}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(og)}">
<meta name="twitter:card" content="summary_large_image">
{prefix(T.chrome.head_extra, R)}</head>
<body>
"""
    current = page.get("nav", page["path"])
    return (head + prefix(T.chrome.nav(current), R) + '\n\n<main id="main">\n' + page["body"].strip() +
            "\n</main>\n" + prefix(T.chrome.footer, R) + prefix(T.chrome.scripts, R) + "</body></html>\n")


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


# ------------------------------------------------------------------ build
class Theme:
    def __init__(self, key):
        self.key = key; self.folder = FOLDERS[key]; self.dir = os.path.join(REPO, self.folder)
        self.base = SITE + self.folder + "/"


def build(key):
    T = Theme(key)
    skin = importlib.import_module(f"skin_{key.lower()}")
    # 1. homepage: real links + SEO tags (nothing else changes)
    ipath = os.path.join(T.dir, "index.html")
    s = open(ipath, encoding="utf-8").read()
    s = relink_home(s)
    if 'property="og:title"' not in s:
        m = re.search(r"<title>(.*?)</title>\n<meta name=\"description\" content=\"(.*?)\">", s)
        og = (f'\n<link rel="canonical" href="{T.base}">\n<meta property="og:type" content="website">\n'
              f'<meta property="og:site_name" content="Ab Initio India">\n<meta property="og:title" content="{m.group(1)}">\n'
              f'<meta property="og:description" content="{m.group(2)}">\n<meta property="og:url" content="{T.base}">\n'
              f'<meta property="og:image" content="{T.base}assets/img/logo.png">\n<meta name="twitter:card" content="summary_large_image">')
        s = s.replace(m.group(0), m.group(0) + og, 1)
    write(ipath, s)
    T.chrome = Chrome(T.folder)
    img = Images(T.dir)
    ctx = dict(T=T, img=img, posts=POSTS, legal=LEGAL_HTML, post_body=post_body, fmt_date=fmt_date, esc=esc, base=T.base)
    import pagespec
    pages = pagespec.pages(ctx, skin)
    for page in pages:
        write(os.path.join(T.dir, page["path"]), shell(T, page))
    img.copy()
    # sitemap + robots
    urls = ["index.html"] + [p["path"] for p in pages if not p.get("noindex")]
    today = datetime.date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = T.base if u == "index.html" else T.base + u
        sm.append(f"  <url><loc>{esc(loc)}</loc><lastmod>{today}</lastmod></url>")
    sm.append("</urlset>")
    write(os.path.join(T.dir, "sitemap.xml"), "\n".join(sm) + "\n")
    write(os.path.join(T.dir, "robots.txt"), f"User-agent: *\nAllow: /\n\nSitemap: {T.base}sitemap.xml\n")
    print(key, len(pages), "pages,", len(img.used), "images")
    return pages


if __name__ == "__main__":
    for k in sys.argv[1:] or ["B"]:
        build(k)
