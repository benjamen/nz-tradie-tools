#!/usr/bin/env python3
"""
Wave 10 SEO content generator — TradieTools NZ
Gap fills: EV charger, switchboard, pest control, glazier for smaller cities
New trades: pool builder (main cities)
New national guides: hot water cylinder, blocked drain, smoke alarm, rewire house
Run: python3 generate_wave10.py
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

SMALL_CITIES = ["napier", "new-plymouth", "palmerston-north", "nelson", "rotorua"]

# ── EV Charger (smaller cities) ───────────────────────────────────────────────

EV_SMALL = {
    "napier":           ("$880–$1,750", "$1,350–$2,750", "Napier's sunny Hawke's Bay climate and growing professional community are driving EV adoption. The city's layout suits EV commuting well — most trips within Napier are well within a single charge."),
    "new-plymouth":     ("$880–$1,750", "$1,350–$2,750", "New Plymouth's growing tech and energy sector workforce is adopting EVs rapidly. The city's compact layout makes EV ownership practical, and home charging overnight eliminates range anxiety."),
    "palmerston-north": ("$860–$1,720", "$1,320–$2,700", "Palmerston North's large public sector and university community is embracing EVs. Massey University and local government fleet electrification is raising awareness of EV charger installation across the city."),
    "nelson":           ("$880–$1,750", "$1,350–$2,750", "Nelson's environmentally-conscious community is among NZ's keenest EV adopters. The region's short commute distances suit EVs perfectly, and Nelson's high sunshine hours make solar + EV charging a popular combination."),
    "rotorua":          ("$860–$1,720", "$1,320–$2,700", "Rotorua's tourism sector is increasingly using EVs for fleet vehicles and tours. Residential EV adoption is growing as the city's younger professional population upgrades to electric vehicles."),
}

def ev_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    level2, smart, local = EV_SMALL[city_key]
    return f"""---
title: "EV Charger Installation {city} 2026 — Home EV Charging Costs and What to Expect"
description: "EV charger installation {city} 2026 — {city} home EV charger costs, Level 2 charging prices, smart charger options, and how to find a qualified electrician near you."
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
| Three-phase charger (22kW, supply + install) | $2,100–$4,300 |
| Installation labour only (charger supplied) | $320–$700 |
| Switchboard upgrade (if required) | $1,400–$3,200 |
| Additional cabling run (per metre) | $32–$70/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Level 1 vs Level 2 Charging

**Level 1 (standard 10A wall socket):** ~15km range per hour. Fine for plug-in hybrids or very low mileage. **Not recommended** for daily EV drivers.

**Level 2 (dedicated 7kW circuit):** ~50km per hour. Charges a full EV battery overnight. **Recommended for most owners.** Requires a licensed electrician to install a dedicated 32A circuit.

## Smart Charger Benefits

Smart chargers allow off-peak scheduling (charge when electricity is cheapest), app monitoring, and solar integration. Popular NZ brands: Wallbox, EVNEX, Ohme.

## Installation Requirements

