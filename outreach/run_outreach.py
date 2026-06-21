"""
TradieTools full outreach pipeline:
1. Pull top unclaimed listings from API
2. Find website via Google Maps (Playwright)
3. Extract email from website
4. Send personalised cold email
"""

import sys
sys.path.insert(0, '/home/ben/.openclaw/workspace/site/.venv/lib/python3.12/site-packages')

import re, csv, time, random, smtplib, requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import daily_limit
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

SMTP_HOST = "smtp.hostinger.com"
SMTP_PORT = 465
SMTP_USER = "contact@tradietools.nz"
SMTP_PASS = "jtck-nlrn-kb6b-eail"

OUTPUT   = Path(__file__).parent / "contacts_found.csv"
SENT_LOG = Path(__file__).parent / "sent.log"
LOG_FILE = Path(__file__).parent / "run_outreach.log"

PRIORITY_TRADES = ["electricians", "plumbers", "builders", "carpenters", "drainlayers"]
TRADE_LABEL = {
    "electricians":"electrician","plumbers":"plumber","builders":"builder",
    "carpenters":"carpenter","drainlayers":"drainlayer",
}

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
SKIP = {"example.","sentry.","wix.","google.","facebook.","tradietools.",
        "nocowboys.","builderscrack.","w3.org","schema.","instagram.","linkedin.",
        ".png",".jpg",".gif","@2x","noreply","no-reply"}

MAPS_SKIP = {"google","facebook","instagram","linkedin","maps","goo.gl",
             "nocowboys","builderscrack","trademe","yellow.co","finda.co"}


def log(msg):
    print(msg, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")


def get_listings():
    out = []
    for trade in PRIORITY_TRADES:
        url = f"https://tradietools.optified.nz/api/method/tradietools.api.get_directory?limit=60&offset=0&trade={trade}"
        try:
            r = requests.get(url, timeout=10)
            for l in r.json().get("message", {}).get("listings", []):
                em = l.get("contact_email","") or ""
                if "noemail.tradietools.nz" in em or not em:
                    out.append({
                        "id": l.get("id",""),
                        "name": l["name"], "trade": trade,
                        "region": l.get("region",""),
                        "reviews": l.get("google_reviews") or 0,
                        "rating": l.get("google_rating") or "",
                    })
        except Exception as e:
            log(f"API error {trade}: {e}")
        time.sleep(0.3)
    out.sort(key=lambda x: x["reviews"], reverse=True)
    return out[:100]


def find_website_maps(page, name, region):
    q = f"{name} {region} New Zealand".replace(" ", "+")
    try:
        page.goto(f"https://www.google.com/maps/search/{q}", timeout=20000, wait_until="domcontentloaded")
        time.sleep(random.uniform(2.5, 4))
        html = page.content()
        # Primary: data-item-id="authority" links
        for pattern in [
            r'href="(https?://[^"]+)"[^>]*data-item-id="authority"',
            r'data-item-id="authority"[^>]*href="(https?://[^"]+)"',
            r'"(https?://(?!(?:maps|www\.google|goo\.gl|google\.))[^"]{8,80})"',
        ]:
            hits = re.findall(pattern, html)
            hits = [h for h in hits if not any(s in h for s in MAPS_SKIP)]
            if hits:
                return hits[0]
    except Exception as e:
        log(f"  Maps error: {e}")
    return None


def find_email(page, website_url):
    domain = urlparse(website_url).netloc.replace("www.", "")
    for path in ["", "/contact", "/contact-us", "/about", "/about-us"]:
        url = website_url.rstrip("/") + path
        try:
            page.goto(url, timeout=12000, wait_until="domcontentloaded")
            html = page.content()
            # mailto links first
            for m in re.findall(r'href=["\']mailto:([^"\'?\s]+)', html, re.I):
                e = m.strip().lower()
                if "@" in e and "." in e.split("@")[1] and not any(s in e for s in SKIP):
                    return e
            # regex scan restricted to same domain
            for m in EMAIL_RE.findall(html):
                e = m.lower()
                d = e.split("@")[1] if "@" in e else ""
                if d == domain and not any(s in e for s in SKIP):
                    return e
        except Exception:
            pass
        time.sleep(0.5)
    return None


HTML_BODY = """\
<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#1a1a1a;
max-width:560px;margin:0 auto;padding:24px;font-size:15px;line-height:1.65}}
a{{color:#e85d26}}
.btn{{display:inline-block;background:#e85d26;color:#fff!important;padding:11px 22px;
border-radius:6px;text-decoration:none;font-weight:600;margin:14px 0}}
.footer{{margin-top:32px;font-size:12px;color:#999;border-top:1px solid #eee;padding-top:14px}}
</style></head><body>
<p>Hi there,</p>
<p>I noticed <strong>{name}</strong> is already listed on
<a href="https://tradietools.nz">TradieTools.nz</a> — a new NZ tradie directory
connecting homeowners with local tradespeople in their area.</p>
<p>Your listing is live right now but unclaimed, so homeowners in {region}
searching for a {label} can't see your phone number or reach you directly through
the platform.</p>
<p><strong>Claiming your free listing takes 5 minutes:</strong></p>
<ul>
  <li>Add your contact details and phone number</li>
  <li>Show up when homeowners in {region} search for a {label}</li>
  <li>Get notified when someone posts a relevant job nearby</li>
</ul>
<a href="https://tradietools.nz/signup/?ref=claim&id={listing_id}" class="btn">Claim your free listing →</a>
<p>If you'd like more leads, our Verified plan ($29/mo) shows you weekly profile
views and lets you list across two trades. Pro ($59/mo) emails you the moment a
homeowner posts a job in your area — before anyone else sees it.</p>
<p>No pressure on the paid plans — the free listing is genuinely free, no card needed.</p>
<p>Happy to answer any questions, just reply to this email.</p>
<p>Cheers,<br><strong>Ben Walsh</strong><br>
TradieTools NZ · <a href="https://tradietools.nz">tradietools.nz</a></p>
<div class="footer">
TradieTools · tradietools.nz · contact@tradietools.nz<br>
Reply "unsubscribe" to be removed immediately.
</div></body></html>"""


def send(to_email, name, trade, region, listing_id=""):
    label = TRADE_LABEL.get(trade, trade.rstrip("s"))
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Your {label} business is listed on TradieTools — claim it free"
    msg["From"]    = "Ben @ TradieTools <contact@tradietools.nz>"
    msg["To"]      = to_email
    msg.attach(MIMEText(HTML_BODY.format(name=name, region=region, label=label, listing_id=listing_id), "html"))
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, to_email, msg.as_string())


