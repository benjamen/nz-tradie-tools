#!/usr/bin/env python3
"""
Wave 2 SEO content generator — TradieTools NZ
Generates suburb × trade articles for missing combinations.
Run: python3 generate_wave2.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

# ── City data ─────────────────────────────────────────────────────────────────

CITIES = {
    "hamilton": {
        "name": "Hamilton",
        "region": "Waikato",
        "region_adj": "Waikato",
        "rate_note": "Hamilton rates are typically 10–15% below Auckland but on par with other major NZ cities.",
        "context": "Hamilton is Waikato's largest city and the country's fourth-largest urban area. Strong residential growth in suburbs like Rototuna, Rotokauri, and Flagstaff keeps tradespeople busy, while the surrounding dairy and agricultural sector drives demand for rural and semi-rural work.",
        "housing": "Much of Hamilton's housing stock was built in the 1960s–1990s, meaning older wiring, galvanised pipes, and roofs that are reaching end of life — renovation and replacement work is common.",
        "pop": "170,000",
        "image_keyword": "waikato",
    },
    "tauranga": {
        "name": "Tauranga",
        "region": "Bay of Plenty",
        "region_adj": "Bay of Plenty",
        "rate_note": "Tauranga rates are broadly similar to Hamilton, though strong demand from a growing population can push prices slightly higher for the best tradespeople.",
        "context": "Tauranga is one of New Zealand's fastest-growing cities. High coastal amenity, a large retiree population, and strong inward migration have fuelled a construction boom that keeps tradespeople in short supply. The Tauranga–Mt Maunganui area and growing suburbs like Pāpāmoa East and Te Tūmu generate substantial new-build and renovation work.",
        "housing": "Tauranga has a mix of older state housing in central areas and brand-new developments on the coastal fringe. Coastal salt air can accelerate corrosion on roofing, gutters, and exterior fittings.",
        "pop": "155,000",
        "image_keyword": "tauranga",
    },
    "dunedin": {
        "name": "Dunedin",
        "region": "Otago",
        "region_adj": "Otago",
        "rate_note": "Dunedin rates are 10–20% below Auckland and reflect the smaller, less pressured market in the South Island's university city.",
        "context": "Dunedin is home to the University of Otago and a large student population, which drives demand for residential maintenance on rental properties. The city has a rich stock of Victorian and Edwardian character homes — a source of both charm and maintenance complexity.",
        "housing": "Older Dunedin homes often have original wiring, lead or galvanised water pipes, single-skin plaster walls, and roofing materials that pre-date modern standards. Renovation and modernisation work is common, and tradespeople with heritage experience are valued.",
        "pop": "130,000",
        "image_keyword": "dunedin",
    },
    "napier": {
        "name": "Napier",
        "region": "Hawke's Bay",
        "region_adj": "Hawke's Bay",
        "rate_note": "Napier rates are broadly in line with regional NZ — lower than Auckland and Wellington but comparable to Hamilton and Tauranga.",
        "context": "Napier is Hawke's Bay's commercial hub, rebuilt in art deco style after the devastating 1931 earthquake. The city has a mix of older character homes and post-war residential areas, with steady demand from homeowners and the region's thriving wine and horticulture industry.",
        "housing": "Post-1931 art deco homes are a Napier signature — beautiful but sometimes requiring specialist attention for heritage materials. Post-war and 1960s–80s housing forms the bulk of the residential market.",
        "pop": "65,000",
        "image_keyword": "hawkes-bay",
    },
    "new-plymouth": {
        "name": "New Plymouth",
        "region": "Taranaki",
        "region_adj": "Taranaki",
        "rate_note": "New Plymouth rates are broadly regional — below Auckland and Wellington but competitive with other mid-sized NZ cities. The oil and gas sector can push industrial trade rates higher than the residential average.",
        "context": "New Plymouth is Taranaki's main city, backed by Mt Taranaki and a strong oil and gas industry. The Taranaki Energy Trust and industrial sector drive commercial and industrial trade work, while steady residential growth keeps domestic tradespeople busy.",
        "housing": "A mix of older bungalows and post-war homes in central areas, with newer subdivisions on the city's edges. Coastal proximity means salt air is a factor for roofing and exterior work.",
        "pop": "58,000",
        "image_keyword": "taranaki",
    },
    "christchurch": {
        "name": "Christchurch",
        "region": "Canterbury",
        "region_adj": "Canterbury",
        "rate_note": "Christchurch rates are broadly similar to Hamilton and Tauranga — below Auckland and Wellington. Post-earthquake rebuild activity has normalised but earthquake-strengthening work and insurance repairs continue.",
        "context": "Christchurch is the South Island's largest city. More than a decade after the 2010–2011 earthquakes, the rebuild is well advanced but insurance repairs, earthquake-strengthening, and new construction continue to keep tradespeople busy across the city.",
        "housing": "The post-earthquake rebuild means Christchurch has a large proportion of newer housing stock. Older homes that survived the earthquakes may have remediation history — important for any tradespeople doing structural or compliance work.",
        "pop": "400,000",
        "image_keyword": "christchurch",
    },
    "auckland": {
        "name": "Auckland",
        "region": "Auckland",
        "region_adj": "Auckland",
        "rate_note": "Auckland rates are 15–25% above the national average, reflecting higher wages, overheads, and demand across the region.",
        "context": "Auckland is New Zealand's largest city with over 1.7 million people. High construction demand, a constrained tradie workforce, and Auckland's sheer geographic size keep prices at a premium across all trades.",
        "housing": "Auckland has everything from 1900s villas in Ponsonby to 1970s brick-and-tile in the suburbs to brand-new townhouses in areas like Māngere East and Ōtāhuhu. Each era brings different maintenance needs.",
        "pop": "1,700,000",
        "image_keyword": "auckland",
    },
    "wellington": {
        "name": "Wellington",
        "region": "Wellington",
        "region_adj": "Wellington",
        "rate_note": "Wellington rates are broadly comparable to Auckland — driven by high cost of living, difficult terrain, and a competitive labour market.",
        "context": "Wellington is New Zealand's capital and a compact, hilly city. The geography makes access and parking challenging for tradespeople, and Wellington's exposure to wind and rain puts extra pressure on roofing, cladding, and drainage systems.",
        "housing": "Wellington has a high proportion of older wooden villas and character homes, particularly in suburbs like Mt Victoria, Newtown, and Karori. These require specialist knowledge and often more complex work than modern homes.",
        "pop": "215,000",
        "image_keyword": "wellington",
    },
}

# ── Trade data ─────────────────────────────────────────────────────────────────

def electrician_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    slug = f"electrician-{city_key}-nz"

    rates_note = c["rate_note"]
    context = c["context"]
    housing = c["housing"]

    if city_key == "hamilton":
        hourly = "$100–$170/hr"; callout = "$70–$160"; after_hours = "$200–$450"
        switchboard = "$1,200–$3,500"; ev = "$1,000–$2,200"; solar = "$1,200–$3,500"
        local_demand = "Hamilton's rapid residential growth and a busy construction pipeline mean electricians are in strong demand. Book at least 1–2 weeks ahead for non-urgent work."
        local_tip = "Hamilton is served by WEL Networks for lines infrastructure. Many Hamilton electricians specialise in both residential and rural/agricultural electrical work — useful if you have a lifestyle block nearby."
    elif city_key == "tauranga":
        hourly = "$105–$175/hr"; callout = "$75–$170"; after_hours = "$220–$480"
        switchboard = "$1,300–$3,800"; ev = "$1,100–$2,400"; solar = "$1,300–$3,800"
        local_demand = "Tauranga's construction boom and large retiree population drive strong demand. EV charger and solar installations are particularly popular given the city's high sunshine hours."
        local_tip = "Tauranga is served by PowerCo for lines. The high sunshine hours (2,300+/year) make solar particularly attractive — Tauranga electricians experienced in solar installation are in strong demand."
    elif city_key == "dunedin":
        hourly = "$90–$155/hr"; callout = "$60–$140"; after_hours = "$180–$400"
        switchboard = "$1,000–$3,000"; ev = "$950–$2,000"; solar = "$1,000–$3,000"
        local_demand = "Dunedin's large student rental market drives steady demand for electrical maintenance. The city's older housing stock means rewiring and switchboard upgrades are common."
        local_tip = "Dunedin is served by Aurora Energy for lines. The city's older housing stock — including many pre-1950 homes — means rewiring projects are common. Make sure your electrician has experience with older installations."
    elif city_key == "napier":
        hourly = "$95–$165/hr"; callout = "$65–$150"; after_hours = "$190–$420"
        switchboard = "$1,100–$3,200"; ev = "$1,000–$2,100"; solar = "$1,100–$3,200"
        local_demand = "Napier has steady residential demand with particular activity in home renovation and heritage property maintenance. Solar is growing due to Hawke's Bay's excellent sunshine."
        local_tip = "Napier/Hastings is served by Unison Networks for lines. Hawke's Bay gets over 2,200 sunshine hours per year — among the highest in NZ — making solar a strong investment."
    else:  # new-plymouth
        hourly = "$95–$165/hr"; callout = "$65–$150"; after_hours = "$195–$430"
        switchboard = "$1,100–$3,200"; ev = "$1,000–$2,100"; solar = "$1,100–$3,200"
        local_demand = "New Plymouth has active residential and commercial/industrial electrical demand. The oil and gas sector drives demand for industrial electricians, which can affect availability for residential work."
        local_tip = "New Plymouth is served by Powerco for lines. The presence of petrochemical and industrial facilities in Taranaki means some local electricians specialise in industrial work — for residential jobs, confirm they cover domestic work."

    return f"""---
