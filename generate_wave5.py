#!/usr/bin/env python3
"""
Wave 5 SEO content generator — TradieTools NZ
Trades: handyman, painter (gap fills), house washer, locksmith, carpet layer
Run: python3 generate_wave5.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "content" / "articles"
TODAY = date.today().isoformat()

CITIES = {
    "auckland":         {"name":"Auckland",        "region":"Auckland",           "rate_adj":"15–25% above national average"},
    "wellington":       {"name":"Wellington",       "region":"Wellington",          "rate_adj":"comparable to Auckland"},
    "christchurch":     {"name":"Christchurch",     "region":"Canterbury",          "rate_adj":"below Auckland and Wellington"},
    "hamilton":         {"name":"Hamilton",         "region":"Waikato",             "rate_adj":"10–15% below Auckland"},
    "tauranga":         {"name":"Tauranga",         "region":"Bay of Plenty",       "rate_adj":"broadly similar to Hamilton"},
    "dunedin":          {"name":"Dunedin",          "region":"Otago",               "rate_adj":"10–20% below Auckland"},
    "napier":           {"name":"Napier",           "region":"Hawke's Bay",         "rate_adj":"broadly regional"},
    "new-plymouth":     {"name":"New Plymouth",     "region":"Taranaki",            "rate_adj":"broadly regional"},
    "palmerston-north": {"name":"Palmerston North", "region":"Manawatu-Whanganui",  "rate_adj":"broadly regional"},
    "nelson":           {"name":"Nelson",           "region":"Nelson-Tasman",       "rate_adj":"broadly regional"},
    "rotorua":          {"name":"Rotorua",          "region":"Bay of Plenty",       "rate_adj":"broadly regional"},
}

# ── Handyman ──────────────────────────────────────────────────────────────────

HANDYMAN_RATES = {
    "auckland":         ("$80–$150/hr", "$100–$200"),
    "wellington":       ("$80–$150/hr", "$100–$200"),
    "christchurch":     ("$70–$130/hr", "$90–$180"),
    "hamilton":         ("$65–$120/hr", "$80–$160"),
    "tauranga":         ("$70–$130/hr", "$85–$165"),
    "dunedin":          ("$60–$115/hr", "$75–$150"),
    "napier":           ("$65–$120/hr", "$80–$160"),
    "new-plymouth":     ("$65–$120/hr", "$80–$160"),
    "palmerston-north": ("$60–$115/hr", "$75–$150"),
    "nelson":           ("$65–$120/hr", "$80–$160"),
    "rotorua":          ("$65–$120/hr", "$80–$160"),
}

def handyman_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    hourly, callout = HANDYMAN_RATES[city_key]

    return f"""---
title: "Handyman {city} 2026 — Hourly Rates, Jobs and What to Expect"
description: "Handyman {city} 2026 — {city} handyman hourly rates, call-out fees, common jobs, what a handyman can and can't do, and how to find a reliable handyman near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["handyman {city}", "handyman cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

A good handyman in {city} can save you time and money on the small-to-medium jobs that don't need a specialist tradie. Here's what {city} handymen charge in 2026 and what they can help with.

## {city} Handyman Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | {hourly} |
| Minimum call-out (first hour) | {callout} |
| Half-day rate (4 hours) | ${int(hourly.split('–')[0].replace('$','').replace('/hr','')) * 4}–${int(hourly.split('–')[1].replace('$','').replace('/hr','')) * 4} |
| Full day rate (8 hours) | ${int(hourly.split('–')[0].replace('$','').replace('/hr','')) * 8}–${int(hourly.split('–')[1].replace('$','').replace('/hr','')) * 8} |
| Flat pack furniture assembly (per item) | $80–$250 |
| TV wall mounting | $150–$350 |
| Door repair / adjustment | $100–$300 |
| Gutter clean (standard house) | $150–$400 |
| Fence repair (per panel) | $150–$400 |
| Tile repair / replacement (per tile) | $80–$250 |
| Painting (small room, walls only) | $400–$1,200 |
| Deck repair (small) | $300–$800 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## What a {city} Handyman Can Do

