---
title: "Labour Cost Calculator — NZ Tradies"
description: "Calculate total labour cost for a job, team, or project. Includes on-costs, overhead, and profitability check."
tags: [labour cost, wages, calculator, NZ, quoting]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchLCTab('job')">Job / Project</button>
    <button class="calc-tab" onclick="switchLCTab('team')">Team Rate</button>
    <button class="calc-tab" onclick="switchLCTab('quote')">Quote Check</button>
  </div>
  <div id="lctab-job">
    <div class="calc-grid">
      <div class="calc-group"><label>Number of workers</label><input type="number" id="lj-num" placeholder="e.g. 2" value="1" oninput="calcLabourJob()"></div>
      <div class="calc-group"><label>Hours per worker per day</label><input type="number" id="lj-hrs" placeholder="e.g. 8" value="8" oninput="calcLabourJob()"></div>
      <div class="calc-group"><label>Number of days</label><input type="number" id="lj-days" placeholder="e.g. 5" oninput="calcLabourJob()"></div>
      <div class="calc-group"><label>Hourly charge-out rate ($/hr)</label><input type="number" id="lj-rate" placeholder="e.g. 95" oninput="calcLabourJob()"></div>
      <div class="calc-group"><label>Overhead / on-cost (%)</label><input type="number" id="lj-oc" placeholder="e.g. 25" value="25" oninput="calcLabourJob()"></div>
    </div>
    <div class="calc-result" id="lj-result" style="display:none">
      <h3>Labour Cost Breakdown</h3>
      <div class="result-row"><span>Total hours</span><span id="lj-thrs"></span></div>
      <div class="result-row"><span>Direct labour cost</span><span id="lj-direct"></span></div>
      <div class="result-row"><span>Overhead / on-costs</span><span id="lj-oc-out"></span></div>
      <div class="result-row"><span>Total labour cost (your cost)</span><span id="lj-cost"></span></div>
      <div class="result-row"><span>Billable amount to client</span><span id="lj-bill" class="result-highlight"></span></div>
      <div class="result-row"><span>Gross margin on labour</span><span id="lj-margin"></span></div>
    </div>
  </div>
  <div id="lctab-team" style="display:none">
    <div style="font-size:.85rem;color:#555;margin-bottom:1rem">Add up to 4 team members with different rates:</div>
    <div class="calc-grid">
      <div class="calc-group"><label>Worker 1 — hourly rate ($)</label><input type="number" id="tm-r1" placeholder="e.g. 45" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Worker 1 — daily hours</label><input type="number" id="tm-h1" placeholder="8" value="8" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Worker 2 — hourly rate ($)</label><input type="number" id="tm-r2" placeholder="e.g. 32" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Worker 2 — daily hours</label><input type="number" id="tm-h2" placeholder="8" value="8" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Worker 3 — hourly rate ($)</label><input type="number" id="tm-r3" placeholder="optional" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Worker 3 — daily hours</label><input type="number" id="tm-h3" placeholder="8" value="8" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Days on job</label><input type="number" id="tm-days" placeholder="e.g. 3" oninput="calcTeam()"></div>
      <div class="calc-group"><label>Target margin on labour (%)</label><input type="number" id="tm-margin" placeholder="e.g. 20" value="20" oninput="calcTeam()"></div>
    </div>
    <div class="calc-result" id="tm-result" style="display:none">
      <h3>Team Labour Cost</h3>
      <div class="result-row"><span>Total team cost/day</span><span id="tm-daily"></span></div>
      <div class="result-row"><span>Total job cost</span><span id="tm-total"></span></div>
      <div class="result-row"><span>Quote this for labour</span><span id="tm-quote" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="lctab-quote" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Quoted labour amount ($)</label><input type="number" id="qc-quote" placeholder="e.g. 4500" oninput="calcQCheck()"></div>
      <div class="calc-group"><label>Your actual labour cost ($)</label><input type="number" id="qc-cost" placeholder="e.g. 3200" oninput="calcQCheck()"></div>
    </div>
    <div class="calc-result" id="qc-result" style="display:none">
      <h3>Quote Check</h3>
      <div class="result-row"><span>Gross profit on labour</span><span id="qc-gp"></span></div>
      <div class="result-row"><span>Gross margin %</span><span id="qc-margin" class="result-highlight"></span></div>
      <div class="result-row"><span>Markup %</span><span id="qc-markup"></span></div>
      <div id="qc-signal" style="margin-top:.5rem;padding:.5rem .75rem;font-size:.84rem;border-radius:3px"></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchLCTab(t){
    ['job','team','quote'].forEach(function(id){document.getElementById('lctab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['job','team','quote'][i]===t);});
  }
  function calcLabourJob(){
    var num=parseFloat(document.getElementById('lj-num').value)||0;
    var hrs=parseFloat(document.getElementById('lj-hrs').value)||8;
    var days=parseFloat(document.getElementById('lj-days').value)||0;
    var rate=parseFloat(document.getElementById('lj-rate').value)||0;
    var oc=parseFloat(document.getElementById('lj-oc').value)||25;
    if(!num||!days||!rate){document.getElementById('lj-result').style.display='none';return;}
    var totalHrs=num*hrs*days;
    var direct=totalHrs*rate;
    var ocCost=direct*oc/100;
    var cost=direct+ocCost;
    var bill=direct*(1+oc/100);
    var margin=(bill-direct)/bill*100;
    document.getElementById('lj-thrs').textContent=totalHrs+' hrs';
    document.getElementById('lj-direct').textContent=nzd(direct);
    document.getElementById('lj-oc-out').textContent=nzd(ocCost);
    document.getElementById('lj-cost').textContent=nzd(cost);
    document.getElementById('lj-bill').textContent=nzd(bill);
    document.getElementById('lj-margin').textContent=margin.toFixed(1)+'%';
    document.getElementById('lj-result').style.display='';
  }
  function calcTeam(){
    var r1=parseFloat(document.getElementById('tm-r1').value)||0;
    var h1=parseFloat(document.getElementById('tm-h1').value)||8;
    var r2=parseFloat(document.getElementById('tm-r2').value)||0;
    var h2=parseFloat(document.getElementById('tm-h2').value)||8;
    var r3=parseFloat(document.getElementById('tm-r3').value)||0;
    var h3=parseFloat(document.getElementById('tm-h3').value)||8;
    var days=parseFloat(document.getElementById('tm-days').value)||0;
    var margin=parseFloat(document.getElementById('tm-margin').value)||20;
    if(!days){document.getElementById('tm-result').style.display='none';return;}
    var daily=r1*h1+r2*h2+(r3?r3*h3:0);
    var total=daily*days;
    var quote=total/(1-margin/100);
    document.getElementById('tm-daily').textContent=nzd(daily)+'/day';
    document.getElementById('tm-total').textContent=nzd(total);
    document.getElementById('tm-quote').textContent=nzd(quote)+' (at '+margin+'% margin)';
    document.getElementById('tm-result').style.display='';
  }
  function calcQCheck(){
    var quote=parseFloat(document.getElementById('qc-quote').value)||0;
    var cost=parseFloat(document.getElementById('qc-cost').value)||0;
    if(!quote||!cost){document.getElementById('qc-result').style.display='none';return;}
    var gp=quote-cost;
    var margin=gp/quote*100;
    var markup=gp/cost*100;
    document.getElementById('qc-gp').textContent=nzd(gp);
    document.getElementById('qc-margin').textContent=margin.toFixed(1)+'%';
    document.getElementById('qc-markup').textContent=markup.toFixed(1)+'%';
    var sig=document.getElementById('qc-signal');
    if(margin<10){sig.style.background='#fef2f2';sig.style.borderLeft='3px solid #ef4444';sig.textContent='⚠ Under 10% margin — barely covering overhead. Review your rate.';}
    else if(margin<20){sig.style.background='#fffbeb';sig.style.borderLeft='3px solid #f59e0b';sig.textContent='⚠ 10–20% margin — acceptable but lean. Consider whether you\'re covering all costs.';}
    else{sig.style.background='#f0fdf4';sig.style.borderLeft='3px solid #22c55e';sig.textContent='✓ Healthy margin. Keep tracking actuals vs estimate to stay profitable.';}
    document.getElementById('qc-result').style.display='';
  }
  </script>
---

## Setting Your Labour Rate in NZ

The right charge-out rate isn't just your wages — it must recover all your costs and leave a profit.

### The Cost-Plus Formula

> **Charge rate = (Actual wage cost × overhead factor) ÷ billable hours ratio**

For a tradesperson earning $50/hr actual cost, with 25% overhead and 75% billable time:
> ($50 × 1.25) ÷ 0.75 = **$83/hr minimum charge-out**

### Overhead Items Often Missed

- Vehicle (loan, insurance, WoF, fuel, registration)
- Tools and equipment
- Software (job management, accounting, invoicing)
- Mobile phone
- ACC employer levy
- Public liability and business insurance
- Downtime (rain days, travel, quoting, admin)
- KiwiSaver contributions

### NZ Trades Labour Benchmarks (2025)

| Trade | Typical charge-out rate |
|---|---|
| Electrician | $95–$130/hr |
| Plumber | $90–$130/hr |
| Builder (LBP) | $80–$120/hr |
| Tiler | $80–$110/hr |
| Painter | $55–$85/hr |
| Landscaper | $65–$95/hr |

Use our [Hourly Rate Calculator](/calculators/hourly-rate-calculator.html) to calculate your minimum viable rate.
