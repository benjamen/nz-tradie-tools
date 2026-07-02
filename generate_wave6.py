#!/usr/bin/env python3
"""
Wave 6 SEO content generator — TradieTools NZ
Gap fills: gasfitter, concreter, drainlayer, landscaper for smaller cities
New trades: glazier, kitchen renovator, floor sander
Run: python3 generate_wave6.py
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

# ── Gasfitter (smaller cities) ────────────────────────────────────────────────

GASFITTER_DATA = {
    "dunedin":          ("$90–$160/hr", "$65–$145", "Dunedin uses a mix of natural gas and LPG. The city's cold winters drive strong demand for gas heating — gas fires and log burners with gas backup are popular in Dunedin's older homes.", "Natural gas is available in parts of Dunedin via First Gas. LPG is used where mains gas isn't connected."),
    "napier":           ("$90–$160/hr", "$65–$145", "Napier's Hawke's Bay climate means gas heating is less critical than in southern cities, but gas cooking and outdoor BBQ connections are popular. LPG is common where natural gas isn't available.", "Natural gas availability is limited in Napier — LPG cylinders are the most common option for most properties."),
    "new-plymouth":     ("$95–$165/hr", "$70–$150", "New Plymouth has strong gas demand from both residential and industrial/petrochemical sectors. The oil and gas industry in Taranaki means industrial gasfitters are in demand, but residential gasfitters serve the city's homeowners well.", "Natural gas is available in New Plymouth via First Gas. The Taranaki gas field historically provided low-cost gas to the region."),
    "palmerston-north": ("$88–$158/hr", "$63–$143", "Palmerston North has steady residential gas demand. The city's cold winters make gas heating attractive. LPG is used in areas without mains gas connections.", "Natural gas is available in parts of Palmerston North. LPG is used in outer suburbs and rural areas."),
    "nelson":           ("$90–$160/hr", "$65–$145", "Nelson's mild climate reduces gas heating demand compared to colder cities, but gas cooking and outdoor entertaining gas connections are popular in lifestyle-oriented Nelson homes.", "Natural gas is not widely available in Nelson — LPG cylinders and tanks are the primary option for gas appliances."),
    "rotorua":          ("$90–$160/hr", "$65–$145", "Rotorua's geothermal environment means some areas have access to geothermal energy for heating, but conventional gas appliances are still widely used. LPG is the most common gas source.", "Natural gas is limited in Rotorua — LPG is the standard fuel for gas appliances in most Rotorua properties."),
}

def gasfitter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    hourly, callout, local, gas_network = GASFITTER_DATA[city_key]

    return f"""---
title: "Gasfitters {city} 2026 — Gas Fitting Rates, Costs and What Requires a Licensed Gasfitter"
description: "Gasfitters {city} 2026 — {city} gasfitter rates, gas hob installation cost, gas hot water prices, LPG vs natural gas, and how to find a licensed gasfitter near you."
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
| Call-out fee (weekday) | {callout} |
| Hourly rate | {hourly} |
| Gas hob installation | $380–$850 |
| Gas oven installation | $480–$1,050 |
| Gas hot water cylinder (install) | $1,900–$3,900 |
| Continuous flow gas hot water (install) | $1,700–$3,300 |
| Gas fire installation (flued) | $2,800–$6,500 |
| Gas BBQ point installation | $380–$850 |
| LPG to natural gas conversion | $450–$1,400 |
| Gas leak detection | $180–$480 |
| Gas line extension (per metre) | $75–$190/m |
| Annual gas appliance service | $140–$320 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Gas Supply

{gas_network}

## What Requires a Licensed Gasfitter in NZ

All gasfitting must be done by someone registered with the PGDB (Plumbers, Gasfitters and Drainlayers Board):

- Connecting any gas appliance (hob, oven, heater, hot water, BBQ point)
- Installing or modifying gas pipework
- LPG to natural gas conversions
- Testing gas systems after any work

