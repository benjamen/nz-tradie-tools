"""
After Wave 2 finishes: backfill listing IDs into contacts_wave2.csv
then upload contacts to outreach_contacts table on server.
Run: python3 outreach/sync_wave2_to_server.py
"""
import sys, csv, subprocess
from pathlib import Path

sys.path.insert(0, '/home/ben/.openclaw/workspace/site/.venv/lib/python3.12/site-packages')

KEY    = '/home/ben/.ssh/tradietools'
SERVER = 'root@77.37.87.141'
DB     = '_0e44d7c556083503'
CSV    = Path(__file__).parent / 'contacts_wave2.csv'

if not CSV.exists():
    print("contacts_wave2.csv not found — Wave 2 may still be running")
    sys.exit(1)

# Step 1: backfill listing IDs via server DB lookup
print("Fetching listing name→id map from server...")
result = subprocess.run(
    ['ssh', '-i', KEY, '-o', 'StrictHostKeyChecking=no', SERVER,
     f"mysql -u root {DB} --batch --skip-column-names -e 'SELECT id, name FROM tradie_listings LIMIT 5000'"],
    capture_output=True, text=True
)
name_to_id = {}
for line in result.stdout.strip().splitlines():
    parts = line.split('\t', 1)
    if len(parts) == 2:
        name_to_id[parts[1].strip()] = parts[0].strip()
print(f"  {len(name_to_id)} listings loaded")

with open(CSV) as f:
    rows = list(csv.DictReader(f))

fieldnames = list(rows[0].keys()) if rows else []
if 'listing_id' not in fieldnames:
    fieldnames = ['listing_id'] + fieldnames

matched = 0
for row in rows:
    lid = name_to_id.get(row.get('name', '').strip(), '')
    row['listing_id'] = lid
    if lid:
        matched += 1

with open(CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
print(f"  Backfilled {matched}/{len(rows)} listing IDs into contacts_wave2.csv")

# Step 2: insert sent contacts into outreach_contacts
sent = [r for r in rows if r.get('status') == 'sent' and r.get('email')]
print(f"\nInserting {len(sent)} Wave 2 contacts into server outreach_contacts...")

vals = []
for r in sent:
    lid    = r.get('listing_id', '').strip() or 'NULL'
    name   = r.get('name', '').replace("'", "\\'")[:299]
    email  = r.get('email', '').replace("'", "\\'")[:199]
    trade  = r.get('trade', '').replace("'", "\\'")[:99]
    region = r.get('region', '').replace("'", "\\'")[:99]
    vals.append(f"({lid if lid != 'NULL' else 'NULL'},'{name}','{email}','{trade}','{region}',2)")

if vals:
    sql = f"INSERT IGNORE INTO outreach_contacts (listing_id,biz_name,email,trade,region,wave) VALUES {','.join(vals)};"
    result = subprocess.run(
        ['ssh', '-i', KEY, '-o', 'StrictHostKeyChecking=no', SERVER,
         f"mysql -u root {DB} -e \"{sql}\""],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("ERROR:", result.stderr[:200])
        sys.exit(1)

result = subprocess.run(
    ['ssh', '-i', KEY, '-o', 'StrictHostKeyChecking=no', SERVER,
     f"mysql -u root {DB} --batch --skip-column-names -e 'SELECT wave, COUNT(*) FROM outreach_contacts GROUP BY wave'"],
    capture_output=True, text=True
)
print("outreach_contacts by wave:")
for line in result.stdout.strip().splitlines():
    print(f"  Wave {line}")
print("Done.")