A handyman is ideal for jobs that are too small for a specialist tradie or involve multiple small tasks in one visit:

- **General repairs:** Door and window adjustments, hinge replacements, lock repairs
- **Furniture:** Flat pack assembly (IKEA, Bunnings), shelving installation
- **Painting:** Small rooms, touch-ups, fence painting
- **Garden:** Minor landscaping, fence repairs, gutter cleaning
- **Plumbing (minor):** Tap washers, toilet seats, shower heads (not requiring licensed work)
- **Electrical (minor):** Light bulb replacement, smoke alarm battery replacement (not wiring)
- **Odd jobs:** TV mounting, picture hanging, draught stopping, weatherstripping

## What a Handyman Cannot Do in {city}

Some work is legally restricted in NZ and requires a licensed tradie — a handyman cannot legally do:

- **Electrical:** Any work on fixed wiring, power points, switches, or the switchboard → requires an EWRB-registered electrician
- **Plumbing:** Any work on water supply, drain connections, hot water cylinders → requires a PGDB-registered plumber
- **Gas:** Any gas appliance connection or pipework → requires a licensed gasfitter
- **Structural building work:** Framing, cladding, weathertightness work → requires an LBP

A reputable handyman will tell you when a job exceeds their scope and recommend the right specialist.

## Finding a Good {city} Handyman

- Hourly rate isn't everything — ask about minimum call-out charges and whether travel time is billed
- Ask for a rough time estimate before they start
- Get a written quote for anything likely to take more than 2–3 hours
- Check Google reviews from recent {city} customers
- Make sure they are GST registered for jobs over a few hundred dollars

