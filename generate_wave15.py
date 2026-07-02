#!/usr/bin/env python3
"""
Wave 15 SEO content generator — TradieTools NZ
Complete the 5 new cities: bathroom, kitchen, deck, floor sander, glazier,
EV charger, switchboard, pergola, rubbish removal, pool builder
Run: python3 generate_wave15.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

NEW_CITIES = {
    "whangarei":    {"name":"Whangarei",    "region":"Northland",          "rate_adj":"broadly regional"},
    "queenstown":   {"name":"Queenstown",   "region":"Queenstown-Lakes",   "rate_adj":"among NZ's highest"},
    "invercargill": {"name":"Invercargill", "region":"Southland",          "rate_adj":"below national average"},
    "whanganui":    {"name":"Whanganui",    "region":"Manawatu-Whanganui", "rate_adj":"broadly regional"},
    "gisborne":     {"name":"Gisborne",     "region":"Gisborne",           "rate_adj":"broadly regional"},
}

CITY_BLURB = {
    "whangarei":    "Whangarei is Northland's commercial hub — a subtropical, fast-growing city with strong construction demand.",
    "queenstown":   "Queenstown is NZ's premier lifestyle and tourism destination with premium trade rates and a discerning client base.",
    "invercargill": "Invercargill is NZ's southernmost city with competitive trade pricing and strong demand for quality workmanship.",
    "whanganui":    "Whanganui is a growing heritage city with beautiful Victorian housing stock and an active renovation market.",
    "gisborne":     "Gisborne is NZ's most isolated city — warm, sunny, with a strong horticulture economy and active construction market.",
}

# ── Bathroom Renovator ────────────────────────────────────────────────────────

BATH_DATA = {
    "whangarei":    ("$15,000–$37,000", "$7,500–$15,000", "$37,000–$92,000+", "Whangarei's subtropical humidity makes waterproofing particularly important — moisture behind tiles causes rot faster in Northland's warm damp climate. Choose experienced local tilers and builders who understand the local conditions."),
    "queenstown":   ("$20,000–$48,000", "$10,000–$20,000", "$48,000–$130,000+", "Queenstown's premium market expects high-end bathroom finishes. Designer tapware, heated floors, frameless glass, and custom tiles are the norm in Queenstown's luxury residential and accommodation sector."),
    "invercargill": ("$13,000–$30,000", "$6,500–$13,000", "$30,000–$75,000+", "Invercargill's cold climate makes a heated towel rail and underfloor heating popular bathroom additions — warmth matters in Southland. Good ventilation is also critical to prevent moisture buildup in cold, damp conditions."),
    "whanganui":    ("$14,000–$32,000", "$7,000–$14,000", "$32,000–$80,000+", "Whanganui's heritage homes often have original small bathrooms ripe for upgrading. Many renovation projects open up the bathroom, combine toilet/bathroom into one space, and add an ensuite — particularly popular as the city attracts new residents."),
    "gisborne":     ("$14,000–$33,000", "$7,000–$14,000", "$33,000–$82,000+", "Gisborne's warm climate means cooling and ventilation matter as much as heating in bathrooms. The post-cyclone rebuild (Gabrielle 2023) drove significant bathroom replacement as flood-damaged bathrooms were gutted and rebuilt."),
}

def bathroom_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    mid, budget, premium, local = BATH_DATA[city_key]
    return f"""---
title: "Bathroom Renovation {city} 2026 — Costs, What's Included and How to Plan"
description: "Bathroom renovation {city} 2026 — {city} bathroom renovation costs, budget vs mid-range vs premium, waterproofing requirements, and how to find reliable bathroom renovators near you."
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

## Tradespeople You'll Need

- **Builder:** Demolition, waterproofing, coordination
- **Plumber:** All plumbing connections and relocations
- **Electrician:** Towel rail, fan, lighting, shaver socket
- **Tiler:** Floor and wall tiles
- **Plasterer:** Wall and ceiling finishing

