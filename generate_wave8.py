#!/usr/bin/env python3
"""
Wave 8 SEO content generator — TradieTools NZ
Gap fills: solar, carpet layer, locksmith, house washer, carpenter, builder
New trade: pest control
Run: python3 generate_wave8.py
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

# ── Solar Installer gap fills ─────────────────────────────────────────────────

SOLAR_DATA = {
    "napier":           ("$8,500–$14,000", "$13,000–$21,000", "Napier's Hawke's Bay sunshine hours are among the highest in NZ — Napier consistently ranks as one of NZ's sunniest cities. This makes solar one of the best-performing investments for Hawke's Bay homeowners. Expect 4.5–5.5 peak sun hours per day on average."),
    "new-plymouth":     ("$8,500–$14,000", "$13,000–$21,000", "New Plymouth's westerly aspect and moderate sunshine hours make solar viable, though cloud cover is more frequent than sunnier east coast cities. A 6.6kW system typically generates 8,000–10,000 kWh per year in Taranaki."),
    "palmerston-north": ("$8,200–$13,500", "$12,500–$20,500", "Palmerston North has moderate sunshine hours affected by cloud from both coasts. Solar still delivers strong returns thanks to high Manawatu electricity prices. Battery storage is popular here due to grid reliability concerns."),
    "nelson":           ("$8,500–$14,000", "$13,000–$21,000", "Nelson is one of NZ's sunniest cities — Nelson-Tasman regularly records the most sunshine hours in the country. Solar performance in Nelson is excellent, with 5–6 peak sun hours per day making it one of NZ's best solar locations."),
    "rotorua":          ("$8,200–$13,500", "$12,500–$20,500", "Rotorua has moderate sunshine hours — good for solar, though less than sunnier east coast cities. Geothermal heating reduces some homes' energy bills, but solar is still worthwhile for hot water and general electricity."),
}

def solar_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    small, large, local = SOLAR_DATA[city_key]

    return f"""---
title: "Solar Installers {city} 2026 — Solar Panel Costs, Payback and What to Expect"
description: "Solar installers {city} 2026 — {city} solar panel installation costs, 6.6kW system pricing, battery storage, payback period, and how to find a reliable solar installer near you."
image: "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["solar installers {city}", "solar panels {city}", "solar installation cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what solar installation costs in {city} in 2026.

## {city} Solar Installation Costs 2026

| System size | {city} typical cost (supply + install) |
|---|---|
| 3kW system (small home / low usage) | $6,500–$10,500 |
| 6.6kW system (standard home) | {small} |
| 10kW system (large home / EV charging) | {large} |
| Battery storage — 10kWh (add-on) | $9,000–$14,000 |
| Solar hot water (evacuated tube) | $4,500–$8,500 |
| Panel replacement (per panel) | $280–$600 |
| System health check / service | $180–$380 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Solar Performance

{local}

**Estimated annual generation (6.6kW system):**

| Location factor | Annual generation estimate |
|---|---|
| Good north-facing roof | 9,000–11,000 kWh/year |
| Mixed aspect | 7,500–9,500 kWh/year |
| Partial shading | 6,000–8,000 kWh/year |

## Solar Payback in {city}

At current {city} electricity prices (~$0.30–$0.38/kWh), a 6.6kW system typically pays back in:

- **No battery:** 6–9 years
- **With battery:** 9–13 years

Solar adds to property value and payback improves as electricity prices rise.

## Choosing a Solar Installer in {city}

- Look for **SEANZ members** (Sustainable Electricity Association of New Zealand)
- Ask for a **production estimate** based on your actual roof and location
- Compare warranties: panels (25yr), inverter (10–12yr), workmanship (5–10yr)
- Get at least 2–3 quotes — solar pricing varies significantly between installers

