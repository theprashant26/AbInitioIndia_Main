"""sitemap.xml (every indexable page) and robots.txt, for BASE_URL. Run by gen2.py on every build.
Articles carry their publication date as lastmod; other pages have none (a build date would say nothing)."""
import os
from html import escape


def build(site_dir, base, pages):
    urls = []
    for p in pages:
        if p.get("noindex"):
            continue
        loc = base if p["path"] == "index.html" else base + p["path"]
        lastmod = f"<lastmod>{p['post']['date']}</lastmod>" if p.get("post") else ""
        urls.append(f"  <url><loc>{escape(loc)}</loc>{lastmod}</url>")
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', *urls, "</urlset>", ""]
    with open(os.path.join(site_dir, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(xml))
    with open(os.path.join(site_dir, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base}sitemap.xml\n")
    return len(urls)
