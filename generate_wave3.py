#!/usr/bin/env python3
"""
Wave 3 SEO content generator — TradieTools NZ
New cities: Palmerston North, Nelson, Rotorua
New trades: drainlayer, heat pump installer, plasterer
Run: python3 generate_wave3.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

# ── City data ─────────────────────────────────────────────────────────────────

CITIES = {
    "palmerston-north": {
        "name": "Palmerston North",
        "region": "Manawatu-Whanganui",
        "region_adj": "Manawatu",
        "rate_note": "Palmerston North rates are broadly regional — below Auckland and Wellington, comparable to Hamilton.",
        "context": "Palmerston North is the Manawatu's largest city and home to Massey University, giving it a large student and academic population. The city has steady residential demand alongside a significant logistics and distribution sector.",
        "housing": "Palmerston North has a mix of older post-war homes and newer subdivisions on the city's edges. The relatively affordable housing market has driven renovation activity as buyers improve older stock.",
        "pop": "90,000",
    },
    "nelson": {
        "name": "Nelson",
        "region": "Nelson-Tasman",
        "region_adj": "Nelson",
        "rate_note": "Nelson rates are broadly regional — similar to Napier and New Plymouth, reflecting a smaller but lifestyle-oriented market.",
        "context": "Nelson is one of New Zealand's sunniest cities, situated at the top of the South Island. Its lifestyle appeal drives strong inward migration and a buoyant property market. Tourism, horticulture, and seafood industries support the local economy.",
        "housing": "Nelson has a mix of older character homes in central areas and newer subdivisions in Richmond and Stoke. The sunshine and mild climate make outdoor living a priority — decks, gardens, and outdoor spaces are valued.",
        "pop": "55,000",
    },
    "rotorua": {
        "name": "Rotorua",
        "region": "Bay of Plenty",
        "region_adj": "Bay of Plenty",
        "rate_note": "Rotorua rates are broadly regional — similar to other mid-sized NZ cities, though geothermal activity can add complexity to some building and plumbing work.",
        "context": "Rotorua is famous for its geothermal activity and Māori culture. The city's tourism industry is significant, driving commercial construction and hospitality fit-out work alongside steady residential demand.",
        "housing": "Geothermal activity in Rotorua has unique implications for building — some areas have geothermal ground conditions that affect foundations, drainage, and pipe materials. Always check geothermal hazard zoning before buying or building.",
        "pop": "60,000",
    },
    # Existing cities for new trades
    "auckland": {
        "name": "Auckland",
        "region": "Auckland",
        "region_adj": "Auckland",
        "rate_note": "Auckland rates are 15–25% above the national average.",
        "context": "Auckland is New Zealand's largest city with over 1.7 million people and the most active construction and trade market in NZ.",
        "housing": "Auckland has everything from 1900s villas to brand-new townhouses. Each era brings different maintenance and upgrade needs.",
        "pop": "1,700,000",
    },
    "wellington": {
        "name": "Wellington",
        "region": "Wellington",
        "region_adj": "Wellington",
        "rate_note": "Wellington rates are broadly comparable to Auckland — driven by high cost of living and a competitive labour market.",
        "context": "Wellington is New Zealand's capital, a compact hilly city with high-quality housing demand and older wooden villa character homes.",
        "housing": "Wellington has a high proportion of older wooden villas and bungalows requiring specialist trade knowledge.",
        "pop": "215,000",
    },
    "christchurch": {
        "name": "Christchurch",
        "region": "Canterbury",
        "region_adj": "Canterbury",
        "rate_note": "Christchurch rates are broadly similar to Hamilton and Tauranga — below Auckland and Wellington.",
        "context": "Christchurch is the South Island's largest city. Post-earthquake rebuild activity continues alongside new residential development.",
        "housing": "Post-earthquake Christchurch has a large proportion of newer housing stock alongside older homes that survived the 2010–2011 earthquakes.",
        "pop": "400,000",
    },
    "hamilton": {
        "name": "Hamilton",
        "region": "Waikato",
        "region_adj": "Waikato",
        "rate_note": "Hamilton rates are typically 10–15% below Auckland but on par with other major NZ cities.",
        "context": "Hamilton is Waikato's largest city with strong residential growth and a busy construction pipeline.",
        "housing": "Much of Hamilton's housing stock was built in the 1960s–1990s, with active renovation and upgrade work.",
        "pop": "170,000",
    },
    "tauranga": {
        "name": "Tauranga",
        "region": "Bay of Plenty",
        "region_adj": "Bay of Plenty",
        "rate_note": "Tauranga rates are broadly similar to Hamilton, though strong demand can push prices higher.",
        "context": "Tauranga is one of New Zealand's fastest-growing cities with a strong construction boom and large retiree population.",
        "housing": "Tauranga has a mix of older state housing and brand-new coastal developments. Salt air is a factor for exterior work.",
        "pop": "155,000",
    },
    "dunedin": {
        "name": "Dunedin",
        "region": "Otago",
        "region_adj": "Otago",
        "rate_note": "Dunedin rates are 10–20% below Auckland, reflecting the smaller, less pressured southern market.",
        "context": "Dunedin is the University of Otago's home city with a large student population and rich Victorian housing stock.",
        "housing": "Older Dunedin homes often have original wiring, lead pipes, and older roofing — renovation work is common.",
        "pop": "130,000",
    },
}

# ── Trade generators ───────────────────────────────────────────────────────────

def electrician_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    housing = c["housing"]
    rates_note = c["rate_note"]

    rate_map = {
        "palmerston-north": ("$90–$160/hr", "$65–$145", "$180–$420", "$1,100–$3,200", "$950–$2,100"),
        "nelson":           ("$95–$165/hr", "$70–$150", "$190–$430", "$1,100–$3,300", "$1,000–$2,200"),
        "rotorua":          ("$90–$160/hr", "$65–$145", "$180–$420", "$1,100–$3,200", "$950–$2,100"),
    }
    hourly, callout, after_hours, switchboard, ev = rate_map.get(city_key, ("$95–$165/hr","$70–$150","$190–$430","$1,100–$3,200","$1,000–$2,100"))

    local_map = {
        "palmerston-north": "Palmerston North has steady residential and commercial electrical demand. Massey University and several large distribution centres generate ongoing commercial and industrial electrical work.",
        "nelson":           f"Nelson's high sunshine hours (2,400+/year) make it one of the best cities in NZ for solar — solar-experienced electricians are in strong demand. The lifestyle market also drives EV charger and home automation work.",
        "rotorua":          "Rotorua's geothermal environment means some local electricians have specialist knowledge of working in geothermal-affected areas. Tourism hospitality venues and the residential market both drive demand.",
    }
    local = local_map.get(city_key, f"{city} has steady residential and commercial electrical demand.")

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
| Solar panel system wiring (grid-tie) | $1,100–$3,300 |
| Underfloor heating wiring (per m²) | $45–$110/m² |

*All prices GST inclusive. {rates_note}*

## {city} Electrical Market

{local}

{housing}

## What Requires a Licensed Electrician in NZ

All "restricted electrical work" must be done by an EWRB-registered electrician:

- Installing or modifying any fixed wiring
- Power points, light switches, ceiling fans
- Switchboard work
- Fixed appliances (heat pump, hot water cylinder, EV charger)
- Testing and certifying (issuing a Certificate of Compliance)

**Verify your electrician:** [ewrb.govt.nz](https://www.ewrb.govt.nz)

## Hiring a {city} Electrician — What to Ask

1. Are you EWRB registered — can I have your licence number?
2. Will I receive a Certificate of Compliance?
3. What is your call-out fee and hourly rate?
4. Do you cover my suburb?
5. What is your availability for non-urgent work?

**Find {city} electricians:** [Electricians {city}](/trades/electricians/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does an electrician cost in {city}?**
Call-out: {callout}. Hourly rate: {hourly}. Simple power point install: $130–$300 total. {rates_note}

**Do I need a Certificate of Compliance in {city}?**
Yes — for all restricted electrical work. It's a legal requirement and protects your insurance.

**How much does EV charger installation cost in {city}?**
{ev} for a standard 7kW home EV charger. Add $500–$1,500 if the switchboard needs upgrading.

---

*Related: [Electrician Cost NZ](/articles/electrician-cost-nz/) | [Heat Pump Installation Cost NZ](/articles/heat-pump-installation-cost-nz/) | [Solar Panel Cost NZ](/articles/solar-panel-cost-nz/)*
"""