## Waterproofing — Critical in {city}

NZ Building Code requires compliant waterproofing in all shower areas to minimum 1,800mm. Must be done by a Licensed Building Practitioner (LBP). {local}

**Find {city} bathroom renovators:** [Bathroom Renovators {city}](/trades/bathroom-renovators/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/) | [Tilers {city}](/articles/tiler-{city_key}-nz/)*
"""


# ── Kitchen Renovator ─────────────────────────────────────────────────────────

KITCHEN_DATA = {
    "whangarei":    ("$18,000–$46,000", "$9,000–$18,000", "$46,000–$115,000+", "Whangarei's growing lifestyle market values quality kitchens. Open-plan layouts connecting to outdoor entertaining are popular in Northland homes where indoor-outdoor flow is used year-round."),
    "queenstown":   ("$25,000–$65,000", "$13,000–$25,000", "$65,000–$160,000+", "Queenstown's premium market demands high-specification kitchens — stone benchtops, custom cabinetry, premium appliances, and sculleries are expected in the luxury residential and holiday accommodation sector."),
    "invercargill": ("$13,000–$30,000", "$6,500–$13,000", "$30,000–$75,000+", "Invercargill's affordable property market makes kitchen renovations a popular value-add strategy. Flat-pack cabinetry with stone benchtops is the sweet spot for Southland renovators."),
    "whanganui":    ("$14,000–$32,000", "$7,000–$14,000", "$32,000–$80,000+", "Whanganui's heritage property market values kitchens that respect the character of the home while offering modern functionality. Semi-custom cabinetry in heritage colours is popular."),
    "gisborne":     ("$15,000–$35,000", "$7,500–$15,000", "$35,000–$88,000+", "Gisborne's food and wine culture makes kitchen quality a priority. The post-cyclone rebuild drove significant kitchen replacement as damaged kitchens were gutted and rebuilt to modern standards."),
}

def kitchen_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    mid, budget, premium, local = KITCHEN_DATA[city_key]
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

## {city} Kitchen Market

{local}

## Budget Allocation Guide

- Cabinetry: 35–45% of budget
- Benchtop: 10–20%
- Appliances: 10–20%
- Labour (all trades): 25–35%
- Splashback, sink, taps: 5–10%

Layout changes (moving plumbing or walls) add significant cost — staying within the existing footprint keeps prices lower.

**Find {city} kitchen renovators:** [Kitchen Renovators {city}](/trades/kitchen-renovators/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Kitchen Renovation Cost NZ](/articles/kitchen-renovation-cost-nz/) | [Bathroom Renovation {city}](/articles/bathroom-renovator-{city_key}-nz/)*
"""


# ── Deck Builder ──────────────────────────────────────────────────────────────

DECK_DATA = {
    "whangarei":    ("$1,650–$3,300/m²", "$16,500–$41,000", "Whangarei's subtropical climate and long outdoor season make decks excellent value — usable 10+ months of the year. Composite decking handles Northland's humidity and UV well with minimal maintenance."),
    "queenstown":   ("$2,000–$4,000/m²", "$20,000–$50,000", "Queenstown's alpine setting makes deck design important — snow loading, wind, and freeze-thaw cycles must be accounted for. Premium hardwood or composite decking outperforms treated pine in Queenstown's demanding climate."),
    "invercargill": ("$1,450–$2,900/m²", "$14,500–$36,000", "Invercargill's wet, cold climate means deck use is more seasonal than in northern NZ. Covered or partially enclosed decks extend the usable season. Composite decking resists Southland's moisture well."),
    "whanganui":    ("$1,500–$3,000/m²", "$15,000–$37,500", "Whanganui's mild climate and outdoor lifestyle make decks popular. The river city's heritage aesthetic suits natural timber decks that complement period homes."),
    "gisborne":     ("$1,600–$3,200/m²", "$16,000–$40,000", "Gisborne's warm sunny climate means decks are well-used year-round. The outdoor entertaining culture in this wine and food region makes quality decks a priority for homeowners."),
}

