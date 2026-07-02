#!/usr/bin/env python3
"""
Wave 14 SEO content generator — TradieTools NZ
More trades for new cities: gasfitter, concreter, plasterer, fence installer,
solar installer, house washer, carpet layer, pest control
Run: python3 generate_wave14.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

NEW_CITIES = {
    "whangarei":    {"name":"Whangarei",    "region":"Northland",           "rate_adj":"broadly regional"},
    "queenstown":   {"name":"Queenstown",   "region":"Queenstown-Lakes",    "rate_adj":"among NZ's highest"},
    "invercargill": {"name":"Invercargill", "region":"Southland",           "rate_adj":"below national average"},
    "whanganui":    {"name":"Whanganui",    "region":"Manawatu-Whanganui",  "rate_adj":"broadly regional"},
    "gisborne":     {"name":"Gisborne",     "region":"Gisborne",            "rate_adj":"broadly regional"},
}

CITY_BLURB = {
    "whangarei":    "Whangarei is Northland's commercial hub — a subtropical, fast-growing city with strong construction demand driven by lifestyle migration from Auckland.",
    "queenstown":   "Queenstown is NZ's premium lifestyle and tourism destination. Tradies here command top rates and quality is expected from a discerning client base.",
    "invercargill": "Invercargill is NZ's southernmost city with a cold climate, competitive trade pricing, and strong demand for heating, insulation, and weathertightness work.",
    "whanganui":    "Whanganui is a growing heritage city with beautiful Victorian housing stock and an active renovation market.",
    "gisborne":     "Gisborne is NZ's most isolated city — warm, sunny, with a strong horticulture economy and an active construction market.",
}

# ── Gasfitter ─────────────────────────────────────────────────────────────────

GASFITTER_DATA = {
    "whangarei":    ("$92–$162/hr", "$68–$150", "Whangarei's subtropical climate means gas heating is less critical than in southern cities, but gas cooking and outdoor BBQ connections are popular. LPG is the primary fuel in most of Northland — natural gas reticulation is limited.", "Natural gas is not widely available in Whangarei — LPG cylinders and tanks are the standard option for gas appliances in most Northland properties."),
    "queenstown":   ("$120–$200/hr", "$90–$188", "Queenstown's cold winters drive strong demand for gas heating and continuous flow hot water. The alpine resort environment has a high proportion of gas appliances in holiday accommodation and premium homes.", "Natural gas is not available in Queenstown — LPG is the exclusive fuel for gas appliances. Bulk LPG tanks are common in larger properties and accommodation businesses."),
    "invercargill": ("$82–$148/hr", "$62–$135", "Invercargill's very cold winters make efficient heating essential — gas fires and gas heating are popular despite LPG's higher cost versus electricity. Gas cooking is prized for its precision control.", "Natural gas is available in parts of Invercargill via Vector Gas. LPG is used in areas without mains gas connection and is common in rural Southland."),
    "whanganui":    ("$85–$152/hr", "$64–$140", "Whanganui has steady residential gas demand. The city's older housing stock often has existing gas connections — upgrades to more efficient gas appliances are common renovation work.", "Natural gas is available in parts of Whanganui. LPG is used in outer suburbs and rural areas of the Manawatu-Whanganui region."),
    "gisborne":     ("$88–$158/hr", "$66–$145", "Gisborne's warm climate means gas heating demand is lower than in colder cities, but gas cooking is popular and outdoor entertaining gas connections are a common request. LPG is the standard fuel in the region.", "Natural gas is not widely available in Gisborne — LPG cylinders and tanks are the primary option for gas appliances across most of the region."),
}

def gasfitter_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    hourly, callout, local, gas_network = GASFITTER_DATA[city_key]
    return f"""---
