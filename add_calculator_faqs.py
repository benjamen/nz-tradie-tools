#!/usr/bin/env python3
"""Add faqs: YAML frontmatter to all calculator .md files."""
import os, re

CALC_DIR = "content/calculators"

FAQS = {
"acc-levy-calculator.md": [
    {"q": "How is ACC levy calculated for self-employed NZ tradies?", "a": "Self-employed tradies pay ACC based on their liable earnings (net profit up to the maximum) multiplied by their industry levy rate. The 2024–25 working safer levy is $0.08 per $100 plus a trade-specific earners' levy, totalling roughly $1.39–$2.80 per $100 for most trades."},
    {"q": "What is the ACC earners' levy rate in New Zealand?", "a": "For 2024–25 the earners' levy is $1.39 per $100 of liable earnings, paid by all NZ earners. Self-employed people also pay a work levy set by their industry classification."},
    {"q": "Is ACC levy tax-deductible for NZ sole traders?", "a": "Yes. The work portion of your ACC levy is fully tax-deductible as a business expense. The earners' levy portion is not deductible."},
    {"q": "What is the maximum liable earnings for ACC?", "a": "The maximum liable earnings for 2024–25 is $142,283. ACC levies are only charged on income up to this threshold."},
],
"apprentice-wage-calculator.md": [
    {"q": "What is the minimum wage for NZ apprentices in 2025?", "a": "From 1 April 2025, the adult minimum wage in NZ is $23.15/hr. Apprentices aged 16–17 may be paid the starting-out wage of $18.52/hr for the first 200 hours or three months, whichever comes first."},
    {"q": "Do apprentices get the same pay as qualified tradies in NZ?", "a": "No. Apprentice pay is negotiated between employer and apprentice but must meet minimum wage. Industry guides suggest a progression from around 50–60% of a qualified rate in year 1 rising to 80–90% by year 3–4."},
    {"q": "Are apprentice wages tax-deductible for a tradie business?", "a": "Yes, all wage payments including apprentice wages are fully deductible as a business expense in NZ."},
    {"q": "How does a Managed Apprenticeships training contract affect wages?", "a": "Under BCITO or other ITOs, the training agreement sets minimum pay bands. These are minimums only — employers can and often do pay more, especially for experienced apprentices."},
],
"bathroom-renovation-calculator.md": [
    {"q": "How much does a bathroom renovation cost in New Zealand?", "a": "A basic NZ bathroom refresh costs $8,000–$15,000. A mid-range renovation with new fittings and tiling runs $15,000–$30,000. A full luxury bathroom with underfloor heating and high-end fixtures can reach $50,000+."},
    {"q": "Do I need a building consent for a bathroom renovation in NZ?", "a": "Replacing like-for-like fittings does not require consent. Moving plumbing, adding a bedroom, or altering structural elements does require a building consent from your local council."},
    {"q": "How long does a bathroom renovation take in NZ?", "a": "A standard bathroom renovation typically takes 1–3 weeks once materials are on site. Delays from council consent, tile lead times, or specialist trades (e.g. waterproofing inspections) can extend this."},
    {"q": "What is the biggest cost in a bathroom renovation?", "a": "Labour is typically the biggest single cost, often 40–50% of total budget. Tiling, plumbing, and waterproofing are the most labour-intensive parts. Premium fixtures and fittings can also push costs up quickly."},
],
"breakeven-calculator.md": [
    {"q": "How do I calculate breakeven for my tradie business?", "a": "Breakeven = Fixed Costs ÷ Gross Margin %. If your monthly fixed costs are $5,000 and your gross margin is 40%, you need $12,500 in revenue to break even. Any revenue above that is profit."},
    {"q": "What counts as a fixed cost for a NZ tradie?", "a": "Fixed costs are expenses that don't change with job volume: insurance, vehicle registration, phone plan, accounting fees, tool finance repayments, and rent for a workshop or yard."},
    {"q": "What is a good gross margin for a NZ tradie business?", "a": "Most NZ tradie businesses target 35–55% gross margin (revenue minus direct job costs, before overheads). Electricians and plumbers typically achieve 40–50%; painters and decorators often see 30–40%."},
    {"q": "Why is knowing my breakeven important?", "a": "Knowing your breakeven tells you the minimum revenue you must generate to cover all costs. It helps you price jobs correctly, set sales targets, and know when you can safely hire another person."},
],
"brick-block-calculator.md": [
    {"q": "How many bricks do I need per square metre in NZ?", "a": "Standard NZ metric bricks (230×110×76 mm) laid in a single-skin stretcher bond require approximately 50 bricks per m². Add 5–10% for cuts and wastage."},
    {"q": "How many concrete blocks per square metre?", "a": "Standard 390×190×190 mm hollow concrete blocks require approximately 12.5 blocks per m² of single-skin wall. Add 5% wastage for cuts."},
    {"q": "How much mortar do I need for bricklaying?", "a": "A rough rule is 1 bag of cement (20 kg) per 70–80 bricks. A standard mix is 1 part cement to 5–6 parts sand by volume. Always allow 10% extra for waste."},
    {"q": "Can I use brick calculators for a retaining wall?", "a": "Yes, but retaining walls need engineering sign-off for heights above 1.5 m in NZ (or lower if surcharge loads apply). The block count calculation is the same; the footing and reinforcing design is additional."},
],
"building-consent-fee-calculator.md": [
    {"q": "How much does a building consent cost in NZ?", "a": "Fees vary by council and project value. As a guide, a $150,000 residential project typically attracts $1,500–$3,500 in council consent fees, plus $150 (MBIE) and $150 (BRANZ) levies."},
    {"q": "How is the MBIE building levy calculated?", "a": "The MBIE levy is $1.75 per $1,000 of project value (on projects over $65,000). So a $200,000 project pays $350 in MBIE levy."},
    {"q": "Do I need a building consent for a deck in NZ?", "a": "Decks under 1.5 m above ground and under 20 m² may be exempt from consent. Larger decks, or those attached to the house structure, generally require consent. Check with your local council."},
    {"q": "What is the BRANZ levy?", "a": "The BRANZ levy is $1.00 per $1,000 of project value for projects over $20,000. It funds building research in NZ. It is paid alongside the MBIE levy when lodging a building consent."},
],
"cable-sizing-calculator.md": [
    {"q": "How do I size electrical cable in NZ?", "a": "Cable sizing in NZ follows AS/NZS 3008. Key factors are: load current (amps), cable installation method, ambient temperature, and permissible voltage drop (typically 5% for final subcircuits). Always consult a licensed electrician."},
    {"q": "What cable size is needed for a 20-amp circuit?", "a": "A 20 A circuit in a typical residential installation (clipped direct, 30°C ambient) generally uses 2.5 mm² twin-and-earth cable. Longer runs or higher ambient temperatures may require 4 mm²."},
    {"q": "What is the maximum voltage drop allowed in NZ?", "a": "AS/NZS 3000:2018 allows a maximum of 5% voltage drop from the supply point to any point of use for lighting and power circuits in NZ installations."},
    {"q": "Do I need a licensed electrician to size cables in NZ?", "a": "All electrical work in NZ must be carried out and certified by a licensed electrical worker (LEW). Cable sizing is part of that design work and must comply with AS/NZS 3008 and the NZ Electrical Code of Practice."},
],
"carpet-flooring-calculator.md": [
    {"q": "How much carpet do I need per square metre in NZ?", "a": "Measure the room's length × width in metres. Add 10–15% for cuts, pattern matching, and doorway wastage. Most NZ carpet comes in 3.66 m or 4 m widths, so room shape affects offcuts."},
    {"q": "How much does carpet installation cost in NZ?", "a": "Carpet supply and install in NZ typically costs $45–$120/m² depending on carpet quality and underlay. Budget $65–$85/m² for a good mid-range carpet with 10 mm underlay fitted."},
    {"q": "What underlay should I use under carpet in NZ?", "a": "An 8–10 mm polyurethane or rubber crumb underlay (rated 150 kg/m³ or above) is standard for residential carpet in NZ. Thicker underlay (12 mm) adds comfort but is not always needed."},
    {"q": "How do I calculate staircase carpet in NZ?", "a": "Measure each step: tread depth + riser height × width, then multiply by number of steps. Add 15% wastage for cutting around spindles. A standard NZ staircase of 14 steps uses roughly 5–7 m² of carpet."},
],
"cash-flow-forecast.md": [
    {"q": "How do I do a cash flow forecast for my tradie business?", "a": "List all expected income by week or month (jobs invoiced, deposits received). Then list all expected outgoings (wages, materials, insurance, ACC, GST payments). The difference each period is your net cash position."},
    {"q": "How far ahead should I forecast cash flow?", "a": "Most small tradie businesses forecast 3–6 months ahead. This is far enough to spot cash shortfalls before they hit, but close enough that numbers remain useful. Update it monthly."},
    {"q": "What causes cash flow problems for NZ tradies?", "a": "The most common causes are: slow-paying clients (30–60 day terms), GST and provisional tax not set aside, uneven work flow (feast and famine), and materials costs paid before jobs are invoiced."},
    {"q": "How can I improve cash flow as a tradie?", "a": "Require a deposit upfront (20–30%), invoice immediately on job completion, offer payment by credit card, chase overdue invoices within 7 days, and hold a GST reserve account separate from operating funds."},
],
"cladding-paint-calculator.md": [
    {"q": "How much paint do I need for weatherboard cladding in NZ?", "a": "A standard 10 m × 2.4 m weatherboard wall (24 m²) needs roughly 3–4 litres of paint per coat at 8–10 m²/L spread rate. Two coats = 6–8 litres. Add 10% for waste and overruns."},
    {"q": "How many coats of paint does exterior cladding need in NZ?", "a": "Bare or repainted timber cladding typically needs 1 coat of primer + 2 topcoats. Previously painted cladding in good condition may need only 2 topcoats. Always follow the paint manufacturer's data sheet."},
    {"q": "What exterior paint is best for NZ weatherboards?", "a": "Water-based acrylic paints are the standard for NZ weatherboards — they flex with timber movement and resist the UV and moisture of NZ's climate. Look for products rated for NZ exterior conditions with a 10+ year durability claim."},
    {"q": "How much does exterior painting cost per square metre in NZ?", "a": "Exterior painting in NZ typically costs $15–$35/m² for labour only, or $25–$50/m² supply and apply. High multi-storey homes, complex profiles, or significant prep work push costs higher."},
],
"concrete-calculator.md": [
    {"q": "How much concrete do I need for a 100 mm slab in NZ?", "a": "Volume = length × width × 0.1 m. For a 6 m × 4 m slab at 100 mm thick: 6 × 4 × 0.1 = 2.4 m³. Always order 5–10% extra for sub-base variation and spillage."},
    {"q": "How much does concrete cost per cubic metre in NZ?", "a": "Ready-mix concrete in NZ costs approximately $200–$260/m³ for standard 25 MPa residential mix, delivered. Prices vary by region and supplier — rural areas typically pay more for delivery."},
    {"q": "What strength concrete do I need for a NZ house slab?", "a": "NZS 3109 specifies minimum 17.5 MPa for concrete in contact with the ground, but 25 MPa is the standard residential specification in NZ. Driveways and heavier loads may require 30 MPa."},
    {"q": "Do I need reinforcing steel in a concrete slab in NZ?", "a": "Most NZ residential slabs require steel reinforcing mesh (usually H8 mesh at 200 mm centres) or steel fibre to control cracking and meet NZS 3604 or engineer-specific requirements."},
],
"contractor-vs-employee-calculator.md": [
    {"q": "Is it better to be a contractor or employee as a tradie in NZ?", "a": "Contractors often earn a higher gross rate but pay their own ACC, tax, and have no paid leave. Employees receive holiday pay, sick leave, and KiwiSaver employer contributions. The calculator helps compare true net take-home."},
    {"q": "What is a contracting premium over employment in NZ?", "a": "A typical contracting premium is 20–30% above equivalent employment rates to compensate for no paid leave, no employer KiwiSaver, and self-funded ACC and insurance. Below 15% premium, employment is usually better financially."},
    {"q": "Can a tradie be forced to be a contractor instead of an employee in NZ?", "a": "No. The Employment Relations Act 2000 uses a 'real nature of the relationship' test. If you work exclusively for one party under their direction, you may be legally an employee regardless of the written contract label."},
    {"q": "What taxes does a self-employed contractor pay in NZ?", "a": "Contractors pay income tax (via provisional tax or schedular payments), ACC earners' and work levies, and GST if turnover exceeds $60,000/year. No employer KiwiSaver contribution is received."},
],
"decking-calculator.md": [
    {"q": "How much timber do I need for a 20 m² deck in NZ?", "a": "A 20 m² deck using 140×45 mm decking boards at 5 mm gaps needs approximately 140 running metres of decking (about 28 × 5.1 m lengths). Add 10% for end cuts and wastage."},
    {"q": "How much does a deck cost to build in NZ?", "a": "A simple ground-level treated pine deck in NZ costs approximately $800–$1,400/m² supply and install. A composite or hardwood deck with stairs and handrails can reach $1,800–$3,000/m²."},
    {"q": "Do I need a building consent for a deck in NZ?", "a": "Decks less than 1.5 m above ground and under 20 m² are typically exempt from building consent. Decks attached to a dwelling, above 1.5 m, or over 20 m² generally require consent from your local council."},
    {"q": "What timber treatment is needed for NZ outdoor decking?", "a": "NZS 3602 requires H3.2 preservative-treated timber for decking in NZ (above ground, exposed). For areas in contact with ground or water, H4 or H5 treatment is required."},
],
"depreciation-calculator.md": [
    {"q": "How does tax depreciation work for tradies in NZ?", "a": "The IRD allows you to deduct the depreciation of business assets over their useful life. For tools and equipment you can use the diminishing value (DV) or straight-line (SL) method based on IRD-set rates."},
    {"q": "Can I write off tools immediately in NZ?", "a": "Yes. Assets costing $1,000 or less (excluding GST) can be written off immediately as a low-value asset deduction. From 17 March 2021 this threshold increased from $500 to $1,000."},
    {"q": "What is the depreciation rate for a ute in NZ?", "a": "The IRD depreciation rate for a light commercial vehicle (ute) is 30% DV or 21% SL. So a $40,000 ute depreciates by $12,000 DV in year 1, $8,400 in year 2, and so on."},
    {"q": "Do I claim depreciation on tools I also use personally?", "a": "You can only claim the business-use portion. If a tool is used 80% for work and 20% personally, you claim 80% of the depreciation. Keep a usage log if the split is likely to be questioned."},
],
"drain-grade-calculator.md": [
    {"q": "What is the minimum fall for a drain in NZ?", "a": "NZS 3114 and the NZ Building Code require a minimum grade of 1:60 (1.67%) for 100 mm wastewater drains. Larger drains (150 mm+) may use 1:100, while very small drains (75 mm) should be 1:40 or steeper."},
    {"q": "How do I calculate drain fall in millimetres?", "a": "Multiply run length by the grade fraction. For 10 m of drain at 1:60: 10,000 mm ÷ 60 = 167 mm fall. The downstream invert should be 167 mm lower than the upstream invert."},
    {"q": "What pipe slope is needed for a 150 mm stormwater drain?", "a": "A 150 mm stormwater pipe typically uses a minimum grade of 1:100 (1%) or 10 mm per metre. Check with your local council — some require steeper grades in areas with high sediment load."},
    {"q": "Can a drain be too steep in NZ?", "a": "Yes. Overly steep drains can allow water to run faster than solids, leaving blockages. As a general rule, grades steeper than 1:10 for wastewater require specialist design consideration."},
],
"earthworks-calculator.md": [
    {"q": "How much does earthworks cost per cubic metre in NZ?", "a": "General earthworks in NZ costs $25–$80/m³ cut and fill, depending on soil type, access, and distance to disposal. Rocky ground can reach $150–$250/m³. Offsite disposal adds tip fees of $80–$120/m³."},
    {"q": "What is swell factor in earthworks?", "a": "When soil is excavated, it expands in volume (swell). Clay expands by 20–35%, gravel by 10–15%. So 100 m³ of in-situ clay becomes approximately 125–135 m³ of loose material for trucking."},
    {"q": "Do I need a resource consent for earthworks in NZ?", "a": "Most councils require resource consent for earthworks exceeding certain thresholds — typically 200–500 m³ or more than 1 m depth, or if near waterways or steep slopes. Check your district plan."},
    {"q": "How do I convert earthworks between cubic metres and tonnes?", "a": "Average NZ soil weighs 1.4–1.8 tonnes/m³ (bulk). A common conversion is 1.6 t/m³. So 100 m³ of general fill = about 160 tonnes. Sandy soil is lighter; heavy clay is heavier."},
],
"employee-total-cost-calculator.md": [
    {"q": "What does it really cost to employ a tradie in NZ?", "a": "On top of wages, an employer pays: employer KiwiSaver (3%), ACC employer levy (varies by industry, typically 0.2–1%), annual leave loading (effectively 8%), and any tools, phone, or vehicle costs. Total true cost is often 15–25% above the gross wage."},
    {"q": "What is the employer KiwiSaver contribution rate in NZ?", "a": "Employers must contribute a minimum of 3% of an employee's gross wages to KiwiSaver. This is paid on top of the employee's wage and is a compulsory cost."},
    {"q": "How much annual leave does an NZ employee get?", "a": "All NZ employees are entitled to 4 weeks' annual leave per year under the Holidays Act 2003. This equates to 8% of gross earnings as a leave reserve."},
    {"q": "What ACC costs does an NZ employer pay?", "a": "Employers pay an ACC work levy based on their industry classification and payroll. Rates for 2024–25 range from about $0.18 to $3.00 per $100 of payroll depending on trade risk. Builders are around $0.90–$1.50/100."},
],
"equipment-finance-calculator.md": [
    {"q": "How do I calculate repayments on a tradie equipment loan?", "a": "Monthly repayment = P × [r(1+r)^n] ÷ [(1+r)^n – 1], where P = loan amount, r = monthly interest rate, n = number of months. For example, $30,000 at 8.5% over 5 years = $615/month."},
    {"q": "Should I buy or finance equipment as a NZ tradie?", "a": "Finance preserves cash flow and keeps capital working in the business. If equipment earns more than its finance cost, borrowing makes sense. If your business can buy outright without straining cash, that eliminates interest cost."},
    {"q": "Can I claim equipment loan repayments as a tax deduction in NZ?", "a": "You can claim the interest portion of loan repayments as a deduction, but not the principal. You also claim depreciation on the asset separately based on IRD depreciation rates."},
    {"q": "What is a balloon payment on equipment finance?", "a": "A balloon payment is a large lump sum due at the end of the loan term. It lowers monthly repayments during the loan but requires you to pay out, refinance, or return the asset at the end."},
],
"fence-calculator.md": [
    {"q": "How much fencing do I need per lineal metre in NZ?", "a": "Measure total fence line in metres. Standard paling fences use posts every 2.4–2.7 m. A 30 m fence needs roughly 12–13 posts. Rails, palings or battens, and fixings are then calculated off this."},
    {"q": "How much does a fence cost per metre in NZ?", "a": "A standard 1.8 m timber paling fence in NZ costs $90–$180/lm supply and install. A metal post-and-rail lifestyle fence is $100–$200/lm. Retaining fences with structural requirements can reach $300–$500/lm."},
    {"q": "Do I need council approval for a fence in NZ?", "a": "Fences up to 2 m high are generally permitted without resource consent. Fences on boundary or over 2 m often require neighbour agreement and council consent. Retaining fences over 1 m usually need a building consent."},
    {"q": "What timber treatment is needed for NZ fence posts?", "a": "Posts in-ground require H5 treatment (CCA-treated). Rails and battens above ground require H3.2. Using the correct hazard class is mandatory under NZS 3602."},
],
"gst-calculator.md": [
    {"q": "What is the GST rate in New Zealand?", "a": "GST in New Zealand is 15%, applied to most goods and services. It was increased from 12.5% to 15% in October 2010."},
    {"q": "How do I add GST to a price in NZ?", "a": "Multiply the GST-exclusive price by 1.15. For example, $500 + GST = $500 × 1.15 = $575. To find the GST amount only: $500 × 0.15 = $75."},
    {"q": "How do I remove GST from a price in NZ?", "a": "Divide the GST-inclusive price by 1.15. For example, $575 ÷ 1.15 = $500 (GST-exclusive). The GST component is $575 − $500 = $75, or equivalently $575 × 3/23 = $75."},
    {"q": "When do I need to register for GST in NZ?", "a": "You must register for GST if your turnover exceeds (or will exceed) $60,000 in any 12-month period. You can register voluntarily below this threshold. Most tradie businesses should register once they start earning consistently."},
    {"q": "How often do I file a GST return in NZ?", "a": "Most small businesses file GST returns every 2 months (bi-monthly). Businesses with turnover under $500,000 can apply for 6-monthly filing. Large businesses (turnover over $24 million) file monthly."},
],
"h1-insulation-calculator.md": [
    {"q": "What R-value do I need under NZ Building Code H1?", "a": "H1 5th edition (from 2023) sets zone-dependent minimum R-values. Auckland (Zone 1) requires R2.9 underfloor, R6.6 ceiling. Queenstown (Zone 6) requires R3.6 underfloor, R9.6 ceiling. Walls range R2.0–R2.8 by zone."},
    {"q": "Which NZ climate zone am I in for insulation?", "a": "NZ has 6 climate zones. Zone 1 covers Northland and Auckland; Zone 2 Waikato to Bay of Plenty; Zone 3 Hawke's Bay and Taranaki; Zone 4 Wellington and Nelson; Zone 5 inland South Island; Zone 6 alpine areas including Queenstown and Wanaka."},
    {"q": "Does H1 5th edition apply to renovations?", "a": "H1 5th edition applies to new builds consented after its adoption date. Renovations that alter the building envelope (e.g. reroofing, new exterior cladding) generally trigger the current H1 requirements for the altered areas."},
    {"q": "How do I meet H1 requirements in my wall assembly?", "a": "Typical NZ wall assemblies meet H1 using a combination of framing R-value (timber), bulk insulation batt R-value, and sometimes external rigid foam insulation. The total system R-value must meet or exceed the zone minimum."},
],
"healthy-homes-cost-estimator.md": [
    {"q": "What are the NZ Healthy Homes Standards for rental properties?", "a": "The five Healthy Homes Standards require landlords to provide: adequate heating (heat pump or equivalent), ceiling and underfloor insulation to H1 spec, effective ventilation (extractor fans), draught stopping, and moisture ingress prevention."},
    {"q": "When do Healthy Homes Standards apply in NZ?", "a": "From 1 July 2024, all private rental properties must comply with all five Healthy Homes Standards. Landlords who don't comply face fines of up to $7,200 per breach."},
    {"q": "How much does it cost to comply with Healthy Homes Standards?", "a": "Average compliance cost for a typical NZ rental property is $3,000–$8,000. Properties needing a new heat pump ($2,000–$5,000), full insulation ($2,000–$4,000), and extractor fans ($300–$600) are at the upper end."},
    {"q": "What heating is required under NZ Healthy Homes?", "a": "The heating standard requires a fixed heater capable of heating the main living room to at least 18°C on the coldest days. A heat pump is the most common solution — it must be sized correctly using the MBIE heating assessment tool."},
],
"heat-pump-sizing-calculator.md": [
    {"q": "How do I size a heat pump for a NZ room?", "a": "MBIE's formula: kW required = room volume (m³) × climate factor ÷ 10. A 45 m² living room (2.4 m ceiling = 108 m³) in Auckland needs about 2.7 kW. Add 20% for older, poorly insulated homes."},
    {"q": "What size heat pump do I need for a NZ house?", "a": "A typical NZ 3-bedroom home needs a 5–7 kW heat pump for the living area, or a multi-split system to cover multiple rooms. Larger homes in cold regions (Zones 5–6) may need 8–12 kW capacity."},
    {"q": "What is the EECA heat pump sizing calculator?", "a": "EECA (Energy Efficiency and Conservation Authority) provides a free online tool to size heat pumps for Healthy Homes compliance. It considers floor area, insulation, climate zone, and window area."},
    {"q": "Does heat pump size affect Healthy Homes compliance?", "a": "Yes. Under the Healthy Homes heating standard, the heat pump must be sized using the MBIE assessment method to verify it can achieve 18°C in the main living room. An undersized unit does not comply."},
],
"holiday-pay-calculator.md": [
    {"q": "How is holiday pay calculated in NZ?", "a": "Under the Holidays Act 2003, annual holiday pay is the greater of: (a) ordinary weekly pay (OWP) at the time of leave, or (b) average weekly earnings (AWE) over the previous 12 months. Most modern payroll software calculates this automatically."},
    {"q": "What is 8% holiday pay in NZ?", "a": "8% is the minimum holiday pay entitlement as a percentage of gross earnings (representing 4 weeks of a 52-week year). It is used when an employee agrees to have holidays paid out, or for casual workers per pay period."},
    {"q": "Can NZ employees cash up annual leave?", "a": "Yes. Employees can cash up one week of their 4-week annual leave entitlement per year, if the employer agrees. The remaining 3 weeks must be taken as actual leave."},
    {"q": "How much notice do I need to give before taking annual leave in NZ?", "a": "There is no specific minimum notice period in law, but employers and employees should agree on leave timing. Employers can also direct employees to take leave with 14 days' notice if this is reasonable."},
],
"hot-water-cylinder-calculator.md": [
    {"q": "What size hot water cylinder do I need in NZ?", "a": "A common rule is 45–55 litres per person. So a household of 4 needs a 180–220 litre cylinder. Large families, frequent bathers, or high hot water demand may need 250–300 litres."},
    {"q": "Does a hot water cylinder need Healthy Homes compliance?", "a": "Healthy Homes Standards do not directly regulate hot water systems in rentals. However, the hot water cylinder must have a functioning pressure relief valve and comply with NZOSHA and plumbing regulations."},
    {"q": "What temperature should a hot water cylinder be set to in NZ?", "a": "NZS 4305 recommends storing hot water at 60°C minimum to prevent Legionella bacteria growth. Tempering valves are required at point-of-use for showers to limit temperature to 45°C for safety."},
    {"q": "Should I get a heat pump hot water system in NZ?", "a": "Heat pump water heaters are 3–4× more energy efficient than electric resistance elements and can reduce water heating costs by 60–70%. EECA estimates payback of 3–5 years at current power prices in NZ."},
],
"hourly-rate-calculator.md": [
    {"q": "How do I calculate my hourly rate as a self-employed NZ tradie?", "a": "Add up all annual costs: wages target + ACC + insurance + vehicle + tools + overheads. Divide by your billable hours per year (typically 1,200–1,400 for a sole trader). Add your profit margin on top."},
    {"q": "What is a fair hourly rate for a NZ tradesperson in 2025?", "a": "Typical NZ tradie rates in 2025: electricians $100–$130/hr, plumbers $110–$150/hr, builders $90–$120/hr, painters $60–$90/hr. Rates vary by region — Auckland and Wellington are generally 10–20% higher."},
    {"q": "How many billable hours can a NZ sole trader charge per year?", "a": "A NZ sole trader working 46 weeks (52 minus 4 weeks leave and 2 weeks public holidays) with 8-hour days has around 1,840 potential hours. After travel, quoting, admin and downtime, realistic billable hours are 1,200–1,500/year."},
    {"q": "Should I charge GST on top of my hourly rate?", "a": "If you are GST-registered, yes — you add 15% GST on top of your rate when invoicing. Your quoted rate may be shown ex-GST or inc-GST; be clear with clients which you are quoting."},
],
"insulation-calculator.md": [
    {"q": "How much ceiling insulation do I need in NZ?", "a": "Measure your ceiling area in m². Add 10% for waste and overlaps. Standard NZ pink batts come in 580 mm or 430 mm widths to fit between joists at 600 mm or 450 mm centres respectively."},
    {"q": "What thickness of insulation do I need in my NZ ceiling?", "a": "H1 5th edition requires R6.6 in ceiling for Auckland/Bay of Plenty and up to R9.6 for alpine zones. A 240 mm glasswool batt gives roughly R6.0, while polyester or higher-density glasswool can achieve R6.6+ in 220–240 mm."},
    {"q": "Does underfloor insulation need vapour barrier in NZ?", "a": "In most NZ climates, a polythene vapour barrier on the ground (0.25 mm minimum) is recommended under the building to reduce ground moisture entering the subfloor space, particularly in zones with high rainfall."},
    {"q": "Can I DIY insulation in NZ?", "a": "Glasswool and polyester ceiling batts can be installed by homeowners in NZ without a licensed contractor. Underfloor insulation installation (particularly polyester wrap systems) is also DIY-friendly. Spray foam insulation must be installed by a licensed applicator."},
],
"irrigation-calculator.md": [
    {"q": "How do I calculate how much water my garden or lawn needs in NZ?", "a": "Lawns need approximately 25 mm of water per week in warm weather. A 100 m² lawn needs 2,500 L/week. Multiply by your sprinkler flow rate to find run time. Vegetable gardens need 30–40 mm/week."},
    {"q": "What pipe size do I need for a garden irrigation system in NZ?", "a": "Typical residential irrigation uses 25 mm poly mainline for runs under 50 m, then 13–19 mm laterals to heads. For larger commercial or lifestyle blocks, 32–40 mm mains may be needed. Always size for pressure losses at design flow."},
    {"q": "Does irrigation work in NZ need council approval?", "a": "Large-scale irrigation (farming or commercial horticultural) may require a water permit under the RMA from your regional council. Residential garden irrigation generally does not require consent."},
    {"q": "What is the best time to run irrigation in NZ?", "a": "Early morning (4–7 am) is ideal — wind is low, evaporation is minimal, and foliage dries before evening reducing disease risk. Avoid midday irrigation as 30–40% of water can be lost to evaporation."},
],
"job-cost-calculator.md": [
    {"q": "How do I calculate the cost of a job as a NZ tradie?", "a": "Job cost = (hours × hourly rate) + materials cost + subcontractor costs + overhead allocation. Add your profit margin last. Always price from cost up, not from what you think the client will pay."},
    {"q": "What profit margin should a NZ tradie add to a job quote?", "a": "A minimum gross margin of 35–45% is typical for NZ trade businesses. Net profit after overheads should target 15–25%. Underpricing may win the job but erodes business viability over time."},
    {"q": "What should I include in a job quote in NZ?", "a": "A valid NZ job quote should include: scope of work, inclusions and exclusions, materials specification, labour hours or fixed price, GST status (+ GST or GST inclusive), payment terms, and expiry date of quote."},
    {"q": "How do I handle variation costs on a quoted job?", "a": "Issue a written variation order before doing extra work, outlining additional scope, cost, and effect on timeline. Under NZ contract law, variations not documented in writing are difficult to enforce as additional charges."},
],
"kitchen-renovation-calculator.md": [
    {"q": "How much does a kitchen renovation cost in NZ?", "a": "A basic kitchen update in NZ costs $10,000–$20,000. A mid-range renovation with new cabinetry, benchtop and appliances runs $20,000–$45,000. A full high-spec kitchen can cost $50,000–$100,000+."},
    {"q": "Does a kitchen renovation require a building consent in NZ?", "a": "Like-for-like replacement of cabinetry, benchtops, and appliances does not require consent. Moving plumbing, drainage, gas, or structural walls requires a building consent and appropriate licensed trades."},
    {"q": "How long does a kitchen renovation take in NZ?", "a": "Most kitchen renovations take 2–5 weeks once all materials are on site and trades are coordinated. Custom cabinetry can add 4–8 weeks of lead time from order to delivery."},
    {"q": "What adds the most value to a kitchen renovation in NZ?", "a": "Quality benchtops (stone or engineered stone), modern cabinetry, good lighting, and energy-efficient appliances add the most resale value. Quality plumbing fitments and good ventilation add practical long-term value."},
],
"kiwisaver-employer-cost-calculator.md": [
    {"q": "How much KiwiSaver does an employer pay in NZ?", "a": "Employers must pay a minimum of 3% of an employee's gross wages as a KiwiSaver employer contribution. This is in addition to the employee's own contribution and is not deducted from wages."},
    {"q": "What is ESCT and how does it work?", "a": "ESCT (Employer Superannuation Contribution Tax) is deducted from the employer's KiwiSaver contribution before it reaches the employee's account. The ESCT rate depends on the employee's annual salary: 10.5% up to $16,800, rising to 39% over $216,000."},
    {"q": "Is the employer KiwiSaver contribution tax-deductible?", "a": "Yes. Employer KiwiSaver contributions are a deductible business expense in NZ. The net cost after tax (at 28% company rate) is approximately 2.16% of payroll for a 3% contribution."},
    {"q": "Does an employer have to pay KiwiSaver for casual workers?", "a": "Employers must enrol employees who work 20+ hours/week unless the employee opts out within 8 weeks. Casual workers under 20 hours/week are not automatically enrolled but can opt in voluntarily."},
],
"labour-cost-calculator.md": [
    {"q": "How do I calculate total labour cost for a NZ construction job?", "a": "Total labour cost = number of workers × hours per worker × fully loaded hourly rate (including ACC, KiwiSaver, leave entitlement, and tool allowance). Always use fully loaded rates in quotes to avoid undercharging."},
    {"q": "What is a fully loaded labour rate in NZ?", "a": "A fully loaded rate includes: gross wage + employer KiwiSaver (3%) + ACC employer levy + holiday pay reserve (8%) + sick leave liability. For a worker on $40/hr, the fully loaded cost is approximately $47–$50/hr."},
    {"q": "How much should I charge for labour on a building project?", "a": "NZ building labour charge-out rates in 2025 range from $85–$130/hr for a licensed builder, $95–$140/hr for a licensed electrician or plumber, and $70–$100/hr for experienced carpenters or labourers."},
    {"q": "Can I claim labour costs as a business expense in NZ?", "a": "Yes. All wages, including your own PAYE wages if you are an employee of your own company, are fully deductible. Subcontractor payments are also deductible provided you hold a valid tax invoice."},
],
"leave-entitlements-calculator.md": [
    {"q": "How much annual leave is an NZ employee entitled to?", "a": "All employees in NZ are entitled to 4 weeks' annual leave per year under the Holidays Act 2003, after completing 12 months of continuous employment. After each additional 12 months, entitlement refreshes."},
    {"q": "How many sick days do NZ employees get?", "a": "Employees in NZ get 10 days' sick leave per year (after 6 months of employment), with up to 20 days able to be carried forward. The total sick leave balance cannot exceed 20 days at any one time."},
    {"q": "What public holidays are NZ employees entitled to?", "a": "NZ has 12 public holidays per year. Employees who would otherwise work on a public holiday are entitled to a paid day off and an alternative holiday if they do work. Provincial anniversaries are also recognised in each region."},
    {"q": "What is the difference between sick leave and bereavement leave in NZ?", "a": "Sick leave is for illness or injury. Bereavement leave provides 3 days for the death of a spouse, parent, child, sibling, or grandparent, and 1 day for other close relatives or people the employee had a close relationship with."},
],
"markup-margin-calculator.md": [
    {"q": "What is the difference between markup and margin?", "a": "Markup is profit as a percentage of COST. Margin is profit as a percentage of SELLING PRICE. A 50% markup on a $100 cost gives a $150 price. A 50% margin on $150 price gives $75 profit — these are very different numbers."},
    {"q": "What markup should a NZ tradie use for materials?", "a": "A common benchmark is 20–30% markup on materials (17–23% margin). This covers admin, procurement time, warranty risk, and waste. Some trades mark up specialty materials higher; consumables are often bundled into the hourly rate."},
    {"q": "How do I convert markup to margin?", "a": "Margin = Markup ÷ (1 + Markup). For a 40% markup: 0.40 ÷ 1.40 = 28.6% margin. To convert margin to markup: Markup = Margin ÷ (1 − Margin). For 30% margin: 0.30 ÷ 0.70 = 42.9% markup."},
    {"q": "Why do tradies need to know the difference between markup and margin?", "a": "Confusing markup and margin is one of the most common pricing errors in trade businesses. A tradie who adds 25% markup thinking it's a 25% margin is actually achieving only a 20% margin — and may not have enough to cover overheads."},
],
"materials-escalation-calculator.md": [
    {"q": "How much have building material costs increased in NZ?", "a": "NZ building material costs rose significantly in 2021–2023, with some materials (structural steel, timber, roofing) up 30–60%. By 2025, most categories have stabilised but remain 20–30% above 2019 levels."},
    {"q": "How do I allow for materials price escalation in a long project quote?", "a": "Add an escalation clause to quotes over 3 months: price materials at quote date and specify that materials will be invoiced at actual cost at time of purchase, or include a fixed escalation allowance of 3–8% per year."},
    {"q": "What is a price escalation clause in NZ construction contracts?", "a": "A price escalation clause (fluctuation clause) in an NZ construction contract allows the contract sum to be adjusted if material or labour costs change beyond an agreed threshold during the contract period. NZS 3910 includes a standard fluctuations provision."},
    {"q": "What materials are most volatile in NZ construction pricing?", "a": "Structural steel, copper (electrical and plumbing), timber, and insulation have historically been most volatile. Imported products (from China, US) are also subject to exchange rate movements."},
],
"overtime-calculator.md": [
    {"q": "Is overtime compulsory in NZ?", "a": "There is no statutory right to overtime in NZ employment law. Overtime terms are set in the employment agreement. However, if required to work overtime, the rate must be agreed (often time-and-a-half or double time)."},
    {"q": "What is time-and-a-half overtime pay in NZ?", "a": "Time-and-a-half means 1.5× the employee's regular hourly rate. If the ordinary rate is $30/hr, time-and-a-half is $45/hr. This is the most common NZ overtime rate for extra hours on weekdays."},
    {"q": "How is overtime taxed in NZ?", "a": "Overtime earnings are taxed as ordinary income under PAYE. The employer withholds PAYE at the employee's applicable tax rate (based on annual income). There is no special tax rate for overtime in NZ."},
    {"q": "What public holiday rates apply when employees work in NZ?", "a": "When an employee works on a public holiday that is also a day they would otherwise work, they must receive at least time-and-a-half pay plus an alternative holiday (time in lieu). Sunday rates are typically set by the employment agreement."},
],
"paint-calculator.md": [
    {"q": "How much paint do I need per square metre?", "a": "Most NZ interior paints cover 10–14 m² per litre (one coat). For a room with 40 m² of wall area, two coats needs 40 ÷ 12 × 2 = 6.7 litres. Always round up and buy the next litre up."},
    {"q": "How do I calculate paint for a room?", "a": "Calculate wall area: add all wall lengths × ceiling height. Subtract door (1.8 m²) and window (1.4 m²) areas. Divide by spread rate (from paint tin label) and multiply by number of coats. Add 10% extra for second-coat touch-ups."},
    {"q": "What paint should I use in a NZ bathroom?", "a": "Use a semi-gloss or gloss finish waterborne paint specifically rated for wet areas or bathrooms. Products with anti-mould or moisture-resistant formulation are recommended for high-humidity NZ bathrooms."},
    {"q": "How much does it cost to paint a house interior in NZ?", "a": "Professional interior painting in NZ costs approximately $20–$40/m² for walls and ceilings (2 coats, walls only). A typical 3-bedroom home with 250–300 m² of paintable surface costs $5,000–$12,000 fully painted."},
],
"paving-calculator.md": [
    {"q": "How much pavers do I need per square metre?", "a": "The number of pavers per m² depends on paver size. Standard 230×115 mm clay pavers laid in a running bond need about 38/m². 400×400 mm concrete pavers need about 6.25/m². Add 5–10% for cuts and waste."},
    {"q": "How deep should a paver base be in NZ?", "a": "For pedestrian areas, a compacted base of 100 mm AP20 (road metal) with 25–30 mm of compacted bedding sand is standard in NZ. For driveways and vehicle areas, increase base to 150–200 mm of compacted AP40."},
    {"q": "How much does paving cost per square metre in NZ?", "a": "Supply and lay of concrete block paving in NZ costs $80–$130/m² for straightforward residential areas. Natural stone or imported cobble sets can reach $150–$250/m². Complex patterns or tight access add cost."},
    {"q": "Do I need a building consent for a driveway in NZ?", "a": "Most residential driveways do not require a building consent but may need council approval for a vehicle crossing permit if connecting to a public road. Check with your local council before laying a new driveway."},
],
"paye-employee-calculator.md": [
    {"q": "How is PAYE calculated in NZ?", "a": "PAYE is calculated on an employee's gross pay using the applicable income tax rate for their annual income bracket. ACC earners' levy ($1.39/$100) is also deducted. The employer calculates and remits this to IRD on the employee's behalf."},
    {"q": "What are the NZ income tax rates for 2025?", "a": "2024–25 NZ income tax rates: 10.5% on $0–$14,000; 17.5% on $14,001–$48,000; 30% on $48,001–$70,000; 33% on $70,001–$180,000; 39% on income over $180,000."},
    {"q": "What is the student loan PAYE deduction rate in NZ?", "a": "Student loan repayments are deducted at 12 cents per dollar of gross earnings above the repayment threshold ($24,128 for 2024–25). Employees notify their employer via their tax code declaration (IR330)."},
    {"q": "What is a tax code in NZ and which one should I use?", "a": "Your tax code tells your employer which PAYE rate to use. 'M' is for your main/only job. 'S' is for secondary income. 'SH' and 'ST' are for higher secondary income. Use 'M SL' if you have a student loan on your primary job."},
],
"pool-volume-calculator.md": [
    {"q": "How do I calculate pool volume in NZ?", "a": "Rectangular pool: length × width × average depth. Circular pool: π × radius² × average depth. A 10 m × 4 m pool with 1.5 m average depth = 60 m³ = 60,000 litres."},
    {"q": "How much does a pool cost to install in NZ?", "a": "A fibreglass pool in NZ costs $35,000–$70,000 fully installed (pool, excavation, fence, pump, filtration). A concrete pool costs $60,000–$120,000+. Ongoing running costs are $2,000–$4,000/year."},
    {"q": "Does a pool need a fence in NZ?", "a": "Yes. All pools with water depth over 400 mm must be fenced to the Building Act 2004 and NZS 8500:2006 pool safety standard. The fence must have a self-closing, self-latching gate. Fines for non-compliance are up to $4,000."},
    {"q": "How much chlorine do I need for a NZ pool?", "a": "Maintain 1–3 ppm free chlorine in outdoor pools (NZRA guidelines). A 60 m³ pool needs approximately 60–180 g of granular chlorine per dose (weekly), adjusted by sun exposure and bather load."},
],
"provisional-tax-calculator.md": [
    {"q": "What is provisional tax in NZ?", "a": "Provisional tax is advance income tax paid during the year by NZ taxpayers whose residual income tax (RIT) exceeds $5,000. It avoids a large end-of-year tax bill by spreading payments across 3 instalments."},
    {"q": "How do I calculate NZ provisional tax using the standard method?", "a": "Standard uplift = prior year RIT × 1.05 (5% increase). This total is paid in 3 equal instalments: 28 August, 15 January, and 7 May (for 31 March balance date). If prior year RIT was $9,000, each instalment is $3,150."},
    {"q": "What is the safe harbour for NZ provisional tax?", "a": "If your RIT for the year is under $60,000 and you pay at least 100% of your prior year RIT (standard uplift without the 5%), you avoid use-of-money interest (UOMI) even if you underpay. This is the 'safe harbour' threshold."},
    {"q": "Can I use the estimation method for provisional tax?", "a": "Yes. If you expect your current-year income to differ significantly from last year's, you can estimate your RIT and pay based on that. However, if your estimate is too low, IRD may charge UOMI on the shortfall."},
    {"q": "When are provisional tax due dates in NZ?", "a": "For taxpayers with a 31 March balance date (most common): Instalment 1 is 28 August, Instalment 2 is 15 January, and Instalment 3 is 7 May of the following year."},
],
"provisional-tax-topup-calculator.md": [
    {"q": "What happens if I underpay provisional tax in NZ?", "a": "If you underpay provisional tax, IRD charges use-of-money interest (UOMI) on the underpaid amount at 10.39% per year from the date the payment was due. You may also face an underestimation penalty if using the estimation method."},
    {"q": "How can I top up provisional tax before year end in NZ?", "a": "Log in to myIR and make a voluntary payment at any time before your final instalment date or tax return due date. Label it as a provisional tax payment for the current tax year."},
    {"q": "What is the UOMI rate in NZ for underpaid provisional tax?", "a": "As of 2024–25, the UOMI rate charged by IRD on underpaid tax is 10.39% per annum. IRD also pays 3.53% UOMI to taxpayers on overpayments."},
    {"q": "Should I top up provisional tax now or wait until year end?", "a": "Topping up early reduces UOMI from the due date. If you're confident your year-end RIT will be higher than your instalments, making an early voluntary payment saves interest. Use your accounting software or tax agent to estimate the shortfall."},
],
"quote-builder-wizard.md": [
    {"q": "What should a NZ tradie quote include to be legally valid?", "a": "A NZ quote should include: your business name and NZBN/GST number, date and expiry, client details, detailed scope of work, inclusions and exclusions, total price (+ GST or GST incl), and payment terms."},
    {"q": "What is the difference between a quote and an estimate in NZ?", "a": "A quote is a fixed price offer. If accepted, you must complete the work at that price unless agreed variations arise. An estimate is an approximation and is not binding. Clients prefer quotes; courts distinguish between the two."},
    {"q": "How long should a tradie quote be valid for in NZ?", "a": "Most NZ tradies set a quote validity of 30–60 days. In periods of material price volatility, 14–30 days may be more appropriate. Always specify the expiry date on the quote document."},
    {"q": "Do I need to charge GST on quotes if I'm not yet GST-registered?", "a": "No. If you're not GST-registered, your quote is GST-exclusive and you should clearly state 'Not registered for GST' or 'No GST applicable'. Once you register, you must charge GST on all taxable supplies."},
],
"retaining-wall-calculator.md": [
    {"q": "Do I need a building consent for a retaining wall in NZ?", "a": "Retaining walls over 1.5 m high (or 1 m near a boundary or a structure) generally require a building consent in NZ. Some councils have lower thresholds. Always check with your local council before construction."},
    {"q": "What materials are used for retaining walls in NZ?", "a": "Common NZ retaining wall materials include: treated timber (H5), concrete block, Besser block, concrete poured in place, Keystone or Allan Block modular systems, and gabion baskets. Timber is common for heights under 1.2 m; engineered systems for taller walls."},
    {"q": "How much does a retaining wall cost per metre in NZ?", "a": "A basic timber retaining wall in NZ costs $300–$500/lm (up to 1 m high). Concrete block walls run $500–$900/lm. For walls over 1.5 m requiring engineering, expect $1,000–$2,000+/lm depending on height, fill, and access."},
    {"q": "How deep do retaining wall posts need to be in NZ?", "a": "As a rule of thumb, treated timber posts should be embedded to at least 1/3 of the exposed height (minimum 600 mm in solid ground). Engineer design typically specifies depth and post size based on soil pressure calculations."},
],
"retaining-wall-load-calculator.md": [
    {"q": "How do engineers calculate retaining wall loads in NZ?", "a": "Lateral earth pressure is calculated using the Rankine formula: Pa = ½ × Ka × γ × H². Ka (active pressure coefficient) depends on soil friction angle. For typical NZ soil with φ=30°, Ka ≈ 0.33. Add surcharge for loaded areas above the wall."},
    {"q": "When does a retaining wall need engineering in NZ?", "a": "Any retaining wall over 1.5 m or near a structure, boundary, or drainage requires engineering design and a building consent. Walls on soft ground, in seismic risk areas, or retaining saturated fill need specific engineering regardless of height."},
    {"q": "What is active earth pressure for a retaining wall?", "a": "Active earth pressure is the minimum lateral force a retained soil mass exerts on a retaining wall. It applies when the wall is free to tilt slightly away from the soil. Most retaining wall design uses active pressure as the design case."},
    {"q": "What surcharge load should I design a retaining wall for in NZ?", "a": "NZS 3604 recommends a minimum surcharge of 5 kPa for residential areas (e.g. foot traffic on soil above). Driveway or parking areas above a retaining wall typically use 10 kPa surcharge in NZ design practice."},
],
"retentions-calculator.md": [
    {"q": "What is a construction retention in NZ?", "a": "A retention is an amount (typically 5–10%) withheld from progress payments on construction contracts. It is held as security against defects and released at practical completion and/or end of defects liability period."},
    {"q": "What does the Construction Contracts Act 2002 say about retentions?", "a": "Under the CCA 2002 (as amended 2015), retention money held by a head contractor or commercial principal must be held on trust and not used for any other purpose. Trust account requirements apply to retentions over $20,000 per sub."},
    {"q": "When must retentions be released in NZ?", "a": "The release schedule is agreed in the contract. Typically 50% is released at practical completion and the remaining 50% at expiry of the defects liability period (usually 12 months after PC). CCA payment claim rules apply."},
    {"q": "What is the maximum retention percentage in NZ?", "a": "There is no statutory maximum, but 5% is the NZ standard. Some residential contracts use 10% for smaller sub-trades. Retentions above 10% are unusual and may be challenged as unreasonable under the CCA."},
],
"roof-area-calculator.md": [
    {"q": "How do I calculate roof area in NZ?", "a": "Measure the building footprint and multiply by a pitch factor. For a 15° pitch (standard NZ gable), pitch factor ≈ 1.04. For a 25° pitch, factor ≈ 1.10. Hip roofs add area for the hip sections. Valleys and dormers need individual calculation."},
    {"q": "How much does roofing cost per square metre in NZ?", "a": "Corrugated iron (Colorsteel) roofing in NZ costs $80–$140/m² supply and install. Concrete or clay tiles cost $100–$180/m². Membrane roofing for low-slope roofs costs $120–$250/m². Prices vary by region and roof complexity."},
    {"q": "How long does a roof last in NZ?", "a": "Steel roofing (Colorsteel, Zincalume) lasts 40–70 years in NZ. Concrete tiles last 50+ years. Corrugated iron without coating lasts 30–40 years in mild coastal climates; less in harsh salt air environments."},
    {"q": "Do I need a building consent to reroof in NZ?", "a": "A like-for-like reroof (same material, same pitch) is generally exempt from consent. Changing roofing material, pitch, or adding skylights/dormers requires a building consent from your local council."},
],
"scaffolding-calculator.md": [
    {"q": "How much scaffolding do I need for a typical NZ house?", "a": "A standard NZ single-storey 200 m² house perimeter (say 60 lm) needs approximately 4–6 bays of scaffolding per side for roof or cladding work. Two-storey houses require additional lift height. Scaffold calculators use lift height × bay width to determine material quantity."},
    {"q": "When is scaffolding required by law in NZ?", "a": "NZ WorkSafe requires fall protection (scaffolding, edge protection, or safety harness) for work at heights above 1.5 m on construction sites. For work at 3 m+ on residential buildings, edge protection is generally mandated on the eave line."},
    {"q": "How much does scaffolding hire cost in NZ?", "a": "Scaffolding hire in NZ typically costs $100–$200 per m² of access coverage per month for erected and dismantled scaffold. A standard residential job (40–60 m² of coverage) might cost $4,000–$10,000 for a 4–6 week hire period."},
    {"q": "What scaffolding standard applies in NZ?", "a": "NZ scaffold erection and use must comply with AS/NZS 4576:1995 (Guidelines for scaffolding) and the Health and Safety at Work Act 2015. Scaffolding over 5 m high is a 'notifiable work' category under HSWA."},
],
"scaffolding-hire-calculator.md": [
    {"q": "How much does scaffolding hire cost per week in NZ?", "a": "Residential scaffolding hire in NZ typically costs $150–$350 per week for a standard single-storey perimeter job. Two-storey and larger commercial jobs can cost $500–$2,000+/week depending on size and complexity."},
    {"q": "Is it cheaper to hire or buy scaffolding as a tradie in NZ?", "a": "For occasional use (less than 20 hire weeks per year), hiring is usually cheaper. Once you reach around 20+ weeks/year of need, owning becomes more cost-effective after factoring in storage, maintenance, and transport."},
    {"q": "What is included in scaffolding hire in NZ?", "a": "Most NZ scaffolding hire includes: delivery and pickup, erection and dismantling by a competent person, standard tubes and fittings, toe boards, and mesh or plank decking. Handrails, stair access towers, and sheeting are often extras."},
    {"q": "How long does it take to erect scaffolding in NZ?", "a": "A standard residential perimeter scaffold for a single-storey NZ house takes 1–2 days to erect. Two-storey homes take 2–3 days. Complex commercial scaffold can take a full week or more for large crews."},
],
"skip-bin-calculator.md": [
    {"q": "What size skip bin do I need for a renovation in NZ?", "a": "A 3 m³ skip suits a bathroom or kitchen renovation (1–2 tonnes of waste). A 6 m³ skip suits a mid-size renovation or small demolition. A 9–12 m³ skip is for large house renovations or roofing jobs. Volume and weight both matter."},
    {"q": "How much does a skip bin cost in NZ?", "a": "Skip bin hire in NZ costs approximately $250–$400 for a 2–3 m³ mini skip, $400–$600 for a 4–6 m³ skip, and $600–$1,000 for a 9–12 m³ large skip. Prices include delivery and pickup but not overfill or heavy material surcharges."},
    {"q": "Can concrete and bricks go in a skip bin in NZ?", "a": "Many skip providers in NZ do not accept heavy materials like concrete, bricks, or tiles in general waste skips due to weight limits. You may need a dedicated 'heavy waste' or 'concrete only' skip, which is priced separately."},
    {"q": "What is the NZ waste levy on skip bins?", "a": "The NZ Waste Minimisation Act levy is currently $60/tonne for waste disposed to landfill (2024). This levy is passed on to customers by skip bin operators and is included in most skip hire prices for mixed construction waste."},
],
"solar-savings-calculator.md": [
    {"q": "How much does a solar system cost in NZ in 2025?", "a": "A typical 5 kW residential solar system in NZ costs $10,000–$16,000 installed including inverter and racking. A 10 kW system costs $18,000–$28,000. Battery storage (10 kWh) adds $8,000–$15,000."},
    {"q": "How much solar power can I generate in NZ?", "a": "NZ annual solar irradiance averages 4–5 peak sun hours/day in most regions. A 5 kW system generates approximately 6,500–7,500 kWh/year. The South Island and areas with more cloud cover generate slightly less."},
    {"q": "What is the payback period for solar in NZ?", "a": "With power prices at 30–35c/kWh and export rates of 7–12c/kWh, a 5 kW system typically pays back in 8–12 years. Payback is faster if you use most power onsite rather than exporting."},
    {"q": "Can a NZ tradie install their own solar panels?", "a": "In NZ, electrical connection of solar systems must be done by a licensed electrical worker (LEW). Panel racking installation can be done by a builder or homeowner, but the electrical DC/AC connection and grid connection requires a LEW."},
],
"staircase-calculator.md": [
    {"q": "What are the code requirements for stair dimensions in NZ?", "a": "NZS 3604 and the NZ Building Code (Clause D1) require: maximum riser height 220 mm, minimum tread depth 250 mm, riser-to-tread formula: 2R + G = 600–700 mm. Handrails are required on all stairs over 4 risers."},
    {"q": "How many steps do I need for a 2.4 m floor-to-floor height?", "a": "At a comfortable 175 mm riser height: 2400 ÷ 175 = 13.7, round to 14 risers (steps). Tread depth would be 600 − (2 × 175) = 250 mm (minimum). Total stair run = 14 × 250 mm = 3,500 mm horizontal."},
    {"q": "Do stairs need a building consent in NZ?", "a": "Internal stair replacements that are like-for-like are exempt from consent. New stairs, stairs serving a new level, or stairs outside NZS 3604 parameters require a building consent."},
    {"q": "What timber is used for stairs in NZ?", "a": "Interior stairs use H1.2 or H3.1 treated pine or laminated timber for structural stringers. Treads are typically 44 mm dressed pine, hardwood, or engineered timber flooring glued and screwed. Hardwood treads are preferred for durability."},
],
"stormwater-grade-calculator.md": [
    {"q": "What is the minimum grade for a stormwater pipe in NZ?", "a": "NZS 3114 and the NZ Building Code require a minimum grade of 1:100 (1%) for 100 mm stormwater pipes. Larger pipes (150 mm+) may use 1:200 in some situations. Upsize the pipe for flat sites to maintain self-cleansing velocity."},
    {"q": "How do I calculate stormwater flow for a roof in NZ?", "a": "Rainfall intensity in NZ varies by region. As a guide, Auckland uses 150 mm/hr for a 10-year storm. Flow = area (m²) × intensity (mm/hr) ÷ 3,600. A 200 m² roof in Auckland at 150 mm/hr produces 8.3 L/s — requiring at least 100 mm pipe."},
    {"q": "What pipe material is used for stormwater in NZ?", "a": "Common NZ stormwater pipe materials: uPVC (NZS 7643), corrugated HDPE (flexible), or concrete (older/larger systems). uPVC is the standard for residential sub-100 mm drainage; HDPE is used for rural and flexible-layout situations."},
    {"q": "Does stormwater need to be diverted away from foundations in NZ?", "a": "Yes. The NZ Building Code Clause E1 requires buildings to be designed and built so that stormwater is managed to protect the building's structural performance. Surface drainage must direct water away from foundations."},
],
"subcontractor-tax-calculator.md": [
    {"q": "How is tax deducted for NZ subcontractors?", "a": "Subcontractors who perform labour in NZ may have schedular payments (withholding tax) deducted by the payer. The standard rate is 20% (15% if the sub gives an election). GST-registered subs can file to reduce or cease withholding."},
    {"q": "What is the NZ schedular payment tax rate for builders?", "a": "Most building and construction labour in NZ falls under the schedular payment regime. The default withholding rate is 20% of gross payment. Subcontractors can elect a lower rate (e.g. 15%) or apply to IRD for a special rate."},
    {"q": "Is withholding tax the same as income tax for subcontractors in NZ?", "a": "Withholding tax is an advance payment toward annual income tax. At year end, the sub files an income tax return and reconciles — if withholding tax paid exceeds their annual liability, they receive a refund; if underpaid, they pay the balance."},
    {"q": "Can a NZ subcontractor avoid withholding tax?", "a": "Yes. If the subcontractor is GST-registered, they can provide a certificate to the payer and elect not to have tax withheld. They are then responsible for paying provisional tax directly to IRD. Apply through your tax agent or myIR."},
],
"tile-calculator.md": [
    {"q": "How many tiles do I need per square metre?", "a": "Divide 1 m² by (tile length × tile width), including the grout joint. For 300×300 mm tiles with a 3 mm joint: 1 ÷ (0.303 × 0.303) ≈ 10.9 tiles/m². Always add 10% for cuts, 15% for diagonal laying."},
    {"q": "How much tile adhesive do I need?", "a": "Standard notched trowel application uses approximately 3–4 kg of adhesive per m². Large-format tiles (600+ mm) using the back-butter method may use 5–6 kg/m². A 20 kg bag covers about 4–6 m²."},
    {"q": "How much does tiling cost per square metre in NZ?", "a": "Professional tiling in NZ costs $60–$100/m² for labour only (floor tiles, straightforward room). Bathroom wall tiling or complex floor patterns (herringbone, diagonal) costs $80–$130/m² labour. Tile supply is additional."},
    {"q": "What grout joint size should I use for floor tiles?", "a": "NZ tile industry guidance: 2–3 mm for rectified tiles (machine-cut), 3–5 mm for standard tiles, 8–10 mm for irregular or natural stone. Wider joints accommodate variation in tile size and are easier to keep clean."},
],
"timber-framing-calculator.md": [
    {"q": "How much timber do I need for wall framing in NZ?", "a": "A standard NZ 90×45 mm wall frame at 600 mm stud centres uses approximately 1.7 linear metres of timber per m² of wall (top plate, bottom plate, studs, and nogs). Add 15% for waste and lintels."},
    {"q": "What is NZS 3604 framing?", "a": "NZS 3604 is the NZ Standard for light timber framing. It provides prescriptive design rules for residential and small commercial buildings without requiring a structural engineer — provided the building falls within defined limits of scope."},
    {"q": "What timber treatment is needed for NZ wall framing?", "a": "Internal wall framing requires H1.2 borate-treated timber in NZ (per NZS 3602). Exterior walls, floors on ground, and wet areas require H3.1 or H3.2. Ground contact requires H4 or higher."},
    {"q": "How do I calculate studs needed for a wall?", "a": "Number of studs = (wall length ÷ stud spacing) + 1, for a plain wall. Add extra studs for: corners (3 studs), T-junctions (3 studs), both sides of each door or window opening, plus trimmers and jack studs for each opening."},
],
"vehicle-mileage-calculator.md": [
    {"q": "What is the IRD mileage rate for NZ in 2025?", "a": "The IRD Tier 1 rate for the first 14,000 km of business travel per year is 73c/km for petrol or diesel vehicles in 2024–25. The Tier 2 rate for km above 14,000 is 21c/km. Electric vehicles use different rates."},
    {"q": "Can NZ tradies claim vehicle expenses or mileage?", "a": "Yes. You can either: (a) claim actual vehicle expenses (fuel, WOF, registration, insurance, loan interest) multiplied by business use %, or (b) use the IRD mileage rate for business km travelled. Most tradies use actual costs with a logbook."},
    {"q": "Do I need a logbook for vehicle expenses in NZ?", "a": "To claim actual vehicle expenses on a mixed-use vehicle, you need a logbook for 3 months every 3 years to establish the business vs private use percentage. The mileage rate method requires a record of business trips only."},
    {"q": "What vehicles qualify for the IRD mileage rate in NZ?", "a": "The IRD kilometre rate method applies to motor vehicles (including utes and vans). It is most suitable for low-km business use. Vehicles used predominantly for work (over 75% business) are often better treated as fully deductible business assets."},
],
"voltage-drop-calculator.md": [
    {"q": "What is voltage drop and why does it matter in NZ electrical installations?", "a": "Voltage drop is the reduction in voltage along a cable due to resistance. AS/NZS 3000:2018 limits voltage drop to 5% from the supply point to the point of use. Excessive voltage drop causes poor equipment performance and motor overheating."},
    {"q": "How do I calculate voltage drop for a NZ electrical circuit?", "a": "Vd = 2 × I × L × R/1000, where I = current (A), L = cable length (m), R = resistance of cable conductor (Ω/km from AS/NZS 3008). For a 20 A circuit, 30 m of 2.5 mm² cable: Vd = 2 × 20 × 30 × 7.41/1000 = 8.9 V (4.0% of 230 V)."},
    {"q": "When does voltage drop require upsizing the cable in NZ?", "a": "If calculated voltage drop exceeds 5% (11.5 V on a 230 V supply), you must use a larger cable cross-section. Increase to the next standard size (e.g. 2.5 mm² to 4 mm²) and recalculate until within limit."},
    {"q": "Does AS/NZS 3000 voltage drop apply to solar PV circuits in NZ?", "a": "Yes. DC wiring from solar panels to the inverter should also be designed for less than 3% voltage drop (some designers use 1–2%) to minimise energy losses. AC output circuits follow the standard 5% limit."},
],
"waterproofing-calculator.md": [
    {"q": "How much waterproofing membrane do I need for a NZ bathroom?", "a": "A typical 3 m² shower floor and 1.5 m high walls on 2 shower walls (3 m²) needs about 6–7 m² of membrane coverage total. Cartridge products cover 1–2 m²/L applied at 1 mm dry film thickness; allow 2 coats."},
    {"q": "What waterproofing is required under tiles in NZ?", "a": "NZS 4237 and the NZ Building Code Clause E3 require a waterproof membrane in all wet area floors and walls to a height of at least 1.5 m in showers, and 150 mm up walls in wet floors. This applies to all new tile installations in NZ."},
    {"q": "What types of waterproofing are used in NZ bathrooms?", "a": "Common NZ products: liquid-applied membrane (TPO or polyurethane — Laticrete, Ardex, Mapei), sheet membrane (torch-on for decks), and sheet-backed foam board (Wedi, Schluter Kerdi). Liquid-applied is most common for residential bathrooms."},
    {"q": "How long should waterproofing cure before tiling in NZ?", "a": "Liquid-applied membranes typically require 24–48 hours dry time between coats and a minimum 24 hours after the final coat before tiling. Always follow the manufacturer's data sheet — temperature and humidity affect cure times."},
],
}

