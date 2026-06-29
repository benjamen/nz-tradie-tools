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
        {"name": "Concrete Driveways",      "description": "New installations and replacements — plain, exposed aggregate or coloured."},
        {"name": "Concrete Paths & Patios", "description": "Durable paths and outdoor living areas that complement your property."},
        {"name": "Concrete Slabs",          "description": "Garage floors, shed pads, pergola bases and more. Levelled and finished to spec."},
        {"name": "Decorative Concrete",     "description": "Exposed aggregate, broom, swirl and coloured finishes for a premium look."},
        {"name": "Retaining Walls",         "description": "Solid concrete retaining walls to manage slopes and protect your land."},
        {"name": "Excavation & Removal",    "description": "Break-up and removal of old concrete before your new pour."},
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
