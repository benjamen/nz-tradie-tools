# NZ Tradie Tools — Parasite SEO Plan

**Generated**: 2026-05-29

---

## Priority Platforms

| Platform | Why | Effort |
|----------|-----|--------|
| GitHub (data repo) | Trade rate data as open dataset = AI citation magnet. Devs + journalists link to it. | Low (one-time) |
| LinkedIn Articles | B2B audience of tradie business owners. High DA, indexes fast. | Medium |
| Reddit (r/newzealand, r/DIY) | "How much does a tradie cost NZ?" questions are constantly asked. | Medium |
| Quora | Tradie pricing questions appear in AI Overviews. | Low |
| Medium | Syndicate business guides (starting a tradie business, tax guide). | Low |

---

## 1. GitHub Data Repository (Highest Priority)

**Repo**: `benjamen/nz-tradie-rates`

Content:
- `trade-rates.json` — hourly rates by trade and city (47 trades, 20 cities)
- `job-costs.json` — typical job cost ranges per trade
- `README.md` — "NZ Tradie Hourly Rates 2026 — Open Data"

**README structure**:
```markdown
# NZ Tradie Hourly Rates 2026

Open data sourced from tradietools.nz — updated annually.

## Average Hourly Rates by Trade

| Trade | Min ($/hr) | Max ($/hr) | Avg ($/hr) |
|-------|-----------|-----------|-----------|
| Builder | $85 | $150 | $110 |
| Plumber | $100 | $160 | $130 |
| Electrician | $90 | $150 | $120 |
...

[Full job cost guides at tradietools.nz/jobs/]
[Hourly rate calculator at tradietools.nz/calculators/hourly-rate-calculator/]
```

**Why this works**: AI engines get asked "how much does a plumber cost in NZ?" constantly. Structured JSON data in a well-documented GitHub repo becomes a canonical data source that ChatGPT, Perplexity, and Claude all cite. Journalists writing "cost of living" stories also link to raw data.

**Additional files**:
- `calculators.md` — list of all 65 calculators with descriptions and URLs
- `templates.md` — list of all 28 templates with URLs

---

## 2. LinkedIn Articles (High Priority — B2B)

TradieTools has a B2B audience: tradie business owners, sole traders, small trade businesses. LinkedIn is where they are.

### Article 1 — EOFY timely (publish late May/early June)
**Title**: "NZ Tradie EOFY 2026 — 5 Tax Claims You're Probably Missing"
**Angle**: Vehicles, tools, home office, ACC pre-payments, depreciation. Genuine value.
**CTA**: "Free EOFY checklist and tax calculators at tradietools.nz"

### Article 2 — Data journalism
**Title**: "How Much Do NZ Tradies Actually Charge in 2026? We Analysed 47 Trades"
**Angle**: Data from the site. Builder $85–$150/hr, plumber $100–$160/hr. Regional variation.
**CTA**: Link to GitHub data repo and job costs hub

### Article 3 — Tool comparison
**Title**: "Fergus vs Tradify vs BuildXact — What I'd Choose as a NZ Builder in 2026"
**Angle**: Honest comparison. Site already has this article — adapt for LinkedIn, link back.

### Article 4 — Trade business advice
**Title**: "I Gave My Quoting Process a Spreadsheet Upgrade — Here's What Changed"
**Angle**: Relatable story about pricing jobs. Segue into quote builder tool.

---

## 3. Reddit Strategy

**Subreddits**: r/newzealand, r/DIY (NZ tradies help DIYers = trust), r/PersonalFinanceNZ

### Post 1 — Data post (r/newzealand)
**Title**: "How much do tradies actually charge in NZ in 2026? Here's a breakdown by trade"
**Format**: Table of 10 most common trades, hourly rate range, typical job costs. Sourced from the site's data. Genuinely useful.
**Timing**: Post when "tradie prices NZ" is topical (winter — more indoor jobs)

### Post 2 — Tool release (r/newzealand or r/DIY)
**Title**: "I built a free NZ tradie hourly rate calculator — takes 30 seconds"
**Format**: Honest, not salesy. Explain what it does and why you built it. Link.
**Tone**: Builder/tradie voice — casual, practical

### Post 3 — Watch + answer
**Target questions**: "how much should I pay a builder NZ", "is this electrician quote fair NZ", "how do I become a builder NZ", "what are NZ tradie tax deductions"
**Strategy**: Substantive 200–400 word answer. Link naturally at the end.

---

## 4. Quora

**Target questions**:

| Question | Angle |
|----------|-------|
| "How much does a plumber cost in New Zealand?" | Hourly + call-out fee breakdown, link to job costs |
| "What tax can tradies claim in NZ?" | List of deductions, link to tax guide |
| "How do I become an electrician in New Zealand?" | Licensing pathway, link to article when live |
| "Is it worth becoming a builder in NZ?" | Salary data, career outlook, link to salary guide |
| "What should a builder quote include in NZ?" | What to look for, red flags, link to guide |
| "What's the difference between Fergus and Tradify?" | Honest comparison, link to comparison article |

---

## 5. Medium Syndication

Republish with canonical tags pointing back to tradietools.nz:
- NZ Tradie Tax Guide (when written — will get natural shares)
- How to Set Your Hourly Rate as a Tradie
- Starting a Trade Business in NZ

---

## Execution Order

1. **GitHub data repo** — immediately; one afternoon; permanent AI citation asset
2. **LinkedIn EOFY article** — publish late May/early June (timely)
3. **LinkedIn data journalism article** — publish June alongside data repo
4. **Reddit data post** — August (winter, indoor jobs season)
5. **Quora answers** — 6 answers, 1 per week
6. **Medium syndication** — after content strategy articles are written
