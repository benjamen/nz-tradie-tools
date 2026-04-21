#!/usr/bin/env python3
"""
Generate job_estimates.json from researched NZ pricing data.
Sources: Builderscrack categories, NZ construction industry rates,
         Rawlinsons NZ Construction Handbook, tradie market data.
"""

import json
from pathlib import Path

OUT_DIR = Path(__file__).parent.parent / "data" / "estimates" / "raw"
OUT_DIR.mkdir(parents=True, exist_ok=True)

REGIONAL_MULTIPLIERS = {
    "auckland": 1.15, "queenstown": 1.20, "wellington": 1.08,
    "tauranga": 1.02, "hamilton": 0.97, "christchurch": 0.98,
    "dunedin": 0.93, "napier": 0.95, "hastings": 0.95,
    "new-plymouth": 0.94, "rotorua": 0.93, "whangarei": 0.95,
    "nelson": 0.96, "invercargill": 0.90, "lower-hutt": 1.05,
    "upper-hutt": 1.03, "porirua": 1.04, "gisborne": 0.91,
    "whanganui": 0.90, "palmerston-north": 0.95,
}

CATEGORIES = [
    {
        "slug": "bathroom-renovation",
        "label": "Bathroom Renovation",
        "trade": "plumbers",
        "icon": "🚿",
        "description": "Full bathroom renovation including tiling, plumbing, fixtures, and waterproofing.",
        "includes": "Labour, fixtures (toilet, vanity, shower/bath), tiling, waterproofing, and plumbing connections.",
        "excludes": "Building consent for structural changes, asbestos removal, electrical work beyond lighting.",
        "related_trade": "/trades/plumbers/",
        "tips": ["Get a licensed plumber for all drainage and water supply work", "Budget 10–15% extra for unexpected issues behind walls", "Choose fittings before quoting so labour scope is clear"],
        "scenarios": [
            {"key": "small",  "label": "Small bathroom (≤5m², budget fixtures)",      "min": 8000,  "max": 14000},
            {"key": "medium", "label": "Medium bathroom (6–10m², standard fixtures)", "min": 15000, "max": 28000},
            {"key": "large",  "label": "Large bathroom (10m²+, premium fixtures)",    "min": 30000, "max": 60000},
        ],
    },
    {
        "slug": "kitchen-renovation",
        "label": "Kitchen Renovation",
        "trade": "builders",
        "icon": "🍳",
        "description": "Kitchen renovation including cabinetry, benchtop, splashback, and connections.",
        "includes": "Labour, cabinetry, benchtop, splashback, plumbing connections, basic electrical.",
        "excludes": "Appliances (unless specified), structural changes, consent fees.",
        "related_trade": "/trades/builders/",
        "tips": ["Get separate quotes for cabinetry, plumbing, and electrical", "Allow 6–12 weeks lead time for custom cabinetry", "Use a project manager for full kitchen gut-and-redo"],
        "scenarios": [
            {"key": "small",  "label": "Minor refresh (new benchtop/splashback only)",  "min": 5000,  "max": 12000},
            {"key": "medium", "label": "Full renovation (new cabinets, bench, appliances)", "min": 18000, "max": 40000},
            {"key": "large",  "label": "Premium fit-out (stone bench, custom cabinetry)",  "min": 45000, "max": 100000},
        ],
    },
    {
        "slug": "decking",
        "label": "Deck Building",
        "trade": "builders",
        "icon": "🪵",
        "description": "New deck construction including framing, decking boards, and balustrades.",
        "includes": "Consent (if needed), framing, posts, decking boards, fixings, and basic balustrades.",
        "excludes": "Painting or staining (optional extra), pergola or shade structure.",
        "related_trade": "/trades/builders/",
        "tips": ["Decks over 1.5m above ground require building consent", "Hardwood and composite last longer but cost more upfront", "Get a fixed-price quote to avoid cost blowout"],
        "scenarios": [
            {"key": "small",  "label": "Small deck (≤20m², treated pine)",     "min": 6000,  "max": 13000},
            {"key": "medium", "label": "Medium deck (20–40m², hardwood)",       "min": 14000, "max": 30000},
            {"key": "large",  "label": "Large deck (40m²+, composite/hardwood)", "min": 32000, "max": 65000},
        ],
    },
    {
        "slug": "painting",
        "label": "Interior & Exterior Painting",
        "trade": "painters",
        "icon": "🎨",
        "description": "Professional interior or exterior painting including preparation and two coats.",
        "includes": "Surface preparation, filling, sanding, primer where needed, two coats of finish paint.",
        "excludes": "Wallpaper removal (extra charge), plaster repair beyond minor filling.",
        "related_trade": "/trades/painters/",
        "tips": ["Good preparation is 80% of a quality paint job", "Ask for a specification listing paint brand and sheen", "Exterior repaints every 8–10 years extend cladding life significantly"],
        "scenarios": [
            {"key": "small",  "label": "Small home interior (2–3 rooms)",       "min": 2500,  "max": 6000},
            {"key": "medium", "label": "Full home interior or exterior repaint", "min": 6000,  "max": 14000},
            {"key": "large",  "label": "Large home interior + exterior",         "min": 15000, "max": 30000},
        ],
    },
    {
        "slug": "roofing",
        "label": "Roof Replacement",
        "trade": "builders",
        "icon": "🏠",
        "description": "Full roof replacement including removal of old roofing, underlay, and new Colorsteel or tile.",
        "includes": "Removal of old roof, underlay, all flashings, new roofing material and fixings.",
        "excludes": "Guttering (quoted separately), fascia/soffit repairs, roof painting.",
        "related_trade": "/trades/builders/",
        "tips": ["Get quotes from licensed roofing contractors only", "Colorsteel is the most cost-effective option in NZ", "Consider insulation upgrade while the roof is off"],
        "scenarios": [
            {"key": "small",  "label": "Small home roof (≤100m², iron/Colorsteel)", "min": 12000, "max": 22000},
            {"key": "medium", "label": "Average home roof (100–180m², Colorsteel)",  "min": 22000, "max": 40000},
            {"key": "large",  "label": "Large home roof (180m²+, Colorsteel/tile)",  "min": 40000, "max": 75000},
        ],
    },
    {
        "slug": "fencing-and-gates",
        "label": "Fencing & Gates",
        "trade": "builders",
        "icon": "🚧",
        "description": "New fence installation including posts, rails, and palings or panels.",
        "includes": "Post holes, concrete, posts, rails, palings or panels, and fixings.",
        "excludes": "Removal of old fencing (usually extra cost), gates unless specified.",
        "related_trade": "/trades/builders/",
        "tips": ["Check boundary lines with your council before starting", "Timber palings are cheapest but need treatment or painting", "Get neighbour agreement in writing for boundary fences"],
        "scenarios": [
            {"key": "small",  "label": "Short fence run (≤25m, timber palings)",  "min": 2500,  "max": 5500},
            {"key": "medium", "label": "Medium fence run (25–60m, timber/Colorbond)", "min": 6000,  "max": 13000},
            {"key": "large",  "label": "Long fence run (60m+, timber/Colorbond)",  "min": 13000, "max": 28000},
        ],
    },
    {
        "slug": "flooring",
        "label": "Flooring Installation",
        "trade": "builders",
        "icon": "🏢",
        "description": "Flooring installation including timber, laminate, vinyl, tile, or carpet.",
        "includes": "Labour, underlay where needed, adhesives, and trims. Materials priced separately unless specified.",
        "excludes": "Subfloor repairs, furniture removal, tile removal (extra cost).",
        "related_trade": "/trades/builders/",
        "tips": ["Vinyl plank is the best value for wet areas like bathrooms and laundries", "Engineered timber is more stable than solid timber in NZ's climate", "Get subfloor checked for moisture before installing timber"],
        "scenarios": [
            {"key": "small",  "label": "Small area (≤40m², vinyl plank/laminate)", "min": 2500,  "max": 7000},
            {"key": "medium", "label": "Full home (80–120m², engineered timber)",   "min": 9000,  "max": 22000},
            {"key": "large",  "label": "Large home (120m²+, hardwood timber)",      "min": 22000, "max": 55000},
        ],
    },
    {
        "slug": "insulation",
        "label": "Insulation Installation",
        "trade": "builders",
        "icon": "🏡",
        "description": "Ceiling, underfloor, or wall insulation installation including batts or blown-in insulation.",
        "includes": "Labour and insulation material. Ceiling, underfloor, or wall options.",
        "excludes": "Removal of old wet/contaminated insulation (extra cost), very restricted access.",
        "related_trade": "/trades/builders/",
        "tips": ["Ceiling insulation gives the best return on investment", "Check if you qualify for Warmer Kiwi Homes government subsidy", "R3.6 is minimum recommended for NZ ceiling insulation"],
        "scenarios": [
            {"key": "small",  "label": "Ceiling only, small home (≤90m²)",       "min": 1200,  "max": 3000},
            {"key": "medium", "label": "Ceiling + underfloor (120–160m² home)",   "min": 3500,  "max": 7000},
            {"key": "large",  "label": "Full home ceiling + underfloor + walls",  "min": 7500,  "max": 16000},
        ],
    },
    {
        "slug": "driveway",
        "label": "Driveway Construction",
        "trade": "builders",
        "icon": "🛣️",
        "description": "New driveway or resurfacing in concrete, asphalt, or pavers.",
        "includes": "Labour, base preparation, compaction, concrete/asphalt/pavers, and edging.",
        "excludes": "Removal of old driveway (usually extra), drainage work, consent if crossing footpath.",
        "related_trade": "/trades/builders/",
        "tips": ["Concrete outlasts asphalt by 15–20 years in NZ conditions", "Exposed aggregate or brushed concrete adds grip and looks better", "Get at least 2 quotes — driveway pricing varies significantly"],
        "scenarios": [
            {"key": "small",  "label": "Short driveway (≤40m², concrete)",    "min": 5000,  "max": 10000},
            {"key": "medium", "label": "Standard driveway (40–80m², concrete)", "min": 10000, "max": 20000},
            {"key": "large",  "label": "Long driveway (80m²+, concrete/pavers)", "min": 20000, "max": 45000},
        ],
    },
    {
        "slug": "landscaping-and-outdoors",
        "label": "Landscaping",
        "trade": "builders",
        "icon": "🌿",
        "description": "Garden landscaping including lawn, planting, paths, and garden beds.",
        "includes": "Labour, topsoil, plants, lawn, garden paths, and irrigation if required.",
        "excludes": "Tree removal, major earthworks and consent for large structures.",
        "related_trade": "/trades/builders/",
        "tips": ["Hire a landscape designer for complex projects — saves cost in the long run", "Native plants require less maintenance and suit NZ conditions", "Ask if topsoil and plants are included in the quote"],
        "scenarios": [
            {"key": "small",  "label": "Small garden makeover (≤60m²)",          "min": 3000,  "max": 9000},
            {"key": "medium", "label": "Medium landscaping project (60–200m²)",   "min": 10000, "max": 28000},
            {"key": "large",  "label": "Full property landscaping (200m²+)",      "min": 30000, "max": 80000},
        ],
    },
    {
        "slug": "retaining-walls",
        "label": "Retaining Walls",
        "trade": "builders",
        "icon": "🧱",
        "description": "Retaining wall construction in timber, concrete block, or engineered stone.",
        "includes": "Labour, materials (timber/block/stone), drainage behind wall, and concrete footings.",
        "excludes": "Building consent for walls over 1.5m high, earthworks and soil disposal.",
        "related_trade": "/trades/builders/",
        "tips": ["Walls over 1.5m require building consent in most NZ councils", "Always include drainage behind the wall to prevent failure", "Concrete block outlasts timber but costs more upfront"],
        "scenarios": [
            {"key": "small",  "label": "Short timber wall (≤6m, up to 1m high)",     "min": 3000,  "max": 7500},
            {"key": "medium", "label": "Medium block wall (6–20m, 1–1.5m high)",      "min": 10000, "max": 25000},
            {"key": "large",  "label": "Large engineered wall (20m+, 1.5m+ high)",    "min": 28000, "max": 70000},
        ],
    },
    {
        "slug": "plasterboard",
        "label": "Plasterboard & Stopping",
        "trade": "builders",
        "icon": "🔲",
        "description": "Plasterboard installation, stopping, and finishing ready for paint.",
        "includes": "Plasterboard supply and installation, all stopping coats, sanding to Level 4 finish.",
        "excludes": "Painting, architectural features/bulkheads quoted separately.",
        "related_trade": "/trades/builders/",
        "tips": ["Level 4 stopping is standard for painted surfaces in NZ", "Ensure stopping is fully dry before painting — rush jobs cause cracking", "GIB Aqualine or equivalent is required in wet areas"],
        "scenarios": [
            {"key": "small",  "label": "1–2 rooms repair/replacement (≤25m²)",  "min": 1500,  "max": 4500},
            {"key": "medium", "label": "Full home fit-out (80–120m²)",           "min": 8000,  "max": 20000},
            {"key": "large",  "label": "Large home or commercial (150m²+)",      "min": 20000, "max": 45000},
        ],
    },
    {
        "slug": "guttering-and-drainage",
        "label": "Guttering & Drainage",
        "trade": "plumbers",
        "icon": "🌧️",
        "description": "Gutter replacement or new installation and stormwater drainage.",
        "includes": "Gutters, downpipes, brackets, sealants, and connection to stormwater drainage.",
        "excludes": "Roof repairs, stormwater drainage beyond the property boundary.",
        "related_trade": "/trades/plumbers/",
        "tips": ["Replace gutters every 20–30 years or when they start sagging or leaking", "Aluminium gutters are the standard in NZ — avoid galvanised in coastal areas", "Check downpipes run to proper stormwater drain, not just the garden"],
        "scenarios": [
            {"key": "small",  "label": "Small home (≤25m of guttering)",    "min": 1500,  "max": 3500},
            {"key": "medium", "label": "Average home (25–60m of guttering)", "min": 3500,  "max": 7500},
            {"key": "large",  "label": "Large home (60m+ guttering + downpipes)", "min": 8000, "max": 16000},
        ],
    },
    {
        "slug": "heating-ventilation-systems",
        "label": "Heating & Ventilation",
        "trade": "electricians",
        "icon": "🌡️",
        "description": "Heat pump, wood burner, or HRV ventilation system supply and installation.",
        "includes": "Supply and installation of heat pump or HRV, electrical connection, and commissioning.",
        "excludes": "Flue for wood burners (specialist), consent fees, electrical switchboard upgrade.",
        "related_trade": "/trades/electricians/",
        "tips": ["Heat pumps are the most cost-effective heating in NZ — 3:1 efficiency ratio", "Check your council rules on wood burner installation (many urban areas restrict)", "HRV or DVS systems are worth it in damp NZ homes"],
        "scenarios": [
            {"key": "small",  "label": "Single heat pump (1 indoor unit)",        "min": 2500,  "max": 4500},
            {"key": "medium", "label": "Multi-split system (2–3 indoor units)",   "min": 6000,  "max": 12000},
            {"key": "large",  "label": "Ducted system or 4+ units",               "min": 15000, "max": 35000},
        ],
    },
    {
        "slug": "lighting",
        "label": "Lighting Installation",
        "trade": "electricians",
        "icon": "💡",
        "description": "Interior or exterior lighting installation including downlights, feature lighting, and sensors.",
        "includes": "Labour, wiring, switch installation, and light fittings (if supply-and-install).",
        "excludes": "Fittings if customer-supplied, switchboard upgrades (quoted separately).",
        "related_trade": "/trades/electricians/",
        "tips": ["LED downlights save significant power over halogen", "Ensure your electrician is registered with the Electrical Workers Registration Board", "Dimmer switches add cost but improve comfort and save power"],
        "scenarios": [
            {"key": "small",  "label": "Small job (5–10 downlights, 1 room)",       "min": 600,   "max": 2000},
            {"key": "medium", "label": "Full home lighting fit-out (20–30 lights)",  "min": 2500,  "max": 7000},
            {"key": "large",  "label": "New build or major refit (40+ lights)",      "min": 7000,  "max": 18000},
        ],
    },
    {
        "slug": "asbestos-removal",
        "label": "Asbestos Removal",
        "trade": "builders",
        "icon": "⚠️",
        "description": "Licensed asbestos identification, removal, and disposal including clearance certificate.",
        "includes": "Site assessment, licensed removal, disposal, and written clearance certificate.",
        "excludes": "Asbestos testing if not yet done, reinstatement/repair work after removal.",
        "related_trade": "/trades/builders/",
        "tips": ["Never remove asbestos yourself — licensed removalist required by NZ law", "Homes built before 1990 often contain asbestos in walls, ceilings, and floor tiles", "Get a clearance certificate after removal — required for council CCC"],
        "scenarios": [
            {"key": "small",  "label": "Small area — tiles or eaves (≤10m²)",      "min": 1500,  "max": 5000},
            {"key": "medium", "label": "Medium area — wall linings or soffit (≤30m²)", "min": 6000,  "max": 16000},
            {"key": "large",  "label": "Large or whole-house removal (30m²+)",      "min": 18000, "max": 45000},
        ],
    },
    {
        "slug": "glass-replacement",
        "label": "Glass & Glazing",
        "trade": "builders",
        "icon": "🪟",
        "description": "Window or door glass replacement including single, double glaze, and retrofit.",
        "includes": "Glass supply and installation, sealing, and glazing beads. Frames if required.",
        "excludes": "Full window frame replacement (separate quote), building consent for major changes.",
        "related_trade": "/trades/builders/",
        "tips": ["Double glazing reduces heat loss by ~50% vs single glaze", "Retrofit double glazing is cheaper than full window replacement", "Safety glass is required by NZ code near doors and low windows"],
        "scenarios": [
            {"key": "small",  "label": "1–3 standard pane replacements",          "min": 400,   "max": 1500},
            {"key": "medium", "label": "Double glaze retrofit (5–10 windows)",     "min": 4000,  "max": 10000},
            {"key": "large",  "label": "Full home re-glaze to double glaze",       "min": 12000, "max": 35000},
        ],
    },
    {
        "slug": "cladding",
        "label": "External Cladding",
        "trade": "builders",
        "icon": "🏗️",
        "description": "External wall cladding replacement or installation including weatherboards, Linea, or Hardie.",
        "includes": "Removal of old cladding if replacing, building wrap, new cladding, and flashings.",
        "excludes": "Painting (usually quoted separately), structural repairs to framing.",
        "related_trade": "/trades/builders/",
        "tips": ["Leaky home era (1994–2004) homes must be fully recladded if using direct-fix", "Cavity-drain cladding systems are now standard — avoid direct-fix", "James Hardie and weathertex are popular mid-range cladding options in NZ"],
        "scenarios": [
            {"key": "small",  "label": "One or two elevations (≤50m²)",          "min": 9000,  "max": 18000},
            {"key": "medium", "label": "Partial re-clad (50–130m², Linea/Hardie)", "min": 22000, "max": 45000},
            {"key": "large",  "label": "Full home re-clad (130m²+)",              "min": 50000, "max": 100000},
        ],
    },
    {
        "slug": "structures",
        "label": "Garages & Sleepouts",
        "trade": "builders",
        "icon": "🏚️",
        "description": "Garage, carport, sleepout, or garden shed construction to lockup stage.",
        "includes": "Foundation/slab, framing, roofing, cladding, windows, and door to lockup stage.",
        "excludes": "Building consent, internal lining/fitout, electrical, plumbing.",
        "related_trade": "/trades/builders/",
        "tips": ["Most garages and sleepouts require building consent — allow 4–8 weeks", "Prefab kitset garages are cheaper but require consent if attached to house", "Insulate if used as a sleepout — NZ building code requires it"],
        "scenarios": [
            {"key": "small",  "label": "Single garage or carport (≤25m²)",  "min": 15000, "max": 30000},
            {"key": "medium", "label": "Double garage or sleepout (25–50m²)", "min": 30000, "max": 60000},
            {"key": "large",  "label": "Large garage-workshop or studio (50m²+)", "min": 60000, "max": 110000},
        ],
    },
]


