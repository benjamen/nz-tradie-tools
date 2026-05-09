---
title: "NZ Vehicle Mileage Claim Calculator"
description: "Calculate your IRD mileage reimbursement or tax deduction using the 2024-25 NZ mileage rates."
tags: [vehicle, mileage, IRD, tax, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group" style="grid-column:1/-1">
      <label>Kilometres driven for business</label>
      <input type="number" id="km" placeholder="e.g. 15000" oninput="calcMile()">
    </div>
    <div class="calc-group" style="grid-column:1/-1">
      <label>IRD mileage rate</label>
      <select id="rate" onchange="calcMile()">
        <option value="0.95">$0.95/km — petrol or diesel (up to 14,000 km/yr)</option>
        <option value="0.35">$0.35/km — petrol or diesel (over 14,000 km/yr)</option>
        <option value="0.09">$0.09/km — electric vehicle</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="mile-result" style="display:none">
    <h3>Mileage Claim</h3>
    <div class="result-row"><span>Kilometres claimed</span><span id="m-km"></span></div>
    <div class="result-row"><span>Rate applied</span><span id="m-rate"></span></div>
    <div class="result-row"><span>Total deduction / reimbursement</span><span id="m-total"></span></div>
    <div class="result-row"><span>Tax saved (approx 28% tax rate)</span><span id="m-tax"></span></div>
  </div>
  <script>
  function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function calcMile(){
    var km=parseFloat(document.getElementById('km').value);
    var r=parseFloat(document.getElementById('rate').value);
    var res=document.getElementById('mile-result');
    if(isNaN(km)||km<=0){res.style.display='none';return;}
    // Handle two-tier rate for petrol over 14000
    var total;
    if(r===0.95&&km>14000){
      total=14000*0.95+(km-14000)*0.35;
    } else {
      total=km*r;
    }
    document.getElementById('m-km').textContent=Math.round(km).toLocaleString()+' km';
    document.getElementById('m-rate').textContent='$'+r.toFixed(2)+'/km';
    document.getElementById('m-total').textContent=fmt(total);
    document.getElementById('m-tax').textContent=fmt(total*0.28);
    res.style.display='';
  }
  </script>
related_articles: [vehicle-expenses-nz-tradies-ird]
faqs:
  - q: 'What is the IRD mileage rate for NZ in 2025?'
    a: 'The IRD Tier 1 rate for the first 14,000 km of business travel per year is 73c/km for petrol or diesel vehicles in 2024–25. The Tier 2 rate for km above 14,000 is 21c/km. Electric vehicles use different rates.'
  - q: 'Can NZ tradies claim vehicle expenses or mileage?'
    a: 'Yes. You can either: (a) claim actual vehicle expenses (fuel, WOF, registration, insurance, loan interest) multiplied by business use %, or (b) use the IRD mileage rate for business km travelled. Most tradies use actual costs with a logbook.'
  - q: 'Do I need a logbook for vehicle expenses in NZ?'
    a: 'To claim actual vehicle expenses on a mixed-use vehicle, you need a logbook for 3 months every 3 years to establish the business vs private use percentage. The mileage rate method requires a record of business trips only.'
  - q: 'What vehicles qualify for the IRD mileage rate in NZ?'
    a: 'The IRD kilometre rate method applies to motor vehicles (including utes and vans). It is most suitable for low-km business use. Vehicles used predominantly for work (over 75% business) are often better treated as fully deductible business assets.'
---

## IRD Mileage Rates for NZ Tradies (2024–25)

If you use your personal vehicle for business, you can claim a tax deduction based on the IRD's kilometre rates.

### 2024–25 IRD Kilometre Rates

| Vehicle type | First 14,000 km | Over 14,000 km |
|---|---|---|
| Petrol or diesel | **$0.95/km** | **$0.35/km** |
| Petrol hybrid | $0.26/km | $0.19/km |
| Electric | $0.09/km | $0.09/km |

*Rates updated August 2024. Always check [ird.govt.nz](https://www.ird.govt.nz) for current rates.*

### What Counts as Business Travel?

- Travel between job sites
- Travel from your office or yard to job sites
- Trips to suppliers to pick up materials
- Client meetings

**Does NOT include:** travel between home and your regular place of business (commuting).

If you work from home and your home is your base, travel from home to client sites **is** deductible.

### How to Claim Vehicle Expenses

**Option 1: IRD kilometre rate (this calculator)**
- Record every business trip (date, km, purpose)
- Multiply by the IRD rate
- No GST to claim, but simpler record-keeping

**Option 2: Actual cost method**
- Track all actual vehicle expenses (fuel, insurance, servicing, registration, depreciation)
- Calculate the business use percentage
- Claim that percentage of actual costs
- More complex but often higher deduction for high-mileage tradies

### Keeping a Mileage Log

IRD can ask for records any time. Keep a logbook with:
- Date of each trip
- Start and end odometer readings (or km for the trip)
- Purpose of the trip
- Client or job name

Apps like [Tradify](https://www.tradifyhq.com/) include built-in mileage tracking. Alternatively, a simple spreadsheet works fine.
