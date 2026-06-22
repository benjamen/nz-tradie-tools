# TradieTools — Product Strategy & Value Maximisation Roadmap
*Full feature review, competitive benchmark, and prioritised roadmap to become NZ's #1 tradie platform.*
*Produced: June 2026*

---

## SECTION 1: FEATURE AUDIT

Rating scale: **Excellent** | **Good** | **Needs Work** | **Missing**

### Visitor-Facing Features

| Feature | Rating | Notes |
|---|---|---|
| /find/ live search (trade + city filters) | **Needs Work** | Only 2 filters. No rating threshold, no budget range, no suburb, no availability. 5 results/page is too few. No map view. |
| /trades/{trade}/{city} top-10 pages | **Good** | 940 pages, good SEO coverage. But static — listings don't reflect real-time ranking or claim status. |
| /get-quotes/ lead capture | **Needs Work** | Anonymous only — homeowner has zero visibility on who got their request, whether anyone responded, or their lead status. One-way black box. |
| /jobs/{job}/{city} cost estimators | **Good** | Solid NZ-specific data. Lacks real-time input from actual tradie rates or reviews. |
| 60+ calculators | **Good** | Strong breadth. Some missing (waterblasting, insulation, double glazing). No embeds in articles. |
| 169 articles (cost guides) | **Needs Work** | Only 3 live out of 169 built. Wave 2 not deployed. Major missed SEO opportunity. |
| PDF templates (invoice, quote) | **Good** | Useful utility. Not connected to tradie profiles — should be downloadable from profile pages too. |
| /tradie-rates/ hourly rate matrix | **Excellent** | Strong differentiator. Data-rich, NZ-specific, covers 47 trades × 20 cities. Needs internal linking. |
| /glossary/ (200+ terms) | **Good** | Solid reference. Underlinked from articles. No schema markup (DefinedTerm). |
| /businesses/{slug}/ profiles | **Needs Work** | No photos. No reviews visible. No licence badge. No availability. Thin and untrustworthy to homeowners. |
| Review display on tradie profiles | **Missing** | DB table exists. Zero UI. Homeowners cannot see or submit reviews anywhere on site. |
| Portfolio / photo gallery | **Missing** | Not implemented. A builder with no photos is invisible to serious homeowners. |
| Licence/insurance badges | **Missing** | Verification_requests table exists. No front-end flow, no badge display. Tradies have no way to prove legitimacy. |
| Saved tradies / favourites | **Missing** | No homeowner accounts. Can't save a tradie for later. |
| Job history for homeowners | **Missing** | No accounts means no history. Homeowners repeat full search on every visit. |
| Homeowner accounts | **Missing** | Entirely anonymous. No login, no profile, no retention. |
| Availability / booking signals | **Missing** | No way for a tradie to signal "taking work" or show busy periods. |
| Response time indicators | **Missing** | No data collected. Homeowners can't tell if a tradie is fast or slow to respond. |
| Dispute resolution | **Missing** | Nothing. If a job goes wrong, TradieTools offers no path. |
| Referral / affiliate program | **Missing** | No mechanism to reward word-of-mouth. |

### Tradie-Facing Features

| Feature | Rating | Notes |
|---|---|---|
| Free listing creation | **Good** | Email verification works. Simple form. Needs more fields (photos, specialities, licence number). |
| Verified badge ($29/mo) | **Needs Work** | Badge means email-verified, nothing more. Homeowners don't know this. The word "verified" implies licence checking — which we don't do. Creates false trust. |
| Pro badge ($59/mo) | **Needs Work** | Same problem as Verified. Lead matching is passive (silent email blast, no acknowledgement). |
| Quote builder (3/mo free, $9.99 unlimited) | **Good** | Solid tool. Well-built with GST, labour/materials breakdown. Disconnected from listing profile — should integrate. |
| Analytics dashboard (views/clicks/rank) | **Good** | Meaningful metrics. Only 30-day window. No trend lines, no benchmarking vs competitors. |
| Ranking system (weekly cron) | **Needs Work** | Formula is (rating×0.5) + (profile_complete×0.25) + (review_count×0.25) but there's no UI for reviews — so rank is based on a metric tradies can't improve. |
| Email lead notifications | **Needs Work** | Silent blast to top-3. No tradie inbox. No "accept/decline lead." No follow-up reminder if no response. |
| Profile management | **Needs Work** | No photo upload. No speciality sub-tags. No availability toggle. No CRM fields. |
| Invoice/proposal tools | **Missing** | Quote builder exists but no invoice generation, no job tracking, no "mark as won/lost." |
| Automated review requests | **Missing** | No trigger to ask homeowner for review post-job. The reviews table can never be populated without this. |
| Profile completeness coaching | **Missing** | No score, no guidance on what to add to rank higher or convert better. |
| Lead inbox / lead history | **Missing** | Tradies receive email blasts but have no dashboard view of leads received, accepted, or won. |
| CRM / customer management | **Missing** | No way to track returning customers or job pipeline. |
| Calendar / availability | **Missing** | No booking or availability signal of any kind. |
| ROI / earnings tracker | **Missing** | Tradies can't see what TradieTools is worth to them in dollar terms. |
| Competitor benchmarking | **Missing** | Tradies don't know where they rank vs others in their trade/city. |
| Business tips content | **Missing** | No hub for tradie education (pricing, tax, compliance, winning jobs). |

---

## SECTION 2: COMPETITIVE BENCHMARK

### Platform Comparison

#### Builderscrack (builderscrack.co.nz) — THE DOMINANT NZ PLAYER
**Scale:** 908,000+ jobs, 346,000+ homeowners, 16,543 tradies, 332,138 verified reviews (2026).
**Pricing:** Three subscription tiers (Basic/Standard/Business). Token/credit system for lead connections. Moved from pure success-fee to predictable subscription in 2025.
**What they do that we don't:**
- Massive review corpus (332k reviews vs our 0 visible). This is their #1 moat.
- Two-way messaging between homeowner and tradie (tradies can write proposals, homeowners choose)
- Homeowner accounts with job history and saved quotes
- Tradie verification with trade licence integration
- Job posting by homeowners (homeowner posts job, tradies bid — not just quote routing)
- Portfolio photos on every profile
- Response time metrics visible on profiles
- Mobile-optimised job posting and quote management
**Differentiation:** Network effect + reviews + two-way communication. Hard to displace directly.
**Our gap vs them:** Reviews, messaging, homeowner accounts, portfolio photos. Everything trust-related.

#### No Cowboys (nocowboys.co.nz) — NZ'S REVIEW PLATFORM
**Scale:** Well-established, NZ's best-known tradie review platform.
**Pricing:** $999/year flat fee for tradies (≈$83/month). No commission. Google integration for review syndication.
**What they do that we don't:**
- Google-synced reviews (reviews appear in Google Business Profile)
- Strong brand recognition for trust ("No Cowboys" is memorable and NZ-resonant)
- Tradie profile claim and management
**Differentiation:** Trust-first brand, review focus, Google integration.
**Our gap vs them:** Review credibility and Google integration.
**Where we beat them:** No Cowboys is review-only. We have cost guides, calculators, job estimators, SEO content, lead routing. We're a resource hub; they're a review board.

#### Hipages (hipages.com.au) — AU-FOCUSED, MINIMAL NZ PRESENCE
**Scale:** Large AU platform. NZ presence is minimal.
**Pricing:** Pay-per-lead (credits). Expensive — tradies report $30-$80/lead with low win rates.
**What they do that we don't:**
- Large job volume in AU
- Profile verification
- Instant booking for some jobs
**Differentiation:** AU volume play.
**Our advantage:** We ARE NZ-first. NZ tradies hate pay-per-lead for low-quality AU leads.

#### Oneflare (oneflare.com.au) — CLOSING 30 JUNE 2026
Oneflare is closing entirely in June 2026 and merging into Airtasker. **This is an opportunity** — tradies on Oneflare need an alternative. Any NZ tradies using it are now actively looking.

#### ServiceSeeking (serviceseeking.com.au) — AU ONLY
Not meaningfully active in NZ. Pay-per-lead model. Known for low lead quality.

