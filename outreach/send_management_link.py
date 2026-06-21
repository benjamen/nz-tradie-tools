#!/usr/bin/env python3
"""Send account management link to a tradie by their lead_token."""
import smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

TRADIE_NAME    = "Kamo Kitchens"
TRADIE_EMAIL   = "hello@kamokitchens.co.nz"
LEAD_TOKEN     = "lzVvYMiOR78QQXMn1Dwd7C20J-DCBY5NXlDmQm9evlU"
DASHBOARD_URL  = f"https://tradietools.nz/dashboard/?token={LEAD_TOKEN}"

SUBJECT = "Your TradieTools NZ listing — here's your management link"

HTML = f"""\
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body style="margin:0;padding:0;background:#f6f6f6;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f6f6f6;padding:32px 0;">
  <tr><td align="center">
    <table width="560" cellpadding="0" cellspacing="0" style="background:#fff;border:1px solid #dcdcdc;border-radius:6px;overflow:hidden;max-width:560px;width:100%;">

      <!-- Header -->
      <tr><td style="background:#1b2a4a;padding:20px 32px;">
        <p style="margin:0;color:#fff;font-size:15px;font-weight:700;">NZ Tradie Tools</p>
      </td></tr>

      <!-- Body -->
      <tr><td style="padding:32px 32px 24px;">
        <h1 style="margin:0 0 16px;font-size:20px;color:#1b1b1b;font-weight:700;">Hi Kamo Kitchens 👋</h1>

        <p style="margin:0 0 16px;font-size:15px;color:#333;line-height:1.6;">
          Thanks for listing on <strong>TradieTools NZ</strong> — your profile is live and homeowners in Whangārei can already find you.
        </p>

        <p style="margin:0 0 16px;font-size:15px;color:#333;line-height:1.6;">
          Use this secure link to manage your listing anytime — update your contact details, view leads, or upgrade your tier:
        </p>

        <!-- CTA Button -->
        <table cellpadding="0" cellspacing="0" style="margin:24px 0;">
          <tr>
            <td style="background:#005ea2;border-radius:5px;">
              <a href="{DASHBOARD_URL}"
                 style="display:inline-block;padding:13px 28px;color:#fff;font-size:15px;font-weight:700;text-decoration:none;font-family:inherit;">
                Manage my listing →
              </a>
            </td>
          </tr>
        </table>

        <p style="margin:0 0 8px;font-size:13px;color:#666;line-height:1.5;">
          Or copy this link into your browser:<br>
          <a href="{DASHBOARD_URL}" style="color:#005ea2;word-break:break-all;font-size:12px;">{DASHBOARD_URL}</a>
        </p>

        <hr style="border:none;border-top:1px solid #e5e5e5;margin:24px 0;">

        <p style="margin:0 0 12px;font-size:14px;color:#333;font-weight:700;">What can I do from my dashboard?</p>
        <ul style="margin:0 0 20px;padding-left:20px;font-size:14px;color:#444;line-height:1.7;">
          <li>Update your phone number, business name or trade category</li>
          <li>View quote requests and leads from homeowners</li>
          <li>Upgrade to <strong>Verified</strong> ($29/mo) or <strong>Pro</strong> ($59/mo) — <a href="https://tradietools.nz/tier-compare/" style="color:#005ea2;">see what's included</a></li>
          <li>Track your listing stats</li>
        </ul>

        <p style="margin:0 0 16px;font-size:14px;color:#555;line-height:1.6;">
          <strong>Keep this email</strong> — your management link is unique to your listing. It's the secure way to access your account without needing a password.
        </p>

        <p style="margin:0;font-size:14px;color:#555;line-height:1.6;">
          Any questions? Just reply to this email.<br><br>
          Cheers,<br>
          <strong>Ben</strong><br>
          <span style="color:#888;">TradieTools NZ</span>
        </p>
      </td></tr>

      <!-- Footer -->
      <tr><td style="background:#f6f6f6;border-top:1px solid #e5e5e5;padding:16px 32px;">
        <p style="margin:0;font-size:11px;color:#999;line-height:1.5;">
          This email was sent to {TRADIE_EMAIL} because you listed on TradieTools NZ.<br>
          Your listing: <a href="https://tradietools.nz/businesses/kamo-kitchens/" style="color:#999;">tradietools.nz/businesses/kamo-kitchens/</a>
        </p>
      </td></tr>

    </table>
  </td></tr>
</table>
</body>
</html>
"""

TEXT = f"""\
Hi Kamo Kitchens,

Thanks for listing on TradieTools NZ — your profile is live and homeowners in Whangarei can already find you.

Use this secure link to manage your listing anytime:
{DASHBOARD_URL}

From your dashboard you can:
- Update your contact details
- View leads and quote requests
- Upgrade to Verified ($29/mo) or Pro ($59/mo)

Keep this email — the link is your secure access to your account.

Any questions? Just reply.

Cheers,
Ben
TradieTools NZ
"""

def send():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From']    = f"Ben @ TradieTools NZ <{SMTP_USER}>"
    msg['To']      = TRADIE_EMAIL
    msg['Reply-To'] = SMTP_USER
    msg.attach(MIMEText(TEXT, 'plain'))
    msg.attach(MIMEText(HTML, 'html'))

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, [TRADIE_EMAIL], msg.as_string())
    print(f"✓ Sent management link to {TRADIE_EMAIL}")

if __name__ == '__main__':
    print(f"Sending management link to: {TRADIE_EMAIL}")
    print(f"Dashboard URL: {DASHBOARD_URL}")
    send()
