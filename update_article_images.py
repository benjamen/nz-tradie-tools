#!/usr/bin/env python3
"""
Assign trade-specific Unsplash images to all article markdown files.
Replaces the generic catch-all photo-1558618666-fcd25c85cd64 and ensures
each trade type has a visually distinct, relevant image.

Run: python3 update_article_images.py
"""
import re
from pathlib import Path

ARTICLES = Path(__file__).parent / "content" / "articles"

BASE = "https://images.unsplash.com/{photo}?w=1200&h=630&fit=crop&auto=format"

# Trade slug → Unsplash photo ID
TRADE_IMAGES = {
    "electrician":              "photo-1621905252472-943afaa20e20",  # electrical panel wiring
    "plumber":                  "photo-1507679799987-c73779587ccf",  # plumber pipes under sink
    "builder":                  "photo-1504307651254-35680f356dfd",  # construction framing
    "painter":                  "photo-1504328345606-18bbc8c9d7d1",  # painter rolling wall
    "roofer":                   "photo-1562259949-e8e7689d7828",     # roofer on roof
    "handyman":                 "photo-1605100804763-247f67b3557e",  # handyman tools belt
    "tiler":                    "photo-1600585154526-990dced4db0d",  # tiling floor
    "landscaper":               "photo-1416879595882-3373a0480b5b",  # garden/landscaping
    "arborist":                 "photo-1535192025727-0d7aaf27a9db",  # tree surgery
    "solar-installer":          "photo-1509391366360-2e959784a276",  # solar panels on roof
    "bathroom-renovator":       "photo-1552321554-5fefe8c9ef14",     # modern bathroom
    "kitchen-renovator":        "photo-1556909114-f6e7ad7d3136",     # modern kitchen
    "deck-builder":             "photo-1449844908441-8829872d2607",  # timber deck outdoor
    "pool-builder":             "photo-1576013551627-0cc20b96c2a7",  # swimming pool
    "pergola-builder":          "photo-1558908067-dd0e7b4ed52e",     # garden pergola
    "carpenter":                "photo-1504307651254-35680f356dfd",  # woodworking construction
    "drainlayer":               "photo-1607472586893-edb57bdc0e39",  # drainage pipes
    "gasfitter":                "photo-1607472586893-edb57bdc0e39",  # pipes/gas fitting
    "glazier":                  "photo-1555041469-a586c61ea9bc",     # window glass installation
    "floor-sander":             "photo-1571115177098-24ec42ed204d",  # timber floor sanding
    "carpet-layer":             "photo-1600210492486-724fe5c67fb0",  # carpet installation
    "insulation-installer":     "photo-1584225064536-4d0abe013e95",  # insulation batts
    "plasterer":                "photo-1558618047-3c8c76ca7d13",     # plastering wall
    "concreter":                "photo-1584536702729-f5bbb3be2d30",  # concrete pour
    "fence-installer":          "photo-1580281657702-257584239a55",  # timber fence
    "house-washer":             "photo-1604328702728-d26d2062c20a",  # pressure washing house
    "rubbish-removal":          "photo-1558618047-3c8c76ca7d13",     # skip bin / demo
    "pest-control":             "photo-1583852151376-4d6d654e6e25",  # pest control spray
    "locksmith":                "photo-1558618047-3c8c76ca7d13",     # lock and key
    "heat-pump-installer":      "photo-1631545804879-ae80498e6e7e",  # heat pump outdoor unit
    "switchboard-upgrade":      "photo-1621905252472-943afaa20e20",  # electrical switchboard
    "ev-charger-installation":  "photo-1593941707882-a5bba14938c7",  # EV charger plug
    "security-alarm":           "photo-1558618047-3c8c76ca7d13",     # security
}

def get_trade_from_slug(slug: str) -> str | None:
    """Extract trade type from article slug like 'electrician-auckland-nz'."""
    for trade in sorted(TRADE_IMAGES.keys(), key=len, reverse=True):
        if slug.startswith(trade):
            return trade
    return None

IMAGE_RE = re.compile(r'^(image:\s*["\']?)https://images\.unsplash\.com/[^?"\'\n]+(\?[^"\'\n]*)?(["\']?)$', re.MULTILINE)

def update_file(path: Path, new_url: str) -> bool:
    text = path.read_text(encoding="utf-8")
    # Match the image: line and replace the URL portion
    new_line = f'image: "{new_url}"'
    updated = IMAGE_RE.sub(new_line, text)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False

if __name__ == "__main__":
    updated = skipped = unchanged = 0
    for md in sorted(ARTICLES.glob("*.md")):
        slug = md.stem
        trade = get_trade_from_slug(slug)
        if not trade:
            unchanged += 1
            continue
        url = BASE.format(photo=TRADE_IMAGES[trade])
        if update_file(md, url):
            print(f"  update  {slug}  → {trade}")
            updated += 1
        else:
            skipped += 1
    print(f"\nDone: {updated} updated, {skipped} already correct, {unchanged} no trade match")