title: "Gasfitters {city} 2026 — Gas Fitting Rates, Costs and What Requires a Licensed Gasfitter"
description: "Gasfitters {city} 2026 — {city} gasfitter rates, gas hob installation cost, gas hot water prices, LPG options, and how to find a licensed gasfitter near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["gasfitters {city}", "gasfitter {city}", "gas fitting {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what gasfitters charge in {city} in 2026.

## {city} Gasfitter Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Call-out fee | {callout} |
| Gas hob installation | $370–$820 |
| Gas oven installation | $470–$1,020 |
| Gas hot water cylinder (install) | $1,900–$3,900 |
| Continuous flow gas hot water | $1,700–$3,300 |
| Gas fire installation (flued) | $2,800–$6,500 |
| Gas BBQ point installation | $370–$820 |
| LPG to natural gas conversion | $440–$1,350 |
| Gas leak detection | $175–$460 |
| Annual gas appliance service | $135–$310 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Gas Supply

{gas_network}

## All Gasfitting is Restricted Work in NZ

All gasfitting must be done by a PGDB-registered gasfitter. Connecting any gas appliance, installing pipework, or modifying gas systems is restricted work requiring a compliance certificate. Verify at [pgdb.co.nz](https://www.pgdb.co.nz).

**Find {city} gasfitters:** [Gasfitters {city}](/trades/gasfitters/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Gas Fitting Cost NZ](/articles/gas-fitting-cost-nz/) | [Hot Water Cylinder Cost NZ](/articles/hot-water-cylinder-cost-nz/)*
"""


# ── Concreter ─────────────────────────────────────────────────────────────────

CONCRETER_DATA = {
    "whangarei":    ("$105–$215/m²", "$5,200–$16,500", "Whangarei's subtropical climate is generally good for concrete curing — warm temperatures accelerate strength gain. However, high rainfall can disrupt pour scheduling. Driveways, paths, and slab work are the most common residential jobs."),
    "queenstown":   ("$130–$250/m²", "$6,500–$20,000", "Queenstown's alpine environment and freeze-thaw conditions demand quality concrete mix design — air-entrained concrete is recommended to resist frost damage. Construction access can be challenging on Queenstown's steep sections."),
    "invercargill": ("$92–$198/m²", "$4,600–$14,800", "Invercargill's cold winters and frost mean concrete pouring is limited in the coldest months — scheduling around frost is important. Spring through autumn is the primary concreting season in Southland."),
    "whanganui":    ("$95–$205/m²", "$4,750–$15,400", "Whanganui's mild climate suits concrete work well. The flat river city has good access for concrete trucks and pump equipment. Driveways, shed slabs, and outdoor entertaining areas are popular jobs."),
    "gisborne":     ("$100–$210/m²", "$5,000–$16,000", "Gisborne's warm sunny climate is excellent for concrete work — ideal curing conditions mean fast strength gain. The region's seismic activity requires good foundation design, particularly for structural slabs."),
}

def concreter_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, driveway, local = CONCRETER_DATA[city_key]
    return f"""---
title: "Concreters {city} 2026 — Concrete Prices, Driveway Costs and What to Expect"
description: "Concreters {city} 2026 — {city} concrete driveway cost, slab pricing, path costs, decorative concrete rates, and how to find a reliable concreter near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["concreters {city}", "concreter {city}", "concrete cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what concreters charge in {city} in 2026.

## {city} Concreter Rates 2026

| Service | {city} typical cost |
|---|---|
| Concrete driveway (per m²) | {m2} |
| Standard driveway (40m²) | {driveway} |
| Concrete path (per m²) | $98–$200/m² |
| Concrete slab — shed/garage (per m²) | $105–$220/m² |
| Exposed aggregate (per m², premium) | $150–$300/m² |
| Coloured / stencilled concrete (per m²) | $160–$320/m² |
| Concrete steps (per step) | $290–$700 |
| Demolish + remove old concrete (per m²) | $40–$88/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Concrete Market

{local}

## Getting Quotes

- Get 2–3 written quotes specifying concrete strength (25–32 MPa for driveways)
- Confirm sub-base preparation is included (150mm compacted AP20 minimum)
- Minimum thickness: 100mm pedestrian, 125mm vehicles
- Ask what finish is included — broom, exposed aggregate, or coloured

**Find {city} concreters:** [Concreters {city}](/trades/concreters/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Concrete Driveway Cost NZ](/articles/concrete-driveway-cost-nz/) | [Asphalt Driveway Cost NZ](/articles/asphalt-driveway-cost-nz/)*
"""


# ── Plasterer ─────────────────────────────────────────────────────────────────

PLASTERER_DATA = {
    "whangarei":    ("$48–$92/m²", "$78–$145/hr", "Whangarei's subtropical humidity requires quality plaster and paint systems that resist moisture. The city's active renovation market keeps plasterers busy year-round, particularly as older homes are upgraded."),
    "queenstown":   ("$62–$115/m²", "$95–$175/hr", "Queenstown's premium construction market demands high-quality plastering — clients expect excellent finishes in luxury homes and accommodation. Plasterers here are often booked months in advance on large premium projects."),
    "invercargill": ("$42–$82/m²", "$68–$128/hr", "Invercargill's cold damp climate requires careful moisture management in plaster systems. Longer drying times in winter mean plasterers schedule around the cold months. Heritage home renovation is a significant part of the Invercargill plastering market."),
    "whanganui":    ("$44–$85/m²", "$70–$132/hr", "Whanganui's heritage housing stock creates demand for specialist plaster restoration — older homes often have original ornate plaster that requires careful repair and matching. Standard GIB stopping for new builds is also in demand."),
    "gisborne":     ("$46–$88/m²", "$72–$135/hr", "Gisborne's active residential construction market, boosted by post-cyclone rebuild activity, keeps plasterers busy. The warm climate provides good drying conditions for plaster work."),
}

def plasterer_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, hourly, local = PLASTERER_DATA[city_key]
    return f"""---
title: "Plasterers {city} 2026 — Plastering Costs, GIB Stopping Rates and What to Expect"
description: "Plasterers {city} 2026 — {city} plastering costs, GIB stopping rates, texture coat prices, and how to find a reliable plasterer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["plasterers {city}", "plasterer {city}", "plastering cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what plasterers charge in {city} in 2026.

## {city} Plasterer Rates 2026

| Service | {city} typical cost |
|---|---|
| GIB stopping (per m², 3 coat) | {m2} |
| Hourly rate | {hourly} |
| Texture coat / roughcast (per m²) | $28–$65/m² |
| Solid plaster (per m²) | $55–$110/m² |
| Patch repair (per hole / crack) | $95–$250 |
| Ceiling plastering (per m²) | $52–$98/m² |
| Cornice installation (per m linear) | $18–$42/m |
| Skim coat (existing walls, per m²) | $32–$72/m² |
| Full room re-plaster (per m²) | $65–$125/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Plastering Market

{local}

## Plasterer Types

**GIB stopper / dry liner:** Finishes plasterboard for paint — most common in NZ new builds and renovations. Applies stopping compound in multiple coats and sands smooth.

**Solid plasterer:** Works with traditional cement and lime plaster on masonry, brick, or for exterior render. Heritage restoration specialist.

**Texture coat applicator:** Applies decorative exterior textures (roughcast, plaster systems like Rockcote, Dryvit).

**Find {city} plasterers:** [Plasterers {city}](/trades/plasterers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Builders {city}](/articles/builder-{city_key}-nz/) | [Painters {city}](/articles/painter-{city_key}-nz/)*
"""


# ── Fence Installer ───────────────────────────────────────────────────────────

FENCE_DATA = {
    "whangarei":    ("$185–$390/m", "$100–$228/m", "Whangarei's subtropical climate and coastal exposure require treated timber and corrosion-resistant fixings. Salt air from the Whangarei Harbour accelerates rust on steel components — use stainless or hot-dipped galvanised fixings."),
    "queenstown":   ("$220–$450/m", "$125–$265/m", "Queenstown's alpine environment means fence designs must handle snow load and strong winds. Quality materials and robust installation are critical — the freeze-thaw cycle can work fence posts loose over time."),
    "invercargill": ("$168–$358/m", "$88–$210/m", "Invercargill's driving southerly winds make wind-load design important. Concrete posts are popular in Southland for their durability in cold, wet conditions. Treated timber must be H4 or better for in-ground use in Invercargill's wet soil."),
    "whanganui":    ("$172–$368/m", "$91–$215/m", "Whanganui's mild climate suits most fencing materials well. The heritage property market values traditional-looking timber fencing that complements the city's Victorian character."),
    "gisborne":     ("$178–$378/m", "$95–$220/m", "Gisborne's warm climate and post-cyclone rebuild activity have driven strong demand for new fencing. Storm-damaged fencing replacement was a major category of work following Cyclone Gabrielle."),
}

def fence_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    timber, post_rail, local = FENCE_DATA[city_key]
    return f"""---
title: "Fence Installers {city} 2026 — Fencing Costs, Materials and What to Expect"
description: "Fence installers {city} 2026 — {city} fencing costs, timber vs Colorbond prices, consent requirements, and how to find a reliable fence installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["fence installers {city}", "fencing {city}", "fence cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what fence installers charge in {city} in 2026.

## {city} Fencing Costs 2026

| Service | {city} typical cost |
|---|---|
| Timber privacy fence (1.8m, per m linear) | {timber} |
| Post and rail fence (per m linear) | {post_rail} |
| Colorbond / metal fence (per m linear) | $225–$430/m |
| Picket fence (1.0m, per m linear) | $145–$290/m |
| Pool fence (compliant, per m linear) | $390–$970/m |
| Fence removal + disposal (per m linear) | $26–$68/m |
| Gate — timber (supply + fit) | $490–$1,250 |
| Gate — automated sliding (supply + fit) | $2,900–$7,800 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Fencing Market

{local}

## Consent Requirements in {city}

Boundary fences up to 2.0m generally don't require consent in most residential zones. Pool fences must comply with NZ Building Code (Clause F9) regardless of height. Front boundary fences in some zones have height restrictions. Always check with {NEW_CITIES[city_key]["region"]} Council for your specific zone.

**Find {city} fence installers:** [Fence Installers {city}](/trades/fencing/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Fencing Cost NZ](/articles/fencing-cost-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/)*
"""


# ── Solar Installer ───────────────────────────────────────────────────────────

SOLAR_DATA = {
    "whangarei":    ("$8,500–$14,000", "$13,000–$21,500", "Whangarei is one of NZ's sunniest cities — Northland consistently records high sunshine hours. Average 4.8–5.5 peak sun hours per day makes solar one of the best investments for Whangarei homeowners. The long summer days in subtropical Northland deliver outstanding solar yield."),
    "queenstown":   ("$8,800–$14,500", "$13,500–$22,000", "Queenstown's alpine location gives good summer solar yield, but winter is significantly weaker due to low sun angles and short days. Battery storage is particularly valuable in Queenstown to capture summer surplus and manage winter shortfall. Annual yield is lower than northern NZ cities."),
    "invercargill": ("$8,200–$13,500", "$12,500–$20,500", "Invercargill has NZ's lowest solar yield — the far south location, frequent cloud cover, and short winter days make solar less effective than in northern NZ. However, rising electricity prices still make solar worthwhile, particularly with battery storage to maximise self-consumption."),
    "whanganui":    ("$8,200–$13,500", "$12,500–$20,500", "Whanganui has moderate sunshine hours — good for solar, with the west coast location giving reasonable performance. A 6.6kW system typically generates 8,500–10,000 kWh/year in Whanganui."),
    "gisborne":     ("$8,500–$14,000", "$13,000–$21,500", "Gisborne is one of NZ's sunniest cities — it's the first city in the world to see the sun each day. Excellent solar resource with 5.0–5.8 peak sun hours per day makes Gisborne one of NZ's best solar locations. Cyclone resilience (Cyclone Gabrielle 2023) has increased interest in battery storage alongside solar."),
}

def solar_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    small, large, local = SOLAR_DATA[city_key]
    return f"""---
title: "Solar Installers {city} 2026 — Solar Panel Costs, Payback and What to Expect"
description: "Solar installers {city} 2026 — {city} solar panel installation costs, system sizing, battery storage, payback period, and how to find a reliable solar installer near you."
image: "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["solar installers {city}", "solar panels {city}", "solar cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what solar installation costs in {city} in 2026.

## {city} Solar Installation Costs 2026

| System size | {city} typical cost (supply + install) |
|---|---|
| 3kW system (small home) | $6,500–$10,500 |
| 6.6kW system (standard home) | {small} |
| 10kW system (large home / EV charging) | {large} |
| Battery storage — 10kWh (add-on) | $9,000–$14,000 |
| Solar hot water (evacuated tube) | $4,500–$8,500 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Solar Performance

{local}

## Payback in {city}

At NZ electricity prices (~$0.30–$0.38/kWh), a 6.6kW system typically pays back in:
- **No battery:** 6–10 years
- **With battery:** 9–14 years

Solar adds to property value and payback improves as electricity prices rise.

## Choosing a Solar Installer

- Look for SEANZ members (Sustainable Electricity Association of NZ)
- Ask for a site-specific production estimate based on your actual roof
- Compare warranties: panels (25yr), inverter (10–12yr), workmanship (5–10yr)
- Get at least 2–3 quotes

**Find {city} solar installers:** [Solar Installers {city}](/trades/solar-installers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Solar Panel Cost NZ](/articles/solar-panel-cost-nz/) | [EV Charger Installation {city}](/articles/ev-charger-installation-{city_key}-nz/)*
"""


# ── House Washer ──────────────────────────────────────────────────────────────

HOUSEWASH_DATA = {
    "whangarei":    ("$290–$600", "$390–$780", "Whangarei's subtropical humidity and warmth accelerate mould and algae growth on exterior surfaces — faster than almost any other NZ city. Annual house washing is strongly recommended for Northland homes. South-facing walls and shaded areas grow mould year-round."),
    "queenstown":   ("$320–$650", "$420–$850", "Queenstown's alpine environment means algae and lichen grow on roofs and walls in the wetter seasons. Pre-paint washing is essential. The premium property market expects well-maintained exteriors — regular house washing is standard practice in Queenstown."),
    "invercargill": ("$265–$545", "$355–$720", "Invercargill's high rainfall and damp climate encourages mould on exterior surfaces, particularly on south and west-facing walls exposed to the prevailing southerly. Annual house washing extends paint life significantly in Southland's wet conditions."),
    "whanganui":    ("$270–$555", "$360–$730", "Whanganui's moderate climate means mould growth is slower than in wetter cities, but annual or bi-annual washing is still recommended. The heritage property market values well-presented exteriors."),
    "gisborne":     ("$275–$560", "$365–$740", "Gisborne's warm sunny climate slows mould growth compared to wetter cities. Post-cyclone (Gabrielle 2023) cleaning was in huge demand as mud and debris coated many properties. House washing and exterior cleaning services remain busy in the ongoing rebuild."),
}

def housewash_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    standard, large, local = HOUSEWASH_DATA[city_key]
    return f"""---
title: "House Washers {city} 2026 — House Washing Costs, Soft Wash vs Pressure Wash"
description: "House washers {city} 2026 — {city} house washing costs, soft wash vs pressure wash, roof treatment prices, and how to find a reliable house washing company near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["house washers {city}", "house washing {city}", "house wash cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what house washing costs in {city} in 2026.

## {city} House Washing Costs 2026

| Service | {city} typical cost |
|---|---|
| Standard house wash (3-bed) | {standard} |
| Large house wash (4–5 bed) | {large} |
| Roof treatment (moss / lichen) | $285–$700 |
| Driveway / path pressure wash | $125–$290 |
| Deck wash (per m²) | $4–$12/m² |
| Gutter clean (per linear metre) | $6–$15/m |
| Full exterior package (house + roof + drive) | $660–$1,450 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} House Washing Market

{local}

## Soft Wash vs Pressure Wash

**Soft wash** (low pressure + biocide): Kills mould at the root, prevents quick regrowth. Lasts 2–4 years. Safe on weatherboards, painted surfaces, and roofs. Recommended for house exteriors.

**High pressure**: Best for concrete driveways, paths, and decks. Too aggressive for most painted or clad surfaces.

**Find {city} house washers:** [House Washers {city}](/trades/house-washing/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [House Washing Cost NZ](/articles/house-washing-cost-nz/) | [Painters {city}](/articles/painter-{city_key}-nz/)*
"""


# ── Carpet Layer ──────────────────────────────────────────────────────────────

CARPET_DATA = {
    "whangarei":    ("$40–$88/m²", "$68–$145/m²", "Whangarei's subtropical climate means natural fibres can be affected by humidity — synthetic carpet with good moisture resistance performs well. Wool carpet is still popular in Northland homes for its comfort and durability."),
    "queenstown":   ("$48–$98/m²", "$80–$165/m²", "Queenstown's cold winters make warm carpet a popular choice — underfoot warmth matters in alpine conditions. Luxury wool carpet is the norm in Queenstown's premium accommodation and residential market."),
    "invercargill": ("$36–$80/m²", "$60–$135/m²", "Invercargill's cold winters make carpet popular for thermal comfort. The city's rental market drives ongoing carpet replacement demand — budget synthetic options are common in investment properties."),
    "whanganui":    ("$37–$82/m²", "$62–$138/m²", "Whanganui's mild climate suits a range of carpet types. Heritage homes often have carpet over beautiful timber floors — many renovation projects now reveal and restore these floors rather than re-carpet."),
    "gisborne":     ("$38–$84/m²", "$63–$140/m²", "Gisborne's warm climate means carpet is less about warmth and more about comfort and aesthetics. The post-cyclone rebuild drove significant carpet replacement as flood-damaged flooring was removed across many properties."),
}

def carpet_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    mid, premium, local = CARPET_DATA[city_key]
    return f"""---
title: "Carpet Layers {city} 2026 — Carpet Costs, Types and What to Expect"
description: "Carpet layers {city} 2026 — {city} carpet laying costs, wool vs synthetic pricing, underlay costs, and how to find a reliable carpet layer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["carpet layers {city}", "carpet layer {city}", "carpet cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what carpet layers charge in {city} in 2026.

## {city} Carpet Laying Costs 2026

| Service | {city} typical cost |
|---|---|
| Mid-range carpet (supply + fit, per m²) | {mid} |
| Premium / wool carpet (supply + fit, per m²) | {premium} |
| Budget synthetic (supply + fit, per m²) | $36–$62/m² |
| Underlay — standard (per m²) | $12–$22/m² |
| Underlay — premium (per m²) | $18–$38/m² |
| Carpet removal + disposal (per m²) | $8–$18/m² |
| Full 3-bed home re-carpet (mid-range) | $4,200–$9,000 |
| Carpet re-stretching (per room) | $78–$175 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Carpet Market

{local}

## Carpet Types for {city}

**Nylon:** Most durable synthetic, excellent stain resistance, best for high traffic. **Polyester:** Soft and affordable. **Wool:** Premium NZ product, 2–3× the cost but lasts 20–30 years. **Underlay:** Don't skimp — quality underlay significantly extends carpet life and comfort.

**Find {city} carpet layers:** [Carpet Layers {city}](/trades/carpet-layers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Carpet Cost NZ](/articles/carpet-cost-nz/) | [Floor Sanders {city}](/articles/floor-sander-{city_key}-nz/)*
"""


# ── Pest Control ──────────────────────────────────────────────────────────────

PEST_DATA = {
    "whangarei":    ("$175–$370", "$265–$640", "Whangarei's subtropical climate supports a wider range of pests than most NZ cities — cockroaches, ants, wasps, and rodents are all common. The warm humid conditions suit insect breeding year-round. Northland's bush surroundings bring additional pressure from possums, rats, and wasps."),
    "queenstown":   ("$195–$410", "$295–$690", "Queenstown's alpine environment limits the pest range but rodents — particularly Norway rats — are common in the ski resort environment. Stoats and weasels are also a consideration near the bush margins. Wasps are a significant nuisance in summer."),
    "invercargill": ("$158–$330", "$235–$560", "Invercargill's cold climate limits insect pests but rodents are active year-round — particularly in the cold months when they seek warmth indoors. Bed bugs in the student accommodation sector and fleas in rental properties are common call-outs."),
    "whanganui":    ("$160–$335", "$240–$570", "Whanganui's mild climate suits a range of pests. Rodents, wasps, and ants are the most common residential call-outs. The river environment brings occasional issues with water-associated pests."),
    "gisborne":     ("$162–$340", "$242–$575", "Gisborne's warm sunny climate suits insects well. Wasps, ants, cockroaches, and rodents are common. The horticulture sector creates specific pest challenges — orchard pests can spread into residential areas. Post-cyclone conditions (2023) temporarily increased rodent populations across Gisborne."),
}

def pest_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    callout, quarterly, local = PEST_DATA[city_key]
    return f"""---
title: "Pest Control {city} 2026 — Pest Control Costs, Common Pests and What to Expect"
description: "Pest control {city} 2026 — {city} pest control costs, rodent treatment prices, cockroach and wasp extermination rates, and how to find a reliable pest controller near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["pest control {city}", "pest controller {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what pest control costs in {city} in 2026.

## {city} Pest Control Costs 2026

| Service | {city} typical cost |
|---|---|
| Inspection / assessment | $95–$215 |
| Rodent treatment (3-bed home) | {callout} |
| Cockroach treatment (3-bed home) | $172–$368 |
| Ant treatment | $152–$308 |
| Wasp nest removal | $122–$268 |
| Flea treatment (3-bed home) | $172–$368 |
| Borer treatment (per m²) | $11–$27/m² |
| Quarterly maintenance contract | {quarterly}/year |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Pest Situation

{local}

## Common {city} Pests

**Rodents:** Most common call-out — especially in autumn as temperatures drop. Signs: droppings, gnaw marks, scratching sounds at night. **Wasps:** Aggressive NZ German wasp — large nests must be treated professionally at night. **Cockroaches:** Multiple visits needed to break the egg cycle. **Borer:** Treat in summer when larvae are near the surface.

Pest controllers applying restricted pesticides must hold a GROWSAFE certificate.

**Find {city} pest controllers:** [Pest Control {city}](/trades/pest-control/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Pest Control Cost NZ](/articles/pest-control-cost-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

for ck in NEW_CITIES:
    ARTICLES += [
        (f"gasfitter-{ck}-nz",            lambda k=ck: gasfitter_article(k)),
        (f"concreter-{ck}-nz",            lambda k=ck: concreter_article(k)),
        (f"plasterer-{ck}-nz",            lambda k=ck: plasterer_article(k)),
        (f"fence-installer-{ck}-nz",      lambda k=ck: fence_article(k)),
        (f"solar-installer-{ck}-nz",      lambda k=ck: solar_article(k)),
        (f"house-washer-{ck}-nz",         lambda k=ck: housewash_article(k)),
        (f"carpet-layer-{ck}-nz",         lambda k=ck: carpet_article(k)),
        (f"pest-control-{ck}-nz",         lambda k=ck: pest_article(k)),
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
