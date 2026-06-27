"""
Send review-request emails to verified tradies asking them to invite
past clients to leave a review on their TradieTools profile.

Run: cd outreach && python3 send_review_requests.py
"""

import smtplib, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, first_name, unsub_link

TRADIES = [
    {
        "name":  "Kiwi House Decorators Limited",
        "email": "hoan@kiwihousedecorators.co.nz",
        "trade": "painting",
        "region": "Wellington",
        "slug":  "kiwi-house-decorators-limited",
    },
    {
        "name":  "Wattex Electrical Limited",
        "email": "mark@wattexelectrical.co.nz",
        "trade": "electrical",
        "region": "Wellington",
        "slug":  "wattex-electrical-limited",
    },
    {
        "name":  "Kamo Kitchens",
        "email": "hello@kamokitchens.co.nz",
        "trade": "kitchen renovation",
        "region": "Whangārei",
        "slug":  "kamo-kitchens-whangarei",
    },
    {
        "name":  "Nelson Heat Pumps",
        "email": "briar@nelsonheatpumps.nz",
        "trade": "heat pump",
        "region": "Nelson",
        "slug":  None,  # profile not built yet — send dashboard link instead
    },
]

HTML = """\
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
body{{font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#334155;font-size:15px;line-height:1.65}}
.btn{{display:inline-block;background:#16a34a;color:#fff!important;padding:12px 24px;border-radius:6px;text-decoration:none;font-weight:700;margin:16px 0;font-size:15px}}
.box{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:14px 18px;margin:14px 0;font-size:13px;color:#475569;font-family:monospace;word-break:break-all}}
.footer{{margin-top:32px;font-size:12px;color:#999;border-top:1px solid #eee;padding-top:14px}}
</style></head><body>

<p>Hi {fname},</p>

<p>Thanks for having your {trade} business listed on <a href="https://tradietools.nz">TradieTools NZ</a>.
Your profile is live and showing up for homeowners searching for a {trade} in {region}.</p>

<p>One of the biggest things that drives enquiries is <strong>reviews from past clients</strong>.
Profiles with even 2–3 genuine reviews get significantly more clicks than profiles without any.</p>

<p>Would you be up for reaching out to 2 or 3 happy past clients and asking them to leave a quick
review on your TradieTools profile? It takes them about a minute.</p>

{cta_block}

<p>You can copy and paste this message to send to clients:</p>

<div class="box">
Hi [Name], I hope all is well. I've recently set up a profile on TradieTools NZ and would really appreciate
a quick review if you have a minute — it makes a big difference for new customers finding us.
Here's the link: {profile_url}
Cheers, {biz_name}
</div>

<p>If you have any questions or want help with your profile, just reply to this email.</p>

<p>Cheers,<br><strong>Ben Walsh</strong><br>
TradieTools NZ · <a href="https://tradietools.nz">tradietools.nz</a></p>

<div class="footer">
TradieTools NZ · tradietools.nz · contact@tradietools.nz<br>
<a href="{unsub_url}" style="color:#94a3b8;font-size:.8em">Unsubscribe</a>
</div>
</body></html>"""

TEXT = """\
Hi {fname},

Thanks for having your {trade} business listed on TradieTools NZ.

One of the biggest drivers of enquiries is reviews from past clients — profiles with even
2-3 genuine reviews get significantly more clicks.

Would you be able to reach out to 2-3 happy past clients and ask them to leave a quick review?

{profile_text}

You can copy and paste this to clients:

---
Hi [Name], I've recently set up a profile on TradieTools NZ and would really appreciate a quick
review if you have a minute — it makes a big difference for new customers finding us.
Here's the link: {profile_url}
Cheers, {biz_name}
---

Any questions, just reply to this email.

Cheers,
Ben Walsh
TradieTools NZ · tradietools.nz

To unsubscribe: {unsub_url}
"""


def send_review_request(t):
    fname = first_name(t["name"], t["email"])
    unsub_url = unsub_link(t["email"])

    if t["slug"]:
        profile_url = f"https://tradietools.nz/businesses/{t['slug']}/#tt-write-review-btn"
        cta_block = (
            f'<p><strong>Your review page:</strong></p>'
            f'<a class="btn" href="{profile_url}">View your profile →</a>'
            f'<p style="font-size:.88rem;color:#475569">Share this link with past clients:<br>'
            f'<a href="https://tradietools.nz/businesses/{t["slug"]}/">'
            f'tradietools.nz/businesses/{t["slug"]}/</a></p>'
        )
        profile_text = f"Your profile: https://tradietools.nz/businesses/{t['slug']}/"
    else:
        profile_url = "https://tradietools.nz/businesses/"
        cta_block = (
            "<p>We're still building your dedicated profile page — it'll be live within "
            "the next few days. We'll email you when it's ready with the direct link to share.</p>"
        )
        profile_text = "Your profile page is being set up — we'll send you the link shortly."

    html = HTML.format(
        fname=fname, trade=t["trade"], region=t["region"],
        biz_name=t["name"], profile_url=profile_url,
        cta_block=cta_block, unsub_url=unsub_url,
    )
    text = TEXT.format(
        fname=fname, trade=t["trade"], region=t["region"],
        biz_name=t["name"], profile_url=profile_url,
        profile_text=profile_text, unsub_url=unsub_url,
    )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Get more enquiries from your TradieTools profile — a quick tip"
    msg["From"]    = "Ben @ TradieTools <contact@tradietools.nz>"
    msg["To"]      = t["email"]
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, t["email"], msg.as_string())
    print(f"  ✓ Sent to {t['email']}")


if __name__ == "__main__":
    dry = "--dry" in sys.argv
    print(f"{'DRY RUN — ' if dry else ''}Sending review request emails to {len(TRADIES)} tradies\n")
    for t in TRADIES:
        print(f"→ {t['name']} <{t['email']}>")
        if not dry:
            try:
                send_review_request(t)
            except Exception as e:
                print(f"  ✗ Failed: {e}")
        else:
            print("  [dry run — skipped]")
    print("\nDone.")