---

### Competitive Position Matrix

| Capability | Builderscrack | No Cowboys | Hipages | TradieTools |
|---|---|---|---|---|
| Review volume | ★★★★★ | ★★★★ | ★★★ | ★☆☆☆☆ |
| Two-way messaging | ★★★★★ | ★★ | ★★★ | ★☆☆☆☆ |
| Cost guides/calculators | ★★★ | ★ | ★★ | **★★★★★** |
| SEO content depth | ★★★ | ★★ | ★★ | **★★★★★** |
| Tradie licence verification | ★★★★ | ★★★ | ★★ | ★★☆☆☆ |
| Homeowner accounts | ★★★★ | ★★★ | ★★★★ | ★☆☆☆☆ |
| NZ-specific focus | ★★★★★ | ★★★★★ | ★★ | **★★★★★** |
| Pricing for tradies | ★★★ | ★★ | ★☆☆☆☆ | **★★★★★** |
| Portfolio photos | ★★★★ | ★★★ | ★★★ | ★☆☆☆☆ |
| Job costing tools | ★★★ | ★ | ★★ | **★★★★★** |

### Where TradieTools Can Win
1. **Content depth** — our cost guides, calculators, rate matrix, and glossary are already better than anyone else. Double down.
2. **Price** — $29/mo Verified is 3× cheaper than No Cowboys ($83/mo). Make that obvious.
3. **Verified = actually verified** — if we build real licence checking, our "Verified" badge will mean more than Builderscrack's or No Cowboys'.
4. **Tradie tools** — Builderscrack is a directory. We can be a directory + admin platform (quotes, invoices, CRM). Give tradies reasons to log in every day.
5. **Transparency** — be the platform that tells homeowners who got their quote request and when tradies responded. Builderscrack doesn't do this well enough.

### The #1 Competitive Reason to Choose TradieTools Today
Honest answer: there isn't one compelling enough yet. The pricing is better than No Cowboys and the content is better than everyone — but reviews are zero visible and trust signals are weak.

**What we need to build to make it obvious:** A working review system + licence verification badges + homeowner visibility on lead status. Once a homeowner can see 15 real reviews, a verified LBP badge, and know that their quote went to 3 real tradies who responded — TradieTools is the most trustworthy option in NZ.

---

## SECTION 3: VISITOR VALUE — WHAT WILL MAKE THEM COME BACK

### A. Find the Right Tradie Faster

**1. Expanded search filters**
- Problem: Homeowners can only filter by trade + city. They can't narrow by rating, response speed, budget, or suburb.
- What it looks like: Add filter sidebar on /find/ — min star rating, max hourly rate, "taking work now" toggle, suburb (text input, fuzzy matched to listings), job size (small/medium/large), verified-only toggle.
- Effort: **Medium** (FastAPI query updates + Vue3 filter components)
- Impact: High retention — homeowners who find the right tradie in one visit come back. Homeowners who scroll through irrelevant results don't.

**2. Suburb-level location search**
- Problem: "Auckland" has 1.7m people. A homeowner in Remuera doesn't want a tradie in Henderson 45km away.
- What it looks like: Add suburb field to listings. Search auto-completes suburb from a NZ suburb database. Show driving distance estimate.
- Effort: **Medium** (add suburb field to tradie_listings, suburb autocomplete JS, distance sorting)
- Impact: High — suburb precision is the #1 request from NZ homeowners on any directory.

**3. Response time indicator on profiles and search results**
- Problem: Homeowners can't tell if a tradie replies in 20 minutes or 5 days.
- What it looks like: "Typically responds within X hours" badge on profile cards and in search results. Calculated from lead notification timestamps vs tradie response emails.
- Effort: **Medium** (track response times in lead routing, display in card)
- Impact: High — fast responders get chosen 3× more often. Tradies are incentivised to respond quickly.

**4. "Taking work" availability toggle**
- Problem: Homeowners contact tradies who are booked for 3 months.
- What it looks like: Tradie sets status in dashboard: "Available now" / "Busy — available [date]" / "Not taking work". Visible in search results as a green/amber/red dot. Optional calendar to block out busy weeks.
- Effort: **Low** (boolean field in tradie_listings + display in search card)
- Impact: High — reduces homeowner frustration, improves lead quality for tradies.

**5. Speciality sub-tags**
- Problem: "Builder" covers everything from decks to heritage homes to commercial fit-outs.
- What it looks like: Each trade has a set of sub-specialities (e.g., Builder → Decks, Renovations, New Builds, Heritage, Commercial, High-Rise). Tradies tick their specialities. Homeowners can filter.
- Effort: **Medium** (new field type in listings DocType, filter UI)
- Impact: Medium — improves match quality and reduces wasted contacts.

**6. Smart match suggestions on quote request**
- Problem: When a homeowner submits a quote request, they get a black-box confirmation email. They have no idea who matched or why.
- What it looks like: After submission, show "Your request was matched to these 3 tradies: [photo] [name] [rating] [response time]." Link to each profile. Include "Add another tradie" option if homeowner wants more quotes.
- Effort: **Medium** (update quote routing response UI, pass matched tradie data to confirmation page)
- Impact: Very High — transforms a black box into a trust-building moment.

---

### B. Build Trust Before Contact

**7. Review system — submit and display**
- Problem: Reviews exist in DB but zero UI. No homeowner can submit a review or read one.
- What it looks like: On each tradie profile, display star rating + reviews (paginated). "Leave a review" button (gated to homeowners who submitted a quote for that tradie, OR email-verified open submission with admin moderation). Review cards show: star rating, date, job type, "verified lead" badge if homeowner used quote routing.
- Effort: **Medium** (Frappe review workflow, profile review component in Vue3 or Jinja2)
- Impact: Critical. Without visible reviews TradieTools cannot compete with Builderscrack or No Cowboys.

**8. Portfolio photo gallery**
- Problem: A builder with no photos is invisible to homeowners comparing options.
- What it looks like: Tradie uploads up to 20 photos via dashboard (photo, job type tag, short caption). Gallery displays on profile page in masonry grid. Cover photo appears in search result cards.
- Effort: **Medium** (file upload to S3/object storage, gallery template, profile card update)
- Impact: Very High — photo galleries increase profile click-through rates by 60%+ on competitor platforms.

**9. Licence verification badges**
- Problem: "Verified" currently means "email verified" but sounds like "licence checked."
- What it looks like: Specific badges per trade: "LBP Registered" (Licensed Building Practitioner), "EWRB Registered" (electricians), "PGD Licensed" (plumbers/gasfitters). Badge shows on profile and search cards. Clicking the badge explains what it means and when it was last verified.
- Effort: **High** (MBIE/EWRB/PGD API integration or manual upload + admin review workflow)
- Impact: Very High — this is the most powerful trust signal in NZ trades.

**10. Job completion rate / responsiveness score**
- Problem: Homeowners can't distinguish active tradies from ones who signed up and disappeared.
- What it looks like: Track: how many leads sent to tradie, how many responded (any response), how many homeowners left a review. Show on profile: "Responds to X% of leads" and "Active on TradieTools" if logged in within 30 days.
- Effort: **Medium** (tracking in lead routing + display)
- Impact: Medium — differentiates engaged tradies from ghosts.

**11. "What this badge means" education layer**
- Problem: Homeowners don't know what "Verified" vs "Pro" means on TradieTools.
- What it looks like: Small info icon next to every badge. Click reveals tooltip: "This tradie has uploaded proof of [X] licence and it was verified by TradieTools in [month/year]." Also a /trust page explaining our verification process.
- Effort: **Low** (tooltip component + /trust page content)
- Impact: Medium — removes confusion, increases trust in the badge system.

---

### C. Reduce Risk

**12. Dispute / feedback pathway**
- Problem: If a job goes wrong, TradieTools offers homeowners nothing. This is a liability.
- What it looks like: /help/dispute page with: (1) Try to resolve directly with tradie first — here's how. (2) Submit a formal complaint to TradieTools — we will investigate and may remove the listing. (3) External escalation: Consumer NZ, Disputes Tribunal, trade-specific regulators. Not a legal guarantee — a clear escalation path.
- Effort: **Low** (static page + contact form → admin email)
- Impact: High — even a credible-looking dispute process increases platform trust enormously.

