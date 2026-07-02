#!/usr/bin/env python3
"""
Wave 4 SEO content generator — TradieTools NZ
New trades: arborist, fence installer, insulation installer, solar installer
Gap fills: tiler, carpenter, painter for remaining cities
Run: python3 generate_wave4.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

CITIES = {
    "auckland":         {"name":"Auckland",         "region":"Auckland",                 "rate_adj":"15–25% above national average", "pop":"1.7M"},
    "wellington":       {"name":"Wellington",        "region":"Wellington",               "rate_adj":"comparable to Auckland",         "pop":"215,000"},
    "christchurch":     {"name":"Christchurch",      "region":"Canterbury",               "rate_adj":"below Auckland and Wellington",   "pop":"400,000"},
    "hamilton":         {"name":"Hamilton",          "region":"Waikato",                  "rate_adj":"10–15% below Auckland",          "pop":"170,000"},
    "tauranga":         {"name":"Tauranga",          "region":"Bay of Plenty",            "rate_adj":"broadly similar to Hamilton",     "pop":"155,000"},
    "dunedin":          {"name":"Dunedin",           "region":"Otago",                    "rate_adj":"10–20% below Auckland",          "pop":"130,000"},
    "napier":           {"name":"Napier",            "region":"Hawke's Bay",              "rate_adj":"broadly regional",               "pop":"65,000"},
    "new-plymouth":     {"name":"New Plymouth",      "region":"Taranaki",                 "rate_adj":"broadly regional",               "pop":"58,000"},
    "palmerston-north": {"name":"Palmerston North",  "region":"Manawatu-Whanganui",       "rate_adj":"broadly regional",               "pop":"90,000"},
    "nelson":           {"name":"Nelson",            "region":"Nelson-Tasman",            "rate_adj":"broadly regional",               "pop":"55,000"},
    "rotorua":          {"name":"Rotorua",           "region":"Bay of Plenty",            "rate_adj":"broadly regional",               "pop":"60,000"},
}

# ── Arborist ──────────────────────────────────────────────────────────────────

ARBORIST_LOCAL = {
    "auckland":     "Auckland's fast-growing urban tree canopy and regular storms make arborist work year-round. Pohutukawa, Norfolk pine, and large eucalyptus are common removal requests. Council consent is required for many tree removals in Auckland — check the Unitary Plan.",
    "wellington":   "Wellington's exposed hilltop sections and powerful northerly winds mean storm damage and preventative pruning are constant arborist work. Many Wellington suburbs have character trees protected under district plan rules.",
    "christchurch": "Post-earthquake Christchurch saw significant tree loss, but the city is rebuilding its canopy. Tree removal in Christchurch often requires consent — check with Christchurch City Council before any removal work.",
    "hamilton":     "Hamilton's leafy suburbs and the Waikato's fertile soils grow large trees quickly. Mature oaks, liquid ambers, and natives in older Hamilton suburbs regularly need professional management.",
    "tauranga":     "Tauranga's coastal setting brings pohutukawa, cabbage trees, and palms alongside introduced species. Salt-wind damage is a factor for coastal trees, and strong growth rates in the Bay of Plenty's warm climate mean regular pruning is important.",
    "napier":       "Napier's Mediterranean-style climate supports large established trees. Macrocarpa, pine, and large deciduous trees in older Hawke's Bay properties are common arborist jobs.",
    "new-plymouth": "New Plymouth's proximity to the Taranaki bush and strong prevailing westerlies means storm damage and preventative pruning are regular work. The coastal esplanade trees require specialist coastal arborist knowledge.",
    "palmerston-north": "Palmerston North's wide streets and parks feature mature exotic trees. The Manawatu's windy conditions drive regular storm damage callouts, and older suburban sections have large trees approaching end of life.",
    "nelson":       "Nelson's sunny climate and fertile Tasman soils produce fast-growing trees. The lifestyle block market around Nelson and the Waimea Plains generates rural tree work alongside urban arborist services.",
    "rotorua":      "Rotorua's volcanic soils and high rainfall grow trees rapidly. The geothermal environment can affect tree health in some areas. The city's tourism parks and large lakeside properties drive professional arborist demand.",
}

def arborist_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    local = ARBORIST_LOCAL.get(city_key, f"{city} has steady arborist demand for tree removal, pruning, and maintenance.")

    rates = {
        "auckland":     ("$250–$600/hr", "$800–$3,500", "$350–$1,500", "$5,000–$20,000+"),
        "wellington":   ("$250–$600/hr", "$800–$3,500", "$350–$1,500", "$5,000–$20,000+"),
        "christchurch": ("$200–$500/hr", "$600–$3,000", "$300–$1,200", "$4,000–$18,000"),
        "hamilton":     ("$200–$480/hr", "$600–$2,800", "$280–$1,100", "$3,500–$15,000"),
        "tauranga":     ("$210–$500/hr", "$650–$3,000", "$300–$1,200", "$4,000–$16,000"),
        "dunedin":      ("$190–$450/hr", "$550–$2,500", "$260–$1,000", "$3,000–$14,000"),
    }
    team, small, prune, large = rates.get(city_key, ("$200–$480/hr","$600–$2,800","$280–$1,100","$3,500–$15,000"))

    return f"""---
