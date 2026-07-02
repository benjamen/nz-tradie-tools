"""
Daily LinkedIn post — TradieTools NZ company page.
Mirrors fb_post_daily.py — rotates through articles, posts to company page.

Run:  venv/bin/python3 outreach/li_post_daily.py [--dry-run]
Cron: runs alongside fb_post_daily.py at 9am NZT

Requires in outreach/.env:
  LI_ACCESS_TOKEN=...   (LinkedIn OAuth token — see README or get from Zapier)
  LI_COMPANY_ID=136044253
"""
import os, re, sys, json, random
from pathlib import Path
from datetime import date

import requests

sys.path.insert(0, str(Path(__file__).parent))

_env = Path(__file__).parent / ".env"
if _env.exists():
    for line in _env.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

LI_ACCESS_TOKEN = os.environ.get("LI_ACCESS_TOKEN", "")
LI_COMPANY_ID   = os.environ.get("LI_COMPANY_ID", "136044253")
ARTICLES_DIR    = Path(__file__).parent.parent / "content" / "articles"
POST_LOG        = Path(__file__).parent / "li_posted.log"
BASE_URL        = "https://tradietools.nz"
DRY_RUN         = "--dry-run" in sys.argv


def parse_frontmatter(text):
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


def first_paragraph(text):
    in_fm = past_fm = past_heading = False
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
        s = line.strip()
        if s and not s.startswith(("#", "|", "!", "*")) and len(s.split()) >= 20:
            if len(s) > 200:
                cut = s[:200]
                dot = cut.rfind(".")
                s = cut[:dot + 1] if dot > 100 else cut.rstrip() + "…"
            return s
    return ""


def build_post(meta, first_para, slug):
    title = meta.get("title", meta.get("seo_title", slug.replace("-", " ").title()))
    url   = f"{BASE_URL}/articles/{slug}/"
    raw_tags = meta.get("tags", "")
    tags = re.findall(r'"([^"]+)"', raw_tags) or re.findall(r"'([^']+)'", raw_tags)
    trade_tags = ["#" + t.replace(" ", "").replace("-", "") + "NZ" for t in tags[:3] if len(t) < 20]
    hashtags = " ".join(trade_tags) if trade_tags else "#TradieNZ #HomeRenovation"
    if "#TradieToolsNZ" not in hashtags:
        hashtags += " #TradieToolsNZ"
    return f"{title}\n\n{first_para}\n\nRead the full guide: {url}\n\n{hashtags}".strip()


def load_posted():
    if not POST_LOG.exists():
        return set()
    return set(POST_LOG.read_text().splitlines())


def mark_posted(slug):
    with POST_LOG.open("a") as f:
        f.write(slug + "\n")


def pick_article(articles, posted):
    unposted = [a for a in articles if a.stem not in posted]
    if not unposted:
        recent = set(list(posted)[-30:]) if len(posted) >= 30 else posted
        unposted = [a for a in articles if a.stem not in recent]
        if not unposted:
            return None
    cost = [a for a in unposted if "cost" in a.stem]
    return random.choice(cost if cost else unposted)


def post_to_linkedin(message, url, title, description):
    """Post to LinkedIn company page via v2 API."""
    org_urn = f"urn:li:organization:{LI_COMPANY_ID}"
    payload = {
        "author": org_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": message},
                "shareMediaCategory": "ARTICLE",
                "media": [{
                    "status": "READY",
                    "description": {"text": description[:256]},
                    "originalUrl": url,
                    "title": {"text": title[:200]},
                }],
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    resp = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers={
            "Authorization": f"Bearer {LI_ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        json=payload,
        timeout=30,
    )
    return resp.status_code, resp.json() if resp.content else {}


def main():
    if not LI_ACCESS_TOKEN:
        print("ERROR: LI_ACCESS_TOKEN not set in outreach/.env")
        print("Get token: https://www.linkedin.com/developers/tools/oauth/token-generator")
        print("Scopes needed: w_organization_social, r_organization_social")
        sys.exit(1)

    articles = sorted(ARTICLES_DIR.glob("*.md"))
    if not articles:
        print("No articles found")
        sys.exit(1)

    posted  = load_posted()
    article = pick_article(articles, posted)
    if not article:
        print("No articles available")
        sys.exit(0)

    text    = article.read_text(encoding="utf-8")
    meta    = parse_frontmatter(text)
    slug    = article.stem
    first_p = first_paragraph(text)
    message = build_post(meta, first_p, slug)
    title   = meta.get("title", slug.replace("-", " ").title())
    url     = f"{BASE_URL}/articles/{slug}/"
    desc    = first_p[:256] if first_p else title

    print(f"{'DRY RUN — ' if DRY_RUN else ''}Article: {slug}")
    print("-" * 60)
    print(message)
    print("-" * 60)

    if DRY_RUN:
        print("(dry run — not posted)")
        return

    status, result = post_to_linkedin(message, url, title, desc)
    if status in (200, 201):
        post_id = result.get("id", "unknown")
        print(f"Posted! LinkedIn post ID: {post_id}")
        mark_posted(slug)
    else:
        print(f"ERROR {status}: {result}")
        sys.exit(1)


if __name__ == "__main__":
    main()