EV charger installation is **restricted electrical work** — must be done by a registered electrician who will issue an Electrical Certificate of Compliance. Older homes may need a switchboard upgrade first.

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Electricians {city}](/articles/electrician-{city_key}-nz/) | [Switchboard Upgrade {city}](/articles/switchboard-upgrade-{city_key}-nz/) | [Solar Installers {city}](/articles/solar-installer-{city_key}-nz/)*
"""


# ── Switchboard Upgrade (smaller cities) ──────────────────────────────────────

SWITCH_SMALL = {
    "napier":           ("$2,000–$4,200", "$3,200–$6,000", "Napier's post-earthquake housing includes older electrical systems in pre-1931 rebuilt homes. As EV chargers and heat pumps are added, many Napier homes need switchboard upgrades to support the increased load."),
    "new-plymouth":     ("$2,000–$4,200", "$3,200–$6,000", "New Plymouth's mix of older and newer housing creates steady switchboard upgrade demand. Homes in the oil and gas sector often have industrial-standard electrical work — residential upgrades follow NZ residential standards."),
    "palmerston-north": ("$1,900–$4,000", "$3,000–$5,800", "Palmerston North's 1960s–80s housing belt has many original fuse boards approaching end of life. The student accommodation sector also drives regular electrical upgrade work."),
    "nelson":           ("$2,000–$4,200", "$3,200–$6,000", "Nelson's active renovation market and solar adoption drive switchboard upgrades. Many older Nelson homes need board upgrades to support solar inverters and EV chargers simultaneously."),
    "rotorua":          ("$1,900–$4,000", "$3,000–$5,800", "Rotorua's older housing stock has electrical systems due for replacement. Geothermal corrosion can affect older wiring and fittings — electricians in Rotorua are familiar with geothermal-related electrical issues."),
}

def switch_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    standard, complex_, local = SWITCH_SMALL[city_key]
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
| Standard switchboard upgrade (single-phase) | {standard} |
| Complex upgrade (three-phase or rewire) | {complex_} |
| Add RCD / safety switch to existing board | $270–$560 |
| Add individual circuit breaker | $170–$360 |
| Switchboard inspection / report | $170–$330 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Switchboard Market

{local}

## When Do You Need an Upgrade?

Your home likely needs a switchboard upgrade if it has ceramic fuse holders, no RCDs (safety switches), frequent fuse-blowing, or if you're adding an EV charger, solar system, heat pump, or induction cooktop. Older fuse boards simply don't have the capacity for modern high-draw appliances.

## What's Included

A full upgrade includes: replace fuse board with modern circuit breaker panel, install RCDs on all circuits, label and test, issue Electrical Certificate of Compliance (eCoC). Must be done by a registered electrician.

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Electricians {city}](/articles/electrician-{city_key}-nz/) | [EV Charger Installation {city}](/articles/ev-charger-installation-{city_key}-nz/)*
"""


# ── Pest Control (smaller cities) ─────────────────────────────────────────────

PEST_SMALL = {
    "napier":           ("$170–$360", "$260–$620", "Napier's warm Hawke's Bay climate suits a range of pests. The 2023 Cyclone Gabrielle caused significant flooding that displaced rats and other pests across Hawke's Bay — pest control demand surged and remains elevated."),
    "new-plymouth":     ("$170–$360", "$260–$620", "New Plymouth's coastal and bush margins create pressure from wasps and rodents. The Taranaki's rural-urban fringe also brings possums and other pest species close to residential areas."),
    "palmerston-north": ("$160–$340", "$240–$580", "Palmerston North's student rental market drives ongoing pest control work — bed bugs and cockroaches are common in high-turnover rental properties. Rodents are the most common residential call-out."),
    "nelson":           ("$170–$360", "$260–$620", "Nelson's warmer climate and fruit-growing industry create pest pressure — wasps (attracted to fallen fruit), ants, and rodents are common. The lifestyle property market also encounters possums and other rural pests."),
    "rotorua":          ("$160–$340", "$240–$580", "Rotorua's geothermal environment and bush surroundings bring rodents and insects close to homes. The tourism accommodation sector has stringent pest control requirements — hotels and motels are major pest control clients."),
}

def pest_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    callout, quarterly, local = PEST_SMALL[city_key]
    return f"""---
title: "Pest Control {city} 2026 — Pest Control Costs, Common Pests and What to Expect"
description: "Pest control {city} 2026 — {city} pest control costs, rodent treatment prices, cockroach and wasp extermination rates, and how to find a reliable pest controller near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["pest control {city}", "pest controller {city}", "pest exterminator {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what pest control costs in {city} in 2026.

## {city} Pest Control Costs 2026

| Service | {city} typical cost |
|---|---|
| Inspection / assessment | $95–$210 |
| Rodent treatment (baiting, 3-bed home) | {callout} |
| Cockroach treatment (3-bed home) | $170–$360 |
| Ant treatment (exterior + interior) | $150–$300 |
| Wasp nest removal | $120–$260 |
| Flea treatment (3-bed home) | $170–$360 |
| Borer treatment (spray, per m²) | $11–$26/m² |
| Ongoing maintenance contract (quarterly) | {quarterly} |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Pest Situation

{local}

## Common Pests in {city}

**Rodents:** Most common call-out. Signs include droppings, gnaw marks, scratching sounds at night. Treatment: baiting stations inside and out, follow-up visit.

**Wasps:** NZ's German wasp is aggressive — large nests should only be treated by professionals, at night when wasps are inactive.

**Borer:** Common in NZ timber homes. Treat in summer when larvae are near the surface.

**Cockroaches:** Multiple treatment visits needed to break the egg cycle.

Pest controllers applying restricted pesticides must hold a GROWSAFE certificate. Always ask for proof before allowing treatment.

**Find {city} pest controllers:** [Pest Control {city}](/trades/pest-control/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Pest Control Cost NZ](/articles/pest-control-cost-nz/)*
"""


