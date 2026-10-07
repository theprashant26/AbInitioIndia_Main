"""Theme B – "Aurora Brand Glass": airy aurora mesh in logo blue + sunflower, white frosted panels, navy type."""
import html
from site_data import *  # noqa
import common as c
from common import e, AC

THEME_COLOR = "#eaf2fb"


def backdrop(R, page):
    return '<div class="aurora" aria-hidden="true"><span class="orb o1"></span><span class="orb o2"></span><span class="orb o3"></span><span class="orb o4"></span></div>'


def header(R, current):
    return c.header(R, current, "Book a consultation", "btn-sun", "hdr-b")


def footer(R):
    return c.footer(R, "btn-blue", "glass-strong")


# ------------------------------------------------------------------ components
def banner(R, title, crumbs, lead=None, icon=None, meta=None, small=False):
    ic = f'<span class="banner-icon anim" aria-hidden="true"><i class="bi {icon}"></i></span>' if icon else ""
    lead = f'<p class="lead anim">{lead}</p>' if lead else ""
    meta = f'<div class="banner-meta anim">{meta}</div>' if meta else ""
    return f"""<section class="banner"><div class="container-xl"><div class="banner-panel glass{' is-small' if small else ''}">
{c.crumbs(R, crumbs, title, "crumbs anim")}
<div class="banner-row">{ic}<div>{meta}<h1 class="anim">{title}</h1>{lead}</div></div>
</div></div></section>"""


def head(kicker, title, sub=None, center=False, h="h2"):
    sub = f"<p>{sub}</p>" if sub else ""
    return f'<div class="sec-head{" text-center mx-auto" if center else ""}" data-reveal><span class="kicker">{kicker}</span><{h}>{title}</{h}>{sub}</div>'


def quote_card(key, cls=""):
    q, who, role = TESTIMONIALS[key]
    return f'<figure class="quote-card glass {cls}"><i class="bi bi-quote" aria-hidden="true"></i><blockquote>{q}</blockquote><figcaption><strong>{who}</strong>{role}</figcaption></figure>'


def bento(ctx, R):
    spans = {0: "b-wide b-img", 4: "b-wide", 6: "b-wide", 7: "b-wide b-img"}
    out = []
    for i, s in enumerate(SERVICES):
        cls = spans.get(i, "")
        bg = ""
        if "b-img" in cls:
            bg = ctx["img"].thumb_tag("services/" + s["slug"], R, "", "bento-bg", 800)
        out.append(f'<a class="bento-card glass {cls}" href="{R}services/{s["slug"]}.html" data-tilt>{bg}<span class="bento-ico"><i class="bi {s["icon"]}" aria-hidden="true"></i></span>'
                   f'<span class="bento-txt"><strong>{s["card_title"]}</strong><span>{s["blurb"]}</span></span><span class="bento-go" aria-hidden="true"><i class="bi bi-arrow-up-right"></i></span></a>')
    return f'<div class="bento">{"".join(out)}</div>'