**Verify at:** [pgdb.co.nz](https://www.pgdb.co.nz) — never allow unlicensed gasfitting.

**Find {city} gasfitters:** [Gasfitters {city}](/trades/gasfitters/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does gasfitting cost in {city}?**
Call-out: {callout}. Gas hob installation: $380–$850. Gas hot water cylinder: $1,900–$3,900 installed.

**Do I need a licensed gasfitter for a gas hob in {city}?**
Yes — connecting any gas appliance is restricted work. A compliance certificate is legally required.

---

*Related: [Gas Fitting Cost NZ](/articles/gas-fitting-cost-nz/) | [Hot Water Cylinder Cost NZ](/articles/hot-water-cylinder-cost-nz/)*
"""


# ── Concreter (smaller cities) ────────────────────────────────────────────────

CONCRETER_DATA = {
    "napier":           ("$100–$210/m²", "$5,000–$16,000", "Napier's warm Hawke's Bay climate is good for concrete curing. The art deco city has a mix of older and newer construction, with driveways and paths a common job type."),
    "new-plymouth":     ("$100–$210/m²", "$5,000–$16,000", "New Plymouth's coastal westerly weather means concrete work must account for wind during pouring and curing. Driveways and paths are popular as homeowners improve their properties."),
    "palmerston-north": ("$95–$205/m²",  "$4,800–$15,500", "Palmerston North's windy conditions can challenge concrete work — experienced concreters manage pour timing around wind. The city's affordable land drives good demand for new driveways and shed slabs."),
    "nelson":           ("$100–$210/m²", "$5,000–$16,000", "Nelson's sunny climate is excellent for concrete work — low rainfall and warm temperatures make for ideal curing conditions. Outdoor entertaining areas and driveways are popular projects."),
    "rotorua":          ("$95–$205/m²",  "$4,800–$15,500", "Rotorua's volcanic soils can affect ground conditions for concrete work. Some geothermal areas require specialist advice on foundation and slab design. Standard residential driveway and path work is common."),
}

def concreter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
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
| Concrete driveway (standard, 40m²) | {driveway} |
| Concrete path (per m²) | $95–$195/m² |
| Concrete slab — shed/garage (per m²) | $100–$215/m² |
| Exposed aggregate (per m², premium) | $145–$290/m² |
| Coloured/stencilled concrete (per m²) | $155–$310/m² |
| Concrete steps (per step) | $280–$680 |
| Demolish + remove old concrete (per m²) | $38–$85/m² |
| Concrete sealing (per m²) | $14–$38/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Concrete Finishes

**Broom finish:** Standard texture for grip — most economical.
**Exposed aggregate:** Stones embedded in the surface — durable and attractive for driveways.
**Stamped / coloured:** Higher cost, more decorative — popular for outdoor entertaining areas.

## Getting Quotes in {city}

- Get 2–3 written quotes including materials and disposal
- Confirm concrete strength (25–32 MPa for driveways)
- Check sub-base preparation is included
- Minimum thickness: 100mm for pedestrian, 125mm for vehicles

**Find {city} concreters:** [Concreters {city}](/trades/concreters/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a concrete driveway cost in {city}?**
Standard 40m² driveway: {driveway}. Exposed aggregate adds 30–50%.

*Related: [Concrete Driveway Cost NZ](/articles/concrete-driveway-cost-nz/) | [Asphalt Driveway Cost NZ](/articles/asphalt-driveway-cost-nz/)*
"""


# ── Drainlayer (smaller cities) ───────────────────────────────────────────────

DRAINLAYER_DATA = {
    "napier":           ("$90–$160/hr", "$65–$145", "Napier's older housing stock and the 1931 earthquake's long-term effects on underground infrastructure mean drain inspection and repair work is common. Pre-purchase drain camera inspections are particularly recommended for older Napier properties."),
    "new-plymouth":     ("$95–$165/hr", "$70–$150", "New Plymouth has steady residential drainlaying demand. The coastal environment and strong rainfall mean stormwater management is important. Industrial drain work for the petrochemical sector also keeps specialist drainlayers busy."),
    "palmerston-north": ("$88–$158/hr", "$63–$143", "Palmerston North's older inner-city housing has original clay drain pipes approaching end of life. Tree root intrusion in older suburbs is common, and the flat terrain can cause slow drainage in poorly designed systems."),
    "nelson":           ("$90–$160/hr", "$65–$145", "Nelson's growing population and lifestyle property market generate steady drainlaying demand. Rural and lifestyle block septic system work is a significant part of the Nelson-Tasman drainlaying market."),
    "rotorua":          ("$90–$160/hr", "$65–$145", "Rotorua's geothermal environment can affect drain materials — hydrogen sulphide and acidic groundwater can corrode standard pipes faster than elsewhere. Local drainlayers experienced in geothermal areas are preferred."),
}

def drainlayer_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    hourly, callout, local = DRAINLAYER_DATA[city_key]

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
| Call-out fee (weekday) | {callout} |
| Hourly rate | {hourly} |
| Drain camera inspection | $240–$480 |
| High-pressure water jetting (unblock) | $190–$480 |
| Root cutting / clearing | $280–$680 |
| Drain repair (pipe patch, per metre) | $380–$880/m |
| Drain replacement (per metre, open cut) | $480–$1,150/m |
| Sewer lateral connection (new) | $2,200–$6,500 |
| Stormwater connection (new) | $1,900–$5,800 |
| Septic tank installation | $7,500–$19,000+ |
| Drainage report / pre-purchase inspection | $380–$850 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## What Requires a Licensed Drainlayer in NZ

All work connecting to the public sewer or stormwater network must be done by a PGDB-registered drainlayer. **Verify at:** [pgdb.co.nz](https://www.pgdb.co.nz)

**Signs you need a drainlayer:** Slow drains, gurgling pipes, wet patches over drain lines, sewage smells, or tree roots near old pipes. A camera inspection ($240–$480) diagnoses the problem before any digging.

**Find {city} drainlayers:** [Drainlayers {city}](/trades/drainlayers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Blocked Drain Cost NZ](/articles/blocked-drain-cost-nz/) | [Drainage Solutions Cost NZ](/articles/drainage-solutions-cost-nz/)*
"""


# ── Landscaper (smaller cities) ───────────────────────────────────────────────

LANDSCAPER_DATA = {
    "napier":           "Napier's warm Hawke's Bay climate is ideal for outdoor living — long summers and mild winters make decks, gardens, and outdoor kitchens year-round assets. Mediterranean-style planting suits the Hawke's Bay climate well.",
    "new-plymouth":     "New Plymouth's stunning coastal parks and the backdrop of Mt Taranaki inspire high landscaping standards in residential properties. The city's mild, wet climate grows lush gardens quickly — regular maintenance is important.",
    "palmerston-north": "Palmerston North's wide suburban sections offer good space for garden projects. The Manawatu's windy conditions mean shelter belts and wind-hardy planting are important design considerations.",
    "nelson":           "Nelson's exceptional sunshine and fertile Tasman soils make it one of NZ's best gardening environments. Mediterranean plants, citrus, and edible gardens thrive — landscapers in Nelson often incorporate food production into residential designs.",
    "rotorua":          "Rotorua's volcanic soils are rich and fast-draining — excellent for plant growth. The geothermal environment does mean some areas have soil chemistry that affects plant selection. The lakeside and tourism aesthetic drives premium landscaping in many Rotorua properties.",
}

def landscaper_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    local = LANDSCAPER_DATA[city_key]

    return f"""---
title: "Landscapers {city} 2026 — Garden Design, Landscaping Costs and What to Expect"
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
| Hourly rate (labourer) | $48–$88/hr |
| Hourly rate (qualified landscaper) | $78–$148/hr |
| Garden design (small section) | $750–$2,400 |
| Full garden makeover (small-medium) | $9,000–$33,000 |
| Lawn installation (turf, per m²) | $23–$58/m² |
| Retaining wall — timber sleeper (per m²) | $380–$880/m² |
| Retaining wall — concrete block (per m²) | $580–$1,380/m² |
| Paving / outdoor tiles (per m², installed) | $95–$290/m² |
| Planting package (mixed shrubs, per m²) | $75–$195/m² |
| Irrigation system (small section) | $1,900–$5,800 |
| Tree removal (small-medium) | $480–$1,900 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Getting a Good Result in {city}

- Always get a written design plan before work begins
- Confirm what's included: plants, irrigation, consent for retaining walls
- Retaining walls over 1.5m typically need building consent — check with {region} Council
- Ask for a portfolio of recent local {city} work
- Look for members of Landscaping New Zealand (LNZ)

**Find {city} landscapers:** [Landscapers {city}](/trades/landscapers/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Landscaping Cost NZ](/articles/landscaping-cost-nz/) | [Retaining Wall Cost NZ](/articles/retaining-wall-cost-nz/) | [Garden Design Cost NZ](/articles/garden-design-cost-nz/)*
"""


# ── Glazier ───────────────────────────────────────────────────────────────────

GLAZIER_DATA = {
    "auckland":     ("$180–$400", "$350–$900", "$800–$2,500", "Auckland's large housing stock and high rates of villa renovation drive strong glazing demand. Double glazing retrofits are increasingly popular as homeowners improve thermal performance."),
    "wellington":   ("$180–$400", "$380–$950", "$850–$2,600", "Wellington's cold, windy winters make double glazing one of the highest-ROI home upgrades. The city's older villas typically have single-glazed sash windows that are expensive to heat around."),
    "christchurch": ("$160–$360", "$320–$850", "$750–$2,300", "Post-earthquake Christchurch required extensive glazing work. Many Christchurch homes upgraded to double glazing during insurance-funded repairs, raising the standard across the city."),
    "hamilton":     ("$150–$340", "$300–$800", "$700–$2,200", "Hamilton's warm summers and cool winters make double glazing worth the investment. New builds in Hamilton subdivisions now commonly specify double glazing as standard."),
    "tauranga":     ("$155–$345", "$310–$820", "$720–$2,250", "Tauranga's coastal lifestyle means large glazed areas to capture the views. Low-E double glazing reduces solar heat gain in summer while retaining warmth in winter."),
    "dunedin":      ("$145–$330", "$290–$780", "$680–$2,100", "Dunedin's cold winters make glazing upgrades particularly impactful. Single-glazed older homes lose enormous amounts of heat through windows — double glazing can cut heat loss by 50%."),
}

def glazier_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    callout, repair, window, local = GLAZIER_DATA[city_key]

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
| Call-out fee (broken glass, standard hours) | {callout} |
| Emergency glass replacement (after hours) | $300–$700 |
| Single glaze repair / replacement (per pane) | {repair} |
| Double glazing replacement (per pane) | $450–$1,200 |
| Window replacement — aluminium (per window) | {window} |
| Window replacement — uPVC (per window) | $1,000–$3,000 |
| Double glazing retrofit (per window) | $800–$2,500 |
| Sliding door glass replacement | $500–$1,800 |
| Splashback glass (per m²) | $250–$600/m² |
| Shower screen supply and fit | $800–$2,500 |
| Glass balustrade (per m linear) | $400–$1,000/m |
| Mirror supply and fit | $300–$900 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Glazing Market

{local}

## Safety Glass Requirements in NZ

NZ Building Code requires safety glass (toughened or laminated) in specific locations:

- **Within 500mm of a door:** Any glazing beside or in a door
- **Low-level glazing:** Below 1,050mm in most situations
- **Wet areas:** Shower screens and bathroom glazing
- **Stairways and balustrades:** All glass in these locations

If you're replacing glass, confirm the replacement meets current code requirements — especially in older homes where original glazing may not have been compliant.

## Double Glazing in {city}

Upgrading from single to double glazing is one of the best thermal improvements for a {city} home:

- Reduces heat loss through windows by ~50%
- Reduces condensation on the glass interior
- Improves acoustic insulation from street noise
- Typically pays back through energy savings in 8–15 years

**Retrofit double glazing:** Secondary glazing units can be fitted into existing aluminium frames in many cases — cheaper than full window replacement. Cost: $400–$900 per window.

**Find {city} glaziers:** [Glaziers {city}](/trades/glaziers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does window glass replacement cost in {city}?**
Single glaze repair: {repair}. Full window replacement (aluminium): {window}.

**What is safety glass and do I need it?**
Toughened or laminated glass required near doors, in wet areas, and at low levels. NZ Building Code specifies where — your glazier will advise.

**Is double glazing worth it in {city}?**
Yes for most {city} homes — reduces heat loss, condensation, and noise. Payback typically 8–15 years through energy savings.

---

*Related: [Window Replacement Cost NZ](/articles/window-replacement-cost-nz/) | [Double Glazing Cost NZ](/articles/double-glazing-cost-nz/) | [Insulation Installers {city}](/articles/insulation-installer-{city_key}-nz/)*
"""


# ── Kitchen Renovator ─────────────────────────────────────────────────────────

KITCHEN_DATA = {
    "auckland":     ("$25,000–$60,000", "$12,000–$25,000", "$60,000–$150,000+", "Auckland has NZ's most active kitchen renovation market. High property values make kitchen upgrades a strong investment — a quality kitchen renovation can add significantly more than its cost to Auckland property values."),
    "wellington":   ("$25,000–$60,000", "$12,000–$25,000", "$60,000–$150,000+", "Wellington homeowners often renovate kitchens in older villas and character homes, balancing heritage features with modern functionality. Open-plan kitchen-living is popular in Wellington's compact homes."),
    "christchurch": ("$22,000–$55,000", "$11,000–$22,000", "$55,000–$130,000+", "Post-earthquake Christchurch saw many kitchen renovations as part of insurance-funded repairs. The city's newer housing stock also drives new kitchen installations in spec builds."),
    "hamilton":     ("$20,000–$50,000", "$10,000–$20,000", "$50,000–$120,000+", "Hamilton's active renovation market and affordable entry-level housing drive kitchen upgrades. Many 1970s–90s homes have dated kitchens that are first on the renovation list."),
    "tauranga":     ("$22,000–$55,000", "$11,000–$22,000", "$55,000–$130,000+", "Tauranga's lifestyle-focused homeowners place high value on kitchen quality. Open-plan living and outdoor entertaining connections are popular in Bay of Plenty renovations."),
    "dunedin":      ("$18,000–$45,000", "$9,000–$18,000", "$45,000–$110,000+", "Dunedin's renovation market is strong among homeowners upgrading older Victorian and Edwardian homes. Budget-conscious renovations using flat-pack cabinetry are common in the student and investor rental market."),
}

def kitchen_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    mid, budget, premium, local = KITCHEN_DATA[city_key]

    return f"""---
title: "Kitchen Renovation {city} 2026 — Costs, What's Included and How to Plan"
description: "Kitchen renovation {city} 2026 — {city} kitchen renovation costs, budget vs mid-range vs premium, what's included, tradespeople needed, and how to find reliable kitchen renovators near you."
image: "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["kitchen renovation {city}", "kitchen renovator {city}", "kitchen cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

A kitchen renovation is typically the highest-value home improvement you can make in {city}. Here's what it costs in 2026 and how to plan your project.

## {city} Kitchen Renovation Costs 2026

| Kitchen type | {city} typical cost (complete) |
|---|---|
| Budget refresh (flat-pack, DIY install) | $5,000–$12,000 |
| Budget renovation (flat-pack, installed) | {budget} |
| Mid-range renovation (semi-custom) | {mid} |
| Premium renovation (custom cabinetry) | {premium} |

### What's Typically Included

| Cost component | Budget | Mid-range | Premium |
|---|---|---|---|
| Cabinetry | Flat-pack | Semi-custom | Custom made |
| Benchtop | Laminate | Stone/engineered | Stone/marble |
| Splashback | Tiles | Glass/tiles | Custom glass/stone |
| Appliances | Entry-level | Mid-range brands | Premium brands |
| Sink and taps | Basic | Mid-range | Designer |
| Lighting | Standard | LED downlights | Feature/designer |
| Flooring | Vinyl | Timber/tile | Timber/stone |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Kitchen Renovation Market

{local}

## Tradespeople You'll Need

A kitchen renovation typically involves multiple trades:

- **Builder / kitchen installer:** Project management, demolition, cabinetry installation, structural work
- **Plumber:** Sink connections, dishwasher connection, relocating plumbing if layout changes
- **Electrician:** Oven circuit, rangehood wiring, additional power points, lighting
- **Tiler:** Splashback and floor tiles
- **Plasterer:** Making good walls after demolition
- **Painter:** Finishing walls and ceiling

A good builder or kitchen company will coordinate all trades. Alternatively, you manage each trade yourself to save the coordination margin (but takes significantly more time).

## Planning Your {city} Kitchen Renovation

**Layout first:** The most expensive change is moving plumbing or structural walls. If you can work within the existing footprint, costs are much lower.

**Budget allocation guide:**
- Cabinetry: 35–45% of budget
- Benchtop: 10–20%
- Appliances: 10–20%
- Labour (all trades): 25–35%
- Splashback, sink, taps: 5–10%

**Consents:** Moving walls (structural) requires building consent. Moving plumbing requires a licensed plumber and compliance certificate. Pure cosmetic renovation (same layout) usually doesn't need consent.

**Timeline:** A standard kitchen renovation takes 3–6 weeks from demolition to completion. Custom cabinetry lead times add 4–8 weeks.

**Find {city} kitchen renovators:** [Kitchen Renovators {city}](/trades/kitchen-renovators/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a kitchen renovation cost in {city}?**
Budget (flat-pack, installed): {budget}. Mid-range (semi-custom): {mid}. Premium (custom): {premium}.

**How long does a kitchen renovation take in {city}?**
3–6 weeks from demolition to completion for a standard renovation. Custom cabinetry adds 4–8 weeks lead time before installation begins.

**Do I need building consent for a kitchen renovation in {city}?**
Not usually for a like-for-like renovation in the same footprint. Removing walls, moving plumbing, or adding new electrical circuits may require consent or compliance certificates — your builder will advise.

**What adds the most value to a kitchen renovation?**
Quality cabinetry, a stone benchtop, and good lighting make the biggest visual impact. Avoid over-capitalising for your suburb — check recent sales of renovated properties nearby.

---

*Related: [Kitchen Renovation Cost NZ](/articles/kitchen-renovation-cost-nz/) | [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/) | [Builder Pricing Guide NZ](/articles/builder-pricing-guide-nz-2026/)*
"""


# ── Floor Sander ──────────────────────────────────────────────────────────────

FLOORSAND_RATES = {
    "auckland":     ("$35–$65/m²", "$25–$50/m²", "$2,500–$6,000"),
    "wellington":   ("$35–$65/m²", "$25–$50/m²", "$2,500–$6,000"),
    "christchurch": ("$30–$58/m²", "$22–$45/m²", "$2,200–$5,500"),
    "hamilton":     ("$28–$55/m²", "$20–$42/m²", "$2,000–$5,000"),
    "tauranga":     ("$30–$58/m²", "$22–$45/m²", "$2,200–$5,500"),
    "dunedin":      ("$27–$52/m²", "$19–$40/m²", "$1,900–$4,800"),
}

def floorsand_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    sand_finish, sand_only, full_home = FLOORSAND_RATES[city_key]

    local_map = {
        "auckland":     "Auckland's villa and bungalow heritage means large quantities of native timber floors — rimu, kauri, matai, and heart macrocarpa — that respond beautifully to sanding and finishing. Floor sanding in Auckland is one of the best-value home improvements.",
        "wellington":   "Wellington's large stock of wooden villas contains some of NZ's finest native timber floors. Rimu and kauri floors sanded and refinished can transform a room — and add significant value to Wellington's character homes.",
        "christchurch": "Pre-earthquake Christchurch homes that survived often have original native timber floors. Post-earthquake rebuilds sometimes include engineered timber that can also be sanded. Christchurch's floor sanding market covers both heritage and modern flooring.",
        "hamilton":     "Hamilton's older housing stock — particularly 1940s–70s homes — has native timber floors that have often been covered with carpet for decades. Revealing and refinishing these floors is a popular renovation in Hamilton.",
        "tauranga":     "Tauranga's mix of older character homes and newer builds creates demand for both heritage floor restoration and engineered timber finishing. The lifestyle market values quality timber floors highly.",
        "dunedin":      "Dunedin's Victorian and Edwardian homes contain some of NZ's oldest and finest timber floors — rimu and matai in excellent condition beneath decades of carpet. Floor restoration is a Dunedin renovation speciality.",
    }
    local = local_map.get(city_key, f"{city} has good demand for floor sanding and finishing across both heritage timber and engineered floors.")

    return f"""---
title: "Floor Sanders {city} 2026 — Timber Floor Sanding Costs and What to Expect"
description: "Floor sanders {city} 2026 — {city} floor sanding cost, timber floor finishing prices, staining rates, what floors can be sanded, and how to find a reliable floor sander near you."
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
| Sand and finish (per m², 3 coats polyurethane) | {sand_finish} |
| Sand only / preparation (per m²) | {sand_only} |
| Full home floor sanding (3-bed, ~80m²) | {full_home} |
| Single room (20m²) | $700–$1,800 |
| Staining (per m², colour stain + finish) | $40–$75/m² |
| Gap filling (per m²) | $8–$20/m² |
| Floor board replacement (per board) | $80–$200 per board |
| Polishing (existing finish, buff and recoat) | $15–$30/m² |
| Deck sanding and oiling (per m²) | $20–$45/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Floor Sanding Market

{local}

## Can My Floor Be Sanded?

**Native timber (rimu, kauri, matai, heart pine):** Usually excellent candidates — thick boards that can be sanded multiple times over their lifetime.

**Engineered timber:** Can be sanded 1–3 times depending on the wear layer thickness (typically 3–6mm). Check the manufacturer specification.

**Bamboo:** Some bamboo floors can be sanded — depends on the product. Ask a professional to assess.

**Parquet:** Intricate parquet blocks can be sanded but require specialist care.

**Cannot be sanded:** Laminate flooring, most vinyl, and floors with less than 2–3mm of wood above the tongue.

## Finish Options

**Polyurethane (oil-based):** Hard-wearing, amber tone, traditional look. 2–3 coats required. Dry time 24–48 hours per coat.

**Water-based polyurethane:** Clearer finish (less amber tone), faster drying, lower odour. More expensive but popular for light-coloured timber.

**Hardwax oil:** Natural look, penetrating finish. Easier spot repairs than surface finishes but requires more maintenance.

**Staining:** Apply a colour stain before the topcoat to change the floor tone. Popular for darkening lighter timber or creating a modern grey/charcoal look.

**Find {city} floor sanders:** [Floor Sanders {city}](/trades/floor-sanding/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does floor sanding cost in {city}?**
Sand and finish (3 coats polyurethane): {sand_finish}/m². Full 3-bed home (~80m²): {full_home}.

**How long does floor sanding take?**
A standard 3-bed home: 2–3 days (sanding + 3 coats of finish with drying time). The home needs to be vacated during sanding (dust) and for 24–48 hours after the final coat.

**How often can I sand my floor?**
Native timber floors can be sanded many times over their life — often 5–8 times or more. The limiting factor is the depth of wood above the tongue groove. Your sander can assess how much material remains.

---

*Related: [Floor Sanding Cost NZ](/articles/floor-sanding-cost-nz/) | [Timber Flooring Cost NZ](/articles/timber-flooring-cost-nz/) | [Carpet Layer {city}](/articles/carpet-layer-{city_key}-nz/)*
"""


# ── Article list ───────────────────────────────────────────────────────────────

ARTICLES = [
    # Gasfitter gap fills
    ("gasfitter-dunedin-nz",           lambda: gasfitter_article("dunedin")),
    ("gasfitter-napier-nz",            lambda: gasfitter_article("napier")),
    ("gasfitter-new-plymouth-nz",      lambda: gasfitter_article("new-plymouth")),
    ("gasfitter-palmerston-north-nz",  lambda: gasfitter_article("palmerston-north")),
    ("gasfitter-nelson-nz",            lambda: gasfitter_article("nelson")),
    ("gasfitter-rotorua-nz",           lambda: gasfitter_article("rotorua")),
    # Concreter gap fills
    ("concreter-napier-nz",            lambda: concreter_article("napier")),
    ("concreter-new-plymouth-nz",      lambda: concreter_article("new-plymouth")),
    ("concreter-palmerston-north-nz",  lambda: concreter_article("palmerston-north")),
    ("concreter-nelson-nz",            lambda: concreter_article("nelson")),
    ("concreter-rotorua-nz",           lambda: concreter_article("rotorua")),
    # Drainlayer gap fills
    ("drainlayer-napier-nz",           lambda: drainlayer_article("napier")),
    ("drainlayer-new-plymouth-nz",     lambda: drainlayer_article("new-plymouth")),
    ("drainlayer-palmerston-north-nz", lambda: drainlayer_article("palmerston-north")),
    ("drainlayer-nelson-nz",           lambda: drainlayer_article("nelson")),
    ("drainlayer-rotorua-nz",          lambda: drainlayer_article("rotorua")),
    # Landscaper gap fills
    ("landscaper-napier-nz",           lambda: landscaper_article("napier")),
    ("landscaper-new-plymouth-nz",     lambda: landscaper_article("new-plymouth")),
    ("landscaper-palmerston-north-nz", lambda: landscaper_article("palmerston-north")),
    ("landscaper-nelson-nz",           lambda: landscaper_article("nelson")),
    ("landscaper-rotorua-nz",          lambda: landscaper_article("rotorua")),
    # Glaziers — main cities
    ("glazier-auckland-nz",            lambda: glazier_article("auckland")),
    ("glazier-wellington-nz",          lambda: glazier_article("wellington")),
    ("glazier-christchurch-nz",        lambda: glazier_article("christchurch")),
    ("glazier-hamilton-nz",            lambda: glazier_article("hamilton")),
    ("glazier-tauranga-nz",            lambda: glazier_article("tauranga")),
    ("glazier-dunedin-nz",             lambda: glazier_article("dunedin")),
    # Kitchen renovators — main cities
    ("kitchen-renovator-auckland-nz",      lambda: kitchen_article("auckland")),
    ("kitchen-renovator-wellington-nz",    lambda: kitchen_article("wellington")),
    ("kitchen-renovator-christchurch-nz",  lambda: kitchen_article("christchurch")),
    ("kitchen-renovator-hamilton-nz",      lambda: kitchen_article("hamilton")),
    ("kitchen-renovator-tauranga-nz",      lambda: kitchen_article("tauranga")),
    ("kitchen-renovator-dunedin-nz",       lambda: kitchen_article("dunedin")),
    # Floor sanders — main cities
    ("floor-sander-auckland-nz",       lambda: floorsand_article("auckland")),
    ("floor-sander-wellington-nz",     lambda: floorsand_article("wellington")),
    ("floor-sander-christchurch-nz",   lambda: floorsand_article("christchurch")),
    ("floor-sander-hamilton-nz",       lambda: floorsand_article("hamilton")),
    ("floor-sander-tauranga-nz",       lambda: floorsand_article("tauranga")),
    ("floor-sander-dunedin-nz",        lambda: floorsand_article("dunedin")),
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