def plumber_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    housing = c["housing"]
    rates_note = c["rate_note"]

    rate_map = {
        "palmerston-north": ("$95–$165/hr", "$70–$150", "$190–$430"),
        "nelson":           ("$100–$170/hr","$75–$155", "$200–$450"),
        "rotorua":          ("$95–$165/hr", "$70–$150", "$190–$430"),
    }
    hourly, callout, after_hours = rate_map.get(city_key, ("$95–$165/hr","$70–$150","$190–$430"))

    local_map = {
        "palmerston-north": "Palmerston North plumbers serve a large student rental market and steady residential demand. The city's older housing stock includes galvanised pipes that regularly need replacing.",
        "nelson":           "Nelson's growing population and lifestyle market drive strong plumbing demand. Solar hot water is popular given the city's exceptional sunshine hours.",
        "rotorua":          "Rotorua's geothermal activity can affect plumbing — some areas have acidic groundwater or geothermal gases that can corrode standard pipe materials. Local plumbers with geothermal experience are preferred.",
    }
    local = local_map.get(city_key, f"{city} has steady residential plumbing demand.")

    return f"""---
title: "Plumbers {city} 2026 — Hourly Rates, Call-Out Fees and Common Job Costs"
description: "Plumbers {city} 2026 — {city} plumber rates, call-out fees, hot water cylinder costs, drain unblocking prices, and how to find a reliable plumber near you."
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

Sanitary plumbing and drainlaying are restricted trades — all work must be done by someone registered with the PGDB:

- Water supply, drainage, and sanitary systems
- Hot water cylinder installation
- Bathroom and kitchen plumbing
- Connections to the public sewer

**Verify your plumber:** [pgdb.co.nz](https://www.pgdb.co.nz)

**Find {city} plumbers:** [Plumbers {city}](/trades/plumbers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a plumber cost in {city}?**
Call-out: {callout}. Hourly: {hourly}. Blocked drain: $150–$350. Hot water cylinder (replace): $1,800–$3,500 installed.

**How much does hot water cylinder replacement cost in {city}?**
$1,800–$3,500 for a standard 180L mains-pressure cylinder installed. Heat pump hot water: $3,500–$6,000 installed.

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

    rate_map = {
        "palmerston-north": ("$80–$150/hr", "$2,400–$4,200/m²"),
        "nelson":           ("$85–$155/hr", "$2,600–$4,600/m²"),
        "rotorua":          ("$80–$150/hr", "$2,400–$4,200/m²"),
    }
    hourly, m2 = rate_map.get(city_key, ("$80–$150/hr","$2,400–$4,200/m²"))

    local_map = {
        "palmerston-north": "Palmerston North's affordable land prices attract first-home buyers and investors, supporting new builds and renovations. Massey University's ongoing campus development also sustains commercial building activity.",
        "nelson":           "Nelson's lifestyle appeal drives strong renovation demand — outdoor decks, kitchen and bathroom upgrades, and additions are popular. New builds in Richmond and Stoke serve the growing population.",
        "rotorua":          "Rotorua's construction market includes residential new builds and significant hospitality/tourism fit-out work. Geothermal ground conditions in some areas require specialist foundation design.",
    }
    local = local_map.get(city_key, f"{city} has steady residential building demand.")

    return f"""---
