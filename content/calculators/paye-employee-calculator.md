---
title: "PAYE Employee Cost Calculator — NZ"
description: "Calculate the true cost of employing someone in NZ — PAYE, ACC, KiwiSaver, holiday pay, and total employer cost."
tags: [PAYE, employee, wages, calculator, NZ, tax]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Gross annual salary ($)</label><input type="number" id="py-sal" placeholder="e.g. 65000" oninput="calcPAYE()"></div>
    <div class="calc-group"><label>KiwiSaver (employer %)</label>
      <select id="py-ks" onchange="calcPAYE()">
        <option value="3" selected>3% (minimum)</option>
        <option value="4">4%</option>
        <option value="6">6%</option>
        <option value="8">8%</option>
        <option value="10">10%</option>
      </select>
    </div>
    <div class="calc-group"><label>Holiday pay treatment</label>
      <select id="py-hp" onchange="calcPAYE()">
        <option value="0.08" selected>8% on gross (included in salary)</option>
        <option value="0">In salary (4 weeks leave)</option>
      </select>
    </div>
    <div class="calc-group"><label>Region (for ACC)</label>
      <select id="py-reg" onchange="calcPAYE()">
        <option value="low">Low risk (office / retail)</option>
        <option value="med" selected>Medium risk (trades / construction)</option>
        <option value="high">High risk (roofing / scaffolding)</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="py-result" style="display:none">
    <h3>Employee Cost Breakdown</h3>
    <div class="result-row"><span>Gross salary</span><span id="py-gross"></span></div>
    <div class="result-row"><span>Employer KiwiSaver</span><span id="py-ks-out"></span></div>
    <div class="result-row"><span>ACC employer levy (est.)</span><span id="py-acc"></span></div>
    <div class="result-row"><span>Holiday pay provision (8%)</span><span id="py-hpout"></span></div>
    <div class="result-row"><span>Total cost to employer / yr</span><span id="py-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Effective hourly rate (2080hrs)</span><span id="py-hr"></span></div>
    <div class="result-row"><span>Employee take-home (est.)</span><span id="py-takehome"></span></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcPAYE(){
    var sal=parseFloat(document.getElementById('py-sal').value)||0;
    var ks=parseFloat(document.getElementById('py-ks').value)/100;
    var hp=parseFloat(document.getElementById('py-hp').value);
    var reg=document.getElementById('py-reg').value;
    if(!sal){document.getElementById('py-result').style.display='none';return;}
    var accRates={low:0.0067,med:0.016,high:0.028};
    var acc=sal*accRates[reg];
    var ksCost=sal*ks;
    var hpCost=hp?sal*0.08:0;
    var total=sal+ksCost+acc+hpCost;
    var hrRate=total/2080;
    var taxable=sal;
    var paye=0;
    if(taxable<=14000)paye=taxable*0.105;
    else if(taxable<=48000)paye=1470+(taxable-14000)*0.175;
    else if(taxable<=70000)paye=7420+(taxable-48000)*0.30;
    else if(taxable<=180000)paye=14020+(taxable-70000)*0.33;
    else paye=50320+(taxable-180000)*0.39;
    var acc_emp=sal*0.016;
    var takehome=sal-paye-acc_emp-(sal*ks);
    document.getElementById('py-gross').textContent=nzd(sal)+'/yr';
    document.getElementById('py-ks-out').textContent=nzd(ksCost)+'/yr ('+(ks*100)+'%)';
    document.getElementById('py-acc').textContent=nzd(acc)+'/yr';
    document.getElementById('py-hpout').textContent=hp?nzd(hpCost)+'/yr':'Included in salary';
    document.getElementById('py-total').textContent=nzd(total)+'/yr';
    document.getElementById('py-hr').textContent='$'+hrRate.toFixed(2)+'/hr';
    document.getElementById('py-takehome').textContent=nzd(takehome)+'/yr (~$'+Math.round(takehome/26).toLocaleString()+'/fortnight)';
    document.getElementById('py-result').style.display='';
  }
  </script>
---

## True Cost of Employment in NZ

Most small businesses underestimate the true cost of an employee. On top of gross salary, you must account for:

### Employer Obligations (2025)

| Cost | Rate |
|---|---|
| KiwiSaver (employer contribution) | Minimum 3% of gross |
| ACC employer levy | $0.67–$2.80 per $100 wages (varies by industry) |
| Holiday pay | 8% of gross (or 4 weeks leave) |
| Statutory holidays | 12 days/yr paid |

### ACC Levy Rates by Industry (2024–25)

Construction and trades pay significantly higher ACC levies than office work. The NZ "work levy" is based on your ANZSIC industry code:
- **Painting / decorating:** $1.18 per $100
- **Plumbing / electrical:** $0.87 per $100  
- **Roofing / scaffolding:** $2.50+ per $100
- **General construction:** $1.60 per $100

ACC levies are updated annually. Check the [ACC website](https://www.acc.co.nz/for-business/levies/) for current rates.

### Rule of Thumb

Budget **20–30% on top of gross salary** for the true employer cost. A $65,000/yr employee typically costs **$78,000–$85,000** all-in.

See our [Overtime Calculator](/calculators/overtime-calculator.html) for weekly pay breakdowns.
