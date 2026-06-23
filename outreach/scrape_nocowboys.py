#!/usr/bin/env python3
"""
Scrape NoCowboys directory for unclaimed listing candidates.
Targets 10 NZ cities × 3 pages = ~300 raw results → ~280 unique after dedup.
Trade is parsed from the card itself (NoCowboys trade query doesn't filter results).
Outputs: outreach/listings_to_seed.csv

Run: cd outreach && python scrape_nocowboys.py
"""
import csv, re, time, random
from pathlib import Path
from playwright.sync_api import sync_playwright

OUTPUT = Path(__file__).parent / "listings_to_seed.csv"
LOG    = Path(__file__).parent / "scrape_nocowboys.log"

# 10 NZ cities — NoCowboys uses lowercase slugs
REGIONS = [
    ("auckland",          "Auckland"),
    ("wellington",        "Wellington"),
    ("christchurch",      "Christchurch"),
    ("hamilton",          "Hamilton"),
    ("tauranga",          "Tauranga"),
    ("dunedin",           "Dunedin"),
    ("palmerston-north",  "Palmerston North"),
    ("nelson",            "Nelson"),
    ("napier",            "Napier"),
    ("whangarei",         "Whangarei"),
]

PAGES_PER_REGION = 3   # 10 results per page → up to 30 per city

BASE = "https://www.nocowboys.co.nz"

# Map NoCowboys trade strings → our trade slugs
TRADE_MAP = {
    "builder":       "builders",
    "construction":  "builders",
    "plumber":       "plumbers",
    "drain":         "plumbers",
    "electric":      "electricians",
    "paint":         "painters",
    "decorator":     "painters",
    "roof":          "roofers",
    "glazier":       "glaziers",
    "landscape":     "landscapers",
    "fence":         "fencers",
    "carpet":        "carpet-layers",
    "heat pump":     "heat-pump-installers",
    "solar":         "solar-installers",
    "scaffold":      "scaffolders",
    "waterproof":    "waterproofers",
    "plaster":       "plasterers",
    "tiler":         "tilers",
    "tiling":        "tilers",
    "concret":       "concreters",
    "excavat":       "excavators",
    "arborist":      "arborists",
    "tree":          "arborists",
    "insul":         "insulators",
    "alarm":         "security",
    "security":      "security",
    "clean":         "cleaners",
    "gas":           "gasfitters",
    "drain":         "drainlayers",
    "drainlay":      "drainlayers",
}


def log(msg):
    print(msg)
    with LOG.open("a") as f:
        f.write(msg + "\n")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_trade(summary_text):
    """Extract trade slug from NoCowboys rating-summary text.
    Format: '100% from N ratings – Located in Suburb (Xkm) – Trade Name / Sub-trade'
    """
    # Get the part after the last " – "
    parts = re.split(r"\s*[–-]\s*", summary_text)
    trade_raw = parts[-1].strip().lower() if parts else ""
    for keyword, slug in TRADE_MAP.items():
        if keyword in trade_raw:
            return slug
    # Fallback: use first word of trade string, slugified
    first_word = re.sub(r"[^a-z0-9]+", "-", trade_raw.split("/")[0].strip()).strip("-")
    return first_word or "other"


def scrape_page(page, region_slug, region_label, page_num):
    """Scrape one page of NoCowboys results for a city. Returns list of dicts."""
    url = f"{BASE}/search?location={region_slug}&page={page_num}"

    try:
        page.goto(url, timeout=25000, wait_until="networkidle")
        time.sleep(random.uniform(1.8, 3.0))
    except Exception as e:
        log(f"  Page load error: {e}")
        return []

    cards = page.query_selector_all(".businsess-search-business")
    log(f"  Page {page_num}: {len(cards)} cards")

    results = []
    for card in cards:
        try:
            name_el = card.query_selector("h3 a, h2 a")
            if not name_el:
                continue
            name = name_el.inner_text().strip()
            if not name:
                continue

            href = name_el.get_attribute("href") or ""
            href = re.sub(r"\?.*$", "", href)
            nc_url = href if href.startswith("http") else BASE + href

            rating = 0.0
            review_count = 0
            trade = "other"
            summary_el = card.query_selector(".rating-summary")
            if summary_el:
                txt = summary_el.inner_text()
                pct_m = re.search(r"(\d+)%", txt)
                rev_m = re.search(r"from (\d+) rating", txt)
                if pct_m:
                    rating = round(float(pct_m.group(1)) / 20, 1)
                if rev_m:
                    review_count = int(rev_m.group(1))
                trade = parse_trade(txt)

            results.append({
                "name":          name,
                "trade":         trade,
                "region":        region_label,
                "phone":         "",
                "nocowboys_url": nc_url,
                "avg_rating":    rating,
                "review_count":  review_count,
            })

        except Exception as e:
            log(f"    Card parse error: {e}")
            continue

    return results


def main():
    LOG.write_text("")
    all_rows = []
    seen = set()  # name|region

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
        )
        page = ctx.new_page()

        for region_slug, region_label in REGIONS:
            log(f"\n=== {region_label} ===")
            region_new = 0
            for page_num in range(1, PAGES_PER_REGION + 1):
                results = scrape_page(page, region_slug, region_label, page_num)
                new = 0
                for r in results:
                    key = f"{slugify(r['name'])}|{region_label.lower()}"
                    if key in seen:
                        continue
                    seen.add(key)
                    all_rows.append(r)
                    new += 1
                region_new += new
                log(f"  → {new} new (running total: {len(all_rows)})")
                if len(results) < 8:
                    log(f"  Short page — stopping pagination for {region_label}")
                    break
                time.sleep(random.uniform(2.0, 3.5))

            log(f"  {region_label} total: {region_new} new listings")
            time.sleep(random.uniform(1.5, 3.0))

        browser.close()

    if not all_rows:
        log("\nNo listings scraped — check selectors.")
        return

    fields = ["name", "trade", "region", "phone", "nocowboys_url", "avg_rating", "review_count"]
    with OUTPUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    # Summary by region and trade
    from collections import Counter
    by_region = Counter(r["region"] for r in all_rows)
    by_trade  = Counter(r["trade"]  for r in all_rows)
    log(f"\nDone. {len(all_rows)} listings saved to {OUTPUT}")
    log("By region: " + ", ".join(f"{k}={v}" for k, v in by_region.most_common()))
    log("By trade:  " + ", ".join(f"{k}={v}" for k, v in by_trade.most_common(10)))


if __name__ == "__main__":
    main()