def deck_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, standard, local = DECK_DATA[city_key]
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
| Treated pine (entry-level) | $1,400–$2,400/m² |
| Hardwood (kwila, vitex) | $2,100–$3,800/m² |
| Composite (Trex, ModWood) | $2,400–$4,300/m² |
| Balustrade — glass (per m linear) | $580–$1,350/m |
| Deck stairs (per flight) | $1,700–$4,200 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Deck Market

{local}

## Consent in {city}

Decks over 1m above ground, over 20m², or attached to the house require building consent from {region} Council. Ground-level decks under 20m² and under 1m are usually exempt — confirm with your deck builder before starting.

**Find {city} deck builders:** [Deck Builders {city}](/trades/deck-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Pergola Builders {city}](/articles/pergola-builder-{city_key}-nz/)*
"""


# ── Floor Sander ──────────────────────────────────────────────────────────────

FLOOR_DATA = {
    "whangarei":    ("$33–$64/m²", "$2,000–$4,900", "Whangarei's older housing stock has rimu and matai floors often hidden under carpet. The subtropical warmth means floors need appropriate finish — hardwax oil performs well in Northland's humidity."),
    "queenstown":   ("$42–$78/m²", "$2,500–$6,200", "Queenstown's premium market expects quality floor finishes. Heritage timber floors in older properties and engineered timber in newer builds are both common. Water-based polyurethane is popular for its clear finish that suits alpine lodge aesthetics."),
    "invercargill": ("$29–$56/m²", "$1,750–$4,400", "Invercargill's older housing has original timber floors in excellent condition beneath decades of carpet. Cold winters make warm timber floors particularly appealing in Southland."),
    "whanganui":    ("$30–$58/m²", "$1,800–$4,500", "Whanganui's Victorian and Edwardian homes have beautiful original timber floors frequently uncovered during renovation. The city's heritage character makes restored timber floors a natural choice."),
    "gisborne":     ("$31–$60/m²", "$1,850–$4,700", "Gisborne's older housing contains native timber floors that restore beautifully. The warm climate is good for floor finishing — fast drying times and low humidity mean quality results."),
}

def floor_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    m2, fullhome, local = FLOOR_DATA[city_key]
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
| Full 3-bed home (~80m²) | {fullhome} |
| Single room (20m²) | $660–$1,650 |
| Staining (per m², colour + finish) | $39–$74/m² |
| Gap filling (per m²) | $7–$18/m² |
| Buff and recoat (existing finish) | $14–$29/m² |
| Deck sanding and oiling (per m²) | $19–$43/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Floor Sanding Market

{local}

## What Can Be Sanded?

Native timber (rimu, kauri, matai) — excellent candidates, thick boards. Engineered timber — 1–3 sands depending on wear layer. Cannot sand: laminate, most vinyl, or flooring with under 2mm of wood above the tongue.

**Find {city} floor sanders:** [Floor Sanders {city}](/trades/floor-sanding/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Floor Sanding Cost NZ](/articles/floor-sanding-cost-nz/) | [Carpet Layers {city}](/articles/carpet-layer-{city_key}-nz/)*
"""


# ── Glazier ───────────────────────────────────────────────────────────────────

GLAZIER_DATA = {
    "whangarei":    ("$172–$395", "$335–$895", "$785–$2,450", "Whangarei's warm subtropical climate makes cooling as important as heating — low-E double glazing reduces solar heat gain in summer. Coastal salt air requires quality anodised aluminium or uPVC frames to resist corrosion."),
    "queenstown":   ("$200–$450", "$400–$1,050", "$950–$2,900", "Queenstown's alpine climate makes double glazing almost essential — single-glazed windows are prohibitively expensive to heat around in winter. Triple glazing is increasingly specified in Queenstown's premium new builds."),
    "invercargill": ("$158–$365", "$310–$840", "$740–$2,300", "Invercargill's cold winters make double glazing one of the highest-ROI home improvements. Condensation on single-glazed windows is a significant issue in Southland's damp cold winters."),
    "whanganui":    ("$163–$375", "$318–$856", "$758–$2,348", "Whanganui's mild climate means glazing upgrades are more about noise reduction and comfort than extreme thermal performance. The heritage property market values period-appropriate window styles."),
    "gisborne":     ("$168–$385", "$325–$868", "$768–$2,375", "Gisborne's sunny warm climate makes glazing selection important for solar control — tinted or low-E double glazing prevents summer overheating while retaining winter warmth."),
}