# ── Glazier (smaller cities) ──────────────────────────────────────────────────

GLAZIER_SMALL = {
    "napier":           ("$170–$390", "$330–$880", "$780–$2,400", "Napier's warm climate still drives double glazing interest — keeping summer heat out is as important as winter warmth retention. The art deco city's character buildings use glazing as an architectural feature."),
    "new-plymouth":     ("$175–$395", "$340–$890", "$790–$2,450", "New Plymouth's coastal westerly winds make good glazing important for thermal comfort. Double glazing significantly reduces noise and heat loss in homes facing the prevailing westerlies."),
    "palmerston-north": ("$165–$380", "$320–$860", "$760–$2,350", "Palmerston North's cold winters and windy conditions make glazing upgrades particularly worthwhile. Double glazing reduces condensation — a significant issue in Manawatu's cold, damp winters."),
    "nelson":           ("$170–$390", "$330–$880", "$780–$2,400", "Nelson's sunny climate reduces heating demand but cold winter nights still make insulation important. Large glazed areas to capture Nelson's sun are popular — low-E double glazing balances solar gain in summer and heat retention in winter."),
    "rotorua":          ("$165–$380", "$320–$860", "$760–$2,350", "Rotorua's cold winters make glazing upgrades worthwhile. The geothermal environment's hydrogen sulphide can corrode aluminium frames faster than normal — quality anodised or powder-coated frames are recommended."),
}

def glazier_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    callout, repair, window, local = GLAZIER_SMALL[city_key]
    return f"""---
title: "Glaziers {city} 2026 — Glass Repair Costs, Window Replacement Prices and What to Expect"
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
| Emergency glass replacement (after hours) | $280–$650 |
| Single glaze repair / replacement (per pane) | {repair} |
| Double glazing replacement (per pane) | $430–$1,150 |
| Window replacement — aluminium (per window) | {window} |
| Double glazing retrofit (per window) | $780–$2,400 |
| Shower screen supply and fit | $760–$2,400 |
| Glass splashback (per m²) | $240–$580/m² |
| Glass balustrade (per m linear) | $380–$980/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Glazing Market

{local}

## Safety Glass Requirements

NZ Building Code requires safety (toughened or laminated) glass within 500mm of doors, at low levels (below 1,050mm), in wet areas, and at stairways/balustrades. When replacing glass in older homes, confirm replacement meets current code.

## Double Glazing Worth It in {city}?

Yes — double glazing reduces heat loss through windows by ~50%, cuts condensation, and improves acoustic insulation. Retrofitting secondary glazing units into existing aluminium frames costs $400–$900 per window — cheaper than full window replacement.

**Find {city} glaziers:** [Glaziers {city}](/trades/glaziers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Window Replacement Cost NZ](/articles/window-replacement-cost-nz/) | [Insulation Installers {city}](/articles/insulation-installer-{city_key}-nz/)*
"""


# ── Pool Builder (main cities) ────────────────────────────────────────────────

