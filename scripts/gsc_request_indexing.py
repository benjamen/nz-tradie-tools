#!/usr/bin/env python3
"""
Request Google indexing for new tradietools.nz pages via GSC URL Inspection API.
Run after granting claude@fastcrew.iam.gserviceaccount.com Owner access in GSC.

GSC → Settings → Users and permissions → Add user → Owner
"""

import json
import time
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_FILE = Path.home() / "Optified-AI/service-account.json"
SITE_URL = "sc-domain:tradietools.nz"

URLS_TO_INDEX = [
    # DIY hub pages
    "https://tradietools.nz/diy/",
    "https://tradietools.nz/diy/electrical-work-i-can-do-myself-nz/",
    "https://tradietools.nz/diy/plumbing-i-can-do-myself-nz/",
    "https://tradietools.nz/diy/building-work-without-consent-nz/",
    "https://tradietools.nz/diy/can-i-be-my-own-builder-nz/",
    # Planning hub pages
    "https://tradietools.nz/planning/",
    "https://tradietools.nz/planning/order-of-trades-nz/",
    "https://tradietools.nz/planning/bathroom-renovation-planning-nz/",
    "https://tradietools.nz/planning/kitchen-renovation-planning-nz/",
    "https://tradietools.nz/planning/house-extension-planning-nz/",
    # New homeowner blog articles
    "https://tradietools.nz/articles/should-i-diy-or-hire-a-tradie-nz.html",
    "https://tradietools.nz/articles/signs-your-house-needs-rewiring-nz.html",
    "https://tradietools.nz/articles/what-to-do-burst-pipe-nz.html",
    "https://tradietools.nz/articles/how-to-get-tradie-quotes-nz.html",
    "https://tradietools.nz/articles/bathroom-renovation-mistakes-nz.html",
    "https://tradietools.nz/articles/kitchen-renovation-mistakes-nz.html",
    "https://tradietools.nz/articles/renovation-vs-new-build-nz.html",
    "https://tradietools.nz/articles/how-to-spot-a-dodgy-tradie-nz.html",
    "https://tradietools.nz/articles/home-renovation-checklist-nz.html",
]


def main():
    creds = service_account.Credentials.from_service_account_file(
        str(CREDENTIALS_FILE),
        scopes=["https://www.googleapis.com/auth/webmasters"],
    )
    service = build("searchconsole", "v1", credentials=creds)

    print(f"Requesting indexing for {len(URLS_TO_INDEX)} URLs...\n")
    ok, errors = 0, 0

    for url in URLS_TO_INDEX:
        try:
            result = service.urlInspection().index().inspect(
                body={
                    "inspectionUrl": url,
                    "siteUrl": SITE_URL,
                }
            ).execute()
            status = result.get("urlInspectionResult", {}).get("indexStatusResult", {}).get("coverageState", "unknown")
            print(f"  ✓ {url.split('tradietools.nz')[1]:50s} → {status}")
            ok += 1
        except Exception as e:
            print(f"  ✗ {url.split('tradietools.nz')[1]:50s} → ERROR: {e}")
            errors += 1
        time.sleep(1)  # GSC URL Inspection API rate limit: 2000/day, ~1/sec safe

    print(f"\nDone: {ok} OK, {errors} errors")

    # Also submit sitemap
    print("\nSubmitting sitemap...")
    try:
        sitemaps = service.sitemaps()
        sitemaps.submit(siteUrl=SITE_URL, feedpath="https://tradietools.nz/sitemap.xml").execute()
        print("  ✓ Sitemap submitted")
    except Exception as e:
        print(f"  ✗ Sitemap error: {e}")


if __name__ == "__main__":
    main()
