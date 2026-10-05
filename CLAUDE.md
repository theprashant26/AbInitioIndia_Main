# Ab Initio India website – notes for Claude

Production website for Ab Initio India LLP (business advisory, New Delhi), replacing the WordPress
site at https://abinitioindia.com. The client approved this design ("Aurora Brand Glass").
See README.md for the folder map and build commands.

## How the project works
- `site/` is the deployable static site; `build/` generates its HTML. **HTML pages in `site/` are
  build output.** Change content in `build/content/site_data.py` (or `posts/`, `legal.json`),
  templates in `build/skin_b_glass.py`, JS in `build/main_glass.js`, then run `python build/gen2.py`.
  Hand edits to `site/**/*.html` or `site/assets/js/main.js` get overwritten on the next build.
- `site/assets/css/style.css` is hand-written; the build never writes it, but every page inlines the CSS it
  uses, so **rebuild after editing style.css**.
- `sitemap.xml` and `robots.txt` are not generated; edit them by hand.
- After a build, `git diff --stat site/` should show only the pages you meant to change.
- Python 3.10+ with Pillow and fontTools (`pip install pillow fonttools brotli`). Windows: `git config core.longpaths true` (two article slugs exceed MAX_PATH;
  the generator writes with the `\\?\` prefix).
- Page URLs (`about.html`, `services/<slug>.html`, `insights/<slug>.html`, …) are fixed: the redirects
  from the old WordPress URLs depend on them.

## Rules
- Content (text, team, articles) comes from the client / live site. Don't invent or reword copy
  unless asked; fix obvious typos only when asked.
- Never submit the contact form (FormSubmit). It emails the client.
- Team portraits: 600×500, head-and-shoulders, pure white background.
- Keep design tokens in `:root` of style.css (`--blue`, `--navy`, `--sun`, `--bg` …).
- Check changes in a browser at 390px and 1440px before calling them done.

## Launch work still to do
Theme B was the design prototype. The launch hardening was done on the sibling "Theme C" and
still needs porting here. That work lives on branch `archive/theme-c-crimson-gold` of
https://github.com/theprashant26/AbInitioIndia_Themes, folder `Theme-C-Crimson-Gold/`:
- `redirects.csv` (83 old WordPress URL → new page rows; page URLs are identical here) and
  `scripts/build-redirects.py` → `.htaccess` + `nginx-redirects.conf`
- `scripts/set-base-url.py`: canonical / og:url / og:image on https://abinitioindia.com/
  (here: `BASE_URL` in `build/gen.py`, currently still the old GitHub Pages preview URL)
- JSON-LD: Organization/ProfessionalService on home, about, contact; Article on each insight
- Per-page critical CSS (`scripts/build-critical.py`) with non-blocking stylesheet loading
- Self-hosted WOFF2 fonts with metric-matched fallbacks (this site still loads Google Fonts)
- Responsive `srcset` hero images, preload of the LCP image
- Regenerate `sitemap.xml` / `robots.txt` for the live domain
- Targets: Lighthouse mobile Performance 85+, Accessibility 95+, SEO 100; no layout shift