def add_faqs_to_file(filepath, faqs):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if faqs already present
    if '\nfaqs:' in content or content.startswith('faqs:'):
        print(f"  SKIP (already has faqs): {os.path.basename(filepath)}")
        return

    # Find end of frontmatter (second ---)
    if not content.startswith('---'):
        print(f"  SKIP (no frontmatter): {os.path.basename(filepath)}")
        return

    end_fm = content.index('\n---\n', 3)  # find closing ---
    fm = content[:end_fm]
    rest = content[end_fm:]

    # Build YAML block
    lines = ['faqs:']
    for faq in faqs:
        q = faq['q'].replace("'", "''")
        a = faq['a'].replace("'", "''")
        lines.append(f"  - q: '{q}'")
        lines.append(f"    a: '{a}'")

    faq_block = '\n'.join(lines)
    new_content = fm + '\n' + faq_block + rest

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  OK: {os.path.basename(filepath)}")

print("Adding FAQs to calculator files...")
for filename, faqs in FAQS.items():
    filepath = os.path.join(CALC_DIR, filename)
    if os.path.exists(filepath):
        add_faqs_to_file(filepath, faqs)
    else:
        print(f"  NOT FOUND: {filepath}")

print(f"\nDone. Processed {len(FAQS)} calculators.")
