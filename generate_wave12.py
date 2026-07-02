#!/usr/bin/env python3
"""
Wave 12 SEO content generator — TradieTools NZ
New cities: Whangarei, Queenstown, Invercargill, Whanganui, Gisborne
Core trades for each: electrician, plumber, builder, painter, roofer, handyman
National guides: granny flat, home extension, security alarm, double garage
Run: python3 generate_wave12.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

NEW_CITIES = {
    "whangarei":    {"name":"Whangarei",    "region":"Northland",           "rate_adj":"broadly regional, tradies in demand due to distance from Auckland"},
    "queenstown":   {"name":"Queenstown",   "region":"Queenstown-Lakes",    "rate_adj":"among NZ's highest — tourism and construction demand drives premium rates"},
    "invercargill": {"name":"Invercargill", "region":"Southland",           "rate_adj":"below national average — lower cost of living reflects in trade pricing"},
    "whanganui":    {"name":"Whanganui",    "region":"Manawatu-Whanganui",  "rate_adj":"broadly regional"},
    "gisborne":     {"name":"Gisborne",     "region":"Gisborne",            "rate_adj":"broadly regional, smaller market with fewer competing tradies"},
}

CITY_CONTEXT = {
    "whangarei": {
        "about":    "Whangarei is NZ's northernmost city and Northland's commercial hub. The subtropical climate, strong boat-building industry, and growing lifestyle migration from Auckland keep tradies busy year-round.",
        "climate":  "subtropical, warm and humid with high rainfall",
        "market":   "Growing strongly as Aucklanders relocate for lifestyle and affordability. Construction and renovation demand is high.",
        "tip":      "Whangarei tradies serve a wide geographic area including the Kaipara and Bay of Islands — book early as good operators fill their books quickly.",
    },
    "queenstown": {
        "about":    "Queenstown is NZ's premium lifestyle and tourism destination. Tradies here command the highest rates outside Auckland — labour is expensive and high-quality work is expected by a demanding client base.",
        "climate":  "alpine, cold winters with snow, warm dry summers",
        "market":   "High-end residential construction, luxury renovations, and tourism accommodation fit-outs dominate. Budget operators are rare — quality is the norm.",
        "tip":      "Queenstown tradies are in extreme demand. For large projects, expect to wait 2–4 months for top operators. Always get multiple quotes as rates vary significantly.",
    },
    "invercargill": {
        "about":    "Invercargill is NZ's southernmost city and Southland's commercial centre. Trade rates are among the lowest in NZ, reflecting the lower cost of living. The city's cold climate drives strong demand for heating and insulation work.",
        "climate":  "cold, wet, and windy — one of NZ's coldest cities",
        "market":   "Steady residential market with strong demand for insulation, heating, and weathertightness work. Affordable property prices drive renovation activity.",
        "tip":      "Invercargill has a strong community of reliable tradies. Prices are competitive — get at least 2 quotes but don't sacrifice quality for the cheapest price.",
    },
    "whanganui": {
        "about":    "Whanganui is a growing arts and heritage city on the west coast of the North Island. Affordable property prices and increasing migration from larger cities are driving renovation and new build activity.",
        "climate":  "mild, moderate rainfall, warm summers",
        "market":   "Heritage home renovation is big in Whanganui — the city has beautiful Victorian and Edwardian stock. New builds are increasing on the city's fringes.",
        "tip":      "Whanganui has a good spread of local tradies. Heritage property work (villa restoration, character features) is a specialty — ask about experience with older homes.",
    },
    "gisborne": {
        "about":    "Gisborne is NZ's most isolated city — the first in the world to see the sunrise. The Poverty Bay wine and horticulture region has strong commercial and residential construction activity. Fewer tradies means booking in advance is important.",
        "climate":  "warm and sunny, one of NZ's sunniest regions",
        "market":   "Active residential market bolstered by the wine and horticulture industry. Smaller tradie pool means good operators fill their books quickly.",
        "tip":      "Plan ahead in Gisborne — fewer tradies means less competition. Book popular operators 4–8 weeks in advance for major work.",
    },
}

# ── Electrician ───────────────────────────────────────────────────────────────

ELEC_RATES = {
    "whangarei":    ("$88–$155/hr", "$68–$148"),
    "queenstown":   ("$115–$195/hr", "$85–$180"),
    "invercargill": ("$78–$140/hr", "$58–$128"),
    "whanganui":    ("$82–$148/hr", "$62–$138"),
    "gisborne":     ("$85–$152/hr", "$65–$142"),
}

def electrician_article(city_key):
    c = NEW_CITIES[city_key]
    ctx = CITY_CONTEXT[city_key]
    city, region = c["name"], c["region"]
    hourly, callout = ELEC_RATES[city_key]
    return f"""---
