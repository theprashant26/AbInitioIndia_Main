"""Markup helpers shared by the three glass skins. Visual styling lives in each theme's style.css;
these helpers only emit semantic, accessible structure with the class names a skin passes in."""
import html
from site_data import *  # noqa

e = lambda s: html.escape(s, quote=True)
AC = ' aria-current="page"'
EXT = ' target="_blank" rel="noopener"'  # links that leave the site (WhatsApp, social) open in a new tab
NEW_TAB = '<span class="visually-hidden"> (opens in a new tab)</span><i class="bi bi-box-arrow-up-right ext-ico" aria-hidden="true"></i>'
NAV = [("About us", [("About", "about.html"), ("Our team", "team.html"), ("Our mentors", "mentors.html")]),
       ("Our services", "services.html"), ("Insights", "insights.html"), ("Contact us", "contact.html")]
ABOUT_GROUP = ("about.html", "team.html", "mentors.html")


def section_of(current):
    return current.split("/")[0] if "/" in current else None


def header(R, current, cta_label, cta_cls, variant=""):
    """Sticky glass header + desktop dropdown + full-screen glass mobile menu."""
    sec = section_of(current)
    items, mitems = [], []
    for label, target in NAV:
        if isinstance(target, list):
            on = current in ABOUT_GROUP
            sub = "".join(f'<li><a class="dropdown-item{" active" if h == current else ""}" href="{R}{h}"{AC if h == current else ""}>{t}</a></li>' for t, h in target)
            items.append(f'<li class="nav-item dropdown"><a class="nav-link dropdown-toggle{" active" if on else ""}" href="{R}about.html" role="button" data-bs-toggle="dropdown" aria-expanded="false">{label}</a>'
                         f'<ul class="dropdown-menu glass-menu">{sub}</ul></li>')
            mitems += [(t, h) for t, h in target]
        else:
            on = target == current or (sec and target == f"{sec}.html")
            exact = target == current
            items.append(f'<li class="nav-item"><a class="nav-link{" active" if on else ""}" href="{R}{target}"{AC if exact else ""}>{label}</a></li>')
            mitems.append((label, target))
    legal_label, legal_url = LEGAL_SITE
    items.append(f'<li class="nav-item"><a class="nav-link nav-ext" href="{legal_url}"{EXT}>{legal_label}{NEW_TAB}</a></li>')
    mlinks = "".join(f'<li><a href="{R}{h}"{AC if h == current else ""}>{t}</a></li>' for t, h in mitems)
    mlinks += f'<li><a href="{legal_url}"{EXT}>{legal_label}{NEW_TAB}</a></li>'
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header {variant}" data-header>
<div class="container-xl"><nav class="nav-bar" aria-label="Main">
<a class="brand" href="{R}index.html"><img src="{R}assets/img/logo.webp" alt="Ab Initio India – Legal, Regulatory, Strategy" width="513" height="184"></a>
<ul class="nav-links">{"".join(items)}</ul>
<a class="btn {cta_cls} nav-cta" href="{R}contact.html">{cta_label}</a>
<button class="menu-btn" type="button" data-menu-open aria-expanded="false" aria-controls="mobileMenu"><span class="visually-hidden">Open menu</span><i class="bi bi-list" aria-hidden="true"></i></button>
</nav></div>
</header>
<div class="mobile-menu" id="mobileMenu" role="dialog" aria-modal="true" aria-label="Menu" hidden>
<div class="mobile-menu-top"><a class="brand" href="{R}index.html"><img src="{R}assets/img/logo.webp" alt="Ab Initio India – home" width="513" height="184"></a>
<button class="menu-close" type="button" data-menu-close><span class="visually-hidden">Close menu</span><i class="bi bi-x-lg" aria-hidden="true"></i></button></div>
<ul class="mobile-links">{mlinks}</ul>
<div class="mobile-menu-foot"><a class="btn {cta_cls}" href="{R}contact.html">{cta_label}</a><a href="tel:{PHONE_TEL}"><i class="bi bi-telephone" aria-hidden="true"></i> {PHONE_DISPLAY}</a><a href="mailto:{EMAIL}"><i class="bi bi-envelope" aria-hidden="true"></i> {EMAIL}</a></div>
</div>"""


def footer(R, cta_btn_cls, cta_panel_cls="glass-strong", extra_cls=""):
    social = "".join(f'<a href="{u}" aria-label="{n}"{EXT}><i class="bi {i}" aria-hidden="true"></i></a>' for u, n, i in SOCIAL)
    legal = "".join(f'<li><a href="{R}{s}.html">{t}</a></li>' for s, _, t, _ in LEGAL)
    return f"""<footer class="site-footer {extra_cls}">