title: "Arborists {city} 2026 — Tree Removal Costs, Pruning Prices and What to Expect"
description: "Arborists {city} 2026 — {city} tree removal cost, pruning prices, stump grinding rates, council consent rules, and how to find a qualified arborist near you."
image: "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["arborists {city}", "arborist {city}", "tree removal {city}", "tree pruning {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{city} has a significant urban and suburban tree canopy that requires ongoing professional management. Here's what arborists charge in {city} in 2026 and what the work involves.

## {city} Arborist Rates 2026

| Service | {city} typical cost |
|---|---|
| Arborist team (hourly, 2-person + equipment) | {team} |
| Small tree removal (under 5m) | $400–$1,200 |
| Medium tree removal (5–10m) | {small} |
| Large tree removal (10–20m) | {large} |
| Very large / complex tree removal | $15,000–$50,000+ |
| Tree pruning / crown reduction (small tree) | {prune} |
| Tree pruning (large, per hour) | {team} |
| Stump grinding (per stump, small-medium) | $200–$600 |
| Emergency storm damage callout | $500–$3,000+ |
| Arborist report (for council consent) | $400–$1,200 |
| Hedge trimming (per hour) | $100–$200/hr |

*All prices GST inclusive. Tree removal costs vary enormously by size, access, proximity to structures, and disposal requirements.*

## {city} Arborist Market

{local}

## Council Consent for Tree Removal in {city}

Many trees in {city} are protected under the district or regional plan. Removing a protected tree without consent can result in significant fines. Before any tree removal:

1. Check the {region} Council's GIS mapping for protected trees on your property
2. Contact the council if in doubt — they can advise whether consent is needed
3. A qualified arborist can prepare the required arborist report for consent applications

**Protected categories typically include:** Notable trees listed on the district schedule, trees within riparian areas or significant ecological areas, and some trees over a certain girth or height threshold.

## Choosing a {city} Arborist

**Qualifications:** Look for NZ Arboricultural Association (NZAA) members or those with a New Zealand Certificate in Arboriculture. Avoid anyone who quotes over the phone without a site visit — reputable arborists assess every job in person.

**Insurance:** Arborist work is high-risk. Your arborist must carry public liability insurance (minimum $1M) and have worker's compensation cover. Ask for proof before work starts.

**Equipment:** A reputable arborist will use appropriate equipment — chipper for green waste, crane or rigging for large removals near structures.

**Quotes:** Always get 2–3 written quotes for any significant tree work.

**Find {city} arborists:** [Arborists {city}](/trades/arborists/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does tree removal cost in {city}?**
Small tree (under 5m): $400–$1,200. Medium (5–10m): {small}. Large (10–20m): {large}. Costs increase significantly with proximity to buildings, power lines, or difficult access.

**Do I need council consent to remove a tree in {city}?**
It depends on whether the tree is protected under the {region} plan. Check with the {region} Council before any removal — an arborist report may be required. Fines for removing protected trees without consent can be substantial.

**What is stump grinding?**
After tree removal, the stump can be ground to below ground level using a stump grinder. Cost: $200–$600 per stump. Without grinding, stumps can regrow (for some species) and are a trip hazard.

**Is arborist work dangerous?**
Yes — it's one of NZ's higher-risk trades. Always use a qualified, insured arborist. Never attempt large tree removal yourself.

---

*Related: [Landscaping Cost NZ](/articles/landscaping-cost-nz/) | [Garden Design Cost NZ](/articles/garden-design-cost-nz/)*
"""


# ── Fence Installer ───────────────────────────────────────────────────────────

FENCE_LOCAL = {
    "auckland":     "Auckland's high property density and relatively small sections mean fencing disputes and replacement work are common. Good fencing adds significant value in Auckland's competitive property market.",
    "wellington":   "Wellington's strong winds are a major factor in fencing choice and installation. Posts must be set deeper and concreted thoroughly — inadequate fencing regularly fails in Wellington's northerly and southerly winds.",
    "christchurch": "Christchurch's flat terrain makes fencing work straightforward, and the post-earthquake rebuild included many new boundary fences as properties were cleared and rebuilt.",
    "hamilton":     "Hamilton's growing suburban subdivisions generate strong demand for new boundary and pool fencing. The Waikato's fertile clay soils hold posts well but expand and contract seasonally.",
    "tauranga":     "Tauranga's coastal environment means salt air accelerates timber and metal corrosion. Treated pine, cedar, and powder-coated aluminium are popular choices for longevity in the Bay of Plenty.",
    "dunedin":      "Dunedin's steep sections and strong winds make fencing installation more complex than flat cities. Posts need thorough concrete footings — Dunedin's wind can bring down poorly installed fences.",
}

def fence_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    local = FENCE_LOCAL.get(city_key, f"{city} has steady demand for boundary, pool, and privacy fencing.")

    rates = {
        "auckland":     ("$150–$350/m", "$200–$500/m", "$180–$400/m"),
        "wellington":   ("$160–$370/m", "$210–$520/m", "$190–$420/m"),
        "christchurch": ("$130–$300/m", "$180–$450/m", "$160–$360/m"),
        "hamilton":     ("$120–$280/m", "$170–$420/m", "$150–$340/m"),
        "tauranga":     ("$130–$300/m", "$180–$450/m", "$160–$360/m"),
        "dunedin":      ("$120–$280/m", "$170–$420/m", "$150–$340/m"),
    }
    timber, pool, paling = rates.get(city_key, ("$130–$300/m","$180–$450/m","$160–$360/m"))

    return f"""---
title: "Fence Installers {city} 2026 — Fencing Costs, Materials and What to Expect"
description: "Fence installers {city} 2026 — {city} fencing costs per metre, timber vs aluminium vs concrete, pool fencing prices, and how to find a reliable fence installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["fence installers {city}", "fencing {city}", "fence cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{city} homeowners regularly need fencing for privacy, security, pool compliance, and boundary definition. Here's what fencing costs in {city} in 2026.

## {city} Fencing Rates 2026

| Service | {city} typical cost |
|---|---|
| Timber paling fence (per metre, installed) | {paling} |
| Timber framed — cedar / hardwood (per metre) | $200–$500/m |
| Lapped and capped timber (per metre) | {timber} |
| Aluminium slat fence (per metre) | $250–$550/m |
| Concrete block / masonry wall (per metre) | $400–$900/m |
| Pool fencing — glass (per metre) | {pool} |
| Pool fencing — aluminium (per metre) | $150–$350/m |
| Post replacement (per post) | $150–$350 |
| Gate installation (standard timber) | $500–$1,500 |
| Gate installation (automatic driveway) | $3,000–$8,000 |
| Fence removal and disposal (per metre) | $30–$80/m |

*All prices GST inclusive. Costs vary by ground conditions, access, and fence height.*

## {city} Fencing Market

{local}

## Fencing Materials for NZ Conditions

**Treated pine:** The most common and affordable NZ fencing timber. H4 treatment required for in-ground posts, H3.2 for above-ground framing. Typical lifespan: 15–25 years with maintenance.

**Cedar:** More durable and attractive than pine. Higher upfront cost but longer lifespan and better appearance. Popular for premium residential fencing.

**Aluminium slat:** Low maintenance, long-lasting, and available in powder-coat colours to match your home. Popular for modern and contemporary homes.

**Glass pool fencing:** Required by law around swimming pools. Frameless glass is premium; semi-frameless is more affordable. Must meet NZ Building Code clause F9.

**Concrete / masonry:** The most durable and secure option. Higher cost but minimal ongoing maintenance.

## Pool Fencing Rules in NZ

All swimming pools in NZ must be fenced to NZ Building Code clause F9 (Swimming pool safety). Key requirements:

- Fence height: minimum 1.2m
- No climbable features within 900mm of the fence
- Self-closing, self-latching gate opening away from the pool
- Pool fencing must be inspected and certified by a building inspector

**Fines for non-compliant pool fencing can be significant.** Your installer should know the requirements — confirm they are familiar with NZ Building Code F9.

**Find {city} fence installers:** [Fence Installers {city}](/trades/fencers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does fencing cost per metre in {city}?**
Timber paling: {paling}. Aluminium slat: $250–$550/m. Glass pool fencing: {pool}. Concrete wall: $400–$900/m.

**Do I need council consent for a fence in {city}?**
Fences under 2m generally don't need consent. Check the {region} Council rules — some areas have lower height limits or heritage restrictions. Pool fencing always requires a building consent and inspection.

**Who is responsible for boundary fencing in NZ?**
The Fencing Act 1978 generally requires adjoining property owners to share the cost of a sufficient fence on a common boundary. If you can't agree with your neighbour, mediation or the Disputes Tribunal can resolve it.

---

*Related: [Fence Installation Cost NZ](/articles/fence-installation-cost-nz/) | [Landscaping Cost NZ](/articles/landscaping-cost-nz/) | [Deck Building Cost NZ](/articles/deck-building-cost-nz/)*
"""


# ── Insulation Installer ──────────────────────────────────────────────────────

INSULATION_LOCAL = {
    "auckland":     "Auckland's mild climate means insulation is often under-prioritised, but ceiling and underfloor insulation significantly reduces energy bills and improves comfort. Many Auckland homes built before 2000 have little or no underfloor insulation.",
    "wellington":   "Wellington's cold, damp winters make insulation critical. Government subsidies (Warmer Kiwi Homes) can cover 80–90% of ceiling and underfloor insulation costs for eligible Wellington homeowners.",
    "christchurch": "Christchurch's cold winters — regularly below 0°C — make insulation one of the highest-ROI home improvements. Post-earthquake repairs included insulation upgrades in many homes.",
    "hamilton":     "Hamilton's humid winters and warm summers benefit from good insulation year-round. The Warmer Kiwi Homes programme is available for eligible Hamilton households.",
    "tauranga":     "Tauranga's mild climate reduces the urgency but good insulation still cuts energy bills and improves comfort in winter months. Underfloor insulation prevents cold, damp floors in wet months.",
    "dunedin":      "Dunedin has some of NZ's coldest winters and the highest proportion of cold, draughty older homes. Insulation is one of the most impactful improvements a Dunedin homeowner can make — Warmer Kiwi Homes subsidies are available.",
}

def insulation_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    local = INSULATION_LOCAL.get(city_key, f"{city} homeowners benefit from ceiling and underfloor insulation for year-round comfort and lower energy bills.")

    rates = {
        "auckland":     ("$1,800–$4,500", "$1,200–$3,000", "$800–$2,500"),
        "wellington":   ("$1,800–$4,500", "$1,200–$3,000", "$800–$2,500"),
        "christchurch": ("$1,600–$4,000", "$1,100–$2,800", "$750–$2,200"),
        "hamilton":     ("$1,600–$4,000", "$1,100–$2,800", "$700–$2,000"),
        "tauranga":     ("$1,600–$4,000", "$1,100–$2,800", "$700–$2,000"),
        "dunedin":      ("$1,500–$3,800", "$1,000–$2,600", "$650–$1,900"),
    }
    ceil, underfloor, wall = rates.get(city_key, ("$1,600–$4,000","$1,100–$2,800","$700–$2,000"))

    return f"""---
title: "Insulation Installers {city} 2026 — Insulation Costs, Types and Subsidies"
description: "Insulation installers {city} 2026 — {city} ceiling insulation cost, underfloor insulation prices, Warmer Kiwi Homes subsidies, and how to find a reliable insulation installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["insulation {city}", "insulation installer {city}", "ceiling insulation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Good insulation is one of the best investments a {city} homeowner can make — cutting heating bills, improving comfort, and meeting NZ's Healthy Homes Standards for rental properties. Here's what insulation costs in {city} in 2026.

## {city} Insulation Costs 2026

| Service | {city} typical cost (installed) |
|---|---|
| Ceiling insulation (standard 3-bed home) | {ceil} |
| Underfloor insulation (standard 3-bed home) | {underfloor} |
| Wall insulation (retrofit, per m²) | $80–$200/m² |
| Ceiling + underfloor (combined, 3-bed) | $2,500–$6,500 |
| Insulation top-up (existing ceiling) | $800–$2,000 |
| Vapour barrier (underfloor, per m²) | $15–$35/m² |
| Draught stopping (doors, windows) | $300–$900 |
| Insulation assessment / report | $150–$400 |

*All prices GST inclusive. Prices before any Warmer Kiwi Homes subsidy.*

## {city} Insulation Market

{local}

## Warmer Kiwi Homes Programme

The NZ Government's Warmer Kiwi Homes programme provides subsidies of **80–90%** of ceiling and underfloor insulation costs for eligible homeowners:

**Eligibility:** Own and live in your home, and receive a qualifying benefit (Community Services Card, NZ Super, Working for Families, etc.) OR live in a lower-income area.

**What's covered:** Ceiling insulation, underfloor insulation, and sometimes heating (heat pumps, wood burners).

**How to apply:** Contact an approved insulation provider in {city} — they will assess eligibility and manage the application. You don't need to apply to EECA directly.

If you qualify, ceiling + underfloor insulation could cost you as little as **$200–$600** out of pocket.

## NZ Insulation Standards

**Healthy Homes Standards:** Rental properties must meet minimum insulation levels (R-value requirements) under the Residential Tenancies Act. Landlords in {city} must comply or face fines.

**NZ Building Code:** New builds must meet Schedule 1 energy efficiency requirements. Insulation must achieve minimum R-values per climate zone.

**{region} climate zone:** {city} is in NZ climate zone {'1' if city_key in ['auckland','tauranga','napier','new-plymouth','nelson'] else '2' if city_key in ['hamilton','rotorua','palmerston-north'] else '3'} — your installer will specify the correct R-value for your zone.

## Insulation Types

**Pink Batts / glasswool:** The standard NZ product. Available in ceiling and underfloor grades. Affordable and effective.

**Polyester:** Itch-free alternative to glasswool. Slightly higher cost but easier to handle. Good choice where roof access is limited.

**Blown-in / loose fill:** Used for retrofit ceiling insulation where batt installation is difficult. Blown into the ceiling cavity.

**PIR / rigid foam:** Used for specific applications — under slabs, in walls. Higher R-value per mm but more expensive.

**Find {city} insulation installers:** [Insulation Installers {city}](/trades/insulation/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does ceiling insulation cost in {city}?**
Full installation in a standard 3-bed home: {ceil}. With Warmer Kiwi Homes subsidy (if eligible): potentially $200–$600 out of pocket.

**Am I eligible for the Warmer Kiwi Homes subsidy in {city}?**
If you own and live in your home and receive a qualifying benefit, you likely qualify. Contact a local approved insulation installer — they'll check your eligibility for free.

**What R-value do I need for {city}?**
Ceiling: minimum R3.3 (zone 1) to R6.6 (zone 3). Underfloor: minimum R1.3 (zone 1) to R2.0 (zone 3). Your installer will advise the correct specification.

---

*Related: [Heat Pump Installation Cost NZ](/articles/heat-pump-installation-cost-nz/) | [Double Glazing Cost NZ](/articles/double-glazing-cost-nz/) | [Insulation Installation Cost NZ](/articles/insulation-installation-cost-nz/)*
"""


# ── Solar Installer ───────────────────────────────────────────────────────────

SOLAR_LOCAL = {
    "auckland":     "Auckland gets 1,700–1,900 kWh/m²/year of solar irradiance — good but not the best in NZ. High electricity prices (often 33–38c/kWh) make the economics strong. EV integration (charge your car from your roof) is a fast-growing category.",
    "wellington":   "Wellington gets 1,800–2,000 kWh/m²/year and benefits from relatively high electricity prices. North-facing roofs on Wellington's hills can be excellent solar sites — though shading from neighbouring properties and trees must be assessed.",
    "christchurch": "Christchurch gets 1,900–2,100 kWh/m²/year — good solar resource for the South Island. The flat Canterbury terrain means minimal shading for many properties. Frost and snow are rare factors for panel efficiency.",
    "hamilton":     "Hamilton gets 1,700–1,900 kWh/m²/year. The Waikato's warm summers provide good peak generation. Payback periods of 6–10 years are typical for well-sized Hamilton systems.",
    "tauranga":     "Tauranga is one of NZ's sunniest cities — 2,300+ hours of sunshine per year and over 2,000 kWh/m²/year irradiance. Solar economics in Tauranga are among the best in NZ, with shorter payback periods than most cities.",
    "dunedin":      "Dunedin gets 1,600–1,800 kWh/m²/year — lower than the north but still viable, especially with high local electricity prices. Winter generation is lower, so battery storage is more valuable here for self-sufficiency.",
}

def solar_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    local = SOLAR_LOCAL.get(city_key, f"{city} has a growing solar market with good returns for well-sited rooftop systems.")

    rates = {
        "auckland":     ("$8,000–$14,000", "$14,000–$22,000", "$8,000–$14,000"),
        "wellington":   ("$8,000–$14,000", "$14,000–$22,000", "$8,000–$14,000"),
        "christchurch": ("$7,500–$13,000", "$13,000–$21,000", "$7,500–$13,000"),
        "hamilton":     ("$7,500–$13,000", "$13,000–$21,000", "$7,500–$13,000"),
        "tauranga":     ("$7,500–$13,000", "$13,000–$21,000", "$7,500–$13,000"),
        "dunedin":      ("$7,000–$12,500", "$12,500–$20,000", "$7,000–$12,500"),
    }
    small, large, battery = rates.get(city_key, ("$7,500–$13,000","$13,000–$21,000","$7,500–$13,000"))

    return f"""---
title: "Solar Installers {city} 2026 — Solar Panel Costs, Payback and What to Expect"
description: "Solar installers {city} 2026 — {city} solar panel installation costs, system sizes, payback periods, battery storage prices, and how to find a reliable solar installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["solar installers {city}", "solar panels {city}", "solar installation cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Rooftop solar is one of the fastest-growing home improvements in {city}. High electricity prices and NZ's good solar resource make the economics increasingly attractive. Here's what solar installation costs in {city} in 2026.

## {city} Solar Installation Costs 2026

| System | {city} typical cost (supply + install) |
|---|---|
| Small system (3–4kW, 8–10 panels) | {small} |
| Medium system (6–8kW, 16–20 panels) | {large} |
| Large system (10–12kW, 26–30 panels) | $18,000–$28,000 |
| Battery storage add-on (10kWh) | {battery} |
| Battery storage add-on (15kWh) | $12,000–$20,000 |
| EV charger integration | $1,500–$3,500 |
| System monitoring setup | Included / $200–$500 |
| Annual maintenance / inspection | $200–$500 |

*All prices GST inclusive. System costs vary by panel brand, inverter type, roof access, and grid connection complexity.*

## {city} Solar Market

{local}

## Is Solar Worth It in {city}?

**Payback calculation:** A typical {city} home with a 6kW system might generate 8,000–9,500 kWh/year. At 35c/kWh avoided (buying from grid), that's $2,800–$3,300/year in savings. A $13,000–$18,000 system payback: **5–9 years**.

**Key variables:**
- How much power you use during the day (self-consumption rate)
- Your electricity tariff and buy-back rate
- Your roof orientation (north-facing is optimal in NZ)
- Shading from trees or neighbouring buildings

**Buy-back rates:** Most NZ retailers offer 8–18c/kWh for solar exported to the grid — much less than the retail rate. Maximising self-consumption (using power when it's being generated) improves returns.

## Solar + Battery in {city}

Battery storage lets you use your solar generation at night, increasing self-consumption to 80–90%+. The economics depend on:
- Your overnight power use (EV charging is the biggest benefit)
- Your electricity buy-back rate (lower rates make batteries more attractive)
- Battery cost payback (typically 8–12 years for battery only)

## Grid Connection in {city}

All solar systems connected to the grid must be approved by your local lines company before connection. Your installer manages this process. Lines companies in {region}: {
    'Vector (most of Auckland)' if city_key == 'auckland' else
    'Wellington Electricity' if city_key == 'wellington' else
    'Orion' if city_key == 'christchurch' else
    'WEL Networks' if city_key == 'hamilton' else
    'PowerCo' if city_key in ['tauranga','new-plymouth','palmerston-north'] else
    'Aurora Energy' if city_key == 'dunedin' else
    'Unison' if city_key in ['napier','rotorua'] else
    'Nelson Electricity' if city_key == 'nelson' else
    'your local lines company'
}.

**Find {city} solar installers:** [Solar Installers {city}](/trades/solar/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does solar panel installation cost in {city}?**
Small system (3–4kW): {small}. Medium (6–8kW): {large}. Battery add-on (10kWh): {battery}.

**How long is the payback for solar in {city}?**
Typically 5–9 years for a well-sized system, depending on your electricity use and self-consumption rate. {local[:100]}...

**Do I need council consent for solar panels in {city}?**
Rooftop solar panels are generally permitted without building consent in NZ, provided they don't significantly alter the roofline. Grid connection requires lines company approval — your installer handles this.

**What direction should solar panels face in {city}?**
North-facing at around 20–30° tilt is optimal in NZ. East/west-facing panels generate less but can still be viable. South-facing is not recommended.

---

*Related: [Solar Panel Cost NZ](/articles/solar-panel-cost-nz/) | [Heat Pump Installation Cost NZ](/articles/heat-pump-installation-cost-nz/) | [Electricians {city}](/articles/electrician-{city_key}-nz/)*
"""


# ── Gap fill: Tiler ───────────────────────────────────────────────────────────

def tiler_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    rates_note = f"Rates are {c['rate_adj']}."

    rate_map = {
        "napier":           ("$75–$130/hr", "$75–$185/m²", "$2,800–$7,500"),
        "new-plymouth":     ("$75–$130/hr", "$75–$185/m²", "$2,800–$7,500"),
        "palmerston-north": ("$70–$125/hr", "$70–$180/m²", "$2,700–$7,000"),
        "nelson":           ("$75–$130/hr", "$75–$185/m²", "$2,800–$7,500"),
        "rotorua":          ("$70–$125/hr", "$70–$180/m²", "$2,700–$7,000"),
    }
    hourly, m2, bathroom = rate_map.get(city_key, ("$70–$125/hr","$70–$180/m²","$2,700–$7,000"))

    return f"""---
title: "Tilers {city} 2026 — Tiling Rates, Bathroom Costs and What to Expect"
description: "Tilers {city} 2026 — {city} tiler hourly rates, bathroom tiling cost, floor and wall tiling prices, and how to find a reliable tiler near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["tilers {city}", "tiler {city}", "tiling cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{city} has steady demand for tiling work across bathrooms, kitchens, and outdoor areas. Here's what tilers charge in {city} in 2026.

## {city} Tiling Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Floor tiling (per m², supply & lay) | {m2} |
| Wall tiling (per m², supply & lay) | $80–$200/m² |
| Bathroom tiling (full, small bathroom) | {bathroom} |
| Kitchen splashback (2m linear) | $600–$2,200 |
| Shower tiling (walls + floor) | $2,200–$5,500 |
| Outdoor paving/tiles (per m²) | $75–$170/m² |
| Tile removal (per m²) | $25–$55/m² |
| Grout repair / regrouting | $280–$1,100 |
| Waterproofing (per m²) | $28–$55/m² |

*All prices GST inclusive. {rates_note}*

## Waterproofing — Critical for {city} Bathrooms

All wet areas must be waterproofed to NZ Building Code (E3) before tiling. Poor waterproofing causes costly hidden damage behind tiles. Confirm your tiler waterproofs to AS/NZS 4858 — ask to see the product they use and request a waterproofing certificate.

## What to Ask a {city} Tiler

1. Is waterproofing included in your quote?
2. What tile brands do you recommend?
3. What is your warranty on labour?
4. Can I see photos of recent work?
5. Are you GST registered?

**Find {city} tilers:** [Tilers {city}](/trades/tilers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does bathroom tiling cost in {city}?**
Small full bathroom (floor + walls, 6–10m²): {bathroom} supply and lay.

**Should I supply my own tiles?**
You can, but confirm with your tiler first. Always order 10–15% extra for cuts and repairs. Your tiler may offer better trade prices on tiles.

---

*Related: [Tiling Cost NZ](/articles/tiling-cost-nz/) | [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/) | [Shower Installation Cost NZ](/articles/shower-installation-cost-nz/)*
"""


# ── Gap fill: Carpenter ───────────────────────────────────────────────────────

def carpenter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]

    rate_map = {
        "tauranga": ("$85–$160/hr", "Tauranga's strong renovation and outdoor living market keeps carpenters busy. Deck builds, pergolas, and outdoor entertaining areas are in high demand given the Bay of Plenty lifestyle."),
        "dunedin":  ("$75–$145/hr", "Dunedin carpenters frequently work on character home renovations — older timber framing, sash windows, and heritage joinery require specialist skills. The student rental market drives ongoing fit-out and maintenance work."),
        "napier":   ("$78–$148/hr", "Napier's art deco character homes and steady renovation market provide consistent carpentry demand. Deck builds and outdoor living improvements are popular in Hawke's Bay's warm climate."),
    }
    hourly, local = rate_map.get(city_key, ("$78–$148/hr", f"{city} has steady residential carpentry demand across renovations, decks, and fit-out work."))

    return f"""---
title: "Carpenters {city} 2026 — Carpenter Rates, Deck Costs and What to Expect"
description: "Carpenters {city} 2026 — {city} carpenter hourly rates, deck build costs, renovation prices, LBP licensing, and how to find a reliable carpenter near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["carpenters {city}", "carpenter {city}", "carpentry cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what carpenters charge in {city} in 2026.

## {city} Carpenter Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Deck build (basic, 20m²) | $7,500–$19,000 |
| Deck build (hardwood/composite, 20m²) | $16,000–$36,000 |
| Pergola | $5,500–$19,000 |
| Fence (timber, per metre) | $130–$380/m |
| Door installation (internal) | $280–$580 per door |
| Door installation (external) | $580–$1,400 per door |
| Window replacement (per window) | $750–$2,400 |
| Kitchen fit-out (carcass install) | $2,800–$9,500 |
| Cladding replacement (per m²) | $140–$330/m² |

*All prices GST inclusive.*

## LBP Licensing

Structural framing and weathertightness work must be done by a Licensed Building Practitioner (LBP). Verify at [lbp.govt.nz](https://www.lbp.govt.nz).

**Find {city} carpenters:** [Carpenters {city}](/trades/carpenters/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a carpenter cost in {city}?**
Hourly: {hourly}. Deck build (20m², basic): $7,500–$19,000. Hardwood deck: $16,000–$36,000.

**Do I need an LBP for a deck in {city}?**
If the deck needs building consent (usually over 1.5m above ground), yes. Ground-level decks below the consent threshold don't legally require an LBP but it's still recommended.

---

*Related: [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Builder Pricing NZ](/articles/builder-pricing-guide-nz-2026/) | [Pergola Cost NZ](/articles/pergola-cost-nz/)*
"""


# ── Article list ───────────────────────────────────────────────────────────────

ARTICLES = [
    # Arborists — major cities
    ("arborist-auckland-nz",         lambda: arborist_article("auckland")),
    ("arborist-wellington-nz",       lambda: arborist_article("wellington")),
    ("arborist-christchurch-nz",     lambda: arborist_article("christchurch")),
    ("arborist-hamilton-nz",         lambda: arborist_article("hamilton")),
    ("arborist-tauranga-nz",         lambda: arborist_article("tauranga")),
    ("arborist-napier-nz",           lambda: arborist_article("napier")),
    ("arborist-new-plymouth-nz",     lambda: arborist_article("new-plymouth")),
    ("arborist-palmerston-north-nz", lambda: arborist_article("palmerston-north")),
    ("arborist-nelson-nz",           lambda: arborist_article("nelson")),
    ("arborist-rotorua-nz",          lambda: arborist_article("rotorua")),
    # Fence installers — major cities
    ("fence-installer-auckland-nz",      lambda: fence_article("auckland")),
    ("fence-installer-wellington-nz",    lambda: fence_article("wellington")),
    ("fence-installer-christchurch-nz",  lambda: fence_article("christchurch")),
    ("fence-installer-hamilton-nz",      lambda: fence_article("hamilton")),
    ("fence-installer-tauranga-nz",      lambda: fence_article("tauranga")),
    ("fence-installer-dunedin-nz",       lambda: fence_article("dunedin")),
    # Insulation — major cities
    ("insulation-installer-auckland-nz",      lambda: insulation_article("auckland")),
    ("insulation-installer-wellington-nz",    lambda: insulation_article("wellington")),
    ("insulation-installer-christchurch-nz",  lambda: insulation_article("christchurch")),
    ("insulation-installer-hamilton-nz",      lambda: insulation_article("hamilton")),
    ("insulation-installer-tauranga-nz",      lambda: insulation_article("tauranga")),
    ("insulation-installer-dunedin-nz",       lambda: insulation_article("dunedin")),
    # Solar installers — major cities
    ("solar-installer-auckland-nz",      lambda: solar_article("auckland")),
    ("solar-installer-wellington-nz",    lambda: solar_article("wellington")),
    ("solar-installer-christchurch-nz",  lambda: solar_article("christchurch")),
    ("solar-installer-hamilton-nz",      lambda: solar_article("hamilton")),
    ("solar-installer-tauranga-nz",      lambda: solar_article("tauranga")),
    ("solar-installer-dunedin-nz",       lambda: solar_article("dunedin")),
    # Gap fills — tilers
    ("tiler-napier-nz",              lambda: tiler_article("napier")),
    ("tiler-new-plymouth-nz",        lambda: tiler_article("new-plymouth")),
    ("tiler-palmerston-north-nz",    lambda: tiler_article("palmerston-north")),
    ("tiler-nelson-nz",              lambda: tiler_article("nelson")),
    ("tiler-rotorua-nz",             lambda: tiler_article("rotorua")),
    # Gap fills — carpenters
    ("carpenter-tauranga-nz",        lambda: carpenter_article("tauranga")),
    ("carpenter-dunedin-nz",         lambda: carpenter_article("dunedin")),
    ("carpenter-napier-nz",          lambda: carpenter_article("napier")),
]


if __name__ == "__main__":
    created = 0
    skipped = 0
    for slug, fn in ARTICLES:
        path = OUT / f"{slug}.md"
        if path.exists():
            print(f"  skip  {slug}")
            skipped += 1
        else:
            path.write_text(fn(), encoding="utf-8")
            print(f"  write {slug}")
            created += 1

    print(f"\nDone: {created} created, {skipped} skipped. Total articles now: {len(list(OUT.glob('*.md')))}")
