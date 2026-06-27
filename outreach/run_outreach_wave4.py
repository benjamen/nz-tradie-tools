"""
TradieTools Wave 4 outreach — electricians, plumbers, builders, roofers, painters.
Targets listings ranked 80-250 (skips top tier already contacted in Waves 1-2).
Run: cd outreach && python3 run_outreach_wave4.py
"""

import sys
sys.path.insert(0, '/home/ben/.openclaw/workspace/site/.venv/lib/python3.12/site-packages')

import re, csv, time, random, smtplib, requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
import daily_limit
import unsubscribe

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, unsub_link, first_name

OUTPUT   = Path(__file__).parent / "contacts_wave4.csv"
SENT_LOG = Path(__file__).parent / "sent_wave4.log"
LOG_FILE = Path(__file__).parent / "run_outreach_wave4.log"

PRIORITY_TRADES = ["electricians", "plumbers", "builders", "roofers", "painters"]
TRADE_LABEL = {
    "electricians": "electrician",
    "plumbers":     "plumber",
    "builders":     "builder",
    "roofers":      "roofer",
    "painters":     "painter",
}

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
SKIP = {"example.", "sentry.", "wix.", "google.", "facebook.", "tradietools.",
        "nocowboys.", "builderscrack.", "w3.org", "schema.", "instagram.", "linkedin.",
        ".png", ".jpg", ".gif", "@2x", "noreply", "no-reply"}
MAPS_SKIP = {"google", "facebook", "instagram", "linkedin", "maps", "goo.gl",
             "nocowboys", "builderscrack", "trademe", "yellow.co", "finda.co"}

HTML_BODY = """\
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
body{{font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#334155;font-size:15px;line-height:1.6}}
.btn{{display:inline-block;background:#ea6325;color:#fff!important;padding:12px 24px;
border-radius:6px;text-decoration:none;font-weight:700;margin:16px 0;font-size:15px}}
.profile-box{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:12px 16px;margin:14px 0;font-size:13px;color:#475569}}
.footer{{margin-top:32px;font-size:12px;color:#999;border-top:1px solid #eee;padding-top:14px}}
</style></head><body>
<p>Hi {fname},</p>
<p>I noticed <strong>{name}</strong> is already listed on
<a href="https://tradietools.nz">TradieTools.nz</a> — a NZ tradie directory
connecting homeowners with local tradespeople.</p>
<p>Your listing is live but unclaimed, so homeowners in {region}
searching for a {label} can't see your contact details or reach you through the platform.</p>
<p>You can view it here:</p>
<div class="profile-box">🔗 <a href="https://tradietools.nz/businesses/{slug}/">{name} — your live profile</a></div>
<p><strong>Claiming your free listing takes about 60 seconds:</strong></p>
<ul>
  <li>Add your contact details so homeowners can reach you</li>
  <li>Show up when locals in {region} search for a {label}</li>
  <li>Get notified when someone nearby posts a job</li>
</ul>
<a href="https://tradietools.nz/signup/?ref=claim&id={listing_id}" class="btn">Claim your free listing →</a>
<p>There's also a Verified plan ($29/mo) with priority placement and direct lead alerts,
but the free listing is genuinely free — no card needed.</p>
<p>Happy to answer questions — just reply.</p>
<p>Cheers,<br><strong>Ben Walsh</strong><br>
TradieTools NZ · <a href="https://tradietools.nz">tradietools.nz</a></p>
<div class="footer">
TradieTools NZ · tradietools.nz · contact@tradietools.nz<br>
<a href="{unsub_url}" style="color:#94a3b8;font-size:.8em">Unsubscribe</a>
</div></body></html>"""

TEXT_BODY = """\
Hi {fname},

I noticed {name} is already listed on TradieTools.nz — a NZ tradie directory connecting homeowners with local tradespeople.

Your listing is live but unclaimed. View it here:
https://tradietools.nz/businesses/{slug}/

Claiming takes about 60 seconds. It's free — no card needed.
https://tradietools.nz/signup/?ref=claim&id={listing_id}

Cheers,
Ben Walsh
TradieTools NZ · tradietools.nz

To unsubscribe: {unsub_url}
"""


