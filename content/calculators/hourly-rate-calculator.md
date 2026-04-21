---
title: "NZ Tradie Hourly Rate Calculator"
description: "Work out what to charge per hour based on your target income, overheads, and billable hours. Includes ACC levy estimates."
tags: [hourly rate, pricing, calculator, NZ]
author: "NZ Tradie Tools"
related_articles: [how-to-price-a-job-nz-tradie-guide, sole-trader-setup-guide-nz-tradies, nz-construction-recovery-2026-what-tradies-need-to-know]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Your trade</label>
      <select id="trade-sel" onchange="showMarket()">
        <option value="">— Select trade (optional) —</option>
        <option value="builders">Builder / LBP</option>
        <option value="plumbers">Plumber / Gasfitter</option>
        <option value="electricians">Electrician</option>
        <option value="painters">Painter</option>
      </select>
    </div>
    <div class="calc-group">
      <label>City / Region</label>
      <select id="city-sel" onchange="showMarket()">
        <option value="">— Select city (optional) —</option>
        <option value="auckland">Auckland</option>
        <option value="wellington">Wellington</option>
        <option value="christchurch">Christchurch</option>
        <option value="hamilton">Hamilton</option>
        <option value="tauranga">Tauranga</option>
        <option value="queenstown">Queenstown</option>
        <option value="dunedin">Dunedin</option>
        <option value="palmerston-north">Palmerston North</option>
        <option value="napier">Napier / Hastings</option>
        <option value="new-plymouth">New Plymouth</option>
        <option value="whangarei">Whangarei</option>
        <option value="nelson">Nelson</option>
        <option value="invercargill">Invercargill</option>
      </select>
    </div>
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
    showMarket();
  }
  var MKT={
    builders:     {auckland:[100,120],wellington:[90,110],christchurch:[85,105],hamilton:[80,100],tauranga:[85,105],queenstown:[105,125],dunedin:[75,95],whangarei:[75,95],"palmerston-north":[75,95],napier:[75,95],"new-plymouth":[75,95],nelson:[80,100],invercargill:[70,90]},
    plumbers:     {auckland:[125,155],wellington:[115,145],christchurch:[105,135],hamilton:[100,130],tauranga:[105,135],queenstown:[130,160],dunedin:[95,125],whangarei:[95,125],"palmerston-north":[95,125],napier:[95,125],"new-plymouth":[95,125],nelson:[100,130],invercargill:[90,120]},
    electricians: {auckland:[118,142],wellington:[108,132],christchurch:[103,127],hamilton:[98,122],tauranga:[103,127],queenstown:[123,147],dunedin:[93,117],whangarei:[93,117],"palmerston-north":[93,117],napier:[93,117],"new-plymouth":[93,117],nelson:[98,122],invercargill:[88,112]},
    painters:     {auckland:[65,85],wellington:[60,80],christchurch:[55,75],hamilton:[50,70],tauranga:[55,75],queenstown:[70,90],dunedin:[48,68],whangarei:[48,68],"palmerston-north":[48,68],napier:[48,68],"new-plymouth":[48,68],nelson:[50,70],invercargill:[45,65]}
  };
  function showMarket(){
    var trade=document.getElementById('trade-sel').value;
    var city=document.getElementById('city-sel').value;
    var box=document.getElementById('market-hint');
    if(!box)return;
    if(trade&&city&&MKT[trade]&&MKT[trade][city]){
      var r=MKT[trade][city];
      var rec=parseFloat((document.getElementById('r-rec')||{}).textContent&&document.getElementById('r-rec').textContent.replace(/[$,]/g,''))||0;
      var cityName=document.getElementById('city-sel').options[document.getElementById('city-sel').selectedIndex].text;
      var tradeName=document.getElementById('trade-sel').options[document.getElementById('trade-sel').selectedIndex].text;
      var status='';
      if(rec>0){
        if(rec<r[0]) status='<span style="color:#dc2626"> — below market rate, consider increasing</span>';
        else if(rec>r[1]) status='<span style="color:#059669"> — above market rate</span>';
        else status='<span style="color:#059669"> — within market range ✓</span>';
      }
      box.style.display='block';
      box.innerHTML='<strong>Market rate for '+tradeName+' in '+cityName+':</strong> $'+r[0]+'–$'+r[1]+'/hr (ex GST)'+status;
    } else { if(box) box.style.display='none'; }
  }
  calcRate();
  </script>
  <div id="market-hint" style="display:none;background:#e8f4fd;border:1px solid #b3d9f5;border-radius:6px;padding:.75rem 1rem;margin-top:1rem;font-size:.9rem;color:#0055a5"></div>
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