**13. Homeowner checklist on profile pages**
- Problem: Homeowners don't know what to ask before hiring.
- What it looks like: Collapsible section on every tradie profile: "Before you hire [name], ask: ✓ Are you licensed for this work? ✓ Do you have public liability insurance? ✓ Can you provide a written quote? ✓ What's your payment schedule?" Links to relevant guides.
- Effort: **Low** (static HTML component on profile template)
- Impact: Medium — builds TradieTools as the "smart homeowner's choice" and differentiates from bare directories.

---

### D. Keep Them Engaged Between Jobs

**14. Homeowner accounts**
- Problem: Every visit starts from scratch. No history, no favourites, no personalisation.
- What it looks like: Optional lightweight account (email + password). Stores: saved tradies, past quote requests, home address (for suburb-level matching), saved articles. Login with Google/email.
- Effort: **High** (new auth system, homeowner DocType, saved items)
- Impact: High — retention multiplier. Accounts turn one-time visitors into repeat users.

**15. Saved tradies / favourites**
- Problem: Homeowners find a great plumber and have no way to remember them on TradieTools.
- What it looks like: Heart icon on tradie profile cards. Requires homeowner account. Saved list accessible from homeowner dashboard. Email drip: "Your saved plumber [Name] has 3 new reviews."
- Effort: **Low** once homeowner accounts exist (junction table + UI)
- Impact: Medium — drives return visits without requiring a current job.

**16. Seasonal maintenance reminders**
- Problem: Homeowners only search for tradies when something breaks. We should be top-of-mind before then.
- What it looks like: Email sequence (opt-in on quote request): "Autumn in NZ is gutter-cleaning season — here's what to check." "Winter is coming — is your heating system ready?" Links to relevant cost guides and /find/ filtered by relevant trade.
- Effort: **Low** (email sequence in Frappe + drip trigger on quote submission)
- Impact: High — recurring touchpoint that drives unprompted return visits and new quote requests.

---

### E. Drive Referrals

**17. Shareable tradie profiles**
- Problem: When a homeowner finds a great tradie through TradieTools, there's no frictionless way to share the profile.
- What it looks like: "Share this tradie" button on profile page — generates a clean shareable link and pre-populates WhatsApp/Facebook/email share text: "Found this plumber on TradieTools — 4.9 stars, available now: [link]"
- Effort: **Low** (share buttons + URL with UTM tracking)
- Impact: Medium — word-of-mouth amplification for both tradie and platform.

**18. "Tell a friend" referral program**
- Problem: No mechanism to reward homeowners who bring new users.
- What it looks like: After a successful quote request, show: "Did TradieTools help you? Give a friend $20 off their first job." Tracked via referral link. $20 credit applies when friend completes a quote request for a Pro tradie.
- Effort: **High** (referral tracking, credit system, redemption flow)
- Impact: Medium-High — organic acquisition channel, especially in tight NZ communities.

---

## SECTION 4: TRADIE VALUE — WHAT WILL MAKE THEM PAY AND STAY

### A. More and Better Leads

**1. Claim-a-lead flow (replace silent email blast)**
- Tradie problem: Receive an email blast with no way to acknowledge, decline, or follow up. They don't know if 2 other tradies are already racing them.
- What it looks like: Email notification includes "Accept this lead" / "Not available" buttons (tokenised link, no login required). Dashboard shows lead inbox. Accepting sends homeowner a notification: "[Name] has accepted your request and will be in touch." Declining frees the slot for the next-ranked tradie.
- Effort: **Medium** (token-based lead action URLs, lead status DocType, homeowner notification)
- Monetisation: Gate "lead inbox history" to Verified ($29) tier. Free tier gets email only.

**2. Lead quality scoring**
- Tradie problem: Not all leads are equal. A "bathroom renovation" could be a $5k job or a $50k job.
- What it looks like: Quote form asks: budget range, timeline urgency, job size, property type. Score shown to tradie before they accept: "Quality: High — budget $20k+, starts within 4 weeks, verified homeowner contact."
- Effort: **Medium** (add scoring fields to quote request form + display in lead notification)
- Monetisation: Pro tier ($59) gets full quality score. Verified ($29) gets just "High/Medium/Low."

**3. Expanded search radius / suburb matching**
- Tradie problem: Can only match by city. A plumber in Ponsonby gets matched to jobs in Manukau 30km away.
- What it looks like: Tradie sets service area by suburb radius (5km, 15km, 30km from their base). Lead matching uses suburb coordinates instead of just city.
- Effort: **Medium** (suburb coordinates in tradie_listings, haversine distance in lead matching SQL)
- Monetisation: Suburb matching = Verified tier feature. City-level only = free.

**4. Lead inbox dashboard**
- Tradie problem: All lead history lives in email inbox, not in TradieTools. Can't track which leads converted.
- What it looks like: Leads tab in tradie dashboard showing: all leads received (date, trade type, suburb, quality score), status (accepted/declined/expired), outcome (won/lost — tradie marks manually), revenue logged.
- Effort: **Medium** (lead_records DocType, dashboard component)
- Monetisation: Full inbox = Pro tier. Last 5 leads = Verified. Email only = free.

---

### B. Win More Jobs

**5. Profile completeness score with coaching**
- Tradie problem: Don't know what's holding their profile back.
- What it looks like: Progress bar in dashboard: "Your profile is 60% complete." Below it: "Add 3 photos (+15%) | Add your NZBN (+10%) | Get your first review (+25%)". Each action links directly to the relevant edit screen.
- Effort: **Low** (score calculation function + dashboard component)
- Monetisation: Free feature — drives engagement and upsell to tiers that unlock more items.

**6. Response time coaching**
- Tradie problem: Don't know that slow responses hurt their ranking and lead win rate.
- What it looks like: Analytics shows: "Your avg response time: 18 hours. Top tradies in your area: 2 hours. Responding within 4 hours doubles your win rate." Red/amber/green indicator.
- Effort: **Medium** (response time tracking in lead routing, display in analytics)
- Monetisation: Verified tier feature.

**7. Quote templates by trade type**
- Tradie problem: Writing quotes from scratch takes 30 minutes. Many sole traders don't bother with formal quotes.
- What it looks like: Pre-built quote templates for top jobs by trade: "Standard plumbing callout quote," "Deck build quote," "Bathroom renovation quote." Tradie fills in job-specific figures. Downloads as PDF or sends via the TradieTools platform.
- Effort: **Low-Medium** (template JSON + quote builder integration)
- Monetisation: Free (drives quote builder tool usage, upsells to paid quote builder subscription).

**8. Proposal builder (win the job before the competition calls)**
- Tradie problem: Homeowners are comparing 3 tradies. A professional proposal beats a text message.
- What it looks like: After accepting a lead, tradie can build a proposal: quote price + timeline + scope of work + 3 photos of similar past work + personalised message. Sent to homeowner via TradieTools (branded email). Homeowner sees all proposals side by side.
- Effort: **High** (proposal DocType, comparison UI for homeowner, email delivery)
- Monetisation: Pro tier only.

---

### C. Save Admin Time

**9. Invoice generation from quote**
- Tradie problem: Win a job, then have to recreate the quote as an invoice in a completely separate tool.
- What it looks like: One-click: convert accepted quote to invoice. Add deposit/progress/final payment stages. Send to homeowner with payment link (Stripe). Mark as paid when received.
- Effort: **Medium** (invoice DocType extending quote, payment integration)
- Monetisation: Professional quote tier ($9.99/mo) or Pro listing tier ($59/mo).

**10. Job pipeline tracker**
- Tradie problem: Managing 5 active jobs in their head (or a spreadsheet).
- What it looks like: Simple Kanban: Leads → Quoted → Won → In Progress → Invoiced → Complete. Drag jobs between stages. Each job card shows: homeowner name, job type, value, due date.
- Effort: **Medium** (job pipeline DocType + dashboard UI)
- Monetisation: Pro listing tier ($59/mo).

