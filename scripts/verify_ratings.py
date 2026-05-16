#!/usr/bin/env python3
"""
Verify business ratings against live NoCowboys and Builderscrack pages.
Updates each JSON file with source_url, verified=True, and corrected ratings.
"""

import json
import pathlib
import re
import time
import sys
import urllib.parse
import urllib.request
import urllib.error
from datetime import date

TOP10_DIR = pathlib.Path('/home/ben/.openclaw/workspace/site/data/top10')
TODAY = date.today().isoformat()

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'en-NZ,en;q=0.9',
}

def fetch(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='ignore'), r.geturl()
    except Exception as e:
        return None, str(e)

def search_nocowboys(name, city, trade_slug):
    """Search NoCowboys for a business and return (url, rating, review_count)."""
    from bs4 import BeautifulSoup

    # Map trade slug to NoCowboys category
    trade_map = {
        'builders': 'builders', 'carpenters': 'carpenters',
        'concreters': 'concrete-contractors', 'drainlayers': 'drain-layers',
        'electricians': 'electricians', 'gasfitters': 'gas-fitters',
        'landscapers': 'landscapers', 'painters': 'painters-painting-contractors',
        'plasterers': 'plasterers', 'plumbers': 'plumbers',
        'roofers': 'roofers', 'tilers': 'tilers-tile-layers',
    }
    nc_trade = trade_map.get(trade_slug, trade_slug)

    # City slug for NoCowboys URL
    city_url = city.replace('-', '%20')

    search_url = f'https://www.nocowboys.co.nz/search/{city_url}/{nc_trade}'
    html, final_url = fetch(search_url)
    if not html:
        return None, None, None

    soup = BeautifulSoup(html, 'html.parser')
    name_lower = name.lower()

    # Look for business cards
    for card in soup.find_all(['div', 'article'], class_=re.compile(r'business|result|tradie|card', re.I)):
        card_text = card.get_text()
        if name_lower in card_text.lower():
            # Try to find a link to the business profile
            link = card.find('a', href=re.compile(r'/business/|/tradie/|/profile/'))
            if link:
                profile_url = 'https://www.nocowboys.co.nz' + link['href'] if link['href'].startswith('/') else link['href']
                # Fetch profile page
                prof_html, _ = fetch(profile_url)
                if prof_html:
                    rating, count = extract_rating_nocowboys(prof_html)
                    if rating:
                        return profile_url, rating, count

    # Try direct name search
    name_slug = name.lower().replace(' ', '-').replace('&', 'and').replace('.', '').replace("'", '')
    direct_url = f'https://www.nocowboys.co.nz/business/{name_slug}'
    html2, final2 = fetch(direct_url)
    if html2 and name_lower in html2.lower():
        rating, count = extract_rating_nocowboys(html2)
        if rating:
            return final2, rating, count

    return None, None, None

