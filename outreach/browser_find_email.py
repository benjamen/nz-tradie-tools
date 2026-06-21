"""
TradieTools outreach — uses headless Chrome to find tradie emails and send cold outreach.
Pulls priority listings from TradieTools API, finds real website via Google search,
extracts contact email, sends personalised "claim your listing" email.
"""

import sys
sys.path.insert(0, '/home/ben/.openclaw/workspace/site/.venv/lib/python3.12/site-packages')

import re
import csv
import time
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from playwright.sync_api import sync_playwright

# ── Config ────────────────────────────────────────────────────────────────────
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
FROM_NAME  = "Ben @ TradieTools"

OUTPUT_CSV = Path(__file__).parent / "contacts_found.csv"
SENT_LOG   = Path(__file__).parent / "sent.log"
LOG_FILE   = Path(__file__).parent / "browser_find.log"

PRIORITY_TRADES = ["electricians", "plumbers", "builders", "carpenters", "drainlayers"]

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
SKIP = {"example.com","sentry.io","wix.com","google.com","facebook.com",
        "tradietools.nz","nocowboys","builderscrack","w3.org","schema.org",
        "instagram","linkedin","twitter","png","jpg"}

TRADE_LABEL = {
    "electricians":"electrician","plumbers":"plumber","builders":"builder",
    "carpenters":"carpenter","drainlayers":"drainlayer","painters":"painter",
}