**11. Customer CRM (simple)**
- Tradie problem: "I had a great experience with that plumber 18 months ago. What was his name again?"
- What it looks like: Each completed job creates a customer record: name, address, job type, notes. Tradie can add "call for spring gutters" reminder. View job history per customer.
- Effort: **Medium** (Customer DocType, notes field, reminder feature)
- Monetisation: Pro listing tier ($59/mo).

**12. Availability calendar**
- Tradie problem: Booked for 6 weeks but still receiving and ignoring leads — wastes homeowner time and damages tradie's response rate.
- What it looks like: Simple weekly calendar in dashboard. Block out unavailable weeks. Public-facing: "Available from [date]" on profile. System pauses lead routing when tradie is blocked out.
- Effort: **Medium** (availability DocType, calendar UI, pause lead routing logic)
- Monetisation: Verified tier feature.

---

### D. Build Reputation

**13. Automated review request after job complete**
- Tradie problem: Happy customers don't think to leave reviews. Reviews require active effort to collect.
- What it looks like: When tradie marks a job as "Complete" in job pipeline, TradieTools sends a branded email to the homeowner: "How did [Name] do? Leave a review (takes 30 seconds)." Timing: 3 days after completion. Reminder after 7 days if no response.
- Effort: **Low** (Frappe Workflow trigger on job status change → sendmail)
- Monetisation: Verified tier feature — biggest incentive to upgrade from free.

**14. Real licence/credential badges**
- Tradie problem: Can't prove they're legitimate without calling a client or emailing their licence number.
- What it looks like: Tradie uploads licence photo + number → admin verifies against MBIE/EWRB/PGD register → badge appears on profile: "LBP #[number] — Verified [month/year]." Expires and is removed if licence lapses.
- Effort: **High** (verification workflow in Frappe, MBIE/register API or manual check, badge display)
- Monetisation: This IS the core value of the Verified ($29) tier — rename and redefine the tier around real verification.

**15. Portfolio gallery (as reputation builder)**
- Tradie problem: No way to show past work on TradieTools.
- What it looks like: Up to 20 photos with job type tags. "Featured project" section with before/after slider. Displays prominently on profile.
- Effort: **Medium** (photo upload to object storage, gallery component)
- Monetisation: Free tier: 5 photos. Verified ($29): 20 photos. Pro ($59): unlimited + before/after feature.

**16. Response time badge**
- Tradie problem: Fast responders aren't rewarded. Slow ones aren't penalised (in a visible way).
- What it looks like: Green "Fast Responder" badge for tradies with avg response < 4 hours. Displayed in search results and profile. Disappears if response time degrades.
- Effort: **Low** (metric from lead routing, badge logic)
- Monetisation: Free — incentivises engagement on all tiers.

---

### E. Grow Their Business

**17. Expanded analytics dashboard**
- Tradie problem: Only see 30-day views/clicks. Can't see trends, search impressions, or what's working.
- What it looks like: 90-day view with trend lines. Search impressions (how many times profile appeared in /find/ results). Click-through rate. Lead conversion rate (impressions → quote requests). Comparison to last month.
- Effort: **Medium** (analytics_events extension, dashboard charts)
- Monetisation: Verified tier ($29): 90-day analytics. Pro tier ($59): full history + competitor benchmarking.

**18. ROI / earnings tracker**
- Tradie problem: "Is TradieTools worth $59/month?" — they genuinely don't know.
- What it looks like: After each won job (marked in pipeline), tradie enters job value. Dashboard shows: "Estimated earnings from TradieTools leads this month: $X,XXX. Your subscription costs $59. ROI: [X]×." Compare to word-of-mouth acquisition cost.
- Effort: **Low** once pipeline tracker exists (job value field + ROI calculation)
- Monetisation: Makes the upsell case for Pro tier almost automatic.

**19. Competitor benchmarking**
- Tradie problem: "Am I good? Am I getting better?" — no context without comparison.
- What it looks like: In analytics: "You rank #3 of 11 plumbers in Auckland. Your review count is below average for your rank position — getting 2 more reviews would likely move you to #1."
- Effort: **Medium** (anonymised peer data from rankings table + display logic)
- Monetisation: Pro tier only.

**20. Weekly business tips email**
- Tradie problem: Most sole traders have no one teaching them the business side of running a trade business.
- What it looks like: Weekly email: "This week's tip: How to price a job so you're not leaving money on the table." Links to article on TradieTools. Soft promotion of tools (quote builder, invoicing). Optional unsubscribe.
- Effort: **Low** (email template + weekly send triggered from content calendar, reuse article content)
- Monetisation: Free — drives content engagement, keeps tradies thinking about TradieTools.

---

## SECTION 5: CONTENT & SEO STRATEGY

### 5A. Missing Cost Guide Topics (High NZ Search Volume) — Wave 2 Priorities

| Priority | Title | Target Keyword | Why High Intent |
|---|---|---|---|
| P1 | How Much Does a Heat Pump Cost to Install in NZ? 2026 | heat pump installation cost nz | High winter demand, $3-8k jobs |
| P1 | Bathroom Renovation Cost NZ 2026: Full Breakdown | bathroom renovation cost nz | Very high volume, commercial intent |
| P1 | Kitchen Renovation Cost NZ 2026 | kitchen renovation cost nz | Top 5 most searched home reno queries |
| P1 | How Much Do Electricians Charge Per Hour in NZ? | electrician cost per hour nz | High volume, clear tradie match |
| P1 | New Roof Cost NZ 2026 — What to Expect | new roof cost nz | Expensive job, homeowners seek validation |
| P1 | Waterblasting Cost NZ 2026 | waterblasting cost nz | Seasonal, high volume, low competition |
| P1 | Double Glazing Cost NZ 2026 | double glazing cost nz | Energy efficiency trend, government subsidies |
| P1 | Landscaping Cost NZ 2026 — Quotes and Rates | landscaping cost nz | Very broad, high volume |
| P1 | Fence Cost NZ 2026: Wood, Colorbond, Concrete | fence cost nz | Common job, good calculator potential |
| P1 | Driveway Cost NZ 2026: Concrete vs Asphalt vs Gravel | driveway cost nz | High comparison intent |
| P1 | Insulation Cost NZ 2026 — Ceiling, Underfloor, Wall | insulation cost nz | Government incentive angle, high demand |
| P1 | Plumber Cost Per Hour NZ 2026 | plumber cost per hour nz | Top searched tradie query |
| P2 | Tiling Cost NZ 2026 | tiling cost nz | Popular bathroom/kitchen job |
| P2 | House Painting Cost NZ 2026 — Interior + Exterior | house painting cost nz | Seasonal, high volume |
| P2 | Garage Door Installation Cost NZ | garage door installation cost nz | Specific, commercial intent |
| P2 | Alarm System Installation Cost NZ | alarm system installation cost nz | Home security trend |
| P2 | Retaining Wall Cost NZ 2026 | retaining wall cost nz | Common Auckland/Wellington job |
| P2 | Solar Panel Installation Cost NZ 2026 | solar panel cost nz | Rapidly growing search volume |
| P2 | Carpet vs Hardwood Floor Cost NZ | carpet installation cost nz | Comparison content, interior reno |
| P2 | Deck Building Cost NZ 2026 | deck cost nz | Existing calc to link from |

### 5B. Informational Content for the Homeowner Journey (Top of Funnel)

**"How to Hire" Series (one per major trade):**
- How to Hire a Builder in NZ: The Definitive Guide
- How to Hire a Plumber in NZ (and Not Get Ripped Off)
- How to Hire an Electrician in NZ — What to Check First
- How to Hire a Roofer in NZ — Key Questions and Red Flags

For each: What the trade covers, what licences are required, how to compare quotes, what a fair price looks like, red flags to watch for, questions to ask before signing. Link to /find/ filtered by that trade.

**"What to Ask" Series:**
- 10 Questions to Ask Your Builder Before Signing Anything
- What Questions Should I Ask a Plumber? (The Non-Obvious Ones)
- Questions to Ask a Tradie Before They Start Work: A Checklist