POOL_DATA = {
    "auckland":     ("$55,000–$95,000", "$95,000–$180,000+", "$28,000–$55,000", "Auckland's subtropical climate makes pools a popular lifestyle upgrade. The long summers (November–April) give strong return on investment. However, Auckland's dense sections mean pool placement requires careful planning — many sections have limited space and complex consent requirements."),
    "wellington":   ("$55,000–$95,000", "$90,000–$170,000+", "$28,000–$55,000", "Wellington's cool southerly winds and shorter summers make pools less popular than in Auckland. Heated pools or those in sheltered north-facing gardens perform well. Indoor or covered pools are more justifiable in Wellington's climate."),
    "christchurch": ("$50,000–$88,000", "$88,000–$160,000+", "$25,000–$50,000", "Christchurch's hot dry summers make pools a popular feature. The city's flat, spacious sections suit pool installation well. Post-earthquake rebuilds sometimes incorporated pools into new home designs."),
    "hamilton":     ("$48,000–$85,000", "$85,000–$155,000+", "$23,000–$48,000", "Hamilton's hot humid Waikato summers make pools attractive. The city's large suburban sections provide good space. Hamilton's pool market is price-competitive — several installers operate in the Waikato region."),
    "tauranga":     ("$50,000–$88,000", "$88,000–$160,000+", "$25,000–$50,000", "Tauranga's warm Bay of Plenty climate — one of NZ's warmest — makes pools excellent value. The beach and lifestyle culture means pools are a common feature in Tauranga's higher-value homes."),
    "dunedin":      ("$45,000–$80,000", "$80,000–$150,000+", "$22,000–$45,000", "Dunedin's cold climate makes outdoor pools less popular — the swimming season is short. Heated indoor or semi-enclosed pools are more common. Fibreglass pools with good heating systems can be used from November to March."),
}