<div class="container-xl">
<div class="footer-cta {cta_panel_cls}" data-reveal>
<div><p class="footer-cta-kicker">Ab Initio India LLP</p><h2>Let's grow your business together</h2></div>
<div class="footer-cta-actions"><a class="btn {cta_btn_cls}" href="{R}contact.html">Reach out now</a><a class="footer-cta-tel" href="tel:{PHONE_TEL}"><i class="bi bi-telephone" aria-hidden="true"></i> {PHONE_DISPLAY}</a></div>
</div>
</div>
<div class="footer-main"><div class="container-xl">
<div class="footer-grid">
<div class="footer-brand"><a class="brand" href="{R}index.html"><img src="{R}assets/img/logo.webp" alt="Ab Initio India" width="513" height="184" loading="lazy"></a>
<p>1011B, 10th Floor, Indraprakash Building,<br>21 Barakhamba Road, New Delhi – 110001</p></div>
<div><h2 class="footer-h">Contact</h2><ul><li><a href="tel:{PHONE_TEL}"><i class="bi bi-telephone" aria-hidden="true"></i> {PHONE_DISPLAY}</a></li><li><a href="mailto:{EMAIL}"><i class="bi bi-envelope" aria-hidden="true"></i> {EMAIL}</a></li><li><a href="{WHATSAPP}"{EXT}><i class="bi bi-whatsapp" aria-hidden="true"></i> WhatsApp</a></li></ul></div>
<div><h2 class="footer-h">Company</h2><ul><li><a href="{R}about.html">About</a></li><li><a href="{R}team.html">Our team</a></li><li><a href="{R}services.html">Services</a></li><li><a href="{R}insights.html">Insights</a></li><li><a href="{R}faq.html">FAQ</a></li><li><a href="{LEGAL_SITE[1]}"{EXT}>{LEGAL_SITE[0]}{NEW_TAB}</a></li></ul></div>
<div><h2 class="footer-h">Legal</h2><ul>{legal}</ul></div>
</div>
<div class="footer-bottom"><span>© 2026 Ab Initio India LLP. All rights reserved.</span><span class="social">{social}</span></div>
</div></div></footer>
<aside aria-label="WhatsApp"><a class="wa-float" href="{WHATSAPP}"{EXT} aria-label="Chat on WhatsApp"><i class="bi bi-whatsapp" aria-hidden="true"></i></a></aside>"""


def crumbs(R, items, title, cls="crumbs"):
    lis = "".join(f'<li><a href="{R}{h}">{t}</a></li>' for t, h in items)
    return f'<nav class="{cls}" aria-label="Breadcrumb"><ol><li><a href="{R}index.html">Home</a></li>{lis}<li aria-current="page">{title}</li></ol></nav>'


def form(ctx, btn_cls, pre="cf"):
    base = ctx["base"]
    req = '<span aria-hidden="true">*</span>'
    def f(key, col, label, inp):
        return f'<div class="{col}"><label class="form-label" for="{pre}-{key}">{label}</label>{inp}</div>'
    return f"""<form class="enquiry-form" action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="New enquiry from the Ab Initio India website">
