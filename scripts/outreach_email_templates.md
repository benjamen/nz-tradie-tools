# TradieTools Outreach Email Templates

## Template 1: Missed Lead (Primary Cold Outreach)

**Subject:** A homeowner in [City] searched for a [Trade] last week

**To:** [tradie name / business name] — sourced from existing listing or cold list

---

Hi [First Name],

Someone in [City] searched for a [Trade] on TradieTools last week.

We didn't have a verified [trade] in your area to send them to, so they probably ended up on a Google search — or a competitor's listing.

If you're covering [City], a verified listing means that next time someone searches, they find you.

It takes about 5 minutes to set up. First 14 days free, then $29/month — less than one job.

[Claim your spot in [City] →](https://tradietools.nz/signup/?trade=[trade_slug]&city=[city_slug])

— Ben @ TradieTools NZ

P.S. Not ready to commit? You can try a single lead credit for $20 instead — no monthly fee, just pay when a lead comes in.

---

## Template 2: Existing Free Listing (Upgrade Nudge)

**Subject:** Your listing is live — here's what you're missing

**To:** Tradies who signed up but didn't upgrade

---

Hi [First Name],

Your free listing on TradieTools is live at:
tradietools.nz/businesses/[your-slug]/

Quick update on what's happening with your trade in [City]:

- [N] homeowners searched for [trade] in your area this month
- Verified listings are showing above yours in results
- Your listing is visible but not priority-ranked yet

Upgrading to Verified ($29/mo) moves you to the top and adds your verification badge — the thing homeowners use to shortlist who to call first.

[Upgrade your listing →](https://tradietools.nz/dashboard/?token=[lead_token])

Or if you'd rather try before you commit, a lead credit ($20) lets you receive one qualified lead with no subscription.

[See how credits work →](https://tradietools.nz/tier-compare/#credits)

— Ben @ TradieTools NZ

---

## Template 3: Warm Follow-Up (Day 14 after free signup)

**Subject:** Two weeks in — any leads come through?

**To:** Free-tier tradies, 14 days after signup

---

Hi [First Name],

It's been two weeks since you listed on TradieTools. Checking in.

Free listings get visibility — but homeowners searching for [trade] in [city] are most likely clicking the verified listings first. That's the ones with the blue badge and priority placement.

If you've had leads come through, great. If not, the upgrade is $29/month — and the first lead that comes in usually covers it.

[Upgrade to Verified →](https://tradietools.nz/dashboard/?token=[lead_token])

Not ready to commit monthly? Try one lead credit for $20. You pay, we send you the next qualified homeowner who searches for [trade] in your area.

[Buy a lead credit →](https://tradietools.nz/tier-compare/#credits)

— Ben

---

## Template 4: Re-engagement (Lapsed / no activity)

**Subject:** Still taking work in [City]?

**To:** Free listings with no dashboard activity in 30+ days

---

Hi [First Name],

Quick question — are you still taking [trade] work in [City]?

Your listing is still live but we haven't seen any activity on it for a while. If you want us to keep sending homeowners your way, it's worth updating your availability.

[Update your listing →](https://tradietools.nz/dashboard/?token=[lead_token])

If things have slowed down or you've taken on a big job and aren't available, you can turn off your listing temporarily — just toggle "Taking work" off from the dashboard.

— Ben

---

## Notes on Personalisation

- `[City]` = their listed region (e.g. Auckland, Christchurch, Whangārei)
- `[Trade]` = their trade in plain English (e.g. Plumber, Electrician, Arborist)
- `[trade_slug]` = URL slug (e.g. plumbers, electricians, tree-services)
- `[lead_token]` = their unique dashboard token from `tradie_listings.lead_token`
- `[your-slug]` = their `listing_slug` from the database
- Send from: ben@tradietools.nz or noreply@tradietools.nz with reply-to ben@

## Sending Schedule

| Template | Trigger | Channel |
|----------|---------|---------|
| Template 1 | Cold outreach (new city/trade gaps) | Manual batch or Zapier |
| Template 2 | 3 days after free signup, no upgrade | Frappe automation or manual |
| Template 3 | Day 14 after free signup | Frappe automation |
| Template 4 | 30+ days no dashboard login | Frappe automation |
