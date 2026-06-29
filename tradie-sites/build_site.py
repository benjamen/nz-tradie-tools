#!/usr/bin/env python3
"""
Build a tradie website from a data dict and the Jinja2 template.

Usage:
  python3 build_site.py                    # builds Dunners Concrete (demo)
  python3 build_site.py --listing-id 2843  # build from TradieTools listing
"""
import json, sys, shutil, datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = Path(__file__).parent / "template"
OUTPUT_DIR   = Path(__file__).parent / "output"

jinja = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=True,
)
jinja.filters['tojson'] = json.dumps


def build(business: dict, slug: str):
    out = OUTPUT_DIR / slug
    out.mkdir(parents=True, exist_ok=True)

    tpl = jinja.get_template("index.html")
    html = tpl.render(business=business, year=datetime.date.today().year)
    (out / "index.html").write_text(html, encoding="utf-8")

    static_src = TEMPLATE_DIR / "static"
    static_dst = out / "static"
    if static_src.exists():
        if static_dst.exists():
            shutil.rmtree(static_dst)
        shutil.copytree(static_src, static_dst)

    print(f"Built → {out}/index.html")
    return out


# ── Demo data for Dunners Concrete ───────────────────────────────────────────

DUNNERS = {
    "name":           "Dunners Concrete Contractor Services",
    "trade_label":    "concrete contractor",
    "api_trade":      "concreter",
    "region":         "Dunedin",
    "phone":          "03 242 03176",
    "email":          "dunnersconcrete@gmail.com",
    "tagline":        "Connecting You With Certified Concrete Experts In Dunedin City!",
    "meta_description": (
        "Dunners Concrete Contractor Services — Dunedin's top-rated concrete "
        "specialists. 5.0 stars across 32 Google reviews. Driveways, paths, slabs, "
        "decorative concrete. Free quotes."
    ),
    "canonical_url":  "https://dunnersconcrete.co.nz",
    "rating":         5.0,
    "review_count":   32,
    "google_url":     "https://maps.google.com/?cid=15160777677105593767",
    "logo_url":       "https://lirp.cdn-website.com/4d49136a/dms3rep/multi/opt/Logo+Dunners+Concrete-1920w.png",
    "brand_color":    "#293d4c",
    "brand_dark":     "#1d2b36",
    "cta_color":      "#ff8400",
    "cta_dark":       "#e07400",
    "services": [
        {"name": "Concrete Driveways",    "url": "https://www.dunnersconcrete.co.nz/concrete-driveway",      "description": "Our experienced driveway concreters transform entrances with durable, custom-designed concrete driveways that Dunedin homeowners trust for decades of reliable service."},
        {"name": "Concrete Paths",        "url": "https://www.dunnersconcrete.co.nz/concrete-path",          "description": "Our path contractors create beautiful, functional footpaths that enhance property accessibility while complementing the aesthetic appeal of your landscape."},
        {"name": "Concrete Patios",       "url": "https://www.dunnersconcrete.co.nz/concrete-patio",         "description": "We craft stunning patios and porch slabs that transform your outdoor space into an ideal entertainment area, tailored to Dunedin's unique climate."},
        {"name": "Pads & Slabs",          "url": "https://www.dunnersconcrete.co.nz/garage/shed-slab/pad",   "description": "From garage and shed slabs to equipment foundations — perfectly level, reinforced surfaces built to local specifications."},
        {"name": "Retaining Walls",       "url": "https://www.dunnersconcrete.co.nz/retaining-wall",         "description": "Our specialists create structurally sound retaining walls that manage slopes while enhancing your property's usable space."},
        {"name": "Decorative Concrete",   "url": "https://www.dunnersconcrete.co.nz/decorative-concrete",    "description": "Exposed aggregate, broom, swirl, and coloured concrete options that combine practicality with distinctive artistic applications."},
        {"name": "Car Park Construction", "url": "https://www.dunnersconcrete.co.nz/car-park-construction",  "description": "From residential carports to commercial parking lots — durable surfaces engineered for heavy vehicle traffic and Otago's weather conditions."},
        {"name": "Commercial Concrete",   "url": "https://www.dunnersconcrete.co.nz/commercial-concrete",    "description": "Foundations, flooring, and infrastructure projects for Dunedin businesses, delivered on schedule with minimal disruption to operations."},
    ],
    "about": [
        "Dunners Concrete Contractor Services delivers high-quality concrete solutions across Dunedin City and surrounding areas. As local concrete contractors, we understand how to handle both residential and commercial projects — from proper excavation preparations through to finishing and curing.",
        "We specialise in concrete driveways, footpaths, patios, pads and slabs, retaining walls, decorative finishes, car parks, and commercial concrete. Dunedin's unique terrain — volcanic hills, coastal conditions, and clay soils — demands concrete mixes and techniques that most contractors don't understand. We do. Our mixes are specifically formulated for Dunedin's 724mm annual rainfall, varying soil types, and coastal salt exposure, ensuring results that last decades.",
        "Want to make your home stand out? Think exposed aggregate driveways that catch the light, or coloured concrete paths that complement Dunedin's greens. Whether you're after a practical broom finish or something more decorative, we have the options and expertise to deliver.",
    ],
    "process": [
        {"title": "Project Discovery", "description": "After your enquiry, Connor arranges a quick consult to confirm purpose, timing, and budget. We review access, drainage, and site constraints, then match you with experienced concrete contractors best suited to your project."},
        {"title": "Three Professional Estimates", "description": "Contractor teams visit to verify measurements, levels, and base requirements, and to confirm reinforcement and finish expectations. You'll receive three tailored proposals outlining methodology, materials, timelines, and pricing."},
        {"title": "Your Confident Decision", "description": "Each submission includes itemised costs, realistic schedules, clear inclusions, and notes on curing and aftercare. With our guidance, you select the option that balances performance and budget, then lock in dates for completion."},
    ],
    "pricing": {
        "title": "Concrete Costs & Pricing Guide for Dunedin",
        "range": "$90–$200/m²",
        "range_note": "Indicative range for most surface projects (driveways, paths, patios, slabs, car parks). Final pricing is determined by your contractor following a site visit.",
        "drivers": [
            "Excavation depth and base preparation",
            "Site access for equipment and concrete trucks",
            "Slab thickness and reinforcement spec",
            "Layout complexity, edges, steps, or awkward shapes",
            "Finish choice — broom/swirl through to exposed aggregate or coloured",
            "Demolition, spoil removal, and reinstatement",
            "Drainage allowances and joint layout",
        ],
        "timeframes": [
            "Preparation and boxing: 1–3 days",
            "Pour and finish: typically 1 day",
            "Light foot traffic: 24–48 hours",
            "Vehicles and loads: 5–7 days",
        ],
        "disclaimer": "Pricing guidance only. Each contractor prepares their own independent quote following a site visit. Confirm whether quotes are GST-inclusive or exclusive.",
    },
    "areas": ["South Dunedin", "St Clair", "Mornington", "North Dunedin", "Mosgiel", "Port Chalmers", "Roslyn", "Dunedin City"],
    "google_business_url": "https://maps.app.goo.gl/S1dhLxZUYRNNxgHv9",
    "form_success_hints": [
        "Approximate measurements in metres (length × width) helps speed things up",
        "Photos of the existing area are always useful",
        "Note any access details — can a concrete truck or digger get close?",
    ],
    "sample_reviews": [
        {"rating": 5, "author": "Sarah M.",   "text": "Absolutely brilliant job on our driveway. Turned up on time, cleaned up perfectly and the finished result looks amazing."},
        {"rating": 5, "author": "John D.",    "text": "Used Dunners Concrete for a new slab and pathway. Professional from start to finish — highly recommend."},
        {"rating": 5, "author": "Rachel T.",  "text": "Great communication throughout the whole job. The concrete work is top quality and priced fairly."},
    ],
    "form_fields": [
        {"type": "row_start"},
        {"type": "text",  "name": "name",    "label": "First & Last Name",      "required": True,  "placeholder": "Jane Smith"},
        {"type": "tel",   "name": "phone",   "label": "Phone Number",           "required": True,  "placeholder": "021 000 000"},
        {"type": "row_end"},
        {"type": "text",  "name": "address", "label": "Project Street Address", "required": True,  "placeholder": "123 Main St, South Dunedin"},
        {"type": "email", "name": "email",   "label": "Email Address",          "required": False, "placeholder": "jane@example.com"},
        {"type": "checkboxes", "name": "project_type", "label": "Project Type",
         "description": "What type of project do you need help with?",
         "options": ["Concrete Driveway", "Concrete Path", "Concrete Patio",
                     "Concrete Pad/Slab", "Retaining Wall", "Concrete Car Park"],
         "required": False},
        {"type": "checkboxes", "name": "finish_type", "label": "Concrete Finish",
         "description": "What type of finish are you interested in?",
         "options": ["Plain Concrete", "Broom Finish", "Swirl Finish",
                     "Exposed Aggregate", "Coloured Concrete", "Pavers"],
         "required": False},
        {"type": "radio", "name": "excavation", "label": "Excavation / Removal",
         "description": "Is excavation or removal work required?",
         "options": ["Yes", "No"],
         "required": False},
        {"type": "radio", "name": "budget", "label": "Project Range (Optional)",
         "description": "This helps us understand the price range you're working within, so we can recommend the right approach.",
         "options": ["Below $4,999", "$5,000 to $9,999", "$10,000 to $19,999", "$20,000 +", "Not Sure / Please Guide Me"],
         "required": False},
        {"type": "radio", "name": "timeline", "label": "Timeline",
         "description": "When are you hoping to start your project?",
         "options": ["As soon as possible", "In the next 1–3 months", "In 3+ months", "Just planning for now"],
         "required": False},
        {"type": "textarea", "name": "description", "label": "Tell Us More About Your Project",
         "description": "Once you submit the form, we may ask for more details and photos.",
         "placeholder": "e.g. New concrete driveway, approximately 80m², replacing existing cracked concrete...",
         "required": False},
        {"type": "checkboxes", "name": "contact_method", "label": "Preferred Contact Method",
         "options": ["Phone Call", "Text", "Email"],
         "required": False},
    ],
}