def extract_rating_nocowboys(html):
    """Extract rating and review count from a NoCowboys page."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    rating = None
    count = None

    # Look for rating patterns
    for tag in soup.find_all(string=re.compile(r'\b[45]\.\d\b')):
        m = re.search(r'\b([45]\.\d)\b', str(tag))
        if m:
            rating = float(m.group(1))
            break

    # Look for review count
    for tag in soup.find_all(string=re.compile(r'\d+\s*(review|rating)', re.I)):
        m = re.search(r'(\d+)\s*(review|rating)', str(tag), re.I)
        if m:
            count = int(m.group(1))
            break

    return rating, count

def search_builderscrack(name, city, trade_slug):
    """Search Builderscrack for a business."""
    from bs4 import BeautifulSoup

    trade_map = {
        'builders': 'builders', 'carpenters': 'carpenters',
        'concreters': 'concrete-layers', 'drainlayers': 'drainlayers',
        'electricians': 'electricians', 'gasfitters': 'gas-fitters',
        'landscapers': 'landscapers', 'painters': 'painters-and-decorators',
        'plasterers': 'plasterers', 'plumbers': 'plumbers',
        'roofers': 'roofers', 'tilers': 'tilers',
    }
    bc_trade = trade_map.get(trade_slug, trade_slug)

    search_url = f'https://builderscrack.co.nz/trades/{bc_trade}/{city}'
    html, final_url = fetch(search_url)
    if not html:
        return None, None, None

    soup = BeautifulSoup(html, 'html.parser')
    name_lower = name.lower()

    for card in soup.find_all(['div', 'li', 'article']):
        card_text = card.get_text()
        if name_lower in card_text.lower():
            # Try to find rating in the card
            m = re.search(r'(\d\.\d)\s*/?\s*5', card_text)
            if m:
                rating = float(m.group(1))
                # Count reviews
                cm = re.search(r'(\d+)\s*review', card_text, re.I)
                count = int(cm.group(1)) if cm else None
                link = card.find('a', href=re.compile(r'/tradies/'))
                if link:
                    source_url = 'https://builderscrack.co.nz' + link['href'] if link['href'].startswith('/') else link['href']
                else:
                    source_url = search_url
                return source_url, rating, count

    return None, None, None

def verify_business(b, trade_slug, city):
    """Try to verify a single business. Returns (source, source_url, rating, review_count) or None."""

    # Try NoCowboys first
    url, rating, count = search_nocowboys(b['name'], city, trade_slug)
    if url and rating:
        return 'NoCowboys', url, rating, count

    time.sleep(0.5)

    # Try Builderscrack
    url, rating, count = search_builderscrack(b['name'], city, trade_slug)
    if url and rating:
        return 'Builderscrack', url, rating, count

    return None

def process_file(f):
    data = json.loads(f.read_text())
    trade = data['trade']
    city = data['city']
    changed = False
    verified_count = 0
    fail_count = 0
    corrections = []

    for b in data['businesses']:
        if b.get('verified') and b.get('source_url'):
            verified_count += 1
            continue

        result = verify_business(b, trade, city)
        time.sleep(1)  # rate limit

        if result:
            source, url, rating, count = result
            old_rating = b['rating']
            old_count = b['review_count']

            b['source'] = source
            b['source_url'] = url
            b['verified'] = True
            b['verified_date'] = TODAY

            if rating and abs(rating - old_rating) >= 0.2:
                b['rating'] = rating
                corrections.append(f"{b['name']}: rating {old_rating}→{rating}")
                changed = True
            if count and count != old_count:
                b['review_count'] = count
                corrections.append(f"{b['name']}: reviews {old_count}→{count}")
                changed = True

            b['verified'] = True
            changed = True
            verified_count += 1
        else:
            fail_count += 1

    if changed:
        f.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    return verified_count, fail_count, corrections

if __name__ == '__main__':
    # Which files to process — default all, or pass filenames as args
    if len(sys.argv) > 1:
        files = [TOP10_DIR / a for a in sys.argv[1:]]
    else:
        files = sorted(TOP10_DIR.glob('*.json'))
        # painters-napier first
        priority = TOP10_DIR / 'painters-napier.json'
        if priority in files:
            files = [priority] + [f for f in files if f != priority]

    total_v = total_f = 0
    all_corrections = []

    for i, f in enumerate(files):
        print(f'[{i+1}/{len(files)}] {f.stem}...', end=' ', flush=True)
        v, fail, corr = process_file(f)
        total_v += v
        total_f += fail
        all_corrections.extend(corr)
        print(f'verified={v} failed={fail}' + (f' CORRECTIONS: {corr}' if corr else ''))

        # Commit every 20 files
        if (i + 1) % 20 == 0:
            import subprocess
            subprocess.run(['git', 'add', 'data/top10/'], cwd='/home/ben/.openclaw/workspace/site')
            subprocess.run(['git', 'commit', '-m', f'data: verified ratings batch {TODAY} ({i+1} files)'],
                           cwd='/home/ben/.openclaw/workspace/site')

    print(f'\nDone. Verified: {total_v}  Unverifiable: {total_f}')
    if all_corrections:
        print('Rating corrections:')
        for c in all_corrections:
            print(f'  {c}')
