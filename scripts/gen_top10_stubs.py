#!/usr/bin/env python3
"""
Generate stub top10 JSON files for all missing trade×city combos.
Stubs have regional_cost_note + empty businesses list.
Run from site/ directory.
"""
import json, os
from pathlib import Path
from datetime import date

BASE = Path(__file__).parent.parent
TOP10_DIR = BASE / "data" / "top10"
TODAY = date.today().isoformat()

# City pricing context: (modifier_label, context_sentence)
CITY_CONTEXT = {
    "auckland": (
        "premium",
        "Auckland rates are the highest in NZ, reflecting the city's cost of living and high demand."
    ),
    "wellington": (
        "high",
        "Wellington rates are among the highest in NZ — budget 5–15% above the national average."
    ),
    "queenstown": (
        "premium",
        "Queenstown commands premium pricing due to high demand and a tight local labour market."
    ),
    "christchurch": (
        "average",
        "Canterbury rates are near the national average; post-earthquake rebuild experience is common across local trades."
    ),
    "hamilton": (
        "average",
        "Waikato rates are generally 10–15% below Auckland for most trades."
    ),
    "tauranga": (
        "average",
        "Bay of Plenty rates are broadly in line with the national average."
    ),
    "dunedin": (
        "average",
        "Dunedin rates are near the national average; the local market is competitive."
    ),
    "napier": (
        "below-average",
        "Hawke's Bay rates typically run 5–10% below the national average."
    ),
    "hastings": (
        "below-average",
        "Hawke's Bay rates typically run 5–10% below the national average."
    ),
    "nelson": (
        "average",
        "Nelson/Tasman rates are broadly in line with the national average."
    ),
    "new-plymouth": (
        "below-average",
        "Taranaki rates are typically 5–10% below the national average."
    ),
    "rotorua": (
        "below-average",
        "Rotorua rates are generally competitive — expect to pay near or slightly below the national average."
    ),
    "whangarei": (
        "average",
        "Northland rates are broadly in line with the national average, with some capacity constraints for specialist trades."
    ),
    "lower-hutt": (
        "high",
        "Lower Hutt trades often price at Wellington rates given the shared labour pool."
    ),
    "upper-hutt": (
        "high",
        "Upper Hutt trades often price at Wellington rates given the shared labour pool."
    ),
    "porirua": (
        "high",
        "Porirua trades often price at Wellington rates given the shared labour pool."
    ),
    "whanganui": (
        "below-average",
        "Whanganui rates are typically 10–15% below the national average."
    ),
    "invercargill": (
        "below-average",
        "Southland rates are typically 10–15% below the national average, though remote work may attract travel charges."
    ),
    "gisborne": (
        "below-average",
        "Gisborne rates are typically 10–15% below the national average; some specialist trades travel from Hawke's Bay."
    ),
    "palmerston-north": (
        "below-average",
        "Manawatū rates are typically 5–10% below the national average."
    ),
}