def log(msg):
    print(msg, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")


def get_listings():
    """Fetch listings from offset 80 onward — skip top tier already contacted."""
    out = []
    for trade in PRIORITY_TRADES:
        for offset in [80, 160]:
            url = (f"https://tradietools.optified.nz/api/method/tradietools.api.get_directory"
                   f"?limit=80&offset={offset}&trade={trade}")
            try:
                r = requests.get(url, timeout=10)
                for l in r.json().get("message", {}).get("listings", []):
                    em = l.get("contact_email", "") or ""
                    if "noemail.tradietools.nz" in em or not em:
                        out.append({
                            "id":      l.get("id", ""),
                            "name":    l["name"],
                            "trade":   trade,
                            "region":  l.get("region", ""),
                            "reviews": l.get("review_count") or 0,
                            "rating":  l.get("avg_rating") or "",
                        })
            except Exception as e:
                log(f"API error {trade} offset={offset}: {e}")
            time.sleep(0.3)
    # Deduplicate by name
    seen = set()
    unique = []
    for l in out:
        if l["name"] not in seen:
            seen.add(l["name"])
            unique.append(l)
    return unique[:200]


def find_website_maps(page, name, region):
    q = f"{name} {region} New Zealand".replace(" ", "+")
    try:
        page.goto(f"https://www.google.com/maps/search/{q}",
                  timeout=20000, wait_until="domcontentloaded")
        time.sleep(random.uniform(2.5, 4))
        html = page.content()
        for pattern in [
            r'href="(https?://[^"]+)"[^>]*data-item-id="authority"',
            r'data-item-id="authority"[^>]*href="(https?://[^"]+)"',
            r'"(https?://(?!(?:maps|www\.google|goo\.gl|google\.))[^"]{8,80})"',
        ]:
            hits = re.findall(pattern, html)
            hits = [h for h in hits if not any(s in h for s in MAPS_SKIP)]
            if hits:
                return hits[0]
    except Exception:
        pass
    return None


def find_email(page, url):
    try:
        page.goto(url, timeout=15000, wait_until="domcontentloaded")
        time.sleep(random.uniform(1.5, 3))
        text = page.content()
        emails = EMAIL_RE.findall(text)
        emails = [e for e in emails if not any(s in e for s in SKIP)]
        if emails:
            return emails[0]
        for path in ["/contact", "/contact-us", "/about"]:
            try:
                parsed = urlparse(url)
                contact_url = f"{parsed.scheme}://{parsed.netloc}{path}"
                page.goto(contact_url, timeout=12000, wait_until="domcontentloaded")
                time.sleep(random.uniform(1, 2))
                emails = EMAIL_RE.findall(page.content())
                emails = [e for e in emails if not any(s in e for s in SKIP)]
                if emails:
                    return emails[0]
            except Exception:
                pass
    except Exception:
        pass
    return None


def get_slug(name):
    import re as _re
    return _re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def send(to_email, name, trade, region, listing_id=""):
    label = TRADE_LABEL.get(trade, trade.replace("-", " ").rstrip("s"))
    slug  = get_slug(name)
    fname = first_name(name, to_email)
    unsub_url = unsub_link(to_email)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Your {label} business is listed on TradieTools — claim it free"
    msg["From"]    = "Ben @ TradieTools <contact@tradietools.nz>"
    msg["To"]      = to_email
    msg.attach(MIMEText(
        TEXT_BODY.format(fname=fname, name=name, region=region, label=label,
                         listing_id=listing_id, slug=slug, unsub_url=unsub_url),
        "plain"
    ))
    msg.attach(MIMEText(
        HTML_BODY.format(fname=fname, name=name, region=region, label=label,
                         listing_id=listing_id, slug=slug, unsub_url=unsub_url),
        "html"
    ))
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, to_email, msg.as_string())


