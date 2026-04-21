---
title: "NZ Tradie Hourly Rate Calculator"
description: "Work out what to charge per hour based on your target income, overheads, and billable hours. Includes ACC levy estimates."
tags: [hourly rate, pricing, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Desired annual income (take-home) — $</label>
      <input type="number" id="income" value="80000" oninput="calcRate()">
    </div>
    <div class="calc-group">
      <label>Billable hours per week</label>
      <input type="number" id="hours" value="35" oninput="calcRate()">
    </div>
    <div class="calc-group">
      <label>Overhead % (tools, van, insurance, etc.)</label>
      <input type="number" id="overhead" value="25" oninput="calcRate()">
    </div>
    <div class="calc-group">
      <label>Profit margin %</label>
      <input type="number" id="margin" value="15" oninput="calcRate()">
    </div>
    <div class="calc-group">
      <label>Weeks off per year (holidays, sick)</label>
      <input type="number" id="weeks-off" value="6" oninput="calcRate()">
    </div>
    <div class="calc-group">
      <label>ACC earners levy rate (2024-25)</label>
      <select id="acc" onchange="calcRate()">
        <option value="0.0139">1.39% — standard</option>
        <option value="0.02">~2% — estimate with work levy</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="rate-result">
    <h3>Your Recommended Rate</h3>
    <div class="result-row"><span>Billable weeks/year</span><span id="r-weeks"></span></div>
    <div class="result-row"><span>Billable hours/year</span><span id="r-bill-hrs"></span></div>
    <div class="result-row"><span>Income needed (gross)</span><span id="r-gross"></span></div>
    <div class="result-row"><span>Total revenue needed (with overhead &amp; margin)</span><span id="r-revenue"></span></div>
    <div class="result-row"><span>Minimum hourly rate (ex GST)</span><span id="r-min"></span></div>
    <div class="result-row"><span>Recommended rate (ex GST)</span><span id="r-rec"></span></div>
    <div class="result-row"><span>Recommended rate (inc GST)</span><span id="r-gst"></span></div>
  </div>
  <script>
  function fmt(n){return '$'+Math.round(n).toLocaleString();}
  function calcRate(){
    var income=parseFloat(document.getElementById('income').value)||80000;
    var hpw=parseFloat(document.getElementById('hours').value)||35;
    var oh=parseFloat(document.getElementById('overhead').value)||25;
    var pm=parseFloat(document.getElementById('margin').value)||15;
    var woff=parseFloat(document.getElementById('weeks-off').value)||6;
    var acc=parseFloat(document.getElementById('acc').value)||0.0139;
    var billWeeks=52-woff;
    var billHrs=billWeeks*hpw;
    // Gross income needed (before income tax, rough estimate adding ~28% for sole trader income tax + ACC)
    var grossIncome=income/(1-0.28-acc);
    var revenueNeeded=grossIncome*(1+oh/100)/(1-pm/100);
    var minRate=grossIncome/billHrs;
    var recRate=revenueNeeded/billHrs;
    document.getElementById('r-weeks').textContent=billWeeks+' weeks';
    document.getElementById('r-bill-hrs').textContent=Math.round(billHrs)+' hrs';
    document.getElementById('r-gross').textContent=fmt(grossIncome);
    document.getElementById('r-revenue').textContent=fmt(revenueNeeded);
    document.getElementById('r-min').textContent=fmt(minRate)+'/hr';
    document.getElementById('r-rec').textContent=fmt(recRate)+'/hr';
    document.getElementById('r-gst').textContent=fmt(recRate*1.15)+'/hr';
  }
  calcRate();
  </script>
---

## How to Set Your Hourly Rate as a NZ Tradie

Getting your hourly rate right is one of the most important decisions you'll make as a sole trader or small business owner. Charge too little and you'll struggle to survive. Charge too much and you'll lose jobs to competitors.

### The Formula

**Hourly rate = (Target income + Overheads + Profit) ÷ Billable hours**

### What to Include in Overheads

Most tradies underestimate overheads. Include:

- **Vehicle costs** — fuel, registration, WOF, insurance, payments
- **Tools and equipment** — purchases, repairs, replacement
- **Insurance** — public liability, professional indemnity, tool insurance
- **Phone and internet**
- **Accounting and admin** — Xero subscription, accountant fees
- **Marketing** — website, Google ads, trade directories
- **Superannuation / KiwiSaver** (if contributing as an employer or self-employed)

A good rule of thumb: overheads are 20–35% of revenue for most NZ tradies.

### ACC Levies for NZ Tradies

ACC (Accident Compensation Corporation) collects two levies from self-employed tradies:
- **Earners' levy** — ~1.39% of your liable earnings (2024–25)
- **Work levy** — varies by industry (construction ~0.8%, electrical ~0.5%)

Your total ACC bill is deducted from your gross earnings, so factor it into your rate.

### Industry Benchmarks (NZ, 2025)

| Trade | Typical rate range (ex GST) |
|---|---|
| Builder (LBP) | $75–$110/hr |
| Electrician | $80–$120/hr |
| Plumber/Gasfitter | $90–$130/hr |
| Painter | $55–$80/hr |
| Landscaper | $50–$75/hr |

Use [Tradify](https://www.tradifyhq.com/) or [Fergus](https://www.fergus.com/) to track your actual billable hours and ensure you're hitting your targets.