title: "Electricians {city} 2026 — Hourly Rates, Call-Out Fees and Common Job Costs"
description: "Electricians {city} 2026 — {city} electrician hourly rates, call-out fees, common job costs, how to verify a licensed electrician, and how to find one near you."
image: "https://images.unsplash.com/photo-1621905252472-943afaa20e20?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["electricians {city}", "electrician {city}", "electrical cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what electricians charge in {city} in 2026 and how to find a reliable one.

## {city} Electrician Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (weekday, standard hours) | {callout} |
| Hourly rate (labour only) | {hourly} |
| After-hours / emergency call-out | {after_hours} + hourly |
| Power point installation (single GPO) | $130–$300 |
| Light fitting replacement | $90–$220 per fitting |
| Safety switch (RCD) installation | $180–$380 |
| Switchboard upgrade (full, 3-bed home) | {switchboard} |
| EV charger installation (7kW, home) | {ev} |
| Heat pump wiring (dedicated circuit) | $300–$600 |
| Smoke alarm installation (hardwired, per alarm) | $180–$400 |
| Solar panel system wiring (grid-tie) | {solar} |
| Underfloor heating wiring (per m²) | $45–$110/m² |

*All prices GST inclusive. {rates_note}*

## {city} Electrical Market

{local_demand}

{housing}

{local_tip}

## What Requires a Licensed Electrician in NZ

All "restricted electrical work" must be done by a person authorised under the Electricity Act 1992:

- Installing or modifying any wiring connected to mains power
- Installing power points, light switches, ceiling fans
- Switchboard work
- Installing any fixed electrical appliance (heat pump, hot water cylinder, EV charger)
- Testing and certifying electrical installations

**Certificate of Compliance (COC):** Every job involving restricted electrical work must be certified with a COC. Insist on receiving one — it's required by law and essential for home insurance.

## Verifying a {city} Electrician