def main():
    LOG_FILE.write_text("=== TradieTools outreach run ===\n")
    sent = set(SENT_LOG.read_text().splitlines()) if SENT_LOG.exists() else set()

    listings = get_listings()
    log(f"Targeting {len(listings)} listings\n")

    results = []
    emailed = 0

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="en-NZ", timezone_id="Pacific/Auckland",
        )
        page = ctx.new_page()

        for i, lst in enumerate(listings):
            name, trade, region = lst["name"], lst["trade"], lst["region"]
            log(f"[{i+1}/{len(listings)}] {name} ({trade}, {region})")

            if name in sent:
                log("  → already sent, skip")
                continue

            website = find_website_maps(page, name, region)
            log(f"  website: {website or 'not found'}")

            if not website:
                results.append({**lst, "website": None, "email": None, "status": "no_website"})
                time.sleep(random.uniform(2, 4))
                continue

            email = find_email(page, website)
            log(f"  email:   {email or 'not found'}")
            results.append({**lst, "website": website, "email": email,
                            "status": "sent" if email else "no_email"})

            if email:
                if not daily_limit.under_limit():
                    log(f"  ⏸ daily limit ({daily_limit.LIMIT}) reached — stopping")
                    results[-1]["status"] = "deferred"
                    break
                try:
                    send(email, name, trade, region, lst.get("id",""))
                    log(f"  ✓ SENT → {email}")
                    with open(SENT_LOG, "a") as f:
                        f.write(name + "\n")
                    daily_limit.record_send()
                    emailed += 1
                    time.sleep(random.uniform(6, 12))
                except Exception as e:
                    log(f"  ✗ send failed: {e}")
                    results[-1]["status"] = "send_failed"
            else:
                time.sleep(random.uniform(2, 5))

        browser.close()

    with open(OUTPUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["listing_id","name","trade","region","website","email","status","reviews","rating"])
        w.writeheader()
        w.writerows(results)

    log(f"\n{'='*40}")
    log(f"Processed:    {len(results)}")
    log(f"Websites found: {sum(1 for r in results if r.get('website'))}")
    log(f"Emails found: {sum(1 for r in results if r.get('email'))}")
    log(f"Emails sent:  {emailed}")
    log(f"CSV: {OUTPUT}")

    # Email summary to owner
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"TradieTools outreach complete — {emailed} emails sent"
        msg["From"]    = "TradieTools <contact@tradietools.nz>"
        msg["To"]      = "instituteofbba@gmail.com"
        found_emails = [r for r in results if r.get("email")]
        rows = "".join(f"<tr><td>{r['name']}</td><td>{r['trade']}</td><td>{r['region']}</td><td>{r['email']}</td></tr>" for r in found_emails)
        summary_html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>body{{font-family:sans-serif;max-width:640px;margin:0 auto;padding:24px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{background:#f5f5f5;padding:7px 10px;text-align:left}}
td{{padding:6px 10px;border-bottom:1px solid #eee}}</style></head><body>
<h2 style="color:#e85d26">Outreach Complete</h2>
<p><strong>{emailed} cold emails sent</strong> to unclaimed TradieTools listings.</p>
<p>Processed {len(results)} businesses &bull; Found {sum(1 for r in results if r.get('website'))} websites &bull; Found {sum(1 for r in results if r.get('email'))} emails</p>
<h3>Emails sent to:</h3>
<table><tr><th>Business</th><th>Trade</th><th>Region</th><th>Email</th></tr>{rows}</table>
</body></html>"""
        msg.attach(MIMEText(summary_html, "html"))
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, "instituteofbba@gmail.com", msg.as_string())
        log("Summary email sent to instituteofbba@gmail.com")
    except Exception as e:
        log(f"Summary email failed: {e}")


if __name__ == "__main__":
    main()
