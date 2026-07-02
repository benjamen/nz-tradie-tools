#!/usr/bin/env python3
"""
Wave 9 SEO content generator — TradieTools NZ
Gap fills: bathroom, deck, kitchen, rubbish removal, floor sander for smaller cities
New trades: EV charger installation, switchboard upgrade (high-margin electrician work)
Run: python3 generate_wave9.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

CITIES = {
    "auckland":         {"name":"Auckland",        "region":"Auckland",          "rate_adj":"15–25% above national average"},
    "wellington":       {"name":"Wellington",       "region":"Wellington",         "rate_adj":"comparable to Auckland"},
    "christchurch":     {"name":"Christchurch",     "region":"Canterbury",         "rate_adj":"below Auckland and Wellington"},
    "hamilton":         {"name":"Hamilton",         "region":"Waikato",            "rate_adj":"10–15% below Auckland"},
    "tauranga":         {"name":"Tauranga",         "region":"Bay of Plenty",      "rate_adj":"broadly similar to Hamilton"},
    "dunedin":          {"name":"Dunedin",          "region":"Otago",              "rate_adj":"10–20% below Auckland"},
    "napier":           {"name":"Napier",           "region":"Hawke's Bay",        "rate_adj":"broadly regional"},
    "new-plymouth":     {"name":"New Plymouth",     "region":"Taranaki",           "rate_adj":"broadly regional"},
    "palmerston-north": {"name":"Palmerston North", "region":"Manawatu-Whanganui", "rate_adj":"broadly regional"},
    "nelson":           {"name":"Nelson",           "region":"Nelson-Tasman",      "rate_adj":"broadly regional"},
    "rotorua":          {"name":"Rotorua",          "region":"Bay of Plenty",      "rate_adj":"broadly regional"},
}

SMALL_CITIES = ["napier","new-plymouth","palmerston-north","nelson","rotorua"]

# ── Bathroom Renovator (smaller cities) ───────────────────────────────────────

BATHROOM_SMALL = {
    "napier":           ("$15,000–$36,000", "$7,500–$15,000", "$36,000–$90,000+", "Napier's growing property market and warm Hawke's Bay lifestyle make bathroom renovations a popular investment. The city's mix of 1930s post-quake housing and newer builds creates varied renovation opportunities."),
    "new-plymouth":     ("$15,000–$36,000", "$7,500–$15,000", "$36,000–$90,000+", "New Plymouth homeowners value quality bathrooms — the Taranaki lifestyle market attracts buyers who expect well-appointed homes. Ensuites are increasingly expected in New Plymouth's market."),
    "palmerston-north": ("$13,500–$33,000", "$6,800–$13,500", "$33,000–$82,000+", "Palmerston North has a strong rental market where bathroom upgrades directly impact yield and tenant quality. Owner-occupiers in the growing city are also active renovators."),
    "nelson":           ("$15,000–$36,000", "$7,500–$15,000", "$36,000–$90,000+", "Nelson's lifestyle-focused property market values bathroom quality highly. The region's outdoor and wellness culture means spa baths, rainfall showers, and quality finishes are popular choices."),
    "rotorua":          ("$13,500–$33,000", "$6,800–$13,500", "$33,000–$82,000+", "Rotorua's tourism-influenced property market means well-presented bathrooms matter for short-term rental performance. Airbnb hosts are active renovators in the Rotorua market."),
}

def bathroom_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    mid, budget, premium, local = BATHROOM_SMALL[city_key]
    return f"""---
title: "Bathroom Renovation {city} 2026 — Costs, What's Included and How to Plan"
description: "Bathroom renovation {city} 2026 — {city} bathroom renovation costs, budget vs mid-range vs premium, tradespeople needed, consents, and how to find reliable bathroom renovators near you."
image: "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["bathroom renovation {city}", "bathroom renovator {city}", "bathroom cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what bathroom renovations cost in {city} in 2026.

## {city} Bathroom Renovation Costs 2026

