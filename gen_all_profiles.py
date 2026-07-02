#!/usr/bin/env python3
"""
Generate static /businesses/[slug]/index.html for every active listing
fetched from the Frappe API. Skips slugs that already have a hand-crafted
claimed profile in data/claimed/.

Run from the site root:
    python3 gen_all_profiles.py [--dry-run]

Outputs are written to docs/businesses/[slug]/index.html.
"""

import html
import json
import os
import sys
import time
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SITE_ROOT = Path(__file__).parent
DATA_DIR   = SITE_ROOT / "data"
PUBLIC_DIR = SITE_ROOT / "docs"
BIZ_DIR    = PUBLIC_DIR / "businesses"
CLAIMED_DIR = DATA_DIR / "claimed"

API_BASE   = "https://tradietools.optified.nz"
BASE_URL   = "https://tradietools.nz"
GA_ID      = "G-BJW7HLW8D8"
FORMSPREE  = "https://formspree.io/f/xgorlloq"

DRY_RUN    = "--dry-run" in sys.argv

# ---------------------------------------------------------------------------
# Trade display-name lookup
# ---------------------------------------------------------------------------
_TRADES_FILE = DATA_DIR / "trades.json"
try:
    _trade_data = json.loads(_TRADES_FILE.read_text())
    TRADE_NAMES = {t["slug"]: t["name"] for t in _trade_data}
    TRADE_AVG   = {t["slug"]: t.get("avg_cost_nz", "") for t in _trade_data}
except Exception:
    TRADE_NAMES = {}
    TRADE_AVG   = {}

def trade_display(slug: str) -> str:
    slug = (slug or "").lower().replace(" ", "-")
    return TRADE_NAMES.get(slug, slug.replace("-", " ").title())

def trade_slug(raw: str) -> str:
    """Normalise raw trade value to known slug."""
    return (raw or "").lower().strip().replace(" ", "-")

# ---------------------------------------------------------------------------
# Helper: star string
# ---------------------------------------------------------------------------
def stars(rating: float) -> str:
    full = int(rating)
    half = 1 if (rating - full) >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + ("½" if half else "") + "☆" * empty

def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)

def json_str(s) -> str:
    return json.dumps(str(s or ""))

# ---------------------------------------------------------------------------
# Fetch all active listings via paginated API
# ---------------------------------------------------------------------------
def fetch_all_listings() -> list:
    listings = []
    offset = 0
    limit  = 200
    session = requests.Session()
    session.headers["Accept"] = "application/json"

    while True:
        url = f"{API_BASE}/api/method/tradietools.api.get_directory"
        try:
            r = session.get(url, params={"limit": limit, "offset": offset}, timeout=30)
            r.raise_for_status()
            data = r.json()
            # Frappe wraps in {"message": {...}}
            inner = data.get("message") or data
            batch = inner.get("listings", [])
            total = inner.get("total", 0)
        except Exception as e:
            print(f"  [WARN] API error at offset {offset}: {e}")
            break

        if not batch:
            break
        listings.extend(batch)
        print(f"  Fetched {len(listings)}/{total} listings…")
        if len(listings) >= total:
            break
        offset += limit
        time.sleep(0.2)

    return listings

# ---------------------------------------------------------------------------
# Already-claimed slugs (don't overwrite hand-crafted profiles)
# ---------------------------------------------------------------------------
def claimed_slugs() -> set:
    slugs = set()
    for f in CLAIMED_DIR.glob("*.json"):
        try:
            d = json.loads(f.read_text())
            slugs.add(d.get("slug", ""))
        except Exception:
            pass
    return slugs

# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------
def external_rating_html(listing: dict) -> str:
    parts = []
    if listing.get("nocowboys_rating"):
        r = listing["nocowboys_rating"]
        c = listing.get("nocowboys_reviews") or 0
        url = listing.get("nocowboys_url") or "https://www.nocowboys.co.nz"
        parts.append(
            f'<div class="ext-rating">'
            f'<span class="ext-source">NoCowboys</span>'
            f'<span class="ext-stars">{stars(r)}</span>'
            f'<strong>{r:.1f}</strong>'
            f'<span class="ext-count">({c} reviews)</span>'
            f'<a href="{esc(url)}" rel="noopener" target="_blank" class="ext-link">View →</a>'
            f'</div>'
        )
    if listing.get("builderscrack_rating"):
        r = listing["builderscrack_rating"]
        c = listing.get("builderscrack_reviews") or 0
        url = listing.get("builderscrack_url") or "https://www.builderscrack.co.nz"
        parts.append(
            f'<div class="ext-rating">'
            f'<span class="ext-source">Builderscrack</span>'
            f'<span class="ext-stars">{stars(r)}</span>'
            f'<strong>{r:.1f}</strong>'
            f'<span class="ext-count">({c} reviews)</span>'
            f'<a href="{esc(url)}" rel="noopener" target="_blank" class="ext-link">View →</a>'
            f'</div>'
        )
    if listing.get("google_rating"):
        r = listing["google_rating"]
        c = listing.get("google_reviews") or 0
        url = listing.get("google_url") or "#"
        parts.append(
            f'<div class="ext-rating">'
            f'<span class="ext-source">Google</span>'
            f'<span class="ext-stars">{stars(r)}</span>'
            f'<strong>{r:.1f}</strong>'
            f'<span class="ext-count">({c} reviews)</span>'
            + (f'<a href="{esc(url)}" rel="noopener" target="_blank" class="ext-link">View →</a>' if url != "#" else "")
            + f'</div>'
        )
    if not parts:
        return ""
    return (
        '<div class="section-title">Ratings</div>'
        '<div class="ext-ratings-wrap">' + "\n".join(parts) + "</div>"
    )


def best_rating(listing: dict):
    """Return (value, count, source) for schema markup — highest review count wins."""
    candidates = []
    if listing.get("nocowboys_rating") and listing.get("nocowboys_reviews", 0) > 0:
        candidates.append((listing["nocowboys_rating"], listing["nocowboys_reviews"], "NoCowboys"))
    if listing.get("builderscrack_rating") and listing.get("builderscrack_reviews", 0) > 0:
        candidates.append((listing["builderscrack_rating"], listing["builderscrack_reviews"], "Builderscrack"))
    if listing.get("google_rating") and listing.get("google_reviews", 0) > 0:
        candidates.append((listing["google_rating"], listing["google_reviews"], "Google"))
    if listing.get("avg_rating") and listing.get("review_count", 0) > 0:
        candidates.append((listing["avg_rating"], listing["review_count"], "TradieTools"))
    if not candidates:
        return None, None, None
    return max(candidates, key=lambda x: x[1])


