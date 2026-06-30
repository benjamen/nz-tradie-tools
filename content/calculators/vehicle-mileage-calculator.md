---
title: "IRD Kilometre Rate Calculator — NZ 2025–26"
seo_title: "Free IRD Kilometre Rate Calculator NZ 2025–26 — Mileage Claim"
description: "Free NZ IRD kilometre rate calculator for 2025–26. Enter your business km and vehicle type to get your exact Tier 1 / Tier 2 tax deduction. Updated rates."
tags: [vehicle, mileage, IRD, tax, calculator, NZ, kilometre rates]
author: "NZ Tradie Tools"
layout: calculator
date: 2026-06-30
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Income year</label>
      <select id="vy" onchange="calcMile()">
        <option value="2526" selected>2025–26 (current)</option>
        <option value="2425">2024–25</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Vehicle type</label>
      <select id="vtype" onchange="calcMile()">
        <option value="petrol" selected>Petrol or diesel</option>
        <option value="hybrid">Hybrid (petrol-electric)</option>
        <option value="electric">Electric</option>
      </select>
    </div>
    <div class="calc-group" style="grid-column:1/-1">
      <label>Total business kilometres driven this year</label>
      <input type="number" id="km" placeholder="e.g. 15000" oninput="calcMile()">
    </div>
    <div class="calc-group">
      <label>Your income tax rate</label>
      <select id="taxrate" onchange="calcMile()">
        <option value="0.17">17.5%</option>
        <option value="0.30" selected>30%</option>
        <option value="0.33">33%</option>
        <option value="0.39">39%</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="mile-result" style="display:none">
    <h3>Mileage Deduction Estimate</h3>
    <div class="result-row"><span>Income year</span><span id="m-year"></span></div>
    <div class="result-row"><span>Tier 1 (<span id="m-t1km"></span> km × <span id="m-t1rate"></span>)</span><span id="m-t1total"></span></div>
    <div class="result-row"><span>Tier 2 (<span id="m-t2km"></span> km × <span id="m-t2rate"></span>)</span><span id="m-t2total"></span></div>
    <div class="result-row"><span>Total deduction</span><span id="m-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Tax saved (at <span id="m-taxpct"></span>)</span><span id="m-tax"></span></div>
    <p id="m-note" style="font-size:.85rem;color:#555;margin-top:.75rem;line-height:1.5"></p>
  </div>
  <script>
  var RATES={
    '2526':{petrol:[1.04,0.35],hybrid:[0.83,0.20],electric:[0.09,0.09]},
    '2425':{petrol:[0.95,0.35],hybrid:[0.26,0.19],electric:[0.09,0.09]}
  };
  function nzd(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function calcMile(){
    var km=parseFloat(document.getElementById('km').value);
    var vy=document.getElementById('vy').value;
    var vt=document.getElementById('vtype').value;
    var tr=parseFloat(document.getElementById('taxrate').value);
    var res=document.getElementById('mile-result');
    if(!km||km<=0){res.style.display='none';return;}
    var rates=RATES[vy][vt];
    var t1r=rates[0], t2r=rates[1];
    var t1km=Math.min(km,14000), t2km=Math.max(0,km-14000);
    var t1total=t1km*t1r, t2total=t2km*t2r;
    var total=t1total+t2total;
    var yearLabel=vy==='2526'?'2025–26':'2024–25';
    document.getElementById('m-year').textContent=yearLabel;
    document.getElementById('m-t1km').textContent=t1km.toLocaleString();
    document.getElementById('m-t1rate').textContent='$'+t1r.toFixed(2);
    document.getElementById('m-t1total').textContent=nzd(t1total);
    document.getElementById('m-t2km').textContent=t2km.toLocaleString();
    document.getElementById('m-t2rate').textContent='$'+t2r.toFixed(2);
    document.getElementById('m-t2total').textContent=t2km>0?nzd(t2total):'—';
    document.getElementById('m-total').textContent=nzd(total);
    document.getElementById('m-taxpct').textContent=Math.round(tr*100)+'%';
    document.getElementById('m-tax').textContent=nzd(total*tr);
    var note=vt==='electric'
      ? 'Electric vehicles use a flat rate — no Tier 1/Tier 2 split. The rate ($0.09/km) covers electricity costs only; you claim actual depreciation and other costs separately if using the actual-cost method.'
      : km>14000
        ? 'You\'ve crossed the 14,000 km Tier 1 threshold. The higher Tier 1 rate covers fixed costs (depreciation, insurance, rego). Tier 2 covers fuel and running costs only. Keep a logbook of every business trip for IRD if audited.'
        : 'All your business km fall within the Tier 1 rate — you\'re claiming the full cost rate. Keep a record of each business trip: date, km, destination and purpose.';
    document.getElementById('m-note').textContent=note;
    res.style.display='block';
  }
  </script>

intro: |
  Calculate your IRD vehicle mileage deduction for the 2025–26 or 2024–25 income year. The calculator automatically applies the Tier 1 / Tier 2 split at 14,000 km and shows your estimated tax saving. Always confirm current rates at ird.govt.nz before filing.

faq:
  - q: "What are the IRD kilometre rates for 2025–26?"
    a: "The 2025–26 IRD kilometre rates are: petrol/diesel $1.04/km (Tier 1, first 14,000 km) and $0.35/km (Tier 2, over 14,000 km). Hybrid: $0.83/km and $0.20/km. Electric: $0.09/km (flat rate). These rates apply to business km driven between 1 April 2025 and 31 March 2026."
  - q: "What is the difference between Tier 1 and Tier 2 IRD mileage rates?"
    a: "Tier 1 covers the first 14,000 km of business travel per year and includes all vehicle costs — depreciation, insurance, registration and fuel. Tier 2 applies above 14,000 km and covers fuel and running costs only, which is why the rate is lower. If you drive under 14,000 km for business, you only use the Tier 1 rate."
  - q: "Can NZ tradies claim vehicle expenses or mileage?"
    a: "Yes. Self-employed tradies can claim either: (a) IRD kilometre rate — multiply business km by the set rate, no receipts needed for fuel; or (b) actual vehicle costs — track all real expenses (fuel, WOF, rego, insurance, depreciation) and claim the business-use percentage. Most low-km tradies use the km rate; high-km tradies often get a larger deduction with actual costs."
  - q: "Do I need a logbook for the IRD kilometre rate method?"
    a: "For the kilometre-rate method you just need a record of each business trip: date, km travelled, destination and purpose. You don't need to track fuel receipts. For the actual-cost method you need a 90-day logbook (once every 3 years) to establish your business use percentage."
  - q: "When is the 2025–26 tax return due?"
    a: "The 2025–26 income year ended 31 March 2026. If you file your IR3 yourself, it's due 7 July 2026. If you use a tax agent, the deadline extends to 31 March 2027. Ensure your vehicle km are tallied before filing."
  - q: "Can I use the km rate for a ute or van?"
    a: "Yes. The IRD kilometre rate applies to any motor vehicle including utes, vans and SUVs. If your ute is a genuine work vehicle not available for private use, it may be fully deductible as a business asset — different from the km-rate method. Talk to your accountant if your vehicle is primarily for work."
  - q: "What kilometre rate should I use for reimbursing employees?"
    a: "For reimbursing employees who use their own vehicles, IRD's Tier 1 rate ($1.04/km for 2025–26) is the standard benchmark. Reimbursements up to the Tier 1 rate are tax-free for the employee. Reimbursements above the Tier 1 rate attract PAYE."
related_articles: [ird-kilometre-rates-2025-26-nz-tradies, vehicle-expenses-nz-tradies-ird]
---

## IRD Kilometre Rates 2025–26

The current IRD kilometre rates for the **2025–26 income year** (1 April 2025 – 31 March 2026):

| Vehicle type | Tier 1 (first 14,000 km) | Tier 2 (over 14,000 km) |
|---|---|---|
| Petrol or diesel | **$1.04/km** | **$0.35/km** |
| Hybrid (petrol-electric) | **$0.83/km** | **$0.20/km** |
| Electric | **$0.09/km** | **$0.09/km** |

*Source: IRD (ird.govt.nz). Verify current rates before filing.*

### What Counts as Business Travel?

- Travel between job sites
- Travel from your home office or yard to job sites
- Trips to suppliers, merchants, or hardware stores
- Client meetings and quotes

**Does NOT count:** Travel between home and a fixed regular workplace (commuting). But if your home is your base of operations, travel from home to client sites **is** deductible.

### Which Method Is Better — Km Rate or Actual Costs?

Use the **km rate** if your business km are relatively low and you want simple record-keeping.

Use the **actual cost method** if you drive a high-km or expensive vehicle — it usually gives a larger deduction but requires tracking all expenses and a 90-day logbook once every 3 years.
