"""
Pull all verified+active listings from DB and write data/claimed/*.json,
then run build.py to regenerate /businesses/ profile pages.

Run from site root:  python3 outreach/sync_profiles.py
"""
import subprocess, json, re, sys
from pathlib import Path
from datetime import datetime

KEY    = '/home/ben/.ssh/tradietools'
SERVER = 'root@77.37.87.141'
DB     = '_0e44d7c556083503'
SITE   = Path(__file__).parent.parent
CLAIMED = SITE / 'data' / 'claimed'

# DB trade value → trades.json slug + display name
TRADE_MAP = {
    'builders':             ('builders',           'Builders & LBPs'),
    'builder':              ('builders',           'Builders & LBPs'),
    'plumbers':             ('plumbers',           'Plumbers & Gasfitters'),
    'plumber':              ('plumbers',           'Plumbers & Gasfitters'),
    'electricians':         ('electricians',       'Electricians'),
    'electrician':          ('electricians',       'Electricians'),
    'painters':             ('painters',           'Painters & Decorators'),
    'painter':              ('painters',           'Painters & Decorators'),
    'roofers':              ('roofers',            'Roofers & Roof Tilers'),
    'roofer':               ('roofers',            'Roofers & Roof Tilers'),
    'landscapers':          ('landscapers',        'Landscapers & Garden Designers'),
    'tilers':               ('tilers',             'Tilers'),
    'plasterers':           ('plasterers',         'Plasterers'),
    'carpet-layers':        ('carpet-layers',      'Carpet Layers & Flooring Specialists'),
    'carpet':               ('carpet-layers',      'Carpet Layers & Flooring Specialists'),
    'concreters':           ('concreters',         'Concreters'),
    'carpenters':           ('carpenters',         'Carpenters & Joiners'),
    'carpenter':            ('carpenters',         'Carpenters & Joiners'),
    'gasfitters':           ('gasfitters',         'Gasfitters'),
    'drainlayers':          ('drainlayers',        'Drainlayers'),
    'glaziers':             ('glaziers',           'Glaziers & Glass Specialists'),
    'fencers':              ('fencers',            'Fencers'),
    'waterproofers':        ('waterproofers',      'Waterproofers'),
    'insulation-installers':('insulation-installers','Insulation Installers'),
    'heat-pump-installers': ('heat-pump-installers','Heat Pump Installers'),
    'solar-installers':     ('solar-installers',   'Solar Panel Installers'),
    'scaffolders':          ('scaffolders',        'Scaffolders'),
}

