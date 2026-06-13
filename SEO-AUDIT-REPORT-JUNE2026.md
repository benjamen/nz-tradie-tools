# NZ Tradie Tools — SEO Audit & Fixes (June 2026)

**Site:** tradietools.nz (static site, GitHub Pages)
**Build:** `venv/bin/python build.py` → 162 articles, 61 calculators, 988 trade pages, 631 job-cost pages, 29 templates. 1,918 HTML pages total.
**Auditor:** seo-tt3 · **Date:** 2026-06-13

## Headline result

The site is already **technically strong**. All structured-data, canonical, OG, and og:image requirements from the brief were **already implemented** before this audit. The high-value work was **content quality** — tightening thin meta descriptions and filling a content gap — not boilerplate. Post-build validation: **3,706 JSON-LD blocks across all pages, 0 invalid.**

## Issues found

| Severity | Issue | File(s) | Fixed? |
|---|---|---|---|
| Medium | 18 article meta descriptions below the 120-char minimum (worst 60) | `content/articles/*.md` | ✅ 10 fixed (worst offenders) |
| Medium | 28 calculator meta descriptions below 120 chars (worst 74) | `content/calculators/*.md` | ✅ 10 fixed (worst offenders) |
| Medium | No dedicated GST hub/overview article (only narrow registration + "should I register" pages) | new file | ✅ Created |
| Low | No titles over 60 chars anywhere on the site | — | ✅ N/A — none found |
| Info | WebSite + Organization schema on homepage | `layouts/index.html` | ✅ Already present |
| Info | SoftwareApplication + HowTo + FAQPage schema on calculators | `layouts/calculator.html` | ✅ Already present |
| Info | Service + ItemList + BreadcrumbList schema on trade hubs | `layouts/trade-hub.html` | ✅ Already present |
| Info | og:image / twitter:image (social-card.svg) sitewide | all layouts | ✅ Already present |
| Info | `static/img/social-card.svg` exists and copies to build | `static/img/` | ✅ Present |

## Fixes applied

### Article descriptions rewritten to 120–160 chars (10)
All rewrites are NZ-specific and keyword-rich:
`june-2-2026-tradie-update`, `june-6-2026-tradie-update`, `plumber-pricing-guide-nz-2026`, `june-2026-tradie-outlook`, `tiler-pricing-guide-nz-2026`, `nz-winter-material-costs-tradie-2026`, `new-plumbing-self-certification-nz`, `sole-trader-vs-company-nz-tradies`, `consent-free-granny-flats-nz-2026`, `tradie-app-fatigue-nz`.

### Calculator descriptions rewritten to 120–160 chars (10)
`gst-calculator`, `subcontractor-tax-calculator`, `vehicle-mileage-calculator`, `earthworks-calculator`, `waterproofing-calculator`, `scaffolding-calculator`, `breakeven-calculator`, `drain-grade-calculator`, `concrete-calculator`, `kitchen-renovation-calculator`.

## Content created

- **`content/articles/gst-guide-nz-tradies-2026.md`** — new GST hub article (~600 words) covering the $60k threshold, filing frequency, claiming GST back, and the 4 most common GST mistakes. Includes 4-question FAQ (renders FAQPage schema) and internal links to `gst-registration-tradies-nz`, `should-i-register-for-gst-nz-tradie`, `gst-calculator`, `tax-dates`, and `nz-tradie-tax-guide-2026`. All link targets verified to exist.
- **`content/articles/best-accounting-software-nz-tradies-2026.md`** — brief asked for a 300-word stub; this article **already existed as a full, superior piece** (comparison table + 3 FAQs). Left as-is rather than downgrading it.

## Remaining recommendations (for humans / next pass)

1. **Finish the description sweep.** 8 more articles and 18 more calculators still sit at 95–119 chars — below ideal but not broken. Same treatment, ~30 mins of work.
2. **Expand the new GST guide** with a worked filing example and a screenshot, and consider adding it to the homepage "Latest Articles" feed promotion.
3. **Internal linking from the new GST guide** is strong outbound; add inbound links to it from `gst-registration-tradies-nz` and `eofy-checklist-nz-tradies-2026` to build the cluster.
4. **Thin "update" articles** (`june-2-2026-tradie-update`, `june-6-2026-tradie-update`) are very short — consider consolidating dated micro-updates into a single rolling "NZ tradie market updates" page to avoid index bloat.
5. No action needed on schema/OG/canonical — already comprehensive and valid.
