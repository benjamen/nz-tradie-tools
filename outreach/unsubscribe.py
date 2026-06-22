"""Unsubscribe list — checked before every outreach send."""
from pathlib import Path

_LIST = Path(__file__).parent / "unsubscribed.txt"


def _load():
    if not _LIST.exists():
        return set()
    return {e.strip().lower() for e in _LIST.read_text().splitlines() if e.strip()}


def is_unsubscribed(email: str) -> bool:
    return email.strip().lower() in _load()


def add(email: str):
    """Append an email to the unsubscribe list (idempotent)."""
    current = _load()
    email = email.strip().lower()
    if email not in current:
        with _LIST.open("a") as f:
            f.write(email + "\n")
        print(f"Unsubscribed: {email}")
    else:
        print(f"Already unsubscribed: {email}")
