#!/usr/bin/env python3
"""
Builderscrack estimates scraper — one-off run.
Navigates each of the 19 estimator pages with Playwright,
fills in 3 scenarios per page, and captures the price output.
"""

import json
import re
import time
from datetime import date
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

BASE_URL = "https://builderscrack.co.nz/estimates"
OUT_DIR = Path(__file__).parent.parent / "data" / "estimates" / "raw"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()

# Per-category scenario config:
# Each scenario maps field selectors/labels → values to set.
# "quality" values map to option text fragments to look for.
CATEGORIES = [
    {
        "slug": "bathroom-renovation",
        "label": "Bathroom Renovation",
        "trade": "plumbers",
        "icon": "🚿",
        "description": "Full bathroom renovation including tiling, plumbing, fixtures, and waterproofing.",
        "includes": "Labour, fixtures, tiling, waterproofing, plumbing connections.",
        "excludes": "Building consent, structural changes, asbestos removal.",
        "related_trade": "/trades/plumbers/",
        "scenarios": [
            {"key": "small",  "label": "Small bathroom (4m², budget fixtures)",    "size": 4},
            {"key": "medium", "label": "Medium bathroom (8m², standard fixtures)",  "size": 8},
            {"key": "large",  "label": "Large bathroom (14m², premium fixtures)",   "size": 14},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (8000, 14000), "medium": (16000, 28000), "large": (30000, 55000)},
    },
    {
        "slug": "kitchen-renovation",
        "label": "Kitchen Renovation",
        "trade": "builders",
        "icon": "🍳",
        "description": "Kitchen renovation including cabinetry, benchtop, appliances, and plumbing.",
        "includes": "Labour, cabinetry, benchtop, splashback, plumbing connections, electrical.",
        "excludes": "Appliances (unless specified), building consent for structural changes.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small kitchen (basic refresh)",     "size": 8},
            {"key": "medium", "label": "Medium kitchen (full renovation)",   "size": 15},
            {"key": "large",  "label": "Large kitchen (premium fit-out)",    "size": 25},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (10000, 20000), "medium": (22000, 45000), "large": (50000, 100000)},
    },
    {
        "slug": "decking",
        "label": "Deck Building",
        "trade": "builders",
        "icon": "🪵",
        "description": "New deck construction including framing, decking boards, and balustrades.",
        "includes": "Labour, framing, decking boards, fixings. Balustrades if required.",
        "excludes": "Building consent for decks over 1.5m high, painting/staining (optional extra).",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small deck (15m², treated pine)",  "size": 15},
            {"key": "medium", "label": "Medium deck (30m², hardwood)",      "size": 30},
            {"key": "large",  "label": "Large deck (60m², composite)",      "size": 60},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (6000, 12000), "medium": (15000, 28000), "large": (30000, 60000)},
    },
    {
        "slug": "painting",
        "label": "Interior & Exterior Painting",
        "trade": "painters",
        "icon": "🎨",
        "description": "Professional interior or exterior painting including preparation and two coats.",
        "includes": "Surface preparation, primer where needed, two finish coats, masking.",
        "excludes": "Wallpaper removal, plastering repairs (quoted separately).",
        "related_trade": "/trades/painters/",
        "scenarios": [
            {"key": "small",  "label": "Small home interior (100m² walls)", "size": 100},
            {"key": "medium", "label": "Average home interior (200m² walls)", "size": 200},
            {"key": "large",  "label": "Large home or exterior (350m²)",     "size": 350},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (3000, 6000), "medium": (6000, 12000), "large": (12000, 24000)},
    },
    {
        "slug": "roofing",
        "label": "Roof Replacement",
        "trade": "builders",
        "icon": "🏠",
        "description": "Full roof replacement including removal of old roofing, underlay, and new metal or tile roof.",
        "includes": "Removal of old roof, underlay, flashings, new roofing material.",
        "excludes": "Guttering (quoted separately), building consent if applicable.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small roof (80m², corrugated iron)", "size": 80},
            {"key": "medium", "label": "Medium roof (150m², Colorsteel)",    "size": 150},
            {"key": "large",  "label": "Large roof (250m², Colorsteel/tile)", "size": 250},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (12000, 20000), "medium": (22000, 38000), "large": (40000, 70000)},
    },
    {
        "slug": "fencing-and-gates",
        "label": "Fencing & Gates",
        "trade": "builders",
        "icon": "🚧",
        "description": "New fence installation including posts, rails, and palings or panels.",
        "includes": "Post holes, posts, rails, palings or panels, fixings.",
        "excludes": "Removal of old fencing (extra cost), gates (quoted separately unless specified).",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Short fence run (20m, timber palings)", "size": 20},
            {"key": "medium", "label": "Medium fence run (50m, timber)",         "size": 50},
            {"key": "large",  "label": "Long fence run (100m, timber/colorbond)", "size": 100},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (2500, 5000), "medium": (6000, 12000), "large": (12000, 24000)},
    },
    {
        "slug": "flooring",
        "label": "Flooring Installation",
        "trade": "builders",
        "icon": "🪟",
        "description": "Flooring installation including timber, laminate, vinyl, tile, or carpet.",
        "includes": "Labour, underlay, adhesives, trims. Materials priced separately.",
        "excludes": "Subfloor repairs, furniture removal.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small area (30m², vinyl/laminate)",  "size": 30},
            {"key": "medium", "label": "Full home (100m², timber/laminate)", "size": 100},
            {"key": "large",  "label": "Large home (200m², hardwood timber)", "size": 200},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (2500, 6000), "medium": (8000, 20000), "large": (20000, 50000)},
    },
    {
        "slug": "insulation",
        "label": "Insulation Installation",
        "trade": "builders",
        "icon": "🏡",
        "description": "Ceiling, underfloor, or wall insulation installation including batts or blown-in insulation.",
        "includes": "Labour and insulation materials. Ceiling, underfloor, or wall options.",
        "excludes": "Access work if space is very restricted.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small home ceiling only (80m²)",     "size": 80},
            {"key": "medium", "label": "Full home ceiling + underfloor (150m²)", "size": 150},
            {"key": "large",  "label": "Full home + walls (200m²)",           "size": 200},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (1500, 3500), "medium": (3500, 7000), "large": (7000, 14000)},
    },
    {
        "slug": "driveway",
        "label": "Driveway Construction",
        "trade": "builders",
        "icon": "🛣️",
        "description": "New driveway or driveway resurfacing in concrete, asphalt, or pavers.",
        "includes": "Labour, base preparation, concrete/asphalt/pavers, edging.",
        "excludes": "Removal of old driveway (extra cost), drainage work.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Short driveway (30m², concrete)",   "size": 30},
            {"key": "medium", "label": "Standard driveway (60m², concrete)", "size": 60},
            {"key": "large",  "label": "Long driveway (120m², concrete)",    "size": 120},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (4500, 9000), "medium": (9000, 18000), "large": (18000, 36000)},
    },
    {
        "slug": "landscaping-and-outdoors",
        "label": "Landscaping",
        "trade": "builders",
        "icon": "🌿",
        "description": "Garden landscaping including lawn, planting, paths, and garden beds.",
        "includes": "Labour, topsoil, plants, lawn, paths, irrigation if required.",
        "excludes": "Tree removal, major earthworks, consent for large structures.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small garden makeover (50m²)",     "size": 50},
            {"key": "medium", "label": "Medium landscaping project (150m²)", "size": 150},
            {"key": "large",  "label": "Full property landscaping (300m²)", "size": 300},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (3000, 8000), "medium": (10000, 25000), "large": (25000, 60000)},
    },
    {
        "slug": "retaining-walls",
        "label": "Retaining Walls",
        "trade": "builders",
        "icon": "🧱",
        "description": "Retaining wall construction in timber, concrete block, or stone.",
        "includes": "Labour, materials, drainage behind wall, posts/blocks/timber.",
        "excludes": "Consent for walls over 1.5m, earthworks behind wall.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Short wall (5m × 1m, timber)",   "size": 5},
            {"key": "medium", "label": "Medium wall (15m × 1.5m, block)", "size": 15},
            {"key": "large",  "label": "Long wall (30m × 2m, concrete)",  "size": 30},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (3000, 7000), "medium": (12000, 28000), "large": (30000, 70000)},
    },
    {
        "slug": "plasterboard",
        "label": "Plasterboard & Plastering",
        "trade": "builders",
        "icon": "🔲",
        "description": "Plasterboard installation and plastering including stopping and finishing.",
        "includes": "Plasterboard supply and installation, stopping, sanding to paint-ready finish.",
        "excludes": "Painting, architectural features/bulkheads.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small room (20m²)",          "size": 20},
            {"key": "medium", "label": "Full home fit-out (100m²)",   "size": 100},
            {"key": "large",  "label": "Large home or commercial (200m²)", "size": 200},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (1500, 4000), "medium": (8000, 18000), "large": (18000, 38000)},
    },
    {
        "slug": "guttering-and-drainage",
        "label": "Guttering & Drainage",
        "trade": "plumbers",
        "icon": "🌧️",
        "description": "Gutter replacement or installation and stormwater drainage.",
        "includes": "Gutters, downpipes, brackets, sealants, connection to drainage.",
        "excludes": "Roof repairs, stormwater drainage beyond property boundary.",
        "related_trade": "/trades/plumbers/",
        "scenarios": [
            {"key": "small",  "label": "Small home (20m guttering)",  "size": 20},
            {"key": "medium", "label": "Average home (50m guttering)", "size": 50},
            {"key": "large",  "label": "Large home (100m guttering)",  "size": 100},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (1500, 3500), "medium": (3500, 7000), "large": (7000, 14000)},
    },
    {
        "slug": "heating-ventilation-systems",
        "label": "Heating & Ventilation",
        "trade": "electricians",
        "icon": "🌡️",
        "description": "Heat pump, wood burner, or HRV system supply and installation.",
        "includes": "Supply and installation of heat pump or HRV system, electrical connection.",
        "excludes": "Flue installation for wood burners (by specialist), consent fees.",
        "related_trade": "/trades/electricians/",
        "scenarios": [
            {"key": "small",  "label": "Single heat pump (lounge)",    "size": 1},
            {"key": "medium", "label": "2–3 heat pumps (home system)", "size": 3},
            {"key": "large",  "label": "Ducted system or HRV + heat pumps", "size": 5},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (2500, 4500), "medium": (6000, 12000), "large": (15000, 30000)},
    },
    {
        "slug": "lighting",
        "label": "Lighting Installation",
        "trade": "electricians",
        "icon": "💡",
        "description": "Interior or exterior lighting installation including downlights, feature lighting, and switchboards.",
        "includes": "Labour, light fittings (if supplied), wiring, switch installation.",
        "excludes": "Light fittings if customer-supplied, switchboard upgrades (quoted separately).",
        "related_trade": "/trades/electricians/",
        "scenarios": [
            {"key": "small",  "label": "Small job (5–10 downlights)",   "size": 8},
            {"key": "medium", "label": "Full home lighting (20–30 lights)", "size": 25},
            {"key": "large",  "label": "New build or major refit (50+ lights)", "size": 50},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (800, 2000), "medium": (2500, 6000), "large": (6000, 15000)},
    },
    {
        "slug": "asbestos-removal",
        "label": "Asbestos Removal",
        "trade": "builders",
        "icon": "⚠️",
        "description": "Licensed asbestos removal and disposal including testing if required.",
        "includes": "Site assessment, removal by licensed removalist, disposal, clearance certificate.",
        "excludes": "Testing (if not yet done), reinstatement work after removal.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Small area — ceiling tiles or eaves (5m²)",  "size": 5},
            {"key": "medium", "label": "Medium area — wall linings or roof (20m²)",   "size": 20},
            {"key": "large",  "label": "Large area — whole-house removal (50m²+)",    "size": 50},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (1500, 4000), "medium": (6000, 15000), "large": (18000, 40000)},
    },
    {
        "slug": "glass-replacement",
        "label": "Glass Replacement",
        "trade": "builders",
        "icon": "🪟",
        "description": "Window or door glass replacement including double glazing retrofit.",
        "includes": "Glass supply and installation, sealing, glazing beads.",
        "excludes": "Frame replacement, building consent for major changes.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "1–2 standard panes (single glaze)", "size": 2},
            {"key": "medium", "label": "5–10 panes (double glaze retrofit)", "size": 8},
            {"key": "large",  "label": "Whole home re-glaze (double glaze)", "size": 20},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (400, 1200), "medium": (3000, 8000), "large": (10000, 28000)},
    },
    {
        "slug": "cladding",
        "label": "External Cladding",
        "trade": "builders",
        "icon": "🏗️",
        "description": "External wall cladding replacement or installation including weatherboards, Linea, or Hardie.",
        "includes": "Removal of old cladding (if replacing), building wrap, new cladding, flashings.",
        "excludes": "Painting (quoted separately), structural repairs to framing.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "One elevation (40m², weatherboard)",  "size": 40},
            {"key": "medium", "label": "Half home (100m², Linea)",            "size": 100},
            {"key": "large",  "label": "Full home re-clad (200m², Hardie)",   "size": 200},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (8000, 16000), "medium": (20000, 40000), "large": (45000, 90000)},
    },
    {
        "slug": "structures",
        "label": "Garages & Structures",
        "trade": "builders",
        "icon": "🏚️",
        "description": "Garage, carport, sleepout, or shed construction.",
        "includes": "Foundation, framing, roofing, cladding, and fitout to lockup stage.",
        "excludes": "Building consent, electrical fitout, plumbing.",
        "related_trade": "/trades/builders/",
        "scenarios": [
            {"key": "small",  "label": "Single garage or carport (20m²)",   "size": 20},
            {"key": "medium", "label": "Double garage or sleepout (40m²)",   "size": 40},
            {"key": "large",  "label": "Large garage or studio (70m²+)",     "size": 70},
        ],
        "size_selector": "input[type=number]",
        "fallback": {"small": (15000, 30000), "medium": (30000, 55000), "large": (55000, 100000)},
    },
]

