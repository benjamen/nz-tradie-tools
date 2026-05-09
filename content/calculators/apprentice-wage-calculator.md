---
title: "Apprentice Wage Calculator — NZ Training Rates 2026"
description: "Calculate minimum and typical apprentice wages for NZ trades — by year of training, trade type, and hours worked."
tags: [apprentice, wages, training, employment, NZ, BCITO]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Trade</label>
      <select id="ap-trade" onchange="calcAP()">
        <option value="construction">Building &amp; Construction (BCITO)</option>
        <option value="electrical">Electrical (E-tec)</option>
        <option value="plumbing">Plumbing &amp; Gasfitting (PGDB)</option>
        <option value="painting">Painting &amp; Decorating</option>
        <option value="engineering">Engineering / Fabrication</option>
        <option value="other">Other trade</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Year of apprenticeship</label>
      <select id="ap-year" onchange="calcAP()">
        <option value="1">Year 1</option>
        <option value="2">Year 2</option>
        <option value="3">Year 3</option>
        <option value="4">Year 4</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Hours per week</label>
      <input type="number" id="ap-hrs" placeholder="e.g. 40" value="40" oninput="calcAP()">
    </div>
    <div class="calc-group">
      <label>Apprentice age</label>
      <select id="ap-age" onchange="calcAP()">
        <option value="adult">20 or older</option>
        <option value="youth">16–19</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="ap-result" style="display:none">
    <h3>Wage Estimate</h3>
    <div class="result-row"><span>Adult minimum wage (2026)</span><span>$23.95/hr</span></div>
    <div class="result-row"><span>Training minimum wage (80%)</span><span id="ap-min-rate"></span></div>
    <div class="result-row"><span>Typical range for this year</span><span id="ap-range"></span></div>
    <div class="result-row"><span>Estimated weekly gross (typical)</span><span id="ap-weekly" class="result-highlight"></span></div>
    <div class="result-row"><span>Estimated annual gross (typical)</span><span id="ap-annual"></span></div>
    <div class="result-row"><span>Employer KiwiSaver cost (3%)</label></span><span id="ap-ks"></span></div>
    <div class="result-row"><span>Total estimated employer cost/week</span><span id="ap-employer"></span></div>
    <div style="margin-top:.75rem;padding:.6rem;background:#fff8e1;border-radius:4px;font-size:.85rem">
      <strong>Note:</strong> The training minimum wage ($<span id="ap-min-note"></span>/hr) is the legal minimum for workers in an Industry Training Agreement of 60+ credits/year. Most employers pay above this. Rates shown are estimates — negotiate based on your trade and local market.
    </div>
  </div>
  <script>
  var AP_RANGES = {
    construction: [[19,23],[22,26],[24,29],[27,34]],
    electrical:   [[20,25],[23,28],[26,32],[29,36]],
    plumbing:     [[20,25],[23,28],[26,32],[29,36]],
    painting:     [[19,23],[21,25],[23,28],[25,31]],
    engineering:  [[19,24],[22,27],[24,30],[27,33]],
    other:        [[19,23],[21,26],[23,28],[26,32]]
  };
  var MIN_WAGE = 23.95;
  var TRAINING_RATE = MIN_WAGE * 0.80;
  function nzd(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function calcAP(){
    var trade = document.getElementById('ap-trade').value;
    var yr = parseInt(document.getElementById('ap-year').value)-1;
    var hrs = parseFloat(document.getElementById('ap-hrs').value)||40;
    var age = document.getElementById('ap-age').value;
    var range = AP_RANGES[trade][yr];
    var low = range[0], high = range[1];
    var mid = (low+high)/2;
    var weeklyMid = mid * hrs;
    var annualMid = weeklyMid * 52;
    var ks = weeklyMid * 0.03;
    var minRate = age === 'youth' ? MIN_WAGE * 0.80 : TRAINING_RATE;
    document.getElementById('ap-min-rate').textContent = nzd(minRate)+'/hr';
    document.getElementById('ap-range').textContent = '$'+low.toFixed(2)+' – $'+high.toFixed(2)+'/hr';
    document.getElementById('ap-weekly').textContent = nzd(weeklyMid)+'/week (midpoint)';
    document.getElementById('ap-annual').textContent = nzd(annualMid)+'/year';
    document.getElementById('ap-ks').textContent = nzd(ks)+'/week';
    document.getElementById('ap-employer').textContent = nzd(weeklyMid+ks);
    document.getElementById('ap-min-note').textContent = TRAINING_RATE.toFixed(2);
    document.getElementById('ap-result').style.display='';
  }
  calcAP();
  </script>
related_articles: [hiring-an-apprentice-nz-tradie-guide-2026, subcontractor-vs-employee-gateway-test-nz-2026]
faqs:
  - q: 'What is the minimum wage for NZ apprentices in 2025?'
    a: 'From 1 April 2025, the adult minimum wage in NZ is $23.15/hr. Apprentices aged 16–17 may be paid the starting-out wage of $18.52/hr for the first 200 hours or three months, whichever comes first.'
  - q: 'Do apprentices get the same pay as qualified tradies in NZ?'
    a: 'No. Apprentice pay is negotiated between employer and apprentice but must meet minimum wage. Industry guides suggest a progression from around 50–60% of a qualified rate in year 1 rising to 80–90% by year 3–4.'
  - q: 'Are apprentice wages tax-deductible for a tradie business?'
    a: 'Yes, all wage payments including apprentice wages are fully deductible as a business expense in NZ.'
  - q: 'How does a Managed Apprenticeships training contract affect wages?'
    a: 'Under BCITO or other ITOs, the training agreement sets minimum pay bands. These are minimums only — employers can and often do pay more, especially for experienced apprentices.'
---

## NZ Apprentice Wage Rates 2026

### Legal Minimum Rates

NZ has two sub-minimum wage rates that may apply to apprentices:

**Training minimum wage: $19.16/hr** (80% of $23.95 adult minimum) — applies to workers aged 20+ who are party to a recognised industry training agreement of at least 60 credits per year.

**Starting-out wage: $19.16/hr** (80% of adult minimum) — may apply to workers aged 16–19 in their first 6 months with a new employer, or those in recognised training.

Most employers in trades pay above these minimums, especially from Year 2 onward.

### Industry Training Bodies

- **BCITO** — Building and Construction Industry Training Organisation (builders, carpenters, roofers, painters)
- **E-tec** — Electrical apprenticeships
- **PGDB** — Plumbers, gasfitters and drainlayers board
- **Competenz** — Engineering, fabrication, and other trades

### What Apprentices Cost Beyond Wages

When budgeting for an apprentice, remember to include:
- **KiwiSaver** — 3% employer contribution minimum
- **ACC employer levy** — varies by trade classification
- **Holiday pay** — 8% of gross or 4 weeks annual leave
- **Training levies** — BCITO charges $50/week approximately per apprentice
- **Tool allowance** — many employers contribute toward personal tools
- **Supervision time** — experienced tradies spend time mentoring

Use our [PAYE Employee Cost Calculator](/calculators/paye-employee-calculator.html) for a full employer cost breakdown.
