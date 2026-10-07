# Ab Initio India – website

The new website for Ab Initio India LLP (abinitioindia.com), a business advisory firm in New Delhi.
The design is the client-approved **"Aurora Brand Glass"** theme (previously Theme B in the
AbInitioIndia_Themes repo): white pages, logo blue `#1552A1` and sunflower `#FACF00`,
Plus Jakarta Sans (self-hosted), frosted-glass cards.

Static HTML/CSS/JS with Bootstrap 5.3 (local, purged), Bootstrap Icons, GSAP + ScrollTrigger.
There is no server code. The enquiry form posts to FormSubmit.

## Folders

The repository root **is** the website: upload it to the web root as it is (`.htaccess` included).
`_build/` holds the generator; it is not part of the site, and `.htaccess` answers 404 for it,
`.git/` and this README in case they are uploaded too.

| Path | What it is |
|---|---|
| `index.html`, `about.html`, `team.html`, `mentors.html`, `services.html`, `insights.html`, `contact.html`, `faq.html` | Main pages |
| `services/*.html` | 8 service pages |
| `insights/*.html` | 38 articles (slugs match the old WordPress site) |
| privacy, disclaimer, terms, cookie, accessibility pages, `404.html`, `thank-you.html` | Legal and utility pages |
| `assets/css/style.css` | **Hand-written** stylesheet (the generator reads it, never writes it; see *Critical CSS*) |
| `assets/js/main.js` | **Generated**: copied from `_build/main_glass.js` on every build |
| `assets/fonts/` | Plus Jakarta Sans variable WOFF2 (latin + latin-ext), its licence (SIL OFL), icon-font subset |
| `assets/vendor/` | Bootstrap (purged subset + JS bundle), GSAP, ScrollTrigger |
| `assets/img/` | Images: team/, mentors/, services/, insights/, pages/, clients/, stock/, v/ (resized WebP variants) |
| `sitemap.xml`, `robots.txt` | **Generated** for https://abinitioindia.com/ (every indexable page; articles carry their date) |
| `.htaccess` | **Generated**: 301 redirects from the old WordPress URLs, `ErrorDocument 404`, compression, caching |

All `.html` files, `sitemap.xml`, `robots.txt` and `.htaccess` are build output: change the sources in
`_build/` and rebuild instead of editing them.

### _build/ (generator, not deployed)
| File | Purpose |
|---|---|
| `gen2.py` | Entry point. Renders every page into the project root |
| `skin_b_glass.py` | Page templates and layout (header, footer, every page type) |
| `common.py`, `pagespec.py`, `gen.py` | Shared helpers, the page list, content loading, image helpers, `BASE_URL` |
| `content/site_data.py` | **Text content**: company info, offices, phones, services, team, mentors, FAQ, testimonials, clients |
| `content/posts/*.json` | The 38 articles |
| `content/legal.json` | Legal page bodies |
| `content/img/` + `content/img-manifest.json` | Source images and their sizes |
| `stock/` | Licensed stock photo (credit in `stock/credits.json`) |
| `clients_src/` | Client logos (source files) |
| `main_glass.js` | Site JavaScript (menu, reveals, insights filter, form validation, parallax…) |
| `structured_data.py` | JSON-LD: ProfessionalService (home, about, contact) and Article (every insight), built from `site_data.py` |
| `brand.py` | Logo (`assets/img/logo.png`/`.webp`), favicons and `favicon.ico`, generated from `content/img/brand/logo-source.png` |
| `sitemap.py` | Writes `sitemap.xml` and `robots.txt` from the page list |
| `redirects.csv` | Old WordPress URL → new page (83 rows; `exact` or `prefix` match) |
| `redirects.py` | Writes `.htaccess` and `_build/nginx-redirects.conf` from `redirects.csv` |
| `critical.py` | Per-page inlined CSS and the icon-font subset (see *Critical CSS*) |
| `purge.py` | Rebuilds `assets/vendor/bootstrap.subset.min.css` from the classes the pages use |
| `vendor/` | Full Bootstrap CSS and Bootstrap Icons: sources for `purge.py` and the icon subset |

## Making changes

Needs Python 3.10+, Pillow and fontTools (`pip install pillow fonttools brotli`).

