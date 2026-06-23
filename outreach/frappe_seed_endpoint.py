# ─────────────────────────────────────────────────────────────────────────────
# ADD THIS to /home/ben/frappe-bench/apps/tradietools/tradietools/api.py
# on the server (77.37.87.141), then:
#   supervisorctl restart frappe-bench-web:frappe-bench-frappe-web
# ─────────────────────────────────────────────────────────────────────────────

import frappe, secrets, re
from frappe import _

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")

@frappe.whitelist(allow_guest=True)
def seed_unclaimed_listing(**kwargs):
    """
    Bulk-insert unclaimed listings scraped from NoCowboys.
    Skips any listing whose name+region already exists in the DB.
    Accepts either a single listing dict or a JSON array via 'listings' param.

    Called by outreach/import_seed_listings.py
    """
    import json

    # Accept single record or batch
    raw = kwargs.get("listings")
    if raw:
        try:
            rows = json.loads(raw) if isinstance(raw, str) else raw
        except Exception:
            frappe.throw(_("Invalid JSON in 'listings'"))
    else:
        # Single record passed as kwargs
        rows = [kwargs]

    inserted = 0
    skipped  = 0

    for row in rows:
        name   = (row.get("name") or "").strip()[:100]
        trade  = (row.get("trade") or "").strip()
        region = (row.get("region") or "").strip()

        if not name or not trade or not region:
            skipped += 1
            continue

        # Skip if already exists (by name + region, case-insensitive)
        exists = frappe.db.sql(
            "SELECT name FROM `tabtradie_listings` WHERE LOWER(listing_name)=%s AND LOWER(region)=%s LIMIT 1",
            (name.lower(), region.lower())
        )
        if exists:
            skipped += 1
            continue

        slug = slugify(name)

        # Ensure slug is unique
        base_slug = slug
        counter = 1
        while frappe.db.exists("tradie_listings", {"slug": slug}):
            slug = f"{base_slug}-{counter}"
            counter += 1

        lead_token = secrets.token_urlsafe(32)

        frappe.db.sql("""
            INSERT INTO `tabtradie_listings`
              (name, listing_name, slug, trade, region, phone,
               nocowboys_url, avg_rating, review_count,
               is_active, is_email_verified, is_verified, is_premium,
               lead_token, creation, modified, docstatus, owner, modified_by)
            VALUES
              (%(slug)s, %(listing_name)s, %(slug)s, %(trade)s, %(region)s, %(phone)s,
               %(nocowboys_url)s, %(avg_rating)s, %(review_count)s,
               1, 0, 0, 0,
               %(lead_token)s, NOW(), NOW(), 0, 'Administrator', 'Administrator')
        """, {
            "slug":          slug,
            "listing_name":  name,
            "trade":         trade,
            "region":        region,
            "phone":         (row.get("phone") or "")[:30],
            "nocowboys_url": (row.get("nocowboys_url") or "")[:255],
            "avg_rating":    float(row.get("avg_rating") or 0),
            "review_count":  int(row.get("review_count") or 0),
            "lead_token":    lead_token,
        })
        frappe.db.commit()
        inserted += 1

    return {"inserted": inserted, "skipped": skipped}
