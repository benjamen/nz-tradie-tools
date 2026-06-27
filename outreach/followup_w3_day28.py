"""
Wave 3 Day 28 follow-up — final touch, social proof + soft close.
Send ~Jul 22 (28 days after Jun 24 wave 3 sends).
Run: venv/bin/python3 outreach/followup_w3_day28.py [--dry-run]
"""
import csv, smtplib, time, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, unsub_link, first_name
import unsubscribe
import daily_limit

CONTACTS_CSV = Path(__file__).parent / "contacts_wave3.csv"
FOLLOWUP_LOG = Path(__file__).parent / "followup_w3_day28.log"

DRY_RUN = "--dry-run" in __import__("sys").argv

CAMPAIGN = "followup_w3_day28"
TRACK_BASE = "https://tradietools.optified.nz/api/method/tradietools.api.track_email_open"

TRADE_LABEL = {
    "electricians": "electrician", "plumbers": "plumber",
    "builders": "builder", "carpenters": "carpenter",
    "drainlayers": "drainlayer", "roofers": "roofer",
    "painters": "painter", "concreters": "concreter",
    "tilers": "tiler", "glaziers": "glazier",
    "landscapers": "landscaper", "fencers": "fencer",
    "plasterers": "plasterer", "gasfitters": "gasfitter",
    "waterproofers": "waterproofer",
}


def make_email(name: str, email: str, trade: str, region: str, reviews: str, rating: str, listing_id: str = "", slug: str = "") -> tuple[str, str, str]:
    short_name = first_name(name, email)
    trade_label = TRADE_LABEL.get(trade, trade.rstrip("s"))
    lid = listing_id or ""
    unsub_url = unsub_link(email)
    claim_url = (
        f"https://tradietools.nz/signup/?ref=claim&id={lid}"
        f"&utm_source=email&utm_medium=email&utm_campaign={CAMPAIGN}"
        if lid else
        f"https://tradietools.nz/signup/?utm_source=email&utm_medium=email&utm_campaign={CAMPAIGN}"
    )
    track_url = f"{TRACK_BASE}?id={lid}&c={CAMPAIGN}" if lid else ""

    subject = f"Last one from me — {name}"

    text = f"""Hi {short_name},

I've reached out a couple of times about a free listing on TradieTools.nz — I'll keep this short.

A number of {trade_label}s across NZ have already claimed their listings and are getting homeowner enquiries through the platform. Yours is still unclaimed.

If you ever want to grab it:
👉 {claim_url}

Either way, good luck with the business.

Cheers,
Ben
TradieTools NZ
https://tradietools.nz

To unsubscribe: {unsub_url}
"""

    pixel = f'<img src="{track_url}" width="1" height="1" alt="" style="display:none">' if track_url else ""

    html = f"""<!DOCTYPE html>
<html>
<body style="font-family:Arial,sans-serif;max-width:560px;margin:0 auto;color:#1e293b;line-height:1.6">
  <div style="background:#0055a5;padding:1rem 1.25rem;border-radius:6px 6px 0 0">
    <span style="color:#fff;font-weight:700;font-size:1rem">TradieTools NZ</span>
  </div>
  <div style="border:1px solid #e2e8f0;border-top:none;padding:1.5rem 1.25rem;border-radius:0 0 6px 6px">
    <p>Hi {short_name},</p>
    <p>I've reached out a couple of times about a free listing on TradieTools.nz — I'll keep this short.</p>
    <p>A number of {trade_label}s across NZ have already claimed their listings and are getting homeowner enquiries through the platform. Yours is still unclaimed.</p>
    <p>Here's your live profile on TradieTools:</p>
    <p style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:.75rem 1rem;font-size:.88rem">
      🔗 <a href="https://tradietools.nz/businesses/{slug}/" style="color:#0055a5">{name} — view your profile</a>
    </p>
    <p style="margin:1.5rem 0">
      <a href="{claim_url}" style="display:inline-block;padding:.7rem 1.5rem;background:#0055a5;color:#fff;text-decoration:none;border-radius:5px;font-weight:700">
        Claim my free listing →
      </a>
    </p>
    <p style="color:#64748b;font-size:.9rem">Either way, good luck with the business.</p>
    <p>Cheers,<br><strong>Ben</strong><br>
    <a href="https://tradietools.nz" style="color:#0055a5">TradieTools NZ</a></p>
    <hr style="border:none;border-top:1px solid #e2e8f0;margin:1.25rem 0">
    <p style="font-size:.75rem;color:#94a3b8">
      Final email from us. <a href="{unsub_url}" style="color:#94a3b8;font-size:.8em">Unsubscribe</a>
    </p>
    {pixel}
  </div>
</body>
</html>"""

    return subject, text, html


def send_email(to_email: str, subject: str, text: str, html: str) -> bool:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = f"Ben from TradieTools <{SMTP_USER}>"
    msg["To"]      = to_email
    msg["Reply-To"] = SMTP_USER
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, [to_email], msg.as_string())
        return True
    except Exception as e:
        print(f"  SMTP error: {e}")
        return False


def main():
    with open(CONTACTS_CSV) as f:
        rows = [r for r in csv.DictReader(f) if r.get("status") == "sent"]

    already_logged = set(FOLLOWUP_LOG.read_text().splitlines()) if FOLLOWUP_LOG.exists() else set()

    print(f"{'DRY RUN — ' if DRY_RUN else ''}Sending Wave 3 Day 28 follow-ups to {len(rows)} contacts")

    sent_count = 0
    failed = []

    for row in rows:
        email  = row.get("email", "").strip()
        name   = row.get("name", "").strip()
        trade  = row.get("trade", "").strip()
        region = row.get("region", "").strip()
        reviews = row.get("reviews", "0").strip()
        rating  = row.get("rating", "0").strip()

        if not email or email in already_logged:
            continue
        if unsubscribe.is_unsubscribed(email):
            print(f"  -> {email} unsubscribed, skip")
            continue

        listing_id = row.get("listing_id", "").strip()
        subject, text, html = make_email(name, email, trade, region, reviews, rating, listing_id, row.get("listing_slug", ""))

        if DRY_RUN:
            print(f"  [DRY] {name} <{email}> — {subject}")
            sent_count += 1
            continue

        if not daily_limit.under_limit():
            print(f"  ⏸ daily limit ({daily_limit.LIMIT}) reached — stopping")
            break
        ok = send_email(email, subject, text, html)
        if ok:
            print(f"  ✓ {name} <{email}>")
            with open(FOLLOWUP_LOG, "a") as lf:
                lf.write(email + "\n")
            daily_limit.record_send()
            sent_count += 1
        else:
            print(f"  ✗ {name} <{email}>")
            failed.append(email)

        time.sleep(random.uniform(8, 18))

    print(f"\nDone: {sent_count} sent, {len(failed)} failed")
    if failed:
        print("Failed:", ", ".join(failed))


if __name__ == "__main__":
    main()