**Find {city} solar installers:** [Solar Installers {city}](/trades/solar-installers/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does solar cost in {city}?**
Standard 6.6kW system (supply + install): {small}. Battery storage adds $9,000–$14,000.

*Related: [Solar Panel Cost NZ](/articles/solar-panel-cost-nz/) | [Insulation Installers {city}](/articles/insulation-installer-{city_key}-nz/)*
"""


# ── Carpet Layer gap fills ─────────────────────────────────────────────────────

CARPET_DATA = {
    "napier":           ("$38–$85/m²", "$65–$140/m²", "Napier's warm Hawke's Bay climate means wool carpet is popular — it performs beautifully in the region's warm summers and cool winters. Carpet layers in Napier are busy with the area's active property market."),
    "new-plymouth":     ("$38–$85/m²", "$65–$140/m²", "New Plymouth has steady carpet demand from both residential and commercial properties. The Taranaki region's moderate climate makes carpet a comfortable choice year-round."),
    "palmerston-north": ("$36–$82/m²", "$62–$135/m²", "Palmerston North's cold winters make carpet particularly appealing — warm underfoot and good insulation contribution. The student rental market drives ongoing carpet replacement demand in Palmerston North."),
    "nelson":           ("$38–$85/m²", "$65–$140/m²", "Nelson's lifestyle focus means quality flooring is valued. Wool carpet from NZ's strong wool industry is popular in Nelson-Tasman homes."),
    "rotorua":          ("$36–$82/m²", "$62–$135/m²", "Rotorua's cold winters make warm carpet popular. Geothermal moisture in some areas requires good underlay selection to prevent moisture issues beneath carpet."),
}

def carpet_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    supply_fit, premium, local = CARPET_DATA[city_key]

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
| Budget synthetic carpet (supply + fit, per m²) | $38–$65/m² |
| Mid-range carpet (supply + fit, per m²) | {supply_fit} |
| Premium / wool carpet (supply + fit, per m²) | {premium} |
| Underlay (supply + fit, per m², standard) | $12–$22/m² |
| Underlay (premium, per m²) | $18–$38/m² |
| Carpet removal + disposal (per m²) | $8–$18/m² |
| Carpet re-stretching (per room) | $80–$180 |
| Carpet repair (per m²) | $80–$200 |
| Full 3-bed home re-carpet (mid-range) | $4,500–$9,500 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Carpet Types in {city}

**Nylon:** Most durable synthetic. Good for high-traffic areas. Excellent stain resistance.
**Polyester (PET):** Soft underfoot, good value, good colour retention. Less durable than nylon.
**Polypropylene (olefin):** Budget-friendly, moisture-resistant. Good for rentals.
**Wool:** Premium NZ product. Naturally fire-resistant, durable, excellent thermal properties. 2–3x the cost of synthetics but lasts 20–30 years.
**Wool blend:** Good balance of wool performance at lower cost.

## Underlay Matters

Don't skimp on underlay — it adds comfort underfoot and extends carpet life significantly. A good underlay on a mid-range carpet outperforms cheap underlay on a premium carpet. Standard underlay: $12–$22/m². Premium: $18–$38/m².

**Find {city} carpet layers:** [Carpet Layers {city}](/trades/carpet-layers/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does carpet cost in {city}?**
Mid-range carpet (supply + fit): {supply_fit}/m². Full 3-bed home re-carpet: $4,500–$9,500.

*Related: [Carpet Cost NZ](/articles/carpet-cost-nz/) | [Floor Sanders {city}](/articles/floor-sander-{city_key}-nz/)*
"""


# ── Locksmith gap fills ────────────────────────────────────────────────────────

LOCKSMITH_DATA = {
    "napier":           ("$130–$280", "$200–$480", "Napier has several reliable locksmiths serving the Hawke's Bay region. The city's tourism and hospitality sector also creates commercial locksmith demand for hotels and motels."),
    "new-plymouth":     ("$130–$280", "$200–$480", "New Plymouth locksmiths serve both the residential market and the commercial/industrial sector tied to the Taranaki oil and gas industry."),
    "palmerston-north": ("$125–$270", "$190–$460", "Palmerston North locksmiths serve a mix of residential, student accommodation, and commercial clients. The student rental market generates regular lock change and key duplication work."),
    "nelson":           ("$130–$280", "$200–$480", "Nelson locksmiths serve the city's residential and tourism/hospitality sectors. The Nelson-Tasman region's lifestyle property market also creates demand for rural property security work."),
    "rotorua":          ("$125–$270", "$190–$460", "Rotorua locksmiths are busy with the city's large tourism accommodation sector — hotels, motels, and holiday parks have ongoing commercial locksmith requirements."),
}

def locksmith_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    callout, emergency, local = LOCKSMITH_DATA[city_key]

    return f"""---
title: "Locksmiths {city} 2026 — Locksmith Costs, Lockout Prices and What to Expect"
description: "Locksmiths {city} 2026 — {city} locksmith call-out rates, lockout costs, lock replacement prices, rekeying costs, and how to find a reliable locksmith near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["locksmiths {city}", "locksmith {city}", "locksmith cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what locksmiths charge in {city} in 2026.

## {city} Locksmith Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (standard hours) | {callout} |
| Emergency lockout (after hours) | {emergency} |
| Lock picking / non-destructive entry | $130–$280 |
| Lock drilling (destructive entry) | $180–$380 |
| Lock replacement — deadbolt (supply + fit) | $220–$520 |
| Lock replacement — knob/lever (supply + fit) | $180–$420 |
| Rekeying (per lock, same key) | $65–$150 |
| Master key system (per lock) | $85–$200 |
| Duplicate key cutting (per key) | $8–$35 |
| Safe opening | $250–$650 |
| Security assessment | $120–$280 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Locksmith Market

{local}

## Rekeying vs Replacing Locks

**Rekey:** Change the internal pins so existing keys no longer work. New keys cut to suit. Cost: $65–$150 per lock. Best when the lock is in good condition but you need to change who has access (new tenants, after losing keys).

**Replace:** Fit an entirely new lock mechanism. Cost: $180–$520 per lock. Best when the lock is worn, damaged, or you want to upgrade security grade.

**Master key systems:** Have multiple locks that open with one master key, plus individual keys for each lock. Useful for landlords with multiple tenants, or commercial premises.

## When to Call a Locksmith in {city}

- Locked out of home or vehicle
- Lost keys — rekey or replace for security
- Moving into a new rental — always rekey after previous tenants
- Upgrading to Grade 1 or Grade 2 security locks
- After a break-in — assess and upgrade entry points

**Find {city} locksmiths:** [Locksmiths {city}](/trades/locksmiths/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a locksmith cost in {city}?**
Standard call-out: {callout}. Emergency lockout (after hours): {emergency}. Lock replacement: $180–$520.

*Related: [Locksmith Cost NZ](/articles/locksmith-cost-nz/)*
"""


# ── House Washer gap fills ─────────────────────────────────────────────────────

HOUSEWASH_DATA = {
    "napier":           ("$280–$580", "$380–$750", "Napier's warm humid climate and proximity to the coast encourages mould and lichen growth on exterior surfaces. Annual or bi-annual house washing is recommended for most Napier properties."),
    "new-plymouth":     ("$280–$580", "$380–$750", "New Plymouth's high rainfall and westerly salt air from the Tasman Sea accelerates algae and mould growth on home exteriors. Regular house washing extends exterior paint life significantly."),
    "palmerston-north": ("$270–$560", "$360–$720", "Palmerston North's damp conditions from both coastal influences promote mould growth, particularly on south-facing walls. House washing before repainting is essential preparation."),
    "nelson":           ("$280–$580", "$380–$750", "Nelson's sunny climate slows mould growth compared to wetter cities, but lichen on roofs and decks is still common. Pre-paint house washing is a routine preparation step for Nelson homes."),
    "rotorua":          ("$270–$560", "$360–$720", "Rotorua's geothermal environment and moderate rainfall promotes algae and mould on exterior surfaces. Some geothermal areas have mineral deposits on surfaces that require specialist cleaning approaches."),
}

def housewash_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
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
| Roof treatment (moss / lichen) | $280–$680 |
| Driveway / path pressure wash | $120–$280 |
| Deck wash (per m²) | $4–$12/m² |
| Gutter clean (per linear metre) | $6–$15/m |
| Window clean (exterior, per window) | $8–$20 |
| Full exterior package (house + roof + drive) | $650–$1,400 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} House Washing Market