# Per-trade cost note templates.
# Uses {city} (city name), {context} (city context sentence)
TRADE_NOTES = {
    "glaziers": (
        "{city} glaziers typically charge $400–$900 per double-glazed unit for standard window replacements. "
        "Shower screens run $900–$2,800 supply and install. {context} Always get a quote before committing — "
        "glass pricing varies significantly with unit size and glazing specification."
    ),
    "fencers": (
        "Fencing in {city} typically costs $160–$300/m for timber paling, $210–$370/m for Colorsteel, "
        "and $320–$650/m for glass pool fencing. {context} Prices include posts, rails, labour, and removal "
        "of old fencing — confirm what's included in any quote."
    ),
    "waterproofers": (
        "{city} waterproofing contractors typically charge $900–$2,800 for bathroom waterproofing, "
        "$85–$190/m² for deck membranes, and $65–$140/m² for roof membranes. {context} Always use a "
        "licensed waterproofer for wet areas — poor waterproofing is one of the most common and costly "
        "defects in NZ homes."
    ),
    "insulation-installers": (
        "Insulation installers in {city} typically charge $22–$35/m² for ceiling insulation and "
        "$20–$30/m² for underfloor, installed. {context} Healthy Homes standards require minimum R-values "
        "— confirm your installer knows the current NZ Building Code requirements for your zone."
    ),
    "heat-pump-installers": (
        "Heat pump installers in {city} typically charge $2,600–$4,800 for a single-room unit (supply and "
        "install) and $8,500–$20,000 for a multi-split system. {context} Get at least 3 quotes — brand, "
        "capacity, and installation complexity vary widely and significantly affect the price."
    ),
    "solar-installers": (
        "Solar panel installers in {city} typically quote $12,500–$17,000 for a 5kW system installed, "
        "and $21,000–$30,000 for a 10kW system. Battery storage adds $8,500–$15,000. {context} "
        "Compare quotes carefully — system size, panel brand, inverter quality, and export metering "
        "arrangements all affect the total cost and payback period."
    ),
    "scaffolders": (
        "Scaffolding in {city} typically costs $2,200–$6,000 for a residential scaffold (erect plus "
        "4 weeks). Commercial jobs are quoted at $25–$55/m² erected. {context} Confirm whether the quote "
        "includes weekly hire after the initial period and dismantling costs."
    ),
    "demolition-contractors": (
        "Demolition contractors in {city} typically charge $3,500–$14,000 for an internal strip-out and "
        "$16,000–$40,000+ for a full house demolition. Asbestos removal is priced separately at $85–$220/m². "
        "{context} Asbestos testing is mandatory before any demolition work on pre-1990 buildings."
    ),
    "arborists": (
        "Arborists in {city} typically charge $550–$1,800 for small tree removal and $2,200–$9,000+ for "
        "large trees. Stump grinding is $220–$650 per stump. {context} Ensure your arborist holds NZ "
        "Arboricultural Association accreditation and has current public liability insurance."
    ),
    "kitchen-renovators": (
        "Kitchen renovations in {city} typically range from $16,000–$28,000 for a budget refresh up to "
        "$33,000–$60,000 for a mid-range full reno, and $65,000–$130,000+ for premium work. {context} "
        "Get fixed-price quotes with a detailed scope — variations are the biggest source of cost blowouts."
    ),
    "bathroom-renovators": (
        "Bathroom renovations in {city} typically cost $9,000–$17,000 for a basic refresh, "
        "$20,000–$38,000 for a mid-range full reno, and $38,000–$85,000+ for premium work. {context} "
        "Waterproofing, tiling, and plumbing are the largest cost components — confirm all are included "
        "in any fixed-price quote."
    ),
    "pest-controllers": (
        "Pest control in {city} typically costs $270–$650 for rodent treatment, $130–$330 for a wasp "
        "nest, and $450–$1,300+ for a full building treatment. {context} For rental properties, "
        "Healthy Homes standards may require documented pest control — keep invoices."
    ),
    "security-system-installers": (
        "Security system installers in {city} typically charge $1,300–$3,000 for a basic alarm system, "
        "$1,600–$3,800 for a 4-camera CCTV setup, and $2,700–$6,500 for a full monitored system. "
        "{context} Monthly monitoring costs ($25–$80/month) are separate — confirm the total cost of "
        "ownership before committing."
    ),
    "hvac-engineers": (
        "HVAC engineers in {city} typically charge $8,500–$20,000 for a residential ducted system and "
        "$150–$420/m² of conditioned space for commercial work. {context} HVAC work must comply with "
        "NZ Building Code G4 and NZBC F7 — use a licensed installer."
    ),
    "architects": (
        "Architects in {city} typically charge 8–15% of construction cost for residential design, "
        "or a fixed fee of $5,500–$28,000+ for smaller projects. {context} An architect adds most "
        "value on complex or high-value projects — for simple alterations a building designer may "
        "be more cost-effective."
    ),
    "excavators": (
        "Excavation in {city} typically costs $185–$230/hr with operator, $38–$70/m³ disposed for "
        "a site cut, and $900–$3,500 for foundation excavation. {context} Confirm spoil disposal "
        "is included — tipping fees and cartage can add significantly to the cost."
    ),
    "steel-fabricators": (
        "Steel fabricators in {city} typically charge $130–$260/m for structural beams installed and "
        "$400–$950/m for balustrades. Steel portal frame buildings run $38,000–$85,000+. {context} "
        "Always verify the fabricator holds current IQP or SCNZ certification for structural work."
    ),
    "cabinet-makers": (
        "Cabinet makers in {city} typically charge $1,600–$3,200/m run for custom kitchen cabinetry, "
        "$900–$2,700/m for custom wardrobes, and higher rates for commercial joinery. {context} "
        "Lead times for custom joinery are typically 8–14 weeks — factor this into your project schedule."
    ),
    "garage-door-installers": (
        "Garage door installers in {city} typically charge $1,900–$3,700 for a single automated roller "
        "door and $3,200–$7,000 for a double panel-lift door, supply and install. {context} Motor "
        "warranty and service response time are worth comparing alongside price."
    ),
    "locksmiths": (
        "Locksmiths in {city} typically charge $130–$270 for a standard lockout callout, $160–$480 "
        "for a new lock supply and fit, and $650–$2,800+ for a master key system. {context} "
        "After-hours callout fees are common — confirm rates before booking an emergency job."
    ),
    "bricklayers": (
        "Bricklayers in {city} typically charge $125–$190/m² for single-skin brickwork, $115–$170/m² "
        "for blockwork, and $210–$420/m² for heritage restoration. {context} Brick is less common in "
        "NZ new builds but remains popular for retaining walls, paving, and heritage restoration."
    ),
    "window-installers": (
        "Window installers in {city} typically charge $650–$1,600 per aluminium double-glazed window "
        "installed, and $16,000–$48,000+ to re-window a full house. {context} All windows must comply "
        "with NZ Building Code H1 energy efficiency requirements — confirm your installer uses compliant products."
    ),
    "irrigation-specialists": (
        "Irrigation specialists in {city} typically charge $2,700–$6,500 for a residential lawn "
        "system and $8–$20/m² for drip irrigation, installed. {context} A well-designed irrigation "
        "system pays for itself in water savings and plant health within 3–5 years."
    ),
    "pool-builders": (
        "Pool builders in {city} typically quote $36,000–$75,000 for a fibreglass pool installed and "
        "$52,000–$130,000+ for a concrete/gunite pool. Above-ground pools start from $3,500. {context} "
        "Building consent is required for most in-ground pools in NZ — confirm your builder handles "
        "consent and fencing compliance."
    ),
    "asphalt-contractors": (
        "Asphalt contractors in {city} typically charge $85–$140/m² for an asphalt driveway and "
        "$28–$60/m² for chip seal. {context} Get a written quote that specifies base preparation — "
        "a well-prepared sub-base is the key to a long-lasting driveway."
    ),
    "interior-designers": (
        "Interior designers in {city} typically charge $110–$190/hr or 10–20% of project value. "
        "A full residential interior design project typically costs $6,000–$35,000+ in fees. {context} "
        "Scope the engagement carefully — hourly rates suit small consultations; percentage-of-project "
        "suits full-service renovations."
    ),
    "surveyors": (
        "Surveyors in {city} typically charge $1,300–$3,800 for a boundary survey, $4,500–$28,000+ "
        "for subdivision, and $900–$2,800 for a building setout. {context} Title searches and LIM "
        "reports are recommended before any boundary-related work — your surveyor can advise."
    ),
    "stonemasons": (
        "Stonemasons in {city} typically charge $360–$750/m² for natural stone walls, $210–$480/m² "
        "for stone paving, and $420–$950/m² for heritage restoration. {context} Heritage stonework "
        "requires specialist skills — always check the mason's portfolio of similar work."
    ),
    "timber-floor-specialists": (
        "Timber floor specialists in {city} typically charge $155–$295/m² for solid hardwood supply "
        "and install, and $28–$60/m² for sanding and polishing existing floors. {context} Engineered "
        "timber floors are often more cost-effective in areas prone to humidity changes."
    ),
    "drainage-specialists": (
        "Drainage specialists in {city} typically charge $85–$160/m for French drains, $1,600–$4,200 "
        "for soakpits, and $5,500–$28,000+ for full site drainage. {context} Poor site drainage is "
        "one of the most common causes of foundation problems — a drainage assessment is worthwhile "
        "before any significant earthworks."
    ),
    "cladding-installers": (
        "Cladding installers in {city} typically charge $125–$190/m² for primed pine weatherboard, "
        "$105–$170/m² for fibre cement, and $190–$295/m² for brick veneer. {context} Weathertightness "
        "is critical — use only licensed builders for restricted building work on cladding."
    ),
    "lighting-specialists": (
        "Lighting specialists in {city} typically charge $2,600–$6,500 for a full-house LED upgrade "
        "(supply and install), $420–$1,900/circuit for outdoor lighting, and $155–$265/hr for "
        "commercial lighting design. {context} All electrical work must be done by a registered "
        "electrician — lighting specialists who aren't electricians can only advise, not install."
    ),
    "commercial-cleaners": (
        "Commercial cleaners in {city} typically charge $32–$58/hr for office cleaning, $2–$6/m² "
        "for construction cleans, and $3–$9/m² for high-pressure washing. {context} Confirm whether "
        "cleaning products, equipment, and waste disposal are included in the quoted rate."
    ),
    "quantity-surveyors": (
        "Quantity surveyors in {city} typically charge $2,200–$9,000 for a construction cost estimate "
        "and 1–3% of construction cost for contract administration. {context} A QS is most valuable "
        "on projects over $200,000 — they typically save more than their fee through better cost "
        "control and contract management."
    ),
    # Already-done trades (for pool-builders missing 1 city, carpet-layers missing 1)
    "carpet-layers": (
        "Carpet layers in {city} typically charge $35–$65/m² supply and lay for mid-range carpet, "
        "with premium wool carpet running $80–$180/m². Underlay is additional at $8–$20/m². {context} "
        "Get quotes that include underlay, gripper rods, and door trims — these are often excluded."
    ),
}


