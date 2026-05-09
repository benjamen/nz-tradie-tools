---
title: "NZ Employee Total Cost of Employment Calculator 2026"
description: "Calculate the true cost of employing a worker in NZ — including wages, KiwiSaver, ESCT, ACC, annual leave, sick leave and public holidays."
tags: [employment, wages, KiwiSaver, ACC, annual leave, NZ]
author: "NZ Tradie Tools"
related_articles: [hiring-an-apprentice-nz-tradie-guide-2026, minimum-wage-increase-april-2026-tradie-costs, kiwisaver-employer-cost-calculator]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Gross annual wage — $</label>
      <input type="number" id="etc-wage" placeholder="e.g. 65000" oninput="calcETC()">
    </div>
    <div class="calc-group">
      <label>Industry / ACC levy class</label>
      <select id="etc-acc" onchange="calcETC()">
        <option value="0.0063">General construction — 0.63%</option>
        <option value="0.0085">Roofing / scaffolding — 0.85%</option>
        <option value="0.0049">Electrical / plumbing — 0.49%</option>
        <option value="0.0038">Painting / decorating — 0.38%</option>
        <option value="0.0072">Earthworks / excavation — 0.72%</option>
        <option value="0.0055">General trades — 0.55%</option>
      </select>
    </div>
    <div class="calc-group">
      <label>KiwiSaver employer rate</label>
      <select id="etc-ks" onchange="calcETC()">
        <option value="0.035">3.5% (minimum from Apr 2026)</option>
        <option value="0.04">4%</option>
        <option value="0.06">6%</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Annual leave weeks</label>
      <select id="etc-leave" onchange="calcETC()">
        <option value="4">4 weeks (minimum)</option>
        <option value="5">5 weeks</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="etc-result" style="display:none">
    <h3>True Cost of Employment</h3>
    <div class="result-row"><span>Gross annual wage</span><span id="etc-r-gross"></span></div>
    <div class="result-row"><span>Employer KiwiSaver</span><span id="etc-r-ks"></span></div>
    <div class="result-row"><span>ESCT on KiwiSaver contribution</span><span id="etc-r-esct"></span></div>
    <div class="result-row"><span>ACC employer levy</span><span id="etc-r-acc"></span></div>
    <div class="result-row"><span>Annual leave loading (included in wage)</span><span id="etc-r-leave"></span></div>
    <div class="result-row"><span>Public holidays (11 days, included in wage)</span><span id="etc-r-ph"></span></div>
    <div class="result-row"><span>Sick leave provision (10 days)</span><span id="etc-r-sick"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total annual cost to employer</span><span id="etc-r-total"></span></div>
    <div class="result-row"><span>Cost per week</span><span id="etc-r-weekly"></span></div>
    <div class="result-row"><span>Cost per billable hour (at 40hr week)</span><span id="etc-r-hourly"></span></div>
    <div style="margin-top:1rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
      The true employment cost is <strong id="etc-r-pct"></strong> above the stated gross wage — a figure that often surprises first-time employers.
    </div>
  </div>
  <script>
  function fmt(n){return "$"+Math.round(n).toLocaleString("en-NZ");}
  function fmth(n){return "$"+n.toFixed(2)+"/hr";}
  function esctRate(w){if(w<=16800)return 0.105;if(w<=57600)return 0.175;if(w<=84000)return 0.30;return 0.33;}
  function calcETC(){
    var w=parseFloat(document.getElementById("etc-wage").value)||0;
    var accRate=parseFloat(document.getElementById("etc-acc").value)||0.0055;
    var ksRate=parseFloat(document.getElementById("etc-ks").value)||0.035;
    var leaveWks=parseInt(document.getElementById("etc-leave").value)||4;
    var r=document.getElementById("etc-result");
    if(!w||w<0){r.style.display="none";return;}
    var ks=w*ksRate;
    var esct=ks*esctRate(w);
    var acc=w*accRate;
    var leaveVal=w/52*leaveWks;
    var ph=w/260*11;
    var sick=w/260*10;
    var total=w+ks+esct+acc+sick;
    var pct=((total/w-1)*100).toFixed(1);
    document.getElementById("etc-r-gross").textContent=fmt(w);
    document.getElementById("etc-r-ks").textContent=fmt(ks);
    document.getElementById("etc-r-esct").textContent=fmt(esct);
    document.getElementById("etc-r-acc").textContent=fmt(acc);
    document.getElementById("etc-r-leave").textContent=fmt(leaveVal)+" (est.)";
    document.getElementById("etc-r-ph").textContent=fmt(ph)+" (est.)";
    document.getElementById("etc-r-sick").textContent=fmt(sick);
    document.getElementById("etc-r-total").textContent=fmt(total);
    document.getElementById("etc-r-weekly").textContent=fmt(total/52);
    document.getElementById("etc-r-hourly").textContent=fmth(total/52/40);
    document.getElementById("etc-r-pct").textContent=pct+"%";
    r.style.display="";
  }
  </script>
faqs:
  - q: 'What does it really cost to employ a tradie in NZ?'
    a: 'On top of wages, an employer pays: employer KiwiSaver (3%), ACC employer levy (varies by industry, typically 0.2–1%), annual leave loading (effectively 8%), and any tools, phone, or vehicle costs. Total true cost is often 15–25% above the gross wage.'
  - q: 'What is the employer KiwiSaver contribution rate in NZ?'
    a: 'Employers must contribute a minimum of 3% of an employee''s gross wages to KiwiSaver. This is paid on top of the employee''s wage and is a compulsory cost.'
  - q: 'How much annual leave does an NZ employee get?'
    a: 'All NZ employees are entitled to 4 weeks'' annual leave per year under the Holidays Act 2003. This equates to 8% of gross earnings as a leave reserve.'
  - q: 'What ACC costs does an NZ employer pay?'
    a: 'Employers pay an ACC work levy based on their industry classification and payroll. Rates for 2024–25 range from about $0.18 to $3.00 per $100 of payroll depending on trade risk. Builders are around $0.90–$1.50/100.'
---

## The Real Cost of Hiring a Tradie in NZ

The salary on the employment agreement is just the starting point. By the time you add KiwiSaver, ESCT, ACC, and statutory leave, the true cost of employment is typically **18–28% above the gross wage**.

### What Gets Added on Top

**KiwiSaver (employer contribution)** — minimum 3.5% of gross from April 2026. This money goes to the employee's KiwiSaver fund and is a direct cost to your business.

**ESCT (Employer Superannuation Contribution Tax)** — tax on your KiwiSaver contribution, ranging from 10.5% to 33% depending on the employee's income. Often overlooked.

**ACC employer levy** — charged by ACC on top of the employee's earners' levy. Rate varies by industry classification.

**Annual leave** — 4 weeks minimum under the Holidays Act 2003. You're paying this even when the employee is not working.

**Sick leave** — 10 days per year after 6 months, increasing to 20 days for longer-serving employees.

**Public holidays** — 11 public holidays per year, all paid at ordinary day's pay.

### Minimum Wage in 2026

The adult minimum wage from 1 April 2026 is **$23.50/hour** ($48,880/year for 40 hours). Starting-out and training wages are 80% of this ($18.80/hour).

See our [apprentice wage calculator](/calculators/apprentice-wage-calculator.html) for trade-specific apprenticeship rates.
