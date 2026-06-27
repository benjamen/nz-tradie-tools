"""
Day 4 follow-up to the 77 initial outreach contacts.
Sent ~Jun 24 (4 days after the Jun 20 initial wave).
Run: .venv/bin/python3 outreach/followup_day4.py [--dry-run]
"""
import sys
sys.path.insert(0, '/home/ben/.openclaw/workspace/site/.venv/lib/python3.12/site-packages')

import csv, smtplib, time, random, sys
import daily_limit
import unsubscribe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, unsub_link
CONTACTS_CSV  = Path(__file__).parent / "contacts_found.csv"
FOLLOWUP_LOG  = Path(__file__).parent / "followup_day4.log"

DRY_RUN = "--dry-run" in sys.argv

TRADE_LABEL = {
    "electricians": "electrician", "plumbers": "plumber",
    "builders": "builder", "carpenters": "carpenter",
    "drainlayers": "drainlayer",
}


def make_email(name: str, email: str, trade: str, region: str, reviews: str, rating: str, listing_id: str = "", slug: str = "") -> tuple[str, str, str]:
    short_name = name.split(" ")[0] if name else "there"
    trade_label = TRADE_LABEL.get(trade, trade.rstrip("s"))
    unsub_url = unsub_link(email)
    claim_url = f"https://tradietools.nz/signup/?ref=claim&id={listing_id}" if listing_id else "https://tradietools.nz/signup/"
    review_line = ""
    if reviews and reviews != "0":
        review_line = f"\nI noticed you have {reviews} Google reviews at {rating} stars — that's great social proof we showcase on your listing.\n"

    subject = f"Quick follow-up — your free {trade_label} listing on TradieTools"

    text = f"""Hi {short_name},

I reached out a few days ago about a free listing on TradieTools.nz — just wanted to make sure this didn't get buried.
{review_line}
We list verified NZ tradies so homeowners can find and contact local pros directly. No fees, no commissions — free to list and free for homeowners.

It takes about 60 seconds to claim your spot:
👉 {claim_url}

You can also view your live profile:
https://tradietools.nz/businesses/{slug}/

If you're not taking on new work right now, no worries — happy to hear from you when things slow down.

Cheers,
Ben
TradieTools NZ
https://tradietools.nz

To unsubscribe: {unsub_url}
"""

    html = f"""<!DOCTYPE html>
<html>
<body style="font-family:Arial,sans-serif;max-width:560px;margin:0 auto;color:#1e293b;line-height:1.6">
  <div style="background:#0055a5;padding:1rem 1.25rem;border-radius:6px 6px 0 0">
    <span style="color:#fff;font-weight:700;font-size:1rem">TradieTools NZ</span>
  </div>
  <div style="border:1px solid #e2e8f0;border-top:none;padding:1.5rem 1.25rem;border-radius:0 0 6px 6px">
    <p>Hi {short_name},</p>
    <p>I reached out a few days ago about a free listing on TradieTools.nz — just wanted to make sure this didn't get buried.</p>
    {"<p>" + review_line.strip() + "</p>" if review_line else ""}
    <p>We list verified NZ tradies so homeowners can find and contact local pros directly. No fees, no commissions — free to list and free for homeowners.</p>
    <p style="margin:1.5rem 0">
      <a href="{claim_url}" style="display:inline-block;padding:.7rem 1.5rem;background:#ea6325;color:#fff;text-decoration:none;border-radius:5px;font-weight:700">
        Claim your free listing →
      </a>
    </p>
    <p style="color:#64748b;font-size:.9rem">If you're not taking on new work right now, no worries — happy to hear from you when things slow down.</p>
    <p>Cheers,<br><strong>Ben</strong><br>
    <a href="https://tradietools.nz" style="color:#0055a5">TradieTools NZ</a></p>
    <hr style="border:none;border-top:1px solid #e2e8f0;margin:1.25rem 0">
    <p style="font-size:.75rem;color:#94a3b8">
      You're receiving this because your business appeared in our NZ trade directory.
      <a href="{unsub_url}" style="color:#94a3b8;font-size:.8em">Unsubscribe</a>
    </p>
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

    print(f"{'DRY RUN — ' if DRY_RUN else ''}Sending Day 4 follow-ups to {len(rows)} contacts")

    sent_count = 0
    failed = []
    already_logged = set()

    # Check who already got a follow-up
    if FOLLOWUP_LOG.exists():
        already_logged = set(FOLLOWUP_LOG.read_text().splitlines())

    for row in rows:
        email = row.get("email", "").strip()
        name  = row.get("name", "").strip()
        trade = row.get("trade", "").strip()
        region = row.get("region", "").strip()
        reviews = row.get("reviews", "0").strip()
        rating  = row.get("rating", "0").strip()

        if not email or email in already_logged:
            continue
        if unsubscribe.is_unsubscribed(email):
            print(f'  -> unsubscribed, skip')
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