<input type="hidden" name="_next" value="{base}thank-you.html">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" class="d-none" tabindex="-1" autocomplete="off">
<div class="row g-3">
{f("name", "col-md-6", f"Full name {req}", f'<input class="form-control" id="{pre}-name" name="name" type="text" autocomplete="name" required>')}
{f("email", "col-md-6", f"Email {req}", f'<input class="form-control" id="{pre}-email" name="email" type="email" autocomplete="email" required>')}
{f("phone", "col-md-6", "Phone", f'<input class="form-control" id="{pre}-phone" name="phone" type="tel" autocomplete="tel">')}
{f("subject", "col-md-6", f"Subject {req}", f'<input class="form-control" id="{pre}-subject" name="subject" type="text" required>')}
{f("message", "col-12", f"Message {req}", f'<textarea class="form-control" id="{pre}-message" name="message" rows="5" required></textarea>')}
<div class="col-12 form-actions"><button class="btn {btn_cls}" type="submit">Send enquiry <i class="bi bi-arrow-right" aria-hidden="true"></i></button><span class="form-note">Fields marked * are required.</span></div>
</div></form>"""


def accordion(R, items, cls, first_open=True, heading="h2"):
    out = []
    for i, (q, a) in enumerate(items, 1):
        op = first_open and i == 1
        out.append(f"""<div class="accordion-item"><{heading} class="accordion-header"><button class="accordion-button{'' if op else ' collapsed'}" type="button" data-bs-toggle="collapse" data-bs-target="#faq{i}" aria-expanded="{'true' if op else 'false'}" aria-controls="faq{i}">{q}</button></{heading}>
<div id="faq{i}" class="accordion-collapse collapse{' show' if op else ''}" data-bs-parent="#faqList"><div class="accordion-body prose">{a.replace("{R}", R)}</div></div></div>""")
    return f'<div class="accordion {cls}" id="faqList">{"".join(out)}</div>'


def related(posts, p, n=3):
    rel = [x for x in posts if x is not p and x["cat"] == p["cat"]][:n]
    if len(rel) < n:
        rel += [x for x in posts if x is not p and x not in rel][:n - len(rel)]
    return rel


def post_nav(R, newer, older, cls="post-nav"):
    out = []
    if older:
        out.append(f'<a class="pn-prev" href="{R}insights/{older["slug"]}.html"><span><i class="bi bi-arrow-left" aria-hidden="true"></i> Previous article</span>{e(older["title"])}</a>')
    if newer:
        out.append(f'<a class="pn-next" href="{R}insights/{newer["slug"]}.html"><span>Next article <i class="bi bi-arrow-right" aria-hidden="true"></i></span>{e(newer["title"])}</a>')
    return f'<nav class="{cls}" aria-label="More articles">{"".join(out)}</nav>'


def legal_nav(R, slug):
    return "".join(f'<li><a href="{R}{s}.html"{AC if s == slug else ""}>{t}</a></li>' for s, t, _, _ in LEGAL)


def services_nav(R, cur=None):
    return "".join(f'<li><a href="{R}services/{x["slug"]}.html"{AC if x is cur else ""}><i class="bi {x["icon"]}" aria-hidden="true"></i>{x["title"]}</a></li>' for x in SERVICES)


def clients(R, cls="logo-chip"):
    out = []
    for i, (f, n) in enumerate(CLIENTS, 1):
        fb = "png" if f.endswith(".png") else "jpg"
        out.append(f'<li class="{cls}"><picture><source srcset="{R}assets/img/clients/client-{i:02d}.webp" type="image/webp">'
                   f'<img src="{R}assets/img/clients/client-{i:02d}.{fb}" alt="{n}" width="150" height="60" loading="lazy"></picture></li>')
    return "".join(out)


def quote_parts(key):
    return TESTIMONIALS[key]


def plain(s):
    return html.unescape(s)


def summary(p, n=180):
    """Article summary without the title the WordPress meta description repeats."""
    d = p["desc"]
    t = p["title"]
    if d.lower().startswith(t.lower()):
        d = d[len(t):].lstrip(" -–:|")
    d = (d or p["excerpt"]).strip()
    if len(d) > n:
        return d[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    if not d.endswith((".", "!", "?", "…")):  # source text was cut mid-word
        d = d.rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return d