{local}

## Soft Wash vs Pressure Wash

**Soft wash (low pressure + chemical treatment):** Preferred for most NZ homes. A biocide kills mould, algae, and lichen at the root — prevents quick regrowth. Safe on weatherboards, painted surfaces, and roofs. Results last 2–4 years.

**High pressure wash:** Good for concrete driveways, paths, decks. Too aggressive for most painted or clad surfaces — can force water behind cladding or strip paint. Not recommended for roof washing.

**Which to use:** Soft wash for the house exterior and roof. High pressure for concrete and hard surfaces.

## How Often Should You Wash Your House in {city}?

{local} For most {city} homes: every 2–3 years minimum. Annual washing recommended if you have a lot of shading (overhanging trees) or if south-facing walls are affected by persistent mould.

**Pre-paint:** Always wash before repainting — paint won't adhere properly to mould or dirt.

**Find {city} house washers:** [House Washers {city}](/trades/house-washing/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does house washing cost in {city}?**
Standard 3-bed house: {standard}. Large house: {large}. Full exterior package (house + roof + driveway): $650–$1,400.

*Related: [House Washing Cost NZ](/articles/house-washing-cost-nz/) | [Painters {city}](/articles/painter-{city_key}-nz/)*
"""


# ── Carpenter gap fills ────────────────────────────────────────────────────────

CARPENTER_DATA = {
    "new-plymouth":     ("$90–$155/hr", "$70–$145", "New Plymouth's active housing market and lifestyle property sector keeps carpenters busy. Deck building, pergolas, and interior fit-outs are popular in Taranaki."),
    "palmerston-north": ("$85–$150/hr", "$65–$140", "Palmerston North's large student and rental accommodation sector drives ongoing carpentry demand for repairs and fit-outs. Residential renovation work is also strong."),
    "nelson":           ("$88–$155/hr", "$68–$143", "Nelson's lifestyle property market and active renovation scene keeps carpenters busy. The region's strong building culture and quality tradespeople make Nelson a competitive carpentry market."),
    "rotorua":          ("$85–$150/hr", "$65–$140", "Rotorua's mix of residential, tourism accommodation, and lifestyle properties creates steady carpentry demand. Deck building and outdoor structures are popular given the region's outdoor lifestyle focus."),
}

def carpenter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    hourly, callout, local = CARPENTER_DATA[city_key]

    return f"""---
title: "Carpenters {city} 2026 — Carpentry Rates, Costs and What to Expect"
description: "Carpenters {city} 2026 — {city} carpenter hourly rates, renovation costs, deck building prices, and how to find a reliable carpenter near you."
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
| Call-out / minimum charge | {callout} |
| Deck construction (per m², supply + install) | $1,500–$3,000/m² |
| Kitchen installation (flat-pack, labour only) | $1,800–$4,500 |
| Door hang and fit (per door) | $180–$380 |
| Window installation (per window) | $280–$650 |
| Framing / structural work (per hour) | $95–$165/hr |
| Architrave / skirting (per m linear) | $18–$45/m |
| Built-in wardrobe (per m wide) | $850–$2,200/m |
| Pergola / outdoor structure | $4,500–$18,000 |
| Bathroom / laundry fit-out (labour) | $2,500–$6,500 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## LBP vs General Carpenter

**Licensed Building Practitioner (LBP):** Required for restricted building work — structural framing, weathertightness work, foundations. If your project requires building consent, restricted work must be carried out or supervised by an LBP.

**General carpenter:** Can do non-restricted carpentry — fit-outs, furniture, decks under 1m high (no consent), cabinetry installation.

Always check your carpenter holds an LBP licence for work that requires it. Verify at [lbp.govt.nz](https://www.lbp.govt.nz).

**Find {city} carpenters:** [Carpenters {city}](/trades/carpenters/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a carpenter cost in {city}?**
Hourly rate: {hourly}. Deck construction: $1,500–$3,000/m². Door hang: $180–$380 per door.

*Related: [Builder {city}](/articles/builder-{city_key}-nz/) | [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/)*
"""


# ── Builder gap fills ─────────────────────────────────────────────────────────

BUILDER_DATA = {
    "napier":           ("$95–$165/hr", "$70–$150", "Napier's Hawke's Bay property market is strong — earthquake-related heritage and the ongoing demand for quality homes keeps builders busy. The region's growing population drives new residential construction.", "Napier / Hawke's Bay", "Hawke's Bay"),
    "new-plymouth":     ("$98–$168/hr", "$72–$152", "New Plymouth has a buoyant building market driven by the Taranaki energy sector and lifestyle appeal. Quality is valued in New Plymouth — tradies with a strong reputation fill their books quickly.", "New Plymouth / Taranaki", "Taranaki"),
}

def builder_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    hourly, callout, local, area, area2 = BUILDER_DATA[city_key]

    return f"""---
title: "Builders {city} 2026 — Builder Rates, Renovation Costs and What to Expect"
description: "Builders {city} 2026 — {city} builder hourly rates, renovation costs, new build pricing, and how to find a reliable licensed builder near you."
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
| New home build (per m², turnkey) | $2,800–$4,800/m² |
| Major renovation (kitchen, bathroom, extension) | $95,000–$350,000+ |
| Extension (per m²) | $2,500–$4,500/m² |
| Bathroom renovation (complete) | $14,000–$40,000 |
| Kitchen renovation (complete) | $16,000–$55,000 |
| Deck construction (per m²) | $1,500–$3,000/m² |
| Earthquake strengthening / LIM report repairs | $8,000–$80,000+ |
| Building inspection pre-purchase | $400–$900 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Building Market

{local}

## Licensed Building Practitioners in {city}

Any restricted building work must be carried out or supervised by an **LBP (Licensed Building Practitioner)**. Restricted work includes:

- Structural framing
- Foundation work
- Weathertightness work (cladding, roofing, windows)
- Design work

Always verify your builder's LBP licence at [lbp.govt.nz](https://www.lbp.govt.nz) before signing a contract.

## Getting the Best Result in {city}

- Get 2–3 written quotes with detailed scope of work
- Check LBP licence and confirm they carry public liability and contract works insurance
- Ask for references from recent {area} projects
- Never pay more than 10–20% upfront — milestone payments are standard
- Understand consent requirements before work begins

**Find {city} builders:** [Builders {city}](/trades/builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a builder cost in {city}?**
Hourly rate: {hourly}. New build: $2,800–$4,800/m². Major renovation: $95,000–$350,000+.

*Related: [Builder Pricing Guide NZ](/articles/builder-pricing-guide-nz-2026/) | [Carpenters {city}](/articles/carpenter-{city_key}-nz/) | [Kitchen Renovation {city}](/articles/kitchen-renovator-{city_key}-nz/)*
"""


# ── Pest Control ──────────────────────────────────────────────────────────────

PEST_DATA = {
    "auckland":     ("$180–$380", "$280–$650", "Auckland's subtropical climate and dense urban population make it NZ's most active pest control market. Rodents, cockroaches, and ants are the most common residential pests. Wasps are a major issue in summer across Auckland's bush margins."),
    "wellington":   ("$180–$380", "$280–$650", "Wellington's cold winters push rodents indoors — rat and mouse infestations are common in autumn and winter. The city's older villa stock has plenty of entry points for rodents. Wasp nests are common in Wellington's bush suburbs."),
    "christchurch": ("$160–$350", "$250–$600", "Post-earthquake Christchurch disturbed rodent populations across the city. The ongoing rebuild and demolition work continues to push pests into residential properties. Christchurch's flat terrain and open drains can harbour cockroaches and rats."),
    "hamilton":     ("$150–$320", "$240–$580", "Hamilton's warm humid Waikato climate suits a wide range of pests. Rodents, cockroaches, and ants are the most common calls. Borer (wood-boring beetles) is a significant issue in Hamilton's older homes."),
    "tauranga":     ("$160–$350", "$250–$600", "Tauranga's warm subtropical climate is excellent for pest activity year-round. Cockroaches, ants, and rodents are all common. Borer treatment is a regular service call in Bay of Plenty's older homes."),
    "dunedin":      ("$140–$300", "$220–$550", "Dunedin's cold climate limits the pest range compared to northern cities, but rodents are a significant issue — particularly in the student accommodation belt and older inner-city suburbs. Fleas are common in student rentals."),
}

def pest_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    callout, full, local = PEST_DATA[city_key]

    return f"""---
title: "Pest Control {city} 2026 — Pest Control Costs, Common Pests and What to Expect"
description: "Pest control {city} 2026 — {city} pest control costs, rodent treatment prices, cockroach and ant extermination rates, and how to find a reliable pest controller near you."
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
| Inspection / assessment | $100–$220 |
| Rodent treatment (baiting, 3-bed home) | {callout} |
| Cockroach treatment (3-bed home) | $180–$380 |
| Ant treatment (exterior + interior) | $160–$320 |
| Wasp nest removal | $130–$280 |
| Flea treatment (3-bed home) | $180–$380 |
| Borer treatment (spray, per m²) | $12–$28/m² |
| Spider treatment (exterior) | $140–$280 |
| Ongoing pest maintenance contract (quarterly) | {full} |
| Commercial pest control (per visit, small premises) | $280–$650 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Common Pests

{local}

### Rodents (Rats and Mice)

The most common pest call-out in {city}. Signs: droppings, gnaw marks, scratching sounds in walls/ceiling, pet food disappearing. Treatment: baiting stations inside and outside the property. Follow-up visit typically required.

### Cockroaches

German cockroaches (small, prefer kitchens/bathrooms) and American cockroaches (large, prefer warm damp areas). Treatment: gel bait plus residual spray. Multiple visits often needed to break the egg cycle.

### Borer (Wood-Boring Beetle)

Common in NZ timber homes — especially older rimu and macrocarpa. Signs: small round holes in timber, powdery frass (sawdust). Treatment: surface spray penetrates and kills larvae. Best done in summer when larvae are active near the surface.

### Wasps

NZ German wasps are aggressive and the nests get very large by summer. Nest removal involves chemical treatment at night (when wasps are inactive). **Do not attempt DIY wasp nest removal on large nests.**

## NZ Pest Control Licensing

Pest controllers applying restricted pesticides must hold a **GROWSAFE certificate** or equivalent. Always ask for proof of certification before allowing pesticide treatment in your home.

**Find {city} pest controllers:** [Pest Control {city}](/trades/pest-control/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does pest control cost in {city}?**
Rodent treatment: {callout}. Quarterly maintenance contract: {full}/year.

*Related: [Pest Control Cost NZ](/articles/pest-control-cost-nz/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = [
    # Solar gap fills
    ("solar-installer-napier-nz",           lambda: solar_article("napier")),
    ("solar-installer-new-plymouth-nz",     lambda: solar_article("new-plymouth")),
    ("solar-installer-palmerston-north-nz", lambda: solar_article("palmerston-north")),
    ("solar-installer-nelson-nz",           lambda: solar_article("nelson")),
    ("solar-installer-rotorua-nz",          lambda: solar_article("rotorua")),
    # Carpet layer gap fills
    ("carpet-layer-napier-nz",           lambda: carpet_article("napier")),
    ("carpet-layer-new-plymouth-nz",     lambda: carpet_article("new-plymouth")),
    ("carpet-layer-palmerston-north-nz", lambda: carpet_article("palmerston-north")),
    ("carpet-layer-nelson-nz",           lambda: carpet_article("nelson")),
    ("carpet-layer-rotorua-nz",          lambda: carpet_article("rotorua")),
    # Locksmith gap fills
    ("locksmith-napier-nz",           lambda: locksmith_article("napier")),
    ("locksmith-new-plymouth-nz",     lambda: locksmith_article("new-plymouth")),
    ("locksmith-palmerston-north-nz", lambda: locksmith_article("palmerston-north")),
    ("locksmith-nelson-nz",           lambda: locksmith_article("nelson")),
    ("locksmith-rotorua-nz",          lambda: locksmith_article("rotorua")),
    # House washer gap fills
    ("house-washer-napier-nz",           lambda: housewash_article("napier")),
    ("house-washer-new-plymouth-nz",     lambda: housewash_article("new-plymouth")),
    ("house-washer-palmerston-north-nz", lambda: housewash_article("palmerston-north")),
    ("house-washer-nelson-nz",           lambda: housewash_article("nelson")),
    ("house-washer-rotorua-nz",          lambda: housewash_article("rotorua")),
    # Carpenter gap fills
    ("carpenter-new-plymouth-nz",     lambda: carpenter_article("new-plymouth")),
    ("carpenter-palmerston-north-nz", lambda: carpenter_article("palmerston-north")),
    ("carpenter-nelson-nz",           lambda: carpenter_article("nelson")),
    ("carpenter-rotorua-nz",          lambda: carpenter_article("rotorua")),
    # Builder gap fills
    ("builder-napier-nz",       lambda: builder_article("napier")),
    ("builder-new-plymouth-nz", lambda: builder_article("new-plymouth")),
    # Pest control — main cities
    ("pest-control-auckland-nz",      lambda: pest_article("auckland")),
    ("pest-control-wellington-nz",    lambda: pest_article("wellington")),
    ("pest-control-christchurch-nz",  lambda: pest_article("christchurch")),
    ("pest-control-hamilton-nz",      lambda: pest_article("hamilton")),
    ("pest-control-tauranga-nz",      lambda: pest_article("tauranga")),
    ("pest-control-dunedin-nz",       lambda: pest_article("dunedin")),
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