def main():
    LOG_FILE.write_text("=== TradieTools Wave 4 outreach ===\n")
    sent = set(SENT_LOG.read_text().splitlines()) if SENT_LOG.exists() else set()
    # Also load all previous wave sent logs to avoid duplicates
    for prev_log in ["sent.log", "sent_wave2.log", "sent_wave3.log"]:
        p = Path(__file__).parent / prev_log
        if p.exists():
            sent.update(p.read_text().splitlines())

    listings = get_listings()
    log(f"Targeting {len(listings)} listings (core trades, offset 80-240)\n")

    results = []
    emailed = 0

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="en-NZ",
            timezone_id="Pacific/Auckland",
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
                if unsubscribe.is_unsubscribed(email):
                    log("  → unsubscribed, skip")
                    results[-1]["status"] = "unsubscribed"
                    continue
                if not daily_limit.under_limit():
                    log(f"  ⏸ daily limit ({daily_limit.LIMIT}) reached — stopping")
                    results[-1]["status"] = "deferred"
                    break
                try:
                    send(email, name, trade, region, str(lst.get("id", "")))
                    log(f"  ✓ SENT → {email}")
                    with open(SENT_LOG, "a") as f:
                        f.write(name + "\n")
                    daily_limit.record_send()
                    emailed += 1
                    time.sleep(random.uniform(8, 15))
                except Exception as e:
                    log(f"  ✗ send failed: {e}")
                    results[-1]["status"] = "send_failed"
            else:
                time.sleep(random.uniform(2, 5))

        browser.close()

    with open(OUTPUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "listing_id", "name", "trade", "region", "website", "email", "status", "reviews", "rating"
        ])
        w.writeheader()
        for r in results:
            w.writerow({
                "listing_id": r.get("id", ""),
                "name":       r.get("name", ""),
                "trade":      r.get("trade", ""),
                "region":     r.get("region", ""),
                "website":    r.get("website", ""),
                "email":      r.get("email", ""),
                "status":     r.get("status", ""),
                "reviews":    r.get("reviews", ""),
                "rating":     r.get("rating", ""),
            })

    log(f"\n{'='*40}")
    log(f"Processed:      {len(results)}")
    log(f"Websites found: {sum(1 for r in results if r.get('website'))}")
    log(f"Emails found:   {sum(1 for r in results if r.get('email'))}")
    log(f"Emails sent:    {emailed}")
    log(f"CSV saved:      {OUTPUT}")

    # Summary email to Ben
    try:
        found_emails = [r for r in results if r.get("email")]
        rows = "".join(
            f"<tr><td>{r['name']}</td><td>{r['trade']}</td><td>{r['region']}</td><td>{r['email']}</td><td>{r['status']}</td></tr>"
            for r in found_emails
        )
        summary = MIMEMultipart("alternative")
        summary["Subject"] = f"TradieTools Wave 4 complete — {emailed} emails sent"
        summary["From"]    = "TradieTools <contact@tradietools.nz>"
        summary["To"]      = "instituteofbba@gmail.com"
        html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>body{{font-family:sans-serif;max-width:640px;margin:0 auto;padding:24px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{background:#f5f5f5;padding:7px 10px;text-align:left}}
td{{padding:6px 10px;border-bottom:1px solid #eee}}</style></head><body>
<h2 style="color:#ea6325">Wave 4 Outreach Complete</h2>
<p><strong>{emailed} cold emails sent</strong> — electricians, plumbers, builders, roofers, painters (tier 2 listings).</p>
<p>Processed {len(results)} &bull; Websites {sum(1 for r in results if r.get('website'))}
&bull; Emails found {sum(1 for r in results if r.get('email'))}</p>
<h3>Sent to:</h3>
<table><tr><th>Business</th><th>Trade</th><th>Region</th><th>Email</th><th>Status</th></tr>{rows}</table>
</body></html>"""
        summary.attach(MIMEText(html, "html"))
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, "instituteofbba@gmail.com", summary.as_string())
        log("Summary email sent to Ben")
    except Exception as e:
        log(f"Summary email failed: {e}")


if __name__ == "__main__":
    main()