title: "Builders {city} 2026 — Hourly Rates, New Build Costs and What to Expect"
description: "Builders {city} 2026 — {city} builder hourly rates, new build cost per m², extension costs, LBP licensing explained, and how to find a reliable builder near you."
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
| New build cost (per m², turnkey) | {m2} |
| House extension (per m²) | $2,800–$5,000/m² |
| Deck build (basic, 20m²) | $7,000–$18,000 |
| Deck build (hardwood, 20m²) | $14,000–$32,000 |
| Garage build (double, standard) | $30,000–$65,000 |
| Kitchen renovation (builder work only) | $5,000–$18,000 |
| Bathroom renovation (builder work only) | $7,000–$22,000 |
| Weatherboard replacement (per m²) | $140–$320/m² |
| Pergola build | $5,000–$18,000 |

*All prices GST inclusive. {rates_note}*

## {city} Building Market

{local}

{housing}

## LBP Licensing

All restricted building work requires a Licensed Building Practitioner (LBP). Verify at [lbp.govt.nz](https://www.lbp.govt.nz). Your builder must provide a Record of Work on completion.

**Find {city} builders:** [Builders {city}](/trades/builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a builder cost in {city}?**
Hourly: {hourly}. New build: {m2} turnkey. Extensions typically cost $2,800–$5,000/m².

**Do I need building consent in {city}?**
Most structural work and new builds require consent from the {region} Council. Your builder should advise.

---

*Related: [Builder Pricing Guide NZ](/articles/builder-pricing-guide-nz-2026/) | [Deck Building Cost NZ](/articles/deck-building-cost-nz/) | [Home Extension Cost NZ](/articles/home-extension-cost-nz/)*
"""


def roofer_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    local_map = {
        "palmerston-north": "Palmerston North's climate includes high rainfall and occasional strong winds from the Manawatu Gorge. Roof maintenance is important — gutters block quickly with leaf debris and moss growth is common.",
        "nelson":           "Nelson's high sunshine and low rainfall make it gentler on roofs than wetter cities. UV degradation is more of a factor — roof coatings and paint need regular maintenance to protect metal roofing.",
        "rotorua":          "Rotorua's geothermal atmosphere — hydrogen sulphide and other gases — can accelerate corrosion on metal roofing more than in other NZ cities. High-grade Colorsteel coatings and regular inspections are important.",
    }
    local = local_map.get(city_key, f"{city} has steady roofing demand across replacement, repair, and maintenance work.")

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
| Re-roofing — corrugated iron (per m²) | $75–$145/m² |
| Re-roofing — long-run steel (per m²) | $85–$160/m² |
| Re-roofing — concrete tile (per m²) | $95–$175/m² |
| Full roof replacement (100m² home) | $11,000–$28,000 |
| Gutter replacement (per metre) | $55–$140/m |
| Roof painting / treatment | $2,800–$7,500 |
| Skylight installation | $1,500–$4,000 |
| Moss and lichen treatment | $500–$2,000 |

*All prices GST inclusive. {rates_note}*

## {city} Roofing Market

{local}

## Getting Quotes for {city} Roofing

- Get 2–3 written quotes for any work over $5,000
- Confirm the steel product and warranty (15–50 years depending on coating grade)
- Scaffolding must be included (legally required for most roof work)
- Ask if the roofer is a member of the Roofing Association of NZ (RANZ)

**Find {city} roofers:** [Roofers {city}](/trades/roofers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a roof replacement cost in {city}?**
Full replacement on a 100m² home: $11,000–$28,000. Corrugated iron: $75–$145/m². Long-run steel: $85–$160/m².

**Does roofing work need building consent in {city}?**
Like-for-like re-roofing generally doesn't. Changing material, pitch, or adding skylights typically does — your roofer will advise.

---

*Related: [Roof Replacement Cost NZ](/articles/roof-replacement-cost-nz/) | [Roof Painting Cost NZ](/articles/roof-painting-cost-nz/) | [Guttering Replacement Cost NZ](/articles/guttering-replacement-cost-nz/)*
"""


def drainlayer_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    rate_map = {
        "auckland":      ("$110–$185/hr", "$80–$180", "$3,000–$8,000"),
        "wellington":    ("$105–$180/hr", "$80–$170", "$3,000–$8,000"),
        "christchurch":  ("$95–$165/hr",  "$70–$155", "$2,500–$7,000"),
        "hamilton":      ("$90–$160/hr",  "$65–$150", "$2,500–$6,500"),
        "tauranga":      ("$95–$165/hr",  "$70–$155", "$2,500–$7,000"),
        "dunedin":       ("$85–$155/hr",  "$60–$140", "$2,200–$6,000"),
    }
    hourly, callout, sewer = rate_map.get(city_key, ("$90–$160/hr","$65–$150","$2,500–$6,500"))

    local_map = {
        "auckland":     "Auckland's ageing clay and concrete sewer pipes — many dating to the 1950s–1970s — are a major source of drainlaying work. Tree root intrusion in older suburbs like Remuera, Epsom, and Mt Eden is extremely common.",
        "wellington":   "Wellington's hilly terrain makes stormwater drainage particularly important. Many older Wellington homes have original clay drains that have shifted or cracked over decades of seismic activity.",
        "christchurch": "Post-earthquake Christchurch required massive sewer and stormwater infrastructure repair. While the main rebuild is complete, residential drain repair and upgrade work continues as older pipes reach end of life.",
        "hamilton":     "Hamilton's flat terrain and clay soils are prone to slow drainage and root intrusion in older sewer laterals. New subdivisions in growth areas generate strong demand for new drainlaying.",
        "tauranga":     "Tauranga's rapid growth has pushed council infrastructure — drain upgrades and new connections for subdivisions keep drainlayers busy. Coastal areas require careful stormwater management.",
        "dunedin":      "Dunedin's older housing stock — including many pre-1960 homes — frequently has original clay drain pipes that crack, sag, or become root-infested. Drain camera inspections are a common first step.",
    }
    local = local_map.get(city_key, f"{city} has steady drainlaying demand across new connections and pipe replacement.")

    return f"""---
title: "Drainlayers {city} 2026 — Drain Costs, Sewer Repair Prices and What to Expect"
description: "Drainlayers {city} 2026 — {city} drainlayer rates, sewer repair costs, drain camera inspection prices, new connection fees, and how to find a licensed drainlayer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["drainlayers {city}", "drainlayer {city}", "drain cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what drainlayers charge in {city} in 2026 and what the work involves.

## {city} Drainlayer Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (weekday) | {callout} |
| Hourly rate | {hourly} |
| Drain camera inspection | $250–$500 |
| High-pressure water jetting (unblock) | $200–$500 |
| Root cutting / clearing | $300–$700 |
| Drain repair (pipe patch, per metre) | $400–$900/m |
| Drain replacement (per metre, open cut) | $500–$1,200/m |
| Sewer lateral connection (new) | {sewer} |
| Stormwater connection (new) | $2,000–$6,000 |
| Septic tank installation | $8,000–$20,000+ |
| Soakage pit / field installation | $3,000–$8,000 |
| Drainage report / pre-purchase inspection | $400–$900 |

*All prices GST inclusive. {rates_note}*

## {city} Drainlaying Market

{local}

## What Requires a Licensed Drainlayer in NZ

Drainlaying is a restricted trade — all work must be done by someone registered with the Plumbers, Gasfitters and Drainlayers Board (PGDB):

- Installing or altering any drain connected to the public sewer or stormwater network
- Septic system installation and repair
- Sewer lateral connections
- Stormwater drainage

**Verify your drainlayer:** [pgdb.co.nz](https://www.pgdb.co.nz)

## Signs Your {city} Home Needs Drain Work

- Slow-draining sinks, showers, or toilets
- Gurgling sounds in pipes
- Wet patches in the lawn over the drain line
- Tree roots near older clay pipes
- Sewage smell inside the home

A drain camera inspection ($250–$500) is the best first step — it shows exactly what's happening inside the pipes before any digging.

**Find {city} drainlayers:** [Drainlayers {city}](/trades/drainlayers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does drain repair cost in {city}?**
Depends on the problem — a simple jetting to clear a blockage: $200–$500. Pipe repair (per metre): $400–$900. Full lateral replacement: $3,000–$8,000.

**Do I need a licensed drainlayer in {city}?**
Yes — any work connecting to the public sewer or stormwater network is restricted work requiring a PGDB-registered drainlayer.

**What is a drain camera inspection?**
A CCTV camera run through the drain pipes to identify blockages, cracks, root intrusion, or misaligned joints. Cost: $250–$500. Essential before buying an older property.

---

*Related: [Blocked Drain Cost NZ](/articles/blocked-drain-cost-nz/) | [Drainage Solutions Cost NZ](/articles/drainage-solutions-cost-nz/) | [Plumbers {city}](/articles/plumber-{city_key}-nz/)*
"""


def heatpump_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    rate_map = {
        "auckland":     ("$2,500–$4,500", "$4,500–$8,000", "$800–$1,800"),
        "wellington":   ("$2,800–$5,000", "$5,000–$9,000", "$900–$2,000"),
        "christchurch": ("$2,500–$4,500", "$4,500–$8,000", "$800–$1,800"),
        "hamilton":     ("$2,200–$4,000", "$4,000–$7,500", "$750–$1,600"),
        "tauranga":     ("$2,200–$4,000", "$4,000–$7,500", "$750–$1,600"),
        "dunedin":      ("$2,300–$4,200", "$4,200–$7,800", "$800–$1,700"),
    }
    single, multi, service = rate_map.get(city_key, ("$2,300–$4,200","$4,200–$7,500","$800–$1,600"))

    local_map = {
        "auckland":     "Auckland's mild winters mean heat pumps are used more for cooling in summer than heating in winter. Reverse-cycle units that do both efficiently are the norm. EV integration (solar + heat pump + EV) is a growing category.",
        "wellington":   "Wellington's cold, windy winters make heat pumps the heating method of choice. Cold-climate heat pumps (efficient to -15°C) are recommended for exposed Wellington properties. Positioning to avoid prevailing NW winds is important.",
        "christchurch": "Christchurch's cold winters — including regular frosts — make heat pumps essential. Cold-climate models rated to -15°C are strongly recommended. The city's flat terrain and single-storey housing makes installation straightforward.",
        "hamilton":     "Hamilton's warm humid summers and cool winters mean heat pumps work hard year-round. The Waikato's warm summers particularly benefit from reverse-cycle air conditioning — keeping homes cool in January is as important as heating in July.",
        "tauranga":     "Tauranga's mild coastal climate means heat pumps are often as much about cooling as heating. Salt air can affect outdoor unit corrosion over time — marine-grade units and regular servicing are recommended within 2km of the coast.",
        "dunedin":      "Dunedin has some of New Zealand's coldest winters, making efficient heating critical. Cold-climate heat pumps rated to -15°C are essential for reliable Dunedin performance. The city was historically reliant on gas and wood burners — heat pumps are increasingly replacing both.",
    }
    local = local_map.get(city_key, f"{city} has strong demand for heat pump installation and servicing.")

    return f"""---
title: "Heat Pump Installation {city} 2026 — Costs, Brands and What to Expect"
description: "Heat pump installation {city} 2026 — {city} heat pump costs, best brands for NZ conditions, installation prices, servicing costs, and how to find a reliable installer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["heat pump installation {city}", "heat pump {city}", "heat pump cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what heat pump installation costs in {city} in 2026 and how to choose the right system.

## {city} Heat Pump Installation Costs 2026

| System | {city} typical cost (supply + install) |
|---|---|
| Single split system (wall-mounted, 2.5–3.5kW) | {single} |
| Single split system (larger, 5–7kW) | $3,200–$5,500 |
| Multi-split system (2 rooms) | {multi} |
| Multi-split system (3+ rooms) | $7,000–$14,000+ |
| Ducted system (whole home) | $12,000–$30,000+ |
| Heat pump hot water cylinder | $3,500–$6,000 |
| Annual service / clean | {service} |
| Filter replacement | $80–$200 |

*All prices GST inclusive. {rates_note}*

## {city} Heat Pump Market

{local}

## Choosing a Heat Pump for {city}

**Capacity:** Size matters — too small won't heat the room; too large short-cycles and wastes energy. A qualified installer will calculate the right kW for your room size, insulation, and ceiling height.

**Cold-climate rating:** Check the COP (Coefficient of Performance) at low temperatures. For {city}, look for units rated to at least -10°C (ideally -15°C) for reliable winter performance.

**Brands in NZ:** Mitsubishi Electric, Daikin, Fujitsu, Panasonic, and LG are the main brands with full NZ dealer and service networks. All offer comparable performance — installer quality and warranty support matter as much as brand.

**Installation:** All heat pump electrical work must be done by an EWRB-registered electrician. The refrigerant work must be done by an MTA-certified refrigeration technician. Most heat pump companies provide both in one team.

## Heat Pump Servicing in {city}

Heat pumps should be serviced every 1–2 years:
- Filter clean (you can do this yourself every 3 months)
- Coil clean (requires professional equipment)
- Refrigerant check
- Drain check

Annual service cost in {city}: {service}. Regular servicing maintains efficiency and extends unit life.

**Find {city} heat pump installers:** [Heat Pump Installers {city}](/trades/heat-pump-installers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does heat pump installation cost in {city}?**
Single split system (2.5–3.5kW): {single} supply and installed. Multi-split (2 rooms): {multi}.

**What size heat pump do I need for {city}?**
A rough guide: 1kW per 10m² of well-insulated floor space. A 25m² lounge needs roughly 2.5kW. Your installer will calculate based on your specific home — get a site assessment before buying.

**How often should I service my heat pump in {city}?**
Filter: clean every 3 months yourself. Full professional service: every 1–2 years. Cost: {service}.

---

*Related: [Heat Pump Installation Cost NZ](/articles/heat-pump-installation-cost-nz/) | [Heat Pump Servicing Cost NZ](/articles/heat-pump-servicing-cost-nz/) | [Electricians {city}](/articles/electrician-{city_key}-nz/)*
"""


def plasterer_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    context = c["context"]
    rates_note = c["rate_note"]

    rate_map = {
        "auckland":     ("$55–$100/m²", "$45–$85/m²", "$3,500–$9,000"),
        "wellington":   ("$55–$100/m²", "$45–$85/m²", "$3,500–$9,000"),
        "christchurch": ("$50–$90/m²",  "$40–$75/m²", "$3,000–$8,000"),
        "hamilton":     ("$45–$85/m²",  "$38–$72/m²", "$2,800–$7,500"),
        "tauranga":     ("$48–$88/m²",  "$40–$75/m²", "$3,000–$7,800"),
        "dunedin":      ("$45–$82/m²",  "$38–$70/m²", "$2,700–$7,000"),
    }
    walls, stop, reno = rate_map.get(city_key, ("$48–$88/m²","$40–$75/m²","$3,000–$7,800"))

    local_map = {
        "auckland":     "Auckland's busy renovation market and high proportion of older plaster-clad homes keep plasterers in demand. Stopping (GIB finishing) for new builds and renovations is the largest category, with texture coat cladding repair also common.",
        "wellington":   "Wellington's older villas frequently have original lath-and-plaster walls — specialist plasterers who understand heritage plaster are valued. New GIB stopping work is also strong in the renovation market.",
        "christchurch": "Post-earthquake Christchurch required extensive plaster repair and replacement. While the main rebuild is complete, renovation plastering work remains strong as homeowners update post-quake repairs.",
        "hamilton":     "Hamilton's active renovation market drives steady plastering demand. GIB stopping for extensions and new rooms is common as homeowners improve 1960s–80s homes.",
        "tauranga":     "Tauranga's strong renovation and new-build market keeps plasterers busy. Exterior texture coat (Rockcote, Unitex) application and repair is also common on newer homes.",
        "dunedin":      "Dunedin's Victorian and Edwardian character homes have original plaster walls that require specialist repair. Students and investors renovating rental properties also drive steady demand for GIB stopping and painting prep.",
    }
    local = local_map.get(city_key, f"{city} has steady demand for plastering across new builds and renovations.")

    return f"""---
title: "Plasterers {city} 2026 — Plastering Costs, GIB Stopping Prices and What to Expect"
description: "Plasterers {city} 2026 — {city} plastering costs, GIB stopping prices, texture coat rates, plaster repair costs, and how to find a reliable plasterer near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["plasterers {city}", "plasterer {city}", "plastering cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{context} Here's what plasterers charge in {city} in 2026 and what the work involves.

## {city} Plastering Rates 2026

| Service | {city} typical cost |
|---|---|
| GIB stopping / wall finishing (per m²) | {stop} |
| Texture coat plaster (per m²) | {walls} |
| Full interior plaster (room, supply + labour) | $800–$2,500 per room |
| Full renovation (3-bed home, stopping) | {reno} |
| Cornice installation (per linear metre) | $25–$60/m |
| Plaster repair (small, per patch) | $200–$600 |
| Exterior texture coat (Rockcote, per m²) | $55–$110/m² |
| Solid plaster (traditional, per m²) | $80–$160/m² |
| Skim coat (over existing plaster, per m²) | $35–$65/m² |
| Ceiling repair (water damage, per m²) | $150–$400/m² |

*All prices GST inclusive. {rates_note}*

## {city} Plastering Market

{local}

## Types of Plastering Work in NZ

**GIB stopping:** Finishing the joints and screw holes in GIB (plasterboard) to create a smooth, paint-ready surface. Required in all new builds and renovations using GIB. Quality of stopping is critical — poor stopping shows under paint.

**Texture coat / Rockcote:** Acrylic texture coat applied over a base coat. Common on 1990s–2010s homes as an exterior cladding finish. Prone to cracking and water ingress if not maintained — cracks should be repaired promptly.

**Traditional plaster:** Solid plaster on wire mesh or masonry. Found in older NZ homes. Repairs require matching the original mix — specialist work.

**Skimming:** Applying a thin finish plaster layer over existing plaster to renew the surface. Cheaper than full replastering.

## Hiring a {city} Plasterer

- Get 2–3 written quotes for any job over $3,000
- Ask to see previous work (photos or site visits)
- Confirm whether GIB supply is included or separate
- Check they are GST registered
- Clarify the finish level (Level 4 is standard for painted walls; Level 5 for high-sheen paint)

**Find {city} plasterers:** [Plasterers {city}](/trades/plasterers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does plastering cost in {city}?**
GIB stopping: {stop}/m². Full renovation stopping (3-bed home): {reno}. Plaster repair (small patch): $200–$600.

**What is GIB stopping?**
The process of finishing plasterboard joints and screw holes to create a smooth, paint-ready surface. Done in levels — Level 4 is standard for most painted walls.

**How long does plastering take to dry before painting?**
GIB stopping: 24–48 hours between coats, 3–5 days total before painting. Traditional plaster: allow 4–6 weeks to fully cure. Your plasterer will advise.

---

*Related: [Plasterer Cost NZ](/articles/plasterer-cost-nz/) | [Interior Painting Cost NZ](/articles/interior-painting-cost-nz/) | [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/)*
"""


# ── Article list ───────────────────────────────────────────────────────────────

ARTICLES = [
    # New cities — electricians
    ("electrician-palmerston-north-nz", lambda: electrician_article("palmerston-north")),
    ("electrician-nelson-nz",           lambda: electrician_article("nelson")),
    ("electrician-rotorua-nz",          lambda: electrician_article("rotorua")),
    # New cities — plumbers
    ("plumber-palmerston-north-nz",     lambda: plumber_article("palmerston-north")),
    ("plumber-nelson-nz",               lambda: plumber_article("nelson")),
    ("plumber-rotorua-nz",              lambda: plumber_article("rotorua")),
    # New cities — builders
    ("builder-palmerston-north-nz",     lambda: builder_article("palmerston-north")),
    ("builder-nelson-nz",               lambda: builder_article("nelson")),
    ("builder-rotorua-nz",              lambda: builder_article("rotorua")),
    # New cities — roofers
    ("roofer-palmerston-north-nz",      lambda: roofer_article("palmerston-north")),
    ("roofer-nelson-nz",                lambda: roofer_article("nelson")),
    ("roofer-rotorua-nz",               lambda: roofer_article("rotorua")),
    # Drainlayers — all major cities
    ("drainlayer-auckland-nz",          lambda: drainlayer_article("auckland")),
    ("drainlayer-wellington-nz",        lambda: drainlayer_article("wellington")),
    ("drainlayer-christchurch-nz",      lambda: drainlayer_article("christchurch")),
    ("drainlayer-hamilton-nz",          lambda: drainlayer_article("hamilton")),
    ("drainlayer-tauranga-nz",          lambda: drainlayer_article("tauranga")),
    ("drainlayer-dunedin-nz",           lambda: drainlayer_article("dunedin")),
    # Heat pump installers — all major cities
    ("heat-pump-installer-auckland-nz",      lambda: heatpump_article("auckland")),
    ("heat-pump-installer-wellington-nz",    lambda: heatpump_article("wellington")),
    ("heat-pump-installer-christchurch-nz",  lambda: heatpump_article("christchurch")),
    ("heat-pump-installer-hamilton-nz",      lambda: heatpump_article("hamilton")),
    ("heat-pump-installer-tauranga-nz",      lambda: heatpump_article("tauranga")),
    ("heat-pump-installer-dunedin-nz",       lambda: heatpump_article("dunedin")),
    # Plasterers — all major cities
    ("plasterer-auckland-nz",           lambda: plasterer_article("auckland")),
    ("plasterer-wellington-nz",         lambda: plasterer_article("wellington")),
    ("plasterer-christchurch-nz",       lambda: plasterer_article("christchurch")),
    ("plasterer-hamilton-nz",           lambda: plasterer_article("hamilton")),
    ("plasterer-tauranga-nz",           lambda: plasterer_article("tauranga")),
    ("plasterer-dunedin-nz",            lambda: plasterer_article("dunedin")),
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
