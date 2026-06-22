"""
TradieTools cold outreach — contact scraper
Pulls tradie business names + websites from Finda.co.nz and Yellow Pages NZ,
then extracts emails from their websites.
Outputs: outreach/contacts.csv
"""

import requests
import re
import csv
import time
import random
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin, urlparse

OUTPUT = Path(__file__).parent / "contacts.csv"
LOG = Path(__file__).parent / "scrape.log"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-NZ,en;q=0.9",
}

# Trades × Cities to scrape
TARGETS = [
    ("electrician", "Auckland"),
    ("electrician", "Wellington"),
    ("electrician", "Christchurch"),
    ("plumber", "Auckland"),
    ("plumber", "Wellington"),
    ("plumber", "Christchurch"),
    ("builder", "Auckland"),
    ("builder", "Wellington"),
    ("builder", "Christchurch"),
    ("electrician", "Hamilton"),
    ("plumber", "Hamilton"),
    ("electrician", "Tauranga"),
    ("plumber", "Tauranga"),
]

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
SKIP_DOMAINS = {
    "example.com", "sentry.io", "wix.com", "google.com", "facebook.com",
    "tradietools.nz", "nocowboys.co.nz", "builderscrack.co.nz",
    "noemail", "png", "jpg", "jpeg", "gif", "svg",
}


def log(msg):
    print(msg)
    with open(LOG, "a") as f:
        f.write(msg + "\n")


def get(url, timeout=10):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        return r
    except Exception as e:
        log(f"  GET failed {url}: {e}")
        return None


def find_emails_in_html(html, base_domain=""):
    emails = set()
    for match in EMAIL_RE.findall(html):
        m = match.lower()
        domain = m.split("@")[1] if "@" in m else ""
        if any(s in domain for s in SKIP_DOMAINS):
            continue
        if base_domain and domain == base_domain:
            emails.add(m)
        elif not base_domain:
            emails.add(m)
    return emails


def extract_email_from_website(website_url):
    """Visit homepage and /contact page to find a contact email."""
    if not website_url or not website_url.startswith("http"):
        return None
    base_domain = urlparse(website_url).netloc.replace("www.", "")

    pages_to_try = [website_url, urljoin(website_url, "/contact"), urljoin(website_url, "/contact-us")]
    for url in pages_to_try:
        r = get(url, timeout=8)
        if not r:
            continue
        emails = find_emails_in_html(r.text, base_domain)
        # Also check mailto: links
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("mailto:"):
                email = href[7:].split("?")[0].strip().lower()
                if email and not any(s in email for s in SKIP_DOMAINS):
                    emails.add(email)
        if emails:
            return sorted(emails)[0]
        time.sleep(0.5)
    return None


def scrape_finda(trade, city, max_pages=3):
    """Scrape finda.co.nz for a trade+city combo."""
    results = []
    base = f"https://www.finda.co.nz/search/{trade}/{city.lower()}"
    for page in range(1, max_pages + 1):
        url = base if page == 1 else f"{base}?page={page}"
        log(f"  Finda: {url}")
        r = get(url)
        if not r:
            break
        soup = BeautifulSoup(r.text, "html.parser")

        # Business cards
        cards = soup.select("div.listing-card, article.listing, div[class*='business']")
        if not cards:
            # Try generic name + website extraction
            cards = soup.select("li.result, div.result")

        for card in cards:
            name_el = card.select_one("h2, h3, .listing-name, .business-name, a.name")
            name = name_el.get_text(strip=True) if name_el else ""
            if not name:
                continue

            website = None
            web_el = card.select_one("a[href*='http']:not([href*='finda'])")
            if web_el:
                website = web_el["href"]

            phone = None
            phone_el = card.select_one(".phone, [class*='phone'], [itemprop='telephone']")
            if phone_el:
                phone = phone_el.get_text(strip=True)

            if name:
                results.append({
                    "name": name,
                    "trade": trade,
                    "city": city,
                    "website": website,
                    "phone": phone,
                    "email": None,
                    "source": "finda",
                })

        if not cards:
            break
        time.sleep(random.uniform(2, 4))
    return results


def scrape_yellow(trade, city, max_pages=3):
    """Scrape yellow.co.nz for a trade+city combo."""
    results = []
    slug = trade.replace(" ", "+")
    city_slug = city.lower().replace(" ", "+")
    for page in range(1, max_pages + 1):
        url = (
            f"https://www.yellow.co.nz/search/{slug}/{city_slug}"
            if page == 1
            else f"https://www.yellow.co.nz/search/{slug}/{city_slug}?page={page}"
        )
        log(f"  Yellow: {url}")
        r = get(url)
        if not r:
            break
        soup = BeautifulSoup(r.text, "html.parser")

        cards = soup.select("div.listing, article, li.search-result, div[class*='result']")
        for card in cards:
            name_el = card.select_one("h2, h3, .name, a[class*='name']")
            name = name_el.get_text(strip=True) if name_el else ""
            if not name or len(name) < 3:
                continue

            website = None
            for a in card.select("a[href]"):
                href = a["href"]
                if href.startswith("http") and "yellow.co.nz" not in href:
                    website = href
                    break

            phone = None
            phone_el = card.select_one("[class*='phone'], [itemprop='telephone']")
            if phone_el:
                phone = phone_el.get_text(strip=True)

            results.append({
                "name": name,
                "trade": trade,
                "city": city,
                "website": website,
                "phone": phone,
                "email": None,
                "source": "yellow",
            })

        if not cards:
            break
        time.sleep(random.uniform(2, 4))
    return results


def main():
    log("=== TradieTools contact scraper ===")
    all_contacts = []
    seen_names = set()

    for trade, city in TARGETS:
        log(f"\n[{trade} / {city}]")

        for scraper in [scrape_finda, scrape_yellow]:
            contacts = scraper(trade, city)
            log(f"  Found {len(contacts)} listings")
            for c in contacts:
                key = c["name"].lower().strip()
                if key not in seen_names:
                    seen_names.add(key)
                    all_contacts.append(c)
            time.sleep(random.uniform(1, 3))

    log(f"\nTotal unique contacts before email enrichment: {len(all_contacts)}")

    # Email enrichment — visit websites
    log("\n=== Email enrichment ===")
    enriched = 0
    for i, c in enumerate(all_contacts):
        if c.get("website"):
            log(f"  [{i+1}/{len(all_contacts)}] {c['name']} → {c['website']}")
            email = extract_email_from_website(c["website"])
            if email:
                c["email"] = email
                enriched += 1
                log(f"    ✓ {email}")
            time.sleep(random.uniform(1.5, 3))

    log(f"\nEmails found: {enriched}/{len(all_contacts)}")

    # Write CSV
    OUTPUT.parent.mkdir(exist_ok=True)
    with open(OUTPUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "trade", "city", "email", "phone", "website", "source"])
        w.writeheader()
        w.writerows(all_contacts)

    log(f"\nSaved to {OUTPUT}")
    log(f"Contacts with email: {enriched}")
    log(f"Contacts with phone only: {sum(1 for c in all_contacts if c.get('phone') and not c.get('email'))}")


if __name__ == "__main__":
    main()
