---
title: "ACC Levy Calculator NZ — Self-Employed Tradie Levies 2025/26"
description: "Calculate your ACC levies as a self-employed NZ tradie — work levy, earner levy, and working safer levy based on your trade and income."
tags: [ACC, levy, self-employed, insurance, tradie, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Trade / occupation</label>
      <select id="acc-trade" onchange="calcACC()">
        <option value="2.14">Builder / Carpenter (general)</option>
        <option value="1.02">Electrician</option>
        <option value="1.52">Plumber / Gasfitter</option>
        <option value="4.38">Roofer</option>
        <option value="1.85">Painter / Decorator</option>
        <option value="2.60">Landscaper / Groundskeeper</option>
        <option value="3.10">Demolition Worker</option>
        <option value="1.95">Concreter</option>
        <option value="2.30">Tiler / Flooring</option>
        <option value="1.45">HVAC / Heat Pump Installer</option>
        <option value="2.80">Excavator / Earthworks</option>
        <option value="1.20">Kitchen / Cabinet Maker</option>
        <option value="2.00">Other construction trade</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Annual liable income ($)</label>
      <input type="number" id="acc-income" placeholder="e.g. 80000" oninput="calcACC()">
    </div>
    <div class="calc-group">
      <label>Levy year</label>
      <select id="acc-year" onchange="calcACC()">
        <option value="2526" selected>2025/26</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="acc-result" style="display:none">
    <h3>ACC Levy Estimate</h3>
    <div class="result-row"><span>Work levy rate</span><span id="acc-work-rate"></span></div>
    <div class="result-row"><span>Work levy</span><span id="acc-work"></span></div>
    <div class="result-row"><span>Earner levy (1.33% up to $139,384)</span><span id="acc-earner"></span></div>
    <div class="result-row"><span>Working Safer levy (0.08%)</span><span id="acc-safer"></span></div>
    <div class="result-row"><span>Total ACC levy (estimated)</span><span id="acc-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Effective rate of income</span><span id="acc-eff"></span></div>
    <div class="result-row"><span>Weekly ACC cost</span><span id="acc-weekly"></span></div>
    <div style="margin-top:.75rem;padding:.6rem;background:#fff8e1;border-radius:4px;font-size:.85rem">
      <strong>Important:</strong> These are estimates based on published ACC levy rates. Your actual levy is calculated by IRD from your tax return and invoiced by ACC separately. Rates vary by industry classification unit (CU) — ACC may reclassify your trade if your work description changes.
    </div>
  </div>
  <script>
  function nzd(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  var EARNER_RATE = 1.33/100;
  var EARNER_MAX = 139384;
  var SAFER_RATE = 0.08/100;
  function calcACC(){
    var workRate = parseFloat(document.getElementById('acc-trade').value);
    var income = parseFloat(document.getElementById('acc-income').value)||0;
    if(!income){document.getElementById('acc-result').style.display='none';return;}
    var workLevy = income * workRate/100;
    var earnerBase = Math.min(income, EARNER_MAX);
    var earnerLevy = earnerBase * EARNER_RATE;
    var saferLevy = income * SAFER_RATE;
    var total = workLevy + earnerLevy + saferLevy;
    var eff = total/income*100;
    document.getElementById('acc-work-rate').textContent = workRate.toFixed(2)+'% of liable income';
    document.getElementById('acc-work').textContent = nzd(workLevy);
    document.getElementById('acc-earner').textContent = nzd(earnerLevy);
    document.getElementById('acc-safer').textContent = nzd(saferLevy);
    document.getElementById('acc-total').textContent = nzd(total);
    document.getElementById('acc-eff').textContent = eff.toFixed(2)+'%';
    document.getElementById('acc-weekly').textContent = nzd(total/52)+'/week';
    document.getElementById('acc-result').style.display='';
  }
  </script>
related_articles: [nz-tradie-tax-guide-what-you-can-claim, income-protection-insurance-nz-tradies]
faqs:
  - q: 'How is ACC levy calculated for self-employed NZ tradies?'
    a: 'Self-employed tradies pay ACC based on their liable earnings (net profit up to the maximum) multiplied by their industry levy rate. The 2024–25 working safer levy is $0.08 per $100 plus a trade-specific earners'' levy, totalling roughly $1.39–$2.80 per $100 for most trades.'
  - q: 'What is the ACC earners'' levy rate in New Zealand?'
    a: 'For 2024–25 the earners'' levy is $1.39 per $100 of liable earnings, paid by all NZ earners. Self-employed people also pay a work levy set by their industry classification.'
  - q: 'Is ACC levy tax-deductible for NZ sole traders?'
    a: 'Yes. The work portion of your ACC levy is fully tax-deductible as a business expense. The earners'' levy portion is not deductible.'
  - q: 'What is the maximum liable earnings for ACC?'
    a: 'The maximum liable earnings for 2024–25 is $142,283. ACC levies are only charged on income up to this threshold.'
---

## How ACC Levies Work for Self-Employed Tradies

As a self-employed person in New Zealand, you pay **three separate ACC levies** based on your liable earnings:

### 1. Work Levy
Covers workplace injuries. The rate varies significantly by trade — roofers pay more than electricians because the statistical injury risk is higher. ACC assigns each trade a **classification unit (CU)** with its own levy rate.

### 2. Earner Levy (1.33% for 2025/26)
Covers non-work injuries (e.g., a weekend sports injury, car accident outside work). Applied to all earning New Zealanders, capped at the maximum liable earnings ($139,384 for 2025/26).

### 3. Working Safer Levy (0.08%)
A flat levy that funds WorkSafe NZ's activities. Small relative to the other levies.

### How It's Collected

As a self-employed person, your ACC levies are **calculated by IRD from your tax return** and billed directly by ACC — usually twice per year. You don't pay through PAYE.

ACC sends:
- A **cover plus invoice** for the current year (estimated)
- An **end-of-year adjustment** once your actual income is known

### Is ACC Enough?

ACC only covers **accident-related** injury. It doesn't cover illness, gradual onset conditions (like back problems from years of heavy work), or mental health conditions. Read our article on [Income Protection Insurance](/articles/income-protection-insurance-nz-tradies.html) for the full picture.

### Reducing Your ACC Levies

- **ACC CoverPlus Extra** — negotiate a fixed agreed income for ACC purposes rather than actual income. Useful if your income fluctuates
- **Good employer discount** — available if you've had no claims and meet safety criteria
- **Industry training levies** — apprentices and trainees may attract reduced rates