title: "Electricians {city} 2026 — Electrician Rates, Costs and What to Expect"
description: "Electricians {city} 2026 — {city} electrician hourly rates, call-out costs, common job prices, and how to find a reliable registered electrician near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["electricians {city}", "electrician {city}", "electrician cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{ctx["about"]} Here's what electricians charge in {city} in 2026.

## {city} Electrician Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Call-out fee (weekday) | {callout} |
| After-hours call-out | $150–$320 |
| Power point installation (per point) | $180–$380 |
| Light fitting installation (per fitting) | $120–$280 |
| Switchboard upgrade | $1,800–$4,500 |
| EV charger installation (7kW, supply + install) | $850–$1,750 |
| Heat pump wiring (per unit) | $280–$580 |
| Smoke alarm installation (per alarm) | $90–$210 |
| Rangehood / oven circuit | $280–$580 |
| Rewire (3-bed home) | $11,000–$24,000 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Electrician Market

{ctx["market"]} {ctx["tip"]}

## Registered Electricians in {city}

All electrical work in NZ is **restricted work** — it must be done by a registered electrician who issues an Electrical Certificate of Compliance (eCoC). Verify your electrician is registered at [electricians.org.nz](https://www.electricians.org.nz) before any work begins.

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does an electrician cost in {city}?**
Hourly rate: {hourly}. Call-out: {callout}. Switchboard upgrade: $1,800–$4,500.

*Related: [EV Charger Installation {city}](/articles/ev-charger-installation-{city_key}-nz/) | [Switchboard Upgrade {city}](/articles/switchboard-upgrade-{city_key}-nz/)*
"""


# ── Plumber ───────────────────────────────────────────────────────────────────

PLUMB_RATES = {
    "whangarei":    ("$90–$160/hr", "$68–$150"),
    "queenstown":   ("$120–$200/hr", "$90–$190"),
    "invercargill": ("$80–$145/hr", "$60–$132"),
    "whanganui":    ("$84–$152/hr", "$64–$140"),
    "gisborne":     ("$88–$158/hr", "$66–$145"),
}

def plumber_article(city_key):
    c = NEW_CITIES[city_key]
    ctx = CITY_CONTEXT[city_key]
    city, region = c["name"], c["region"]
    hourly, callout = PLUMB_RATES[city_key]
    return f"""---
title: "Plumbers {city} 2026 — Plumber Rates, Costs and What to Expect"
description: "Plumbers {city} 2026 — {city} plumber hourly rates, call-out costs, common job prices, and how to find a reliable registered plumber near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["plumbers {city}", "plumber {city}", "plumber cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{ctx["about"]} Here's what plumbers charge in {city} in 2026.

## {city} Plumber Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Call-out fee (weekday) | {callout} |
| After-hours call-out | $160–$350 |
| Tap replacement (per tap) | $180–$380 |
| Toilet installation | $380–$750 |
| Hot water cylinder replacement (180L, supply + install) | $1,800–$3,300 |
| Heat pump hot water (supply + install) | $3,800–$7,500 |
| Shower installation | $580–$1,400 |
| Burst pipe repair | $280–$680 |
| Blocked drain (unblock) | $180–$420 |
| Leak detection | $180–$420 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Plumbing Market

{ctx["market"]} {ctx["tip"]}

## Licensed Plumbers in {city}

All plumbing work in NZ must be done by a **registered plumber** (PGDB-registered). A plumbing compliance certificate is legally required for any plumbing work. Verify at [pgdb.co.nz](https://www.pgdb.co.nz).

**Find {city} plumbers:** [Plumbers {city}](/trades/plumbers/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a plumber cost in {city}?**
Hourly rate: {hourly}. Call-out: {callout}. Hot water cylinder replacement: $1,800–$3,300.

*Related: [Hot Water Cylinder Cost NZ](/articles/hot-water-cylinder-cost-nz/) | [Blocked Drain Cost NZ](/articles/blocked-drain-cost-nz/)*
"""


# ── Builder ───────────────────────────────────────────────────────────────────

BUILDER_RATES = {
    "whangarei":    ("$92–$162/hr", "$68–$148", "Whangarei's growing construction market is driven by lifestyle migration and holiday home development across Northland. The marine and boat-building heritage gives Whangarei tradespeople excellent skills in precision craftsmanship."),
    "queenstown":   ("$125–$210/hr", "$95–$195", "Queenstown is NZ's most expensive building market outside Auckland. Luxury residential and hospitality construction dominates. Expect premium pricing — and premium quality — from established Queenstown builders."),
    "invercargill": ("$82–$148/hr", "$62–$135", "Invercargill has a cost-competitive building market. The city's cold climate means builders are experienced with robust weathertightness, insulation, and heating systems. Quality is generally good at competitive prices."),
    "whanganui":    ("$85–$152/hr", "$64–$138", "Whanganui's heritage housing stock keeps builders busy with villa restoration and character home renovation. New builds on the city's fringes are increasing as affordability attracts migrants from Wellington and beyond."),
    "gisborne":     ("$88–$158/hr", "$66–$142", "Gisborne's smaller tradie pool means quality builders are in demand. The wine and horticulture industry drives commercial construction alongside strong residential demand."),
}

def builder_article(city_key):
    c = NEW_CITIES[city_key]
    ctx = CITY_CONTEXT[city_key]
    city, region = c["name"], c["region"]
    hourly, callout, local = BUILDER_RATES[city_key]
    return f"""---
title: "Builders {city} 2026 — Builder Rates, Renovation Costs and What to Expect"
description: "Builders {city} 2026 — {city} builder hourly rates, renovation costs, new build pricing, and how to find a reliable Licensed Building Practitioner near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["builders {city}", "builder {city}", "builder cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what builders charge in {city} in 2026.

## {city} Builder Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Call-out / minimum charge | {callout} |
| New home build (per m², turnkey) | $2,800–$4,600/m² |
| Extension (per m²) | $2,400–$4,300/m² |
| Major renovation | $85,000–$320,000+ |
| Bathroom renovation (complete) | $13,000–$38,000 |
| Kitchen renovation (complete) | $15,000–$52,000 |
| Deck construction (per m²) | $1,400–$2,900/m² |
| Building inspection pre-purchase | $380–$850 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Building Market

{local} {ctx["tip"]}

## Licensed Building Practitioners (LBP) in {city}

Restricted building work — structural framing, weathertightness, foundations — must be done by an LBP. Verify at [lbp.govt.nz](https://www.lbp.govt.nz) before signing any contract.

**Find {city} builders:** [Builders {city}](/trades/builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a builder cost in {city}?**
Hourly rate: {hourly}. New build: $2,800–$4,600/m². Major renovation: $85,000–$320,000+.

*Related: [New Home Build Cost NZ](/articles/new-home-build-cost-nz/) | [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/)*
"""


# ── Painter ───────────────────────────────────────────────────────────────────

PAINTER_RATES = {
    "whangarei":    ("$60–$115/hr", "$45–$105", "$6,500–$13,000"),
    "queenstown":   ("$80–$150/hr", "$60–$140", "$9,000–$19,000"),
    "invercargill": ("$55–$105/hr", "$40–$95", "$5,500–$11,000"),
    "whanganui":    ("$58–$110/hr", "$42–$100", "$5,800–$12,000"),
    "gisborne":     ("$60–$115/hr", "$45–$105", "$6,500–$13,000"),
}

def painter_article(city_key):
    c = NEW_CITIES[city_key]
    ctx = CITY_CONTEXT[city_key]
    city, region = c["name"], c["region"]
    hourly, callout, exterior = PAINTER_RATES[city_key]
    return f"""---
title: "Painters {city} 2026 — Painting Rates, Costs and What to Expect"
description: "Painters {city} 2026 — {city} painter rates, interior painting costs, exterior house painting prices, and how to find a reliable painter near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["painters {city}", "painter {city}", "painting cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{ctx["about"]} Here's what painters charge in {city} in 2026.

## {city} Painter Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Day rate | {callout.replace("$", "$").split("–")[0].strip()}–$850/day |
| Interior — bedroom (supply + paint) | $550–$1,350 |
| Interior — living room (supply + paint) | $750–$1,900 |
| Full interior (3-bed home) | $5,000–$11,500 |
| Full exterior (3-bed home) | {exterior} |
| Exterior preparation (wash, sand, fill) | included in above |
| Deck staining / oiling (per m²) | $16–$40/m² |
| Fence painting (per m linear) | $18–$45/m |
| Roof painting (per m²) | $12–$28/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Painting Market

{ctx["market"]}

## Getting the Best Paint Job in {city}

Quality preparation is 30–40% of a good paint job. A painter who washes, sands, fills, and primes properly will produce a job that lasts 10+ years. Always ask what preparation is included in your quote — shortcuts here mean the job fails in 3–5 years.

For exteriors in {city}'s {ctx["climate"]} climate, use quality exterior paint — Resene X-200 or Dulux Weathershield are proven NZ products.

**Find {city} painters:** [Painters {city}](/trades/painters/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a painter cost in {city}?**
Hourly rate: {hourly}. Interior 3-bed home: $5,000–$11,500. Exterior 3-bed home: {exterior}.

*Related: [Interior Painting Cost NZ](/articles/interior-painting-cost-nz/) | [Exterior House Painting Cost NZ](/articles/exterior-house-painting-cost-nz/)*
"""


# ── Roofer ────────────────────────────────────────────────────────────────────

ROOFER_RATES = {
    "whangarei":    ("$88–$158/hr", "$68–$148", "$18,000–$38,000"),
    "queenstown":   ("$115–$200/hr", "$88–$188", "$25,000–$55,000"),
    "invercargill": ("$80–$145/hr", "$60–$132", "$15,000–$32,000"),
    "whanganui":    ("$84–$152/hr", "$64–$140", "$16,000–$34,000"),
    "gisborne":     ("$88–$158/hr", "$66–$145", "$18,000–$38,000"),
}

def roofer_article(city_key):
    c = NEW_CITIES[city_key]
    ctx = CITY_CONTEXT[city_key]
    city, region = c["name"], c["region"]
    hourly, callout, reroof = ROOFER_RATES[city_key]
    return f"""---
title: "Roofers {city} 2026 — Roofing Costs, Repairs and What to Expect"
description: "Roofers {city} 2026 — {city} roofing costs, roof repair prices, re-roofing quotes, iron vs tile vs membrane costs, and how to find a reliable roofer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["roofers {city}", "roofer {city}", "roofing cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{ctx["about"]} Here's what roofers charge in {city} in 2026.

## {city} Roofing Costs 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Call-out (leak investigation) | {callout} |
| Minor repair (refix, reseal) | $280–$650 |
| Tile replacement (per tile) | $80–$200 |
| Flashing repair / replacement | $380–$1,200 |
| Full re-roof — corrugated iron (3-bed) | {reroof} |
| Full re-roof — pressed steel tile (3-bed) | $22,000–$48,000 |
| Full re-roof — butynol membrane (flat) | $85–$160/m² |
| Roof inspection / report | $280–$580 |
| Fascia / barge board replacement (per m) | $85–$195/m |
| Gutter replacement (per m linear) | $55–$120/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Roofing Market

{ctx["market"]} {ctx["tip"]}

## {city} Climate and Roofing

{city}'s {ctx["climate"]} climate affects roofing material selection and maintenance frequency. {"Northland's high rainfall and humidity accelerate moss and lichen growth — annual roof treatments are recommended in Whangarei." if city_key == "whangarei" else "Queenstown's alpine freeze-thaw cycles stress roofing materials — quality flashings and thermal movement allowance are important." if city_key == "queenstown" else "Invercargill's cold wet climate and driving southerly winds demand robust roofing with quality flashings and sealed penetrations." if city_key == "invercargill" else "Gisborne's sunny climate with periodic heavy rain events means good drainage design is important for Gisborne roofs." if city_key == "gisborne" else "Whanganui's mild climate is generally kind to roofing materials — standard maintenance intervals apply."}

**Find {city} roofers:** [Roofers {city}](/trades/roofers/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a roofer cost in {city}?**
Hourly rate: {hourly}. Full re-roof (corrugated iron, 3-bed): {reroof}.

*Related: [Roofer Pricing Guide NZ](/articles/roofer-pricing-guide-nz-2026/) | [Builders {city}](/articles/builder-{city_key}-nz/)*
"""


# ── Handyman ──────────────────────────────────────────────────────────────────

HANDYMAN_RATES = {
    "whangarei":    ("$68–$125/hr", "$52–$112"),
    "queenstown":   ("$90–$165/hr", "$68–$155"),
    "invercargill": ("$60–$112/hr", "$45–$100"),
    "whanganui":    ("$62–$118/hr", "$48–$105"),
    "gisborne":     ("$65–$122/hr", "$50–$110"),
}

def handyman_article(city_key):
    c = NEW_CITIES[city_key]
    ctx = CITY_CONTEXT[city_key]
    city, region = c["name"], c["region"]
    hourly, callout = HANDYMAN_RATES[city_key]
    return f"""---
title: "Handyman {city} 2026 — Handyman Rates, Costs and What They Can Do"
description: "Handyman {city} 2026 — {city} handyman hourly rates, typical job costs, what a handyman can and can't do, and how to find a reliable handyman near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["handyman {city}", "handyman cost {city}", "odd jobs {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{ctx["about"]} Here's what handymen charge in {city} in 2026.

## {city} Handyman Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Minimum call-out / half day | {callout} |
| Full day rate | $450–$900/day |
| Flat-pack furniture assembly (per item) | $80–$200 |
| TV wall mounting | $120–$250 |
| Picture / mirror hanging (per item) | $45–$95 |
| Door adjustment / rehang | $120–$250 |
| Curtain rod installation (per rod) | $65–$145 |
| Fence repair (per post) | $120–$280 |
| Gutter cleaning (per linear metre) | $6–$14/m |
| Caulking / weathersealing | $120–$280 |
| Minor plastering / patching (per hole) | $80–$200 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## What a Handyman Can and Can't Do in {city}

**Handymen can do:** Flat-pack assembly, painting and patching, minor carpentry (shelves, rods), gutter cleaning, fence repairs, tiling (non-structural), garden work, moving furniture.

**Cannot do (licensed trades only):**
- Electrical work (requires registered electrician)
- Gas fitting (requires registered gasfitter)
- Plumbing (requires registered plumber)
- Structural building work (requires LBP)

A good handyman knows when to refer to a licensed trade — if they claim to do everything, ask questions.

**Find {city} handymen:** [Handymen {city}](/trades/handymen/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a handyman cost in {city}?**
Hourly rate: {hourly}. Minimum call-out: {callout}. Full day: $450–$900.

*Related: [Builders {city}](/articles/builder-{city_key}-nz/) | [Painters {city}](/articles/painter-{city_key}-nz/)*
"""


# ── National Guides ───────────────────────────────────────────────────────────

def granny_flat_article():
    return f"""---
title: "Granny Flat Cost NZ 2026 — Sleepout, Minor Dwelling and Detached Unit Prices"
description: "Granny flat cost NZ 2026 — cost to build a granny flat in NZ, sleepout vs minor dwelling, prefab vs site-built costs, consent requirements, and rental income potential."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["granny flat cost NZ", "sleepout cost NZ", "minor dwelling NZ", "backyard cottage NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Granny flats, sleepouts, and minor dwellings are one of NZ's most popular property investments. Here's what they cost and what's involved in 2026.

## Granny Flat Cost NZ 2026

| Type | Typical NZ cost |
|---|---|
| Basic sleepout (no plumbing, 20–30m²) | $35,000–$65,000 |
| Studio / sleepout with bathroom (30–40m²) | $65,000–$120,000 |
| Self-contained minor dwelling (45–60m²) | $120,000–$200,000 |
| Self-contained minor dwelling (60–80m²) | $180,000–$280,000 |
| Prefab / modular unit (supply + install) | $75,000–$160,000 |
| Relocatable home (purchase + relocation) | $45,000–$120,000 |

*All prices GST inclusive. Auckland and Wellington at higher end. Prices vary by site conditions, specifications, and whether services (power, water, sewer) need extending.*

## Types of Granny Flat in NZ

### Sleepout (No Plumbing)
A room for sleeping and living, sharing the main house's bathroom and kitchen. No separate plumbing means simpler consent and lower cost. Can be built under a simpler consent pathway.

### Self-Contained Minor Dwelling
Has its own kitchen, bathroom, and laundry. Can be legally rented as a separate dwelling. Requires full building consent and must meet NZ Building Code for habitable buildings. Most valuable for rental income.

### Prefab / Modular Unit
Factory-built unit delivered to site and craned into position. Faster than site-built. Quality varies — choose a reputable NZ manufacturer. Still requires building consent.

### Relocated House
An existing house moved to your site. Lower cost than new build but relocation and foundation costs add up. Good option if you can find a suitable house in your area.

## What's Included in the Cost?

The prices above typically include the structure but you should budget separately for:

| Item | Typical additional cost |
|---|---|
| Site preparation / earthworks | $5,000–$25,000 |
| Extending power supply | $3,000–$8,000 |
| Extending water supply | $2,000–$6,000 |
| Sewer / septic connection | $3,000–$15,000 |
| Driveway / path | $3,000–$12,000 |
| Landscaping | $3,000–$15,000 |
| Building consent | $3,000–$10,000 |

**Total all-up budget:** Add 20–40% to the structure cost to cover site and service costs.

## Consent Requirements for Granny Flats in NZ

**2023 reform:** NZ now allows minor dwellings up to 60m² **without resource consent** on most residential sites under the NPS-UD (National Policy Statement for Urban Development). **Building consent is still required.**

**Key rules:**
- Up to 60m² = resource consent exempt in most urban zones
- Must still get **building consent** from your local council
- Must comply with NZ Building Code (insulation, weathertightness, services)
- Setbacks from boundaries still apply (typically 1–1.5m)
- Height restrictions (typically 5m for flat sites)

**Check with your local council** — rules vary by zone. The 60m² exemption doesn't apply everywhere.

## Rental Income Potential

A self-contained minor dwelling can generate:

| Location | Typical weekly rent |
|---|---|
| Auckland (suburban) | $400–$650/week |
| Wellington | $380–$600/week |
| Christchurch | $320–$500/week |
| Regional cities | $250–$420/week |

At $400/week, a granny flat generating $20,800/year provides a strong return on a $150,000 investment — approximately 14% gross yield before costs.

**Find builders:** [Builders Near You](/trades/builders/) | [Post a Job Free](/post-job/)

---

**How much does a granny flat cost in NZ?**
Basic sleepout: $35,000–$65,000. Self-contained minor dwelling: $120,000–$280,000. Prefab: $75,000–$160,000.

**Do I need consent for a granny flat in NZ?**
Building consent is always required. Resource consent is now exempt for minor dwellings up to 60m² on most urban residential sites under the 2023 NPS-UD reform.

*Related: [New Home Build Cost NZ](/articles/new-home-build-cost-nz/) | [Builders Near You](/trades/builders/)*
"""


def home_extension_article():
    return f"""---
title: "Home Extension Cost NZ 2026 — Single Storey, Double Storey and What to Expect"
description: "Home extension cost NZ 2026 — cost to extend a house in NZ, single vs double storey extension prices per m², what's included, consent requirements, and how to find a builder near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["home extension cost NZ", "house extension cost NZ", "extension NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

A home extension is often a better financial decision than moving — you add space without paying agent fees, stamp duty, or the stress of selling. Here's what it costs in NZ in 2026.

## Home Extension Cost NZ 2026

| Extension type | Typical NZ cost per m² | Total (30m² extension) |
|---|---|---|
| Single storey (standard) | $2,800–$4,200/m² | $84,000–$126,000 |
| Single storey (premium finish) | $4,200–$6,000/m² | $126,000–$180,000 |
| Double storey (standard) | $3,200–$5,000/m² | $96,000–$150,000 |
| Double storey (premium) | $5,000–$7,500/m² | $150,000–$225,000 |
| Garage conversion (habitable space) | $1,800–$3,500/m² | $36,000–$70,000 |
| Carport / garage addition | $1,400–$2,800/m² | $28,000–$56,000 |

*All prices GST inclusive. Auckland and Wellington at the higher end. Prices vary significantly with existing house construction type, foundation requirements, and specification.*

## What Drives Extension Cost?

**Matching the existing house:** Blending new work with existing weatherboarding, roofline, windows, and interior finishes adds complexity.

**Foundation type:** If the extension is over a sloped site or requires piles, foundation costs increase significantly.

**Services extension:** Extending plumbing, electrical, and HVAC into the new space adds cost.

**Structural opening:** Creating an opening into the existing house may require removing load-bearing walls and installing structural steel — a significant cost.

**Ceiling height:** Standard 2.4m stud is cheapest. Higher studs (2.7m, 3.0m) increase wall area and cost.

## Extension vs Moving House

| Factor | Extension | Moving |
|---|---|---|
| Upfront cost | $80,000–$250,000+ | Agent fees 2–3%, legal, moving |
| Disruption | Months of construction | Move out and in |
| Location | Keep your location | New location (good or bad) |
| Stamp duty / transfer costs | None | Legal, title transfer |
| Result | Customised to your needs | Takes what's available |

For most NZ families in a location they love, extending is financially better than moving if the existing house has a suitable section.

## Consent Requirements

Home extensions **always require building consent**. Resource consent may also be required if the extension:
- Breaches setback distances from boundaries
- Exceeds height limits for your zone
- Is in a heritage zone or overlay

Your builder or architect will advise on consent requirements for your specific site.

**Building consent fees:** $5,000–$15,000 depending on scope.
**Design / architect fees:** $8,000–$25,000 for a standard extension.

## Timeline

A standard 30m² single-storey extension:
- Design and consent: 2–4 months
- Construction: 3–5 months
- Total: 5–9 months from decision to completion

**Find NZ builders:** [Builders Near You](/trades/builders/) | [Post a Job Free](/post-job/)

---

**How much does a home extension cost in NZ?**
Single storey (30m², standard): $84,000–$126,000. Double storey (30m², standard): $96,000–$150,000.

**Do I need consent to extend my house in NZ?**
Yes — building consent is always required. Resource consent may also be needed depending on your zone and the extension's size and position.

*Related: [New Home Build Cost NZ](/articles/new-home-build-cost-nz/) | [Granny Flat Cost NZ](/articles/granny-flat-cost-nz/) | [Builders Near You](/trades/builders/)*
"""


def security_alarm_article():
    return f"""---
title: "Security Alarm Installation Cost NZ 2026 — Home Alarm System Prices"
description: "Security alarm installation cost NZ 2026 — home alarm system costs, monitored vs unmonitored, smart alarm prices, and how to find a reliable security installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["security alarm cost NZ", "home alarm NZ", "security system NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

A home security alarm is one of the most effective deterrents against burglary. Here's what alarm systems cost to install in NZ in 2026.

## Security Alarm Installation Cost NZ 2026

| System type | Typical NZ cost (supply + install) |
|---|---|
| Basic DIY alarm kit (self-monitored) | $300–$800 |
| Professionally installed alarm (unmonitored) | $800–$2,200 |
| Professionally installed (monitored, 3-bed) | $1,200–$3,000 |
| Smart alarm system (app-controlled) | $1,500–$3,500 |
| Premium system with cameras (3-bed) | $2,500–$6,000 |
| Add-on sensor (per door / window) | $120–$280 |
| Add-on camera (per camera, installed) | $280–$650 |
| Monitoring service (monthly fee) | $25–$65/month |
| System service / maintenance (annual) | $150–$380 |

*All prices GST inclusive. Auckland and Wellington at the higher end.*

## Monitored vs Unmonitored Alarms

**Unmonitored (self-monitoring):**
- Alarm sounds locally and sends notification to your phone
- You decide whether to call police
- No monthly fees
- Good for low-risk areas or as a deterrent

**Professionally monitored:**
- Alarm centre receives alert and responds 24/7
- Can dispatch police or security patrol if you don't respond
- Monthly monitoring fee ($25–$65/month)
- Stronger deterrent — burglars know monitored alarms are responded to
- Insurance discounts of 5–15% common with monitored alarms

## Components of a Home Alarm System

| Component | What it does |
|---|---|
| Control panel | Brain of the system — processes all inputs |
| PIR motion sensors | Detects movement (infrared) |
| Door/window contacts | Detects opening of entry points |
| Siren (internal + external) | Deters intruders, alerts neighbours |
| Keypad | Arm/disarm at entry points |
| Remote / key fob | Arm/disarm from outside |
| Backup battery | Works during power cuts |
| Communicator | Sends signals to monitoring centre or phone |

## Smart / App-Based Alarm Systems

Smart alarm systems (Yale, Ring, Bosch, Ajax) offer:
- App-based arming and disarming
- Live notifications and alerts
- Integration with smart home (Google Home, Alexa)
- Remote camera access
- Easy DIY installation (though professional is recommended for hard-wired systems)

**Popular NZ brands:** Yale, Paradox, DSC, Bosch, Ajax, Ring (self-monitored)

## NZ Security Licensing

Professional security installers must hold a **Certificate of Approval** under the Private Security Personnel and Private Investigators Act 2010. Always verify your installer is licensed — unlicensed security installation is illegal.

**Find NZ security installers:** [Electricians Near You](/trades/electricians/) | [Post a Job Free](/post-job/)

---

**How much does a home alarm cost in NZ?**
Professionally installed monitored system (3-bed): $1,200–$3,000 plus $25–$65/month monitoring.

**Does a monitored alarm reduce home insurance in NZ?**
Yes — most NZ insurers offer discounts of 5–15% for professionally monitored alarm systems. Check with your insurer.

*Related: [Electricians Near You](/trades/electricians/) | [Smoke Alarm Installation NZ](/articles/smoke-alarm-installation-nz/)*
"""


def double_garage_article():
    return f"""---
title: "Double Garage Cost NZ 2026 — Prices, Types and What to Expect"
description: "Double garage cost NZ 2026 — cost to build a double garage in NZ, single vs double, kit set vs custom build prices, consent requirements, and how to find a builder near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["double garage cost NZ", "garage cost NZ", "build a garage NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Adding a garage adds storage, security, and value to your home. Here's what garages cost to build in NZ in 2026.

## Garage Build Cost NZ 2026

| Garage type | Typical NZ cost |
|---|---|
| Single garage (kit set, basic) | $18,000–$35,000 |
| Single garage (site built, standard) | $28,000–$55,000 |
| Double garage (kit set, basic) | $28,000–$52,000 |
| Double garage (site built, standard) | $42,000–$85,000 |
| Double garage (premium, insulated, lined) | $65,000–$140,000 |
| Triple garage (site built) | $65,000–$160,000 |
| Garage with loft / room above | $80,000–$200,000+ |
| Garage door (double, automatic, supply + fit) | $2,800–$6,500 |
| Concrete floor (per m²) | $100–$200/m² |

*All prices GST inclusive. Auckland and Wellington at the higher end.*

## Kit Set vs Site Built

**Kit set garage:**
- Cheaper upfront ($28,000–$52,000 for double)
- Faster to build (1–2 weeks once consent approved)
- Limited design flexibility
- Still requires consent, foundation, and electrical
- NZ suppliers: Totalspan, Steel-Line, Ranbuild

**Site built (custom):**
- Matches your house style and materials
- Any size and layout
- Higher cost ($42,000–$85,000+)
- Takes longer (4–8 weeks construction)
- Best for garages attached to or adjacent to the house

## What Affects Garage Cost?

**Size:** Standard double garage (6×6m to 6×7m) vs oversized (7×8m+).

**Cladding:** Coloursteel/metal is cheapest. Weatherboard or brick veneer to match the house costs more.

**Roofline:** Simple mono-pitch is cheapest. Hip or gable to match the house costs more.

**Floor:** Plain concrete is standard. Epoxy coating adds $2,000–$5,000. Tiles add more.

**Insulation and lining:** An uninsulated, unlined garage is functional. An insulated, GIB-lined garage suitable for a workshop or conversion costs significantly more.

**Services:** Power (lights, power points, EV charger) adds $1,500–$4,000. Water adds more.

## Consent Requirements in NZ

Garages generally require building consent. Exceptions:

- **Exempt:** A garage under 10m² may be exempt, but a standard double garage is well over this
- **Most garages require consent** — check with your local council

If attached to the house, it's part of the main building consent. Detached garages are a separate consent.

**Find NZ builders:** [Builders Near You](/trades/builders/) | [Post a Job Free](/post-job/)

---

**How much does a double garage cost in NZ?**
Kit set double garage: $28,000–$52,000. Site built standard: $42,000–$85,000. Premium (insulated, lined): $65,000–$140,000.

**Do I need consent to build a garage in NZ?**
Yes — most garages require building consent. Check with your local council for your specific zone and size.

*Related: [New Home Build Cost NZ](/articles/new-home-build-cost-nz/) | [Builders Near You](/trades/builders/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

# New city core trades
for ck in NEW_CITIES:
    ARTICLES.append((f"electrician-{ck}-nz",  lambda k=ck: electrician_article(k)))
    ARTICLES.append((f"plumber-{ck}-nz",       lambda k=ck: plumber_article(k)))
    ARTICLES.append((f"builder-{ck}-nz",       lambda k=ck: builder_article(k)))
    ARTICLES.append((f"painter-{ck}-nz",       lambda k=ck: painter_article(k)))
    ARTICLES.append((f"roofer-{ck}-nz",        lambda k=ck: roofer_article(k)))
    ARTICLES.append((f"handyman-{ck}-nz",      lambda k=ck: handyman_article(k)))

# National guides
ARTICLES += [
    ("granny-flat-cost-nz",      granny_flat_article),
    ("home-extension-cost-nz",   home_extension_article),
    ("security-alarm-cost-nz",   security_alarm_article),
    ("double-garage-cost-nz",    double_garage_article),
]


if __name__ == "__main__":
    created = skipped = 0
    for slug, fn in ARTICLES:
        path = OUT / f"{slug}.md"
        if path.exists():
            print(f"  skip  {slug}"); skipped += 1
        else:
            path.write_text(fn(), encoding="utf-8")
            print(f"  write {slug}"); created += 1
    print(f"\nDone: {created} created, {skipped} skipped. Total: {len(list(OUT.glob('*.md')))}")
