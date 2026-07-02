#!/usr/bin/env python3
"""
Wave 13 SEO content generator — TradieTools NZ
Expand new cities (Whangarei, Queenstown, Invercargill, Whanganui, Gisborne)
Additional trades: tiler, landscaper, heat pump, insulation, arborist, drainlayer, locksmith, carpenter
Run: python3 generate_wave13.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

NEW_CITIES = {
    "whangarei":    {"name":"Whangarei",    "region":"Northland",           "rate_adj":"broadly regional"},
    "queenstown":   {"name":"Queenstown",   "region":"Queenstown-Lakes",    "rate_adj":"among NZ's highest — premium rates reflect the tourism and construction demand"},
    "invercargill": {"name":"Invercargill", "region":"Southland",           "rate_adj":"below national average"},
    "whanganui":    {"name":"Whanganui",    "region":"Manawatu-Whanganui",  "rate_adj":"broadly regional"},
    "gisborne":     {"name":"Gisborne",     "region":"Gisborne",            "rate_adj":"broadly regional"},
}

CITY_BLURB = {
    "whangarei":    "Whangarei is Northland's commercial hub with a subtropical climate, strong lifestyle appeal, and active construction market driven by Aucklanders relocating north.",
    "queenstown":   "Queenstown is NZ's premier lifestyle and tourism destination. Tradies here command premium rates — quality and reliability are expected from a demanding client base.",
    "invercargill": "Invercargill is NZ's southernmost city with a cold climate, competitive trade pricing, and steady residential demand for heating, insulation, and weathertightness work.",
    "whanganui":    "Whanganui is a growing heritage city with beautiful Victorian stock and an active renovation market as new residents arrive from larger centres.",
    "gisborne":     "Gisborne is NZ's most isolated city — sunny, warm, and with a strong wine and horticulture economy driving both residential and commercial construction.",
}

CLIMATE = {
    "whangarei":    "subtropical, warm and humid with high rainfall",
    "queenstown":   "alpine, cold winters with snow, warm dry summers",
    "invercargill": "cold, wet, and windy — one of NZ's coldest cities",
    "whanganui":    "mild, moderate rainfall with warm summers",
    "gisborne":     "warm and sunny — one of NZ's sunniest and warmest regions",
}

# ── Tiler ─────────────────────────────────────────────────────────────────────

TILER_RATES = {
    "whangarei":    ("$90–$165/m²", "$68–$148"),
    "queenstown":   ("$120–$200/m²", "$90–$190"),
    "invercargill": ("$78–$148/m²", "$58–$132"),
    "whanganui":    ("$82–$155/m²", "$62–$138"),
    "gisborne":     ("$85–$158/m²", "$64–$142"),
}

def tiler_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, callout = TILER_RATES[city_key]
    blurb = CITY_BLURB[city_key]
    return f"""---
title: "Tilers {city} 2026 — Tiling Rates, Costs and What to Expect"
description: "Tilers {city} 2026 — {city} tiler rates, floor and wall tiling costs, bathroom tiling prices, and how to find a reliable tiler near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["tilers {city}", "tiler {city}", "tiling cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{blurb} Here's what tilers charge in {city} in 2026.

## {city} Tiler Rates 2026

| Service | {city} typical cost |
|---|---|
| Floor tiling (per m², supply + install) | {m2} |
| Wall tiling (per m², supply + install) | $85–$165/m² |
| Bathroom tiling (floor + walls, full) | $3,200–$8,000 |
| Shower cubicle (supply + install) | $2,000–$5,200 |
| Kitchen splashback (per m²) | $120–$270/m² |
| Outdoor / alfresco tiling (per m²) | $110–$220/m² |
| Tile removal (per m²) | $22–$52/m² |
| Grout cleaning / regrouting (per m²) | $42–$90/m² |
| Call-out / minimum charge | {callout} |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Tiling Market

{blurb}

## Waterproofing in Wet Areas

All shower and bathroom tiling must be done over a waterproofed substrate — tiles alone don't waterproof. NZ Building Code requires a compliant waterproof membrane in wet areas to minimum 1,800mm height. A good {city} tiler will either waterproof themselves or coordinate with a builder to ensure compliance before tiling begins.

