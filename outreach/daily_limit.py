"""
Shared 50-per-day send cap across all outreach scripts.
Writes outreach/sent_YYYY-MM-DD.count to track daily sends.
"""
from datetime import date
from pathlib import Path

LIMIT = 50
_DIR = Path(__file__).parent


def _count_file():
    return _DIR / f"sent_{date.today().isoformat()}.count"


def sends_today():
    f = _count_file()
    return int(f.read_text().strip()) if f.exists() else 0


def under_limit():
    return sends_today() < LIMIT


def record_send():
    f = _count_file()
    n = (int(f.read_text().strip()) if f.exists() else 0) + 1
    f.write_text(str(n))
    return n


def remaining():
    return max(0, LIMIT - sends_today())
