#!/usr/bin/env python3
"""
Scrape NoCowboys directory for unclaimed listing candidates.
Targets 5 trades x 3 cities = 15 combos, up to 40 listings each → ~600 candidates.
Outputs: outreach/listings_to_seed.csv

Run: cd outreach && python scrape_nocowboys.py
"""
import csv, re, time, random
from pathlib import Path
from playwright.sync_api import sync_playwright

OUTPUT = Path(__file__).parent / "listings_to_seed.csv"
LOG    = Path(__file__).parent / "scrape_nocowboys.log"

TRADES = [
    ("builders",        "builders"),
    ("plumbers",        "plumbers"),
    ("electricians",    "electricians"),
    ("painters",        "painters"),
    ("roofers",         "roofers"),
]

REGIONS = [
    ("auckland",        "Auckland"),
    ("wellington",      "Wellington"),
    ("christchurch",    "Christchurch"),
]

# Map our trade slugs to NoCowboys category slugs
NC_TRADE_MAP = {
    "builders":      "builders",
    "plumbers":      "plumbers",
    "electricians":  "electricians",
    "painters":      "painters-decorators",
    "roofers":       "roofers",
}

NC_REGION_MAP = {
    "auckland":      "auckland",
    "wellington":    "wellington",
    "christchurch":  "christchurch",
}

BASE = "https://www.nocowboys.co.nz"
PER_PAGE = 40


def log(msg):
    print(msg)
    with LOG.open("a") as f:
        f.write(msg + "\n")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def scrape_page(page, trade_slug, region_slug, offset=0):
    """Scrape one page of NoCowboys results. Returns list of dicts."""
    nc_trade  = NC_TRADE_MAP.get(trade_slug, trade_slug)
    nc_region = NC_REGION_MAP.get(region_slug, region_slug)
    url = f"{BASE}/search?q={nc_trade}&location={nc_region}&page={offset // PER_PAGE + 1}"

    try:
        page.goto(url, timeout=25000, wait_until="networkidle")
        time.sleep(random.uniform(2.0, 3.5))
    except Exception as e:
        log(f"  Page load error: {e}")
        return []

    results = []

    # NoCowboys uses a CSS typo: "businsess-search-business" (confirmed Jun 2026)
    cards = page.query_selector_all(".businsess-search-business")

    log(f"  Found {len(cards)} cards on page")

    for card in cards:
        try:
            # Business name + profile URL
            name_el = card.query_selector("h3 a, h2 a")
            if not name_el:
                continue
            name = name_el.inner_text().strip()
            if not name:
                continue
            href = name_el.get_attribute("href") or ""
            # Strip UTM params, build absolute URL
            href = re.sub(r"\?.*$", "", href)
            nc_url = href if href.startswith("http") else BASE + href

            # Rating + review count from ".rating-summary" text
            # Format: "100% from 25 ratings – Located in ..."
            rating = 0.0
            review_count = 0
            summary_el = card.query_selector(".rating-summary")
            if summary_el:
                txt = summary_el.inner_text()
                pct_m = re.search(r"(\d+)%", txt)
                rev_m = re.search(r"from (\d+) rating", txt)
                if pct_m:
                    rating = round(float(pct_m.group(1)) / 20, 1)  # 100% → 5.0
                if rev_m:
                    review_count = int(rev_m.group(1))

            # Location text from rating-summary (after "Located in")
            location_text = ""
            if summary_el:
                loc_m = re.search(r"Located in ([^–\n]+)", summary_el.inner_text())
                if loc_m:
                    location_text = loc_m.group(1).strip()

            results.append({
                "name":          name,
                "trade":         trade_slug,
                "region":        REGIONS[[r[0] for r in REGIONS].index(region_slug)][1],
                "phone":         "",
                "nocowboys_url": nc_url,
                "avg_rating":    rating,
                "review_count":  review_count,
                "location_raw":  location_text,
            })

        except Exception as e:
            log(f"    Card parse error: {e}")
            continue

    return results


def scrape_detail(page, nc_url):
    """Visit a NoCowboys profile page to get extra detail (phone, rating)."""
    if not nc_url:
        return {}
    try:
        page.goto(nc_url, timeout=15000, wait_until="domcontentloaded")
        time.sleep(random.uniform(1.0, 2.0))

        phone = ""
        phone_el = page.query_selector("[class*='phone'], [href^='tel:']")
        if phone_el:
            phone = (phone_el.get_attribute("href") or phone_el.inner_text() or "").replace("tel:", "").strip()

        rating = 0.0
        rating_el = page.query_selector("[class*='rating-value'], [class*='score-value'], [itemprop='ratingValue']")
        if rating_el:
            m = re.search(r"[\d.]+", rating_el.inner_text())
            if m:
                rating = float(m.group())

        review_count = 0
        review_el = page.query_selector("[class*='review-count'], [itemprop='reviewCount']")
        if review_el:
            m = re.search(r"\d+", review_el.inner_text())
            if m:
                review_count = int(m.group())

        return {"phone": phone, "avg_rating": rating, "review_count": review_count}
    except Exception:
        return {}


def main():
    LOG.write_text("")  # clear log
    all_rows = []
    seen_names = set()

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
        )
        page = ctx.new_page()

        for trade_slug, trade_label in TRADES:
            for region_slug, region_label in REGIONS:
                log(f"\n[{trade_label} / {region_label}]")
                results = scrape_page(page, trade_slug, region_slug)

                new = 0
                for r in results:
                    key = slugify(r["name"])
                    if key in seen_names:
                        continue
                    seen_names.add(key)
                    all_rows.append(r)
                    new += 1

                log(f"  → {new} new listings (total so far: {len(all_rows)})")
                time.sleep(random.uniform(2.0, 4.0))

        browser.close()

    if not all_rows:
        log("\nNo listings scraped — NoCowboys may have changed their HTML. Check selectors.")
        return

    # Write CSV
    fields = ["name", "trade", "region", "phone", "nocowboys_url", "avg_rating", "review_count", "location_raw"]
    with OUTPUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    log(f"\nDone. {len(all_rows)} listings saved to {OUTPUT}")


if __name__ == "__main__":
    main()
