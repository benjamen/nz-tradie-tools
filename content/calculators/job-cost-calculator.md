---
title: "NZ Job Cost & Quote Builder"
description: "Calculate job costs, apply your markup, and produce a quote price with GST for NZ tradie jobs — with regional labour rates by city."
tags: [quoting, job cost, markup, GST, calculator, NZ]
author: "NZ Tradie Tools"
related_articles: [how-to-price-a-job-nz-tradie-guide, how-to-write-a-quote-that-wins-jobs-nz, nz-construction-recovery-2026-what-tradies-need-to-know]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Your trade</label>
      <select id="trade-sel" onchange="updateRate()">
        <option value="">— Select trade —</option>
        <option value="builders">Builder / LBP</option>
        <option value="plumbers">Plumber / Gasfitter</option>
        <option value="electricians">Electrician</option>
        <option value="painters">Painter</option>
        <option value="other">Other</option>
      </select>
    </div>
    <div class="calc-group">
      <label>City / Region</label>
      <select id="city-sel" onchange="updateRate()">
        <option value="">— Select city —</option>
        <option value="auckland">Auckland</option>
        <option value="wellington">Wellington</option>
        <option value="christchurch">Christchurch</option>
        <option value="hamilton">Hamilton</option>
        <option value="tauranga">Tauranga</option>
        <option value="dunedin">Dunedin</option>
        <option value="palmerston-north">Palmerston North</option>
        <option value="napier">Napier / Hastings</option>
        <option value="new-plymouth">New Plymouth</option>
        <option value="rotorua">Rotorua</option>
        <option value="whangarei">Whangarei</option>
        <option value="nelson">Nelson</option>
        <option value="queenstown">Queenstown</option>
        <option value="invercargill">Invercargill / Dunedin South</option>
        <option value="lower-hutt">Lower Hutt / Upper Hutt / Porirua</option>
        <option value="gisborne">Gisborne</option>
        <option value="whanganui">Whanganui</option>
      </select>
    </div>
  </div>
  <div id="rate-hint" style="display:none;background:#e8f4fd;border:1px solid #b3d9f5;border-radius:6px;padding:.75rem 1rem;margin-bottom:1rem;font-size:.9rem;color:#0055a5"></div>
  <div class="calc-grid">
    <div class="calc-group">
      <label>Labour hours</label>
      <input type="number" id="hours" value="" placeholder="e.g. 8" oninput="calcLabour()">
    </div>
    <div class="calc-group">
      <label>Hourly rate (ex GST) — $/hr</label>
      <input type="number" id="rate" value="" placeholder="e.g. 95" oninput="calcLabour()">
    </div>
    <div class="calc-group">
      <label>Labour cost (ex GST) — $</label>
      <input type="number" id="labour" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Materials cost (ex GST) — $</label>
      <input type="number" id="materials" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Subcontractor cost (ex GST) — $</label>
      <input type="number" id="sub" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Other costs (ex GST) — $</label>
      <input type="number" id="other" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Markup on labour %</label>
      <input type="number" id="labour-markup" value="20" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Markup on materials %</label>
      <input type="number" id="mat-markup" value="15" oninput="calcJob()">
    </div>
  </div>
  <div class="calc-result" id="job-result">
    <h3>Quote Summary</h3>
    <div class="result-row"><span>Labour (with markup)</span><span id="j-labour"></span></div>
    <div class="result-row"><span>Materials (with markup)</span><span id="j-mat"></span></div>
    <div class="result-row"><span>Subcontractors</span><span id="j-sub"></span></div>
    <div class="result-row"><span>Other costs</span><span id="j-other"></span></div>
    <div class="result-row"><span>Subtotal (ex GST)</span><span id="j-sub-total"></span></div>
    <div class="result-row"><span>GST (15%)</span><span id="j-gst"></span></div>
    <div class="result-row total-row"><span>Total quote price (inc GST)</span><span id="j-total"></span></div>
    <div class="result-row"><span>Your gross profit</span><span id="j-profit" class="result-highlight"></span></div>
  </div>
  <script>
  var RATES = {
    builders:     {auckland:110,wellington:100,christchurch:95,hamilton:90,tauranga:95,queenstown:115,dunedin:85,whangarei:85,"palmerston-north":85,napier:85,"new-plymouth":85,rotorua:85,nelson:90,invercargill:80,"lower-hutt":95,gisborne:80,whanganui:80,other:90},
    plumbers:     {auckland:140,wellington:130,christchurch:120,hamilton:115,tauranga:125,queenstown:145,dunedin:110,whangarei:110,"palmerston-north":110,napier:110,"new-plymouth":110,rotorua:110,nelson:115,invercargill:105,"lower-hutt":125,gisborne:105,whanganui:105,other:115},
    electricians: {auckland:130,wellington:120,christchurch:115,hamilton:110,tauranga:115,queenstown:135,dunedin:105,whangarei:105,"palmerston-north":105,napier:105,"new-plymouth":105,rotorua:105,nelson:110,invercargill:100,"lower-hutt":115,gisborne:100,whanganui:100,other:110},
    painters:     {auckland:75,wellington:70,christchurch:65,hamilton:60,tauranga:65,queenstown:80,dunedin:58,whangarei:58,"palmerston-north":58,napier:58,"new-plymouth":58,rotorua:58,nelson:60,invercargill:55,"lower-hutt":68,gisborne:55,whanganui:55,other:62},
    other:        {auckland:100,wellington:95,christchurch:90,hamilton:85,tauranga:90,queenstown:105,dunedin:80,whangarei:80,"palmerston-north":80,napier:80,"new-plymouth":80,rotorua:80,nelson:85,invercargill:75,"lower-hutt":90,gisborne:75,whanganui:75,other:85}
  };
  var RANGE = {
    builders:10, plumbers:15, electricians:12, painters:10, other:10
  };
  function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function updateRate(){
    var trade=document.getElementById('trade-sel').value;
    var city=document.getElementById('city-sel').value;
    var hint=document.getElementById('rate-hint');
    if(trade && city && RATES[trade]){
      var mid=RATES[trade][city]||RATES[trade]['other'];
      var rng=RANGE[trade]||10;
      var lo=mid-rng; var hi=mid+rng;
      var cityName=document.getElementById('city-sel').options[document.getElementById('city-sel').selectedIndex].text;
      var tradeName=document.getElementById('trade-sel').options[document.getElementById('trade-sel').selectedIndex].text;
      hint.style.display='block';
      hint.innerHTML='<strong>Typical '+tradeName+' rate in '+cityName+':</strong> $'+lo+'–$'+hi+'/hr (ex GST). We\'ve pre-filled the midpoint — adjust to your actual rate.';
      document.getElementById('rate').value=mid;
      calcLabour();
    } else {
      hint.style.display='none';
    }
  }
  function calcLabour(){
    var h=parseFloat(document.getElementById('hours').value)||0;
    var r=parseFloat(document.getElementById('rate').value)||0;
    if(h>0&&r>0){
      document.getElementById('labour').value=(h*r).toFixed(2);
    }
    calcJob();
  }
  function calcJob(){
    var lab=parseFloat(document.getElementById('labour').value)||0;
    var mat=parseFloat(document.getElementById('materials').value)||0;
    var sub=parseFloat(document.getElementById('sub').value)||0;
    var oth=parseFloat(document.getElementById('other').value)||0;
    var lm=parseFloat(document.getElementById('labour-markup').value)||0;
    var mm=parseFloat(document.getElementById('mat-markup').value)||0;
    var labCharge=lab*(1+lm/100);
    var matCharge=mat*(1+mm/100);
    var subtotal=labCharge+matCharge+sub+oth;
    var gst=subtotal*0.15;
    var total=subtotal+gst;
    var profit=(labCharge-lab)+(matCharge-mat);
    document.getElementById('j-labour').textContent=fmt(labCharge);
    document.getElementById('j-mat').textContent=fmt(matCharge);
    document.getElementById('j-sub').textContent=fmt(sub);
    document.getElementById('j-other').textContent=fmt(oth);
    document.getElementById('j-sub-total').textContent=fmt(subtotal);
    document.getElementById('j-gst').textContent=fmt(gst);
    document.getElementById('j-total').textContent=fmt(total);
    document.getElementById('j-profit').textContent=fmt(profit);
  }
  calcJob();
  </script>