All NZ electricians must be registered under the Electricity (Safety) Regulations 2010. Verify at [ewrb.govt.nz](https://www.ewrb.govt.nz) — search by name or company.

**Ask before hiring:**
1. Are you EWRB registered — can I have your licence number?
2. Will I receive a Certificate of Compliance?
3. What is your call-out fee and hourly rate?
4. Do you cover my suburb in {city}?
5. What is your lead time for non-urgent work?

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does an electrician cost in {city}?**
Call-out fee: {callout}. Hourly rate: {hourly}. A simple job (single power point): $130–$300 total. {rates_note}

**How do I check if a {city} electrician is licensed?**
Search the EWRB register at ewrb.govt.nz — enter the electrician's name or company to verify their registration status.

**Do I need a Certificate of Compliance for electrical work in {city}?**
Yes — for all restricted electrical work. It's legally required, protects your insurance, and is important when selling your home.

**How much does EV charger installation cost in {city}?**
{ev} for a standard 7kW home EV charger including dedicated circuit and COC. Add $500–$1,500 if the switchboard needs upgrading.

---

*Related: [Electrician Cost NZ](/articles/electrician-cost-nz/) | [Heat Pump Installation Cost NZ](/articles/heat-pump-installation-cost-nz/) | [Solar Panel Cost NZ](/articles/solar-panel-cost-nz/)*
"""


def plumber_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    slug = f"plumber-{city_key}-nz"
    context = c["context"]
    housing = c["housing"]
    rates_note = c["rate_note"]

    if city_key == "tauranga":
        hourly = "$110–$180/hr"; callout = "$80–$170"; after_hours = "$220–$500"
        local = "Tauranga's growth drives strong demand for plumbing in new builds. The coastal environment means salt-related corrosion can affect older copper pipes and hot water cylinders — check these if buying an older Tauranga home."
    elif city_key == "dunedin":
        hourly = "$90–$155/hr"; callout = "$65–$140"; after_hours = "$180–$400"
        local = "Dunedin's older housing stock includes many homes with original galvanised steel pipes — these corrode over time and are a common reason for replumbing. The colder Dunedin winters also mean more burst pipe callouts in frosty months."
    elif city_key == "napier":
        hourly = "$95–$165/hr"; callout = "$70–$150"; after_hours = "$190–$420"
        local = "Napier plumbers cover both residential and some rural/horticultural work in the Hawke's Bay region. Post-earthquake pipe assessment is part of many older Napier homes' history."
    else:  # new-plymouth
        hourly = "$95–$165/hr"; callout = "$70–$150"; after_hours = "$195–$430"
        local = "New Plymouth plumbers handle a mix of residential and commercial work. The oil and gas sector also drives demand for industrial plumbing and gasfitting, which can affect tradesperson availability for domestic jobs."

    return f"""---
title: "Plumbers {city} 2026 — Hourly Rates, Call-Out Fees and Common Job Costs"
description: "Plumbers {city} 2026 — {city} plumber hourly rates, call-out fees, hot water cylinder costs, drain unblocking prices, and how to find a reliable plumber near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["plumbers {city}", "plumber {city}", "plumbing cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what plumbers charge in {city} in 2026 and how to find a reliable one.

## {city} Plumber Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (weekday, standard hours) | {callout} |
| Hourly rate (labour only) | {hourly} |
| After-hours / emergency call-out | {after_hours} + hourly |
| Blocked drain (standard) | $150–$350 |
| Toilet replacement | $400–$900 |
| Tap replacement (bathroom/kitchen) | $150–$350 per tap |
| Hot water cylinder replacement (180L) | $1,800–$3,500 installed |
| Heat pump hot water system | $3,500–$6,000 installed |
| Bathroom renovation (plumbing only) | $2,500–$6,000+ |
| Leak detection | $200–$500 |
| Drain camera inspection | $250–$500 |
| Burst pipe repair | $300–$800 |

*All prices GST inclusive. {rates_note}*

## {city} Plumbing Market

{local}

{housing}

## What Requires a Licensed Plumber in NZ

In NZ, "sanitary plumbing" and "drainlaying" are restricted trades. Licensed plumbers must be registered with the Plumbers, Gasfitters and Drainlayers Board (PGDB).

Licensed work includes:
- Installing or modifying water supply, drainage, or sanitary systems
- Hot water cylinder installation and replacement
- Bathroom and kitchen plumbing fit-out
- Any work connecting to the public sewer

**Verify your plumber:** Check registration at [pgdb.co.nz](https://www.pgdb.co.nz). Every completed job should result in a compliance certificate.

## Common {city} Plumbing Jobs

### Hot Water Cylinder Replacement
The most common major plumbing job for homeowners. Standard 180L mains-pressure electric cylinders cost $1,800–$3,500 installed. Heat pump hot water systems are increasingly popular for energy efficiency ($3,500–$6,000 installed).

### Blocked Drains
Tree roots, grease, and debris cause most drain blockages. A standard drain unblock (high-pressure water jetting) costs $150–$350. A camera inspection ($250–$500) identifies recurring root problems.

### Bathroom Renovations
Plumbing-only costs for a bathroom renovation (moving fixtures, new waste, supply connections) typically run $2,500–$6,000. Full bathroom reno including tiles and fittings: $15,000–$35,000+.

## Finding a Reliable {city} Plumber

**Ask before hiring:**
1. Are you PGDB registered — can I have your licence number?
2. Will I receive a compliance certificate?
3. What is your call-out fee and hourly rate?
4. Do you cover my suburb in {city}?

**Find {city} plumbers:** [Plumbers {city}](/trades/plumbers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a plumber cost in {city}?**
Call-out: {callout}. Hourly: {hourly}. Blocked drain: $150–$350. Hot water cylinder (replace): $1,800–$3,500 installed.

**How do I find a licensed plumber in {city}?**
Check registration at pgdb.co.nz. Licensed plumbers must display their licence number on quotes and invoices.

**How much does a hot water cylinder replacement cost in {city}?**
$1,800–$3,500 for a standard 180L mains-pressure electric cylinder, installed. Heat pump hot water: $3,500–$6,000 installed but saves 60–75% on water heating energy.

---

*Related: [Blocked Drain Cost NZ](/articles/blocked-drain-cost-nz/) | [Hot Water Cylinder Cost NZ](/articles/hot-water-cylinder-cost-nz/) | [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/)*
"""


def builder_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    housing = c["housing"]
    rates_note = c["rate_note"]

    if city_key == "hamilton":
        hourly = "$85–$160/hr"; m2_rate = "$2,500–$4,500/m²"
        local = "Hamilton's strong population growth has created a busy new-build market, particularly in northern and western growth corridors. Renovation and extension work is also strong as homeowners improve older housing stock rather than move."
    elif city_key == "tauranga":
        hourly = "$90–$165/hr"; m2_rate = "$2,800–$4,800/m²"
        local = "Tauranga's construction boom is one of the most active in NZ. New builds are strong in Pāpāmoa, Te Tūmu, and Ōmokoroa, while renovation work is common in established suburbs like Mt Maunganui and Papamoa Beach."
    elif city_key == "dunedin":
        hourly = "$80–$150/hr"; m2_rate = "$2,400–$4,200/m²"
        local = "Dunedin's builder market is steadier than the main centres. Character home renovations are a Dunedin specialty — working with older materials and heritage features requires experience. The student rental market also drives demand for maintenance and fit-out work."
    else:
        hourly = "$85–$160/hr"; m2_rate = "$2,500–$4,500/m²"
        local = f"{city} has steady construction demand across residential new builds, extensions, and renovation work."

    return f"""---
title: "Builders {city} 2026 — Hourly Rates, New Build Costs and What to Expect"
description: "Builders {city} 2026 — {city} builder hourly rates, new build cost per m², how to get quotes, LBP licensing explained, and how to find a reliable builder near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["builders {city}", "builder {city}", "building cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what builders charge in {city} in 2026 and how to find a reliable one.

## {city} Builder Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate (residential builder) | {hourly} |
| New build cost (per m², turnkey) | {m2_rate} |
| House extension (per m²) | $3,000–$5,500/m² |
| Deck build (basic, 20m²) | $8,000–$18,000 |
| Deck build (composite/hardwood, 20m²) | $15,000–$35,000 |
| Garage build (double, standard) | $35,000–$70,000 |
| Kitchen renovation (builder work only) | $5,000–$20,000 |
| Bathroom renovation (builder work only) | $8,000–$25,000 |
| Carport (steel, freestanding) | $8,000–$18,000 |
| Pergola build | $5,000–$20,000 |
| Weatherboard replacement (per m²) | $150–$350/m² |

*All prices GST inclusive. {rates_note}*

## {city} Building Market

{local}

{housing}

## LBP Licensing — What You Need to Know

All "restricted building work" in NZ must be done by a Licensed Building Practitioner (LBP) or under LBP supervision. This covers:

- Structural work (foundations, framing, load-bearing walls)
- Weathertightness work (cladding, roofing, windows)
- Foundation and drainage work

**Verify LBP:** Search at [lbp.govt.nz](https://www.lbp.govt.nz) by name or licence number.

**Record of Work:** Your LBP builder must provide a Record of Work on completion — keep this with your property file.

## Getting Good Quotes in {city}

- Get 3 quotes minimum for any job over $10,000
- Ensure quotes are written and itemised
- Confirm what's included: consents, materials, subcontractors
- Check the builder holds public liability insurance
- Ask for references from recent {city} jobs

**Find {city} builders:** [Builders {city}](/trades/builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a builder cost in {city}?**
Hourly rate: {hourly}. New build: {m2_rate} turnkey. Extensions typically cost more per m² than new builds due to tie-in complexity.

**How do I check if a {city} builder is licensed?**
Search the LBP register at lbp.govt.nz. For restricted building work, your builder must be an LBP — ask for their licence class and number.

**Do I need building consent in {city}?**
Most structural work, new builds, and significant renovations require building consent from the {region} Council. Your builder should advise — never skip consent to save money.

---

*Related: [Builder Cost NZ](/articles/builder-pricing-guide-nz-2026/) | [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Home Extension Cost NZ](/articles/home-extension-cost-nz/)*
"""


def roofer_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    if city_key == "hamilton":
        local = "Hamilton's mix of 1960s–80s housing means many roofs are approaching or past their design life. Concrete tile and corrugated iron are the most common roofing types. Moss and lichen growth is common in the Waikato's humid climate."
    elif city_key == "tauranga":
        local = "Tauranga's coastal environment accelerates roof deterioration. Salt air corrodes metal fixings and flashings faster than inland locations. Regular inspections are especially important within 2–3km of the coast."
    elif city_key == "dunedin":
        local = "Dunedin's weather — rain, wind, and occasional snow on the Port Hills — is tough on roofs. Many older Dunedin homes have corrugated iron or slate tiles, both of which require specialist repair knowledge."
    elif city_key == "napier":
        local = "Napier's coastal location and Hawke's Bay's warm summers mean roofs need to handle both UV exposure and salt-laden winds. Post-earthquake Napier homes may have had roof work done during repairs — check the history."
    else:  # new-plymouth
        local = "New Plymouth's Taranaki location exposes roofs to prevailing westerly weather off the Tasman Sea. Wind and rain are the primary weathering factors — flashing integrity is critical."

    return f"""---
title: "Roofers {city} 2026 — Roof Replacement Costs, Repair Prices and What to Expect"
description: "Roofers {city} 2026 — {city} roof replacement cost, repair prices, iron vs tile vs membrane, how to get quotes, and how to find a reliable roofer near you."
image: "https://images.unsplash.com/photo-1632207691143-643e2a9a9361?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["roofers {city}", "roofer {city}", "roof replacement {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what roofers charge in {city} in 2026 and how to find a reliable one.

## {city} Roofing Rates 2026

| Service | {city} typical cost |
|---|---|
| Roof inspection | $150–$400 |
| Minor repair (single area) | $300–$800 |
| Flashing replacement (per metre) | $80–$200/m |
| Re-roofing — corrugated iron (per m²) | $80–$150/m² |
| Re-roofing — long-run steel (per m²) | $90–$170/m² |
| Re-roofing — concrete tile (per m²) | $100–$180/m² |
| Full roof replacement (100m² home) | $12,000–$30,000 |
| Gutter replacement (per metre) | $60–$150/m |
| Roof painting / treatment | $3,000–$8,000 |
| Skylight installation | $1,500–$4,000 |
| Moss and lichen treatment | $500–$2,000 |

*All prices GST inclusive. {rates_note}*

## {city} Roofing Market

{local}

## Roofing Materials in NZ

**Corrugated and long-run steel:** The most common NZ roofing material. Modern Colorsteel (ZINCALUME or COLORBOND-equivalent) has a 15–50 year lifespan depending on coating and environment. Coastal locations require the highest-grade coatings.

**Concrete tile:** Heavy but durable. Common on 1970s–90s homes. Individual cracked or slipped tiles can be replaced. Full recladding typically required when the sarking or underlay fails.

**Butyl / TPO membrane:** Used on low-pitch or flat roofs. Lifespan 20–30 years. Repairs require specialist membrane roofers.

**Slate:** Found on older homes. Expensive to repair (matching slate is scarce) but very long-lasting if individual slates are maintained.

## Getting Quotes for {city} Roofing

- Get at least 2–3 written quotes for any work over $5,000
- Ask for the specific product and warranty (manufacturer's warranty on steel is typically 15–50 years)
- Confirm scaffolding is included (required by law for most roof work)
- Check the roofer carries public liability and is a member of the Roofing Association of NZ (RANZ)

**Find {city} roofers:** [Roofers {city}](/trades/roofers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a roof replacement cost in {city}?**
Full replacement on a 100m² home: $12,000–$30,000 depending on material and pitch. Corrugated iron: $80–$150/m². Long-run steel: $90–$170/m².

**How do I know if my roof needs replacing in {city}?**
Signs: visible rust or corrosion on metal roofs, cracked or slipping tiles, staining on interior ceilings, moss buildup not responding to treatment, flashings lifting or cracking. A professional inspection ($150–$400) gives a clear picture.

**Does roofing work need building consent in {city}?**
Like-for-like re-roofing generally doesn't require consent. Changing the roofing material, pitch, or adding skylights typically does. Your roofer should advise.

---

*Related: [Roof Replacement Cost NZ](/articles/roof-replacement-cost-nz/) | [Roof Painting Cost NZ](/articles/roof-painting-cost-nz/) | [Guttering Replacement Cost NZ](/articles/guttering-replacement-cost-nz/)*
"""


def tiler_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    if city_key == "hamilton":
        local = "Hamilton's active renovation market keeps tilers busy year-round. Bathroom renovations and kitchen splashbacks are the most common residential tiling jobs."
    elif city_key == "tauranga":
        local = "Tauranga's strong renovation and new-build market drives good demand for tilers. Coastal homes often choose larger-format porcelain tiles for outdoor entertaining areas due to salt air durability."
    elif city_key == "dunedin":
        local = "Dunedin tilers frequently work on bathroom renovations in older homes and student rental properties. Heated tile floors are popular given Dunedin's cold winters."
    else:
        local = f"{city} has steady residential demand for tiling across bathrooms, kitchens, and outdoor areas."

    return f"""---
title: "Tilers {city} 2026 — Tiling Rates, Bathroom and Kitchen Tile Costs"
description: "Tilers {city} 2026 — {city} tiler hourly rates, bathroom tiling cost, kitchen splashback prices, floor tiling rates, and how to find a reliable tiler near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["tilers {city}", "tiler {city}", "tiling cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what tilers charge in {city} in 2026 and how to find a reliable one.

## {city} Tiling Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | $80–$140/hr |
| Floor tiling (per m², supply & lay) | $80–$200/m² |
| Wall tiling (per m², supply & lay) | $90–$220/m² |
| Bathroom tiling (full, small bathroom) | $3,000–$8,000 |
| Kitchen splashback (2m linear) | $600–$2,500 |
| Shower tiling (walls + floor) | $2,500–$6,000 |
| Outdoor paving/tiles (per m²) | $80–$180/m² |
| Tile removal (per m²) | $30–$60/m² |
| Grout repair / regrouting | $300–$1,200 |
| Waterproofing (per m²) | $30–$60/m² |

*All prices GST inclusive. {rates_note}*

## {city} Tiling Market

{local}

## Choosing Tiles for NZ Conditions

**Bathrooms and wet areas:** Use tiles rated for wet areas (slip resistance R10 minimum for floors, R11+ for shower floors). Porcelain is more durable and less porous than ceramic.

**Kitchens:** Splashbacks can be glass, ceramic, or porcelain. Ensure grout joints are sealed to prevent moisture penetration behind the tiles.

**Outdoor areas:** Use frost-resistant tiles rated for outdoor use. In coastal {city} areas, choose tiles with low water absorption.

**Waterproofing:** All wet areas must be waterproofed to NZ Building Code requirements (E3) before tiling. This is a critical step — inadequate waterproofing causes costly damage. Confirm your tiler waterproofs to AS/NZS 4858.

## What to Ask a {city} Tiler

1. Do you supply waterproofing as part of your quote?
2. What tile brands do you recommend and why?
3. What is your warranty on labour?
4. Can I see recent work (photos or site visits)?
5. Are you GST registered with a NZ business number?

**Find {city} tilers:** [Tilers {city}](/trades/tilers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does bathroom tiling cost in {city}?**
A small full bathroom (floor + walls, 6–10m²): $3,000–$8,000 supply and lay. Larger bathrooms and premium tiles push costs higher.

**How long does tiling take?**
A standard bathroom: 2–4 days. Kitchen splashback: half a day to 1 day. Allow additional time for waterproofing cure time (24–48 hours) before tiling begins.

**Should I supply my own tiles?**
You can, but confirm this with your tiler first. Tilers typically carry trade accounts and may be able to supply tiles at better prices. Always order 10–15% extra to allow for cuts and future repairs.

---

*Related: [Tiling Cost NZ](/articles/tiling-cost-nz/) | [Bathroom Tiling Cost NZ](/articles/bathroom-tiling-cost-nz/) | [Shower Tiling Cost NZ](/articles/shower-tiling-cost-nz/)*
"""


def landscaper_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    if city_key == "christchurch":
        local = "Christchurch's post-earthquake rebuild created significant opportunity for garden and outdoor living redesign. Many Christchurch homeowners have used insurance settlements to invest in outdoor spaces, and the flat Canterbury terrain makes large landscaping projects more straightforward than in hilly cities."
    elif city_key == "hamilton":
        local = "Hamilton's lifestyle and the Waikato's natural environment make outdoor living a priority for many homeowners. The city's warm, humid summers are ideal for lush gardens, and new-build subdivisions create strong demand for garden establishment packages."
    elif city_key == "tauranga":
        local = "Tauranga's coastal lifestyle and long warm summers make outdoor living areas highly valued. Decks, plunge pools, outdoor kitchens, and established gardens are in strong demand, particularly in lifestyle-oriented suburbs like Mt Maunganui and Papamoa Beach."
    else:  # dunedin
        local = "Dunedin's cooler climate shapes landscaping choices — shelter belts, wind-hardy plantings, and low-maintenance gardens are popular. The city's older character homes often have large established sections that require ongoing maintenance."

    return f"""---
title: "Landscapers {city} 2026 — Garden Design, Landscaping Costs and What to Expect"
description: "Landscapers {city} 2026 — {city} landscaping costs, garden design prices, retaining wall quotes, lawn and planting packages, and how to find a reliable landscaper near you."
image: "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["landscapers {city}", "landscaper {city}", "landscaping cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what landscapers charge in {city} in 2026 and how to find a reliable one.

## {city} Landscaping Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate (labourer) | $50–$90/hr |
| Hourly rate (qualified landscaper/designer) | $80–$150/hr |
| Garden design (small section) | $800–$2,500 |
| Full garden makeover (small-medium) | $10,000–$35,000 |
| Lawn installation (turf, per m²) | $25–$60/m² |
| Retaining wall — timber sleeper (per m²) | $400–$900/m² |
| Retaining wall — concrete block (per m²) | $600–$1,400/m² |
| Paving / outdoor tiles (per m², installed) | $100–$300/m² |
| Planting package (mixed shrubs, per m²) | $80–$200/m² |
| Irrigation system (small section) | $2,000–$6,000 |
| Outdoor lighting | $1,500–$6,000 |
| Tree removal (small-medium) | $500–$2,000 |

*All prices GST inclusive. {rates_note}*

## {city} Landscaping Market

{local}

## What's Included in a Landscaping Quote

Landscaping quotes can vary significantly in scope. Always confirm:

- **Design fees:** Is a design plan included or charged separately?
- **Materials:** Are plants, pavers, and other materials included or priced separately?
- **Subcontractors:** Retaining walls requiring building consent, irrigation, and outdoor lighting may involve subcontractors.
- **Waste removal:** Is site clean-up and green waste disposal included?
- **Consents:** Retaining walls over 1.5m (and sometimes lower) require building consent — confirm who manages this.

## Retaining Walls in {city}

Retaining walls over 1.5m typically require building consent from the {region} Council and may require engineering input. Your landscaper should advise — never build a significant retaining wall without checking consent requirements.

**Find {city} landscapers:** [Landscapers {city}](/trades/landscapers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does landscaping cost in {city}?**
A small garden makeover: $10,000–$35,000. Lawn installation: $25–$60/m² turfed. Retaining wall: $400–$1,400/m² depending on material.

**Do I need consent for a retaining wall in {city}?**
Walls under 1.5m generally don't require consent, but check with the {region} Council — rules vary by site. Walls over 1.5m almost always require consent and often engineering certification.

**How do I find a good landscaper in {city}?**
Look for members of Landscaping New Zealand (LNZ). Ask for a portfolio of recent local work and get 2–3 written quotes for any significant project.

---

*Related: [Landscaping Cost NZ](/articles/landscaping-cost-nz/) | [Retaining Wall Cost NZ](/articles/retaining-wall-cost-nz/) | [Garden Design Cost NZ](/articles/garden-design-cost-nz/)*
"""


def gasfitter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    if city_key == "auckland":
        hourly = "$110–$180/hr"; callout = "$80–$180"
        local = "Auckland's high density and large number of apartments make gasfitters busy year-round. Gas hob and oven installations are extremely common in Auckland renovations. Natural gas is available across most of urban Auckland via Vector's network."
        gas_network = "Natural gas is widely available in Auckland via Vector's network."
    elif city_key == "wellington":
        hourly = "$105–$175/hr"; callout = "$80–$170"
        local = "Wellington has strong demand for gas heating given its cool, windy winters. Gas fires and heat pump combinations are popular. Wellington's older homes often have original gas infrastructure that requires updating."
        gas_network = "Natural gas is available across most of Wellington via Vector's network."
    elif city_key == "christchurch":
        hourly = "$95–$165/hr"; callout = "$70–$155"
        local = "Christchurch has good natural gas availability and strong demand for gas heating and cooking. Post-earthquake work included gas line assessment and replacement in many suburbs."
        gas_network = "Natural gas is available across most of Christchurch via First Gas network."
    elif city_key == "hamilton":
        hourly = "$95–$165/hr"; callout = "$70–$155"
        local = "Hamilton has natural gas available in many suburbs and a strong market for gas cooking and hot water. LPG is the alternative for properties not connected to the gas network."
        gas_network = "Natural gas is available in many Hamilton suburbs. LPG is used where mains gas isn't connected."
    else:  # tauranga
        hourly = "$100–$170/hr"; callout = "$75–$160"
        local = "Tauranga has more limited natural gas availability than the main centres — LPG is commonly used. Gas hobs, outdoor BBQ connections, and gas hot water are popular."
        gas_network = "Natural gas availability is limited in Tauranga — LPG is the most common option."

    return f"""---
title: "Gasfitters {city} 2026 — Gas Fitting Rates, Costs and What Requires a Licensed Gasfitter"
description: "Gasfitters {city} 2026 — {city} gasfitter rates, gas hob installation cost, gas hot water prices, LPG vs natural gas, and how to find a licensed gasfitter near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["gasfitters {city}", "gasfitter {city}", "gas fitting cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what gasfitters charge in {city} in 2026 and what gas work legally requires a licensed professional.

## {city} Gasfitter Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (weekday) | {callout} |
| Hourly rate | {hourly} |
| Gas hob installation | $400–$900 |
| Gas oven installation | $500–$1,100 |
| Gas hot water cylinder (install) | $2,000–$4,000 |
| Continuous flow gas hot water (install) | $1,800–$3,500 |
| Gas fire installation (flued) | $3,000–$7,000 |
| Gas BBQ point installation | $400–$900 |
| LPG to natural gas conversion | $500–$1,500 |
| Gas leak detection | $200–$500 |
| Gas line extension (per metre) | $80–$200/m |
| Annual gas appliance service | $150–$350 |

*All prices GST inclusive. {rates_note}*

## {city} Gas Market

{local}

{gas_network}

## What Requires a Licensed Gasfitter in NZ

All gasfitting work in NZ must be done by a person licensed under the Gas Act 1992 and registered with the Plumbers, Gasfitters and Drainlayers Board (PGDB). This includes:

- Connecting any gas appliance (hob, oven, hot water, heater, BBQ point)
- Installing or modifying gas pipework
- Converting between LPG and natural gas
- Testing gas systems

**Never attempt DIY gasfitting.** Gas leaks cause fires and carbon monoxide poisoning. All gasfitting work must result in a compliance certificate.

**Verify your gasfitter:** [pgdb.co.nz](https://www.pgdb.co.nz) — check registration before any work starts.

## Gas Safety in {city} Homes

- Have gas appliances serviced every 1–2 years
- Install CO (carbon monoxide) detectors in rooms with gas appliances
- If you smell gas: don't use switches or flames, open windows, leave the building, call your gas supplier
- Annual gas pipe inspection is recommended for older homes

**Find {city} gasfitters:** [Gasfitters {city}](/trades/gasfitters/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does gasfitting cost in {city}?**
Call-out: {callout}. Gas hob installation: $400–$900. Gas hot water cylinder: $2,000–$4,000 installed.

**Do I need a licensed gasfitter for a gas hob in {city}?**
Yes — connecting any gas appliance to the gas supply is restricted work requiring a licensed gasfitter. A compliance certificate is required.

**How do I check if my {city} gasfitter is licensed?**
Search the PGDB register at pgdb.co.nz by name or company. Always ask for their licence number before work starts.

---

*Related: [Gas Fitting Cost NZ](/articles/gas-fitting-cost-nz/) | [Hot Water Cylinder Cost NZ](/articles/hot-water-cylinder-cost-nz/) | [Kitchen Renovation Cost NZ](/articles/kitchen-renovation-cost-nz/)*
"""


def concreter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    if city_key == "auckland":
        m2_rate = "$120–$250/m²"; driveway = "$6,000–$18,000"
        local = "Auckland's busy construction market and high land values make concrete work essential for driveways, paths, and foundations. Access challenges on steep Auckland sections can add significantly to costs."
    elif city_key == "wellington":
        m2_rate = "$130–$260/m²"; driveway = "$6,500–$20,000"
        local = "Wellington's hilly terrain makes concrete work more complex and expensive than flat cities. Retaining and foundation work often requires significant excavation. Seismic considerations influence foundation design."
    elif city_key == "christchurch":
        m2_rate = "$110–$230/m²"; driveway = "$5,500–$17,000"
        local = "Post-earthquake Christchurch saw massive demand for foundation repair and new concrete work. While the rebuild is mature, concrete work remains strong with ongoing new residential development."
    elif city_key == "hamilton":
        m2_rate = "$100–$210/m²"; driveway = "$5,000–$16,000"
        local = "Hamilton's growing suburbs generate steady demand for concrete driveways, paths, and slab foundations. The Waikato's warm climate is good for curing concrete."
    elif city_key == "tauranga":
        m2_rate = "$105–$220/m²"; driveway = "$5,500–$17,000"
        local = "Tauranga's construction boom includes strong demand for concrete driveways, pool surrounds, and outdoor entertaining areas. Coastal salt air is a factor for exposed concrete — sealants are recommended."
    else:  # dunedin
        m2_rate = "$95–$200/m²"; driveway = "$4,500–$15,000"
        local = "Dunedin concreters work on a mix of driveways, paths, and foundation work. Dunedin's cold winters require careful timing — concrete shouldn't be poured in near-freezing conditions without protection."

    return f"""---
title: "Concreters {city} 2026 — Concrete Prices, Driveway Costs and What to Expect"
description: "Concreters {city} 2026 — {city} concrete driveway cost, slab pricing, path costs, decorative concrete rates, and how to find a reliable concreter near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["concreters {city}", "concreter {city}", "concrete cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what concreters charge in {city} in 2026 and what to expect.

## {city} Concreter Rates 2026

| Service | {city} typical cost |
|---|---|
| Concrete driveway (per m²) | {m2_rate} |
| Concrete driveway (standard, 40m²) | {driveway} |
| Concrete path (per m²) | $100–$200/m² |
| Concrete slab — shed/garage (per m²) | $110–$220/m² |
| Exposed aggregate (per m², premium) | $150–$300/m² |
| Coloured/stencilled concrete (per m²) | $160–$320/m² |
| Concrete steps (per step) | $300–$700/step |
| Retaining wall — concrete block (per m²) | $600–$1,400/m² |
| Demolish + remove old concrete (per m²) | $40–$90/m² |
| Concrete sealing (per m²) | $15–$40/m² |

*All prices GST inclusive. {rates_note}*

## {city} Concrete Market

{local}

## Concrete Finishes Available in NZ

**Plain broom finish:** The standard for driveways and paths — textured for grip. Most economical.

**Exposed aggregate:** Small stones embedded in the surface, exposed by washing while wet. Popular for driveways — durable and attractive.

**Stamped / stencilled concrete:** Patterns impressed or stencilled into the concrete surface. Can mimic pavers or stone. Higher maintenance than plain finishes.

**Coloured concrete:** Oxide pigments added to the mix. UV exposure can cause some fading — use UV-resistant sealers.

**Polished concrete:** Used indoors (slab floors). Mechanically ground and polished to a sheen. Popular in renovations.

## Getting Concrete Quotes in {city}

- Get 2–3 written quotes including materials, labour, and disposal of existing concrete
- Confirm concrete strength (MPa) — driveways: 25–32 MPa minimum; structural slabs: 32–40 MPa
- Check if sub-base preparation (compaction) is included
- Confirm thickness — driveways: 100mm minimum; light vehicle: 125mm

**Find {city} concreters:** [Concreters {city}](/trades/concreters/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a concrete driveway cost in {city}?**
A standard 40m² driveway: {driveway} including preparation, concrete, and finishing. Exposed aggregate or coloured concrete adds 30–50%.

**How long does concrete take to cure?**
Concrete is walkable after 24–48 hours and driveable after 7 days. Full strength (28-day cure) takes 4 weeks. Avoid heavy vehicles for 4 weeks minimum.

**How thick should a concrete driveway be in {city}?**
Minimum 100mm for pedestrian use, 125mm for domestic vehicles, 150mm+ for heavy vehicles. Your concreter should advise based on your soil type.

---

*Related: [Concrete Driveway Cost NZ](/articles/concrete-driveway-cost-nz/) | [Asphalt Driveway Cost NZ](/articles/asphalt-driveway-cost-nz/) | [Retaining Wall Cost NZ](/articles/retaining-wall-cost-nz/)*
"""


def carpenter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    if city_key == "auckland":
        hourly = "$90–$165/hr"
        local = "Auckland carpenters are busy across new builds, renovations, and fit-out work. Demand for deck builds, pergolas, and outdoor entertainment areas has been strong, and cladding replacement (particularly Rockcote and monolithic cladding) remains a major category."
    elif city_key == "wellington":
        hourly = "$90–$165/hr"
        local = "Wellington carpenters frequently work on character villas and bungalows — jobs requiring skill with older timber framing, sash windows, and heritage details. Wind-driven rain means weathertightness detailing is especially important."
    elif city_key == "christchurch":
        hourly = "$85–$155/hr"
        local = "Post-earthquake Christchurch created massive demand for carpentry. While the main rebuild phase is complete, strong new residential development and renovation work keeps carpenters well occupied."
    else:  # hamilton
        hourly = "$80–$150/hr"
        local = "Hamilton carpenters work across a strong residential market — new builds in growth areas, renovations of older homes, and fit-out work in the city's growing commercial sector."

    return f"""---
title: "Carpenters {city} 2026 — Carpenter Rates, Fit-Out Costs and What to Expect"
description: "Carpenters {city} 2026 — {city} carpenter hourly rates, deck build costs, renovation prices, framing rates, and how to find a reliable carpenter near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["carpenters {city}", "carpenter {city}", "carpentry cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what carpenters charge in {city} in 2026 and what to expect.

## {city} Carpenter Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Deck build (basic, 20m²) | $8,000–$20,000 |
| Deck build (hardwood, 20m²) | $18,000–$40,000 |
| Pergola | $6,000–$20,000 |
| Fence (timber, per m linear) | $150–$400/m |
| Door installation (internal) | $300–$600 per door |
| Door installation (external) | $600–$1,500 per door |
| Window replacement (per window) | $800–$2,500 |
| Kitchen fit-out (carcass install) | $3,000–$10,000 |
| Staircase (new, straight) | $5,000–$15,000 |
| Framing (new extension, per m²) | $150–$350/m² |
| Cladding replacement (per m²) | $150–$350/m² |

*All prices GST inclusive. {rates_note}*

## {city} Carpentry Market

{local}

## LBP Licensing for Carpenters

Carpenters doing "restricted building work" must be Licensed Building Practitioners (LBPs). This covers:
- Structural framing
- Weathertightness work (cladding, windows, doors to the exterior)

LBP licence classes relevant to carpentry: **Carpentry** and **Site** (for site supervisors). Verify at [lbp.govt.nz](https://www.lbp.govt.nz).

For non-structural fit-out work (internal doors, kitchens, decking that doesn't require consent), an LBP is not legally required — but experience and quality still matter.

## What to Ask a {city} Carpenter

1. Are you an LBP — what is your licence class and number?
2. Do you manage consents or do I need to arrange that?
3. Is your quote fixed-price or time-and-materials?
4. Who supplies materials — you or me?
5. What is your timeline and deposit structure?

**Find {city} carpenters:** [Carpenters {city}](/trades/carpenters/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a carpenter cost in {city}?**
Hourly rate: {hourly}. Deck build (20m², basic): $8,000–$20,000. Hardwood or composite deck: $18,000–$40,000.

**Do I need an LBP carpenter for a deck?**
If the deck requires building consent (usually decks over 1.5m above ground), yes — LBP sign-off is required. For ground-level decks under the consent threshold, an LBP is not legally required but still recommended.

**How long does a deck build take in {city}?**
A standard 20m² deck: 3–7 days depending on complexity, materials, and access. Hardwood decks take longer due to denser timber and more complex joinery.

---

*Related: [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Builder Pricing Guide NZ](/articles/builder-pricing-guide-nz-2026/) | [Pergola Cost NZ](/articles/pergola-cost-nz/)*
"""


# ── Article definitions ────────────────────────────────────────────────────────

ARTICLES = [
    # Electricians
    ("electrician-hamilton-nz",    lambda: electrician_article("hamilton")),
    ("electrician-tauranga-nz",    lambda: electrician_article("tauranga")),
    ("electrician-dunedin-nz",     lambda: electrician_article("dunedin")),
    ("electrician-napier-nz",      lambda: electrician_article("napier")),
    ("electrician-new-plymouth-nz",lambda: electrician_article("new-plymouth")),
    # Plumbers
    ("plumber-tauranga-nz",        lambda: plumber_article("tauranga")),
    ("plumber-dunedin-nz",         lambda: plumber_article("dunedin")),
    ("plumber-napier-nz",          lambda: plumber_article("napier")),
    ("plumber-new-plymouth-nz",    lambda: plumber_article("new-plymouth")),
    # Builders
    ("builder-hamilton-nz",        lambda: builder_article("hamilton")),
    ("builder-tauranga-nz",        lambda: builder_article("tauranga")),
    ("builder-dunedin-nz",         lambda: builder_article("dunedin")),
    # Roofers
    ("roofer-hamilton-nz",         lambda: roofer_article("hamilton")),
    ("roofer-tauranga-nz",         lambda: roofer_article("tauranga")),
    ("roofer-dunedin-nz",          lambda: roofer_article("dunedin")),
    ("roofer-napier-nz",           lambda: roofer_article("napier")),
    ("roofer-new-plymouth-nz",     lambda: roofer_article("new-plymouth")),
    # Tilers
    ("tiler-hamilton-nz",          lambda: tiler_article("hamilton")),
    ("tiler-tauranga-nz",          lambda: tiler_article("tauranga")),
    ("tiler-dunedin-nz",           lambda: tiler_article("dunedin")),
    # Landscapers
    ("landscaper-christchurch-nz", lambda: landscaper_article("christchurch")),
    ("landscaper-hamilton-nz",     lambda: landscaper_article("hamilton")),
    ("landscaper-tauranga-nz",     lambda: landscaper_article("tauranga")),
    ("landscaper-dunedin-nz",      lambda: landscaper_article("dunedin")),
    # Gasfitters
    ("gasfitter-auckland-nz",      lambda: gasfitter_article("auckland")),
    ("gasfitter-wellington-nz",    lambda: gasfitter_article("wellington")),
    ("gasfitter-christchurch-nz",  lambda: gasfitter_article("christchurch")),
    ("gasfitter-hamilton-nz",      lambda: gasfitter_article("hamilton")),
    ("gasfitter-tauranga-nz",      lambda: gasfitter_article("tauranga")),
    # Concreters
    ("concreter-auckland-nz",      lambda: concreter_article("auckland")),
    ("concreter-wellington-nz",    lambda: concreter_article("wellington")),
    ("concreter-christchurch-nz",  lambda: concreter_article("christchurch")),
    ("concreter-hamilton-nz",      lambda: concreter_article("hamilton")),
    ("concreter-tauranga-nz",      lambda: concreter_article("tauranga")),
    ("concreter-dunedin-nz",       lambda: concreter_article("dunedin")),
    # Carpenters
    ("carpenter-auckland-nz",      lambda: carpenter_article("auckland")),
    ("carpenter-wellington-nz",    lambda: carpenter_article("wellington")),
    ("carpenter-christchurch-nz",  lambda: carpenter_article("christchurch")),
    ("carpenter-hamilton-nz",      lambda: carpenter_article("hamilton")),
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
