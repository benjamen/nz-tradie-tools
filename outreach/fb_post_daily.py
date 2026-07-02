"""
Daily Facebook post — TradieTools NZ.
Rotates through cost guide / article content, posts to the TradieTools Facebook Page.

Run:  venv/bin/python3 outreach/fb_post_daily.py [--dry-run]
Cron: 0 9 * * * (9am NZT — use NZST/NZDT offset when scheduling)

Requires in outreach/.env:
  FB_PAGE_TOKEN=...   (Page Access Token from Graph API Explorer)
  FB_PAGE_ID=...      (1210712172124925)
"""
import os
import re
import sys
import json
import random
from pathlib import Path
from datetime import date, timedelta

import requests

sys.path.insert(0, str(Path(__file__).parent))

# Load .env
_env = Path(__file__).parent / ".env"
if _env.exists():
    for line in _env.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

FB_PAGE_TOKEN = os.environ.get("FB_PAGE_TOKEN", "")
FB_PAGE_ID    = os.environ.get("FB_PAGE_ID", "1210712172124925")
GRAPH_BASE    = "https://graph.facebook.com/v25.0"
ARTICLES_DIR  = Path(__file__).parent.parent / "content" / "articles"
POST_LOG      = Path(__file__).parent / "fb_posted.log"
BASE_URL      = "https://tradietools.nz"
DRY_RUN       = "--dry-run" in sys.argv


def parse_frontmatter(text: str) -> dict:
    """Extract YAML-ish frontmatter from markdown (simple key: value only)."""
    meta = {}
    if not text.startswith("---"):
        return meta
    end = text.find("---", 3)
    if end == -1:
        return meta
    for line in text[3:end].splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta


def first_paragraph(text: str) -> str:
    """Get the first non-empty paragraph after the frontmatter + heading."""
    in_fm = False
    past_fm = False
    past_heading = False
    for line in text.splitlines():
        if line.strip() == "---":
            in_fm = not in_fm
            if not in_fm:
                past_fm = True
            continue
        if in_fm or not past_fm:
            continue
        if line.startswith("#"):
            past_heading = True
            continue
        if not past_heading:
            continue
        stripped = line.strip()
        if (stripped and not stripped.startswith("#") and not stripped.startswith("|")
                and not stripped.startswith("!") and not stripped.startswith("*")
                and len(stripped.split()) >= 20):
            # Trim to ~180 chars at a sentence boundary
            if len(stripped) > 180:
                cut = stripped[:180]
                last_dot = cut.rfind(".")
                if last_dot > 100:
                    stripped = cut[:last_dot + 1]
                else:
                    stripped = cut.rstrip() + "…"
            return stripped
    return ""


def slug_from_path(p: Path) -> str:
    return p.stem


def build_post(meta: dict, first_para: str, slug: str) -> str:
    title = meta.get("title", meta.get("seo_title", slug.replace("-", " ").title()))
    url   = f"{BASE_URL}/articles/{slug}/"

    # Pick 3–4 relevant hashtags from tags field
    raw_tags = meta.get("tags", "")
    # Strip list brackets and quotes
    tags = re.findall(r'"([^"]+)"', raw_tags) or re.findall(r"'([^']+)'", raw_tags)
    trade_tags = [
        "#" + t.replace(" ", "").replace("-", "") + "NZ"
        for t in tags[:3]
        if len(t) < 20
    ]
    hashtags = " ".join(trade_tags) if trade_tags else "#TradieNZ #HomeRenovation"
    if "#TradieToolsNZ" not in hashtags:
        hashtags += " #TradieToolsNZ"

    body = f"""{title}

{first_para}

Read the full guide 👇
{url}

{hashtags}"""
    return body.strip()


def load_posted() -> set:
    if not POST_LOG.exists():
        return set()
    return set(POST_LOG.read_text().splitlines())


def mark_posted(slug: str) -> None:
    with POST_LOG.open("a") as f:
        f.write(slug + "\n")


def pick_article(articles: list[Path], posted: set) -> Path | None:
    """Pick an unposted article. Prefer cost guides, then any article."""
    unposted = [a for a in articles if a.stem not in posted]
    if not unposted:
        # All posted — reset and start over (keep last 30 to avoid immediate repeats)
        recent = list(posted)[-30:] if len(posted) >= 30 else list(posted)
        unposted = [a for a in articles if a.stem not in set(recent)]
        if not unposted:
            return None

    # Prefer cost guides for higher engagement
    cost = [a for a in unposted if "cost" in a.stem]
    pool = cost if cost else unposted
    return random.choice(pool)


def post_to_facebook(message: str) -> dict:
    url  = f"{GRAPH_BASE}/{FB_PAGE_ID}/feed"
    resp = requests.post(url, data={
        "message":      message,
        "access_token": FB_PAGE_TOKEN,
    }, timeout=30)
    return resp.json()


def main():
    if not FB_PAGE_TOKEN:
        print("ERROR: FB_PAGE_TOKEN not set in outreach/.env")
        print("Add: FB_PAGE_TOKEN=<your page access token>")
        sys.exit(1)

    articles = sorted(ARTICLES_DIR.glob("*.md"))
    if not articles:
        print("No articles found in", ARTICLES_DIR)
        sys.exit(1)

    posted = load_posted()
    article = pick_article(articles, posted)
    if not article:
        print("No articles available to post")
        sys.exit(0)

    text    = article.read_text(encoding="utf-8")
    meta    = parse_frontmatter(text)
    first_p = first_paragraph(text)
    slug    = slug_from_path(article)
    message = build_post(meta, first_p, slug)

    print(f"{'DRY RUN — ' if DRY_RUN else ''}Article: {slug}")
    print("-" * 60)
    print(message)
    print("-" * 60)

    if DRY_RUN:
        print("(dry run — not posted)")
        return

    result = post_to_facebook(message)
    if "id" in result:
        print(f"Posted! Post ID: {result['id']}")
        mark_posted(slug)
    else:
        print(f"ERROR posting to Facebook: {result}")
        error = result.get("error", {})
        print(f"  Code: {error.get('code')}  Message: {error.get('message')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
