---
title: "Business Breakeven Calculator — NZ Tradies"
description: "Calculate your breakeven point, minimum revenue, and profit margin as an NZ tradie or small business."
tags: [breakeven, profit, business, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchBETab('be')">Breakeven Point</button>
    <button class="calc-tab" onclick="switchBETab('rev')">Revenue Target</button>
    <button class="calc-tab" onclick="switchBETab('job')">Per-Job Profit</button>
  </div>
  <div id="betab-be">
    <p style="font-size:.85rem;color:#666;margin-bottom:1rem">Enter your monthly fixed costs and your average gross margin to find your breakeven revenue.</p>
    <div class="calc-grid">
      <div class="calc-group"><label>Monthly rent / premises ($)</label><input type="number" id="be-rent" placeholder="0" value="0" oninput="calcBE()"></div>
      <div class="calc-group"><label>Vehicle / lease costs ($)</label><input type="number" id="be-veh" placeholder="e.g. 800" oninput="calcBE()"></div>
      <div class="calc-group"><label>Insurance (monthly) ($)</label><input type="number" id="be-ins" placeholder="e.g. 300" oninput="calcBE()"></div>
      <div class="calc-group"><label>Software subscriptions ($)</label><input type="number" id="be-sw" placeholder="e.g. 150" oninput="calcBE()"></div>
      <div class="calc-group"><label>Other fixed costs ($)</label><input type="number" id="be-other" placeholder="e.g. 500" oninput="calcBE()"></div>
      <div class="calc-group"><label>Average gross margin (%)</label><input type="number" id="be-margin" placeholder="e.g. 40" value="40" oninput="calcBE()"></div>
    </div>
    <div class="calc-result" id="be-result" style="display:none">
      <h3>Breakeven Analysis</h3>
      <div class="result-row"><span>Total monthly fixed costs</span><span id="be-fixed"></span></div>
      <div class="result-row"><span>Breakeven monthly revenue</span><span id="be-rev" class="result-highlight"></span></div>
      <div class="result-row"><span>Breakeven annual revenue</span><span id="be-ann"></span></div>
      <div class="result-row"><span>Breakeven daily revenue (21 days)</span><span id="be-daily"></span></div>
      <div class="result-row"><span>Revenue needed for $80k take-home</span><span id="be-80k"></span></div>
    </div>
  </div>
  <div id="betab-rev" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Target annual income ($)</label><input type="number" id="rv-target" placeholder="e.g. 90000" oninput="calcRev()"></div>
      <div class="calc-group"><label>Monthly fixed costs ($)</label><input type="number" id="rv-fixed" placeholder="e.g. 2500" oninput="calcRev()"></div>
      <div class="calc-group"><label>Gross margin (%)</label><input type="number" id="rv-margin" placeholder="e.g. 45" value="45" oninput="calcRev()"></div>
      <div class="calc-group"><label>Billable days per year</label><input type="number" id="rv-days" placeholder="e.g. 220" value="220" oninput="calcRev()"></div>
    </div>
    <div class="calc-result" id="rv-result" style="display:none">
      <h3>Revenue Required</h3>
      <div class="result-row"><span>Annual revenue needed</span><span id="rv-ann" class="result-highlight"></span></div>
      <div class="result-row"><span>Monthly revenue needed</span><span id="rv-mon"></span></div>
      <div class="result-row"><span>Daily rate needed</span><span id="rv-day"></span></div>
      <div class="result-row"><span>Hourly rate (8hr day)</span><span id="rv-hr"></span></div>
    </div>
  </div>
  <div id="betab-job" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Job quote price ($)</label><input type="number" id="jb-price" placeholder="e.g. 3500" oninput="calcJob()"></div>
      <div class="calc-group"><label>Materials cost ($)</label><input type="number" id="jb-mat" placeholder="e.g. 1200" oninput="calcJob()"></div>
      <div class="calc-group"><label>Labour hours</label><input type="number" id="jb-hrs" placeholder="e.g. 16" oninput="calcJob()"></div>
      <div class="calc-group"><label>Your hourly cost (incl. overhead) ($)</label><input type="number" id="jb-cost" placeholder="e.g. 75" oninput="calcJob()"></div>
      <div class="calc-group"><label>Subcontractor costs ($)</label><input type="number" id="jb-sub" placeholder="0" value="0" oninput="calcJob()"></div>
    </div>
    <div class="calc-result" id="jb-result" style="display:none">
      <h3>Job Profitability</h3>
      <div class="result-row"><span>Total costs</span><span id="jb-total-cost"></span></div>
      <div class="result-row"><span>Gross profit</span><span id="jb-gp" class="result-highlight"></span></div>
      <div class="result-row"><span>Gross margin %</span><span id="jb-margin"></span></div>
      <div class="result-row"><span>Effective hourly rate</span><span id="jb-ehr"></span></div>
      <div id="jb-warn" style="display:none;background:#fef2f2;border:1px solid #fca5a5;padding:.5rem .75rem;font-size:.84rem;margin-top:.5rem;border-radius:3px"></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchBETab(t){
    ['be','rev','job'].forEach(function(id){document.getElementById('betab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['be','rev','job'][i]===t);});
  }
  function calcBE(){
    var rent=parseFloat(document.getElementById('be-rent').value)||0;
    var veh=parseFloat(document.getElementById('be-veh').value)||0;
    var ins=parseFloat(document.getElementById('be-ins').value)||0;
    var sw=parseFloat(document.getElementById('be-sw').value)||0;
    var other=parseFloat(document.getElementById('be-other').value)||0;
    var margin=parseFloat(document.getElementById('be-margin').value)/100;
    if(!margin){document.getElementById('be-result').style.display='none';return;}
    var fixed=rent+veh+ins+sw+other;
    var revMon=fixed/margin;
    document.getElementById('be-fixed').textContent=nzd(fixed)+'/mo';
    document.getElementById('be-rev').textContent=nzd(revMon)+'/mo';
    document.getElementById('be-ann').textContent=nzd(revMon*12)+'/yr';
    document.getElementById('be-daily').textContent=nzd(revMon/21)+'/day';
    document.getElementById('be-80k').textContent=nzd((fixed+80000/12)/margin)+'/mo';
    document.getElementById('be-result').style.display='';
  }
  function calcRev(){
    var target=parseFloat(document.getElementById('rv-target').value)||0;
    var fixed=parseFloat(document.getElementById('rv-fixed').value)||0;
    var margin=parseFloat(document.getElementById('rv-margin').value)/100;
    var days=parseFloat(document.getElementById('rv-days').value)||220;
    if(!target||!margin){document.getElementById('rv-result').style.display='none';return;}
    var ann=(target+fixed*12)/margin;
    document.getElementById('rv-ann').textContent=nzd(ann);
    document.getElementById('rv-mon').textContent=nzd(ann/12);
    document.getElementById('rv-day').textContent=nzd(ann/days);
    document.getElementById('rv-hr').textContent='$'+(ann/days/8).toFixed(2)+'/hr';
    document.getElementById('rv-result').style.display='';
  }
  function calcJob(){
    var price=parseFloat(document.getElementById('jb-price').value)||0;
    var mat=parseFloat(document.getElementById('jb-mat').value)||0;
    var hrs=parseFloat(document.getElementById('jb-hrs').value)||0;
    var costHr=parseFloat(document.getElementById('jb-cost').value)||0;
    var sub=parseFloat(document.getElementById('jb-sub').value)||0;
    if(!price){document.getElementById('jb-result').style.display='none';return;}
    var labCost=hrs*costHr;
    var total=mat+labCost+sub;
    var gp=price-total;
    var margin=price?gp/price*100:0;
    var ehr=hrs?gp/hrs:0;
    document.getElementById('jb-total-cost').textContent=nzd(total);
    document.getElementById('jb-gp').textContent=nzd(gp);
    document.getElementById('jb-margin').textContent=margin.toFixed(1)+'%';
    document.getElementById('jb-ehr').textContent='$'+ehr.toFixed(2)+'/hr effective';
    var warn=document.getElementById('jb-warn');
    if(gp<0){warn.innerHTML='<strong>⚠ Loss-making job.</strong> Your costs exceed the quote price. Review your pricing.';warn.style.display='';}
    else if(margin<15){warn.innerHTML='<strong>⚠ Low margin.</strong> Under 15% gross margin is risky for a trades business. Consider your overhead recovery.';warn.style.display='';}
    else{warn.style.display='none';}
    document.getElementById('jb-result').style.display='';
  }
  </script>
---

## Why Tradies Need to Know Their Numbers

Most tradespeople focus on doing great work — but fail to track whether the business is actually profitable. Common mistakes:

### The #1 Pricing Error

**Not including overhead in your hourly rate.** Your "cost" isn't just your wages — it includes vehicle, insurance, tools, software, ACC, KiwiSaver, and downtime. A good rule of thumb for NZ tradies:

> **Charge rate = (desired take-home ÷ billable hours) × 2.0–2.5**

If you want $80k take-home and bill 1,600 hours/year: minimum charge rate = $80,000 ÷ 1,600 × 2.2 = **$110/hr**

### Gross Margin Benchmarks

| Business type | Typical gross margin |
|---|---|
| Labour-only trades (electricians, plumbers) | 40–60% |
| Material + labour (builders, concreters) | 25–40% |
| Maintenance / service work | 50–70% |

Under 20% gross margin = your business is working hard for very little. Use our [Hourly Rate Calculator](/calculators/hourly-rate-calculator.html) to set the right rate.
