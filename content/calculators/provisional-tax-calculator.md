---
title: "NZ Provisional Tax Calculator 2025–26"
description: "Calculate your NZ provisional tax instalments using the standard or estimation method — IRD dates, 105% uplift, and safe harbour built in."
tags: [provisional tax, IRD, tax, self-employed, NZ]
author: "NZ Tradie Tools"
related_articles: [provisional-tax-nz-tradies, common-tax-mistakes-nz-tradies, sole-trader-setup-guide-nz-tradies]
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchPT('standard')">Standard Method</button>
    <button class="calc-tab" onclick="switchPT('estimate')">Estimation Method</button>
  </div>
  <div id="pt-standard">
    <div class="calc-grid">
      <div class="calc-group" style="grid-column:1/-1">
        <label>Prior year Residual Income Tax (RIT) — $</label>
        <input type="number" id="pt-prior-rit" placeholder="e.g. 8500" oninput="calcPTStd()">
        <small>Find your RIT on your prior year IR3 return or ask your accountant.</small>
      </div>
    </div>
    <div class="calc-result" id="pt-std-result" style="display:none">
      <h3>Standard Method — 2025–26</h3>
      <div class="result-row"><span>Prior year RIT</span><span id="pts-prior"></span></div>
      <div class="result-row"><span>105% uplift (total provisional tax)</span><span id="pts-total"></span></div>
      <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Each instalment (÷3)</span><span id="pts-each"></span></div>
      <div style="margin-top:1rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
        <strong>Payment dates:</strong><br>
        1st instalment: <strong>28 August 2025</strong><br>
        2nd instalment: <strong>15 January 2026</strong><br>
        3rd instalment: <strong>7 May 2026</strong>
      </div>
      <div id="pts-safe" style="display:none;margin-top:.75rem;background:#f0fff4;border:1px solid #68d391;border-radius:6px;padding:.75rem;font-size:.85rem;color:#22543d">
        <strong>Safe harbour applies.</strong> Your prior year RIT is under $5,000 — no provisional tax required. Full tax is due 7 February 2027 (or 7 April 2027 if you use a tax agent).
      </div>
    </div>
  </div>
  <div id="pt-estimate" style="display:none">
    <div class="calc-grid">
      <div class="calc-group">
        <label>Estimated gross income this year — $</label>
        <input type="number" id="pt-income" placeholder="e.g. 95000" oninput="calcPTEst()">
      </div>
      <div class="calc-group">
        <label>Estimated business expenses — $</label>
        <input type="number" id="pt-expenses" placeholder="e.g. 18000" oninput="calcPTEst()">
      </div>
    </div>
    <div class="calc-result" id="pt-est-result" style="display:none">
      <h3>Estimation Method — 2025–26</h3>
      <div class="result-row"><span>Estimated taxable income</span><span id="pte-taxable"></span></div>
      <div class="result-row"><span>Income tax</span><span id="pte-tax"></span></div>
      <div class="result-row"><span>ACC earners levy (1.60%)</span><span id="pte-acc"></span></div>
      <div class="result-row"><span>Estimated RIT</span><span id="pte-rit"></span></div>
      <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Each instalment (÷3)</span><span id="pte-each"></span></div>
      <div style="margin-top:.75rem;background:#fff8e1;border:1px solid #f6c90e;border-radius:6px;padding:.75rem;font-size:.85rem">
        <strong>Underestimate risk:</strong> If you pay less than required, IRD charges UOMI at <strong>10.91% p.a.</strong> on the shortfall. Use this method only if your income has dropped significantly.
      </div>
    </div>
  </div>
  <script>
  function fmt(n){return '$'+Math.round(n).toLocaleString('en-NZ');}
  function switchPT(m){
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',i===(m==='standard'?0:1));});
    document.getElementById('pt-standard').style.display=m==='standard'?''':''';
    document.getElementById('pt-estimate').style.display=m==='estimate'?'':'none';
  }
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
  function calcPTStd(){
    var p=parseFloat(document.getElementById('pt-prior-rit').value)||0;
    var r=document.getElementById('pt-std-result');
    if(!p||p<0){r.style.display='none';return;}
    var tot=p*1.05,each=tot/3;
    document.getElementById('pts-prior').textContent=fmt(p);
    document.getElementById('pts-total').textContent=fmt(tot);
    document.getElementById('pts-each').textContent=fmt(each);
    document.getElementById('pts-safe').style.display=p<5000?''':''';
    r.style.display='';
  }
  function calcPTEst(){
    var inc=parseFloat(document.getElementById('pt-income').value)||0;
    var exp=parseFloat(document.getElementById('pt-expenses').value)||0;
    var r=document.getElementById('pt-est-result');
    if(!inc||inc<0){r.style.display='none';return;}
    var taxable=Math.max(0,inc-exp);
    var tax=nzTax(taxable);
    var acc=Math.min(taxable,139384)*0.016;
    var rit=tax+acc;
    document.getElementById('pte-taxable').textContent=fmt(taxable);
    document.getElementById('pte-tax').textContent=fmt(tax);
    document.getElementById('pte-acc').textContent=fmt(acc);
    document.getElementById('pte-rit').textContent=fmt(rit);
    document.getElementById('pte-each').textContent=fmt(rit/3);
    r.style.display='';
  }
  </script>
---

## What Is Provisional Tax?

Provisional tax is how self-employed NZ tradies pay income tax throughout the year in three instalments, rather than one lump sum at the end.

You must pay provisional tax if your **Residual Income Tax (RIT)** for the prior year was $5,000 or more. RIT = total income tax − PAYE already deducted − tax credits.

### The Three Methods

**Standard method** (most common) — pay 105% of last year's RIT in three equal instalments. Safe if income is similar to prior year.

**Estimation method** — estimate this year's income and pay that instead. If you underestimate, IRD charges use-of-money interest (UOMI) at 10.91% p.a.

**Ratio method** — for GST-registered businesses with taxable supplies under $5M; provisional tax is a percentage of your GST returns.

### 2025–26 Instalment Dates

| Instalment | Due Date |
|---|---|
| 1st | 28 August 2025 |
| 2nd | 15 January 2026 |
| 3rd | 7 May 2026 |

### Safe Harbour

If prior year RIT was under **$5,000**, no provisional tax is required — your full tax bill is due 7 February 2027.

See the [IRD Tax Toolbox](https://www.ird.govt.nz/the-tax-toolbox) for further guidance. If you're unsure which method suits you best, talk to your accountant before the first instalment date.
