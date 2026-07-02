#!/usr/bin/env python3
"""
One-off script: email all active tradies their personal dashboard link.

Framed as a helpful product update — not an alarm. Copy reads:
"We've added a login page so you can always get back in. Here's your link."

Usage:
  python3 scripts/send_dashboard_links.py            # live send
  python3 scripts/send_dashboard_links.py --dry-run  # preview only, no emails sent

Requires SSH access to the Frappe server. Runs the send via the tradie_login
API endpoint so email delivery goes through the same path as normal logins.
"""

import argparse
import json
import sys
import time
import urllib.request
import urllib.parse

API_BASE = "https://tradietools.optified.nz/api/method/tradietools.api."

def call_api(endpoint, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        API_BASE + endpoint,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Frappe-CSRF-Token": "fetch",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def main():
    parser = argparse.ArgumentParser(description="Broadcast dashboard links to all active tradies")
    parser.add_argument("--dry-run", action="store_true", help="Print emails that would be sent, don't send")
    parser.add_argument("--delay", type=float, default=0.5, help="Seconds between sends (default 0.5)")
    args = parser.parse_args()

    print("Fetching tradie list...")
    result = call_api("get_active_tradies_for_broadcast", {})
    tradies = result.get("message", {}).get("tradies", [])

    if not tradies:
        print("No tradies returned. Check that get_active_tradies_for_broadcast endpoint exists.")
        sys.exit(1)

    print(f"Found {len(tradies)} tradies with real emails and active tokens.\n")

    sent = 0
    failed = 0
    skipped = 0

    for t in tradies:
        email = t.get("contact_email", "").strip()
        name = t.get("name", "Unknown")

        if not email or "noemail" in email:
            skipped += 1
            continue

        if args.dry_run:
            print(f"  [DRY RUN] Would send to: {email} ({name})")
            sent += 1
            continue

        try:
            call_api("tradie_login", {"email": email})
            print(f"  ✓ Sent to {email} ({name})")
            sent += 1
            time.sleep(args.delay)
        except Exception as e:
            print(f"  ✗ Failed for {email} ({name}): {e}")
            failed += 1

    print(f"\nDone. Sent: {sent}  Failed: {failed}  Skipped: {skipped}")
    if args.dry_run:
        print("(Dry run — no emails were actually sent)")


if __name__ == "__main__":
    main()
