---
title: "Scaffolding Cost Calculator — NZ"
description: "Estimate scaffolding hire costs for NZ building projects — residential, commercial, and roof access."
tags: [scaffolding, hire, calculator, NZ, construction]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Building perimeter to scaffold (m)</label><input type="number" id="sc-per" placeholder="e.g. 40" oninput="calcScaff()"></div>
    <div class="calc-group"><label>Building height (m)</label>
      <select id="sc-h" onchange="calcScaff()">
        <option value="4.5">Single storey (up to 4.5m)</option>
        <option value="7.5" selected>Two storey (up to 7.5m)</option>
        <option value="10.5">Three storey (up to 10.5m)</option>
        <option value="14">Four storey+</option>
      </select>
    </div>
    <div class="calc-group"><label>Hire duration (weeks)</label><input type="number" id="sc-wks" placeholder="e.g. 4" value="4" oninput="calcScaff()"></div>
    <div class="calc-group"><label>Access type</label>
      <select id="sc-type" onchange="calcScaff()">
        <option value="1" selected>Standard perimeter scaffold</option>
        <option value="0.6">Partial / one face only</option>
        <option value="1.4">Roof scaffold with edge protection</option>
        <option value="1.8">Internal scaffold (commercial)</option>
      </select>
    </div>
    <div class="calc-group"><label>Region</label>
      <select id="sc-reg" onchange="calcScaff()">
        <option value="1.15">Auckland</option>
        <option value="1.0" selected>Wellington / Hamilton</option>
        <option value="0.95">Christchurch</option>
        <option value="0.9">Provincial / South Island</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="sc-result" style="display:none">
    <h3>Scaffolding Estimate</h3>
    <div class="result-row"><span>Scaffold area (approx)</span><span id="sc-area"></span></div>
    <div class="result-row"><span>Erect &amp; dismantle</span><span id="sc-ed"></span></div>
    <div class="result-row"><span>Weekly hire charge</span><span id="sc-week"></span></div>
    <div class="result-row"><span>Total hire (<span id="sc-wks-out"></span> weeks)</span><span id="sc-hire"></span></div>
    <div class="result-row"><span>Total estimate (excl. GST)</span><span id="sc-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Total incl. 15% GST</span><span id="sc-gst"></span></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcScaff(){
    var per=parseFloat(document.getElementById('sc-per').value)||0;
    var h=parseFloat(document.getElementById('sc-h').value);
    var wks=parseFloat(document.getElementById('sc-wks').value)||4;
    var type=parseFloat(document.getElementById('sc-type').value);
    var reg=parseFloat(document.getElementById('sc-reg').value);
    if(!per){document.getElementById('sc-result').style.display='none';return;}
    var area=per*h*type;
    var ed=(area*22+1200)*reg;
    var weeklyHire=(area*3.5)*reg;
    var hireTotal=weeklyHire*wks;
    var total=ed+hireTotal;
    document.getElementById('sc-area').textContent=area.toFixed(0)+' m²';
    document.getElementById('sc-ed').textContent=nzd(ed);
    document.getElementById('sc-week').textContent=nzd(weeklyHire)+'/wk';
    document.getElementById('sc-wks-out').textContent=wks;
    document.getElementById('sc-hire').textContent=nzd(hireTotal);
    document.getElementById('sc-total').textContent=nzd(total);
    document.getElementById('sc-gst').textContent=nzd(total*1.15);
    document.getElementById('sc-result').style.display='';
  }
  </script>
---

## Scaffolding Costs in NZ

Scaffolding is a significant cost for any multi-level building project. In NZ, scaffolding must comply with **WorkSafe NZ** requirements and the **Health and Safety at Work Act 2015**.

### Typical NZ Scaffolding Rates

| Job type | Cost range |
|---|---|
| Single storey house (erect + 4wks hire) | $1,800–$3,500 |
| Two storey house (full perimeter) | $3,500–$6,500 |
| Roof scaffold with edge protection | $2,500–$5,000 |
| Commercial project (per m²) | $25–$50/m² erected |

### When Scaffolding Is Required

Under NZ workplace safety regulations:
- **Any work at height over 1.8m** requires fall prevention
- Scaffolding is required where **catch platforms** or safety nets aren't practicable
- Scaffolding must be erected and dismantled by a **competent person**

### Scaffold Hire vs Buy

For most residential projects, hire is cheaper than buying. Only consider buying if you have multiple ongoing projects. Typical hire rates: **$3–$6 per m² per week** plus erection/dismantling.

Find [certified scaffolding contractors](/trades/scaffolders/) in your area.
