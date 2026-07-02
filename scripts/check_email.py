#!/usr/bin/env python3
"""
Read unread emails from contact@tradietools.nz inbox.
Outputs JSON array of new emails, then marks them as read.
Usage: python3 check_email.py [--dry-run]
"""
import imaplib, email, json, sys, os, re
from email.header import decode_header
from datetime import datetime

IMAP_HOST = "imap.hostinger.com"
IMAP_PORT = 993
IMAP_USER = "contact@tradietools.nz"
IMAP_PASS = os.environ.get("IMAP_PASS", "jxg0-a3qd-hzqs-31wu")

DRY_RUN = "--dry-run" in sys.argv


def decode_str(value):
    if not value:
        return ""
    parts = decode_header(value)
    result = []
    for part, enc in parts:
        if isinstance(part, bytes):
            result.append(part.decode(enc or "utf-8", errors="replace"))
        else:
            result.append(part)
    return "".join(result)


def get_body(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            cd = str(part.get("Content-Disposition", ""))
            if ct == "text/plain" and "attachment" not in cd:
                try:
                    body = part.get_payload(decode=True).decode(
                        part.get_content_charset() or "utf-8", errors="replace"
                    )
                    break
                except Exception:
                    pass
    else:
        try:
            body = msg.get_payload(decode=True).decode(
                msg.get_content_charset() or "utf-8", errors="replace"
            )
        except Exception:
            body = str(msg.get_payload())
    # Clean up excessive whitespace
    body = re.sub(r"\n{3,}", "\n\n", body.strip())
    return body[:4000]  # cap at 4k chars


def classify(subject, body, sender):
    text = (subject + " " + body).lower()
    s = sender.lower()
    if "mailer-daemon" in s or "delivery system" in s or "undelivered" in subject.lower() or "550" in body:
        return "bounce"
    if any(w in text for w in ["broken", "error", "not working", "bug", "wrong", "missing", "404", "crash"]):
        return "bug_report"
    if any(w in text for w in ["claim", "listing", "sign up", "signup", "dashboard", "link"]):
        return "claim_support"
    if any(w in text for w in ["unsubscribe", "remove", "opt out", "spam"]):
        return "unsubscribe"
    if any(w in text for w in ["quote", "lead", "job"]):
        return "quote_query"
    return "general"


def main():
    conn = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    conn.login(IMAP_USER, IMAP_PASS)
    conn.select("INBOX")

    _, msg_ids = conn.search(None, "UNSEEN")
    ids = msg_ids[0].split()

    results = []
    for mid in ids:
        _, data = conn.fetch(mid, "(RFC822)")
        raw = data[0][1]
        msg = email.message_from_bytes(raw)

        subject = decode_str(msg.get("Subject", ""))
        sender  = decode_str(msg.get("From", ""))
        date    = msg.get("Date", "")
        msg_id  = msg.get("Message-ID", "")
        body    = get_body(msg)

        results.append({
            "imap_id":  mid.decode(),
            "message_id": msg_id,
            "from":     sender,
            "subject":  subject,
            "date":     date,
            "body":     body,
            "category": classify(subject, body, sender),
        })

        if not DRY_RUN:
            conn.store(mid, "+FLAGS", "\\Seen")

    conn.logout()
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return len(results)


if __name__ == "__main__":
    n = main()
    sys.stderr.write(f"{n} new email(s) processed\n")