| Bathroom type | {city} typical cost |
|---|---|
| Budget (new suite, same layout) | {budget} |
| Mid-range (re-layout, quality fittings) | {mid} |
| Premium (full custom, designer fittings) | {premium} |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## What's Included

A complete bathroom renovation in {city} typically involves:

- **Builder:** Demolition, waterproofing, structural changes, project coordination
- **Plumber:** All plumbing connections, relocations if layout changes
- **Electrician:** Towel rail, fan, lighting, shaver socket
- **Tiler:** Floor and wall tiles
- **Plasterer:** Wall and ceiling finishing

## Waterproofing — Non-Negotiable

NZ Building Code requires compliant waterproofing in all wet areas. Shower areas must be waterproofed to minimum 1,800mm. Always use a Licensed Building Practitioner (LBP) for bathroom work — non-compliant waterproofing causes hidden rot discovered only when it becomes major structural damage.

## Timeline

Standard mid-range bathroom: 2–4 weeks from demolition to completion. Layout changes or custom fittings: 4–8 weeks.

**Find {city} bathroom renovators:** [Bathroom Renovators {city}](/trades/bathroom-renovators/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/) | [Kitchen Renovation {city}](/articles/kitchen-renovator-{city_key}-nz/) | [Tiler {city}](/articles/tiler-{city_key}-nz/)*
"""


# ── Deck Builder (smaller cities) ─────────────────────────────────────────────

DECK_SMALL = {
    "napier":           ("$1,600–$3,200/m²", "$16,000–$40,000", "Napier's warm Hawke's Bay summers make outdoor decks a natural extension of the living space. The art deco city's lifestyle aesthetic favours well-designed outdoor entertaining areas."),
    "new-plymouth":     ("$1,600–$3,200/m²", "$16,000–$40,000", "New Plymouth's coastal lifestyle and the backdrop of Mt Taranaki inspire quality outdoor living. Decks face coastal winds so design and material selection are important considerations."),
    "palmerston-north": ("$1,500–$3,000/m²", "$15,000–$37,000", "Palmerston North's large suburban sections provide good space for decks. The Manawatu wind means sheltered deck placement and solid balustrades are important design elements."),
    "nelson":           ("$1,600–$3,200/m²", "$16,000–$40,000", "Nelson's exceptional sunshine record makes it one of NZ's best cities for outdoor decks. The lifestyle market values well-designed outdoor spaces that capture Nelson's sun."),
    "rotorua":          ("$1,500–$3,000/m²", "$15,000–$37,000", "Rotorua's lake and outdoor lifestyle makes decks a valued feature. The region's tourism accommodation market also benefits from well-presented outdoor areas."),
}

def deck_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, standard, local = DECK_SMALL[city_key]
    return f"""---
title: "Deck Builders {city} 2026 — Deck Costs, Materials and What to Expect"
description: "Deck builders {city} 2026 — {city} deck building costs, timber vs composite pricing, consent requirements, and how to find a reliable deck builder near you."
image: "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["deck builders {city}", "deck builder {city}", "deck cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what deck builders charge in {city} in 2026.

## {city} Deck Costs 2026

| Service | {city} typical cost |
|---|---|
| Deck construction (per m²) | {m2} |
| Standard 20m² deck with balustrade | {standard} |
| Treated pine (entry-level) | $1,500–$2,500/m² |
| Hardwood (kwila, vitex) | $2,200–$4,000/m² |
| Composite (Trex, ModWood) | $2,500–$4,500/m² |
| Balustrade — glass (per m linear) | $600–$1,400/m |
| Balustrade — timber/aluminium (per m linear) | $280–$650/m |
| Deck stairs (per flight) | $1,800–$4,500 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Deck Market

{local}

## Consent Requirements in {city}

Decks over 1m above ground, over 20m², or attached to the house typically require building consent from {region} Council. Ground-level decks under 20m² and under 1m high are usually exempt — confirm with your deck builder before starting.

