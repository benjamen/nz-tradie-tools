---
title: "NZ KiwiSaver Employer Cost Calculator 2026"
description: "Calculate the true employer cost of KiwiSaver including the 3.5% contribution and ESCT (employer superannuation contribution tax) for NZ tradies."
tags: [KiwiSaver, ESCT, employer, wages, tax, NZ]
author: "NZ Tradie Tools"
related_articles: [hiring-an-apprentice-nz-tradie-guide-2026, minimum-wage-increase-april-2026-tradie-costs, subcontractor-vs-employee-gateway-test-nz-2026]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Employee gross annual wage — $</label>
      <input type="number" id="ks-wage" placeholder="e.g. 65000" oninput="calcKS()">
    </div>
    <div class="calc-group">
      <label>Employee KiwiSaver rate</label>
      <select id="ks-ee-rate" onchange="calcKS()">
        <option value="0.03">3% (minimum)</option>
        <option value="0.04">4%</option>
        <option value="0.06">6%</option>
        <option value="0.08">8%</option>
        <option value="0.10">10%</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="ks-result" style="display:none">
    <h3>Employer KiwiSaver Cost</h3>
    <div class="result-row"><span>Gross annual wage</span><span id="ks-gross"></span></div>
    <div class="result-row"><span>Employer KiwiSaver (3.5%)</span><span id="ks-er-contrib"></span></div>
    <div class="result-row"><span>ESCT rate</span><span id="ks-esct-rate"></span></div>
    <div class="result-row"><span>ESCT on employer contribution</span><span id="ks-esct-amt"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total employer cost per year</span><span id="ks-total"></span></div>
    <div class="result-row"><span>Total employer cost per week</span><span id="ks-weekly"></span></div>
    <div style="margin-top:1rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
      <strong>Employee take-home:</strong> Gross wage minus PAYE, ACC earners levy (1.60%), and employee KiwiSaver (<span id="ks-ee-pct"></span>).
      The employee KiwiSaver of <span id="ks-ee-amt"></span>/year comes out of their gross pay.
    </div>
  </div>
  <script>
  function fmt(n){return '$'+Math.round(n).toLocaleString('en-NZ');}
  function fmtp(n){return n.toFixed(1)+'%';}
  function esctRate(wage){
    if(wage<=16800)return 0.105;
    if(wage<=57600)return 0.175;
    if(wage<=84000)return 0.30;
    return 0.33;
  }
  function calcKS(){
    var wage=parseFloat(document.getElementById('ks-wage').value)||0;
    var eeRate=parseFloat(document.getElementById('ks-ee-rate').value)||0.03;
    var r=document.getElementById('ks-result');
    if(!wage||wage<0){r.style.display='none';return;}
    var erContrib=wage*0.035;
    var esct=esctRate(wage);
    var esctAmt=erContrib*esct;
    var total=wage+erContrib+esctAmt;
    var eeContrib=wage*eeRate;
    document.getElementById('ks-gross').textContent=fmt(wage);
    document.getElementById('ks-er-contrib').textContent=fmt(erContrib);
    document.getElementById('ks-esct-rate').textContent=fmtp(esct*100);
    document.getElementById('ks-esct-amt').textContent=fmt(esctAmt);
    document.getElementById('ks-total').textContent=fmt(total);
    document.getElementById('ks-weekly').textContent=fmt(total/52);
    document.getElementById('ks-ee-pct').textContent=fmtp(eeRate*100);
    document.getElementById('ks-ee-amt').textContent=fmt(eeContrib);
    r.style.display='';
  }
  </script>
faqs:
  - q: 'How much KiwiSaver does an employer pay in NZ?'
    a: 'Employers must pay a minimum of 3% of an employee''s gross wages as a KiwiSaver employer contribution. This is in addition to the employee''s own contribution and is not deducted from wages.'
  - q: 'What is ESCT and how does it work?'
    a: 'ESCT (Employer Superannuation Contribution Tax) is deducted from the employer''s KiwiSaver contribution before it reaches the employee''s account. The ESCT rate depends on the employee''s annual salary: 10.5% up to $16,800, rising to 39% over $216,000.'
  - q: 'Is the employer KiwiSaver contribution tax-deductible?'
    a: 'Yes. Employer KiwiSaver contributions are a deductible business expense in NZ. The net cost after tax (at 28% company rate) is approximately 2.16% of payroll for a 3% contribution.'
  - q: 'Does an employer have to pay KiwiSaver for casual workers?'
    a: 'Employers must enrol employees who work 20+ hours/week unless the employee opts out within 8 weeks. Casual workers under 20 hours/week are not automatically enrolled but can opt in voluntarily.'
---

## Understanding the True Cost of KiwiSaver for Employers

Most tradies know they have to contribute to KiwiSaver for their employees — but many don't realise there's a second cost on top: **ESCT (Employer Superannuation Contribution Tax)**.

### How Employer KiwiSaver Works in 2026

From **1 April 2026**, the minimum employer contribution rate increased from 3% to **3.5%**. This applies to all eligible employees.

As an employer, you must:
1. Contribute at least 3.5% of the employee's gross earnings to their KiwiSaver fund
2. Pay ESCT on that contribution to IRD

### What Is ESCT?

ESCT is a tax on the employer's KiwiSaver contribution. The rate depends on the employee's income:

| Employee's annual income | ESCT rate |
|---|---|
| Up to $16,800 | 10.5% |
| $16,801 – $57,600 | 17.5% |
| $57,601 – $84,000 | 30% |
| Over $84,000 | 33% |

### Example: Apprentice on $52,000/year

- Employer KiwiSaver contribution: $52,000 × 3.5% = **$1,820**
- ESCT rate: 17.5% (income in $16,801–$57,600 band)
- ESCT: $1,820 × 17.5% = **$318.50**
- **Total employer cost on top of gross wage: $2,138.50/year**

This is money leaving your business on top of the wages you're paying — and it's required by law.

See [IRD's KiwiSaver employer guide](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers) for full details.