**Find {city} handymen:** [Handymen {city}](/trades/handymen/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a handyman cost in {city}?**
Hourly rate: {hourly}. Minimum call-out (first hour): {callout}. Most small jobs take 1–3 hours.

**Is a handyman cheaper than a specialist tradie in {city}?**
Yes — hourly rates are typically 20–40% lower than electricians, plumbers, or builders. But for licensed work (electrical, plumbing, gas), you must use a licensed specialist regardless of cost.

**Do I need a licensed tradie or can a handyman do my job?**
If the job involves fixed electrical wiring, plumbing connections, gas work, or structural building work, you need a licensed specialist. For everything else — repairs, assembly, painting, minor fixes — a handyman is usually fine and more affordable.

---

*Related: [Handyman Cost NZ](/articles/handyman-cost-nz/) | [Painter {city}](/articles/painters-{city_key}-nz/) | [Post a Job Free](/post-job/)*
"""


# ── Painter ───────────────────────────────────────────────────────────────────

PAINTER_DATA = {
    "new-plymouth":     ("$40–$70/m²", "$35–$60/m²", "$4,500–$12,000", "New Plymouth's coastal position means exterior paint must withstand salt air and Taranaki's prevailing westerly weather. Quality exterior paints with UV and mould inhibitors are essential."),
    "palmerston-north": ("$38–$65/m²", "$33–$58/m²", "$4,200–$11,500", "Palmerston North's windy climate accelerates exterior paint weathering. The 'Windy City' reputation means quality preparation and paint selection are especially important for lasting results."),
    "nelson":           ("$40–$68/m²", "$35–$60/m²", "$4,500–$12,000", "Nelson's exceptional sunshine — over 2,400 hours per year — is great for living but accelerates UV degradation of exterior paint. Quality UV-resistant coatings and regular maintenance cycles are important."),
    "rotorua":          ("$38–$65/m²", "$33–$58/m²", "$4,200–$11,500", "Rotorua's geothermal atmosphere — hydrogen sulphide and other gases — can accelerate paint degradation, particularly on metal surfaces. Specialist paints and more frequent repainting cycles are common in geothermal-affected areas."),
}

def painter_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    ext_m2, int_m2, exterior_house, local = PAINTER_DATA[city_key]

    return f"""---
title: "Painters {city} 2026 — Interior and Exterior Painting Costs"
description: "Painters {city} 2026 — {city} painter hourly rates, exterior house painting cost, interior room prices, and how to find a reliable painter near you."
image: "https://images.unsplash.com/photo-1562259929-b4e1fd3aef09?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["painters {city}", "painter {city}", "painting cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{city} has steady demand for both interior and exterior painting — from full house repaint projects to single room refreshes. Here's what painters charge in {city} in 2026.

## {city} Painter Rates 2026

| Service | {city} typical cost |
|---|---|
| Hourly rate | $55–$95/hr |
| Interior painting (per m², 2 coats) | {int_m2} |
| Exterior painting (per m², 2 coats) | {ext_m2} |
| Single room interior (walls only, 12m²) | $600–$1,800 |
| Single room (walls + ceiling + trim) | $900–$2,500 |
| Full exterior house paint (standard 3-bed) | {exterior_house} |
| Roof painting | $3,000–$8,000 |
| Deck staining / oiling (per m²) | $15–$40/m² |
| Fence painting (per m linear, both sides) | $20–$50/m |
| Interior repaint (full 3-bed home) | $6,000–$18,000 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Painting Market

{local}

## Exterior vs Interior Painting in {city}

**Exterior:** The preparation is everything — surface cleaning (waterblasting), filling cracks, sanding, and priming are as important as the topcoats. Skimping on prep leads to paint failure. In {city}, expect to repaint exteriors every 8–12 years depending on exposure.

**Interior:** Less weather-driven but equally dependent on preparation. Filling, sanding, and priming surfaces ensures the topcoat adheres and looks good. Quality paints (Resene, Dulux, Haymes) make a visible difference in finish and longevity.

## Getting Quotes from {city} Painters

- Get 2–3 written quotes for any job over $3,000
- Confirm exactly what prep is included — filling, sanding, priming
- Ask what paint brand and grade will be used
- Check how many coats are included
- Confirm scaffolding or ladder access is included for exterior work
- Ask about the warranty on their workmanship

**Find {city} painters:** [Painters {city}](/trades/painters/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does exterior house painting cost in {city}?**
Standard 3-bed home exterior: {exterior_house}. Larger homes, complex weatherboards, or homes needing significant prep work cost more.

**How often should I repaint my house exterior in {city}?**
Every 8–12 years for a well-prepared, quality paint job. {local[:80]}...

**Do painters in {city} supply paint or do I buy it?**
Most painters supply paint — they have trade accounts and can often source paint more cheaply than retail. Confirm this in your quote and ask what brand/grade they use.

---

*Related: [Exterior House Painting Cost NZ](/articles/exterior-house-painting-cost-nz/) | [Interior Painting Cost NZ](/articles/interior-painting-cost-nz/) | [Roof Painting Cost NZ](/articles/roof-painting-cost-nz/)*
"""


# ── House Washer / Waterblaster ───────────────────────────────────────────────

WASH_RATES = {
    "auckland":     ("$400–$900", "$200–$500", "$150–$400"),
    "wellington":   ("$400–$900", "$200–$500", "$150–$400"),
    "christchurch": ("$350–$800", "$180–$450", "$130–$360"),
    "hamilton":     ("$330–$750", "$170–$420", "$120–$340"),
    "tauranga":     ("$350–$800", "$180–$450", "$130–$360"),
    "dunedin":      ("$320–$720", "$160–$400", "$120–$320"),
}

def housewash_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    house, driveway, roof = WASH_RATES[city_key]

    local_map = {
        "auckland":     "Auckland's humid subtropical climate encourages rapid moss, lichen, and mould growth on roofs, cladding, and driveways. Most Auckland homes benefit from an annual or biennial wash.",
        "wellington":   "Wellington's wind-driven rain and damp climate promote algae and mould on south-facing walls and roofs. Regular house washing protects cladding and paint.",
        "christchurch": "Christchurch's dry easterly winds blow dust and grime onto homes. House washing before repainting is especially important in Canterbury.",
        "hamilton":     "Hamilton's warm, humid summers accelerate biological growth on roofs and cladding. The Waikato's fertility extends to moss and lichen on hard surfaces.",
        "tauranga":     "Tauranga's coastal salt air deposits on cladding and combine with the Bay of Plenty's humidity to grow algae quickly. Coastal homes benefit from more frequent washing.",
        "dunedin":      "Dunedin's damp, cool climate promotes moss and lichen growth, particularly on south-facing surfaces and roofs. Regular treatment prevents permanent staining.",
    }
    local = local_map.get(city_key, f"{city}'s climate means regular house washing keeps your home looking its best and protects the cladding and paint.")

    return f"""---
title: "House Washing {city} 2026 — Waterblasting Costs and What to Expect"
description: "House washing {city} 2026 — {city} house washing costs, waterblasting prices, roof treatment rates, driveway cleaning costs, and how to find a reliable house washer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["house washing {city}", "waterblasting {city}", "house wash cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Regular house washing removes moss, lichen, algae, and grime — protecting your cladding and paint and keeping your home looking its best. Here's what house washing costs in {city} in 2026.

## {city} House Washing Rates 2026

| Service | {city} typical cost |
|---|---|
| Full house wash (standard 3-bed) | {house} |
| House wash + treatment (moss/mould) | $500–$1,200 |
| Driveway waterblast (standard) | {driveway} |
| Deck waterblast and clean | $150–$500 |
| Roof wash and treatment | {roof} |
| Fence wash (per m linear) | $5–$15/m |
| Gutter flush (included with house wash) | Often included |
| Soft wash (chemical wash, low pressure) | $350–$900 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} House Washing Market

{local}

## Waterblasting vs Soft Washing

**Waterblasting (high pressure):** Uses high-pressure water to remove dirt and biological growth. Effective on concrete, brick, and robust cladding. Can damage weatherboards, painted surfaces, or older cladding if done incorrectly — confirm your washer knows your cladding type.

**Soft washing (low pressure + chemicals):** Uses biodegradable chemicals (sodium hypochlorite or similar) at low pressure to kill and remove moss, lichen, and mould. Safer for painted surfaces, cedar weatherboards, and tile roofs. Results last longer as the chemical kills spores rather than just removing visible growth.

**Roof washing:** Most professionals recommend soft washing for roofs — high pressure can lift tiles, damage coatings, and void warranties.

## Protecting Your {city} Home

- House wash every 1–3 years depending on aspect and climate
- North-facing walls need washing less often than south and west-facing surfaces
- Treat after washing with a moss/mould inhibitor to slow regrowth
- Wash before repainting — paint won't adhere to dirty or biological-covered surfaces

**Find {city} house washers:** [House Washers {city}](/trades/house-washing/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does house washing cost in {city}?**
Standard 3-bed house wash: {house}. Including moss/mould treatment: $500–$1,200.

**How often should I wash my house in {city}?**
Every 1–3 years for most {city} homes. Shaded, south-facing, or coastal properties may need annual washing.

**Can waterblasting damage my cladding?**
Yes — high pressure can damage weatherboards, painted surfaces, and some cladding types. A professional will use appropriate pressure for your cladding. Soft washing is safer for older or more delicate surfaces.

---

*Related: [House Washing Cost NZ](/articles/house-washing-cost-nz/) | [Waterblasting Cost NZ](/articles/waterblasting-cost-nz/) | [Exterior House Painting Cost NZ](/articles/exterior-house-painting-cost-nz/)*
"""


# ── Locksmith ─────────────────────────────────────────────────────────────────

LOCK_RATES = {
    "auckland":     ("$120–$220", "$250–$500", "$180–$380"),
    "wellington":   ("$120–$220", "$250–$500", "$180–$380"),
    "christchurch": ("$100–$190", "$220–$450", "$160–$340"),
    "hamilton":     ("$90–$180",  "$200–$420", "$150–$320"),
    "tauranga":     ("$95–$185",  "$210–$430", "$155–$330"),
    "dunedin":      ("$85–$175",  "$190–$400", "$140–$300"),
}

def locksmith_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    callout, lockout, rekey = LOCK_RATES[city_key]

    return f"""---
title: "Locksmiths {city} 2026 — Call-Out Costs, Lock Change Prices and What to Expect"
description: "Locksmiths {city} 2026 — {city} locksmith call-out fees, lockout costs, lock replacement prices, after-hours rates, and how to find a reliable locksmith near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["locksmiths {city}", "locksmith {city}", "locksmith cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Whether you're locked out, need new locks after a break-in, or want to upgrade your home security, a {city} locksmith can help. Here's what locksmith services cost in {city} in 2026.

## {city} Locksmith Rates 2026

| Service | {city} typical cost |
|---|---|
| Call-out fee (weekday, business hours) | {callout} |
| After-hours / weekend call-out | $200–$400 |
| Lockout — open door (standard lock) | {lockout} |
| Lockout — after hours | $350–$700 |
| Lock re-key (per lock) | {rekey} |
| Lock replacement (standard deadbolt) | $200–$450 |
| Lock replacement (high-security) | $350–$800 |
| Deadbolt installation (new) | $250–$500 |
| Master key system (residential) | $500–$1,500 |
| Safe opening | $300–$800 |
| Car lockout | $150–$350 |
| Key cutting (standard) | $10–$40 per key |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## Common {city} Locksmith Situations

### Locked Out of Your Home
The most common callout. A locksmith can usually open a standard door lock non-destructively. Cost: {lockout}. If the lock must be drilled (damaged or very high-security): add $100–$300 for lock replacement.

**Tip:** Before calling a locksmith, check all windows and other doors — and ask a neighbour if they have a spare key. After-hours lockouts cost significantly more.

### Lock Change After Break-In or Lost Keys
If you've been burgled or lost your keys, changing or re-keying your locks is essential. Re-keying is cheaper than full replacement — the locksmith modifies the existing lock to use a new key. Cost per lock: {rekey}.

### Upgrading Home Security
Standard NZ residential locks are often low-security. Locksmiths can supply and install:
- Deadbolts (high-security, pick-resistant)
- Restricted key systems (keys can't be copied without authorisation)
- Smart locks (keypad, app-controlled)
- Window locks and door reinforcement

**Find {city} locksmiths:** [Locksmiths {city}](/trades/locksmiths/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does a locksmith cost in {city}?**
Call-out (business hours): {callout}. Lockout (open door): {lockout}. After-hours lockout: $350–$700.

**What should I do if I'm locked out in {city}?**
Check all entry points first. Call a {city} locksmith — keep a local number in your phone before you need it. After-hours callouts cost more, so it's worth confirming your costs before they arrive.

**How do I find a trustworthy locksmith in {city}?**
Use a locksmith from a reputable directory (like TradieTools NZ) with verifiable local reviews. Be wary of very cheap advertised rates — some charge large hidden fees on arrival.

---

*Related: [Locksmith Cost NZ](/articles/locksmith-cost-nz/) | [Handyman {city}](/articles/handyman-{city_key}-nz/)*
"""


# ── Carpet Layer ──────────────────────────────────────────────────────────────

CARPET_RATES = {
    "auckland":     ("$60–$130/m²", "$45–$95/m²", "$3,500–$8,000"),
    "wellington":   ("$60–$130/m²", "$45–$95/m²", "$3,500–$8,000"),
    "christchurch": ("$55–$115/m²", "$40–$85/m²", "$3,000–$7,000"),
    "hamilton":     ("$50–$110/m²", "$38–$80/m²", "$2,800–$6,500"),
    "tauranga":     ("$52–$115/m²", "$40–$82/m²", "$3,000–$6,800"),
    "dunedin":      ("$48–$105/m²", "$35–$78/m²", "$2,600–$6,000"),
}

def carpet_article(city_key):
    c = CITIES[city_key]
    city = c["name"]
    region = c["region"]
    supply_lay, lay_only, full_home = CARPET_RATES[city_key]

    local_map = {
        "auckland":     "Auckland's diverse housing from villas to townhouses means carpet layers work across a wide range of property types. Wool carpet is popular in premium Auckland homes; nylon and polyester are the practical choice for families and rentals.",
        "wellington":   "Wellington's cold winters make carpet especially valued — hard floors can be cold underfoot in older Wellington homes. Wool blends are popular for their warmth and durability.",
        "christchurch": "Christchurch's post-earthquake rebuild and active renovation market keep carpet layers busy. Many Christchurch homeowners are updating their flooring as part of broader renovations.",
        "hamilton":     "Hamilton's strong residential market — both new builds and renovation — drives steady carpet demand. Practical, durable carpets are popular in family homes and the rental sector.",
        "tauranga":     "Tauranga's lifestyle market favours high-quality carpets in living areas paired with hard flooring in kitchens and outdoor spaces. The retiree population drives premium wool carpet demand.",
        "dunedin":      "Dunedin's cold winters make carpet the dominant flooring choice in most rooms. The large student rental market drives demand for durable, easy-clean carpets in rental properties.",
    }
    local = local_map.get(city_key, f"{city} has steady demand for carpet laying across residential new builds, renovation, and rental properties.")

    return f"""---
title: "Carpet Layers {city} 2026 — Carpet Installation Costs and What to Expect"
description: "Carpet layers {city} 2026 — {city} carpet installation cost, supply and lay prices, carpet types for NZ homes, and how to find a reliable carpet layer near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["carpet layers {city}", "carpet installation {city}", "carpet cost {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

New carpet transforms a room — and {city} has plenty of experienced carpet layers for everything from a single bedroom to a full home. Here's what carpet installation costs in {city} in 2026.

## {city} Carpet Installation Costs 2026

| Service | {city} typical cost |
|---|---|
| Supply and lay — budget carpet (per m²) | $45–$80/m² |
| Supply and lay — mid-range carpet (per m²) | {supply_lay} |
| Supply and lay — premium wool (per m²) | $120–$220/m² |
| Lay only (customer-supplied carpet, per m²) | {lay_only} |
| Underlay (per m², standard) | $8–$20/m² |
| Underlay (per m², premium) | $20–$45/m² |
| Full home carpet (3-bed, mid-range) | {full_home} |
| Single bedroom (12m², mid-range) | $700–$1,800 |
| Lounge (20m², mid-range) | $1,200–$3,000 |
| Carpet removal and disposal (per m²) | $8–$18/m² |
| Re-stretching / repair (per room) | $150–$400 |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Carpet Market

{local}

## Choosing Carpet for {city} Homes

**Wool:** Premium NZ product — naturally stain-resistant, durable, warm, and fire-resistant. Higher upfront cost but long lifespan. Best for living areas and bedrooms in family homes.

**Nylon (PA):** The most popular synthetic carpet in NZ. Excellent durability and stain resistance. Good value for high-traffic areas, family homes, and rental properties.

**Polyester (PET/PTT):** Soft, good colour range, and increasingly recycled-content options. Less durable than nylon in very high traffic areas but excellent value for bedrooms.

**Loop pile vs cut pile:** Loop pile (Berber) is durable and hides footprints. Cut pile (twist, plush) is softer and more luxurious. Twist pile is the most practical all-rounder for NZ homes.

## Underlay — Don't Skip It

Good underlay makes carpet last longer, feel more comfortable underfoot, and provide better thermal and acoustic insulation. In {city}, a quality underlay (8–12mm foam or rubber) adds $10–$30/m² but significantly extends carpet life and warmth.

**Find {city} carpet layers:** [Carpet Layers {city}](/trades/carpet-layers/?location={city_key}) | [Post a Job Free](/post-job/)

---

## Frequently Asked Questions

**How much does carpet installation cost in {city}?**
Mid-range supply and lay: {supply_lay}/m². Full 3-bed home: {full_home}. Lay only (your carpet): {lay_only}/m².

**How long does carpet last?**
Budget carpet: 5–10 years. Mid-range nylon: 10–15 years. Quality wool: 15–25+ years. Lifespan depends heavily on traffic and maintenance.

**Do I need underlay for new carpet?**
Yes — always. Underlay provides comfort, extends carpet life, and improves thermal and acoustic performance. Most carpet installations include underlay; confirm it's in your quote.

---

*Related: [Carpet Installation Cost NZ](/articles/carpet-installation-cost-nz/) | [Timber Flooring Cost NZ](/articles/timber-flooring-cost-nz/) | [Vinyl Flooring Cost NZ](/articles/vinyl-flooring-cost-nz/)*
"""


# ── Article list ───────────────────────────────────────────────────────────────

ARTICLES = [
    # Handyman — all cities
    ("handyman-auckland-nz",          lambda: handyman_article("auckland")),
    ("handyman-wellington-nz",        lambda: handyman_article("wellington")),
    ("handyman-christchurch-nz",      lambda: handyman_article("christchurch")),
    ("handyman-hamilton-nz",          lambda: handyman_article("hamilton")),
    ("handyman-tauranga-nz",          lambda: handyman_article("tauranga")),
    ("handyman-dunedin-nz",           lambda: handyman_article("dunedin")),
    ("handyman-napier-nz",            lambda: handyman_article("napier")),
    ("handyman-new-plymouth-nz",      lambda: handyman_article("new-plymouth")),
    ("handyman-palmerston-north-nz",  lambda: handyman_article("palmerston-north")),
    ("handyman-nelson-nz",            lambda: handyman_article("nelson")),
    ("handyman-rotorua-nz",           lambda: handyman_article("rotorua")),
    # Painter gap fills
    ("painters-new-plymouth-nz",      lambda: painter_article("new-plymouth")),
    ("painters-palmerston-north-nz",  lambda: painter_article("palmerston-north")),
    ("painters-nelson-nz",            lambda: painter_article("nelson")),
    ("painters-rotorua-nz",           lambda: painter_article("rotorua")),
    # House washers
    ("house-washer-auckland-nz",      lambda: housewash_article("auckland")),
    ("house-washer-wellington-nz",    lambda: housewash_article("wellington")),
    ("house-washer-christchurch-nz",  lambda: housewash_article("christchurch")),
    ("house-washer-hamilton-nz",      lambda: housewash_article("hamilton")),
    ("house-washer-tauranga-nz",      lambda: housewash_article("tauranga")),
    ("house-washer-dunedin-nz",       lambda: housewash_article("dunedin")),
    # Locksmiths
    ("locksmith-auckland-nz",         lambda: locksmith_article("auckland")),
    ("locksmith-wellington-nz",       lambda: locksmith_article("wellington")),
    ("locksmith-christchurch-nz",     lambda: locksmith_article("christchurch")),
    ("locksmith-hamilton-nz",         lambda: locksmith_article("hamilton")),
    ("locksmith-tauranga-nz",         lambda: locksmith_article("tauranga")),
    ("locksmith-dunedin-nz",          lambda: locksmith_article("dunedin")),
    # Carpet layers
    ("carpet-layer-auckland-nz",      lambda: carpet_article("auckland")),
    ("carpet-layer-wellington-nz",    lambda: carpet_article("wellington")),
    ("carpet-layer-christchurch-nz",  lambda: carpet_article("christchurch")),
    ("carpet-layer-hamilton-nz",      lambda: carpet_article("hamilton")),
    ("carpet-layer-tauranga-nz",      lambda: carpet_article("tauranga")),
    ("carpet-layer-dunedin-nz",       lambda: carpet_article("dunedin")),
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
