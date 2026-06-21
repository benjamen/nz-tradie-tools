"""
Retry send_failed contacts from any wave CSV.
Usage: .venv/bin/python3 outreach/retry_failed.py [wave1|wave2|all]
"""
import csv, smtplib, time, random, sys
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import daily_limit

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
SITE_URL  = "https://tradietools.nz"

DIR = Path(__file__).parent

CSVS = {
    'wave1': DIR / 'contacts_found.csv',
    'wave2': DIR / 'contacts_wave2.csv',
}


def make_email(name, trade, region, listing_id=""):
    claim_url = f"{SITE_URL}/signup/?ref=claim&id={listing_id}" if listing_id else f"{SITE_URL}/signup/?ref=claim"
    html = f"""<!DOCTYPE html>
<html><body style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#334155">
<div style="background:#0055a5;padding:1rem 1.5rem">
  <span style="color:#fff;font-weight:700;font-size:1rem">TradieTools NZ</span>
</div>
<div style="padding:1.5rem;border:1px solid #e2e8f0;border-top:none">
  <p>Hi {name},</p>
  <p>We're building NZ's best tradie directory and your {trade} business in {region} already has a listing — with your Google reviews included.</p>
  <p>Claim it free so homeowners in {region} can contact you directly:</p>
  <p style="margin:1.5rem 0">
    <a href="{claim_url}" style="background:#ea6325;color:#fff;padding:.75rem 1.5rem;text-decoration:none;border-radius:5px;font-weight:700;font-size:1rem">
      Claim my free listing →
    </a>
  </p>
  <p style="font-size:.85rem;color:#64748b">Takes 2 minutes. No credit card required.</p>
  <p style="font-size:.8rem;color:#94a3b8;margin-top:2rem;border-top:1px solid #e2e8f0;padding-top:1rem">
    TradieTools NZ · <a href="https://tradietools.nz" style="color:#0055a5">tradietools.nz</a>
    · <a href="https://tradietools.nz/unsubscribe/" style="color:#94a3b8">Unsubscribe</a>
  </p>
</div>
</body></html>"""
    return html


def send(to_email, name, trade, region, listing_id=""):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Your {trade} listing on TradieTools — claim it free"
    msg['From']    = f"Ben from TradieTools NZ <{SMTP_USER}>"
    msg['To']      = to_email
    msg['Reply-To'] = "contact@tradietools.nz"
    msg.attach(MIMEText(make_email(name, trade, region, listing_id), 'html'))
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, to_email, msg.as_string())


def retry_csv(csv_path, wave_label):
    print(f"\n=== {wave_label} — {csv_path.name} ===")
    with open(csv_path) as f:
        rows = list(csv.DictReader(f))

    failed = [r for r in rows if r.get('status') == 'send_failed' and r.get('email')]
    print(f"  {len(failed)} send_failed contacts")

    retried = 0
    for r in failed:
        name       = r.get('name', 'there')
        trade      = r.get('trade', 'tradie')
        region     = r.get('region', 'NZ')
        email      = r['email']
        listing_id = r.get('listing_id', '')
        if not daily_limit.under_limit():
            print(f"  ⏸ daily limit ({daily_limit.LIMIT}) reached — stopping")
            break
        try:
            send(email, name, trade, region, listing_id)
            r['status'] = 'sent'
            daily_limit.record_send()
            retried += 1
            print(f"  ✓ sent: {name} ({email})")
        except Exception as e:
            print(f"  ✗ failed again: {name} — {e}")
        time.sleep(random.uniform(8, 15))

    # Write back updated CSV
    if retried > 0:
        fieldnames = list(rows[0].keys()) if rows else []
        with open(csv_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        print(f"  Updated {csv_path.name} ({retried} rows → sent)")
    return retried


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    total = 0
    if target in ('wave1', 'all') and CSVS['wave1'].exists():
        total += retry_csv(CSVS['wave1'], 'Wave 1')
    if target in ('wave2', 'all') and CSVS['wave2'].exists():
        total += retry_csv(CSVS['wave2'], 'Wave 2')
    print(f"\nDone. Retried {total} contacts.")


if __name__ == '__main__':
    main()