## Tile Selection Tips

- **Shower floor:** Choose R10+ slip-rated matt or textured tiles
- **Large format (600mm+):** Stunning but needs a very flat substrate and adds labour cost
- **Rectified tiles:** Machine-cut edges allow 1–2mm grout lines for a seamless finish

**Find {city} tilers:** [Tilers {city}](/trades/tilers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Bathroom Tiling Cost NZ](/articles/bathroom-tiling-cost-nz/) | [Bathroom Renovation {city}](/articles/bathroom-renovator-{city_key}-nz/)*
"""


# ── Landscaper ────────────────────────────────────────────────────────────────

LANDSCAPER_DATA = {
    "whangarei":    ("$75–$145/hr", "Whangarei's subtropical climate grows lush gardens rapidly — fast-growing species like hebes, flaxes, and natives thrive. The warm climate suits tropical plants rarely possible further south. Regular maintenance is key as growth rates are high year-round."),
    "queenstown":   ("$95–$175/hr", "Queenstown's alpine environment demands careful plant selection — frost-hardy species, wind-resistant plants, and designs that handle snow load on structures. The luxury market expects premium landscaping to match premium properties."),
    "invercargill": ("$68–$128/hr", "Invercargill's cold climate limits plant selection but creates beautiful cool-season gardens. Hardy perennials, conifers, and shelter belts that protect from the southerly wind are important design elements."),
    "whanganui":    ("$70–$132/hr", "Whanganui's mild climate and fertile soils suit a wide range of plants. The river city's heritage character inspires traditional cottage-style gardens alongside contemporary outdoor living spaces."),
    "gisborne":     ("$72–$135/hr", "Gisborne's warm sunny climate is excellent for Mediterranean-style planting, citrus, and edible gardens. The wine region's aesthetic influences residential landscaping — outdoor entertaining and lush productive gardens are popular."),
}

def landscaper_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    hourly, local = LANDSCAPER_DATA[city_key]
    return f"""---
title: "Landscapers {city} 2026 — Landscaping Costs, Garden Design and What to Expect"
description: "Landscapers {city} 2026 — {city} landscaping costs, garden design prices, retaining wall quotes, lawn installation rates, and how to find a reliable landscaper near you."
image: "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["landscapers {city}", "landscaper {city}", "landscaping cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what landscapers charge in {city} in 2026.

## {city} Landscaping Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate (qualified landscaper) | {hourly} |
| Garden design (small section) | $700–$2,200 |
| Full garden makeover (small-medium) | $8,500–$30,000 |
| Lawn installation (turf, per m²) | $22–$55/m² |
| Retaining wall — timber sleeper (per m²) | $360–$850/m² |
| Retaining wall — concrete block (per m²) | $560–$1,300/m² |
| Paving / outdoor tiles (per m²) | $90–$280/m² |
| Planting package (per m²) | $70–$185/m² |
| Irrigation system (small section) | $1,800–$5,500 |
| Tree removal (small–medium) | $460–$1,800 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Landscaping Market

{local}

## Getting the Best Result

- Get a written design plan before work begins
- Confirm what's included: plants, irrigation, consent for retaining walls over 1.5m
- Ask for a portfolio of recent {city} work
- Members of Landscaping New Zealand (LNZ) follow professional standards

