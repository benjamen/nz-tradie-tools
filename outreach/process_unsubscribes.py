#!/usr/bin/env python3
"""
Auto-unsubscribe processor.

Polls the contact@tradietools.nz inbox via IMAP.
Any email whose subject or body contains "unsubscribe" (case-insensitive)
gets the sender added to unsubscribed.txt and receives a confirmation reply.

Run hourly via cron: 0 * * * * cd /path/to/site/outreach && python process_unsubscribes.py
"""
import imaplib
import smtplib
import ssl
import email as emaillib
import os
import sys
import re
from email.mime.text import MIMEText
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
import unsubscribe as unsub_mod

IMAP_HOST = "imap.hostinger.com"
IMAP_PORT = 993
LOG = Path(__file__).parent / "unsubscribe_processor.log"


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def is_unsubscribe_message(subject: str, body: str) -> bool:
    text = (subject + " " + body).lower()
    return "unsubscribe" in text


def send_confirmation(to_email: str, name_hint: str = ""):
    greeting = f"Hi{' ' + name_hint if name_hint else ''},"
    body = f"""{greeting}

You've been unsubscribed from TradieTools NZ outreach emails.

You won't receive any further emails from us.

If this was a mistake, reply to this email and we'll re-add you.

— Ben, TradieTools NZ
"""
    msg = MIMEText(body, "plain")
    msg["Subject"] = "You've been unsubscribed — TradieTools NZ"
    msg["From"] = f"Ben @ TradieTools NZ <{SMTP_USER}>"
    msg["To"] = to_email

    ctx = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx) as s:
            s.login(SMTP_USER, SMTP_PASS)
            s.sendmail(SMTP_USER, [to_email], msg.as_string())
        log(f"  Confirmation sent to {to_email}")
    except Exception as e:
        log(f"  Failed to send confirmation to {to_email}: {e}")


def get_text(msg) -> str:
    """Extract plain text from an email message."""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    return part.get_payload(decode=True).decode("utf-8", errors="replace")
                except Exception:
                    pass
        return ""
    try:
        return msg.get_payload(decode=True).decode("utf-8", errors="replace")
    except Exception:
        return ""


def process():
    log("Connecting to IMAP...")
    ctx = ssl.create_default_context()
    try:
        mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT, ssl_context=ctx)
        mail.login(SMTP_USER, SMTP_PASS)
    except Exception as e:
        log(f"IMAP connection failed: {e}")
        return

    mail.select("INBOX")

    # Search unread messages
    _, data = mail.search(None, "UNSEEN")
    msg_ids = data[0].split()
    log(f"Found {len(msg_ids)} unread message(s)")

    processed = 0
    for mid in msg_ids:
        _, raw = mail.fetch(mid, "(RFC822)")
        raw_email = raw[0][1]
        msg = emaillib.message_from_bytes(raw_email)

        subject = msg.get("Subject", "") or ""
        from_header = msg.get("From", "") or ""
        body = get_text(msg)

        # Extract sender email — handles .co.nz two-part TLDs
        match = re.search(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,4}", from_header)
        if not match:
            continue
        sender = match.group(0).lower()

        if is_unsubscribe_message(subject, body):
            log(f"Unsubscribe request from: {sender} (subject: {subject!r})")
            unsub_mod.add(sender)
            send_confirmation(sender)
            processed += 1
            # Mark as read
            mail.store(mid, "+FLAGS", "\\Seen")
        else:
            log(f"Not an unsubscribe — from {sender}: {subject!r}")

    mail.logout()
    log(f"Done. Processed {processed} unsubscribe request(s).")
    return processed


if __name__ == "__main__":
    process()