def glazier_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    callout, repair, window, local = GLAZIER_DATA[city_key]
    return f"""---
title: "Glaziers {city} 2026 — Glass Repair Costs, Window Replacement and What to Expect"
description: "Glaziers {city} 2026 — {city} glazier call-out rates, glass repair costs, window replacement prices, double glazing costs, and how to find a reliable glazier near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["glaziers {city}", "glazier {city}", "glass repair {city}", "window replacement {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what glaziers charge in {city} in 2026.

## {city} Glazier Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (standard hours) | {callout} |
| Emergency glass replacement (after hours) | $290–$680 |
| Single glaze repair / replacement (per pane) | {repair} |
| Double glazing replacement (per pane) | $440–$1,200 |
| Window replacement — aluminium (per window) | {window} |
| Double glazing retrofit (per window) | $790–$2,450 |
| Shower screen supply and fit | $770–$2,450 |
| Glass balustrade (per m linear) | $390–$990/m |
| Glass splashback (per m²) | $245–$590/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Glazing Market

{local}

## Safety Glass Requirements

NZ Building Code requires safety (toughened or laminated) glass within 500mm of doors, below 1,050mm, in wet areas, and at balustrades. When replacing glass in older homes, confirm replacement meets current code.

**Find {city} glaziers:** [Glaziers {city}](/trades/glaziers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Window Replacement Cost NZ](/articles/window-replacement-cost-nz/) | [Insulation Installers {city}](/articles/insulation-installer-{city_key}-nz/)*
"""


# ── EV Charger ────────────────────────────────────────────────────────────────

EV_DATA = {
    "whangarei":    ("$880–$1,760", "$1,360–$2,760", "Whangarei's growing population and long Northland commutes are making EV ownership practical — home charging is essential to manage running costs. Auckland to Whangarei is within one charge for most modern EVs."),
    "queenstown":   ("$960–$1,900", "$1,460–$2,900", "Queenstown's alpine tourist economy is rapidly electrifying — tour operators, accommodation providers, and high-income residents are adopting EVs quickly. Home charging demand is strong in Queenstown's premium residential market."),
    "invercargill": ("$820–$1,640", "$1,260–$2,580", "Invercargill's cold winters reduce EV range slightly — home charging to full overnight ensures maximum range on cold mornings. Southland's low electricity prices from the national hydro grid make EV running costs particularly low."),
    "whanganui":    ("$840–$1,680", "$1,280–$2,620", "Whanganui's compact city layout suits EV ownership well — most daily trips are well within a single charge. The city's growing professional community is adopting EVs as part of a broader lifestyle upgrade."),
    "gisborne":     ("$850–$1,700", "$1,300–$2,640", "Gisborne's isolation makes reliable home charging important — public charging infrastructure is limited in the region. A Level 2 home charger ensures Gisborne EV owners always start the day with a full battery."),
}

