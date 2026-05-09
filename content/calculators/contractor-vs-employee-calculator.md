---
title: "NZ Contractor vs Employee Tax Calculator 2025–26"
description: "Compare net take-home pay as a self-employed contractor versus a PAYE employee on the same gross income — including tax, ACC, KiwiSaver and leave."
tags: [contractor, employee, PAYE, tax, self-employed, NZ]
author: "NZ Tradie Tools"
related_articles: [subcontractor-vs-employee-gateway-test-nz-2026, sole-trader-vs-company-nz-tradies, going-self-employed-nz-tradie-guide]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group" style="grid-column:1/-1">
      <label>Gross annual income — $</label>
      <input type="number" id="cve-income" placeholder="e.g. 90000" oninput="calcCvE()">
      <small>For a fair comparison, use the same gross figure for both. As a contractor, this is your income before expenses.</small>
    </div>
    <div class="calc-group">
      <label>Annual business expenses (contractor only) — $</label>
      <input type="number" id="cve-expenses" placeholder="e.g. 15000" oninput="calcCvE()">
    </div>
    <div class="calc-group">
      <label>KiwiSaver rate</label>
      <select id="cve-ks" onchange="calcCvE()">
        <option value="0.03">3%</option>
        <option value="0.04">4%</option>
        <option value="0.06">6%</option>
        <option value="0">Not enrolled</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="cve-result" style="display:none">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem">
      <div>
        <h3 style="text-align:center;font-size:1rem">Employee (PAYE)</h3>
        <div class="result-row"><span>Gross wage</span><span id="cve-e-gross"></span></div>
        <div class="result-row"><span>Income tax (PAYE)</span><span id="cve-e-tax" style="color:#c53030"></span></div>
        <div class="result-row"><span>ACC earners levy</span><span id="cve-e-acc" style="color:#c53030"></span></div>
        <div class="result-row"><span>Employee KiwiSaver</span><span id="cve-e-ks" style="color:#c53030"></span></div>
        <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Net take-home</span><span id="cve-e-net"></span></div>
        <div class="result-row"><span>+ Employer KiwiSaver</span><span id="cve-e-erks" style="color:#22543d;font-size:.82rem"></span></div>
        <div class="result-row"><span>+ 4 weeks paid leave</span><span id="cve-e-leave" style="color:#22543d;font-size:.82rem"></span></div>
      </div>
      <div>
        <h3 style="text-align:center;font-size:1rem">Sole Trader (Contractor)</h3>
        <div class="result-row"><span>Gross income</span><span id="cve-c-gross"></span></div>
        <div class="result-row"><span>Business expenses</span><span id="cve-c-exp" style="color:#c53030"></span></div>
        <div class="result-row"><span>Income tax</span><span id="cve-c-tax" style="color:#c53030"></span></div>
        <div class="result-row"><span>ACC levies (earners + working)</span><span id="cve-c-acc" style="color:#c53030"></span></div>
        <div class="result-row"><span>KiwiSaver (self-contrib.)</span><span id="cve-c-ks" style="color:#c53030"></span></div>
        <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Net take-home</span><span id="cve-c-net"></span></div>
        <div class="result-row"><span>No employer KiwiSaver</span><span style="color:#c53030;font-size:.82rem">—</span></div>
        <div class="result-row"><span>No paid leave</span><span style="color:#c53030;font-size:.82rem">—</span></div>
      </div>
    </div>
    <div style="margin-top:1rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
      <strong>Difference:</strong> Contractor takes home <span id="cve-diff"></span> more/less than the employee per year on the same gross — before accounting for the value of employer KiwiSaver and paid leave.
    </div>
  </div>
  <script>
  function fmt(n){return '$'+Math.round(Math.abs(n)).toLocaleString('en-NZ');}
  function nzTax(inc){
    if(inc<=0)return 0;
    var t=0;
    if(inc>180000)t+=(inc-180000)*0.39;
    if(inc>70000)t+=Math.min(inc-70000,110000)*0.33;
    if(inc>48000)t+=Math.min(inc-48000,22000)*0.30;
    if(inc>14000)t+=Math.min(inc-14000,34000)*0.175;
    t+=Math.min(inc,14000)*0.105;
    return t;
  }
  function calcCvE(){
    var gross=parseFloat(document.getElementById('cve-income').value)||0;
    var exp=parseFloat(document.getElementById('cve-expenses').value)||0;
    var ksRate=parseFloat(document.getElementById('cve-ks').value)||0;
    var r=document.getElementById('cve-result');
    if(!gross||gross<0){r.style.display='none';return;}
    var eTax=nzTax(gross);
    var eAcc=Math.min(gross,139384)*0.016;
    var eKs=gross*ksRate;
    var eNet=gross-eTax-eAcc-eKs;
    var eErKs=gross*0.035;
    var eLeave=gross/52*4;
    var cTaxable=Math.max(0,gross-exp);
    var cTax=nzTax(cTaxable);
    var cAcc=Math.min(cTaxable,139384)*0.016+Math.min(cTaxable,139384)*0.0139;
    var cKs=cTaxable*ksRate;
    var cNet=gross-exp-cTax-cAcc-cKs;
    var diff=cNet-eNet;
    document.getElementById('cve-e-gross').textContent=fmt(gross);
    document.getElementById('cve-e-tax').textContent='−'+fmt(eTax);
    document.getElementById('cve-e-acc').textContent='−'+fmt(eAcc);
    document.getElementById('cve-e-ks').textContent=ksRate?'−'+fmt(eKs):'—';
    document.getElementById('cve-e-net').textContent=fmt(eNet);
    document.getElementById('cve-e-erks').textContent=fmt(eErKs)+'/yr';
    document.getElementById('cve-e-leave').textContent=fmt(eLeave)+'/yr';
    document.getElementById('cve-c-gross').textContent=fmt(gross);
    document.getElementById('cve-c-exp').textContent=exp?'−'+fmt(exp):'—';
    document.getElementById('cve-c-tax').textContent='−'+fmt(cTax);
    document.getElementById('cve-c-acc').textContent='−'+fmt(cAcc);
    document.getElementById('cve-c-ks').textContent=ksRate?'−'+fmt(cKs):'—';
    document.getElementById('cve-c-net').textContent=fmt(cNet);
    document.getElementById('cve-diff').textContent=(diff>=0?fmt(diff)+' more':fmt(diff)+' less')+' as contractor';
    r.style.display='';
  }
  </script>
