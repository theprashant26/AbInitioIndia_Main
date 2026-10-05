"""Write assets/vendor/bootstrap.subset.min.css: Bootstrap 5.3 rules used by a theme's pages.
Keeps a selector only when every class it requires (outside :not()) is used in the HTML or is a
class Bootstrap's JS toggles at runtime. :root, @font-face, @keyframes and element rules are kept."""
import os, re, glob, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
# Usage (from the project root): python build/purge.py site
RUNTIME = {"show", "showing", "hiding", "collapsing", "collapse", "collapsed", "fade", "active", "disabled",
           "dropdown-menu-end", "dropdown-menu-start", "dropup", "dropend", "dropstart", "dropdown-toggle",
           "dropdown-menu", "dropdown-item", "dropdown", "visually-hidden", "visually-hidden-focusable"}


def used_classes(theme_dir):
    used = set(RUNTIME)
    for f in glob.glob(os.path.join(theme_dir, "**", "*.html"), recursive=True):
        s = open("\\\\?\\" + os.path.abspath(f), encoding="utf-8").read()
        for attr in re.findall(r'class="([^"]*)"', s):
            used.update(attr.split())
    return used


def blocks(css):
    """Split CSS into top-level (prelude, body) pairs, honouring nested braces."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while depth and k < n:
            if css[k] == "{": depth += 1
            elif css[k] == "}": depth -= 1
            k += 1
        out.append((prelude, css[j + 1:k - 1]))
        i = k
    return out


def keep_selector(sel, used):
    sel = re.sub(r":not\([^)]*\)", "", sel)
    classes = re.findall(r"\.(-?[_a-zA-Z][\w-]*)", sel)
    return all(c in used for c in classes)


def purge(css, used):
    out = []
    for prelude, body in blocks(css):
        if prelude.startswith("@charset"):
            continue
        if prelude.startswith(("@media", "@supports", "@container", "@layer")):
            inner = purge(body, used)
            if inner:
                out.append(f"{prelude}{{{inner}}}")
        elif prelude.startswith(("@keyframes", "@-webkit-keyframes", "@font-face", "@page")):
            out.append(f"{prelude}{{{body}}}")
        else:
            sels = [s for s in prelude.split(",") if keep_selector(s, used)]
            if sels:
                out.append(f"{','.join(sels)}{{{body}}}")
    return "".join(out)


if __name__ == "__main__":
    for folder in sys.argv[1:]:
        d = os.path.join(REPO, folder)
        src = open(os.path.join(d, "assets", "vendor", "bootstrap.min.css"), encoding="utf-8").read()
        header = src[:src.index("*/") + 2] if src.startswith("/*") else ""
        body = src[len(header):]
        css = purge(re.sub(r"/\*.*?\*/", "", body, flags=re.S), used_classes(d))
        note = "/* Subset of Bootstrap v5.3 generated from this theme's pages (full file: bootstrap.min.css) */\n"
        open(os.path.join(d, "assets", "vendor", "bootstrap.subset.min.css"), "w", encoding="utf-8").write(header + "\n" + note + css)
        print(folder, len(src) // 1024, "KB ->", len(css) // 1024, "KB")