def process(R):
    steps = "".join(f'<li class="step glass"><span class="step-no">{i:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(PROCESS, 1))
    return f"""<section class="sec process" aria-labelledby="how-h" data-carousel><div class="container-xl">
<div class="process-head" data-reveal><div><span class="kicker">How we work</span><h2 id="how-h">A systematic approach, shaped around your business</h2><p>{PROCESS_INTRO}</p></div>
<div class="carousel-btns"><button class="round-btn" type="button" data-prev aria-controls="processTrack"><span class="visually-hidden">Previous steps</span><i class="bi bi-arrow-left" aria-hidden="true"></i></button><button class="round-btn" type="button" data-next aria-controls="processTrack"><span class="visually-hidden">Next steps</span><i class="bi bi-arrow-right" aria-hidden="true"></i></button></div></div>
<ol class="timeline" id="processTrack" data-track tabindex="0" aria-label="Advisory process steps">{steps}</ol>
</div></section>"""


CARD_SIZES = "(min-width: 1400px) 410px, (min-width: 992px) 31vw, (min-width: 768px) 46vw, 88vw"
FIGURE_SIZES = "(min-width: 1400px) 760px, (min-width: 992px) 66vw, (min-width: 576px) 85vw, 76vw"
HIGH = ' fetchpriority="high"'  # the page's main (LCP) image


def ins_card(ctx, R, p, h="h3", eager=False, high=False):
    ctx["img"](p["img_key"], R)
    url = f'{R}insights/{p["slug"]}.html'
    cats = "|".join(p["cats"])
    thumb = ctx["img"].srcset_tag(p["img_key"], R, "", (400, 640), CARD_SIZES, eager=eager, extra=HIGH if high else "")
    return (f'<article class="ins-card" data-cats="{e(cats)}"><a class="ins-media" href="{url}" tabindex="-1" aria-hidden="true">{thumb}</a>'
            f'<div class="ins-body"><p class="ins-meta"><span class="tag">{p["cat"]}</span><time datetime="{p["date"]}">{ctx["fmt_date"](p["date"])}</time></p>'
            f'<{h}><a href="{url}">{e(p["title"])}</a></{h}></div></article>')


def side_cta(R):
    return f"""<div class="side-cta glass-sun"><h2>Book a consultation</h2><p>Tell us what you need and our team will get back to you.</p>
<a class="btn btn-blue" href="{R}contact.html">Contact Us</a><a class="side-tel" href="tel:{PHONE_TEL}"><i class="bi bi-telephone" aria-hidden="true"></i> {PHONE_DISPLAY}</a></div>"""


# ------------------------------------------------------------------ home
def home(ctx, R):
    posts = ctx["posts"]
    q, who, role = TESTIMONIALS["dinesh"]
    pillars = "".join(f'<div class="col-sm-6"><div class="pillar glass-on-blue"><i class="bi {ic}" aria-hidden="true"></i><h3>{t}</h3><p>{d}</p></div></div>' for t, d, ic in PILLARS)
    stats = "".join(f'<li><strong>{n}</strong><span>{t}</span></li>' for n, t in ABOUT["stats"])
    return f"""<section class="hero"><div class="container-xl"><div class="row g-5 align-items-center">
<div class="col-lg-6 hero-copy">
<span class="chip glass-strong anim"><i class="bi bi-geo-alt-fill" aria-hidden="true"></i> {HOME["kicker"]}</span>
<h1 class="anim">True partners to your <span class="grad">success</span></h1>
<p class="lead anim">{HOME["lead_b"]}</p>
<div class="hero-ctas anim"><a class="btn btn-blue btn-lg" href="{R}services.html">Explore services <i class="bi bi-arrow-right" aria-hidden="true"></i></a><a class="btn btn-glass btn-lg" href="{R}contact.html">Talk to an advisor</a></div>
</div>
<div class="col-lg-6"><div class="hero-visual">
<figure class="hv-photo glass anim" data-parallax="4">{ctx["img"].srcset_tag("stock/meeting", R, "Advisors in a meeting around a conference table", (480, 760, 1100), "(min-width: 992px) 560px, 92vw", eager=True, extra=' fetchpriority="high"')}</figure>
<figure class="hv-quote glass-strong anim" data-parallax="10"><i class="bi bi-quote" aria-hidden="true"></i><blockquote>My experience with Ab Initio has been phenomenal so far.</blockquote><figcaption><strong>{who}</strong>Legal Head, Radico Khaitan Limited</figcaption></figure></div></div>
</div></div></section>

<section class="clients" aria-label="Clients"><div class="container-xl"><div class="clients-band glass" data-reveal>
<p>Trusted by leading brands across India</p><ul class="logo-row">{c.clients(R)}</ul></div></div></section>

<section class="sec" aria-labelledby="svc-h"><div class="container-xl">
<div class="split-head" data-reveal><div><span class="kicker">Our Services</span><h2 id="svc-h">{HOME["svc_h"]}</h2></div><p>{HOME["svc_p"]} <a class="link-arrow" href="{R}services.html">All services <i class="bi bi-arrow-right" aria-hidden="true"></i></a></p></div>
{bento(ctx, R)}
</div></section>

{process(R)}

<section class="sec pt-0" aria-labelledby="why-h"><div class="container-xl"><div class="blue-panel" data-reveal>
<div class="row g-4 g-lg-5 align-items-center">
<div class="col-lg-5"><span class="kicker kicker-sun">Why Ab Initio</span><h2 id="why-h">{HOME["why_h"]}</h2><p>{HOME["why_p"]}</p>
<ul class="stat-chips">{stats}</ul>
<a class="btn btn-sun" href="{R}about.html">About Ab Initio</a></div>
<div class="col-lg-7"><div class="row g-3">{pillars}</div></div>
</div></div></div></section>

<section class="sec pt-0" aria-labelledby="ins-h"><div class="container-xl">
<div class="split-head" data-reveal><div><span class="kicker">Insights</span><h2 id="ins-h">Latest insights</h2></div><p><a class="btn btn-glass" href="{R}insights.html">View all insights</a></p></div>
<div class="ins-grid">{"".join(ins_card(ctx, R, p) for p in posts[:3])}</div>
</div></section>"""


# ------------------------------------------------------------------ inner pages
def about(ctx, R):
    A = ABOUT; img = ctx["img"]
    stats = "".join(f'<li><strong>{n}</strong><span>{t}</span></li>' for n, t in A["stats"])
    deals = "".join(f'<li class="deal"><span class="deal-no">{i:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(A["deals"], 1))
    tags = "".join(f'<li>{t}</li>' for t in A["deals_tags"])
    quotes = "".join(quote_card(k) for k in A["testimonials"])
    return f"""{banner(R, "About Us", [], A["kicker"])}
<section class="sec pt-4"><div class="container-xl"><div class="row g-4 g-lg-5 align-items-center">
<div class="col-lg-6" data-reveal><span class="kicker">Who we are</span><h2>{A["intro_h"]}</h2><p class="lead-sm">{A["intro"]}</p>{quote_card("dinesh", "mt-4")}</div>
<div class="col-lg-6" data-reveal><figure class="frame glass">{img.tag("pages/about", R, "Workspace with a laptop and business magazines")}</figure></div>
</div></div></section>
<section class="sec pt-0"><div class="container-xl"><div class="blue-panel" data-reveal><div class="row g-4 g-lg-5">
<div class="col-lg-5"><span class="kicker kicker-sun">{A["what_kicker"]}</span><h2 class="h-statement">{A["what_h"]}</h2></div>
<div class="col-lg-7"><blockquote class="pull">“{A["results_quote"]}”</blockquote><h3>{A["results_h"]}</h3>{"".join(f"<p>{p}</p>" for p in A["results"])}</div>
</div><ul class="stat-row">{stats}</ul></div></div></section>
<section class="sec pt-0"><div class="container-xl"><div class="row g-4 g-lg-5">
<div class="col-lg-5" data-reveal><span class="kicker">{A["philosophy_kicker"]}</span><h2>{A["philosophy_h"]}</h2>{"".join(f"<p>{p}</p>" for p in A["philosophy"])}</div>
<div class="col-lg-7"><div class="row g-4">
<div class="col-md-6" data-reveal><div class="mv glass-strong"><i class="bi bi-bullseye" aria-hidden="true"></i><h3>Mission</h3><p>{A["mission"]}</p></div></div>
<div class="col-md-6" data-reveal><div class="mv glass-strong"><i class="bi bi-eye" aria-hidden="true"></i><h3>Vision</h3><p>{A["vision"]}</p></div></div></div></div>
</div></div></section>
<section class="sec pt-0"><div class="container-xl">{head("Testimonials", "What they've said about us", "Trusted by some of the biggest names")}<div class="quote-grid">{quotes}</div></div></section>
<section class="sec pt-0"><div class="container-xl"><div class="split-head" data-reveal><div><span class="kicker">Track record</span><h2>{A["deals_h"]}</h2></div><ul class="tag-row">{tags}</ul></div>
<ol class="deals">{deals}</ol></div></section>"""


def team(ctx, R):
    img = ctx["img"]
    first, rest = TEAM[0], TEAM[1:]
    slug, name, role, tag, bio = first
    lead_card = f"""<article class="founder glass-strong" data-reveal><div class="founder-photo">{img.tag("team/" + slug, R, name)}</div>
<div class="founder-body"><span class="role-chip">{role}</span><h3>{name}</h3>{"".join(f"<p>{p}</p>" for p in bio)}</div></article>"""
    cards = []
    for slug, name, role, tag, bio in rest:
        tl = f'<p class="team-tag">{tag}</p>' if tag else ""
        cards.append(f'<article class="person" data-reveal><div class="person-photo">{img.tag("team/" + slug, R, name)}<span class="role-chip">{role}</span></div>'
                     f'<div class="person-body"><h3>{name}</h3>{tl}{"".join(f"<p>{p}</p>" for p in bio)}</div></article>')
    h, _ = TEAM_INTRO
    return f"""{banner(R, "Our Team", [("About Us", "about.html")], "Our team is comprised of genuinely gifted minds.")}
<section class="sec pt-4"><div class="container-xl">
{head("The people", h, "Our expertise across diverse practice areas and sectors covers varied and nuanced needs.")}
{lead_card}
<div class="people">{"".join(cards)}</div>
</div></section>"""


def mentors(ctx, R):
    img = ctx["img"]; rows = []
    for i, (slug, name, bio, extra) in enumerate(MENTORS):
        x = f'<p><strong>{extra[0]}</strong></p><ul>{"".join(f"<li>{li}</li>" for li in extra[1])}</ul>' if extra else ""
        rows.append(f'<article class="mentor glass-strong{" is-flip" if i % 2 else ""}" data-reveal><div class="mentor-photo">{img.tag("mentors/" + slug, R, name)}</div>'
                    f'<div class="mentor-body"><span class="role-chip">Mentor</span><h3>{name}</h3>{"".join(f"<p>{p}</p>" for p in bio)}{x}</div></article>')
    h, p = MENTORS_INTRO
    return f"""{banner(R, "Our Mentors", [("About Us", "about.html")], p)}
<section class="sec pt-4"><div class="container-xl">
{head("Mentors", h, "Our expertise across diverse practice areas and sectors covers varied and nuanced needs.")}
<div class="mentors">{"".join(rows)}</div>
</div></section>"""


def services(ctx, R):
    vals = "".join(f'<li><strong>{t}</strong><span>{d}</span></li>' for t, d in VALUES)
    return f"""{banner(R, "Our Services", [], "Our expertise across diverse practice areas and sectors covers varied and nuanced needs.")}
<section class="sec pt-4"><div class="container-xl">
<div class="split-head" data-reveal><div><span class="kicker">Practice areas</span><h2>All the solutions you need, under one roof</h2></div><p>Your requirements are manifold, and so is our experience.</p></div>
{bento(ctx, R)}
</div></section>
<section class="sec pt-0"><div class="container-xl"><div class="blue-panel" data-reveal>
<div class="row g-4 align-items-center"><div class="col-lg-4"><span class="kicker kicker-sun">We are known for</span><h2>Company values</h2></div>
<div class="col-lg-8"><ul class="values">{vals}</ul></div></div></div></div></section>
{process(R)}"""


def service(ctx, R, s):
    img = ctx["img"]
    intro_h = f'<h2 class="h-intro">{s["intro_h"]}</h2>' if s.get("intro_h") else ""
    lead = "".join(f'<p class="lead-sm">{p}</p>' for p in s["lead"])
    return f"""{banner(R, s["title"], [("Our Services", "services.html")], s["blurb"], icon=s["icon"])}
<section class="sec pt-4"><div class="container-xl"><div class="row g-4 g-lg-5">
<div class="col-lg-8"><div class="reading-card">
<figure class="reading-figure">{img.srcset_tag("services/" + s["slug"], R, html.unescape(s["title"]) + " – Ab Initio India", (480, 800, 1200), FIGURE_SIZES, eager=True, extra=HIGH)}</figure>
{intro_h}{lead}
<div class="prose">{s["body"]}</div>
</div>{quote_card(s["quote"], "mt-4")}</div>
<aside class="col-lg-4"><div class="side"><div class="side-card glass-strong"><h2>Our Services</h2><ul class="side-nav">{c.services_nav(R, s)}</ul></div>{side_cta(R)}</div></aside>
</div></div></section>"""


def insights(ctx, R):
    posts = ctx["posts"]
    cats = []
    for p in posts:
        for cat in p["cats"]:
            if cat not in cats: cats.append(cat)
    counts = {cat: sum(cat in p["cats"] for p in posts) for cat in cats}
    cats.sort(key=lambda x: -counts[x])
    btns = f'<button type="button" class="filter-btn" data-cat="all" data-label="all" aria-pressed="true">All <span>{len(posts)}</span></button>' + "".join(
        f'<button type="button" class="filter-btn" data-cat="{e(cat)}" data-label="{e(cat)}" aria-pressed="false">{cat} <span>{counts[cat]}</span></button>' for cat in cats)
    return f"""{banner(R, "Insights", [], "Articles, regulatory updates and case studies from the Ab Initio India team.")}
<section class="sec pt-4"><div class="container-xl">
<div class="filter-bar glass" data-filter="#insGrid" role="group" aria-label="Filter articles by category">{btns}</div>
<p class="filter-status" data-filter-status aria-live="polite">{len(posts)} articles</p>
<div class="ins-grid" id="insGrid">{"".join(ins_card(ctx, R, p, "h2", eager=i == 0, high=i == 0) for i, p in enumerate(posts))}</div>
</div></section>"""


def article(ctx, R, p, newer, older):
    img = ctx["img"]
    body, featured_in_body = ctx["post_body"](p, R, img)
    fig = "" if featured_in_body else f'<figure class="art-figure">{img.srcset_tag(p["img_key"], R, p["title"], (480, 800, 1200), FIGURE_SIZES, eager=True, extra=HIGH)}</figure>'
    meta = "".join(f'<span class="tag">{x}</span>' for x in p["cats"]) + f'<time datetime="{p["date"]}">{ctx["fmt_date"](p["date"])}</time>'
    return f"""{banner(R, e(p["title"]), [("Insights", "insights.html")], meta=meta, small=True)}
<section class="sec pt-4"><div class="container-xl"><article class="reading-card article">
{fig}<div class="prose">{body}</div>
{c.post_nav(R, newer, older)}
</article></div></section>
<section class="sec pt-0"><div class="container-xl">
<div class="split-head" data-reveal><div><span class="kicker">Keep reading</span><h2>Related insights</h2></div><p><a class="btn btn-glass" href="{R}insights.html">All insights</a></p></div>
<div class="ins-grid">{"".join(ins_card(ctx, R, x) for x in c.related(ctx["posts"], p))}</div>
</div></section>"""


def contact(ctx, R):
    C = CONTACT
    offices = "".join(f'<li><i class="bi bi-geo-alt" aria-hidden="true"></i><span><strong>{n}</strong>{a}</span></li>' for n, a in C["offices"])
    phones = "".join(f'<li><i class="bi bi-telephone" aria-hidden="true"></i><span><strong>{l}</strong><a href="tel:{t}">{d}</a></span></li>' for l, d, t in C["phones"])
    return f"""{banner(R, "Contact Us", [], C["lead"])}
<section class="sec pt-4"><div class="container-xl"><div class="row g-4">
<div class="col-lg-5"><div class="info-panel glass-strong" data-reveal><h2>Visit our office or simply send us an email</h2><p>{C["intro"]}</p>
<ul class="info-list">{offices}{phones}
<li><i class="bi bi-envelope" aria-hidden="true"></i><span><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
<li><i class="bi bi-whatsapp" aria-hidden="true"></i><span><strong>WhatsApp</strong><a href="{WHATSAPP}" target="_blank" rel="noopener">+91 8800 808 022</a></span></li>
<li><i class="bi bi-clock" aria-hidden="true"></i><span><strong>Available</strong>{C["hours"][0]}, {C["hours"][1]}</span></li></ul></div></div>
<div class="col-lg-7"><div class="form-panel glass-strong" data-reveal><span class="kicker">Enquiry</span><h2>Send us an enquiry</h2><p>For any questions, please feel free to contact us.</p>{c.form(ctx, "btn-blue")}</div></div>
</div>
<div class="map-frame glass" data-reveal><iframe src="{C["map"]}" title="Map: Indraprakash Building, 21 Barakhamba Road, New Delhi" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>"""


def faq(ctx, R):
    return f"""{banner(R, "Frequently asked questions", [], "Answers to the questions we are asked most often.")}
<section class="sec pt-4"><div class="container-xl"><div class="row g-4 g-lg-5">
<div class="col-lg-8">{c.accordion(R, FAQ, "faq")}</div>
<aside class="col-lg-4"><div class="side">{side_cta(R)}<div class="side-card glass-strong"><h2>Explore</h2><ul class="side-nav"><li><a href="{R}services.html"><i class="bi bi-grid" aria-hidden="true"></i>Our Services</a></li><li><a href="{R}about.html"><i class="bi bi-info-circle" aria-hidden="true"></i>About Us</a></li><li><a href="{R}insights.html"><i class="bi bi-journal-text" aria-hidden="true"></i>Insights</a></li></ul></div></div></aside>
</div></div></section>"""


def legal(ctx, R, slug, title):
    return f"""{banner(R, title, [])}
<section class="sec pt-4"><div class="container-xl"><div class="row g-4 g-lg-5">
<div class="col-lg-8"><div class="reading-card"><div class="prose">{ctx["legal"][slug]}</div></div></div>
<aside class="col-lg-4"><div class="side"><div class="side-card glass-strong"><h2>Legal</h2><ul class="side-nav plain">{c.legal_nav(R, slug)}</ul></div>{side_cta(R)}</div></aside>
</div></div></section>"""


def _center(R, chip, title, lead, buttons):
    return f"""<section class="center-sec"><div class="container-xl"><div class="center-panel glass-strong">
<span class="chip glass anim">{chip}</span><h1 class="anim">{title}</h1><p class="lead anim">{lead}</p>
<div class="hero-ctas justify-content-center anim">{buttons}</div></div></div></section>"""


def not_found(ctx, R):
    return _center(R, "Error 404", "Page not found", "Sorry, the page you are looking for does not exist or has been moved.",
                   f'<a class="btn btn-blue" href="{R}index.html">Back to home</a><a class="btn btn-glass" href="{R}services.html">Our Services</a><a class="btn btn-glass" href="{R}contact.html">Contact Us</a>')


def thanks(ctx, R):
    return _center(R, '<i class="bi bi-check-circle-fill" aria-hidden="true"></i> Enquiry sent', "Thank you", "Your message has reached us. Our team will get back to you shortly.",
                   f'<a class="btn btn-blue" href="{R}index.html">Back to home</a><a class="btn btn-glass" href="{R}insights.html">Read our insights</a>')