def render_profile(listing: dict) -> str:
    name        = listing.get("name") or "Unknown"
    raw_trade   = listing.get("trade") or ""
    t_slug      = trade_slug(raw_trade)
    t_name      = trade_display(t_slug)
    region      = listing.get("region") or "New Zealand"
    suburb      = listing.get("suburb") or region
    slug        = listing.get("listing_slug") or ""
    phone       = listing.get("phone") or ""
    is_verified = bool(listing.get("is_verified"))
    is_premium  = bool(listing.get("is_premium"))
    is_featured = bool(listing.get("is_featured"))
    top_badge   = bool(listing.get("top_tradie_badge"))
    avg_rating  = listing.get("avg_rating") or 0
    review_count = listing.get("review_count") or 0
    response_time = listing.get("response_time_label") or ""
    hourly_rate = listing.get("hourly_rate")
    exp_years   = listing.get("experience_years")
    taking_work = listing.get("taking_work", True)

    rating_val, rating_cnt, rating_src = best_rating(listing)

    # SEO fields
    page_title  = f"{esc(name)} — {esc(t_name)} in {esc(region)}, NZ | TradieTools"
    meta_desc_parts = [f"{name} is a {t_name.lower()} based in {suburb}, {region}."]
    if rating_val and rating_cnt:
        meta_desc_parts.append(f"Rated {rating_val:.1f}/5 from {rating_cnt} reviews.")
    meta_desc_parts.append(f"Get free quotes from verified {t_name.lower()} in {region}.")
    meta_desc = esc(" ".join(meta_desc_parts))

    canonical = f"{BASE_URL}/businesses/{slug}/"
    region_slug = region.lower().replace(" ", "-")
    trade_hub   = f"/trades/{t_slug}/"
    trade_city  = f"/trades/{t_slug}/{region_slug}"

    # Schema rating block
    schema_rating = ""
    if rating_val and rating_cnt and 1 <= rating_val <= 5:
        schema_rating = f''',
          "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": {rating_val},
            "reviewCount": {rating_cnt},
            "bestRating": 5
          }}'''

    # Badges HTML
    badges_html = ""
    if is_premium:
        badges_html += '<span class="badge badge-pro">⭐ Pro Member</span>'
    elif is_verified:
        badges_html += '<span class="badge badge-verified">✅ Verified</span>'
    if top_badge:
        badges_html += '<span class="badge badge-top">🏆 Top Tradie</span>'
    if response_time:
        badges_html += f'<span class="badge badge-response">⚡ {esc(response_time)}</span>'

    # Contact
    phone_btn = (
        f'<a href="tel:{esc(phone)}" class="btn-phone">📞 {esc(phone)}</a>'
        if phone else ""
    )

    # Rate / experience
    meta_row_parts = []
    if hourly_rate:
        meta_row_parts.append(f"<span>~${hourly_rate}/hr</span>")
    if exp_years:
        meta_row_parts.append(f"<span>{exp_years} yrs experience</span>")
    if not taking_work:
        meta_row_parts.append('<span style="color:#dc2626">Not taking new work</span>')
    meta_row = " · ".join(meta_row_parts)

    # TT rating display
    tt_rating_html = ""
    if avg_rating and avg_rating >= 1 and review_count > 0:
        tt_rating_html = (
            f'<div class="profile-rating">'
            f'<span class="stars">{stars(avg_rating)}</span>'
            f'<span class="rating-num">{avg_rating:.1f}</span>'
            f'<span class="rating-count">({review_count} reviews on TradieTools)</span>'
            f'</div>'
        )

    # Claim CTA (shown if not verified or premium)
    claim_cta = ""
    if not is_verified and not is_premium:
        claim_cta = (
            f'<div class="claim-cta">'
            f'<strong>Is this your business?</strong> '
            f'<a href="/claim/?slug={esc(slug)}" style="color:#92400e;font-weight:700">Claim this listing for free →</a> '
            f'Add your contact details, photos, and get notified of quote requests.'
            f'</div>'
        )

    # External ratings
    ext_ratings = external_rating_html(listing)

    return f"""<!DOCTYPE html>
<html lang="en-NZ">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="geo.region" content="NZ">
  <meta name="geo.placename" content="{esc(region)}">
  <link rel="preconnect" href="https://tradietools.optified.nz">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&display=swap">
  <title>{page_title}</title>
  <meta name="description" content="{meta_desc}">
  <meta property="og:title" content="{esc(name)} — {esc(t_name)} in {esc(region)}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="TradieTools NZ">
  <meta property="og:image" content="{BASE_URL}/static/img/social-card.svg">
  <link rel="canonical" href="{canonical}">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": {json_str(name)},
    "description": {json_str(f"{name} — {t_name} serving {region}, New Zealand.")},
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": {json_str(suburb)},
      "addressRegion": {json_str(region)},
      "addressCountry": "NZ"
    }}{schema_rating},
    "url": "{canonical}",
    "telephone": {json_str(phone)}
  }}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"{BASE_URL}"}},
    {{"@type":"ListItem","position":2,"name":"Find a Tradie","item":"{BASE_URL}/find/"}},
    {{"@type":"ListItem","position":3,"name":{json_str(t_name)},"item":"{BASE_URL}{trade_hub}"}},
    {{"@type":"ListItem","position":4,"name":{json_str(region)},"item":"{BASE_URL}{trade_city}"}},
    {{"@type":"ListItem","position":5,"name":{json_str(name)}}}
  ]}}
  </script>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/static/css/style.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
  <style>
  .profile-header{{background:#f0f4f8;border-radius:8px;padding:1.5rem;margin-bottom:1.5rem;border:1px solid #dde3ec}}
  .profile-name{{font-size:1.5rem;font-weight:700;color:#1b2a4a;margin-bottom:.35rem}}
  .profile-trade{{display:inline-block;background:#0055a5;color:#fff;font-size:.78rem;font-weight:700;padding:.2rem .65rem;border-radius:3px;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.75rem}}
  .profile-rating{{display:flex;align-items:center;gap:.6rem;margin-bottom:.75rem}}
  .stars{{color:#f59e0b;font-size:1.1rem}}
  .rating-num{{font-size:1.1rem;font-weight:700;color:#1b2a4a}}
  .rating-count{{color:#666;font-size:.9rem}}
  .badges{{display:flex;flex-wrap:wrap;gap:.5rem;margin:.75rem 0}}
  .badge{{display:inline-flex;align-items:center;gap:.3rem;font-size:.8rem;font-weight:600;padding:.25rem .6rem;border-radius:4px}}
  .badge-verified{{background:#dcfce7;color:#166534}}
  .badge-pro{{background:#fff3cd;color:#92400e;border:1px solid #fde68a}}
  .badge-top{{background:#fef9c3;color:#854d0e}}
  .badge-response{{background:#ede9fe;color:#5b21b6}}
  .contact-buttons{{display:flex;flex-wrap:wrap;gap:.65rem;margin:1rem 0}}
  .btn-phone{{display:inline-flex;align-items:center;gap:.4rem;background:#0055a5;color:#fff;padding:.6rem 1.1rem;border-radius:6px;font-weight:600;font-size:.9rem;text-decoration:none}}
  .btn-phone:hover{{background:#003d7a}}
  .btn-quote{{display:inline-flex;align-items:center;gap:.4rem;background:#16a34a;color:#fff;padding:.6rem 1.1rem;border-radius:6px;font-weight:600;font-size:.9rem;text-decoration:none}}
  .btn-quote:hover{{background:#15803d}}
  .section-title{{font-size:1.05rem;font-weight:700;color:#1b2a4a;margin:1.25rem 0 .5rem;border-bottom:1px solid #e8ecf0;padding-bottom:.3rem}}
  .claim-cta{{background:#fff8e1;border:1px solid #ffe082;border-radius:6px;padding:.85rem 1rem;margin-top:1.5rem;font-size:.85rem;color:#78350f}}
  .ext-ratings-wrap{{display:flex;flex-direction:column;gap:.5rem;margin:.5rem 0}}
  .ext-rating{{display:flex;align-items:center;gap:.5rem;background:#fff;border:1px solid #dde3ec;border-radius:6px;padding:.65rem .9rem;font-size:.88rem}}
  .ext-source{{font-weight:700;color:#1b2a4a;min-width:110px}}
  .ext-stars{{color:#f59e0b}}
  .ext-count{{color:#64748b}}
  .ext-link{{margin-left:auto;color:#0055a5;font-size:.82rem;text-decoration:none}}
  .ext-link:hover{{text-decoration:underline}}
  .meta-row{{font-size:.85rem;color:#64748b;margin:.25rem 0}}
  .back-link{{display:inline-flex;align-items:center;gap:.3rem;font-size:.88rem;color:#0055a5;margin-bottom:1rem;text-decoration:none}}
  .back-link:hover{{text-decoration:underline}}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container">
      <a href="/" class="logo"><img src="/static/img/logo-dark.png" alt="TradieTools NZ" class="logo-img"></a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="main-nav">
        <span></span><span></span><span></span>
      </button>
      <nav class="main-nav" id="main-nav">
        <a href="/find/">Find a Tradie</a>
        <a href="/post-job/">Post a Job</a>
        <a href="/jobs/">Job Costs</a>
        <a href="/calculators/">Calculators</a>
        <a href="/articles/">Articles</a>
        <a href="/for-tradies/">For Tradies</a>
        <a href="/signup/" class="nav-cta">Free Listing →</a>
      </nav>
      <script>
      (function(){{
        var t=document.querySelector('.nav-toggle'),n=document.getElementById('main-nav');
        if(!t||!n)return;
        t.addEventListener('click',function(){{var o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',o);}});
        document.addEventListener('click',function(e){{if(!t.contains(e.target)&&!n.contains(e.target)){{n.classList.remove('is-open');t.setAttribute('aria-expanded','false');}}}});
      }})();
      </script>
    </div>
  </header>

  <div class="container" style="max-width:800px;padding-top:1.5rem;padding-bottom:3rem">
    <nav aria-label="Breadcrumb" style="font-size:.83rem;color:#64748b;margin-bottom:1rem">
      <a href="/" style="color:#0055a5">Home</a> &rsaquo;
      <a href="/find/" style="color:#0055a5">Find a Tradie</a> &rsaquo;
      <a href="{trade_hub}" style="color:#0055a5">{esc(t_name)}</a> &rsaquo;
      <a href="{trade_city}" style="color:#0055a5">{esc(region)}</a> &rsaquo;
      <span>{esc(name)}</span>
    </nav>

    <div class="profile-header">
      <div class="profile-name">{esc(name)}</div>
      <div class="profile-trade">{esc(t_name)}</div>
      {tt_rating_html}
      {'<div class="badges">' + badges_html + '</div>' if badges_html else ''}
      <p style="font-size:.9rem;color:#555;margin:.35rem 0">📍 {esc(suburb)}{(", " + esc(region)) if suburb != region else ""}</p>
      {('<p class="meta-row">' + meta_row + '</p>') if meta_row else ''}
      <div class="contact-buttons">
        {phone_btn}
        <a href="/post-job/?trade={esc(t_slug)}&region={esc(region)}" class="btn-quote">Get a free quote →</a>
      </div>
    </div>

    {ext_ratings}

    {claim_cta}

    <!-- Dynamic TradieTools reviews -->
    <div id="tt-reviews" style="margin-top:1.75rem">
      <h3 style="font-size:1.05rem;font-weight:700;margin-bottom:.75rem;color:#1e293b">
        TradieTools Reviews <span id="tt-review-count" style="font-weight:400;color:#64748b;font-size:.9rem"></span>
      </h3>
      <div id="tt-review-list"><p style="color:#64748b;font-size:.9rem">Loading reviews…</p></div>
      <button id="tt-write-review-btn"
        onclick="document.getElementById('tt-review-form').style.display='block';this.style.display='none'"
        style="margin-top:1rem;padding:.5rem 1.1rem;background:#0055a5;color:#fff;border:none;border-radius:4px;font-size:.9rem;font-weight:600;cursor:pointer">
        Write a review
      </button>
      <form id="tt-review-form" style="display:none;margin-top:1rem;background:#f8fafc;border:1px solid #dde3ec;border-radius:6px;padding:1rem">
        <h4 style="margin:0 0 .75rem;font-size:.95rem">Your review of {esc(name)}</h4>
        <label style="display:block;font-size:.85rem;font-weight:600;margin-bottom:.3rem">Rating *</label>
        <div id="tt-star-picker" style="font-size:1.6rem;cursor:pointer;margin-bottom:.75rem;letter-spacing:.1rem">
          <span data-v="1">☆</span><span data-v="2">☆</span><span data-v="3">☆</span><span data-v="4">☆</span><span data-v="5">☆</span>
        </div>
        <input type="hidden" id="tt-rating-val" value="">
        <label style="display:block;font-size:.85rem;font-weight:600;margin-bottom:.3rem">Your name *</label>
        <input id="tt-r-name" type="text" placeholder="e.g. Sarah T." style="width:100%;padding:.45rem .6rem;border:1px solid #cbd5e1;border-radius:4px;font-size:.9rem;margin-bottom:.65rem;box-sizing:border-box">
        <label style="display:block;font-size:.85rem;font-weight:600;margin-bottom:.3rem">Your email * <span style="font-weight:400;color:#64748b">(not published)</span></label>
        <input id="tt-r-email" type="email" placeholder="you@example.com" style="width:100%;padding:.45rem .6rem;border:1px solid #cbd5e1;border-radius:4px;font-size:.9rem;margin-bottom:.65rem;box-sizing:border-box">
        <label style="display:block;font-size:.85rem;font-weight:600;margin-bottom:.3rem">What type of job? <span style="font-weight:400;color:#64748b">(optional)</span></label>
        <input id="tt-r-jobtype" type="text" placeholder="e.g. Bathroom renovation" style="width:100%;padding:.45rem .6rem;border:1px solid #cbd5e1;border-radius:4px;font-size:.9rem;margin-bottom:.65rem;box-sizing:border-box">
        <label style="display:block;font-size:.85rem;font-weight:600;margin-bottom:.3rem">Your review *</label>
        <textarea id="tt-r-body" rows="4" placeholder="What was the quality of work like? Would you recommend them?" style="width:100%;padding:.45rem .6rem;border:1px solid #cbd5e1;border-radius:4px;font-size:.9rem;margin-bottom:.75rem;box-sizing:border-box;resize:vertical"></textarea>
        <p id="tt-review-msg" style="display:none;margin-bottom:.5rem;font-size:.88rem"></p>
        <button onclick="ttSubmitReview(event)" style="padding:.5rem 1.2rem;background:#16a34a;color:#fff;border:none;border-radius:4px;font-size:.9rem;font-weight:600;cursor:pointer">Submit review</button>
        <button onclick="document.getElementById('tt-review-form').style.display='none';document.getElementById('tt-write-review-btn').style.display='inline-block'" type="button"
          style="margin-left:.5rem;padding:.5rem .9rem;background:#e2e8f0;color:#334155;border:none;border-radius:4px;font-size:.9rem;cursor:pointer">Cancel</button>
      </form>
    </div>

    <div style="margin-top:1.75rem">
      <a href="{trade_city}" class="back-link">← See all {esc(t_name)} in {esc(region)}</a>
    </div>

    <div style="background:#f0f7ff;border:1px solid #bfdbfe;border-radius:8px;padding:1.25rem;margin-top:1.5rem">
      <h3 style="margin:0 0 .5rem;font-size:1rem;color:#1e3a5f">Need a {esc(t_name.lower())} in {esc(region)}?</h3>
      <p style="font-size:.9rem;color:#334155;margin:0 0 .75rem">Post your job and get free quotes from verified {esc(t_name.lower())} nearby.</p>
      <a href="/post-job/?trade={esc(t_slug)}&region={esc(region)}" style="display:inline-block;background:#0055a5;color:#fff;padding:.6rem 1.25rem;font-weight:700;text-decoration:none;border-radius:4px;font-size:.9rem">Post a free job →</a>
    </div>
  </div>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 TradieTools NZ &mdash; <a href="/privacy/">Privacy</a> &mdash; <a href="/contact/">Contact</a></p>
    </div>
  </footer>

  <script>
  (function(){{
    var SLUG = {json_str(slug)};
    var API  = 'https://tradietools.optified.nz/api/method/tradietools.api.';
    var reviewOffset = 0;
    var starPicked = 0;

    // Load reviews
    function loadReviews(){{
      fetch(API + 'get_reviews?listing_slug=' + encodeURIComponent(SLUG) + '&limit=10&offset=' + reviewOffset)
        .then(function(r){{return r.json();}})
        .then(function(d){{
          var data = d.message || d;
          var list = document.getElementById('tt-review-list');
          var count = document.getElementById('tt-review-count');
          var items = data.reviews || [];
          if(count) count.textContent = items.length ? '(' + (data.total||items.length) + ')' : '';
          if(!items.length && reviewOffset === 0){{
            list.innerHTML = '<p style="color:#64748b;font-size:.9rem">No TradieTools reviews yet — be the first!</p>';
            return;
          }}
          var html = '';
          items.forEach(function(r){{
            var stars = '★'.repeat(Math.round(r.rating||0)) + '☆'.repeat(5-Math.round(r.rating||0));
            html += '<div style="border:1px solid #e2e8f0;border-radius:6px;padding:.85rem 1rem;margin-bottom:.65rem">';
            html += '<div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.3rem">';
            html += '<span style="color:#f59e0b">' + stars + '</span>';
            html += '<strong style="font-size:.9rem">' + (r.reviewer_name||'Anonymous') + '</strong>';
            if(r.job_type) html += '<span style="font-size:.8rem;color:#64748b">&mdash; ' + r.job_type + '</span>';
            html += '</div>';
            html += '<p style="margin:0;font-size:.9rem;color:#334155">' + (r.review_body||'') + '</p>';
            html += '</div>';
          }});
          list.innerHTML += html;
          reviewOffset += items.length;
        }})
        .catch(function(){{
          document.getElementById('tt-review-list').innerHTML = '<p style="color:#94a3b8;font-size:.88rem">Reviews unavailable.</p>';
        }});
    }}
    loadReviews();

    // Star picker
    var picker = document.getElementById('tt-star-picker');
    if(picker){{
      picker.querySelectorAll('span').forEach(function(s){{
        s.addEventListener('mouseover',function(){{
          var v=parseInt(s.dataset.v);
          picker.querySelectorAll('span').forEach(function(x,i){{x.textContent=i<v?'★':'☆';}});
        }});
        s.addEventListener('click',function(){{
          starPicked=parseInt(s.dataset.v);
          document.getElementById('tt-rating-val').value=starPicked;
        }});
      }});
      picker.addEventListener('mouseleave',function(){{
        picker.querySelectorAll('span').forEach(function(x,i){{x.textContent=i<starPicked?'★':'☆';}});
      }});
    }}

    window.ttSubmitReview = function(e){{
      e.preventDefault();
      var rating=parseInt(document.getElementById('tt-rating-val').value)||0;
      var rname=document.getElementById('tt-r-name').value.trim();
      var remail=document.getElementById('tt-r-email').value.trim();
      var rbody=document.getElementById('tt-r-body').value.trim();
      var rjob=document.getElementById('tt-r-jobtype').value.trim();
      var msg=document.getElementById('tt-review-msg');
      if(!rating||!rname||!remail||!rbody){{
        msg.style.display='';msg.style.color='#dc2626';msg.textContent='Please fill in all required fields and select a star rating.';return;
      }}
      fetch(API+'submit_review',{{method:'POST',headers:{{'Content-Type':'application/json','X-Frappe-CSRF-Token':'fetch'}},body:JSON.stringify({{listing_slug:SLUG,reviewer_name:rname,reviewer_email:remail,rating:rating,review_body:rbody,job_type:rjob}})}}
      ).then(function(r){{return r.json();}}).then(function(d){{
        var data=d.message||d;
        if(data.success){{
          msg.style.display='';msg.style.color='#16a34a';msg.textContent='Thanks for your review!';
          document.getElementById('tt-review-form').style.display='none';
          document.getElementById('tt-write-review-btn').style.display='inline-block';
        }} else {{
          msg.style.display='';msg.style.color='#dc2626';msg.textContent=data.error||'Could not submit review.';
        }}
      }}).catch(function(){{msg.style.display='';msg.style.color='#dc2626';msg.textContent='Network error. Please try again.';}});
    }};
  }})();
  </script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("TradieTools — Profile Page Generator")
    print(f"  Dry run: {DRY_RUN}")

    skip = claimed_slugs()
    print(f"  Skipping {len(skip)} hand-crafted claimed profiles")

    print("Fetching listings from API…")
    listings = fetch_all_listings()
    print(f"Total listings fetched: {len(listings)}")

    BIZ_DIR.mkdir(parents=True, exist_ok=True)

    created = skipped = errors = 0
    for listing in listings:
        slug = listing.get("listing_slug") or ""
        if not slug:
            errors += 1
            continue
        if slug in skip:
            skipped += 1
            continue

        out_dir = BIZ_DIR / slug
        try:
            html_content = render_profile(listing)
        except Exception as e:
            print(f"  [ERR] {slug}: {e}")
            errors += 1
            continue

        if DRY_RUN:
            created += 1
            continue

        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(html_content, encoding="utf-8")
        created += 1

    print(f"\nDone: {created} pages created, {skipped} claimed profiles skipped, {errors} errors")
    if not DRY_RUN:
        print(f"Output: {BIZ_DIR}")


if __name__ == "__main__":
    main()
