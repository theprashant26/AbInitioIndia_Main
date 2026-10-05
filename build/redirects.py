"""301 redirects from the old WordPress URLs to the new pages (keeps search rankings and old links working).

Reads build/redirects.csv (columns: old_path, new_path, match, note) and writes
  site/.htaccess                  Apache (mod_alias RedirectMatch); deployed with the site
  server/nginx-redirects.conf     nginx map + server snippet, for the server admin
match = exact   -> /old-path and /old-path/ redirect to new_path
match = prefix  -> old_path (with or without the slash) and everything below it redirects to new_path
Run by gen2.py on every build; to run on its own: python build/redirects.py"""
import csv, os, re

S = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(S)
SRC = os.path.join(S, "redirects.csv")


def pattern(old, match):
    base = re.escape(old.rstrip("/")) if old != "/" else ""
    return f"^{base}(/.*)?$" if match == "prefix" else f"^{base}/?$"


def build(site_dir=os.path.join(REPO, "site")):
    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    for r in rows:  # a redirect to a page that does not exist would just trade one 404 for another
        target = r["new_path"].lstrip("/") or "index.html"
        if not os.path.exists("\\\\?\\" + os.path.abspath(os.path.join(site_dir, target))):
            raise SystemExit(f"redirects.csv: {r['old_path']} -> {r['new_path']}: no such page in site/")
    rows.sort(key=lambda r: r["match"] != "exact")  # exact rules first so they win over the broad prefix rules

    ht = ["# 301 redirects from the old WordPress URLs. Generated from build/redirects.csv by build/redirects.py:",
          "# edit the CSV and rebuild instead of editing this file.",
          "<IfModule mod_alias.c>"]
    ht += [f'  RedirectMatch 301 "{pattern(r["old_path"], r["match"])}" "{r["new_path"]}"' for r in rows]
    ht += ["</IfModule>", "", "# Friendly error page", "ErrorDocument 404 /404.html", ""]
    with open(os.path.join(site_dir, ".htaccess"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(ht))

    ng = ["# 301 redirects from the old WordPress URLs. Generated from build/redirects.csv by build/redirects.py.",
          "# 1) Put the map block in the http { } context.",
          "map $uri $abinitio_redirect {",
          '    default "";']
    ng += [f'    "~{pattern(r["old_path"], r["match"])}" "{r["new_path"]}";' for r in rows]
    ng += ["}", "",
           "# 2) Inside the server { } block for abinitioindia.com:",
           "#    if ($abinitio_redirect) { return 301 $abinitio_redirect; }",
           "#    error_page 404 /404.html;", ""]
    os.makedirs(os.path.join(REPO, "server"), exist_ok=True)
    with open(os.path.join(REPO, "server", "nginx-redirects.conf"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(ng))
    return len(rows)


if __name__ == "__main__":
    print(build(), "redirects written to site/.htaccess and server/nginx-redirects.conf")
