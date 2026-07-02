#!/usr/bin/env python3
"""
Wave 11 SEO content generator — TradieTools NZ
Gap fills: pool builder smaller cities
New trade: pergola builder (all 11 cities)
National cost guides: high-value long-tail searches
Run: python3 generate_wave11.py
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

ALL_CITIES  = list(CITIES.keys())
SMALL_CITIES = ["napier","new-plymouth","palmerston-north","nelson","rotorua"]
MAIN_CITIES  = ["auckland","wellington","christchurch","hamilton","tauranga","dunedin"]

# ── Pool Builder (smaller cities) ─────────────────────────────────────────────

POOL_SMALL = {
    "napier":           ("$45,000–$82,000", "$82,000–$150,000+", "$22,000–$45,000", "Napier's warm Hawke's Bay summers make pools well-used from November through April. The art deco city's lifestyle market values outdoor entertaining, and a pool can be a strong addition to higher-value Hawke's Bay properties."),
    "new-plymouth":     ("$45,000–$82,000", "$82,000–$150,000+", "$22,000–$45,000", "New Plymouth's coastal lifestyle and warm summers make pools popular. The mountain and sea backdrop means well-designed outdoor spaces with pools are highly valued in the Taranaki property market."),
    "palmerston-north": ("$42,000–$78,000", "$78,000–$145,000+", "$20,000–$42,000", "Palmerston North's hot summers make pools popular despite the shorter season compared to northern NZ. The Manawatu's large suburban sections provide good space for pool installation."),
    "nelson":           ("$45,000–$82,000", "$82,000–$150,000+", "$22,000–$45,000", "Nelson's exceptional sunshine record — consistently one of NZ's sunniest cities — makes it one of the best locations in NZ for pool ROI. The long warm season from October through April gives Nelson pools excellent utilisation."),
    "rotorua":          ("$42,000–$78,000", "$78,000–$145,000+", "$20,000–$42,000", "Rotorua's tourism market means pools add significant value to short-term rental properties. The city's warm summers make pools well-used. Geothermal areas may have ground conditions that affect pool construction — local builders know what to expect."),
}

def pool_small(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    concrete, premium, fibreglass, local = POOL_SMALL[city_key]
    return f"""---
title: "Pool Builders {city} 2026 — Swimming Pool Costs, Types and What to Expect"
description: "Pool builders {city} 2026 — {city} swimming pool installation costs, concrete vs fibreglass prices, consent requirements, and how to find a reliable pool builder near you."
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
| Fibreglass pool (6–8m, basic) | {fibreglass} |
| Concrete pool (standard, 6–8m) | {concrete} |
| Concrete pool (custom, premium) | {premium} |
| Above-ground pool (steel/resin) | $4,000–$15,000 |
| Spa pool / hot tub | $8,000–$30,000 |
| Pool heat pump (add-on) | $4,500–$9,000 |
| Pool fencing (compliant, per m linear) | $380–$950/m |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Pool Market

{local}

## Concrete vs Fibreglass

**Fibreglass:** Pre-made shell, faster install (6–8 weeks), lower maintenance, lower upfront cost. Limited shapes and sizes.
**Concrete:** Any shape and size, longer lifespan (50+ years), higher cost and longer build (3–6 months), needs resurfacing every 10–15 years.

## Consent Requirements

All pools over 400mm deep require building consent from {region} Council and compliant pool fencing (NZ Building Code Clause F9 — 1.2m min height, self-latching gates). Non-compliant fencing is a serious liability risk.

