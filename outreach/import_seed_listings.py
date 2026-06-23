#!/usr/bin/env python3
"""
Import scraped NoCowboys listings into TradieTools as unclaimed listings.

Prerequisites:
  1. Run scrape_nocowboys.py first → produces listings_to_seed.csv
  2. Add frappe_seed_endpoint.py code to server api.py and restart frappe

Run: cd outreach && python import_seed_listings.py [--dry-run]
"""
import csv, json, sys, time, requests
from pathlib import Path

INPUT      = Path(__file__).parent / "listings_to_seed.csv"
IMPORT_LOG = Path(__file__).parent / "import_seed.log"
API_URL    = "https://tradietools.optified.nz/api/method/tradietools.api.seed_unclaimed_listing"
BATCH_SIZE = 20   # listings per API call
DRY_RUN    = "--dry-run" in sys.argv

def log(msg):
    print(msg)
    with IMPORT_LOG.open("a") as f:
        f.write(msg + "\n")


def send_batch(rows):
    """POST a batch of listings to the Frappe seed endpoint."""
    payload = {"listings": json.dumps(rows)}
    try:
        r = requests.post(API_URL, data=payload, timeout=30)
        r.raise_for_status()
        result = r.json().get("message", {})
        return result.get("inserted", 0), result.get("skipped", 0)
    except requests.HTTPError as e:
        log(f"  HTTP error: {e} — {r.text[:200]}")
        return 0, len(rows)
    except Exception as e:
        log(f"  Error: {e}")
        return 0, len(rows)


def main():
    if not INPUT.exists():
        print(f"ERROR: {INPUT} not found. Run scrape_nocowboys.py first.")
        sys.exit(1)

    with INPUT.open() as f:
        rows = list(csv.DictReader(f))

    log(f"{'DRY RUN — ' if DRY_RUN else ''}Importing {len(rows)} listings in batches of {BATCH_SIZE}")

    total_inserted = 0
    total_skipped  = 0

    for i in range(0, len(rows), BATCH_SIZE):
        batch = rows[i:i + BATCH_SIZE]
        batch_clean = [
            {
                "name":          r["name"],
                "trade":         r["trade"],
                "region":        r["region"],
                "phone":         r.get("phone", ""),
                "nocowboys_url": r.get("nocowboys_url", ""),
                "avg_rating":    float(r.get("avg_rating") or 0),
                "review_count":  int(r.get("review_count") or 0),
            }
            for r in batch
        ]

        log(f"Batch {i // BATCH_SIZE + 1}: {len(batch_clean)} listings...")

        if DRY_RUN:
            for r in batch_clean:
                log(f"  [DRY] {r['name']} ({r['trade']}, {r['region']})")
            continue

        inserted, skipped = send_batch(batch_clean)
        total_inserted += inserted
        total_skipped  += skipped
        log(f"  → inserted: {inserted}, skipped (duplicate): {skipped}")
        time.sleep(0.5)

    if not DRY_RUN:
        log(f"\nDone. Total inserted: {total_inserted} | Skipped: {total_skipped}")
    else:
        log(f"\nDry run complete — {len(rows)} listings would be processed.")


if __name__ == "__main__":
    main()