**Find {city} deck builders:** [Deck Builders {city}](/trades/deck-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/) | [Fence Installers {city}](/articles/fence-installer-{city_key}-nz/)*
"""


# ── Kitchen Renovator (smaller cities) ────────────────────────────────────────

KITCHEN_SMALL = {
    "napier":           ("$18,000–$45,000", "$9,000–$18,000", "$45,000–$110,000+", "Napier's active property market and Hawke's Bay food and wine culture make kitchen quality a priority. Open-plan living connecting kitchen to outdoor entertaining is popular."),
    "new-plymouth":     ("$18,000–$45,000", "$9,000–$18,000", "$45,000–$110,000+", "New Plymouth homeowners invest in quality kitchens — the Taranaki lifestyle market expects well-appointed homes. Open-plan layouts that capture outdoor views are popular."),
    "palmerston-north": ("$16,000–$40,000", "$8,000–$16,000", "$40,000–$95,000+", "Palmerston North has a strong renovation market. The city's affordable entry-level homes often have dated kitchens — upgrading adds significant value in the Manawatu market."),
    "nelson":           ("$18,000–$45,000", "$9,000–$18,000", "$45,000–$110,000+", "Nelson's food culture and lifestyle market make kitchens a high priority. Sculleries, island benches, and outdoor kitchen connections are popular in Nelson renovations."),
    "rotorua":          ("$16,000–$40,000", "$8,000–$16,000", "$40,000–$95,000+", "Rotorua's property market has Airbnb and short-term rental influence — well-presented kitchens drive rental performance in the tourism market."),
}

def kitchen_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    mid, budget, premium, local = KITCHEN_SMALL[city_key]
    return f"""---
title: "Kitchen Renovation {city} 2026 — Costs, What's Included and How to Plan"
description: "Kitchen renovation {city} 2026 — {city} kitchen renovation costs, budget vs mid-range vs premium, tradespeople needed, and how to find reliable kitchen renovators near you."
image: "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["kitchen renovation {city}", "kitchen renovator {city}", "kitchen cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what kitchen renovations cost in {city} in 2026.

## {city} Kitchen Renovation Costs 2026

| Kitchen type | {city} typical cost |
|---|---|
| Budget (flat-pack, installed) | {budget} |
| Mid-range (semi-custom) | {mid} |
| Premium (custom cabinetry) | {premium} |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Kitchen Renovation Market

{local}

## Tradespeople You'll Need

- **Builder / kitchen installer:** Project management, demolition, cabinetry, coordination
- **Plumber:** Sink, dishwasher, any plumbing relocations
- **Electrician:** Oven circuit, rangehood, lighting, extra power points
- **Tiler:** Splashback and floor tiles
- **Plasterer:** Walls after demolition

## Planning Tips

Layout changes (moving plumbing or structural walls) add cost significantly — working within the existing footprint keeps costs lower. Budget 35–45% for cabinetry, 10–20% for benchtop, 25–35% for labour.

**Find {city} kitchen renovators:** [Kitchen Renovators {city}](/trades/kitchen-renovators/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Kitchen Renovation Cost NZ](/articles/kitchen-renovation-cost-nz/) | [Bathroom Renovation {city}](/articles/bathroom-renovator-{city_key}-nz/)*
"""


# ── Rubbish Removal (smaller cities) ─────────────────────────────────────────

RUBBISH_SMALL = {
    "napier":           ("$170–$420", "$350–$820", "Napier's renovation market and tourism accommodation sector drive rubbish removal demand. Hawke's Bay's disaster recovery (2023 cyclone) also generated significant rubbish removal activity."),
    "new-plymouth":     ("$170–$420", "$350–$820", "New Plymouth has steady rubbish removal demand from its active renovation market and the commercial sector. The Taranaki industrial sector also generates commercial waste removal work."),
    "palmerston-north": ("$160–$400", "$330–$790", "Palmerston North's student population and rental market creates regular end-of-tenancy cleanout work for rubbish removal companies. The renovation market adds further demand."),
    "nelson":           ("$170–$420", "$350–$820", "Nelson's growing population and lifestyle property market generate steady rubbish removal demand. Deceased estate clearances are a significant part of the Nelson rubbish removal market given the region's older demographic."),
    "rotorua":          ("$160–$400", "$330–$790", "Rotorua's tourism accommodation sector generates commercial rubbish removal and skip bin demand. Residential renovation work also drives demand in this growing city."),
}

def rubbish_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    small, medium, local = RUBBISH_SMALL[city_key]
    return f"""---