def pool_article(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    concrete, premium, fibreglass, local = POOL_DATA[city_key]
    return f"""---
title: "Pool Builders {city} 2026 — Swimming Pool Costs, Types and What to Expect"
description: "Pool builders {city} 2026 — {city} swimming pool costs, concrete vs fibreglass prices, pool consent requirements, running costs, and how to find a reliable pool builder near you."
image: "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["pool builders {city}", "swimming pool cost {city}", "pool installation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what swimming pools cost to install in {city} in 2026.

## {city} Swimming Pool Costs 2026

| Pool type | {city} typical cost (supply + install) |
|---|---|
| Fibreglass pool (6–8m, basic) | {fibreglass} |
| Concrete pool (6–8m, standard) | {concrete} |
| Concrete pool (custom, premium) | {premium} |
| Above-ground pool (steel/resin) | $4,000–$15,000 |
| Spa pool / hot tub | $8,000–$30,000 |
| Pool heating — heat pump (add-on) | $4,500–$9,000 |
| Pool fencing (compliant, per m linear) | $380–$950/m |
| Pool safety cover (motorised) | $5,000–$15,000 |
| Pool renovation / resurfacing | $8,000–$25,000 |
| Annual pool maintenance service | $800–$2,500/year |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Concrete vs Fibreglass

| | Concrete | Fibreglass |
|---|---|---|
| Upfront cost | Higher | Lower |
| Customisation | Any shape/size | Pre-made shells (limited shapes) |
| Installation time | 3–6 months | 6–8 weeks |
| Lifespan | 50+ years | 25–30 years |
| Maintenance | Higher (resurfacing every 10–15yr) | Lower |
| Best for | Large/custom designs | Standard sizes, faster install |

## {city} Pool Market

{local}

## Pool Consent Requirements in {city}

In NZ, all pools capable of holding water deeper than 400mm require:

1. **Building consent** from {region} Council before construction
2. **Pool fencing** compliant with NZ Building Code (Clause F9) — 1.2m minimum height, specific gate latch requirements
3. **Compliance certificate** on completion
4. **Pool safety inspection** — councils can inspect at any time

**Pool fencing is non-negotiable** — non-compliant pool fencing can result in council enforcement action and personal liability if a drowning occurs. Always use a compliant pool fencing installer.

## Running Costs

Factor in ongoing costs for a {city} pool:

| Cost item | Typical annual cost |
|---|---|
| Chemicals (chlorine, pH, algaecide) | $600–$1,500 |
| Electricity (pump, heating) | $800–$2,500 |
| Professional servicing | $800–$2,000 |
| **Total running cost** | **$2,200–$6,000/year** |

A pool heat pump extends your season by 2–3 months and adds $200–$600/year to electricity costs.

**Find {city} pool builders:** [Pool Builders {city}](/trades/pool-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a swimming pool cost in {city}?**
Fibreglass (6–8m): {fibreglass}. Concrete (standard): {concrete}. Premium custom concrete: {premium}.

**Do I need consent for a pool in {city}?**
Yes — all pools over 400mm deep require building consent and must have compliant fencing. Apply to {region} Council before any work starts.

**How long does pool installation take?**
Fibreglass: 6–8 weeks. Concrete: 3–6 months. Consent processing adds time — apply early.

---

*Related: [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/) | [Fence Installers {city}](/articles/fence-installer-{city_key}-nz/)*
"""


# ── National Cost Guides ──────────────────────────────────────────────────────

def hot_water_article():
    return f"""---
title: "Hot Water Cylinder Replacement Cost NZ 2026 — Prices, Types and What to Expect"
description: "Hot water cylinder replacement cost NZ 2026 — electric vs heat pump vs gas vs solar hot water costs, cylinder sizes, installation prices, and how to find a reliable plumber near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["hot water cylinder cost NZ", "hot water cylinder replacement NZ", "water heater cost NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Replacing a hot water cylinder is one of the most common plumbing jobs in New Zealand. Here's what it costs in 2026 and what you need to know about the options.

## Hot Water Cylinder Replacement Cost NZ 2026

| Type | Supply + installation |
|---|---|
| Electric cylinder (180L, standard) | $1,800–$3,200 |
| Electric cylinder (250–300L, large home) | $2,200–$3,900 |
| Heat pump hot water (180–250L) | $3,800–$7,500 |
| Gas continuous flow (no tank) | $1,700–$3,300 |
| Gas storage cylinder (135–180L) | $2,000–$3,600 |
| Solar hot water (evacuated tube, 300L) | $4,500–$8,500 |
| Wetback (open fire connection) | $2,500–$5,500 |
| Disposal of old cylinder | $80–$200 |

*All prices GST inclusive. Prices vary by brand, cylinder size, and installation complexity.*

## Which Hot Water System Is Best for NZ?

### Electric Cylinder
**Best for:** Most NZ homes. Simple, reliable, cheap to buy. Running cost is higher than alternatives but the upfront cost is low. Use with an off-peak timer (cheapest electricity rates at night).

### Heat Pump Hot Water
**Best for:** Homes wanting the lowest running cost. Extracts heat from the air — 3–4x more efficient than a standard electric element. Upfront cost is high but energy savings typically pay back in 4–7 years. Needs space around the unit. Performance reduces in very cold climates (below 5°C).

### Gas Continuous Flow
**Best for:** Homes with natural gas connected who want hot water on demand. No storage tank means endless hot water and no standby heat loss. Not suitable where gas isn't available.

### Solar Hot Water
**Best for:** Homes with good north-facing roof space and high hot water usage. Works well in sunny regions (Nelson, Hawke's Bay, Bay of Plenty). Needs electric or gas backup for cloudy periods.

## When to Replace vs Repair

| Symptom | Likely action |
|---|---|
| Cylinder over 12–15 years old | Replace proactively |
| Rusty or discoloured water | Replace (corrosion inside tank) |
| Small leak from cylinder body | Replace |
| No hot water, element failed | Repair (replace element, $300–$600) |
| Thermostat fault | Repair ($200–$400) |
| Relief valve dripping | Repair ($150–$300) |

Hot water cylinders have a typical lifespan of 10–15 years. After 15 years, replacement is usually more cost-effective than ongoing repairs.

## Installation Requirements

- All hot water cylinder installation is **restricted plumbing work** in NZ
- Must be done by a registered plumber (or gasfitter for gas systems)
- A **plumbing compliance certificate** is legally required
- Electric connections must be done by a registered electrician
- Heat pump hot water also requires a refrigeration technician for installation

**Find a plumber:** [Plumbers Near You](/trades/plumbers/) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a hot water cylinder replacement cost in NZ?**
Standard electric (180L, supply + install): $1,800–$3,200. Heat pump hot water: $3,800–$7,500. Gas continuous flow: $1,700–$3,300.

**How long does hot water cylinder replacement take?**
A standard electric cylinder replacement: 2–4 hours. Heat pump hot water: 4–6 hours. Gas systems may need both a plumber and gasfitter.

**Do I need a plumber to replace a hot water cylinder in NZ?**
Yes — hot water cylinder installation is restricted plumbing work. A compliance certificate is legally required.

**Is a heat pump hot water cylinder worth it in NZ?**
Yes for most NZ homes — saves $600–$1,200/year on electricity versus a standard electric cylinder. Payback typically 4–7 years.

---

*Related: [Plumbers Near You](/trades/plumbers/) | [Gas Fitting Cost NZ](/articles/gas-fitting-cost-nz/)*
"""


def blocked_drain_article():
    return f"""---
title: "Blocked Drain Cost NZ 2026 — Prices, Causes and How to Fix It"
description: "Blocked drain cost NZ 2026 — plumber call-out costs for blocked drains, water jetting prices, drain camera inspection costs, and when to call a drainlayer vs plumber."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["blocked drain cost NZ", "blocked drain NZ", "drain unblocking cost NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

A blocked drain is one of the most common plumbing call-outs in NZ. Here's what it costs to fix and what to expect from the process.

## Blocked Drain Cost NZ 2026

| Service | Typical NZ cost |
|---|---|
| Plumber call-out (standard hours) | $100–$180 |
| Plumber call-out (after hours/weekend) | $180–$380 |
| Hand rodding / snake to unblock | $180–$380 |
| High-pressure water jetting | $220–$550 |
| Drain camera inspection | $280–$550 |
| Root cutting treatment | $320–$750 |
| Drain repair (pipe patch, per metre) | $400–$950/m |
| Drain replacement (open cut, per metre) | $500–$1,200/m |
| No-dig pipe relining (per metre) | $450–$900/m |

*All prices GST inclusive. Auckland and Wellington typically at the higher end.*

## Plumber vs Drainlayer — Who Do You Call?

**Plumber:** Call for blockages inside the house — kitchen sink, bathroom basin, shower, toilet. Plumbers handle internal drainage.

**Drainlayer:** Call for blockages in the underground drainage between your house and the street, or sewer/stormwater connections. Drainlayers are licensed to work on the underground network.

**Not sure?** Call a plumber first — they'll refer to a drainlayer if the blockage is in the underground drainage.

## Common Causes of Blocked Drains in NZ

| Cause | Location | Fix |
|---|---|---|
| Fat/grease buildup | Kitchen drain | Water jetting, preventative |
| Hair / soap buildup | Shower, basin | Rodding, strainer |
| Tree root intrusion | Underground drain | Root cutting, relining or replacement |
| Collapsed pipe (old clay/concrete) | Underground | Camera, repair or replace |
| Foreign objects | Toilet | Rodding |
| Mineral buildup (scale) | Any pipe | Jetting, descaling |

## Signs of a Blocked Drain

- Slow-draining sink, shower, or bath
- Gurgling sounds from drains or toilet
- Sewage smells from drains
- Water backing up in one fixture when another is used
- Wet patches in the yard over drain lines

## After-Hours Call-Out

Emergency (after-hours) blocked drain call-outs cost significantly more — $180–$380 call-out, then standard rates per hour. For non-urgent blockages (slow drains, no overflow), waiting until business hours saves money.

**Find a plumber:** [Plumbers Near You](/trades/plumbers/) | [Drainlayers Near You](/trades/drainlayers/) | [Post a Job Free](/post-job/)

---

**How much does a plumber charge to unblock a drain in NZ?**
Call-out + unblocking: $280–$550 for a standard blockage. Water jetting: $220–$550. Camera inspection: $280–$550.

*Related: [Plumber Cost NZ](/articles/plumber-pricing-guide-nz-2026/) | [Drainlayers NZ](/trades/drainlayers/)*
"""


def smoke_alarm_article():
    return f"""---
title: "Smoke Alarm Installation Cost NZ 2026 — Prices, Requirements and What to Expect"
description: "Smoke alarm installation cost NZ 2026 — NZ smoke alarm requirements, photoelectric vs ionisation, interconnected alarm costs, and how to find a qualified installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["smoke alarm installation NZ", "smoke alarm cost NZ", "smoke alarms NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

NZ law requires working smoke alarms in all homes. Here's what installation costs in 2026 and what the requirements are.

## Smoke Alarm Installation Cost NZ 2026

| Service | Typical NZ cost |
|---|---|
| Single smoke alarm (supply + install) | $65–$180 |
| Photoelectric alarm (10-year sealed battery, supply + install) | $95–$220 |
| Interconnected alarm system (per alarm, supply + install) | $130–$280 |
| Hard-wired alarm (per alarm, electrician required) | $180–$380 |
| Alarm test / maintenance visit | $80–$180 |
| Carbon monoxide detector (supply + fit) | $95–$220 |

*All prices GST inclusive.*

## NZ Smoke Alarm Requirements

**All NZ homes must have:**
- At least one working smoke alarm per floor
- Alarms within 3 metres of each bedroom door
- **Photoelectric alarms only** (ionisation alarms no longer acceptable for new installs under the Residential Tenancies Act)
- Long-life (10-year) sealed battery alarms recommended

**Rental properties (Healthy Homes Standards):**
- At least one alarm per floor
- Alarm within 3m of each sleeping area
- Must be photoelectric (not ionisation)
- Must have long-life battery or be hard-wired
- Tenants cannot be left without working alarms

**New builds:**
- Interconnected alarms required — if one triggers, all sound
- Hard-wired with battery backup recommended

## Photoelectric vs Ionisation

| | Photoelectric | Ionisation |
|---|---|---|
| Detects | Smouldering fires (slow burn) | Fast flaming fires |
| False alarms | Less prone | More prone (cooking) |
| NZ requirement | **Required for all new installs** | Not acceptable for new installs |
| 10-year sealed battery | Available | Available |

**Always buy photoelectric alarms for NZ homes.**

## DIY vs Professional Installation

**DIY (battery alarms):** Battery-powered smoke alarms can be installed by homeowners — no electrical licence required. Follow manufacturer instructions for placement.

**Professional required for:** Hard-wired alarms or interconnected wireless systems. Hard-wired installation is restricted electrical work requiring a registered electrician.

**Find an electrician:** [Electricians Near You](/trades/electricians/) | [Post a Job Free](/post-job/)

---

**How much does smoke alarm installation cost in NZ?**
Single photoelectric alarm (supply + install): $95–$220. Full home system (4 alarms, interconnected): $520–$1,120.

**What type of smoke alarm is required in NZ?**
Photoelectric only — ionisation alarms are not acceptable for new installs under the Residential Tenancies Act 2016.

*Related: [Electricians Near You](/trades/electricians/)*
"""


def rewire_article():
    return f"""---
title: "Rewire a House Cost NZ 2026 — Full and Partial Rewiring Prices"
description: "Rewire a house cost NZ 2026 — full house rewire cost, partial rewire pricing, signs you need a rewire, and how to find a qualified electrician near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["rewire house cost NZ", "house rewire NZ", "electrical rewire NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Rewiring a house is one of the largest electrical jobs you can undertake. Here's what it costs in NZ in 2026 and when you need one.

## House Rewire Cost NZ 2026

| Service | Typical NZ cost |
|---|---|
| Full rewire — 2-bedroom home | $8,000–$18,000 |
| Full rewire — 3-bedroom home | $12,000–$25,000 |
| Full rewire — 4-bedroom home | $16,000–$35,000 |
| Partial rewire (specific circuits) | $1,500–$6,000 |
| Switchboard upgrade (often done with rewire) | $2,000–$5,000 |
| Additional power point (per point) | $180–$380 |
| New circuit installation | $350–$750 |

*All prices GST inclusive. Auckland and Wellington at the higher end. Prices vary significantly based on home layout, wall construction, and accessibility.*

## Signs You Need a Rewire

**Your home may need rewiring if it has:**
- Wiring over 30–40 years old (especially aluminium wiring from the 1960s–70s)
- Ceramic fuse holders instead of circuit breakers
- Outlets with only two pins (no earth)
- Flickering lights or frequently tripping breakers
- Burning smell from switches or outlets
- Scorch marks around outlets or switches
- Rubber or fabric insulation (original knob-and-tube wiring)

**After a major renovation:** If walls are opened up, it's often the right time to upgrade wiring in those areas.

## Aluminium Wiring — A NZ Issue

Homes built between approximately 1965 and 1975 may have **aluminium wiring** instead of copper. Aluminium wiring expands and contracts more than copper, causing connections to loosen over time — a fire risk. Signs: warm outlets or switch plates, flickering lights.

**If your home has aluminium wiring:** Have an electrician assess it. Options include full rewire, fitting aluminium-compatible outlets and switches, or installing pigtail connectors at all connection points.

## What's Involved in a Full Rewire

1. **Assessment:** Electrician inspects existing wiring and plans the new layout
2. **Switchboard upgrade:** Old fuse board replaced with modern circuit breakers and RCDs
3. **Cable installation:** New cables run through walls and ceiling — may require opening wall linings in some areas
4. **New outlets and switches:** All points replaced
5. **Testing:** Full testing of all circuits
6. **Certificate:** Electrical Certificate of Compliance (eCoC) issued

**Rewiring and decoration:** Cable runs through walls may require making good after the electrician finishes. Factor in plastering and painting costs.

## Partial Rewire

If only specific circuits are problematic or you're renovating specific rooms, a partial rewire is more cost-effective. Common partial rewires:
- Kitchen circuits (new oven, induction cooktop)
- Bathroom circuits
- Addition of new circuits (EV charger, heat pump)
- Garage or workshop circuits

## Is a Rewire Restricted Work?

Yes — all electrical wiring is **restricted electrical work** in NZ. Must be done by a registered electrician who will issue an Electrical Certificate of Compliance. Never attempt DIY electrical wiring.

**Find an electrician:** [Electricians Near You](/trades/electricians/) | [Post a Job Free](/post-job/)

---

**How much does it cost to rewire a house in NZ?**
3-bedroom home: $12,000–$25,000 for a full rewire including new switchboard. Partial rewire (single room or circuit): $1,500–$6,000.

**How long does a house rewire take?**
2-bed home: 3–5 days. 3-bed home: 5–8 days. Larger or complex homes: 1–3 weeks.

*Related: [Electricians Near You](/trades/electricians/) | [Switchboard Upgrade Cost NZ](/articles/switchboard-upgrade-auckland-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

for ck in SMALL_CITIES:
    ARTICLES.append((f"ev-charger-installation-{ck}-nz",  lambda k=ck: ev_small(k)))
    ARTICLES.append((f"switchboard-upgrade-{ck}-nz",      lambda k=ck: switch_small(k)))
    ARTICLES.append((f"pest-control-{ck}-nz",             lambda k=ck: pest_small(k)))
    ARTICLES.append((f"glazier-{ck}-nz",                  lambda k=ck: glazier_small(k)))

for ck in ["auckland","wellington","christchurch","hamilton","tauranga","dunedin"]:
    ARTICLES.append((f"pool-builder-{ck}-nz", lambda k=ck: pool_article(k)))

ARTICLES += [
    ("hot-water-cylinder-cost-nz",   hot_water_article),
    ("blocked-drain-cost-nz",        blocked_drain_article),
    ("smoke-alarm-installation-nz",  smoke_alarm_article),
    ("rewire-house-cost-nz",         rewire_article),
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