if __name__ == "__main__":
    import argparse, requests

    parser = argparse.ArgumentParser()
    parser.add_argument("--listing-id", type=int, help="TradieTools listing ID to fetch")
    parser.add_argument("--slug",       type=str, help="Output folder name (default: derived from name)")
    args = parser.parse_args()

    if args.listing_id:
        print(f"Fetching listing {args.listing_id} from TradieTools API…")
        r = requests.get(
            "https://tradietools.optified.nz/api/method/tradietools.api.get_tradie_home",
            params={"listing_id": args.listing_id},
            timeout=10,
        )
        data = r.json().get("message", {})
        # Map API fields → template fields (basic, expand as API grows)
        biz = {
            "name":           data.get("name", ""),
            "trade_label":    data.get("trade", "tradie").rstrip("s"),
            "api_trade":      data.get("trade", "").rstrip("s"),
            "region":         data.get("region", ""),
            "phone":          data.get("phone", ""),
            "email":          data.get("contact_email", "").replace("@noemail.tradietools.nz", "") or "",
            "tagline":        data.get("tagline") or f"Professional {data.get('trade','tradie')} in {data.get('region','NZ')}",
            "meta_description": data.get("description") or f"Top-rated {data.get('trade','')} in {data.get('region','NZ')} — free quotes.",
            "canonical_url":  f"https://tradietools.nz/businesses/{data.get('listing_slug','')}",
            "rating":         data.get("avg_rating") or data.get("google_rating") or 5.0,
            "review_count":   data.get("review_count") or data.get("google_reviews") or 0,
            "google_url":     data.get("google_url", ""),
            "brand_color":    "#1d4ed8",
            "brand_dark":     "#1e3a8a",
            "services":       [],
            "sample_reviews": [],
        }
        slug = args.slug or data.get("listing_slug", f"listing-{args.listing_id}")
        build(biz, slug)
    else:
        slug = args.slug or "dunners-concrete"
        build(DUNNERS, slug)
        print("Open: tradie-sites/output/dunners-concrete/index.html")
