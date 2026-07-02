"""One-off nurture emails to organic template downloaders."""
import smtplib, ssl, os, sys, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sys.path.insert(0, os.path.dirname(__file__))
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, dkim_sign

SIGNUP_URL = "https://tradietools.nz/signup/"

LEADS = [
    {
        "to_email": "Karl@beckerbuilding.co.nz",
        "to_name":  "Karl",
        "business": "Becker Building",
        "trade":    "builder",
        "template": "handover checklist",
        "template_note": "Having a solid handover process makes a real difference — both for the client relationship and your paper trail if anything comes up later.",
    },
    {
        "to_email": "clare@tasbayplumbing.co.nz",
        "to_name":  "Clare",
        "business": "Tas Bay Plumbing",
        "trade":    "plumber",
        "template": "incident report template",
        "template_note": "Good to have that documented — incident records are one of those things you hope you never need but are really glad you have when you do.",
    },
    {
        "to_email": "wilsonconcrete2002@gmail.com",
        "to_name":  "there",
        "business": "your concrete business",
        "trade":    "concreter",
        "template": "site safety plan",
        "template_note": "Site safety docs are one of those things worth getting right early — saves a lot of headaches down the track.",
    },
    {
        "to_email": "eddygraham21@gmail.com",
        "to_name":  "Eddy",
        "business": "your business",
        "trade":    "tradie",
        "template": "subcontractor agreement",
        "template_note": "A solid subcontractor agreement makes a big difference when you're bringing on subbies — good to get that sorted.",
    },
    {
        "to_email": "Fairsiminvestments@gmail.com",
        "to_name":  "there",
        "business": "your business",
        "trade":    "tradie",
        "template": "terms of trade",
        "template_note": "Terms of trade are one of the most important documents to have right — they protect you when clients try to shift goalposts.",
    },
]


def make_email(lead):
    name        = lead["to_name"]
    biz         = lead["business"]
    trade       = lead["trade"]
    template    = lead["template"]
    note        = lead["template_note"]

    subject = f"Re: your {template} from TradieTools"

    html = f"""\
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f6f6f6;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f6f6f6;padding:32px 0;">
  <tr><td align="center">
    <table width="560" cellpadding="0" cellspacing="0" style="background:#fff;border:1px solid #dcdcdc;border-radius:6px;overflow:hidden;max-width:560px;width:100%;">

      <tr><td style="background:#1b2a4a;padding:20px 32px;">
        <p style="margin:0;color:#fff;font-size:15px;font-weight:700;">NZ Tradie Tools</p>
      </td></tr>

      <tr><td style="padding:32px;">
        <p style="margin:0 0 16px;font-size:15px;color:#222;">Hi {name},</p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          Noticed you grabbed our <strong>{template}</strong> from TradieTools — hope it's been useful.
          {note}
        </p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          While you're here — we run a free NZ tradie directory at
          <a href="https://tradietools.nz" style="color:#005ea2;">tradietools.nz</a>
          that connects homeowners with local {trade}s. If {biz} isn't listed yet,
          it takes about 2 minutes to set up and it's completely free.
        </p>

        <p style="margin:0 0 24px;text-align:center;">
          <a href="{SIGNUP_URL}"
             style="display:inline-block;background:#e85d26;color:#fff;font-weight:700;
                    font-size:15px;padding:12px 28px;border-radius:5px;text-decoration:none;">
            Claim Your Free Listing →
          </a>
        </p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          No lock-in, no credit card — just your listing visible to homeowners searching
          for a {trade} in your area.
        </p>

        <p style="margin:0 0 4px;font-size:15px;color:#222;">Cheers,</p>
        <p style="margin:0;font-size:15px;color:#222;font-weight:600;">Ben</p>
        <p style="margin:4px 0 0;font-size:13px;color:#666;">NZ Tradie Tools &nbsp;|&nbsp; tradietools.nz</p>
      </td></tr>

      <tr><td style="background:#f6f6f6;padding:16px 32px;border-top:1px solid #e5e7eb;">
        <p style="margin:0;font-size:12px;color:#999;text-align:center;">
          NZ Tradie Tools · tradietools.nz<br>
          <a href="https://tradietools.nz/unsubscribe/?type=outreach&email={lead['to_email'].lower()}"
             style="color:#999;">Unsubscribe</a>
        </p>
      </td></tr>

    </table>
  </td></tr>
</table>
</body>
</html>"""

    text = f"""Hi {name},

Noticed you grabbed our {template} from TradieTools — hope it's been useful. {note}

While you're here — we run a free NZ tradie directory at tradietools.nz that connects homeowners with local {trade}s. If {biz} isn't listed yet, it takes about 2 minutes to set up and it's completely free:

{SIGNUP_URL}

No lock-in, no credit card — just your listing visible to homeowners searching for a {trade} in your area.

Cheers,
Ben
NZ Tradie Tools | tradietools.nz
"""
    return subject, html, text


def send(lead):
    subject, html, text = make_email(lead)
    msg = MIMEMultipart('alternative')
    msg['Subject']  = subject
    msg['From']     = f"Ben @ TradieTools NZ <{SMTP_USER}>"
    msg['To']       = lead["to_email"]
    msg['Reply-To'] = SMTP_USER
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, [lead["to_email"]], dkim_sign(msg))
    print(f"  ✓ {lead['to_email']}")


if __name__ == '__main__':
    print(f"Sending to {len(LEADS)} template leads...")
    for lead in LEADS:
        try:
            send(lead)
            time.sleep(2)
        except Exception as e:
            print(f"  ✗ {lead['to_email']}: {e}")
    print("Done.")