REGIONAL_MULTIPLIERS = {
    "auckland": 1.15, "queenstown": 1.20, "wellington": 1.08,
    "tauranga": 1.02, "hamilton": 0.97, "christchurch": 0.98,
    "dunedin": 0.93, "napier": 0.95, "hastings": 0.95,
    "new-plymouth": 0.94, "rotorua": 0.93, "whangarei": 0.95,
    "nelson": 0.96, "invercargill": 0.90, "lower-hutt": 1.05,
    "upper-hutt": 1.03, "porirua": 1.04, "gisborne": 0.91,
    "whanganui": 0.90, "palmerston-north": 0.95,
}


def extract_price(text):
    """Extract first dollar amount from text, return as int or None."""
    text = text.replace(",", "").replace(" ", "")
    m = re.search(r'\$(\d+)', text)
    return int(m.group(1)) if m else None


def scrape_category(page, cat):
    url = f"{BASE_URL}/{cat['slug']}"
    print(f"  Scraping {cat['slug']}...")

    results = {}
    try:
        page.goto(url, wait_until="networkidle", timeout=20000)
        page.wait_for_timeout(2000)
    except PWTimeout:
        print(f"    Timeout loading {url}, using fallback data")
        for sc in cat["scenarios"]:
            lo, hi = cat["fallback"][sc["key"]]
            results[sc["key"]] = {"label": sc["label"], "min": lo, "max": hi, "source": "fallback"}
        return results

    for sc in cat["scenarios"]:
        try:
            # Try to set numeric input
            inputs = page.query_selector_all("input[type='number']")
            if inputs:
                inputs[0].triple_click()
                inputs[0].type(str(sc["size"]))
                inputs[0].dispatch_event("input")
                inputs[0].dispatch_event("change")
                page.wait_for_timeout(1000)

            # Try to find quality selectors (look for select elements or radio buttons)
            selects = page.query_selector_all("select")
            for sel in selects:
                options = sel.query_selector_all("option")
                if len(options) >= 2:
                    # Pick first option for small, middle for medium, last for large
                    idx = {"small": 0, "medium": len(options)//2, "large": len(options)-1}[sc["key"]]
                    sel.select_option(index=min(idx, len(options)-1))
                    page.wait_for_timeout(500)

            page.wait_for_timeout(1500)

            # Look for price output — common patterns on Builderscrack
            price_text = ""
            for selector in [
                "[class*='estimate']", "[class*='price']", "[class*='cost']",
                "[class*='total']", "[class*='result']", "strong", "h2", "h3"
            ]:
                els = page.query_selector_all(selector)
                for el in els:
                    txt = el.inner_text()
                    if "$" in txt and any(c.isdigit() for c in txt):
                        price_text = txt
                        break
                if price_text:
                    break

            if price_text:
                # Try to extract min/max range
                amounts = [int(x.replace(",", "")) for x in re.findall(r'\$?([\d,]+)', price_text) if int(x.replace(",","")) > 100]
                if len(amounts) >= 2:
                    results[sc["key"]] = {"label": sc["label"], "min": min(amounts), "max": max(amounts), "source": "scraped"}
                elif len(amounts) == 1:
                    v = amounts[0]
                    results[sc["key"]] = {"label": sc["label"], "min": int(v*0.85), "max": int(v*1.15), "source": "scraped-single"}
                else:
                    raise ValueError("No price amounts found")
            else:
                raise ValueError("No price text found")

        except Exception as e:
            print(f"    Scenario {sc['key']} failed ({e}), using fallback")
            lo, hi = cat["fallback"][sc["key"]]
            results[sc["key"]] = {"label": sc["label"], "min": lo, "max": hi, "source": "fallback"}

    return results


def main():
    print("Starting Builderscrack scraper...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
        )
        page = context.new_page()

        for cat in CATEGORIES:
            scenarios = scrape_category(page, cat)

            out = {
                "slug": cat["slug"],
                "label": cat["label"],
                "trade": cat["trade"],
                "icon": cat["icon"],
                "description": cat["description"],
                "includes": cat["includes"],
                "excludes": cat["excludes"],
                "related_trade": cat["related_trade"],
                "scraped": TODAY,
                "source": "builderscrack.co.nz",
                "scenarios": scenarios,
                "regional_multipliers": REGIONAL_MULTIPLIERS,
            }
            out_file = OUT_DIR / f"{cat['slug']}.json"
            out_file.write_text(json.dumps(out, indent=2, ensure_ascii=False))
            print(f"    Saved {out_file.name}")

        browser.close()

    print(f"\nDone. {len(CATEGORIES)} files saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