def log(msg):
    print(msg, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")


# ── Pull listings from API ────────────────────────────────────────────────────

def get_listings():
    listings = []
    for trade in PRIORITY_TRADES:
        url = f"https://tradietools.optified.nz/api/method/tradietools.api.get_directory?limit=50&offset=0&trade={trade}"
        try:
            r = requests.get(url, timeout=10)
            for l in r.json().get("message", {}).get("listings", []):
                email = l.get("contact_email", "") or ""
                if "noemail.tradietools.nz" in email or not email:
                    listings.append({
                        "id": l["id"], "name": l["name"],
                        "trade": trade, "region": l.get("region",""),
                        "reviews": l.get("google_reviews") or 0,
                        "rating": l.get("google_rating"),
                    })
        except Exception as e:
            log(f"API error {trade}: {e}")
        time.sleep(0.3)
    listings.sort(key=lambda x: x["reviews"], reverse=True)
    log(f"Listings to process: {len(listings)}")
    return listings[:120]


# ── Email extraction ──────────────────────────────────────────────────────────

def extract_email_from_html(html, base_domain=""):
    emails = set()
    # mailto links are most reliable
    for m in re.findall(r'href=["\']mailto:([^"\'?]+)', html, re.I):
        e = m.strip().lower()
        if "@" in e and not any(s in e for s in SKIP):
            emails.add(e)
    # regex scan
    for m in EMAIL_RE.findall(html):
        e = m.lower()
        domain = e.split("@")[1] if "@" in e else ""
        if base_domain and domain != base_domain:
            continue
        if not any(s in e for s in SKIP):
            emails.add(e)
    return sorted(emails)


def find_email_on_site(page, website_url):
    domain = urlparse(website_url).netloc.replace("www.", "")
    for path in ["", "/contact", "/contact-us", "/about"]:
        url = website_url.rstrip("/") + path
        try:
            page.goto(url, timeout=12000, wait_until="domcontentloaded")
            html = page.content()
            emails = extract_email_from_html(html, domain)
            if emails:
                return emails[0]
        except Exception:
            pass
    return None


# ── Google search for business website ───────────────────────────────────────

def google_find_website(page, name, region):
    query = f'"{name}" {region} NZ electrician OR plumber OR builder site contact email'
    try:
        page.goto(f"https://www.google.com/search?q={requests.utils.quote(f'{name} {region} NZ contact')}&num=5",
                  timeout=15000, wait_until="domcontentloaded")
        time.sleep(random.uniform(1.5, 3))
        # Get all result links, skip google-internal
        links = page.eval_on_selector_all(
            "a[href]",
            "els => els.map(e => e.href)"
        )
        skip_domains = {"google.", "youtube.", "facebook.", "instagram.", "linkedin.",
                        "nocowboys.", "builderscrack.", "trademe.", "yellow.co.nz",
                        "finda.co.nz", "tradietools."}
        for href in links:
            if href.startswith("http") and not any(s in href for s in skip_domains):
                # Validate it's a real website (not a directory)
                parsed = urlparse(href)
                if parsed.netloc and "." in parsed.netloc:
                    return href
    except Exception as e:
        log(f"    Google search error: {e}")
    return None


# ── Send email ────────────────────────────────────────────────────────────────

HTML_TMPL = """\
<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#1a1a1a;max-width:560px;margin:0 auto;padding:24px;font-size:15px;line-height:1.65}}
a{{color:#e85d26}}.btn{{display:inline-block;background:#e85d26;color:#fff!important;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;margin:14px 0}}
.footer{{margin-top:32px;font-size:12px;color:#999;border-top:1px solid #eee;padding-top:14px}}
</style></head><body>
<p>Hi there,</p>
<p>I noticed <strong>{name}</strong> is already listed on <a href="https://tradietools.nz">TradieTools.nz</a> — a new NZ tradie directory connecting homeowners with local tradespeople.</p>
<p>Your listing is live right now but unclaimed, so homeowners in {region} searching for a {label} can't see your phone number or reach you directly.</p>
<p><strong>Claiming your free listing takes 5 minutes:</strong></p>
<ul>
<li>Add your contact details and phone number</li>
<li>Show up when homeowners in {region} search for a {label}</li>
<li>We notify you when someone posts a relevant job nearby</li>
</ul>
<a href="https://tradietools.nz/signup/" class="btn">Claim your free listing →</a>
<p>If you'd like more leads, our Verified plan ($29/mo) shows weekly profile views and lets you list across two trades. Pro ($59/mo) emails you the moment a homeowner posts a job in your area — before anyone else sees it.</p>
<p>No pressure on the paid plans — the free listing is genuinely free, no card required.</p>
<p>Happy to answer any questions, just reply.</p>
<p>Cheers,<br>Ben Walsh<br>TradieTools NZ</p>
<div class="footer">TradieTools · <a href="https://tradietools.nz">tradietools.nz</a> · contact@tradietools.nz<br>
Reply "unsubscribe" to be removed immediately.</div>
</body></html>"""


def send_email(to_email, name, trade, region):
    label = TRADE_LABEL.get(trade, trade.rstrip("s"))
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Your {label} business is listed on TradieTools — claim it free"
    msg["From"]    = f"{FROM_NAME} <{SMTP_USER}>"
    msg["To"]      = to_email
    msg.attach(MIMEText(HTML_TMPL.format(name=name, region=region, label=label), "html"))
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, to_email, msg.as_string())


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    LOG_FILE.write_text("=== TradieTools browser outreach ===\n")

    sent = set()
    if SENT_LOG.exists():
        sent = set(SENT_LOG.read_text().splitlines())

    listings = get_listings()
    results  = []
    emailed  = 0

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        ctx     = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="en-NZ",
        )
        page = ctx.new_page()

        for i, lst in enumerate(listings):
            name   = lst["name"]
            trade  = lst["trade"]
            region = lst["region"]
            log(f"\n[{i+1}/{len(listings)}] {name} ({trade}, {region})")

            if name in sent:
                log("  → already sent, skip")
                continue

            # Find website
            website = google_find_website(page, name, region)
            log(f"  website: {website or 'not found'}")

            if not website:
                results.append({**lst, "website": None, "email": None, "status": "no_website"})
                time.sleep(random.uniform(3, 5))
                continue

            # Find email
            email = find_email_on_site(page, website)
            log(f"  email:   {email or 'not found'}")

            results.append({**lst, "website": website, "email": email,
                            "status": "found" if email else "no_email"})

            if email:
                try:
                    send_email(email, name, trade, region)
                    log(f"  ✓ SENT → {email}")
                    with open(SENT_LOG, "a") as f:
                        f.write(name + "\n")
                    emailed += 1
                    time.sleep(random.uniform(5, 10))
                except Exception as e:
                    log(f"  ✗ send failed: {e}")
            else:
                time.sleep(random.uniform(2, 4))

        browser.close()

    # Save results
    with open(OUTPUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name","trade","region","website","email","status","reviews","rating"])
        w.writeheader()
        w.writerows(results)

    log(f"\n=== Complete ===")
    log(f"Processed:    {len(results)}")
    log(f"Emails found: {sum(1 for r in results if r.get('email'))}")
    log(f"Emails sent:  {emailed}")
    log(f"No website:   {sum(1 for r in results if r['status']=='no_website')}")
    log(f"Results CSV:  {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
