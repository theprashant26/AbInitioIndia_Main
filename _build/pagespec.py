"""Theme-independent page list: paths, titles, descriptions and breadcrumbs.
Each skin module renders the bodies in its own design language."""
import html
from site_data import *  # noqa

SUFFIX = " | Ab Initio India"


def pages(ctx, S):
    posts, img = ctx["posts"], ctx["img"]
    out = []
    add = lambda **k: out.append(k)

    add(path="about.html", title="About Us" + SUFFIX,
        desc="Ab Initio India LLP is a global business consulting firm in New Delhi focused on business strategy, fund raising, corporate finance, mergers & acquisitions and regulatory advisory.",
        og_image="assets/img/" + img("pages/about")[0].split("assets/img/")[1], body=S.about(ctx, ""))
    add(path="team.html", title="Our Team" + SUFFIX,
        desc="Meet the Ab Initio India team: partners and associates with expertise in corporate advisory, secretarial compliance, litigation and regulatory affairs.",
        body=S.team(ctx, ""))
    add(path="mentors.html", title="Our Mentors" + SUFFIX,
        desc="The mentors who guide Ab Initio India, with decades of experience in corporate finance, government, telecom, company secretarial practice and dispute resolution.",
        body=S.mentors(ctx, ""))
    add(path="services.html", title="Our Services" + SUFFIX,
        desc="Business advocacy, strategic, transaction, structure and regulatory advisory, mergers & acquisitions, India entry strategy and capital market services from Ab Initio India.",
        body=S.services(ctx, ""))
    for s in SERVICES:
        add(path=f"services/{s['slug']}.html", nav="services/", title=html.unescape(s["title"]) + SUFFIX,
            desc=html.unescape(s["meta"]), og_image="assets/img/" + img("services/" + s["slug"])[0].split("assets/img/")[1],
            body=S.service(ctx, "../", s))
    add(path="insights.html", title="Insights" + SUFFIX,
        desc="Articles, regulatory updates and case studies from Ab Initio India on corporate law, FSSAI, capital markets, real estate, insolvency and doing business in India and Dubai.",
        body=S.insights(ctx, ""))
    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        add(path=f"insights/{p['slug']}.html", nav="insights/", title=p["title"] + SUFFIX, desc=p["desc"], og_type="article", post=p,
            og_image="assets/img/" + img(p["img_key"])[0].split("assets/img/")[1],
            body=S.article(ctx, "../", p, newer, older))
    add(path="contact.html", title="Contact Us" + SUFFIX,
        desc="Contact Ab Initio India LLP, Indraprakash Building, 21 Barakhamba Road, New Delhi. Call +91-11-40393888, email mail@abinitioindia.com or send us an enquiry.",
        body=S.contact(ctx, ""))
    add(path="faq.html", title="Frequently Asked Questions" + SUFFIX,
        desc="Answers to common questions about Ab Initio India's business advisory process, pricing, setting up a business in India, funding support and article submissions.",
        body=S.faq(ctx, ""))
    for slug, title, _, desc in LEGAL:
        add(path=f"{slug}.html", title=title + SUFFIX, desc=desc, body=S.legal(ctx, "", slug, title))
    # the server shows 404.html at any missing URL (e.g. /insights/a/b/), so its links are root-relative
    add(path="404.html", title="Page not found" + SUFFIX, desc="The page you are looking for could not be found.", noindex=True,
        root="/", body=S.not_found(ctx, "/"))
    add(path="thank-you.html", title="Thank you" + SUFFIX, desc="Thank you for contacting Ab Initio India. Our team will get back to you shortly.", noindex=True,
        body=S.thanks(ctx, ""))
    return out
