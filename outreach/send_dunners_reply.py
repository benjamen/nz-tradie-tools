"""One-off: reply to Connor (Dunners Concrete) — thanks + website design pitch."""
import smtplib, ssl, os, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sys.path.insert(0, os.path.dirname(__file__))
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, dkim_sign

TO_EMAIL  = "dunnersconcrete@gmail.com"
TO_NAME   = "Connor"
DEMO_URL  = "https://tradietools.nz/demo/dunners-concrete/"
SUBJECT   = "Re: TradieTools listing — also, we built you something"

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

      <tr><td style="background:#1b2a4a;padding:20px 32px;">
        <p style="margin:0;color:#fff;font-size:15px;font-weight:700;">NZ Tradie Tools</p>
      </td></tr>

      <tr><td style="padding:32px;">
        <p style="margin:0 0 16px;font-size:15px;color:#222;">Hi {TO_NAME},</p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          Thanks for getting in touch — really appreciated hearing from you, and good to know a
          site refresh is on the radar for later in the year.
        </p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          While we had your details up we actually put together a quick demo site for Dunners
          Concrete — using your logo, brand colours, and your full service list — so you can see
          what a modern lead-capture site could look like:
        </p>

        <p style="margin:0 0 24px;text-align:center;">
          <a href="{DEMO_URL}"
             style="display:inline-block;background:#ff8400;color:#fff;font-weight:700;
                    font-size:15px;padding:12px 28px;border-radius:5px;text-decoration:none;">
            View Your Demo Site →
          </a>
        </p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          The form on the demo connects directly to our lead system, so any enquiry submitted
          goes straight to you — no middleman, no shared regional pool.
        </p>

        <p style="margin:0 0 8px;font-size:15px;color:#222;line-height:1.6;">
          One other thing worth mentioning: we also design and build sites like this as a
          standalone service. Pricing is straightforward:
        </p>

        <table cellpadding="0" cellspacing="0" style="margin:16px 0 24px;width:100%;border:1px solid #e5e7eb;border-radius:6px;overflow:hidden;">
          <tr style="background:#f0f7ff;">
            <td style="padding:12px 16px;font-size:14px;font-weight:700;color:#1b2a4a;">Website design &amp; build</td>
            <td style="padding:12px 16px;font-size:14px;font-weight:700;color:#1b2a4a;text-align:right;">$499 one-off</td>
          </tr>
          <tr>
            <td style="padding:12px 16px;font-size:14px;color:#444;border-top:1px solid #e5e7eb;">Hosting &amp; domain</td>
            <td style="padding:12px 16px;font-size:14px;color:#444;border-top:1px solid #e5e7eb;text-align:right;">At cost (passed through, no markup)</td>
          </tr>
        </table>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          That covers a fully custom site built around your brand, services, and the quote form
          you already use — plus we handle the setup so you don't have to deal with any of the
          technical side.
        </p>

        <p style="margin:0 0 16px;font-size:15px;color:#222;line-height:1.6;">
          No pressure at all — happy to chat more when the timing is right. If you have any
          questions or want to tweak anything on the demo in the meantime, just reply here.
        </p>

        <p style="margin:0 0 4px;font-size:15px;color:#222;">Cheers,</p>
        <p style="margin:0;font-size:15px;color:#222;font-weight:600;">Ben</p>
        <p style="margin:4px 0 0;font-size:13px;color:#666;">NZ Tradie Tools &nbsp;|&nbsp; tradietools.nz</p>
      </td></tr>

      <tr><td style="background:#f6f6f6;padding:16px 32px;border-top:1px solid #e5e7eb;">
        <p style="margin:0;font-size:12px;color:#999;text-align:center;">
          NZ Tradie Tools · tradietools.nz<br>
          <a href="https://tradietools.nz/unsubscribe/?type=outreach&email=dunnersconcrete%40gmail.com"
             style="color:#999;">Unsubscribe</a>
        </p>
      </td></tr>

    </table>
  </td></tr>
</table>
</body>
</html>
"""

TEXT = f"""Hi {TO_NAME},

Thanks for getting in touch — really appreciated hearing from you, and good to know a site refresh is on the radar for later in the year.

While we had your details up we actually put together a quick demo site for Dunners Concrete — using your logo, brand colours, and your full service list — so you can see what a modern lead-capture site could look like:

{DEMO_URL}

The form on the demo connects directly to our lead system, so any enquiry submitted goes straight to you — no middleman, no shared regional pool.

One other thing worth mentioning: we also design and build sites like this as a standalone service. Pricing is straightforward:

  Website design & build: $499 one-off
  Hosting & domain: at cost (passed through, no markup)

That covers a fully custom site built around your brand, services, and the quote form you already use — plus we handle the setup so you don't have to deal with any of the technical side.

No pressure at all — happy to chat more when the timing is right. If you have any questions or want to tweak anything on the demo in the meantime, just reply here.

Cheers,
Ben
NZ Tradie Tools | tradietools.nz
"""


def send():
    msg = MIMEMultipart('alternative')
    msg['Subject']  = SUBJECT
    msg['From']     = f"Ben @ TradieTools NZ <{SMTP_USER}>"
    msg['To']       = f"{TO_NAME} @ Dunners Concrete <{TO_EMAIL}>"
    msg['Reply-To'] = SMTP_USER

    msg.attach(MIMEText(TEXT, 'plain'))
    msg.attach(MIMEText(HTML, 'html'))

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, [TO_EMAIL], dkim_sign(msg))
    print(f"Sent to {TO_EMAIL}")


if __name__ == '__main__':
    send()
