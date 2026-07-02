#!/usr/bin/env python3
"""
Wave 7 SEO content generator — TradieTools NZ
New trades: bathroom renovator, deck builder, rubbish removal
Gap fills: insulation, fence installer, heat pump installer for smaller cities
Run: python3 generate_wave7.py
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

# ── Bathroom Renovator ────────────────────────────────────────────────────────

BATHROOM_DATA = {
    "auckland":     ("$18,000–$40,000", "$8,000–$18,000", "$40,000–$100,000+", "Auckland has NZ's most active bathroom renovation market. High property values make quality bathrooms a strong investment. Auckland's heritage villas and units have typically small bathrooms that homeowners love to enlarge and modernise."),
    "wellington":   ("$18,000–$40,000", "$8,000–$18,000", "$40,000–$100,000+", "Wellington's character villas often have original small bathrooms that are first on the renovation list. Space is at a premium in many Wellington homes, making smart layout design crucial."),
    "christchurch": ("$15,000–$35,000", "$7,000–$15,000", "$35,000–$90,000+",  "Post-earthquake Christchurch saw many bathroom renovations as part of insurance-funded repairs. The rebuild lifted baseline standards across the city. Christchurch's growing housing market continues to drive strong renovation demand."),
    "hamilton":     ("$14,000–$32,000", "$6,500–$14,000", "$32,000–$80,000+",  "Hamilton's 1960s–80s housing stock has dated bathrooms that are popular renovation targets. The city's affordable land makes renovating to add value a popular strategy."),
    "tauranga":     ("$15,000–$35,000", "$7,000–$15,000", "$35,000–$90,000+",  "Tauranga's lifestyle focus means bathrooms are a high priority — outdoor-indoor living and quality finishes are valued highly in Bay of Plenty homes. Ensuite additions are popular in Tauranga's growing new-build market."),
    "dunedin":      ("$13,000–$30,000", "$6,000–$13,000", "$30,000–$75,000+",  "Dunedin's Victorian and Edwardian homes typically have original bathrooms with outdated plumbing and fitments. Bathroom renovations in older Dunedin homes often uncover moisture damage in walls and floors, adding to project costs."),
}

def bathroom_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    mid, budget, premium, local = BATHROOM_DATA[city_key]

    return f"""---
title: "Bathroom Renovation {city} 2026 — Costs, What's Included and How to Plan"
description: "Bathroom renovation {city} 2026 — {city} bathroom renovation costs, budget vs mid-range vs premium, tradespeople needed, consents, and how to find reliable bathroom renovators near you."
image: "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["bathroom renovation {city}", "bathroom renovator {city}", "bathroom cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

A bathroom renovation is one of the most popular home improvements in {city}. Here's what it costs in 2026 and what to expect from the process.

## {city} Bathroom Renovation Costs 2026

| Bathroom type | {city} typical cost (complete) |
|---|---|
| Budget refresh (existing layout, cosmetic) | $5,000–$9,000 |
| Budget renovation (new suite, same layout) | {budget} |
| Mid-range renovation (re-layout, quality fittings) | {mid} |
| Premium renovation (full custom, top fittings) | {premium} |

### What's Included at Each Level

| Cost component | Budget | Mid-range | Premium |
|---|---|---|---|
| Toilet | Entry-level | Mid-range | Wall-hung/designer |
| Vanity | Flat-pack | Semi-custom | Custom cabinetry |
| Basin | Standard | Semi-inset | Vessel/designer |
| Shower | Budget screen | Frameless glass | Frameless + niche |
| Bath | Acrylic freestanding | Standard | Premium freestanding |
| Tapware | Budget | Mid-range | Designer |
| Tiles | Budget tiles | 300×600 format | Large format/natural stone |
| Heated towel rail | Basic | Standard | Designer |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Bathroom Renovation Market

{local}

## Tradespeople You'll Need

A bathroom renovation involves multiple trades:

- **Builder:** Project management, demolition, waterproofing, framing changes, and coordination
- **Plumber:** Toilet, basin, shower/bath connections, relocation if layout changes
- **Electrician:** Heated towel rail, ventilation fan, lighting, shaver socket
- **Tiler:** Floor and wall tiles — the biggest visual impact
- **Plasterer:** Making good walls and ceiling after demolition