---

## Contractor vs Employee — What's the Real Difference?

One of the most common questions for NZ tradies considering going self-employed: will I take home more money as a contractor? The answer depends heavily on your income level, expenses, and the hidden costs of self-employment.

### What Employees Get That Contractors Don't

- **4 weeks paid annual leave** — worth approximately 7.7% of annual salary
- **Employer KiwiSaver** — 3.5% of gross wage contributed by employer
- **Sick leave** — 10 days/year after 6 months
- **PAYE handled automatically** — no provisional tax, no UOMI risk

### What Contractors Get That Employees Don't

- **Tax deductions on expenses** — tools, vehicle, phone, insurance, home office, accountant
- **Choice of structure** — operate as sole trader, partnership, or company
- **Flexibility** — work for multiple clients, set your own rates
- **Higher gross rates** — the market generally pays contractors more per hour to compensate for self-employment costs

### The ACC Difference

As a PAYE employee, you pay the ACC **earners' levy only** (1.60%). As a sole trader, you pay both the **earners' levy** and a **working cover levy** (rate depends on your industry — typically 1.39% for most trade work). This is an additional cost employees don't face.

### The Gateway Test

IRD uses the [Contractor Gateway Test](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/contractors/determining-whether-a-worker-is-an-employee-or-contractor) to determine whether a worker is truly self-employed. Getting this wrong can result in back-taxes and penalties. See our [Gateway Test article](/articles/subcontractor-vs-employee-gateway-test-nz-2026.html) for details.