**Find {city} landscapers:** [Landscapers {city}](/trades/landscapers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Landscaping Cost NZ](/articles/landscaping-cost-nz/) | [Retaining Wall Cost NZ](/articles/retaining-wall-cost-nz/) | [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/)*
"""


# ── Heat Pump Installer ────────────────────────────────────────────────────────

HEATPUMP_DATA = {
    "whangarei":    ("$3,100–$5,500", "$5,200–$10,500", "Whangarei's subtropical climate means cooling demand in summer is significant — a reverse-cycle heat pump provides both efficient heating in winter and cooling on Northland's hot summer days. The combination makes heat pumps an ideal year-round solution."),
    "queenstown":   ("$3,400–$6,200", "$5,800–$12,000", "Queenstown's cold alpine winters make heating critical — a quality heat pump is the most energy-efficient option. Alpine-rated heat pumps (capable of operating below -15°C) are recommended for Queenstown's coldest nights. Premium brands perform best in extreme cold."),
    "invercargill": ("$3,000–$5,400", "$5,000–$10,200", "Invercargill's very cold winters make heat pump selection important. Look for a heat pump with a cold climate rating — standard units lose efficiency below -5°C, which Invercargill regularly reaches. Mitsubishi Electric's Hyper Heat and Daikin's Altherma series perform well in Southland winters."),
    "whanganui":    ("$3,000–$5,300", "$5,000–$10,000", "Whanganui's mild climate means a standard heat pump works well year-round. Heating demand is moderate by NZ standards, making heat pumps a cost-effective choice for both new and existing Whanganui homes."),
    "gisborne":     ("$3,000–$5,300", "$5,000–$10,000", "Gisborne's warm sunny climate means heating demand is lower than many NZ cities, but a heat pump still makes sense for cool winter nights and air quality. Cooling in Gisborne's hot summers is an added benefit."),
}

def heatpump_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    single, multi, local = HEATPUMP_DATA[city_key]
    return f"""---
title: "Heat Pump Installers {city} 2026 — Heat Pump Costs, Brands and What to Expect"
description: "Heat pump installers {city} 2026 — {city} heat pump installation costs, single vs multi-split pricing, best brands for {city}'s climate, and how to find a reliable installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["heat pump installers {city}", "heat pump cost {city}", "heat pump installation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what heat pump installation costs in {city} in 2026.

## {city} Heat Pump Installation Costs 2026

| Service | {city} typical cost |
|---|---|
| Single split system (supply + install) | {single} |
| Multi-split 2 indoor units (supply + install) | {multi} |
| Ducted heat pump (whole home) | $12,000–$28,000 |
| Heat pump service / regas | $170–$460 |
| Relocate existing unit | $460–$1,050 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Heat Pump Selection

{local}

## Sizing for {city}

| Room size | Recommended kW |
|---|---|
| Bedroom / small room (<15m²) | 2.0–2.5 kW |
| Medium living (15–30m²) | 2.5–4.0 kW |
| Large open plan (30–60m²) | 5.0–7.0 kW |
| Very large (60m²+) | 7.0–12.0 kW |

A good installer will assess your room, insulation, and window area before recommending a size.

**Find {city} heat pump installers:** [Heat Pump Installers {city}](/trades/heat-pump-installation/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Heat Pump Cost NZ](/articles/heat-pump-cost-nz/) | [Insulation Installers {city}](/articles/insulation-installer-{city_key}-nz/)*
"""


# ── Insulation Installer ──────────────────────────────────────────────────────

INSULATION_DATA = {
    "whangarei":    ("$2,100–$5,200", "$1,400–$3,600", "Whangarei's subtropical humidity makes good insulation important for moisture management as much as temperature. Ceiling insulation reduces summer heat gain — critical in Northland's hot summers. Warmer Kiwi Homes grants are available to eligible Whangarei homeowners."),
    "queenstown":   ("$2,400–$5,800", "$1,600–$4,000", "Queenstown's cold alpine winters make insulation one of the highest-ROI investments. Homes with poor insulation are extremely expensive to heat in Queenstown's winters. The alpine climate demands higher R-values than most NZ homes — aim for R4.0+ in ceilings."),
    "invercargill": ("$2,000–$5,000", "$1,350–$3,500", "Invercargill has some of NZ's highest insulation demand — the cold climate makes it one of the best returns on investment available to homeowners. Warmer Kiwi Homes grants are particularly well-utilised in Southland given the cold conditions."),
    "whanganui":    ("$2,000–$5,000", "$1,350–$3,500", "Whanganui's older housing stock has significant uninsulated properties — the heritage homes that make the city beautiful can also be cold and draughty. Ceiling and underfloor insulation upgrades are among the most cost-effective improvements for Whanganui homeowners."),
    "gisborne":     ("$2,000–$5,000", "$1,350–$3,500", "Gisborne's warm climate means insulation is less urgent than in colder cities, but it still pays off — keeping summer heat out is as valuable as keeping winter warmth in. Warmer Kiwi Homes grants are available to eligible Gisborne homeowners."),
}

def insulation_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    ceiling, underfloor, local = INSULATION_DATA[city_key]
    return f"""---