def make_note(trade_slug, city_name, city_slug):
    template = TRADE_NOTES.get(trade_slug)
    if not template:
        return f"{city_name} {trade_slug.replace('-', ' ')} pricing varies — always get at least 3 written quotes for your job."
    ctx = CITY_CONTEXT.get(city_slug, ("average", "Rates are broadly in line with the national average."))
    return template.format(city=city_name, context=ctx[1])


def main():
    with open(BASE / "data" / "trades.json") as f:
        trades = json.load(f)
    with open(BASE / "data" / "cities.json") as f:
        cities = json.load(f)

    existing = set(os.listdir(TOP10_DIR))
    generated = 0

    for trade in trades:
        for city in cities:
            fname = f"{trade['slug']}-{city['slug']}.json"
            if fname in existing:
                continue  # already exists

            note = make_note(trade["slug"], city["name"], city["slug"])
            stub = {
                "trade": trade["slug"],
                "city": city["slug"],
                "updated": TODAY,
                "regional_cost_note": note,
                "businesses": []
            }
            out = TOP10_DIR / fname
            out.write_text(json.dumps(stub, indent=2, ensure_ascii=False))
            generated += 1

    print(f"Generated {generated} stub files.")
    # Verify
    total = sum(1 for _ in os.listdir(TOP10_DIR) if _.endswith(".json"))
    print(f"Total top10 files now: {total} (expected 940)")


if __name__ == "__main__":
    main()