title: "Rubbish Removal {city} 2026 — Costs, Skip Bins and What to Expect"
description: "Rubbish removal {city} 2026 — {city} rubbish removal costs, skip bin hire prices, same-day collection rates, and how to find a reliable rubbish removal company near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["rubbish removal {city}", "skip bin {city}", "junk removal {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what rubbish removal costs in {city} in 2026.

## {city} Rubbish Removal Costs 2026

| Service | {city} typical cost |
|---|---|
| Small load (ute/trailer, 1–2m³) | {small} |
| Medium load (small truck, 3–5m³) | {medium} |
| Large load (truck, 6–10m³) | $680–$2,000 |
| Full house / estate clearance | $900–$3,200 |
| Skip bin hire — 3m³ (3 days) | $240–$460 |
| Skip bin hire — 6m³ (3 days) | $360–$650 |
| Skip bin hire — 9m³ (3 days) | $460–$840 |
| Concrete / heavy materials (per m³) | $110–$260/m³ |
| Green waste (per m³) | $75–$170/m³ |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Rubbish Removal Market

{local}

## Skip Bin vs Same-Day Collection

**Skip bin:** Fill over several days at your own pace. Suits ongoing renovation projects. Needs road or driveway access. May need {region} Council permit for road placement.

**Same-day man-and-van:** Crew turns up, loads, done in an hour. Better for one-off clearances, heavy items, or tight access properties.

**Find {city} rubbish removal:** [Rubbish Removal {city}](/trades/rubbish-removal/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Skip Bin Cost NZ](/articles/skip-bin-cost-nz/)*
"""


# ── Floor Sander (smaller cities) ─────────────────────────────────────────────

FLOOR_SMALL = {
    "napier":           ("$32–$62/m²", "$1,900–$4,800", "Napier's older housing stock contains beautiful rimu and matai floors that have often been covered for decades. Floor restoration is a popular renovation in Napier's character homes."),
    "new-plymouth":     ("$32–$62/m²", "$1,900–$4,800", "New Plymouth's mix of older and newer homes creates demand for both heritage floor restoration and engineered timber finishing. Timber floors suit the region's lifestyle aesthetic."),
    "palmerston-north": ("$30–$58/m²", "$1,800–$4,500", "Palmerston North's 1940s–70s housing often has original timber floors hidden under carpet. Revealing and finishing these floors is a popular and cost-effective renovation."),
    "nelson":           ("$32–$62/m²", "$1,900–$4,800", "Nelson's lifestyle market values quality timber floors highly. The region's dry climate is good for timber — floors perform well and hold their finish longer than in wetter cities."),
    "rotorua":          ("$30–$58/m²", "$1,800–$4,500", "Rotorua's older homes have native timber floors that respond beautifully to sanding and finishing. The geothermal environment's warmth and humidity requires appropriate finish selection."),
}

def floor_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, fullhome, local = FLOOR_SMALL[city_key]
    return f"""---
title: "Floor Sanders {city} 2026 — Timber Floor Sanding Costs and What to Expect"
description: "Floor sanders {city} 2026 — {city} floor sanding costs, timber finishing prices, staining rates, and how to find a reliable floor sander near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["floor sanding {city}", "floor sanders {city}", "timber floor {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what floor sanding costs in {city} in 2026.

## {city} Floor Sanding Rates 2026

| Service | {city} typical cost |
|---|---|
| Sand and finish (per m², 3 coats) | {m2} |
| Full 3-bed home sanding (~80m²) | {fullhome} |
| Single room (20m²) | $650–$1,600 |
| Staining (per m², colour + finish) | $38–$72/m² |
| Gap filling (per m²) | $7–$18/m² |
| Buff and recoat (existing floors) | $14–$28/m² |
| Deck sanding and oiling (per m²) | $18–$42/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Floor Sanding Market

{local}

## What Can Be Sanded?

**Native timber (rimu, kauri, matai):** Excellent candidates — thick boards that last many sandings.
**Engineered timber:** 1–3 sands depending on wear layer thickness (check manufacturer spec).
**Cannot be sanded:** Laminate, most vinyl, bamboo (check manufacturer), flooring with under 2mm of wood above tongue.

## Finish Options

**Polyurethane (oil-based):** Hard-wearing, amber tone, traditional. **Water-based polyurethane:** Clearer finish, faster dry, lower odour. **Hardwax oil:** Natural penetrating finish, easy spot repairs.

**Find {city} floor sanders:** [Floor Sanders {city}](/trades/floor-sanding/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Floor Sanding Cost NZ](/articles/floor-sanding-cost-nz/) | [Carpet Layers {city}](/articles/carpet-layer-{city_key}-nz/)*
"""


# ── EV Charger Installation ────────────────────────────────────────────────────

EV_DATA = {
    "auckland":     ("$900–$1,800", "$1,400–$2,800", "Auckland has NZ's highest EV adoption rate. The city's long commutes and traffic make EV ownership particularly appealing. Demand for home EV charger installation has grown rapidly as Tesla, BYD, and other EVs become mainstream in Auckland."),
    "wellington":   ("$950–$1,900", "$1,450–$2,900", "Wellington's hilly terrain and stop-start traffic actually suit EVs well — regenerative braking works effectively. Many Wellington homeowners are installing EV chargers ahead of their first EV purchase."),
    "christchurch": ("$850–$1,700", "$1,300–$2,600", "Christchurch has NZ's flattest terrain, making it ideal for EV range efficiency. The post-earthquake rebuild saw many homes wired with future EV charging in mind. Christchurch electricians are experienced with EV charger installation."),
    "hamilton":     ("$800–$1,600", "$1,200–$2,500", "Hamilton's growing EV adoption and suburban lifestyle — where having a home charger is more practical than in central cities — makes residential EV charger installation increasingly common."),
    "tauranga":     ("$850–$1,700", "$1,300–$2,600", "Tauranga's lifestyle demographics and high EV uptake among the Bay of Plenty's affluent retiree and professional population drives steady EV charger installation demand."),
    "dunedin":      ("$800–$1,600", "$1,200–$2,500", "Dunedin's student and professional population is increasingly going electric. The city's cold winters make it worth noting that EV range reduces in very cold weather — home charging overnight to full ensures maximum range."),
}

def ev_article(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    level2, smart, local = EV_DATA[city_key]
    return f"""---
title: "EV Charger Installation {city} 2026 — Home EV Charging Costs and What to Expect"
description: "EV charger installation {city} 2026 — {city} home EV charger costs, Level 2 charging prices, smart charger options, and how to find a qualified EV charger installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["EV charger installation {city}", "home EV charger {city}", "electric vehicle charger {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what home EV charger installation costs in {city} in 2026.

## {city} EV Charger Installation Costs 2026

| Service | {city} typical cost |
|---|---|
| Level 2 charger (7kW, supply + install) | {level2} |
| Smart / Wi-Fi charger (supply + install) | {smart} |
| Three-phase charger (22kW, supply + install) | $2,200–$4,500 |
| Installation labour only (charger supplied) | $350–$750 |
| Switchboard upgrade (if required) | $1,500–$3,500 |
| Additional cabling run (per metre) | $35–$75/m |
| Outdoor weatherproof installation | add $150–$400 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} EV Charger Market

{local}

## Level 1 vs Level 2 — Which Do You Need?

**Level 1 (standard 10A/2.4kW wall socket):**
- Free to use — already in your garage
- Charges ~15km of range per hour
- Suitable for low-mileage drivers or plug-in hybrids
- **Not recommended** for full EVs driven daily

**Level 2 (7kW dedicated circuit):**
- Charges ~50km of range per hour
- Full EV (60–80kWh battery) charged overnight
- Requires a dedicated 32A circuit installed by a licensed electrician
- **Recommended for most EV owners** — peace of mind, full charge every morning

**Three-phase (22kW):**
- Charges ~150km per hour
- Primarily useful for commercial/fleet or drivers with very high mileage
- Requires three-phase power supply (many NZ homes are single-phase only)

## Smart Chargers

Smart / Wi-Fi chargers allow:
- **Off-peak scheduling** — charge overnight when electricity is cheapest
- **Load balancing** — reduce charge rate if household power demand is high
- **App monitoring** — track kWh charged and cost
- **Solar integration** — some models can prioritise charging from solar generation

Popular brands in NZ: Wallbox, EVNEX, Schneider Electric EVlink, Ohme.

## What the Installation Involves

1. Electrician assesses switchboard capacity
2. Dedicated 32A (or 40A) circuit run from switchboard to garage/carport
3. Charger mounted and wired
4. Electrical Warrant of Fitness (eWoF) issued

**Important:** Home EV charger installation is **restricted electrical work** — must be done by a registered electrician. A compliance certificate is legally required.

**Find {city} EV charger installers:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does EV charger installation cost in {city}?**
Level 2 (7kW, supply + install): {level2}. Smart charger: {smart}. Switchboard upgrade may add $1,500–$3,500 if required.

**Do I need an electrician to install a home EV charger in {city}?**
Yes — installing a dedicated charging circuit is restricted electrical work. Must be done by a registered electrician who will issue a compliance certificate.

**How long does EV charger installation take?**
Typically half a day for a straightforward installation. Longer if switchboard upgrades or long cable runs are required.

**Will my switchboard need upgrading for an EV charger?**
Older homes with fuse boards or limited capacity may need a switchboard upgrade before an EV charger can be installed. Your electrician will assess this during the quote.

---

*Related: [Electricians {city}](/articles/electrician-{city_key}-nz/) | [Switchboard Upgrade Cost {city}](/articles/switchboard-upgrade-{city_key}-nz/) | [Solar Installers {city}](/articles/solar-installer-{city_key}-nz/)*
"""


# ── Switchboard Upgrade ────────────────────────────────────────────────────────

SWITCH_DATA = {
    "auckland":     ("$2,200–$4,500", "$3,500–$6,500", "Auckland has a large stock of pre-1980s homes with outdated fuse boards that need upgrading before EV chargers, heat pumps, or solar can be added. Switchboard upgrades are one of Auckland's most common electrician jobs."),
    "wellington":   ("$2,300–$4,700", "$3,700–$6,800", "Wellington's old villa stock is full of original ceramic fuse boards. As homeowners add heat pumps, EV chargers, and solar, upgrading to modern circuit breakers with RCDs becomes necessary."),
    "christchurch": ("$2,000–$4,200", "$3,200–$6,200", "Post-earthquake Christchurch upgrades often included switchboard replacement. However, many pre-quake homes still have old boards needing attention, especially in areas that weren't significantly damaged."),
    "hamilton":     ("$1,900–$4,000", "$3,000–$5,800", "Hamilton's 1960s–80s housing belt has many original fuse boards reaching end of life. Upgrading is commonly triggered by adding an EV charger, heat pump, or electric stove."),
    "tauranga":     ("$2,000–$4,200", "$3,200–$6,200", "Tauranga's growing demand for home EV chargers and solar installations is driving switchboard upgrade work as older homes' fuse boards can't support the added load."),
    "dunedin":      ("$1,800–$3,800", "$2,800–$5,500", "Dunedin's Victorian and Edwardian homes often have original or early 20th-century electrical systems that are well past their useful life. Switchboard upgrades are frequently required when these homes are renovated."),
}

def switch_article(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    standard, complex_, local = SWITCH_DATA[city_key]
    return f"""---
title: "Switchboard Upgrade {city} 2026 — Costs, What's Involved and When You Need One"
description: "Switchboard upgrade {city} 2026 — {city} switchboard upgrade costs, fuse board replacement prices, RCD installation rates, and how to find a qualified electrician near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["switchboard upgrade {city}", "fuse board replacement {city}", "electrician {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what switchboard upgrades cost in {city} in 2026.

## {city} Switchboard Upgrade Costs 2026

| Service | {city} typical cost |
|---|---|
| Standard switchboard upgrade (single-phase) | {standard} |
| Complex upgrade (three-phase or rewire involved) | {complex_} |
| Add RCD / safety switch (to existing board) | $280–$580 |
| Add circuit breaker (individual circuit) | $180–$380 |
| Switchboard inspection / report | $180–$350 |
| Underground supply upgrade (lines company) | $1,500–$5,000+ |

*All prices GST inclusive. {c["rate_adj"].capitalize()}. Price depends heavily on board location, number of circuits, and whether rewiring is required.*

## {city} Switchboard Market

{local}

## When Do You Need a Switchboard Upgrade?

**You likely need an upgrade if your home has:**
- Original ceramic or glass fuse holders (not circuit breakers)
- No RCDs (safety switches) — required by NZ Building Code for new work
- Fuses blowing frequently
- Less than 63A capacity for a modern home
- Aluminium wiring (pre-1975 homes — special attention needed)

**Triggered by adding:**
- EV charger (requires dedicated 32A circuit)
- Solar system (requires AC disconnect and metering changes)
- Electric vehicle charger
- Induction cooktop or electric oven (high draw)
- Heat pump (particularly multi-split or ducted systems)

## What an Upgrade Includes

A full switchboard upgrade in {city} typically includes:

1. Replace fuse board with modern consumer unit (circuit breakers)
2. Install RCDs (residual current devices) for personal protection
3. Label and test all circuits
4. Issue Electrical Certificate of Compliance (eCoC)

Your electrician will also identify any unsafe wiring and recommend remediation.

## Safety Switches (RCDs) — Why They Matter

RCDs detect earth faults and trip in under 30ms — fast enough to prevent electrocution. NZ Building Code requires RCD protection on all new circuits and upgraded switchboards. **If your switchboard has no RCDs, this is a safety issue** — particularly important if you have young children.

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a switchboard upgrade cost in {city}?**
Standard single-phase upgrade: {standard}. Complex/three-phase: {complex_}.

**Do I need a switchboard upgrade for an EV charger?**
Often yes — older fuse boards don't have capacity for a dedicated 32A EV charging circuit. Your electrician will assess during the quote.

**Is a switchboard upgrade restricted electrical work?**
Yes — must be done by a registered electrician who will issue an Electrical Certificate of Compliance. Never attempt DIY on a switchboard.

---

*Related: [Electricians {city}](/articles/electrician-{city_key}-nz/) | [EV Charger Installation {city}](/articles/ev-charger-installation-{city_key}-nz/) | [Solar Installers {city}](/articles/solar-installer-{city_key}-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

# Gap fills for smaller cities
for ck in SMALL_CITIES:
    ARTICLES.append((f"bathroom-renovator-{ck}-nz",  lambda k=ck: bathroom_small(k)))
    ARTICLES.append((f"deck-builder-{ck}-nz",         lambda k=ck: deck_small(k)))
    ARTICLES.append((f"kitchen-renovator-{ck}-nz",    lambda k=ck: kitchen_small(k)))
    ARTICLES.append((f"rubbish-removal-{ck}-nz",      lambda k=ck: rubbish_small(k)))
    ARTICLES.append((f"floor-sander-{ck}-nz",         lambda k=ck: floor_small(k)))

# EV charger — all main cities
for ck in ["auckland","wellington","christchurch","hamilton","tauranga","dunedin"]:
    ARTICLES.append((f"ev-charger-installation-{ck}-nz", lambda k=ck: ev_article(k)))

# Switchboard upgrade — all main cities
for ck in ["auckland","wellington","christchurch","hamilton","tauranga","dunedin"]:
    ARTICLES.append((f"switchboard-upgrade-{ck}-nz", lambda k=ck: switch_article(k)))


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