def ev_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    level2, smart, local = EV_DATA[city_key]
    return f"""---
title: "EV Charger Installation {city} 2026 — Home EV Charging Costs and What to Expect"
description: "EV charger installation {city} 2026 — {city} home EV charger costs, Level 2 vs smart charger pricing, and how to find a qualified electrician near you."
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
| Three-phase charger (22kW, supply + install) | $2,100–$4,400 |
| Labour only (charger supplied) | $320–$700 |
| Switchboard upgrade (if required) | $1,400–$3,200 |
| Additional cabling (per metre) | $32–$70/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} EV Charging Market

{local}

## Level 1 vs Level 2

**Level 1 (standard socket):** ~15km range/hour. Fine for plug-in hybrids. Not recommended for daily EV drivers. **Level 2 (7kW dedicated):** ~50km/hour. Full EV charged overnight. Requires a licensed electrician and dedicated 32A circuit.

EV charger installation is **restricted electrical work** — must be done by a registered electrician who issues an Electrical Certificate of Compliance.

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Electricians {city}](/articles/electrician-{city_key}-nz/) | [Switchboard Upgrade {city}](/articles/switchboard-upgrade-{city_key}-nz/)*
"""


# ── Switchboard Upgrade ───────────────────────────────────────────────────────

SWITCH_DATA = {
    "whangarei":    ("$1,950–$4,100", "$3,100–$5,900", "Whangarei's older housing stock has many original fuse boards — triggered by EV charger or heat pump installation, many Northland homeowners are discovering their boards need upgrading before new high-draw appliances can be added."),
    "queenstown":   ("$2,200–$4,600", "$3,500–$6,600", "Queenstown's rapid development means both old and new electrical systems co-exist. Luxury renovations often require board upgrades to support premium appliances, home automation, and EV chargers."),
    "invercargill": ("$1,750–$3,750", "$2,750–$5,400", "Invercargill's cold climate drives heat pump and EV charger installation — both of which often trigger switchboard upgrades in homes with older fuse boards. Southland's affordable electrician rates make upgrades cost-effective."),
    "whanganui":    ("$1,800–$3,800", "$2,800–$5,500", "Whanganui's heritage homes often have original or early-replacement electrical boards that can't safely support modern loads. Board upgrades are commonly discovered during renovation work."),
    "gisborne":     ("$1,850–$3,900", "$2,900–$5,600", "Gisborne's post-cyclone rebuild included many electrical upgrades as damaged systems were replaced. Modern switchboards with RCDs are now standard in rebuilt properties."),
}

def switch_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    standard, complex_, local = SWITCH_DATA[city_key]
    return f"""---
title: "Switchboard Upgrade {city} 2026 — Costs, What's Involved and When You Need One"
description: "Switchboard upgrade {city} 2026 — {city} switchboard upgrade costs, fuse board replacement prices, RCD installation, and how to find a qualified electrician near you."
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
| Standard upgrade (single-phase) | {standard} |
| Complex upgrade (three-phase or rewire) | {complex_} |
| Add RCD to existing board | $270–$560 |
| Add circuit breaker | $170–$360 |
| Board inspection / report | $165–$325 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Switchboard Market

{local}

## When You Need an Upgrade

Your home likely needs a switchboard upgrade if it has ceramic fuse holders, no RCDs (safety switches), or if you're adding an EV charger, solar, heat pump, or induction cooktop. Must be done by a registered electrician who issues an Electrical Certificate of Compliance.

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Electricians {city}](/articles/electrician-{city_key}-nz/) | [EV Charger Installation {city}](/articles/ev-charger-installation-{city_key}-nz/)*
"""


# ── Pergola Builder ───────────────────────────────────────────────────────────

PERGOLA_DATA = {
    "whangarei":    ("$8,800–$22,500", "$22,500–$56,000+", "Whangarei's subtropical climate and near year-round outdoor season make pergolas excellent value. A louvred pergola with automated roof lets Northland homeowners use their outdoor space even during the region's frequent rain showers."),
    "queenstown":   ("$10,500–$27,000", "$27,000–$68,000+", "Queenstown's alpine environment demands robust pergola construction — snow load, high winds, and freeze-thaw cycles must be accounted for. Premium louvred systems with motorised closure for rain and snow are popular in Queenstown's luxury market."),
    "invercargill": ("$7,500–$19,500", "$19,500–$49,000+", "Invercargill's cold, wet climate makes a well-enclosed pergola more valuable than an open frame. Insulated roof panels and wind-sheltering side panels create an outdoor room usable even in Southland's challenging weather."),
    "whanganui":    ("$7,800–$20,000", "$20,000–$50,000+", "Whanganui's mild climate and outdoor lifestyle make pergolas a popular addition. The river city's heritage character suits timber pergolas that complement period homes and gardens."),
    "gisborne":     ("$8,000–$20,500", "$20,500–$51,500+", "Gisborne's excellent sunshine and outdoor food and wine culture make pergolas a natural investment. Open timber pergolas with shade cloth work well in Gisborne's dry summer climate."),
}