**Find {city} pool builders:** [Pool Builders {city}](/trades/pool-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

*Related: [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/)*
"""


# ── Pergola Builder ───────────────────────────────────────────────────────────

PERGOLA_DATA = {
    "auckland":         ("$8,500–$22,000", "$22,000–$55,000+", "Auckland's subtropical climate and long outdoor season make pergolas one of the most popular outdoor additions. A louvred pergola with automated roof panels lets Auckland homeowners use their outdoor space year-round, even in rain."),
    "wellington":       ("$9,000–$23,000", "$23,000–$58,000+", "Wellington's wind is the key challenge for pergola design — solid posts, robust connections, and wind-resistant roof panels are essential. Many Wellington pergolas incorporate solid side panels for wind shelter, creating an outdoor room that's usable even in the famous southerly."),
    "christchurch":     ("$7,800–$20,000", "$20,000–$50,000+", "Christchurch's hot, dry summers make shaded outdoor spaces very desirable. A pergola with shade cloth or louvres creates a comfortable outdoor dining and entertaining area through the intense Canterbury summer."),
    "hamilton":         ("$7,500–$19,000", "$19,000–$48,000+", "Hamilton's hot humid summers and occasional heavy rain make a covered pergola a popular addition. The Waikato's outdoor lifestyle and large suburban sections give good space for pergola installations."),
    "tauranga":         ("$7,800–$20,000", "$20,000–$50,000+", "Tauranga's beach and lifestyle culture makes quality outdoor living essential. Louvred pergolas are particularly popular in Bay of Plenty — the automated roof panels handle the region's frequent afternoon showers."),
    "dunedin":          ("$7,000–$18,000", "$18,000–$45,000+", "Dunedin's cold, wet climate makes a fully enclosed pergola more valuable than an open structure. Insulated roofing and side panels create an outdoor room usable through the Otago winter."),
    "napier":           ("$7,800–$20,000", "$20,000–$50,000+", "Napier's warm sunny climate is ideal for outdoor pergolas. Hawke's Bay's food and wine culture makes outdoor entertaining spaces a high priority — a quality pergola complements the region's alfresco lifestyle."),
    "new-plymouth":     ("$7,800–$20,000", "$20,000–$50,000+", "New Plymouth's coastal lifestyle and westerly weather makes a sheltered pergola particularly valuable. Designs that provide wind protection while capturing the summer sun are popular in Taranaki."),
    "palmerston-north": ("$7,500–$19,000", "$19,000–$48,000+", "Palmerston North's windy conditions and variable weather make a covered, wind-protected pergola a practical choice. A well-designed pergola extends outdoor living by several months in the Manawatu."),
    "nelson":           ("$7,800–$20,000", "$20,000–$50,000+", "Nelson's exceptional sunshine and outdoor lifestyle culture make pergolas a natural addition. The long Nelson summer (10+ months of usable outdoor weather) gives pergolas outstanding value — possibly the best ROI of any NZ city."),
    "rotorua":          ("$7,500–$19,000", "$19,000–$48,000+", "Rotorua's outdoor lifestyle and tourism influence make quality outdoor spaces valuable. A pergola extending the living space toward the garden or lake view is a popular addition in Rotorua's higher-end properties."),
}

def pergola_article(city_key):
    c = CITIES[city_key]
    city, region = c["name"], c["region"]
    standard, premium, local = PERGOLA_DATA[city_key]
    return f"""---
title: "Pergola Builders {city} 2026 — Pergola Costs, Types and What to Expect"
description: "Pergola builders {city} 2026 — {city} pergola costs, louvred vs shade sail vs timber prices, consent requirements, and how to find a reliable pergola builder near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["pergola builders {city}", "pergola cost {city}", "pergola {city}", "{region}", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

{local} Here's what pergola builders charge in {city} in 2026.

## {city} Pergola Costs 2026

| Pergola type | {city} typical cost (supply + install) |
|---|---|
| Timber pergola (open frame, basic) | $4,500–$12,000 |
| Aluminium pergola (fixed louvres) | $8,000–$18,000 |
| Louvred pergola (motorised, standard) | {standard} |
| Louvred pergola (premium, with lighting/heaters) | {premium} |
| Shade sail (supply + posts + install) | $2,500–$7,500 |
| Polycarbonate roof pergola | $6,000–$15,000 |
| Insulated panel roof pergola | $9,000–$24,000 |
| Decking beneath pergola (per m²) | $1,500–$3,000/m² |

*All prices GST inclusive. {c["rate_adj"].capitalize()}.*

## {city} Pergola Market

{local}

## Pergola Types Compared

**Open timber frame:** Most affordable. Traditional look. Provides partial shade only — no rain protection. Requires regular sealing/painting.

**Polycarbonate roof:** Budget rain cover. Provides full shelter but can be hot in summer (clear panels let heat through). Tinted panels help.

**Insulated panel roof:** Full shelter, excellent thermal performance. Feels like an extension of the house. Popular for year-round outdoor rooms.

**Louvred (fixed):** Aluminium louvres at a fixed angle — partial shade and rain protection without full closure.

**Louvred (motorised):** Aluminium louvres that open and close with a remote. Open for sun, close for rain. Most popular premium option in NZ right now. Often includes integrated LED lighting, heating strips, and rain sensors.

## Do I Need Consent for a Pergola in {city}?

**Generally exempt** if:
- The pergola is detached (not attached to the house)
- Under 20m² in area
- Under 2.5m in height

**Consent required** if:
- Attached to the house (becomes a building work)
- Over 20m² or over 2.5m high
- Includes electrical work (lighting, heaters)

Always confirm with {region} Council — exempt status depends on your specific zone and section. A good pergola builder will advise.

**Find {city} pergola builders:** [Deck Builders {city}](/trades/deck-builders/?location={city_key}) | [Post a Job Free](/post-job/)

---

**How much does a pergola cost in {city}?**
Motorised louvred pergola (standard): {standard}. Open timber frame: $4,500–$12,000. Polycarbonate roof: $6,000–$15,000.

*Related: [Deck Builders {city}](/articles/deck-builder-{city_key}-nz/) | [Landscapers {city}](/articles/landscaper-{city_key}-nz/)*
"""


# ── National Cost Guides ──────────────────────────────────────────────────────

def retaining_wall_article():
    return f"""---
title: "Retaining Wall Cost NZ 2026 — Timber, Concrete Block and Stone Prices"
description: "Retaining wall cost NZ 2026 — timber sleeper, concrete block, gabion and stone retaining wall costs, height limits before consent, and how to find a reliable builder near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["retaining wall cost NZ", "retaining wall NZ", "retaining wall price NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Retaining walls are one of the most common landscaping jobs in hilly NZ. Here's what different types cost in 2026.

## Retaining Wall Cost NZ 2026

| Type | Cost per m² (supply + install) | Notes |
|---|---|---|
| Timber sleeper (H5 treated) | $350–$750/m² | Most common, 10–20yr lifespan |
| Timber sleeper (hardwood) | $480–$950/m² | 25–40yr lifespan |
| Concrete block (besser block) | $480–$950/m² | Durable, engineered for height |
| Mortared stone / rock | $550–$1,200/m² | Premium natural look |
| Dry-stack stone | $420–$900/m² | Permeable, no mortar |
| Gabion baskets (rock-filled) | $380–$780/m² | Good drainage, modern look |
| Concrete poured (engineered) | $650–$1,400/m² | For larger/critical retaining |
| Timber crib wall | $320–$680/m² | Good for large informal areas |

*All prices GST inclusive. Auckland and Wellington typically at the higher end. Height, soil type, and drainage requirements heavily affect cost.*

## What Drives Retaining Wall Cost?

**Height:** The biggest cost driver. A 2m wall needs far more engineering than a 0.8m wall — soil pressure increases with the square of height.

**Soil type:** Clay soil (common in Auckland) exerts more lateral pressure than sandy soil. Clay behind a wall needs robust drainage to prevent hydrostatic pressure buildup.

**Drainage:** All retaining walls need drainage behind them — gravel backfill and agricultural drain pipe. If drainage is poor, water pressure will eventually cause wall failure.

**Access:** Walls on steep sites or with restricted machinery access cost more.

## Consent Requirements for Retaining Walls

Under NZ Building Code, retaining walls generally require building consent if they:

- Are **over 1.5m high** in most situations
- Retain soil next to a building, pool, or public space (lower thresholds may apply)
- Are on a boundary near a neighbour's property

**Under 1.5m:** Usually exempt from consent but must still be structurally sound. Many councils have specific rules — check before building.

**Engineered design:** Walls over 1.5m or in challenging conditions should be designed by a structural or geotechnical engineer. The cost of engineering ($800–$2,500) is worthwhile — a failed retaining wall can cause significant property damage.

## Choosing the Right Type

| Situation | Recommended type |
|---|---|
| Garden terracing, under 1m | Timber sleepers or dry-stack stone |
| House site cut, 1–2m | Timber sleepers (H5) or concrete block |
| Over 2m or near building | Concrete block or engineered concrete |
| Aesthetic focal point | Stone, gabion, or hardwood |
| High water table or clay soil | Concrete block with robust drainage |
| Rural / informal | Crib wall or gabion |

**Find landscapers and builders:** [Landscapers Near You](/trades/landscapers/) | [Builders Near You](/trades/builders/) | [Post a Job Free](/post-job/)

---

**How much does a retaining wall cost in NZ?**
Timber sleeper: $350–$750/m². Concrete block: $480–$950/m². Stone: $550–$1,200/m².

**Do I need consent for a retaining wall in NZ?**
Generally yes for walls over 1.5m. Check with your local council — rules vary by zone and proximity to boundaries or buildings.

*Related: [Landscaping Cost NZ](/articles/landscaping-cost-nz/) | [Concrete Driveway Cost NZ](/articles/concrete-driveway-cost-nz/)*
"""


def interior_painting_article():
    return f"""---
title: "Interior Painting Cost NZ 2026 — Room by Room Prices and What to Expect"
description: "Interior painting cost NZ 2026 — cost to paint a room, full house interior painting prices, painter hourly rates, paint quality guide, and how to get the best result."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["interior painting cost NZ", "cost to paint a room NZ", "interior painter NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Interior painting transforms a home faster than almost any other renovation. Here's what it costs in NZ in 2026.

## Interior Painting Cost NZ 2026

### Room-by-Room Prices (Labour + Paint)

| Room | Typical NZ cost |
|---|---|
| Bedroom (standard, 2 coats) | $600–$1,400 |
| Living room (standard, 2 coats) | $800–$2,000 |
| Kitchen (including ceiling) | $700–$1,600 |
| Bathroom (incl. moisture-resistant paint) | $650–$1,400 |
| Hallway / corridor | $400–$900 |
| Full 3-bed home (walls + ceilings) | $5,500–$12,000 |
| Full 4-bed home (walls + ceilings) | $7,500–$16,000 |
| Ceilings only (per room) | $200–$550 |
| Trim / skirting / architraves (per room) | $150–$380 |

### Hourly Rates

| | Typical NZ rate |
|---|---|
| Painter hourly rate | $65–$130/hr |
| Day rate (painter) | $500–$950/day |

*All prices GST inclusive. Auckland and Wellington at the higher end. Rates vary with ceiling height, wall condition, and number of colours.*

## What Affects the Cost?

**Ceiling height:** Stud walls over 2.7m cost more — extra reach required, more paint used.

**Wall condition:** New Gib (smooth) paints cleanly. Walls with holes, cracks, or texture need prep work — filling, sanding, priming. Good prep is 30–40% of a quality paint job.

**Number of coats:** Two coats is standard for a quality finish. Drastic colour changes (dark to white, or vice versa) may need three coats.

**Number of colours:** Each colour change means masking — which takes time. Feature walls and multi-colour schemes add cost.

**Furniture:** Painter will move light items and cover floors. Heavily furnished rooms take longer.

## Paint Quality Guide for NZ Homes

| Grade | NZ brands | Best for |
|---|---|---|
| Entry-level | Resene, Dulux basic ranges | Rental properties, budget renos |
| Mid-range | Resene Lumbersider, Dulux Wash&Wear | Most NZ homes |
| Premium | Resene SpaceCote, Dulux Aquanamel | High-traffic areas, feature walls |
| Bathroom/kitchen | Resene Zylone Sheen, moisture-resistant ranges | Wet areas |

**Resene** is NZ's most popular paint brand — widely used by professional painters. **Dulux** is also common. Both offer excellent quality at mid-range price points.

## DIY vs Professional

**DIY saves:** 40–60% of the cost (labour). A room's paint and supplies: $100–$250.

**Professional results in:** Straighter lines, better coverage, faster completion, proper prep. Professionals charge for quality — cutting in ceilings and architraves cleanly takes practice.

**When to hire a professional:** Feature ceilings, stairwells, high studs, or when you need it done quickly and to a high standard.

**Find NZ painters:** [Painters Near You](/trades/painters/) | [Post a Job Free](/post-job/)

---

**How much does it cost to paint a room in NZ?**
Standard bedroom (labour + paint): $600–$1,400. Full 3-bed home interior: $5,500–$12,000.

*Related: [Painters Auckland](/articles/painter-auckland-nz/) | [Exterior House Painting Cost NZ](/articles/exterior-house-painting-cost-nz/)*
"""


def exterior_painting_article():
    return f"""---
title: "Exterior House Painting Cost NZ 2026 — Full Price Guide"
description: "Exterior house painting cost NZ 2026 — cost to paint the outside of a house, preparation costs, paint types for NZ weather, and how to find a reliable painter near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["exterior house painting cost NZ", "exterior painting NZ", "house painting cost NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Exterior painting protects your home from NZ's demanding weather. Here's what it costs and what to look for in a quality job.

## Exterior House Painting Cost NZ 2026

| Home type | Typical NZ cost (full exterior) |
|---|---|
| Small home / unit (under 120m²) | $4,500–$9,000 |
| Standard 3-bed home (120–180m²) | $7,000–$14,000 |
| Large 4+ bed home (180–250m²) | $10,000–$20,000 |
| Very large / two-storey (250m²+) | $15,000–$35,000+ |
| Trim / fascia / soffits only | $1,800–$4,500 |
| Deck staining / oiling (per m²) | $18–$42/m² |
| Weatherboard preparation (sanding, per m²) | $12–$28/m² |

*All prices GST inclusive. Auckland and Wellington at the higher end. Prices vary significantly based on home condition, height, and preparation required.*

## What's Included in a Good Exterior Paint Job

**Preparation (30–40% of a quality job):**
- Wash the exterior (mould treatment and rinse)
- Sand and scrape loose paint
- Fill cracks and gaps with flexible filler
- Prime bare wood and repaired areas
- Mask windows, gutters, paths

**Painting:**
- Two coats minimum on walls
- One to two coats on trim
- Back-roll after spraying (ensures paint penetrates weatherboard grain)

**A painter who skips preparation will produce a job that peels within 2–3 years.** Always ask what preparation is included.

## Best Exterior Paints for NZ Conditions

NZ's combination of UV intensity, coastal salt air, humidity, and temperature extremes demands quality exterior paint.

| Product | Best for | Notes |
|---|---|---|
| Resene X-200 | Most NZ homes | Excellent durability, 10yr guarantee |
| Resene Lumbersider | Timber weatherboards | Penetrating, flexible |
| Dulux Weathershield | Masonry and fibre cement | Very good UV resistance |
| Resene Hi-Glo | High-gloss trim | Long-lasting sheen |
| Wattyl Solagard | Budget option | Good for rentals |

**Gloss level:** Walls typically in low-sheen or satin. Trim in semi-gloss or gloss. High-gloss highlights surface imperfections — avoid on rough or patchy surfaces.

## How Often Does Exterior Paint Need Replacing?

| Paint quality | NZ lifespan |
|---|---|
| Budget paint, poor prep | 4–6 years |
| Mid-range paint, good prep | 8–12 years |
| Premium paint, excellent prep | 12–18 years |

Northern NZ (Auckland, Bay of Plenty) — higher UV and humidity shortens paint life. Southern NZ (Otago, Southland) — freeze-thaw cycles can cause paint to crack faster.

**Find NZ painters:** [Painters Near You](/trades/painters/) | [Post a Job Free](/post-job/)

---

**How much does exterior house painting cost in NZ?**
Standard 3-bed home: $7,000–$14,000. Small home/unit: $4,500–$9,000. Large 4-bed: $10,000–$20,000.

**How often should I repaint my house exterior in NZ?**
Every 8–12 years with quality paint and preparation. Coastal or northern NZ properties may need repainting every 6–10 years.

*Related: [Painters Near You](/trades/painters/) | [Interior Painting Cost NZ](/articles/interior-painting-cost-nz/) | [House Washing Cost NZ](/articles/house-washing-cost-nz/)*
"""


def bathroom_tiling_article():
    return f"""---
title: "Bathroom Tiling Cost NZ 2026 — Floor, Wall and Shower Tile Prices"
description: "Bathroom tiling cost NZ 2026 — cost to tile a bathroom floor, shower tiling prices, wall tile installation rates, tile size effect on cost, and how to find a reliable tiler near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["bathroom tiling cost NZ", "bathroom tile cost NZ", "shower tiling cost NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Tiling is the most visually impactful part of a bathroom renovation. Here's what it costs in NZ in 2026.

## Bathroom Tiling Cost NZ 2026

| Service | Typical NZ cost |
|---|---|
| Floor tiling — budget tile (per m², labour only) | $65–$120/m² |
| Floor tiling — mid-range tile (per m², supply + install) | $120–$280/m² |
| Wall tiling — standard (per m², supply + install) | $110–$260/m² |
| Shower tiling — full cubicle (supply + install) | $2,200–$5,500 |
| Niche / shelf in shower (per niche) | $250–$600 |
| Splashback tiling — bathroom (per m²) | $130–$280/m² |
| Full bathroom tiling (floor + walls, 4m²) | $3,500–$8,500 |
| Large format tile premium (600×600mm+) | add 20–40% |
| Heated floor tile installation | add $450–$900 |
| Tile removal (per m²) | $25–$55/m² |
| Grout cleaning / regrouting (per m²) | $45–$95/m² |

*All prices GST inclusive. Auckland and Wellington at the higher end.*

## Tile Sizes and Cost Impact

**Small tiles (mosaic, subway under 100×200mm):**
More cuts, more grout lines = more labour time. Cost is 20–40% higher per m² than standard tiles.

**Standard tiles (200×200 to 400×600mm):**
Most efficient to lay. Best value for labour.

**Large format (600×600mm and above):**
Needs a very flat substrate (extra prep cost) and careful cutting. Labour premium of 20–40% but stunning visual result. Trend in premium NZ bathrooms 2024–2026.

## Tile Selection Guide for NZ Bathrooms

| Area | Recommended tile | Why |
|---|---|---|
| Shower floor | Matt or textured, R10+ slip rating | Safety — wet underfoot |
| Bathroom floor | Matt or low-sheen, R10 slip rating | Wet when exiting shower |
| Shower walls | Rectified (straight-edged) | Tight grout lines, premium look |
| Feature wall | Large format, pattern, or stone look | Visual impact |
| Splashback | Any glazed tile | Easy to clean |

**Rectified tiles** (machine-cut edges) allow tighter grout lines (1–2mm) for a seamless look. Non-rectified tiles need wider grout lines (3–5mm). Rectified tiles are more expensive but worth it in shower areas.

## Waterproofing First

Tiles alone do not waterproof a bathroom. The substrate behind the tiles must be waterproofed — typically a liquid membrane or waterproof board (Dens Shield, Cempanel, etc.) in shower areas.

**NZ Building Code requires:**
- Waterproofing behind all shower and bath areas to at least 1,800mm height
- Compliance certificate from a Licensed Building Practitioner
- Waterproofing tested before tiling begins

Never tile over un-waterproofed substrate in wet areas — moisture behind tiles causes rot, mould, and structural damage.

**Find NZ tilers:** [Tilers Near You](/trades/tilers/) | [Post a Job Free](/post-job/)

---

**How much does it cost to tile a bathroom in NZ?**
Full bathroom (floor + walls, ~4m²): $3,500–$8,500 supply + install. Shower cubicle (supply + install): $2,200–$5,500.

*Related: [Tilers Auckland](/articles/tiler-auckland-nz/) | [Bathroom Renovation Cost NZ](/articles/bathroom-renovation-cost-nz/)*
"""


def new_build_article():
    return f"""---
title: "New Home Build Cost NZ 2026 — Per m² Prices, What's Included and How to Budget"
description: "New home build cost NZ 2026 — cost per m² to build a house in NZ, turnkey vs bare build pricing, what's included, build time, and how to find a reliable builder near you."
image: "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["new home build cost NZ", "cost to build a house NZ", "new build NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Building a new home in NZ is a major financial commitment. Here's what it costs in 2026 and how to budget realistically.

## New Home Build Cost NZ 2026

### Build Cost per m² (house footprint, excl. land)

| Build type | Cost per m² (NZ average) |
|---|---|
| Basic spec build (entry-level) | $2,200–$2,800/m² |
| Standard quality (most NZ new builds) | $2,800–$3,600/m² |
| Mid-to-high quality | $3,600–$4,500/m² |
| Premium / architectural | $4,500–$7,000+/m² |
| Auckland premium (highest costs) | Add 15–25% |

### Total Build Cost by Home Size

| Home size | Standard quality | Premium quality |
|---|---|---|
| 120m² (3-bed, 1-bath) | $336,000–$432,000 | $540,000–$840,000 |
| 160m² (3-bed, 2-bath) | $448,000–$576,000 | $720,000–$1,120,000 |
| 200m² (4-bed, 2-bath) | $560,000–$720,000 | $900,000–$1,400,000 |
| 250m² (4-bed, 3-bath) | $700,000–$900,000 | $1,125,000–$1,750,000 |

*All prices GST inclusive, house build only — does not include land, site costs, or landscaping.*

## What's Included (and Not) in These Prices

### Typically Included

- All framing, roofing, cladding
- Windows and external doors
- Electrical, plumbing, and gas rough-in
- Insulation (ceiling, walls, underfloor)
- Internal linings (Gib/plasterboard)
- Internal doors
- Kitchen (standard specification)
- Bathrooms (standard specification)
- Painting (internal walls)
- Concrete floor slab or timber floor
- Driveway (basic concrete)

### Typically Not Included (Budget Separately)

| Item | Typical NZ cost |
|---|---|
| Land | $150,000–$800,000+ depending on location |
| Section preparation / earthworks | $15,000–$80,000+ |
| Architect / designer fees | $15,000–$60,000 |
| Resource consent (if required) | $3,000–$20,000 |
| Building consent | $5,000–$20,000 |
| Landscaping and fencing | $15,000–$80,000 |
| Driveway upgrade | $5,000–$18,000 |
| Deck / outdoor area | $15,000–$50,000 |

## Turnkey vs Bare Build

**Turnkey:** Builder manages everything — design, consents, build, and handover. You get a completed home ready to move in. Higher total cost, less involvement required.

**Bare build (owner builds or project manages):** You contract each trade directly. Can save 10–20% of build cost but requires significant time and expertise. Any errors you manage are your responsibility.

**Volume builder:** Companies like G.J. Gardner, Signature Homes, Jennian use standardised designs and bulk buying power to reduce costs. Good value but limited customisation.

**Custom architect-designed:** Highest quality and flexibility. Architect fees add 8–15% of build cost but result in a home designed specifically for your site and needs.

## Building in NZ — Key Consent Steps

1. **Resource consent** (if required — depends on zone and design)
2. **Building consent** from your local council (mandatory)
3. **Foundation inspection** before pouring concrete
4. **Frame inspection** before lining
5. **Pre-line inspection** (plumbing, electrical, insulation)
6. **Code Compliance Certificate (CCC)** at completion — essential for resale and finance

Building without consent is illegal and creates serious issues at resale. Your builder will manage consents on a turnkey build.

**Find NZ builders:** [Builders Near You](/trades/builders/) | [Post a Job Free](/post-job/)

---

**How much does it cost to build a house in NZ in 2026?**
Standard quality: $2,800–$3,600/m². A 160m² 3-bed home: $448,000–$576,000 build cost (excl. land and site costs).

**How long does building a house take in NZ?**
Standard new build: 6–12 months from consent to handover. Custom/architectural: 12–24 months.

*Related: [Builders Auckland](/articles/builder-auckland-nz/) | [Builder Pricing Guide NZ](/articles/builder-pricing-guide-nz-2026/)*
"""


def asphalt_driveway_article():
    return f"""---
title: "Asphalt Driveway Cost NZ 2026 — Prices, vs Concrete, and What to Expect"
description: "Asphalt driveway cost NZ 2026 — asphalt vs concrete driveway costs, pricing per m², maintenance costs, lifespan, and how to find a reliable driveway contractor near you."
image: "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=630&fit=crop&auto=format"
date: {TODAY}
tags: ["asphalt driveway cost NZ", "asphalt driveway NZ", "tarmac driveway NZ", "NZ", "2026"]
author: "TradieTools NZ"
draft: false
---

Asphalt (tarmac) driveways are a popular choice in NZ for their balance of cost, durability, and kerb appeal. Here's what they cost in 2026.

## Asphalt Driveway Cost NZ 2026

| Service | Typical NZ cost |
|---|---|
| Asphalt driveway (per m², supply + lay) | $60–$130/m² |
| Standard single car driveway (30m²) | $1,800–$3,900 |
| Standard double car driveway (50m²) | $3,000–$6,500 |
| Long driveway (100m²) | $6,000–$13,000 |
| Sub-base preparation (per m²) | $18–$45/m² |
| Old concrete / asphalt removal (per m²) | $25–$55/m² |
| Edging / kerbing (per m linear) | $35–$75/m |
| Asphalt sealing / resealing (per m²) | $8–$22/m² |
| Crack repair (per linear metre) | $25–$65/m |

*All prices GST inclusive. Auckland at the higher end. Minimum job sizes apply — very small jobs cost more per m².*

## Asphalt vs Concrete Driveway

| | Asphalt | Concrete |
|---|---|---|
| Cost per m² | $60–$130 | $100–$210 |
| Installation time | 1–2 days (usable next day) | 1–2 days + 7 days curing |
| Lifespan | 20–30 years | 25–40 years |
| Maintenance | Reseal every 3–5 years | Low maintenance |
| Repairs | Easy to patch | Harder to patch invisibly |
| Appearance | Black / dark grey | Light grey |
| Hot weather | Can soften slightly | No issue |
| Cold weather | Flexible, handles frost well | Can crack if poorly laid |

**Asphalt is better for:** Tighter budgets, faster installation, cold southern NZ climates, long rural driveways.
**Concrete is better for:** Premium appearance, higher traffic, steeper driveways (better grip and won't soften in sun).

## Sub-Base — The Critical Foundation

Driveway failure almost always comes back to inadequate sub-base preparation:

- Minimum 150mm compacted AP20 (aggregate base) required
- Soft or unstable ground needs deeper sub-base or geotextile fabric
- Poor drainage causes premature failure — ensure sub-base drains away from the house

A quality asphalt contractor will dig out, compact the sub-grade, then lay compacted aggregate before laying asphalt. Shortcuts here mean your driveway fails in 5–10 years instead of 20–30.

## Asphalt Thickness

- **Residential driveway:** 40–50mm asphalt over 100–150mm compacted base
- **Heavy vehicles (trucks, RVs):** 50–75mm asphalt over 200mm+ compacted base

**Find driveway contractors:** [Concreters Near You](/trades/concreters/) | [Post a Job Free](/post-job/)

---

**How much does an asphalt driveway cost in NZ?**
Per m²: $60–$130. Standard 30m² single car driveway: $1,800–$3,900.

**Is asphalt cheaper than concrete in NZ?**
Yes — asphalt is typically 40–50% cheaper per m² than concrete. However, concrete lasts longer and requires less maintenance.

*Related: [Concrete Driveway Cost NZ](/articles/concrete-driveway-cost-nz/) | [Concreters Near You](/trades/concreters/)*
"""


# ── Article list ──────────────────────────────────────────────────────────────

ARTICLES = []

# Pool builder small cities
for ck in SMALL_CITIES:
    ARTICLES.append((f"pool-builder-{ck}-nz", lambda k=ck: pool_small(k)))

# Pergola builder all cities
for ck in ALL_CITIES:
    ARTICLES.append((f"pergola-builder-{ck}-nz", lambda k=ck: pergola_article(k)))

# National cost guides
ARTICLES += [
    ("retaining-wall-cost-nz",           retaining_wall_article),
    ("interior-painting-cost-nz",        interior_painting_article),
    ("exterior-house-painting-cost-nz",  exterior_painting_article),
    ("bathroom-tiling-cost-nz",          bathroom_tiling_article),
    ("new-home-build-cost-nz",           new_build_article),
    ("asphalt-driveway-cost-nz",         asphalt_driveway_article),
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