**Trust & Safety Content:**
- How to Spot a Cowboy Builder in NZ — 7 Red Flags
- Do I Need a Licensed Building Practitioner? (LBP Explained for NZ Homeowners)
- Understanding Tradie Quotes: What Should Be in Writing
- What Your Home Insurance Covers When a Tradie Messes Up
- How to Make a Complaint About a Tradie in NZ (Disputes Tribunal, MBIE, Trade Boards)

**Emergency Guides (very high commercial intent):**
- Burst Pipe in NZ — What to Do Right Now [link to /find/plumbers]
- Power Outage: Is It Your Fuse Box? What an Electrician Can Fix Tonight
- Roof Leak in a Storm — Immediate Steps and Emergency Roofers

### 5C. Location Pages Gap Analysis

**Current:** 20 major cities
**Missing — Towns with meaningful tradie search volume:**

Immediate additions (P1):
- Taupo, Masterton, Ashburton, Oamaru, Westport/Greymouth, Kaitaia, Kerikeri/Paihia, Levin, Paraparaumu/Kapiti (already listed as Kapiti Coast — confirm URL), Fielding, Matamata, Pukekohe, Waiuku

**Suburb-level pages — Auckland is the priority:**
- The Auckland metro has 1.7m people across 21 distinct suburb clusters
- High-priority: Remuera, Ponsonby, Parnell, Epsom, Mt Eden, Botany, Manukau, Henderson, Kumeu, Pukekohe, North Shore (Takapuna, Devonport, Albany), Waitakere/West Auckland
- Rule of thumb: build suburb pages for any suburb cluster with 50k+ population

**Wellington suburbs:**
- Petone, Lower Hutt, Upper Hutt (already listed), Johnsonville, Karori, Island Bay, Tawa

**Christchurch suburbs:**
- Riccarton, Papanui, Hornby, Rolleston (fast growing), Rangiora

**Threshold for new location pages:** Build when: (a) town population > 15,000 OR (b) suburb cluster population > 30,000 in Auckland/Wellington/Christchurch.

### 5D. Schema Markup Gaps

| Missing Schema | What It Enables | Priority | Implementation |
|---|---|---|---|
| **LocalBusiness** on tradie profile pages | Rich results: star rating, hours, phone in SERPs for individual profile pages | **Critical** | Add to /businesses/{slug}/ template |
| **Review + AggregateRating** | Star ratings in Google search results for tradie profiles and trade-city pages | **Critical** | Add to profile pages and trade-city pages once reviews are live |
| **Service** schema | Google understands what specific services each tradie offers | High | Add to profile pages with service types |
| **Article / BlogPosting** | Google News eligibility, structured display for cost guide articles | High | Add to /articles/{slug}/ template |
| **Product** schema | Rich results for template downloads | Medium | Add to /templates/ page items |
| **DefinedTerm** | Rich results from glossary | Medium | Wrap each glossary term |
| **SpeakableSpecification** | Voice search (Google Home, Siri) reads FAQ answers | Low | Add to FAQ page |
| **Event** | Time-sensitive content (tax dates) | Low | Add to /tax-dates/ |

### 5E. What Makes Our Content 10× Better

1. **Real data from actual listings.** Our /tradie-rates/ matrix uses real hourly rates from tradie_listings. Competitors use made-up ranges. Use this in every cost guide: "Based on 47 plumbers listed on TradieTools across NZ, the average is $X/hr."

2. **Embedded calculators inside articles.** Every cost guide should have the relevant calculator embedded mid-article, not just linked. Someone reading "how much does a deck cost?" should be able to enter their measurements and get a live estimate on the same page.

3. **Live rate lookup in cost guides.** "What do plumbers charge in Christchurch?" — show the live top-5 ranked plumbers in Christchurch with their hourly rate pulled from the listing. Bridges content and directory.

4. **NZ-accuracy obsession.** Competitors publish generic AU/NZ content. We publish NZ-specific prices by city, NZ licensing requirements, NZ GST calculations, NZ seasonal context (heating before winter, waterblasting after winter). This is our moat.

5. **Tradie education hub.** Create /for-tradies/ content cluster: pricing strategy, tax basics, how to win jobs, building your online profile. This content ranks for tradie searches AND drives tradie listing signups.

6. **Before/after case studies.** Partner with 3-5 pro-tier tradies for "Project Stories" — real before/after photos, cost breakdown, homeowner testimonial, tradie's tips. Rich content competitors don't have.

### 5F. Technical SEO Quick Wins (Do Now)

