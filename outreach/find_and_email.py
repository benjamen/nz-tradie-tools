"""
TradieTools outreach — find emails for seeded listings and send cold email.
Uses DuckDuckGo HTML search (no API key needed) to find business websites,
extracts contact emails, then sends personalised outreach.

Run: python3 find_and_email.py
"""

import requests
import re
import csv
import time
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin, urlparse, quote_plus

# ── Config ───────────────────────────────────────────────────────────────────
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
FROM_NAME = "Ben @ TradieTools"

OUTPUT_CSV = Path(__file__).parent / "contacts_found.csv"
SENT_LOG   = Path(__file__).parent / "sent.log"
LOG_FILE   = Path(__file__).parent / "find_email.log"

# Priority trades to target
PRIORITY_TRADES = {"electricians", "plumbers", "builders", "carpenters", "drainlayers", "gasfitters"}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-NZ,en;q=0.9",
}

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
SKIP_EMAIL_DOMAINS = {
    "example.com", "sentry.io", "wix.com", "google.com", "facebook.com",
    "tradietools.nz", "nocowboys.co.nz", "builderscrack.co.nz",
    "w3.org", "schema.org", "png", "jpg", "jpeg",
}

TRADE_LABELS = {
    "electricians": "electrician",
    "plumbers": "plumber",
    "builders": "builder",
    "carpenters": "carpenter",
    "drainlayers": "drainlayer",
    "gasfitters": "gasfitter",
    "painters": "painter",
    "tilers": "tiler",
}


def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")


def get_url(url, timeout=10, verify=False):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout,
                         verify=verify, allow_redirects=True)
        if r.status_code == 200:
            return r
    except Exception as e:
        log(f"    GET failed {url}: {e}")
    return None


# ── Step 1: Pull priority listings from TradieTools API ──────────────────────

def get_priority_listings(limit=200):
    listings = []
    for trade in PRIORITY_TRADES:
        url = f"https://tradietools.optified.nz/api/method/tradietools.api.get_directory?limit=50&offset=0&trade={trade}"
        r = get_url(url)
        if not r:
            continue
        try:
            data = r.json().get("message", {}).get("listings", [])
            for l in data:
                # Only unclaimed (no real email)
                email = l.get("contact_email", "") or ""
                if "noemail.tradietools.nz" in email or not email:
                    listings.append({
                        "id": l.get("id"),
                        "name": l.get("name", ""),
                        "trade": trade,
                        "region": l.get("region", ""),
                        "google_rating": l.get("google_rating"),
                        "google_reviews": l.get("google_reviews", 0),
                    })
        except Exception as e:
            log(f"  Parse error for {trade}: {e}")
        time.sleep(0.5)

    # Sort: highest-rated first (most credible businesses)
    listings.sort(key=lambda x: (x.get("google_reviews") or 0), reverse=True)
    log(f"Priority listings found: {len(listings)}")
    return listings[:limit]


# ── Step 2: DuckDuckGo search to find business website ───────────────────────

def ddg_find_website(business_name, region):
    query = f'"{business_name}" {region} NZ contact'
    url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
    r = get_url(url, timeout=12)
    if not r:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    for result in soup.select("div.result__body, div.result, .web-result"):
        link_el = result.select_one("a.result__url, a[href*='http']")
        if not link_el:
            continue
        href = link_el.get("href", "")
        # Skip directories/social
        skip = {"duckduckgo", "facebook", "nocowboys", "builderscrack",
                 "yellow.co.nz", "finda.co.nz", "trademe", "linkedin",
                 "instagram", "tradietools"}
        if any(s in href for s in skip):
            continue
        if href.startswith("http"):
            return href
    return None


# ── Step 3: Extract email from website ───────────────────────────────────────

def extract_email(website_url):
    if not website_url:
        return None
    base_domain = urlparse(website_url).netloc.replace("www.", "")
    for path in ["", "/contact", "/contact-us", "/about"]:
        url = website_url.rstrip("/") + path if path else website_url
        r = get_url(url, timeout=8)
        if not r:
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        # mailto links first (most reliable)
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.lower().startswith("mailto:"):
                email = href[7:].split("?")[0].strip().lower()
                if email and "@" in email and not any(s in email for s in SKIP_EMAIL_DOMAINS):
                    return email
        # Regex scan
        for match in EMAIL_RE.findall(r.text):
            m = match.lower()
            domain = m.split("@")[1]
            if domain == base_domain and not any(s in m for s in SKIP_EMAIL_DOMAINS):
                return m
        time.sleep(random.uniform(0.5, 1.5))
    return None