```bash
# 1. edit content (_build/content/…), templates (_build/skin_b_glass.py) or JS (_build/main_glass.js)
python _build/gen2.py              # 2. rebuild all pages
python _build/purge.py .           # 3. only if you used new Bootstrap classes, then rebuild again
```

* Styling: edit `assets/css/style.css`, then **rebuild**: every page inlines the CSS it uses.
* New team member: add an entry to `TEAM` in `_build/content/site_data.py`, put a 600×500 JPG on
  a white background in `_build/content/img/team/<slug>.jpg`, add it to `img-manifest.json`, rebuild.
* Absolute URLs (canonical, og:url, JSON-LD, sitemap) come from `BASE_URL` in `_build/gen.py`.
* New logo: replace `_build/content/img/brand/logo-source.png` (logo on a white background is fine; the
  white is made transparent) and rebuild.
* The "Ab Initio Legal" link (main menu, mobile menu, footer) comes from `LEGAL_SITE` in `site_data.py`.
* After a build, `git status` should list only the pages you meant to change.

## Redirects from the old site
Every old abinitioindia.com URL (pages, the 38 articles, team profiles, services, blog, category/tag
archives, old theme-demo pages) has a 301 to its new page, so search rankings and old links carry over.
Edit `_build/redirects.csv` and rebuild; the build stops if a target page does not exist.

* **Apache** (most shared hosting): `.htaccess` is uploaded with the site. Needs `mod_alias` (standard).
* **nginx**: put the `map {}` block from `_build/nginx-redirects.conf` in the `http {}` context and add
  `if ($abinitio_redirect) { return 301 $abinitio_redirect; }` and `error_page 404 /404.html;` to the `server {}` block.
* After launch, check e.g. https://abinitioindia.com/our-team/ → `/team.html` and
  https://abinitioindia.com/digital-lending/ → `/insights/digital-lending.html`.
* `404.html` uses root-relative links (`/assets/…`) so it is styled at any missing URL on the live
  domain. On the GitHub Pages preview (served from `/AbInitioIndia_Main/`) the 404 page is unstyled; that is expected.

## Fonts
Plus Jakarta Sans is served from `assets/fonts/` (no Google Fonts request). Every page preloads the
latin file; the latin-ext file (e.g. for ₹) only downloads where it is needed. Until the font arrives, text
is set in Arial scaled to the same metrics (the `"Plus Jakarta Sans fallback"` faces in section 0 of
`style.css`), so the swap does not move the layout. Avoid `ch` units for widths: they depend on which
font is showing.

## Critical CSS and images
* Each page inlines the CSS it can use (Bootstrap subset + icon rules + `style.css`, pruned to the classes,
  ids and attributes on that page or added by the site JavaScript) in a `<style>` in `<head>`, so it renders
  without waiting for a stylesheet. The full `bootstrap.subset.min.css` and `style.css` still load without
  blocking, as a safety net. **After editing `style.css`, rebuild**, or pages keep the old inlined rules.
* Icons: pages inline only the Bootstrap Icons they use, and `assets/fonts/bootstrap-icons-subset.woff2`
  (built from `_build/vendor/bootstrap-icons/`) holds just the icons used site-wide (3 KB instead of 130 KB).
  A new `bi-*` icon in a template is picked up automatically on the next build.
* Images: insight cards, article and service images use resized WebP variants (`srcset`); each page's main
  image (hero, first insight card, article or service image) has `fetchpriority="high"` and is preloaded.

## Notes
* **Hosting / preview:** there is no deploy workflow in the repo. For a GitHub Pages preview, set Pages to
  *Deploy from a branch → main → / (root)*; Pages skips the `_build/` folder.
* **Windows long paths:** two article file names are very long. Run `git config core.longpaths true`.
* **FormSubmit:** the first real submission sends an activation email to mail@abinitioindia.com,
  which must be confirmed once. Don't send test enquiries: they go to the client's inbox.
* Content, logos, team photos and article images come from the current abinitioindia.com.

## History
Design options were explored in https://github.com/theprashant26/AbInitioIndia_Themes.
That repo keeps every version of this theme on the branch `archive/theme-b-brand-blue`
(tag `theme-b-brand-blue-v1`). The unused "Royal Crimson Glass" theme is on `archive/theme-c-crimson-gold`.