1. **Deploy all 169 articles** — the single highest ROI action available. Each article takes ~30 seconds to deploy. Do it.
2. **Add Article schema to all 169 cost guides** — missing on current build.
3. **Add LocalBusiness schema to all /businesses/{slug}/ pages** — missing, should be first priority for profile pages.
4. **Internal linking: cross-link articles to /find/ filtered results** — every "how to hire a plumber" article should have a contextual link to `/find/?trade=plumber&city=auckland`.
5. **Add AggregateRating schema to /trades/{trade}/{city}/ pages** — use aggregated rating from rankings table.
6. **Fix title tag lengths** — audit all pages for >70 char titles (known issue from prior audit, 22 trimmed already).
7. **Submit XML sitemap for wave 2 articles to Google Search Console** immediately after deploy.
8. **Add missing alt text to all listing card images** in /find/ output.
9. **Add DefinedTerm schema to /glossary/** — 200 terms are schema-rich content sitting untagged.
10. **Add canonical tags to paginated /find/ results** — prevent duplicate content signals as pagination grows.

---

## SECTION 6: MONETISATION IMPROVEMENTS

### Is $29/$59 Optimally Positioned?

**Current structure assessment:**
- Free: listing, appears in directory — good entry point
- Verified $29/mo: email-verified badge + analytics — **underpowered** (badge means nothing meaningful)
- Pro $59/mo: same as above + passive lead matching + priority support — gap too narrow from $29
- Quote builder $9.99/mo (separate): good tool, confusingly separate from listing tiers

**Problems with current structure:**
1. "Verified" badge is misleading — it means "email verified," not "licence checked"
2. $29 → $59 jump for "lead matching" is underwhelming — tradies don't see the value
3. Quote builder is siloed — a plumber who wants both a good listing AND a quote tool pays $29 + $9.99 = $38.99 which is close to Pro tier ($59) but with worse listing features
4. No tier clearly earns its own ROI story

**Recommended new tier structure:**

| Tier | Price | Name | Target | Core Value Prop |
|---|---|---|---|---|
| **Starter** | Free | Listed | New tradies, testing TradieTools | Appear in directory, basic profile, 3 quotes/month |
| **Verified** | $29/mo | Verified | Established tradies wanting leads | Real licence badge + photos + review collection + analytics + quote builder (10/mo) |
| **Pro** | $59/mo | Pro | Growth-focused tradies | Everything in Verified + lead inbox + claim-a-lead + job pipeline + invoicing + unlimited quotes + competitor benchmarking |
| **Business** | $99/mo | Business (new) | Multi-person operations | Everything in Pro + 3 team logins + branded proposals + account manager |

**Key changes:**
- Rename "Verified" to mean ACTUAL verification (LBP/EWRB/PGD badge)
- Merge quote builder into Verified ($29) tier — remove the separate $9.99 sub
- Add Business tier at $99 to capture multi-person operations (currently invisible to us)
- Gap $29→$59: close the gap by making Pro about lead management tools, not just more leads

### What Should Be Gated (Currently Free → Paid)

| Feature | Move to | Reason |
|---|---|---|
| More than 5 profile photos | Verified ($29) | Photos are a core conversion driver |
| Lead inbox (dashboard view) | Verified ($29) | Email-only for free tier |
| Analytics beyond 7 days | Verified ($29) | 30-day window is a paid differentiator |
| Suburb-level lead matching | Verified ($29) | City-level for free |
| Claim-a-lead flow | Pro ($59) | Core Pro value |
| Response time badge | Free (earned) | Incentivises engagement on all tiers |
| Profile completeness coaching | Free | Drives upgrades organically |
| Quote templates | Verified ($29) | Bundled with quote builder |

### New Revenue Streams

1. **Featured listing spots** — 1-3 "Sponsored" cards above organic results in /find/ and /trades/{trade}/{city}. Fixed weekly rate by trade + city combo (e.g., $25/week for "Auckland Electricians"). Sold via self-serve in dashboard. Estimate: 20 slots × avg $20/week = $2k/mo immediately achievable.

2. **Homeowner-posted jobs** (reverse marketplace) — Homeowner posts a job ("I need a painter in Wellington next month, budget $3k"). Tradies browse and apply. Pro tier tradies get first look. This flips from push (TradieTools sends leads) to pull (tradies seek work). Revenue: Free to post for homeowners, included for Pro tradies, or $5/job for Verified tradies to apply.

3. **Tool/supply affiliate links** — Every cost guide references materials. Mitre 10, Placemakers, Bunnings all have affiliate programs. "Materials for a deck build: Here's what you'll need and where to buy it in NZ [affiliate links]." Conservative estimate: 2% of traffic × average $80 cart = meaningful passive income.

4. **Insurance referral partnership** — Partner with a NZ public liability insurer (e.g., BizCover NZ, Ando Insurance). When a tradie signs up: "Get public liability insurance — required for Pro verification." Referral fee per quote/policy.

5. **Lead credits (à la carte)** — For free-tier tradies who want occasional extra leads without a subscription. $5/lead credit, buy in packs of 5 or 10. Lower barrier than a monthly subscription.

6. **Tradie directory placements for suppliers** — Tool suppliers (Makita, DeWalt, Hilti) want to reach tradies. Sponsored placement in the tradie dashboard "Tools we recommend" section. Display advertising to a targeted tradie audience.

### What Makes Each Upgrade Feel Obvious

**Free → Verified ($29):**
"You've received 3 lead notifications this month via email. With Verified, you get: (1) A real licence badge so homeowners trust you more. (2) A lead inbox to manage all leads in one place. (3) Automated review requests that build your reputation while you sleep. (4) Unlimited quote builder. For $29/month — that's one extra job per year to cover it."

**Verified → Pro ($59):**
"You're ranked #4 in Auckland plumbers. To reach #1, you need more reviews and faster lead responses. With Pro: Claim leads before competitors, see lead quality scores, manage your job pipeline, send professional proposals, and track which leads turned into revenue. Most Pro tradies see ROI within their first month."

**Pro → Business ($99):**
"Your business has multiple team members but only one TradieTools login. With Business: 3 team logins, branded proposals, and a dedicated account manager to help you get the most out of TradieTools."

### Quote Builder vs Listing Tiers — Merge Recommendation

**Merge** — keep one billing relationship per tradie. Quote builder becomes part of the listing tier:
- Free: 3 quotes/month (keep as is)
- Verified ($29): 20 quotes/month
- Pro ($59): Unlimited quotes + invoicing
- Existing $9.99/mo quote subscribers: migrate to Verified ($29) tier — they get more (badge, analytics, reviews) for an extra $19/month. Frame as upgrade, not price increase.

---

## SECTION 7: TRUST & SAFETY

### 7A. Licence & Credential Verification

**Builders — Licensed Building Practitioners (LBP)**
- Legal requirement: Mandatory for all restricted building work in NZ (new homes, structural work, weathertightness work) under the Building Act 2004.
- How to verify: MBIE maintains a public LBP register. API available via MBIE open data or web lookup at lbp.mbie.govt.nz. Tradie provides name + licence number → we look up against register.
- Implementation: Admin-side Frappe workflow: tradie submits licence number → Python script pings MBIE register API or scrapes public lookup → if match, auto-approve badge; if no match, flag for manual review.
- Badge: "LBP Licensed — Verified [Month Year]" with licence class (e.g., Carpentry, Design, Site).
- Expiry: LBP licences renew every 2 years. Set badge expiry date; send reminder 30 days before to re-verify.

**Electricians — EWRB (Electrical Workers Registration Board)**
- Legal requirement: All electrical work in NZ must be performed by a registered/licensed electrical worker.
- How to verify: EWRB public register at ewrb.govt.nz/public-register. Lookup by name/licence number.
- Badge: "EWRB Registered — [Category]" (e.g., Electrician, Electrical Inspector).

**Plumbers/Gasfitters/Drainlayers — PGD Board**
- Legal requirement: Gasfitting requires a licensed gasfitter. Drainlaying requires a licensed drainlayer. Some plumbing is restricted.
- How to verify: PGD Board public register at pgdb.co.nz.
- Badge: "PGD Licensed — [Type]" (Plumber / Gasfitter / Drainlayer / Certifying Plumber).

**Engineers — Engineering NZ**
- Voluntary but significant: CPEng (Chartered Professional Engineer) is the recognised credential.
- How to verify: Engineering NZ register.
- Badge: "Chartered Professional Engineer" — niche but important for structural/civil engineering work.

**Other regulated trades:**
- Pest controllers: No formal NZ licence register — check for ChemCert training instead.
- Refrigeration technicians: Tradesperson Certificate from BCITO. Verify by certificate number.
- Asbestos removal: WorkSafe NZ licensing for Class A/B removers. Verify via WorkSafe register.

**Implementation approach (Frappe):**
```
Verification Request DocType:
- tradie_id, trade_type, licence_number, submitted_at
- verification_status: pending/approved/rejected/expired
- verified_by (admin user), verified_at
- expiry_date (auto-calculated from licence type)
- badge_display_text

Frappe Workflow:
Submitted → Auto-check API → [Match] Auto-approve + set badge
                           → [No match] Flag for manual review → Admin approves/rejects
```

### 7B. Insurance Verification

**What tradies should hold:**
- **Public liability insurance** (minimum $1M NZD) — covers damage to homeowner property
- **Professional indemnity** (relevant for designers, project managers) — covers advice/design errors
- **Employer's liability** (if they have employees) — covers staff injuries
- **Contractor's all-risk** (for larger projects) — covers tools and work-in-progress

**How to verify without becoming an insurer:**
- Self-declaration upload: tradie uploads Certificate of Currency (insurance certificate) showing policy name, coverage type, coverage amount, expiry date.
- Admin manually reviews document (spot check) — not full underwriter review.
- Badge: "Insured — Public Liability $[X]M — Verified [Month Year]"
- Refresh cycle: Annual (insurance policies renew yearly). Send reminder 45 days before expiry.
- **We do not guarantee coverage** — add clear disclaimer: "TradieTools verifies the existence of the policy at verification date. Contact the tradie for current certificate before signing a contract."

**Minimum bar for "Insured" badge:** Public liability ≥ $1M NZD, policy not expired at time of verification.

### 7C. Identity & NZBN Verification

**NZBN (New Zealand Business Number):**
- All NZ businesses and sole traders can have an NZBN from the Companies Office.
- Public NZBN register: api.business.govt.nz (open API, free).
- Tradie provides NZBN → we confirm it matches their business name and is active.
- Badge: "NZBN Verified Business" — not a quality signal, but confirms they're a registered entity.
- Value: Eliminates fake listings from non-existent businesses.

**Driver's licence / identity:**
- Not recommended as mandatory — creates friction and privacy concerns.
- Optional: Tradies can verify identity via a photo ID upload (driver's licence or passport) if they want an additional "ID Verified" badge. Admin holds the ID securely — never shown publicly.
- NZ Privacy Act note: ID documents are sensitive personal information. Must be deleted after verification. Do not store full image in database — store only verification status and date.

**Recommended verification tier:**
- Free tier: Email verified only
- Verified ($29): NZBN verification + licence check
- Pro ($59): All of the above + insurance verification + optional ID verification

### 7D. Review Integrity

**Fake review prevention:**
- Require lead connection: Only homeowners who submitted a quote request for that tradie can leave a review by default. Reviewers are matched to quote request records.
- Optional open reviews: Homeowners can also review tradies they found "offline" (off-platform) — but these require email verification and show as "Unverified Job" reviews (vs "Verified Lead" reviews).
- One review per homeowner per tradie: Prevent repeat reviews from same email.
- Rate limiting: IP-based — max 3 new reviews per IP per hour.
- Competitor sabotage detection: Flag reviews from email addresses that have reviewed 5+ tradies in the same trade in 30 days (unusual pattern).

**What "Verified Review" means on TradieTools:**
- The reviewer submitted a quote request for this specific tradie through TradieTools AND their lead was matched to this tradie.
- This is stronger than Builderscrack/No Cowboys because the homeowner-to-tradie connection is on-platform and auditable.

**Review moderation workflow:**
1. Review submitted
2. Auto-check: does the reviewer email match a quote request for this tradie? If yes → "Verified Lead" status
3. Auto-check: profanity filter, link filter, personal info filter
4. If passes all: auto-publish (no delay — speed matters for tradie confidence)
5. Tradie can flag a review → goes to admin queue → reviewed within 48 hours
6. Admin options: Keep / Remove (with reason) / Request reviewer clarification

**Tradie response mechanism:**
- One public response per review. Response appears below the review: "Response from [Tradie Name]:..."
- 500 character limit. No HTML. Admin can remove responses that are abusive.
- Guidance in dashboard: "Responding professionally to negative reviews increases homeowner trust."

**Triggers for manual review:**
- Rating is 1-star AND review length < 20 words (often fake negative)
- Rating is 5-star AND review is from a newly-created account with no other activity (potentially fake positive)
- Review contains phone number, email address, or external URL (contact data extraction attempt)
- Reviewer has reviewed the same tradie twice

### 7E. Dispute Resolution Process

**Step-by-step flow:**
1. **Homeowner tries direct resolution first** — "Contact the tradie directly about your concern. Most issues are resolved with a conversation. Here's guidance on how to do that professionally."

2. **Formal complaint to TradieTools** (submit form at /help/dispute):
   - Nature of complaint: quality issue / no-show / overcharge / safety incident / fraud
   - Evidence upload: photos, messages, quote/contract
   - TradieTools response time SLA: Acknowledge within 24 hours, initial decision within 5 business days

3. **TradieTools investigation:**
   - Contact tradie with complaint details
   - Request tradie response within 48 hours
   - Review evidence from both sides
   - Decision: (a) No action — complaint not substantiated; (b) Warning issued — tradie notified; (c) Listing suspended — pending investigation; (d) Listing removed — serious breach

4. **External escalation (TradieTools provides guidance, not representation):**
   - Disputes Tribunal (for claims up to $30,000) — disputes.govt.nz
   - Relevant trade board (MBIE, EWRB, PGD Board) for licence complaints
   - Consumer NZ for consumer protection issues
   - WorkSafe NZ if safety incident occurred on site

**What TradieTools will NOT do:**
- Act as a guarantor for quality of work
- Provide financial compensation to homeowners
- Arbitrate legally binding decisions
- Vouch for tradies in legal proceedings

**Protecting TradieTools legally:**
- Terms of Service must clearly state: "TradieTools is a directory service and does not employ or guarantee tradies."
- Dispute page must clearly state: "We will investigate complaints fairly but our decisions are not legally binding."
- Ensure Terms are up to date under NZ Fair Trading Act and Consumer Guarantees Act.

### 7F. Bad Actor Prevention

**Fake listings:**
- Prevention: NZBN verification (at Verified tier) eliminates fake businesses
- Detection: Admin review queue for new free listings. Flag any listing with: no profile photo, no phone number, no website, only one-word bio, or email from a free provider (Gmail, Hotmail) with no domain
- Response: Hold suspicious listings for 24-hour human review before publishing

**Spam lead requests:**
- Prevention: Rate limiting on /get-quotes/ — max 3 submissions per IP per hour, max 5 per day
- CAPTCHA on form submission (lightweight — Cloudflare Turnstile, invisible to real users)
- Pattern detection: same email + same job description across multiple cities = likely competitor intel gathering
- Response: Shadow block (allow submission but don't route to tradies, log for review)

**Contact data scraping:**
- Prevention: Tradies on free tier have phone/email behind a "Reveal contact" click (trackable event). Don't render phone numbers in raw HTML — use JS or a reveal endpoint
- Rate limiting on contact reveal events: max 20 per session per IP
- Honeypot phone field in free listing pages (catches scrapers)

**Account hijacking:**
- Passwords stored as bcrypt hashes (standard)
- Login rate limiting: 5 failed attempts → 15-minute lockout → email alert to account holder
- Session invalidation on password change
- No admin-level session tokens in URL parameters

**Payment fraud:**
- Stripe handles card fraud detection (Stripe Radar)
- For disputes/chargebacks: document all subscription signups with IP, email, timestamp
- Idempotency keys already implemented (good) — prevents double-charge
- Monitor for subscription cycling (subscribe, extract value, cancel, repeat)

### 7G. NZ Privacy Act 2020 Compliance

**Personal data we collect:**
- **Tradies:** Name, email, phone, address, trade type, hourly rate, NZBN, licence numbers, bank details (if invoicing), photos, location
- **Homeowners:** Name, email, phone, home address/suburb, job description, budget

**Key NZ Privacy Act 2020 obligations:**
1. **Collection limitation:** Only collect data necessary for the service. Don't collect homeowner address until needed for job matching.
2. **Use limitation:** Don't use tradie contact data for our own marketing without consent. Don't sell homeowner data to third parties.
3. **Security:** Data must be protected. Encrypt PII at rest. HTTPS only. Audit access logs.
4. **Individual access:** Any person can request their data within 20 working days. Need a process for this.
5. **Correction:** Persons can correct incorrect data. Allow self-service correction in dashboard.
6. **Retention limits:** Quote request data: delete homeowner details after 12 months if no account created. Tradie data: retain while account active + 7 years after closure (tax purposes).

**Privacy policy gaps to address:**
- Clearly state what data is collected and why
- Disclose data processors: Stripe (US), email provider, server host (if offshore)
- Cross-border disclosure: NZ Privacy Act requires disclosure when data is sent offshore (US = Stripe, Google Analytics, etc.)
- Right to erasure process: How do users request deletion? (Add email contact or form)
- Cookie policy (if using GA4 or advertising cookies)
- Data breach response procedure (must notify Privacy Commissioner and affected individuals within 72 hours of a notifiable breach)

**Data retention policy:**
- Quote requests: homeowner PII deleted after 12 months if no account
- Tradie listings: retained while active; deleted within 30 days of account closure (except for reviews which may retain anonymised data)
- Payment records: 7 years (IRD requirement)
- Verification documents (licence photos): delete originals after verification; retain verification record indefinitely

### 7H. Trust Roadmap

**Must have before scaling (build before major marketing push):**
- Visible review system (submit + display on profiles) — without this, all trust is performative
- Honest badge rename: "Email Verified" ≠ "Licence Verified." Fix naming before users notice
- Dispute contact page (even just an email link) — legal protection + homeowner confidence
- NZ Privacy Act compliant privacy policy — legal obligation
- Rate limiting on quote form (bot prevention)
- NZBN verification option for Verified tier tradies

**Should have in 3 months:**
- LBP badge (MBIE lookup) — highest-value trust signal in NZ trades
- EWRB badge (electricians) — second most searched regulated trade
- Portfolio photos — trust signal nearly as strong as reviews
- Review moderation workflow — automated checks + admin queue
- Availability toggle — quick win, reduces homeowner frustration
- Security review of authentication (session management, rate limiting on login)

**Nice to have at scale:**
- PGD Board verification (plumbers/gasfitters)
- Insurance certificate upload + "Insured" badge
- Full homeowner account with claim-a-review system
- NZBN auto-verification via API
- Background check partnership (police vetting for in-home trades)
- Formal dispute mediator relationship (Consumer NZ partnership?)

---

## SECTION 8: THE NORTH STAR

### What TradieTools Needs to Become

TradieTools must become **New Zealand's most trusted place to find and hire a verified tradie** — not just a directory, but the tool that makes the entire process of finding, vetting, hiring, and reviewing a tradie safer and smarter than anywhere else.

The brand promise is simple and memorable: *"Find a tradie you can actually trust."*

Today, Builderscrack wins on volume (332k reviews, 16k tradies). No Cowboys wins on brand recognition. TradieTools can win on **verification credibility** — by being the only platform where a badge means something real, where content tells homeowners what to look for before they even pick up the phone, and where tradies get the tools to run a better business.

We don't need to out-review Builderscrack. We need to be the platform that homeowners who've been burned by a cowboy builder turn to next — because TradieTools is the platform that checks.

### The Unique Value Proposition

*"The only NZ tradie platform where 'Verified' means what it says — licence-checked, insured, and reviewed by real homeowners."*

### The 3 Features That Will Define Us as #1

**1. Real Licence Verification Badges (LBP, EWRB, PGD)**
*Why it defines us:* No other NZ platform currently shows specific trade licence badges checked against MBIE/EWRB/PGD registers. "Verified" on competitors means email confirmed. "Verified" on TradieTools means the government register agrees they're qualified. This is a platform-defining trust signal that Builderscrack, No Cowboys, and Hipages cannot match quickly.

**2. Review System with Verified Lead Badge**
*Why it defines us:* Anyone can fake reviews. Our reviews are attached to actual quote request records — so "Verified Lead Review" means the homeowner used TradieTools to find this tradie, not just that they typed in an email address. This is structurally more trustworthy than No Cowboys ($999/year, unverified reviews) and catches up to Builderscrack's review moat with a credibility edge.

**3. Claim-a-Lead with Homeowner Visibility**
*Why it defines us:* Homeowners hate the black box of sending a quote request and hearing nothing. Tradies hate silent email blasts they can't manage. "Claim-a-lead" closes both loops — homeowner sees "[Name] has accepted your request," tradie manages their lead pipeline. This is a better UX than Builderscrack's model and converts the one-time homeowner visitor into a return user.

Together, these three features mean:
- A homeowner arrives, searches, sees real reviews and a real LBP badge → trusts the platform
- They submit a quote → know exactly who got it and when someone responded → trust the process
- The tradie accepts the lead, builds their pipeline, collects reviews automatically → sees ROI → stays on the platform

That flywheel — trust → engagement → retention → more reviews → more trust — is how you beat a 16-year-old incumbent with 332,000 reviews.

---

## PRIORITISED ROADMAP

### NOW — 0 to 4 Weeks (Quick Wins, High Impact, Low Effort)

| Feature | Beneficiary | Effort | Impact | Why It Matters |
|---|---|---|---|---|
| Deploy all 169 articles (SEO wave 2) | Both | S | H | Each article builds organic search traffic — currently 166 articles built but not live is leaving the biggest SEO opportunity on the table |
| Rename "Verified" badge copy honestly | Tradie | S | H | "Email Verified" vs implied licence check is a legal and trust liability — fix the wording everywhere before you scale |
| Add dispute contact page /help/dispute | Visitor | S | H | Costs nothing to build; immediately increases platform trust and provides basic legal cover |
| Availability toggle ("Taking work" / "Busy") | Both | S | H | Free improvement that reduces homeowner frustration and makes listings feel alive |
| Add profile completeness score to tradie dashboard | Tradie | S | M | Shows tradies exactly what to do to rank higher — drives self-serve profile improvements |
| Rate limiting on /get-quotes/ + CAPTCHA | Both | S | M | Prevents lead spam from bots and competitors harvesting tradie contact data |
| Smart match confirmation page after quote submission | Visitor | S | H | Transform the "black box" — show homeowner who matched their request with profile cards |
| Add Article schema to all cost guide articles | Both | S | M | Missing schema that enables rich results in Google — 30 minutes to implement in Jinja2 template |
| Add LocalBusiness schema to /businesses/{slug}/ | Visitor | S | H | Enables star ratings in Google SERPs for profile pages |
| NZ Privacy Act compliant privacy policy | Both | S | H | Legal obligation — likely non-compliant today |
| Featured listing spots (self-serve) | Tradie | S | M | New revenue stream, minimal build — 1-3 "Sponsored" cards in search results |

### NEXT — 1 to 3 Months (Core Value Features, Growth Drivers)

| Feature | Beneficiary | Effort | Impact | Why It Matters |
|---|---|---|---|---|
| Review system (submit + display + moderation) | Both | M | H | The single biggest trust gap — without reviews, every other trust investment is undermined |
| Portfolio photo upload (gallery on profile) | Both | M | H | Photos are the #1 conversion driver on any services marketplace — tradies without photos are invisible |
| LBP verification badge (MBIE lookup) | Both | M | H | Platform-defining trust signal that no NZ competitor currently offers |
| EWRB verification badge (electricians) | Both | M | H | Second most searched trade in NZ; electricians are heavily regulated |
| Expanded /find/ filters (rating, budget, availability, suburb) | Visitor | M | H | Current 2-filter search is inadequate for serious homeowners |
| Claim-a-lead flow (accept/decline with homeowner notification) | Both | M | H | Replaces silent email blast with a two-way interaction that homeowners can see |
| Lead inbox dashboard (all leads, status, outcome) | Tradie | M | H | Gives tradies a reason to log into TradieTools daily, not just check email |
| Automated review request (trigger on job complete) | Tradie | L | H | Passive review collection is the fastest way to build the review corpus |
| Quote templates by trade (bundled into Verified tier) | Tradie | L | M | Reduces time-to-quote, drives quote builder engagement and tier upgrades |
| Seasonal maintenance email drip (opt-in from quote form) | Visitor | M | M | Re-engage homeowners between jobs with relevant seasonal content |
| NZBN verification option (Verified tier) | Both | M | M | Eliminates fake listings at Verified tier without requiring full identity check |
| Suburb-level search and matching | Both | M | H | Auckland/Wellington homeowners need suburb precision — city-level is too broad |
| Merge quote builder into listing tiers (one subscription) | Tradie | M | M | Simplifies billing and increases perceived value of Verified tier |

### LATER — 3 to 12 Months (Platform-Defining Features)

| Feature | Beneficiary | Effort | Impact | Why It Matters |
|---|---|---|---|---|
| Homeowner accounts (login, history, saved tradies) | Visitor | H | H | Unlocks retention, personalisation, and review gating by verified homeowner |
| Insurance certificate upload + "Insured" badge | Both | M | H | Completes the trust trifecta: licence + insurance + reviews |
| Job pipeline tracker (Kanban: lead → invoiced) | Tradie | M | H | Gives tradies a full business management tool — daily login driver |
| Invoice generation from quote | Tradie | M | H | Closes the admin loop — win job → build invoice → send → get paid, all in TradieTools |
| Proposal builder (professional homeowner-facing proposal) | Both | H | H | Helps tradies win more jobs, gives homeowners structured comparison |
| Competitor benchmarking in analytics | Tradie | M | M | "You rank #3 of 12 Auckland plumbers" — clearest possible ROI message |
| Homeowner-posted jobs (reverse marketplace) | Both | H | H | Flips the model — tradies browse homeowner jobs and apply; higher quality matching |
| Business tier ($99/mo) with team logins | Tradie | M | M | Captures multi-person operations currently paying Pro tier for single login |
| Auckland suburb-level pages (top 12 suburbs) | Visitor | M | H | 1.7m people in Auckland metro; suburb pages will rank and convert better than city pages |
| Tradie education hub (/for-tradies/) | Tradie | M | M | Content that ranks for tradie searches drives listing signups and retention |
| PGD Board verification (plumbers/gasfitters/drainlayers) | Both | M | H | Third most regulated trade in NZ after electricians and builders |
| ROI/earnings tracker in Pro dashboard | Tradie | L | H | Makes the case for staying on Pro tier automatically — show them the dollar value |
| Tool/supply affiliate links in cost guides | Visitor | L | M | Passive revenue from content — Mitre 10, Placemakers, Bunnings affiliates |
| Lead credit system (à la carte for free tier) | Tradie | M | M | Reduces barrier to entry for tradies not ready for monthly subscription |
| Google review syndication partnership | Both | H | H | No Cowboys' main differentiator — getting TradieTools reviews to appear in Google Business Profiles |

---

*TradieTools Product Strategy — June 2026*
*Next review: September 2026 or after reaching 500 active listings, whichever comes first.*