def pergola_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    standard, premium, local = PERGOLA_DATA[city_key]
    return f"""---
title: "Pergola Builders {city} 2026 — Pergola Costs, Types and What to Expect"
description: "Pergola builders {city} 2026 — {city} pergola costs, louvred vs timber vs polycarbonate prices, consent requirements, and how to find a reliable pergola builder near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["pergola builders {city}", "pergola cost {city}", "pergola {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what pergola builders charge in {city} in 2026.

## {city} Pergola Costs 2026

| Pergola type | {city} typical cost |
|---|---|
| Open timber frame | $4,200–$11,500 |
| Polycarbonate roof pergola | $5,800–$14,500 |
| Louvred pergola (motorised, standard) | {standard} |
| Louvred pergola (premium, lights/heaters) | {premium} |
| Shade sail (supply + posts + install) | $2,400–$7,200 |
| Insulated panel roof pergola | $8,800–$23,000 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Pergola Market

{local}

## Consent Requirements

Pergolas attached to the house, over 20m², or over 2.5m high typically require building consent from {region} Council. Detached pergolas under 20m² and under 2.5m are usually exempt — confirm with your builder.

**Find {city} pergola builders:** [Deck Builders {city}](/trades/deck-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Pergola Cost NZ](/articles/pergola-cost-nz/) | [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/)*
"""


# ── Rubbish Removal ───────────────────────────────────────────────────────────

RUBBISH_DATA = {
    "whangarei":    ("$168–$415", "$348–$812", "Whangarei's growing population and active construction market generate steady rubbish removal demand. The subtropical climate also drives regular garden and green waste removal."),
    "queenstown":   ("$195–$480", "$395–$950", "Queenstown's premium construction and renovation market generates significant rubbish removal work. The tourism sector creates commercial waste removal demand year-round. Tight access in parts of Queenstown's steep terrain can complicate collections."),
    "invercargill": ("$148–$390", "$308–$758", "Invercargill's steady renovation market and affordable housing drive rubbish removal demand. The city's agricultural surrounds also generate rural waste removal work."),
    "whanganui":    ("$152–$398", "$315–$775", "Whanganui's active heritage renovation market generates rubbish removal demand from demolition and renovation work. Deceased estate clearances are also a regular part of the Whanganui rubbish removal market."),
    "gisborne":     ("$158–$405", "$325–$790", "Gisborne's post-cyclone (Gabrielle 2023) rebuild generated unprecedented rubbish removal demand. Ongoing rebuild and renovation activity continues to keep rubbish removal operators busy in Gisborne."),
}

def rubbish_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    small, medium, local = RUBBISH_DATA[city_key]
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
| Small load (1–2m³) | {small} |
| Medium load (3–5m³) | {medium} |
| Large load (6–10m³) | $670–$1,980 |
| Full house / estate clearance | $880–$3,100 |
| Skip bin hire — 3m³ (3 days) | $235–$455 |
| Skip bin hire — 6m³ (3 days) | $355–$645 |
| Skip bin hire — 9m³ (3 days) | $455–$835 |
| Concrete / heavy materials (per m³) | $108–$255/m³ |
| Green waste (per m³) | $72–$165/m³ |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Rubbish Removal Market

{local}

