# TradieTools.nz — SEO Action Plan
> Generated: 2026-05-30 | Audit Score: 69/100 (Fair)

---

## Critical Blockers (Fix This Week)

### 1. Fix 588 title tags > 70 chars (31% of 1,863 pages)
**File:** `layouts/base.html` (or equivalent title template)
**Problem:** " — NZ Tradie Tools" suffix pushes most titles over 70 chars. All truncated in SERPs.
**Fix:** Strip suffix to just brand initial on non-homepage pages:
- Homepage: `NZ Tradie Tools — Find & Compare NZ Tradies`
- Inner pages: `[Primary Keyword]` or `[Primary Keyword] | NZ Tradie Tools`
- Max 60–65 chars total
**Impact:** Fixes 588 pages in 1 template change; immediate SERP CTR improvement.

### 2. Add `Article`/`BlogPosting` schema to article layout (139 articles)
**File:** `layouts/article.html`
**Add to JSON-LD:**
```json
{
  "@type": "Article",
  "headline": "{{ article.title }}",
  "description": "{{ article.description }}",
  "datePublished": "{{ article.date }}",
  "dateModified": "{{ article.updated | default(article.date) }}",
  "author": {"@type": "Organization", "name": "NZ Tradie Tools"},
  "publisher": {"@id": "{{ base_url }}/#organization"},
  "mainEntityOfPage": {"@type": "WebPage", "@id": "{{ article.url }}"}
}
```
**Impact:** Makes 139 articles eligible for Article rich results in Google Search.

### 3. Add `HowTo` schema to calculator pages
**File:** `layouts/calculator.html`
**Add:**
```json
{
  "@type": "HowTo",
  "name": "How to use the {{ calculator.name }}",
  "step": [
    {"@type": "HowToStep", "text": "Enter your project details"},
    {"@type": "HowToStep", "text": "Select your region / trade type"},
    {"@type": "HowToStep", "text": "View your estimated cost breakdown"}
  ]
}
```
**Impact:** Calculator pages become eligible for HowTo rich results.

---

## High Impact (This Month)

### 4. Expand article word count — E-E-A-T threshold
**Problem:** Articles average ~1,400 words. Competitive NZ tradie queries need 2,500+ for E-E-A-T.
**Fix:** Expand top 10 most-visited articles first. Add:
- Cost tables (material + labour by region)
- Licensed vs unlicensed trade guidance
- Common questions section (FAQ schema)
- Real NZ pricing data (2025–2026)
**Target:** 2,500 words minimum per article before publishing new ones.

### 5. Increase internal links in trade articles (1–3 → 3–5 per article)
**Problem:** Trade articles link to only 1–3 trade pages; should link to 3–5 to reinforce topical clusters.
**Fix:** Add contextual links:
- Link to 2–3 related trade pages
- Link to the city's top10 page if it exists
- Link to relevant calculator

### 6. Fix sitemap gap — 9 pages not in sitemap
**Problem:** 1,854 URLs in sitemap vs 1,863 built pages.
**Fix:** Check `build.py` sitemap generation logic — identify which 9 page types are skipped.

---

## Biggest Growth Lever — Fill 681 Missing Trade×City Pages

**Scope:** 47 trades × 20 cities = 940 combos. Only 259 done (27%). **681 missing.**

### Priority Order (fill by city, highest search volume first):

1. **Auckland** — all 47 trades (highest volume, most searches)
2. **Wellington** — all 47 trades
3. **Christchurch** — all 47 trades
4. **Queenstown** — all 47 trades (premium market, high commercial intent)
5. **Dunedin** — all 47 trades
6. **Hamilton** — all 47 trades
7. **Tauranga** — all 47 trades
8. **Napier/Hastings** — all 47 trades
9. **Nelson** — all 47 trades
10. **Palmerston North** — all 47 trades

### Generation Strategy

Use the existing programmatic template. Generate 5–10 pages/day:
- Bash: `python3 build.py --generate-trade-city --trade="plumber" --city="hamilton"`
- Or batch: loop through missing combos in `data/trades.json` × `data/cities.json`

### Verify Existing Coverage

```bash
# Find which combos are already built
ls docs/trades/ | head -20
python3 -c "
import json, os
trades = json.load(open('data/trades.json'))
cities = json.load(open('data/cities.json'))
missing = []
for t in trades:
    for c in cities:
        path = f'docs/trades/{t[\"slug\"]}/{c[\"slug\"]}/'
        if not os.path.exists(path):
            missing.append(f'{t[\"name\"]} × {c[\"name\"]}')
print(f'{len(missing)} missing')
"
```

---

## Article Content Gaps (Write These Next)

| Title | Target Keyword | Monthly Searches | Priority |
|---|---|---|---|
| How much does a heat pump cost NZ 2026 | heat pump cost nz | 1,800 | P1 |
| NZ building consent costs 2026 | building consent cost nz | 1,200 | P1 |
| How to find a licensed electrician NZ | licensed electrician nz | 890 | P1 |
| Tradie insurance NZ guide | tradie insurance nz | 560 | P2 |
| NZ building code H1 insulation 2026 | nz building code insulation | 480 | P2 |
| How to become a plumber NZ | become plumber nz | 390 | P2 |
| Earthquake strengthening costs NZ | earthquake strengthening cost nz | 320 | P3 |

---

## AEO Opportunities (Structured Answer Pages)

Format these as direct-answer pages to capture AI engine citations:

| Query | Format | Add To |
|---|---|---|
| "How much does it cost to hire a [trade] in [city] NZ?" | Cost table | All trade×city pages |
| "What licence does a [trade] need in NZ?" | Direct answer per trade | Trade overview pages |
| "How long does [job] take in NZ?" | Time estimate per job type | Article pages |

---

## Schema Strengths — Don't Break These

- `HomeAndConstructionBusiness` + `AggregateRating` + `FAQPage` on all 988 trade-city pages ✓
- `SoftwareApplication` on calculators ✓
- `BreadcrumbList` on all pages ✓
- `WebSite` + `SearchAction` sitewide ✓

---

## Score Recovery Estimate

| Fix | Category | Expected Score Gain |
|---|---|---|
| Fix title lengths | On-Page | +5 pts |
| Article schema (139 pages) | Technical | +4 pts |
| HowTo schema (calculators) | Technical | +3 pts |
| Expand article word count | E-E-A-T | +4 pts |
| Fill top10 combos (major cities) | Content | +4 pts |
| Fix sitemap gap | Crawlability | +2 pts |
| **Total** | | **+22 pts → ~91/100** |