# DB region → city slug + display
REGION_MAP = {
    'Auckland':        ('auckland',     'Auckland'),
    'Wellington':      ('wellington',   'Wellington'),
    'Christchurch':    ('christchurch', 'Christchurch'),
    'Hamilton':        ('hamilton',     'Hamilton'),
    'Tauranga':        ('tauranga',     'Tauranga'),
    'Dunedin':         ('dunedin',      'Dunedin'),
    'Palmerston North':('palmerston-north','Palmerston North'),
    'Nelson':          ('nelson',       'Nelson'),
    'Rotorua':         ('rotorua',      'Rotorua'),
    'Napier':          ('napier',       'Napier'),
    'Whangarei':       ('whangarei',    'Whangārei'),
    'New Plymouth':    ('new-plymouth', 'New Plymouth'),
    'Invercargill':    ('invercargill', 'Invercargill'),
    'Queenstown':      ('queenstown',   'Queenstown'),
    'Lower Hutt':      ('lower-hutt',   'Lower Hutt'),
    'Upper Hutt':      ('upper-hutt',   'Upper Hutt'),
    'Porirua':         ('porirua',      'Porirua'),
    'Kapiti':          ('kapiti',       'Kāpiti'),
    'Hastings':        ('hastings',     'Hastings'),
    'Whanganui':       ('whanganui',    'Whanganui'),
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-')


def pull_verified():
    sql = (
        "SELECT id, name, trade, region, phone, contact_email, hourly_rate, "
        "experience_years, avg_rating, review_count, google_url, nocowboys_url "
        "FROM tradie_listings "
        "WHERE is_email_verified=1 AND is_active=1"
    )
    r = subprocess.run(
        ['ssh', '-i', KEY, '-o', 'StrictHostKeyChecking=no', SERVER,
         f"mysql -u root {DB} --batch --skip-column-names -e \"{sql}\""],
        capture_output=True, text=True
    )
    rows = []
    for line in r.stdout.strip().splitlines():
        parts = line.split('\t')
        if len(parts) >= 12:
            rows.append({
                'id':           parts[0],
                'name':         parts[1],
                'trade':        parts[2],
                'region':       parts[3],
                'phone':        parts[4] if parts[4] != 'NULL' else '',
                'email':        parts[5] if parts[5] != 'NULL' else '',
                'hourly_rate':  parts[6] if parts[6] not in ('NULL','0') else '',
                'experience':   parts[7] if parts[7] not in ('NULL','0') else '',
                'rating':       parts[8] if parts[8] != 'NULL' else '0',
                'reviews':      parts[9] if parts[9] != 'NULL' else '0',
                'google_url':   parts[10] if parts[10] != 'NULL' else '',
                'website':      parts[11] if parts[11] != 'NULL' else '',
            })
    return rows


def make_profile(row):
    trade_slug, trade_name = TRADE_MAP.get(row['trade'], (row['trade'], row['trade'].title()))
    city_slug, city_name   = REGION_MAP.get(row['region'], (slugify(row['region']), row['region']))

    biz_slug = slugify(row['name'])
    rating   = float(row['rating'] or 0)
    reviews  = int(row['reviews'] or 0)

    trade_display = trade_name.split(' &')[0].rstrip('s').lower()  # "Builders & LBPs" → "builder"
    tagline = f"{city_name} {trade_display} with {row['experience']} years experience" \
        if row['experience'] else f"{city_name} {trade_display}"

    services = []
    if row['hourly_rate']:
        services.append(f"Hourly rate: ${row['hourly_rate']}/hr")

    return {
        "slug":             biz_slug,
        "business_name":    row['name'],
        "trade":            trade_slug,
        "trade_name":       trade_name,
        "city":             city_slug,
        "city_name":        city_name,
        "claimed":          True,
        "claimed_date":     datetime.now().strftime('%Y-%m-%d'),
        "verified":         True,
        "tagline":          tagline,
        "description":      f"{row['name']} is a verified {trade_display} based in {city_name}, New Zealand.",
        "phone":            row['phone'],
        "email":            "",
        "website":          row['website'],
        "suburb":           "",
        "rating":           rating,
        "review_count":     reviews,
        "source":           "Google" if row['google_url'] else "TradieTools",
        "source_url":       row['google_url'],
        "known_for":        f"{row['name']} — verified {trade_display} in {city_name}.",
        "services":         services,
        "areas_served":     [city_name],
        "licensed":         False,
        "lbp":              False,
        "insured":          False,
        "years_in_business": int(row['experience']) if row['experience'] else None,
        "lbp_number":       "",
        "ewrb":             False,
        "ewrb_number":      "",
        "pgd":              False,
        "pgd_number":       "",
    }


def main():
    CLAIMED.mkdir(exist_ok=True)
    rows = pull_verified()
    print(f"Found {len(rows)} verified listings")

    written = 0
    for row in rows:
        # skip test/placeholder entries
        if 'noemail' in row['email'].lower() or not row['name']:
            continue
        profile = make_profile(row)
        slug = profile['slug']
        out = CLAIMED / f"{slug}.json"
        # don't overwrite manually curated entries unless forced
        if out.exists():
            existing = json.loads(out.read_text())
            if existing.get('manually_curated'):
                print(f"  skip (manual): {slug}")
                continue
        out.write_text(json.dumps(profile, indent=2, ensure_ascii=False))
        print(f"  wrote: {slug}.json")
        written += 1

    print(f"\nWrote {written} profile JSON files")

    if written > 0:
        print("\nRebuilding site...")
        r = subprocess.run(
            [str(SITE / '.venv/bin/python'), str(SITE / 'build.py')],
            cwd=str(SITE), capture_output=True, text=True
        )
        print(r.stdout[-800:] if r.stdout else '')
        if r.returncode != 0:
            print("BUILD ERROR:", r.stderr[-400:])
        else:
            print("Build complete.")


if __name__ == '__main__':
    main()