def main():
    for cat in CATEGORIES:
        out = {
            "slug": cat["slug"],
            "label": cat["label"],
            "trade": cat["trade"],
            "icon": cat["icon"],
            "description": cat["description"],
            "includes": cat["includes"],
            "excludes": cat["excludes"],
            "related_trade": cat["related_trade"],
            "tips": cat["tips"],
            "source": "NZ Tradie Tools Research 2026",
            "scenarios": {
                sc["key"]: {
                    "label": sc["label"],
                    "min": sc["min"],
                    "max": sc["max"],
                }
                for sc in cat["scenarios"]
            },
        }
        out_file = OUT_DIR / f"{cat['slug']}.json"
        out_file.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    print(f"Generated {len(CATEGORIES)} estimate files in {OUT_DIR}")

    # Also write the combined job_estimates.json + regional multipliers
    combined = {
        "regional_multipliers": REGIONAL_MULTIPLIERS,
        "jobs": {cat["slug"]: {
            "label": cat["label"],
            "trade": cat["trade"],
            "icon": cat["icon"],
            "description": cat["description"],
            "includes": cat["includes"],
            "excludes": cat["excludes"],
            "related_trade": cat["related_trade"],
            "tips": cat["tips"],
            "source": "NZ Tradie Tools Research 2026",
            "scenarios": {
                sc["key"]: {"label": sc["label"], "min": sc["min"], "max": sc["max"]}
                for sc in cat["scenarios"]
            },
        } for cat in CATEGORIES}
    }
    out_combined = Path(__file__).parent.parent / "data" / "job_estimates.json"
    out_combined.write_text(json.dumps(combined, indent=2, ensure_ascii=False))
    print(f"Written combined: {out_combined}")


if __name__ == "__main__":
    main()