title: "Insulation Installers {city} 2026 — Insulation Costs, Grants and What to Expect"
description: "Insulation installers {city} 2026 — {city} ceiling and underfloor insulation costs, Warmer Kiwi Homes grants, and how to find a reliable insulation installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["insulation installers {city}", "insulation cost {city}", "ceiling insulation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what insulation costs in {city} in 2026.

## {city} Insulation Costs 2026

| Service | {city} typical cost |
|---|---|
| Ceiling insulation (full house, 3-bed) | {ceiling} |
| Underfloor insulation (full house, 3-bed) | {underfloor} |
| Ceiling insulation (per m²) | $17–$46/m² |
| Underfloor insulation — batts (per m²) | $11–$30/m² |
| Underfloor insulation — foil (per m²) | $7–$20/m² |
| Wall insulation — retrofit (per m²) | $42–$105/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Insulation Market

{local}

## Warmer Kiwi Homes Grants

You may qualify for a government subsidy covering up to 80% of insulation costs (90% for Community Services Card holders) if:
- You own and live in your home
- Your home was built before 2008

Approved {city} installers can check your eligibility and manage the grant application. Check eligibility at [energywise.govt.nz](https://www.energywise.govt.nz/at-home/warmer-kiwi-homes/)

**Find {city} insulation installers:** [Insulation Installers {city}](/trades/insulation-installers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Insulation Cost NZ](/articles/insulation-cost-nz/) | [Heat Pump Installers {city}](/articles/heat-pump-installer-{city_key}-nz/)*
"""


# ── Arborist ──────────────────────────────────────────────────────────────────

ARBORIST_DATA = {
    "whangarei":    ("$280–$680", "$1,200–$4,500", "Whangarei's subtropical climate produces fast-growing trees — palms, pohutukawa, and large tropical species are common. Annual tree maintenance is important in Northland as growth rates are high and storm damage risk is elevated during cyclone season."),
    "queenstown":   ("$320–$780", "$1,500–$5,500", "Queenstown's alpine environment features poplars, willows, and native beech forest. Snow and ice loading on trees is a real hazard in winter — arborist inspections before winter are worthwhile for large trees near structures."),
    "invercargill": ("$260–$620", "$1,100–$4,000", "Invercargill's windy southerly climate stresses trees significantly. Regular pruning to maintain wind-resistant form is important. Sitka spruce, macrocarpa, and shelter-belt species are common in Southland."),
    "whanganui":    ("$265–$630", "$1,100–$4,000", "Whanganui's river environment features large mature trees — willows along the river, mature oaks, and established native bush in many properties. The city's heritage character means tree removal often has amenity and community implications."),
    "gisborne":     ("$270–$640", "$1,100–$4,200", "Gisborne's warm climate produces fast-growing trees. The region's exposure to tropical cyclones (Cyclone Gabrielle 2023) highlighted the importance of proactive tree maintenance — weakened trees caused significant property damage in the storm."),
}

def arborist_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    prune, removal, local = ARBORIST_DATA[city_key]
    return f"""---
title: "Arborists {city} 2026 — Tree Removal, Pruning Costs and What to Expect"
description: "Arborists {city} 2026 — {city} arborist rates, tree removal costs, tree pruning prices, and how to find a qualified arborist near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["arborists {city}", "arborist {city}", "tree removal {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what arborists charge in {city} in 2026.

## {city} Arborist Rates 2026

| Service | {city} typical cost |
|---|---|
| Tree pruning — small tree | {prune} |
| Tree pruning — large tree | $580–$1,800 |
| Tree removal — small (under 5m) | $480–$1,200 |
| Tree removal — medium (5–10m) | {removal} |
| Tree removal — large (10m+) | $2,500–$8,000+ |
| Stump grinding (per stump) | $180–$480 |
| Emergency tree work (storm damage) | $380–$1,500+ |
| Tree health assessment / report | $180–$480 |
| Mulching (per m³) | $45–$120 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}. Size, access, and proximity to structures are the biggest cost variables.*

## {city} Tree Market

{local}

## Do I Need a Consent to Remove a Tree in {city}?

Tree removal rules vary by {NEW_CITIES[city_key]["region"]} Council zone and whether trees are listed or in a notable tree schedule. **Always check with {NEW_CITIES[city_key]["region"]} Council before removing trees** — fines for removing protected trees can be substantial. A qualified arborist will know local rules and can advise.

**Certified arborists:** Look for NZ Arboriculture Association (NZAA) members or ISA (International Society of Arboriculture) certified arborists for complex or high-risk work.

**Find {city} arborists:** [Arborists {city}](/trades/arborists/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Tree Removal Cost NZ](/articles/tree-removal-cost-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/)*
"""


# ── Drainlayer ────────────────────────────────────────────────────────────────

DRAIN_DATA = {
    "whangarei":    ("$92–$162/hr", "$68–$150", "Whangarei's high rainfall and clay soils in many areas create drainage challenges. The subtropical environment accelerates root growth in older clay drain pipes — camera inspections before purchasing older Whangarei properties are strongly recommended."),
    "queenstown":   ("$118–$198/hr", "$88–$188", "Queenstown's rocky alpine geology can make drain trenching expensive — rock breaking adds cost. The rapid population growth has stressed existing infrastructure in some areas, making new connections more complex."),
    "invercargill": ("$82–$148/hr", "$62–$135", "Invercargill's flat terrain can cause slow gravity drainage — careful system design is important. The city's older suburbs have original clay drain pipes that are reaching end of life, and root intrusion from established trees is common."),
    "whanganui":    ("$84–$152/hr", "$64–$140", "Whanganui's older inner-city housing has original clay drains that are increasingly failing. The river proximity also means stormwater management requires careful attention to prevent flooding."),
    "gisborne":     ("$86–$155/hr", "$65–$142", "Gisborne's experience with Cyclone Gabrielle (2023) highlighted the importance of robust stormwater drainage. Many properties had flood damage — upgrading stormwater systems is a priority for many Gisborne homeowners."),
}

def drainlayer_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    hourly, callout, local = DRAIN_DATA[city_key]
    return f"""---
title: "Drainlayers {city} 2026 — Drain Costs, Sewer Repair Prices and What to Expect"
description: "Drainlayers {city} 2026 — {city} drainlayer rates, sewer repair costs, drain camera inspection prices, and how to find a licensed drainlayer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["drainlayers {city}", "drainlayer {city}", "drain cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what drainlayers charge in {city} in 2026.

## {city} Drainlayer Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee | {callout} |
| Hourly rate | {hourly} |
| Drain camera inspection | $230–$470 |
| High-pressure water jetting | $185–$460 |
| Root cutting / clearing | $270–$660 |
| Drain repair (per metre) | $370–$860/m |
| Drain replacement (open cut, per metre) | $470–$1,100/m |
| Sewer lateral connection (new) | $2,100–$6,200 |
| Stormwater connection (new) | $1,800–$5,500 |
| Pre-purchase drainage inspection | $360–$820 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Drainage Situation

{local}

## PGDB-Licensed Drainlayers

All work connecting to the public sewer or stormwater network must be done by a PGDB-registered drainlayer. Verify at [pgdb.co.nz](https://www.pgdb.co.nz).

**Slow drains, gurgling pipes, wet patches in the lawn, or sewage smells** are all signs of drain problems. A camera inspection ($230–$470) diagnoses the issue before digging begins.

**Find {city} drainlayers:** [Drainlayers {city}](/trades/drainlayers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Blocked Drain Cost NZ](/articles/blocked-drain-cost-nz/) | [Plumbers {city}](/articles/plumber-{city_key}-nz/)*
"""


# ── Locksmith ─────────────────────────────────────────────────────────────────

LOCK_DATA = {
    "whangarei":    ("$128–$272", "$195–$470"),
    "queenstown":   ("$155–$320", "$240–$580"),
    "invercargill": ("$115–$255", "$175–$430"),
    "whanganui":    ("$118–$260", "$178–$440"),
    "gisborne":     ("$120–$265", "$180–$450"),
}

def locksmith_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    callout, emergency = LOCK_DATA[city_key]
    blurb = CITY_BLURB[city_key]
    return f"""---
title: "Locksmiths {city} 2026 — Locksmith Costs, Lockout Prices and What to Expect"
description: "Locksmiths {city} 2026 — {city} locksmith call-out rates, emergency lockout costs, lock replacement prices, and how to find a reliable locksmith near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["locksmiths {city}", "locksmith {city}", "locksmith cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{blurb} Here's what locksmiths charge in {city} in 2026.

## {city} Locksmith Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (standard hours) | {callout} |
| Emergency lockout (after hours) | {emergency} |
| Lock picking / non-destructive entry | $125–$270 |
| Lock replacement — deadbolt (supply + fit) | $210–$500 |
| Lock replacement — knob/lever (supply + fit) | $175–$400 |
| Rekeying (per lock) | $60–$145 |
| Master key system (per lock) | $80–$190 |
| Key cutting (per key) | $7–$32 |
| Safe opening | $240–$620 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Rekeying vs Replacing

**Rekey ($60–$145/lock):** Change the pins so old keys no longer work. Best after moving into a new home or when a tenant moves out — fast, affordable.

**Replace ($175–$500/lock):** New lock mechanism. Best when locks are worn, damaged, or you want to upgrade security grade.

**Find {city} locksmiths:** [Locksmiths {city}](/trades/locksmiths/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Locksmith Cost NZ](/articles/locksmith-cost-nz/)*
"""


# ── Carpenter ─────────────────────────────────────────────────────────────────

CARP_DATA = {
    "whangarei":    ("$88–$155/hr", "$68–$145"),
    "queenstown":   ("$115–$195/hr", "$88–$185"),
    "invercargill": ("$78–$142/hr", "$58–$130"),
    "whanganui":    ("$80–$148/hr", "$60–$135"),
    "gisborne":     ("$83–$150/hr", "$62–$138"),
}

def carpenter_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    hourly, callout = CARP_DATA[city_key]
    blurb = CITY_BLURB[city_key]
    return f"""---
title: "Carpenters {city} 2026 — Carpentry Rates, Costs and What to Expect"
description: "Carpenters {city} 2026 — {city} carpenter hourly rates, renovation costs, deck building prices, and how to find a reliable carpenter near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["carpenters {city}", "carpenter {city}", "carpentry cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{blurb} Here's what carpenters charge in {city} in 2026.

## {city} Carpenter Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Call-out / minimum charge | {callout} |
| Deck construction (per m²) | $1,400–$2,900/m² |
| Kitchen installation (flat-pack, labour) | $1,700–$4,300 |
| Door hang and fit (per door) | $170–$360 |
| Window installation (per window) | $270–$620 |
| Built-in wardrobe (per m wide) | $800–$2,100/m |
| Pergola / outdoor structure | $4,200–$17,000 |
| Architrave / skirting (per m linear) | $17–$42/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## LBP vs General Carpenter

**Licensed Building Practitioner (LBP):** Required for restricted building work — structural framing, weathertightness, foundations. Verify at [lbp.govt.nz](https://www.lbp.govt.nz).

**General carpenter:** Non-restricted work — fit-outs, cabinetry, decks under 1m, furniture.

**Find {city} carpenters:** [Carpenters {city}](/trades/carpenters/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Builders {city}](/articles/builder-{city_key}-nz/) | [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

for ck in NEW_CITIES:
    ARTICLES += [
        (f"tiler-{ck}-nz",                     lambda k=ck: tiler_article(k)),
        (f"landscaper-{ck}-nz",                lambda k=ck: landscaper_article(k)),
        (f"heat-pump-installer-{ck}-nz",        lambda k=ck: heatpump_article(k)),
        (f"insulation-installer-{ck}-nz",       lambda k=ck: insulation_article(k)),
        (f"arborist-{ck}-nz",                   lambda k=ck: arborist_article(k)),
        (f"drainlayer-{ck}-nz",                 lambda k=ck: drainlayer_article(k)),
        (f"locksmith-{ck}-nz",                  lambda k=ck: locksmith_article(k)),
        (f"carpenter-{ck}-nz",                  lambda k=ck: carpenter_article(k)),
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