**Find {city} rubbish removal:** [Rubbish Removal {city}](/trades/rubbish-removal/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Skip Bin Cost NZ](/articles/skip-bin-cost-nz/)*
"""


# ── Pool Builder ──────────────────────────────────────────────────────────────

POOL_DATA = {
    "whangarei":    ("$46,000–$84,000", "$84,000–$155,000+", "$23,000–$46,000", "Whangarei's subtropical climate gives Northland pools one of NZ's longest swimming seasons — October through April with ease, and heated pools year-round. The long warm season makes pools excellent value in Whangarei."),
    "queenstown":   ("$55,000–$100,000", "$100,000–$200,000+", "$28,000–$55,000", "Queenstown's alpine climate means outdoor pools have a short unheated season. Indoor or heated covered pools are more practical. Luxury properties do feature pools — often heated and spa-integrated. Expect premium construction costs."),
    "invercargill": ("$40,000–$74,000", "$74,000–$138,000+", "$20,000–$40,000", "Invercargill's cold climate makes outdoor pools less popular — the season is short. Indoor or enclosed heated pools are more common. A well-heated fibreglass pool in a sheltered north-facing location can be used from November to March."),
    "whanganui":    ("$42,000–$78,000", "$78,000–$145,000+", "$21,000–$42,000", "Whanganui's warm summers make outdoor pools enjoyable from November through March. The city's affordable land and larger sections provide good space for pool installation."),
    "gisborne":     ("$45,000–$82,000", "$82,000–$152,000+", "$22,000–$45,000", "Gisborne's warm sunny climate — one of NZ's sunniest — makes outdoor pools well-used. The long warm season and outdoor lifestyle culture make pools a popular feature in higher-value Gisborne properties."),
}

def pool_article(city_key):
    c = NEW_CITIES[city_key]
    city, region = c["name"], c["region"]
    concrete, premium, fibreglass, local = POOL_DATA[city_key]
    return f"""---
title: "Pool Builders {city} 2026 — Swimming Pool Costs, Types and What to Expect"
description: "Pool builders {city} 2026 — {city} swimming pool costs, concrete vs fibreglass prices, pool consent requirements, and how to find a reliable pool builder near you."
image: "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["pool builders {city}", "swimming pool cost {city}", "pool installation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what swimming pools cost in {city} in 2026.

## {city} Swimming Pool Costs 2026

| Pool type | {city} typical cost |
|---|---|
| Fibreglass pool (6–8m) | {fibreglass} |
| Concrete pool (standard) | {concrete} |
| Concrete pool (custom, premium) | {premium} |
| Above-ground pool | $4,000–$15,000 |
| Spa pool / hot tub | $8,000–$30,000 |
| Pool heat pump (add-on) | $4,500–$9,000 |
| Pool fencing (compliant, per m linear) | $385–$960/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Pool Market

{local}

## Consent Requirements

All pools over 400mm deep require building consent from {region} Council and compliant pool fencing (NZ Building Code Clause F9). Pool fencing is non-negotiable — non-compliance creates serious liability risk.

**Find {city} pool builders:** [Pool Builders {city}](/trades/pool-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

for ck in NEW_CITIES:
    ARTICLES += [
        (f"bathroom-renovator-{ck}-nz",        lambda k=ck: bathroom_article(k)),
        (f"kitchen-renovator-{ck}-nz",         lambda k=ck: kitchen_article(k)),
        (f"deck-builder-{ck}-nz",              lambda k=ck: deck_article(k)),
        (f"floor-sander-{ck}-nz",             lambda k=ck: floor_article(k)),
        (f"glazier-{ck}-nz",                   lambda k=ck: glazier_article(k)),
        (f"ev-charger-installation-{ck}-nz",   lambda k=ck: ev_article(k)),
        (f"switchboard-upgrade-{ck}-nz",       lambda k=ck: switch_article(k)),
        (f"pergola-builder-{ck}-nz",           lambda k=ck: pergola_article(k)),
        (f"rubbish-removal-{ck}-nz",           lambda k=ck: rubbish_article(k)),
        (f"pool-builder-{ck}-nz",              lambda k=ck: pool_article(k)),
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
