"""Per-page critical CSS, inlined so a page can render without waiting for a stylesheet request.

For every page, the rules of Bootstrap (subset), the icon rules and style.css are pruned to those that can
match the page: a selector is kept unless it needs a class, id or attribute name that appears neither in
the page's HTML nor in the site JavaScript (which adds state classes such as is-open, show, collapsing).
The result is minified and written into <style> in <head>; the full stylesheets still load without
blocking rendering, as a safety net for anything added later.

Icons: instead of the 86 KB bootstrap-icons.min.css, each page inlines the rules for the icons it uses, and
build_icon_font() writes a WOFF2 holding only the icons used anywhere on the site (fonttools)."""
import os, re

ICON_CSS = os.path.join("assets", "vendor", "bootstrap-icons", "bootstrap-icons.min.css")
ICON_FONT = os.path.join("assets", "vendor", "bootstrap-icons", "fonts", "bootstrap-icons.woff2")
ICON_SUBSET = "assets/fonts/bootstrap-icons-subset.woff2"
SHEETS = [os.path.join("assets", "vendor", "bootstrap.subset.min.css"), os.path.join("assets", "css", "style.css")]
JS = [os.path.join("assets", "js", "main.js"), os.path.join("assets", "vendor", "bootstrap.bundle.min.js")]


# ------------------------------------------------------------------ tiny CSS parser
def _strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def _blocks(css):
    """Top-level (prelude, body) pairs; body is None for statements such as @import/@charset."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = i
        while j < n and css[j] not in "{;":
            if css[j] in "\"'":  # skip strings
                q = css[j]; j += 1
                while j < n and css[j] != q: j += 2 if css[j] == "\\" else 1
            j += 1
        if j >= n:
            break
        prelude = css[i:j].strip()
        if css[j] == ";":
            if prelude: out.append((prelude, None))
            i = j + 1; continue
        depth, k = 1, j + 1
        while k < n and depth:
            c = css[k]
            if c in "\"'":
                q = c; k += 1
                while k < n and css[k] != q: k += 2 if css[k] == "\\" else 1
            elif c == "{": depth += 1
            elif c == "}": depth -= 1
            k += 1
        out.append((prelude, css[j + 1:k - 1]))
        i = k
    return out


def _split_selectors(prelude):
    parts, depth, cur = [], 0, ""
    for c in prelude:
        if c == "(": depth += 1
        elif c == ")": depth -= 1
        if c == "," and depth == 0:
            parts.append(cur); cur = ""
        else:
            cur += c
    return [p.strip() for p in parts + [cur] if p.strip()]


_FUNC = re.compile(r":(?:not|is|where|has)\((?:[^()]|\([^()]*\))*\)")


def _may_match(selector, words):
    s = _FUNC.sub("", selector)  # :not(.x) etc. never make a selector need .x
    s = re.sub(r"\[([\w-]+)[^\]]*\]", lambda m: " [" + m.group(1) + "] ", s)  # attribute values don't matter
    s = re.sub(r"::?[\w-]+(\([^)]*\))?", "", s)  # pseudo-classes / elements
    need = re.findall(r"[.#](-?[_a-zA-Z][\w-]*)", s) + re.findall(r"\[([\w-]+)\]", s)
    return all(w in words for w in need)


def _minify(css):
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


def prune(css, words):
    out = []
    for prelude, body in _blocks(css):
        if body is None:
            out.append(prelude + ";")
        elif prelude.startswith("@"):
            name = prelude.split()[0].lower()
            if name in ("@media", "@supports", "@container", "@layer"):
                inner = prune(body, words)
                if inner: out.append(prelude + "{" + inner + "}")
            else:  # @font-face, @keyframes, @property, @page: keep as written
                out.append(prelude + "{" + body.strip() + "}")
        else:
            sels = [s for s in _split_selectors(prelude) if _may_match(s, words)]
            if sels: out.append(",".join(sels) + "{" + body.strip() + "}")
    return "".join(out)


# ------------------------------------------------------------------ icons
def icon_map(site):
    css = open(os.path.join(site, ICON_CSS), encoding="utf-8").read()
    return dict(re.findall(r'\.bi-([\w-]+)::before\{content:"\\([0-9a-f]+)"\}', css))


def icon_css(site, names):
    """@font-face + base rule + one rule per icon used on the page (paths relative to the site root)."""
    css = open(os.path.join(site, ICON_CSS), encoding="utf-8").read()
    base = re.search(r'\.bi::before,\[class\*=" bi-"\]::before,\[class\^=bi-\]::before\{[^}]*\}', css).group(0)
    face = ('@font-face{font-display:block;font-family:bootstrap-icons;'
            'src:url("{R}' + ICON_SUBSET + '") format("woff2")}')
    m = icon_map(site)
    return face + base + "".join(f'.bi-{n}::before{{content:"\\{m[n]}"}}' for n in sorted(names) if n in m)


def icons_used(text, site):
    m = icon_map(site)
    return {n for n in re.findall(r"\bbi-([\w-]+)", text) if n in m}


def build_icon_font(site, names):
    """WOFF2 with only the given icons (about 4 KB instead of 130 KB). Needs: pip install fonttools brotli"""
    import logging
    from fontTools import subset
    logging.getLogger("fontTools").setLevel(logging.ERROR)  # the upstream font has a harmless post-table quirk
    m = icon_map(site)
    opts = subset.Options(); opts.flavor = "woff2"; opts.layout_features = []; opts.name_IDs = ["*"]; opts.notdef_outline = True
    font = subset.load_font(os.path.join(site, ICON_FONT), opts)
    s = subset.Subsetter(opts); s.populate(unicodes=[int(m[n], 16) for n in names]); s.subset(font)
    dst = os.path.join(site, ICON_SUBSET)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subset.save_font(font, dst, opts)


# ------------------------------------------------------------------ per page
class Critical:
    def __init__(self, site):
        self.site = site
        self.sheets = [_strip_comments(open(os.path.join(site, p), encoding="utf-8").read()) for p in SHEETS]
        self.js = " ".join(open(os.path.join(site, p), encoding="utf-8").read() for p in JS)
        self.js_words = set(re.findall(r"[\w-]+", self.js))

    def css(self, html, R):
        words = set(re.findall(r"[\w-]+", html)) | self.js_words
        bootstrap, style = (prune(s, words) for s in self.sheets)
        icons = icon_css(self.site, icons_used(html + self.js, self.site))
        css = _minify(bootstrap + icons + style)
        # style.css is in assets/css/: its url(../fonts/...) become paths from the page
        return css.replace("url(../fonts/", "url(" + R + "assets/fonts/").replace("{R}", R)
