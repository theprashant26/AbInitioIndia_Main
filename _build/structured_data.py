"""JSON-LD structured data (schema.org): the firm as a ProfessionalService on the home, about and contact
pages, and an Article on every insight. Built from site_data.py, so it always matches the visible content."""
import json, re, html
from site_data import *  # noqa

# Head office as shown on the contact page and in the footer. The asserts stop the build if that text
# changes without this block being updated.
_OFFICE = CONTACT["offices"][0][1]
ADDRESS = {"@type": "PostalAddress", "streetAddress": "1011B, 10th Floor, Indraprakash Building, 21 Barakhamba Road",
           "addressLocality": "New Delhi", "addressRegion": "Delhi", "postalCode": "110001", "addressCountry": "IN"}
assert "1011B, 10th Floor, Indraprakash Building" in _OFFICE and "21 Barakhamba Road" in _OFFICE and "110001" in _OFFICE, _OFFICE
assert CONTACT["hours"] == ("9:00 AM to 6:00 PM", "Monday to Saturday"), CONTACT["hours"]
HOURS = [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          "opens": "09:00", "closes": "18:00"}]


def _script(data):
    # "</" would end the <script> element early
    return '\n<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def organization(base, desc):
    return _script({
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": base + "#organization",
        "name": "Ab Initio India LLP", "alternateName": "Ab Initio India", "url": base,
        "logo": base + "assets/img/logo.png", "image": base + "assets/img/logo.png", "description": desc,
        "telephone": PHONE_TEL, "email": EMAIL, "address": ADDRESS, "openingHoursSpecification": HOURS,
        "sameAs": [u for u, _, _ in SOCIAL],
    })


def article(base, page, p):
    org = {"@type": "Organization", "name": "Ab Initio India LLP", "url": base}
    return _script({
        "@context": "https://schema.org", "@type": "Article",
        "headline": html.unescape(re.sub(r"<[^>]+>", "", p["title"])),
        "datePublished": p["date"], "dateModified": p.get("modified", p["date"]),
        "image": [base + page["og_image"]], "mainEntityOfPage": base + page["path"],
        "articleSection": p["cat"], "inLanguage": "en-IN",
        "author": org, "publisher": {**org, "logo": {"@type": "ImageObject", "url": base + "assets/img/logo.png"}},
    })