---

## How to Build an Accurate Job Quote

Winning jobs is great, but winning profitable jobs is better. Many NZ tradies underprice their work because they forget to account for all costs and apply the right markup.

### Regional Labour Rates in NZ (2025)

Rates vary significantly across New Zealand. Auckland and Queenstown are consistently the most expensive due to higher overheads and demand. Use the city selector above to get the typical rate for your region.

| Trade | Auckland | Wellington | Christchurch | Hamilton | Queenstown |
|---|---|---|---|---|---|
| Builder / LBP | $100–$120/hr | $90–$110/hr | $85–$105/hr | $80–$100/hr | $105–$125/hr |
| Plumber | $125–$155/hr | $115–$145/hr | $105–$135/hr | $100–$130/hr | $130–$160/hr |
| Electrician | $118–$142/hr | $108–$132/hr | $103–$127/hr | $98–$122/hr | $123–$147/hr |
| Painter | $65–$85/hr | $60–$80/hr | $55–$75/hr | $50–$70/hr | $70–$90/hr |

### The Difference Between Markup and Margin

- **Markup** — the percentage you add on top of your cost (e.g. cost $100, markup 20% = charge $120)
- **Margin** — the percentage of the selling price that is profit (e.g. sell $120, profit $20 = 16.7% margin)

A 20% markup gives you a 16.7% gross margin — not 20%.

### What to Always Include in a Quote

1. All labour time (including travel, site prep, cleanup)
2. Materials at supplier cost — then apply your markup
3. Any subcontractor or hire costs
4. A contingency for variations (5–10% on complex jobs)
5. GST clearly shown separately

### Quote Presentation Tips

- Use a professional template — [Tradify](https://www.tradifyhq.com/) and [Fergus](https://www.fergus.com/) both produce great-looking quotes
- Always specify what's **included** and what's **excluded**
- Set a quote validity period (e.g. 30 days)
- Require a deposit on large jobs (10–20% is standard)