# ── Step 4: Send cold email ───────────────────────────────────────────────────

EMAIL_SUBJECT = "Your {trade} business is listed on TradieTools — claim it free"

EMAIL_BODY_HTML = """\
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #1a1a1a; max-width: 560px; margin: 0 auto; padding: 24px; font-size: 15px; line-height: 1.6; }}
  a {{ color: #e85d26; }}
  .btn {{ display: inline-block; background: #e85d26; color: white !important; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: 600; margin: 16px 0; }}
  .footer {{ margin-top: 32px; font-size: 12px; color: #999; border-top: 1px solid #eee; padding-top: 16px; }}
</style>
</head>
<body>
<p>Hi there,</p>

<p>I noticed <strong>{name}</strong> is already listed on <a href="https://tradietools.nz">TradieTools.nz</a> — New Zealand's newest tradie directory.</p>

<p>Your listing is live right now, but it's unclaimed, so homeowners in {region} can't see your phone number or contact you directly through the platform.</p>

<p>Claiming it is completely free and takes about 5 minutes:</p>
<ul>
  <li>Add your phone number and contact details</li>
  <li>Upload a photo and a short description</li>
  <li>Start showing up when homeowners search for a {trade_label} in {region}</li>
</ul>

<a href="https://tradietools.nz/signup/" class="btn">Claim your free listing →</a>

<p>If you want more leads, our Verified plan ($29/mo) shows you how many homeowners viewed your profile each week and lets you list across two trades. Pro ($59/mo) emails you directly when a homeowner posts a job near you.</p>

<p>No pressure though — the free listing is genuinely free, no card required.</p>

<p>Happy to answer any questions — just reply to this email.</p>

<p>Cheers,<br>
Ben Walsh<br>
TradieTools NZ</p>

<div class="footer">
TradieTools · <a href="https://tradietools.nz">tradietools.nz</a> · contact@tradietools.nz<br>
To unsubscribe, reply with "unsubscribe" and we'll remove you immediately.
</div>
</body>
</html>
"""


def send_email(to_email, business_name, trade, region):
    trade_label = TRADE_LABELS.get(trade, trade.rstrip("s"))
    subject = EMAIL_SUBJECT.format(trade=trade_label)
    html = EMAIL_BODY_HTML.format(
        name=business_name,
        trade=trade,
        trade_label=trade_label,
        region=region,
    )
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = f"{FROM_NAME} <{SMTP_USER}>"
    msg["To"]      = to_email
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as srv:
        srv.login(SMTP_USER, SMTP_PASS)
        srv.sendmail(SMTP_USER, to_email, msg.as_string())


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    LOG_FILE.write_text("")
    log("=== TradieTools outreach: find + email ===\n")

    # Load already-sent to avoid duplicates
    sent = set()
    if SENT_LOG.exists():
        sent = set(SENT_LOG.read_text().splitlines())

    listings = get_priority_listings(limit=150)
    results  = []
    emailed  = 0

    for i, listing in enumerate(listings):
        name   = listing["name"]
        trade  = listing["trade"]
        region = listing["region"]

        log(f"\n[{i+1}/{len(listings)}] {name} ({trade}, {region})")

        # Skip already contacted
        if name in sent:
            log("  → already contacted, skip")
            continue

        # Find website via DuckDuckGo
        website = ddg_find_website(name, region)
        log(f"  website: {website or 'not found'}")
        time.sleep(random.uniform(2, 4))   # polite DDG rate limit

        if not website:
            results.append({**listing, "website": None, "email": None, "status": "no_website"})
            continue

        # Extract email
        email = extract_email(website)
        log(f"  email:   {email or 'not found'}")
        time.sleep(random.uniform(1, 2))

        results.append({**listing, "website": website, "email": email,
                        "status": "found" if email else "no_email"})

        if email:
            try:
                send_email(email, name, trade, region)
                log(f"  ✓ SENT to {email}")
                with open(SENT_LOG, "a") as f:
                    f.write(name + "\n")
                emailed += 1
                time.sleep(random.uniform(3, 6))   # don't spam
            except Exception as e:
                log(f"  ✗ send failed: {e}")

    # Save CSV
    with open(OUTPUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name","trade","region","website","email","status","google_rating","google_reviews"])
        w.writeheader()
        w.writerows(results)

    log(f"\n=== Done ===")
    log(f"Processed:    {len(results)}")
    log(f"Emails found: {sum(1 for r in results if r.get('email'))}")
    log(f"Emails sent:  {emailed}")
    log(f"CSV saved:    {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
