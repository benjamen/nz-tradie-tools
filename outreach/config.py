"""Loads SMTP credentials from outreach/.env (never committed)."""
import os
from pathlib import Path

_env = Path(__file__).parent / '.env'
if _env.exists():
    for line in _env.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, _, v = line.partition('=')
            os.environ.setdefault(k.strip(), v.strip())

SMTP_HOST = os.environ.get('SMTP_HOST', 'smtp.hostinger.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '465'))
SMTP_USER = os.environ.get('SMTP_USER', '')
SMTP_PASS = os.environ.get('SMTP_PASS', '')
UNSUB_SECRET = os.environ.get('UNSUB_SECRET', '')


_GENERIC_PREFIXES = {
    'info', 'contact', 'hello', 'admin', 'office', 'sales', 'support',
    'enquiries', 'enquiry', 'accounts', 'reception', 'mail', 'team',
    'noreply', 'no-reply', 'service', 'help', 'billing', 'post',
    'webmaster', 'marketing', 'media', 'news', 'general',
}


def first_name(business_name: str, email: str = '') -> str:
    """Return a personal first name to use in email greetings.

    Tries the email prefix first (hoan@ → 'Hoan'), falls back to 'there'
    if the prefix is a generic inbox word or the business name first word
    looks like a non-person word.
    """
    if email:
        prefix = email.split('@')[0].split('.')[0].split('+')[0].lower()
        if prefix and prefix not in _GENERIC_PREFIXES and prefix.isalpha() and len(prefix) >= 2:
            return prefix.capitalize()
    return 'there'


def unsub_link(email: str) -> str:
    """Return a signed one-click unsubscribe URL for outreach emails."""
    import hmac, hashlib, urllib.parse
    sig = hmac.new(UNSUB_SECRET.encode(), email.lower().encode(), hashlib.sha256).hexdigest()[:16]
    return (
        'https://tradietools.nz/unsubscribe/?type=outreach'
        '&email=' + urllib.parse.quote(email.lower())
        + '&sig=' + sig
    )