A good builder or bathroom company coordinates all trades. Self-managing trades saves the margin (typically 15–25%) but requires significantly more time.

## Waterproofing — The Most Important Step

NZ Building Code requires waterproofing in wet areas. This is non-negotiable:

- All shower areas must be fully waterproofed to the **correct height** (minimum 1,800mm for showers)
- Floor-to-wall junctions are the most common failure point
- Must use a **consented** waterproofing system with a compliance certificate
- Your builder must be Licensed Building Practitioner (LBP) for restricted work

**Warning:** Non-compliant waterproofing means invisible rot behind tiles — often not discovered until major damage occurs. Never skip or cheap out on waterproofing.

## Do I Need Building Consent?

**Usually no** for a like-for-like renovation in the same location. **Yes** if you are:
- Moving plumbing to a new location (structural/drainage work)
- Removing walls or changing the room's footprint
- Adding a new bathroom where one didn't exist

Your builder will advise — most standard bathroom renovations don't require consent.

**Find {city} bathroom renovators:** [Bathroom Renovators {city}](/trades/bathroom-renovators/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a bathroom renovation cost in {city}?**
Budget (new suite, same layout): {budget}. Mid-range (re-layout, quality fittings): {mid}. Premium: {premium}.

**How long does a bathroom renovation take in {city}?**
Typical mid-range bathroom: 2–4 weeks. Complex renovations with layout changes: 4–8 weeks.

**What is the most important part of a bathroom renovation?**
Waterproofing. Everything else is cosmetic — bad waterproofing causes structural rot that can cost far more to fix than the original renovation.

**Can I use my bathroom during renovation?**
No — you'll need to plan for no bathroom access for the duration. Most homeowners use another bathroom or stay elsewhere for major renovations.

---

*Related: [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/) | [Kitchen Renovation {city}](/articles/kitchen-renovator-{city_key}-nz/) | [Tiler {city}](/articles/tiler-{city_key}-nz/)*
"""


# ── Deck Builder ──────────────────────────────────────────────────────────────

DECK_DATA = {
    "auckland":     ("$1,800–$3,500/m²", "$18,000–$45,000", "Auckland's long outdoor season makes decks one of the best lifestyle investments. The subtropical climate means timber decks require treatment or hardwood species — pine decks need regular oiling/staining in Auckland's humidity. Composite decking is gaining popularity for its lower maintenance."),
    "wellington":   ("$1,900–$3,600/m²", "$19,000–$46,000", "Wellington's challenging terrain — many properties on steep sections — drives strong demand for elevated decks. Wellington's wind is the key design consideration: solid balustrades and sheltered orientations are important. Composite decking withstands the coastal wind and rain well."),
    "christchurch": ("$1,600–$3,200/m²", "$16,000–$40,000", "Christchurch's flat sections and warm dry summers make decks an ideal outdoor entertaining space. Post-earthquake rebuilds incorporated decks into many new designs. Timber decks suit Christchurch's lower rainfall compared to wetter NZ cities."),
    "hamilton":     ("$1,500–$3,000/m²", "$15,000–$37,000", "Hamilton's warm summers and large suburban sections make decks popular additions. The Waikato's mild climate means standard treated pine decks last well with regular maintenance. Ground-level and low-level decks are most common on Hamilton's flat sections."),
    "tauranga":     ("$1,600–$3,200/m²", "$16,000–$40,000", "Tauranga's beach and lake lifestyle means decks are near-essential. The Bay of Plenty's warm climate is ideal for outdoor living — decks are often designed to connect with pools, outdoor kitchens, and garden spaces."),
    "dunedin":      ("$1,500–$3,000/m²", "$15,000–$37,000", "Dunedin decks must be designed for the city's cold winters and frequent rain. Elevated decks on Dunedin's many hilly sections are popular, though wind and driving rain are key design considerations. Durable treated timber or composite materials perform best."),
}

def deck_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    m2, standard, local = DECK_DATA[city_key]

    return f"""---
title: "Deck Builders {city} 2026 — Deck Costs, Materials and What to Expect"
description: "Deck builders {city} 2026 — {city} deck building costs, timber vs composite pricing, deck consent requirements, and how to find a reliable deck builder near you."
image: "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["deck builders {city}", "deck builder {city}", "deck cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what deck builders charge in {city} in 2026.

## {city} Deck Building Costs 2026

| Service | {city} typical cost |
|---|---|
| Deck construction (per m², supply + install) | {m2} |
| Standard deck 10m² (ground level) | $18,000–$35,000 |
| Standard deck 20m² (elevated, balustrade) | {standard} |
| Treated pine deck (entry-level material) | $1,500–$2,500/m² |
| Kwila / hardwood deck (premium timber) | $2,200–$4,000/m² |
| Composite decking (Trex, ModWood etc.) | $2,500–$4,500/m² |
| Balustrade (glass, per m linear) | $600–$1,400/m |
| Balustrade (timber/aluminium, per m linear) | $280–$650/m |
| Deck stairs (per flight) | $1,800–$4,500 |
| Deck removal + disposal | $900–$2,500 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Timber vs Composite Decking

**Treated pine:** Most affordable. Requires sealing/oiling every 1–2 years. Lifespan 15–25 years with maintenance.

**Hardwood (kwila, vitex, garapa):** Premium look, naturally durable. Requires oiling annually. Lifespan 25–40+ years.

**Composite (Trex, ModWood, Titan):** High upfront cost, near-zero maintenance. Doesn't need oiling. Lifespan 25–30 years. Best for busy households.

## Do I Need Building Consent for a Deck in {city}?

**Consent required if your deck:**
- Is more than 1 metre above ground at any point
- Is larger than 20m²
- Attaches to the house (requires structural connection sign-off)

Many ground-level decks under 20m² and under 1m high are **exempt** from consent — but always check with {region} Council before starting. Your deck builder will advise.

An LBP (Licensed Building Practitioner) must carry out or supervise restricted building work.

## Getting the Best Result

- Get 2–3 written quotes — scope what's included (posts, bearers, joists, decking, balustrade, stairs)
- Confirm the timber treatment level (H3.2 minimum for above ground in NZ)
- Ask for a council consent application if needed — don't assume it's exempt
- Consider composite if maintenance is a concern (young kids, rental property)

**Find {city} deck builders:** [Deck Builders {city}](/trades/deck-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a deck cost in {city}?**
Standard 20m² elevated deck with balustrade: {standard}. Budget $1,500–$2,500/m² for treated pine.

**Do I need consent for a deck in {city}?**
Decks over 1m high, over 20m², or attached to the house typically require building consent from {region} Council.

*Related: [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/) | [Builder {city}](/articles/builder-{city_key}-nz/)*
"""


# ── Rubbish Removal ───────────────────────────────────────────────────────────

RUBBISH_DATA = {
    "auckland":     ("$180–$480", "$380–$880", "$950–$3,500", "Auckland has high rubbish removal demand driven by its dense population, busy renovation market, and limited kerbside inorganic collection in many areas. Auckland rubbish removal companies are plentiful — shop around for the best rate."),
    "wellington":   ("$180–$480", "$380–$880", "$950–$3,500", "Wellington's hilly terrain can make rubbish removal more complex — access for skip bins is challenging in many streets. Man-and-van rubbish removal services are particularly popular in central Wellington."),
    "christchurch": ("$160–$440", "$340–$800", "$850–$3,200", "Post-earthquake Christchurch generated enormous rubbish removal demand. The ongoing rebuild and renovation market keeps demand steady. Multiple competing operators means competitive pricing in Christchurch."),
    "hamilton":     ("$150–$420", "$320–$750", "$800–$3,000", "Hamilton's suburban renovation market generates steady rubbish removal work. Large suburban sections mean skip bin placement is usually easy. Hamilton has good competition between rubbish removal operators."),
    "tauranga":     ("$160–$440", "$340–$800", "$850–$3,200", "Tauranga's active property market and large retirement demographic create demand for both renovation rubbish removal and household decluttering services."),
    "dunedin":      ("$140–$400", "$300–$720", "$750–$2,800", "Dunedin's older housing stock generates rubbish removal demand from renovation and deceased estate clearances. The student flatting market also creates regular end-of-tenancy cleanouts."),
}

def rubbish_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    small, medium, large, local = RUBBISH_DATA[city_key]

    return f"""---
title: "Rubbish Removal {city} 2026 — Costs, Skip Bins and What to Expect"
description: "Rubbish removal {city} 2026 — {city} rubbish removal costs, skip bin hire prices, man-and-van rates, what can and can't be removed, and how to find a reliable rubbish removal company near you."
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
| Large load (truck, 6–10m³) | $700–$2,200 |
| Full house/commercial clearance | {large} |
| Skip bin hire — 3m³ (3 days) | $250–$480 |
| Skip bin hire — 6m³ (3 days) | $380–$680 |
| Skip bin hire — 9m³ (3 days) | $480–$880 |
| Concrete / heavy materials (per m³) | $120–$280/m³ |
| Green waste (per m³) | $80–$180/m³ |
| E-waste disposal (per item) | $15–$80 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}. Prices vary by waste type and disposal facility fees.*

## Skip Bin vs Man-and-Van — Which Is Better?

**Skip bin:** Leave it for 3–7 days, fill at your own pace. Better for ongoing renovations or when you want to sort as you go. Needs road access and council permit if placed on the street.

**Man-and-van (same-day):** Turn up, load, gone in an hour. Better for large single items, awkward access, or when you need it done now. Can handle furniture, appliances, and mixed loads.

## What Rubbish Removal Companies Won't Take

Most rubbish removal companies have restrictions on:

- **Hazardous materials:** Asbestos, chemicals, paint, gas bottles (need specialist disposal)
- **Tyres:** Extra charge, must go to tyre recycler
- **Liquids and sludge:** Not accepted
- **Biological waste:** Not accepted

Always ask when booking if your load includes any restricted materials.

## {city} Rubbish Removal Market

{local}

**Find {city} rubbish removal:** [Rubbish Removal {city}](/trades/rubbish-removal/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does rubbish removal cost in {city}?**
Small load (1–2m³): {small}. Medium load (3–5m³): {medium}. Full house clearance: {large}.

**Do I need a permit for a skip bin in {city}?**
Skip bins on private property generally don't need a permit. Bins on public roads or footpaths require a permit from {region} Council — your skip hire company usually arranges this.

*Related: [Skip Bin Cost NZ](/articles/skip-bin-cost-nz/) | [Renovation Cost NZ](/articles/builder-pricing-guide-nz-2026/)*
"""


# ── Insulation Installer gap fills (smaller cities) ────────────────────────────

INSULATION_DATA = {
    "napier":           ("$2,200–$5,500", "$1,500–$3,800", "Napier's warm Hawke's Bay climate means ceiling insulation is important for summer coolness as much as winter warmth. The 1931 earthquake means many rebuilt homes have older insulation that needs replacement."),
    "new-plymouth":     ("$2,200–$5,500", "$1,500–$3,800", "New Plymouth's mild but damp climate makes insulation important for preventing moisture buildup. Taranaki homes benefit from both ceiling and underfloor insulation for year-round comfort."),
    "palmerston-north": ("$2,100–$5,300", "$1,400–$3,600", "Palmerston North has cold winters and the Manawatu wind makes insulation particularly valuable. The city's high proportion of older rental housing has driven significant insulation upgrade activity through Warmer Kiwi Homes grants."),
    "nelson":           ("$2,200–$5,500", "$1,500–$3,800", "Nelson's sunny but cold winter climate makes insulation a high-ROI investment. The Nelson-Tasman region has active Warmer Kiwi Homes grant activity — many homeowners qualify for subsidised insulation."),
    "rotorua":          ("$2,100–$5,300", "$1,400–$3,600", "Rotorua's cold winters and geothermal humidity make insulation important. Some geothermal areas have considerations around underfloor insulation materials — experienced local installers know what works."),
}

def insulation_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    ceiling, underfloor, local = INSULATION_DATA[city_key]

    return f"""---
title: "Insulation Installers {city} 2026 — Insulation Costs, Grants and What to Expect"
description: "Insulation installers {city} 2026 — {city} insulation costs, ceiling vs underfloor prices, Warmer Kiwi Homes grants, and how to find a reliable insulation installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["insulation installers {city}", "insulation cost {city}", "ceiling insulation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what insulation installers charge in {city} in 2026.

## {city} Insulation Costs 2026

| Service | {city} typical cost |
|---|---|
| Ceiling insulation (full house, 3-bed) | {ceiling} |
| Underfloor insulation (full house, 3-bed) | {underfloor} |
| Ceiling insulation (per m²) | $18–$48/m² |
| Underfloor insulation (per m², batts) | $12–$32/m² |
| Underfloor insulation (per m², foil) | $8–$22/m² |
| Wall insulation (retrofit, per m²) | $45–$110/m² |
| Insulation removal + replacement (per m²) | $28–$65/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Warmer Kiwi Homes Grants — {city}

**You may qualify for a government subsidy** on ceiling and underfloor insulation if:
- You own and live in your home (not a rental)
- Your home was built before 2008
- You receive an eligible benefit OR your home is in a lower-income area

**Grant covers:** Up to 80% of ceiling and underfloor insulation costs (or 90% for Community Services Card holders).

**Apply via:** EECA (Energy Efficiency and Conservation Authority) at [energywise.govt.nz](https://www.energywise.govt.nz/at-home/warmer-kiwi-homes/)

Approved installers in {city} can check your eligibility and manage the grant application for you.

## Insulation Types

**Glass wool batts (ceiling):** Most common, cost-effective. R-value R3.2–R6.0.
**Polyester batts:** Good allergen option. Similar cost to glass wool.
**Blown-in loose fill (ceiling):** Good for hard-to-reach areas, fills gaps well.
**Foil (underfloor):** Reflects radiant heat, moisture-resistant. NZ Building Code no longer accepts foil for new builds but it performs well for retrofits.
**Polyester batts (underfloor):** Better cold performance than foil. More expensive.

**Find {city} insulation installers:** [Insulation Installers {city}](/trades/insulation-installers/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does ceiling insulation cost in {city}?**
Full 3-bed house: {ceiling}. May be heavily subsidised through Warmer Kiwi Homes grants.

*Related: [Insulation Cost NZ](/articles/insulation-cost-nz/) | [Heat Pump Installers {city}](/articles/heat-pump-installer-{city_key}-nz/) | [Double Glazing Cost NZ](/articles/double-glazing-cost-nz/)*
"""


# ── Fence Installer gap fills (smaller cities) ────────────────────────────────

FENCE_DATA = {
    "napier":           ("$180–$380/m", "$95–$220/m", "Napier's warm Hawke's Bay lifestyle means outdoor entertaining is popular — good fencing for privacy and section definition is valued. Timber fences suit the region's dry climate, though salt air near the coast accelerates corrosion on metal fixings."),
    "new-plymouth":     ("$185–$390/m", "$98–$225/m", "New Plymouth's coastal westerly winds make fence design important — exposed fences need solid posts and durable materials. The city's lifestyle property market values well-fenced sections for both privacy and stock containment."),
    "palmerston-north": ("$175–$375/m", "$90–$215/m", "Palmerston North's strong Manawatu wind is the key fencing challenge — fence designs must allow for wind load, especially for tall privacy fences. Concrete posts are popular for their durability in the windy Manawatu conditions."),
    "nelson":           ("$180–$380/m", "$95–$220/m", "Nelson's sunny lifestyle and strong outdoor culture means good fencing is valued for privacy and garden definition. Timber fences perform well in Nelson's relatively dry climate — the Tasman region has less rain than many NZ cities."),
    "rotorua":          ("$175–$375/m", "$90–$215/m", "Rotorua's volcanic soils can affect fence post longevity — experienced local fencers know to use the right post treatment or concrete for Rotorua's acidic soils. The geothermal environment accelerates steel corrosion in some areas."),
}

def fence_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    timber, post_rail, local = FENCE_DATA[city_key]

    return f"""---
title: "Fence Installers {city} 2026 — Fencing Costs, Materials and What to Expect"
description: "Fence installers {city} 2026 — {city} fencing costs, timber vs Colorbond prices, fence consent requirements, and how to find a reliable fence installer near you."
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
| Colorbond / metal fence (per m linear) | $220–$420/m |
| Picket fence (1.0m, per m linear) | $140–$280/m |
| Concrete block wall (per m linear) | $380–$850/m |
| Pool fence (compliant, per m linear) | $380–$950/m |
| Fence removal + disposal (per m linear) | $25–$65/m |
| Gate — timber (supply + fit) | $480–$1,200 |
| Gate — automated sliding (supply + fit) | $2,800–$7,500 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Fencing Materials in {city}

**Treated timber:** Most common in NZ. Cost-effective, natural look. Requires painting or staining every 5–8 years. H4-treated posts required in-ground.

**Colorbond steel:** Low maintenance once installed, durable, 20+ year lifespan. More expensive upfront but lower lifetime cost.

**Concrete block:** Most durable, excellent acoustic and security properties. Highest upfront cost.

**Post and rail (timber or Waratah):** Rural, lifestyle, and boundary fencing. Economical for long runs.

## Do I Need Consent for a Fence in {city}?

Generally **no consent** is required for residential boundary fences up to 2.0m in most zones. Exceptions:

- Fences over 2.0m may require consent
- Pool fences must comply with NZ Building Code (Clause F9) regardless of height
- Front boundary fences in some zones have height restrictions
- Check with {region} Council for your specific zone

Boundary disputes: if there's disagreement with a neighbour about the boundary line, get a registered surveyor to peg it before building.

**Find {city} fence installers:** [Fence Installers {city}](/trades/fencing/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does fencing cost in {city}?**
Timber privacy fence (1.8m): {timber}/m. Colorbond: $220–$420/m. 30m of timber fencing: approx $5,400–$11,400.

*Related: [Fencing Cost NZ](/articles/fencing-cost-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/) | [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/)*
"""


# ── Heat Pump Installer gap fills (smaller cities) ─────────────────────────────

HEATPUMP_DATA = {
    "napier":           ("$3,200–$5,800", "$5,500–$11,000", "Napier's warm summers and cool winters make a heat pump an ideal year-round solution. Hawke's Bay's sunny climate means cooling demand is significant in summer, making reverse-cycle heat pumps a strong investment for Napier homes."),
    "new-plymouth":     ("$3,200–$5,800", "$5,500–$11,000", "New Plymouth's mild but wet climate means heating is important, especially in winter. Heat pumps are the most energy-efficient heating option available for Taranaki homes."),
    "palmerston-north": ("$3,100–$5,600", "$5,300–$10,500", "Palmerston North's cold winters and frequent wind make effective heating essential. Heat pumps are NZ's most efficient heater — typically 3x more efficient than electric heaters, which matters in the Manawatu's cold winters."),
    "nelson":           ("$3,200–$5,800", "$5,500–$11,000", "Nelson's cold winters despite its sunny reputation make heat pumps a popular choice. Nelson-Tasman has active Warmer Homes grants — check if you qualify for subsidised heat pump installation."),
    "rotorua":          ("$3,100–$5,600", "$5,300–$10,500", "Rotorua's cold winters and geothermal dampness make indoor heating important. Heat pumps are efficient and effective in Rotorua's climate. Some geothermal areas have air quality considerations — a local installer can advise on the best heating solution for your specific location."),
}

def heatpump_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    single, multi, local = HEATPUMP_DATA[city_key]

    return f"""---
title: "Heat Pump Installers {city} 2026 — Heat Pump Costs, Brands and What to Expect"
description: "Heat pump installers {city} 2026 — {city} heat pump installation costs, single vs multi-split pricing, best brands, and how to find a reliable heat pump installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["heat pump installers {city}", "heat pump cost {city}", "heat pump installation {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what heat pump installers charge in {city} in 2026.

## {city} Heat Pump Installation Costs 2026

| Service | {city} typical cost |
|---|---|
| Single split system (supply + install) | {single} |
| Multi-split system 2 indoor units (supply + install) | {multi} |
| Ducted heat pump system (whole home) | $12,000–$28,000 |
| Heat pump service / regas | $180–$480 |
| Relocate existing heat pump | $480–$1,100 |
| Heat pump removal | $250–$600 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}. Prices vary significantly by kW capacity and brand.*

## Heat Pump Sizing for {city}

The right kW capacity depends on your room size:

| Room size | Recommended capacity |
|---|---|
| Small bedroom / office (<15m²) | 2.0–2.5 kW |
| Medium living room (15–30m²) | 2.5–4.0 kW |
| Large open plan (30–60m²) | 5.0–7.0 kW |
| Very large / high stud (60m²+) | 7.0–12.0 kW |

A good installer will assess your room dimensions, insulation, and windows before recommending a size. Don't just go by the cheapest unit — undersized heat pumps run constantly and don't heat properly.

## {city} Heat Pump Market

{local}

## Popular Brands in NZ

| Brand | Notes |
|---|---|
| **Mitsubishi Electric** | Premium reliability, very popular in NZ |
| **Daikin** | High efficiency, good range |
| **Fujitsu** | Strong mid-range option, good value |
| **Panasonic** | Good efficiency ratings |
| **LG** | Competitive pricing |
| **Samsung** | Good warranty options |

All major brands sold in NZ perform well. Mitsubishi Electric and Daikin have the best service network.

## Installation Requirements

- Heat pumps must be installed by a **registered refrigeration technician** (handling refrigerant is restricted)
- Outdoor unit must have adequate clearance (check manufacturer spec — usually 300mm+)
- Some apartment buildings have rules about outdoor unit placement — check your body corporate

**Warmer Homes / Healthy Homes:** Rental properties must meet Healthy Homes Standards for heating — a heat pump is the most common compliant heating solution.

**Find {city} heat pump installers:** [Heat Pump Installers {city}](/trades/heat-pump-installation/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does heat pump installation cost in {city}?**
Single split system (supply + install): {single}. Multi-split 2 rooms: {multi}.

*Related: [Heat Pump Cost NZ](/articles/heat-pump-cost-nz/) | [Insulation Installers {city}](/articles/insulation-installer-{city_key}-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = [
    # Bathroom renovators — main cities
    ("bathroom-renovator-auckland-nz",     lambda: bathroom_article("auckland")),
    ("bathroom-renovator-wellington-nz",   lambda: bathroom_article("wellington")),
    ("bathroom-renovator-christchurch-nz", lambda: bathroom_article("christchurch")),
    ("bathroom-renovator-hamilton-nz",     lambda: bathroom_article("hamilton")),
    ("bathroom-renovator-tauranga-nz",     lambda: bathroom_article("tauranga")),
    ("bathroom-renovator-dunedin-nz",      lambda: bathroom_article("dunedin")),
    # Deck builders — main cities
    ("deck-builder-auckland-nz",           lambda: deck_article("auckland")),
    ("deck-builder-wellington-nz",         lambda: deck_article("wellington")),
    ("deck-builder-christchurch-nz",       lambda: deck_article("christchurch")),
    ("deck-builder-hamilton-nz",           lambda: deck_article("hamilton")),
    ("deck-builder-tauranga-nz",           lambda: deck_article("tauranga")),
    ("deck-builder-dunedin-nz",            lambda: deck_article("dunedin")),
    # Rubbish removal — main cities
    ("rubbish-removal-auckland-nz",        lambda: rubbish_article("auckland")),
    ("rubbish-removal-wellington-nz",      lambda: rubbish_article("wellington")),
    ("rubbish-removal-christchurch-nz",    lambda: rubbish_article("christchurch")),
    ("rubbish-removal-hamilton-nz",        lambda: rubbish_article("hamilton")),
    ("rubbish-removal-tauranga-nz",        lambda: rubbish_article("tauranga")),
    ("rubbish-removal-dunedin-nz",         lambda: rubbish_article("dunedin")),
    # Insulation gap fills
    ("insulation-installer-napier-nz",           lambda: insulation_article("napier")),
    ("insulation-installer-new-plymouth-nz",     lambda: insulation_article("new-plymouth")),
    ("insulation-installer-palmerston-north-nz", lambda: insulation_article("palmerston-north")),
    ("insulation-installer-nelson-nz",           lambda: insulation_article("nelson")),
    ("insulation-installer-rotorua-nz",          lambda: insulation_article("rotorua")),
    # Fence installer gap fills
    ("fence-installer-napier-nz",           lambda: fence_article("napier")),
    ("fence-installer-new-plymouth-nz",     lambda: fence_article("new-plymouth")),
    ("fence-installer-palmerston-north-nz", lambda: fence_article("palmerston-north")),
    ("fence-installer-nelson-nz",           lambda: fence_article("nelson")),
    ("fence-installer-rotorua-nz",          lambda: fence_article("rotorua")),
    # Heat pump gap fills
    ("heat-pump-installer-napier-nz",           lambda: heatpump_article("napier")),
    ("heat-pump-installer-new-plymouth-nz",     lambda: heatpump_article("new-plymouth")),
    ("heat-pump-installer-palmerston-north-nz", lambda: heatpump_article("palmerston-north")),
    ("heat-pump-installer-nelson-nz",           lambda: heatpump_article("nelson")),
    ("heat-pump-installer-rotorua-nz",          lambda: heatpump_article("rotorua")),
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
