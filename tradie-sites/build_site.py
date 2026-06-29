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
    "brand_color":    "#1d4ed8",
    "brand_dark":     "#1e3a8a",
    "services": [
        {"name": "Concrete Driveways",      "description": "New installations and replacements — plain, exposed aggregate or coloured."},
        {"name": "Pathways & Footpaths",    "description": "Durable paths that complement your property and stand up to Dunedin's climate."},
        {"name": "Concrete Slabs",          "description": "Garage floors, shed pads, pergola bases and more. Levelled and finished to spec."},
        {"name": "Decorative Concrete",     "description": "Exposed aggregate, stamped and coloured concrete for a premium finish."},
        {"name": "Concrete Removal",        "description": "Break-up and removal of old concrete before your new pour."},
        {"name": "Repairs & Resurfacing",   "description": "Crack filling, grinding and resurfacing to restore tired concrete surfaces."},
    ],
    "sample_reviews": [
        {"rating": 5, "author": "Sarah M.",   "text": "Absolutely brilliant job on our driveway. Turned up on time, cleaned up perfectly and the finished result looks amazing."},
        {"rating": 5, "author": "John D.",    "text": "Used Dunners Concrete for a new slab and pathway. Professional from start to finish — highly recommend."},
        {"rating": 5, "author": "Rachel T.",  "text": "Great communication throughout the whole job. The concrete work is top quality and priced fairly."},
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
