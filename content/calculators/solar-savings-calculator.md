---
title: "Solar Panel Savings Calculator — NZ"
description: "Estimate how much solar panels will save you in NZ — system size, annual generation, payback period, and ROI."
tags: [solar, panels, savings, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>System size (kW)</label>
      <select id="sl-kw" onchange="calcSolar()">
        <option value="3">3 kW (approx 9 panels)</option>
        <option value="5" selected>5 kW (approx 14 panels)</option>
        <option value="6.6">6.6 kW (approx 18 panels)</option>
        <option value="10">10 kW (approx 27 panels)</option>
        <option value="13">13 kW (approx 36 panels)</option>
      </select>
    </div>
    <div class="calc-group"><label>Location</label>
      <select id="sl-loc" onchange="calcSolar()">
        <option value="1600">Auckland / Northland</option>
        <option value="1650">Bay of Plenty / Gisborne</option>
        <option value="1500" selected>Waikato / Wellington</option>
        <option value="1750">Nelson / Marlborough</option>
        <option value="1850">Hawke's Bay / Manawatu</option>
        <option value="1600">Canterbury</option>
        <option value="1450">Otago / Southland</option>
      </select>
    </div>
    <div class="calc-group"><label>Current electricity rate ($/kWh)</label><input type="number" id="sl-rate" placeholder="e.g. 0.32" value="0.32" step="0.01" oninput="calcSolar()"></div>
    <div class="calc-group"><label>Annual power bill ($)</label><input type="number" id="sl-bill" placeholder="e.g. 2400" oninput="calcSolar()"></div>
    <div class="calc-group"><label>Add battery storage?</label>
      <select id="sl-bat" onchange="calcSolar()">
        <option value="0">No</option>
        <option value="8000">Yes — 10kWh battery (~$8,000)</option>
        <option value="14000">Yes — 15kWh battery (~$14,000)</option>
      </select>
    </div>
    <div class="calc-group"><label>Export buyback rate ($/kWh)</label><input type="number" id="sl-export" placeholder="e.g. 0.12" value="0.12" step="0.01" oninput="calcSolar()"></div>
  </div>
  <div class="calc-result" id="sl-result" style="display:none">
    <h3>Solar Savings Estimate</h3>
    <div class="result-row"><span>Annual generation</span><span id="sl-gen"></span></div>
    <div class="result-row"><span>Self-consumption (est. 60%)</span><span id="sl-self"></span></div>
    <div class="result-row"><span>Export to grid (est. 40%)</span><span id="sl-exp"></span></div>
    <div class="result-row"><span>Annual savings (import avoided)</span><span id="sl-save"></span></div>
    <div class="result-row"><span>Annual export income</span><span id="sl-einc"></span></div>
    <div class="result-row"><span>Total annual benefit</span><span id="sl-total" class="result-highlight"></span></div>
    <div class="result-row"><span>System + install cost (est.)</span><span id="sl-cost"></span></div>
    <div class="result-row"><span>Simple payback period</span><span id="sl-payback"></span></div>
    <div class="result-row"><span>25-year return (no inflation)</span><span id="sl-25yr"></span></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcSolar(){
    var kw=parseFloat(document.getElementById('sl-kw').value);
    var loc=parseFloat(document.getElementById('sl-loc').value);
    var rate=parseFloat(document.getElementById('sl-rate').value)||0.32;
    var bat=parseFloat(document.getElementById('sl-bat').value)||0;
    var export_rate=parseFloat(document.getElementById('sl-export').value)||0.12;
    var annualGen=kw*loc*0.78;
    var selfPct=bat>0?0.75:0.60;
    var selfUse=annualGen*selfPct;
    var exported=annualGen*(1-selfPct);
    var savings=selfUse*rate;
    var exportInc=exported*export_rate;
    var total=savings+exportInc;
    var systemCost=kw*2200+2500+bat;
    var payback=systemCost/total;
    var ret25=total*25-systemCost;
    document.getElementById('sl-gen').textContent=Math.round(annualGen).toLocaleString()+' kWh/yr';
    document.getElementById('sl-self').textContent=Math.round(selfUse).toLocaleString()+' kWh/yr';
    document.getElementById('sl-exp').textContent=Math.round(exported).toLocaleString()+' kWh/yr';
    document.getElementById('sl-save').textContent=nzd(savings)+'/yr';
    document.getElementById('sl-einc').textContent=nzd(exportInc)+'/yr';
    document.getElementById('sl-total').textContent=nzd(total)+'/yr';
    document.getElementById('sl-cost').textContent=nzd(systemCost)+' – '+nzd(systemCost*1.15);
    document.getElementById('sl-payback').textContent=payback.toFixed(1)+' years';
    document.getElementById('sl-25yr').textContent=nzd(ret25);
    document.getElementById('sl-result').style.display='';
  }
  calcSolar();
  </script>
---

## Solar in New Zealand — Is It Worth It?

Yes, for most NZ homeowners — especially in the top of the South Island and East Coast regions which get excellent solar hours. A typical 5kW system in Nelson can generate **8,500 kWh/yr**, covering 70–80% of average household use.

### System Costs in NZ (2025)

| System size | Approx cost (installed) |
|---|---|
| 3 kW | $8,000–$12,000 |
| 5 kW | $12,000–$16,000 |
| 6.6 kW | $14,000–$19,000 |
| 10 kW | $20,000–$28,000 |
| + 10kWh battery | Add $8,000–$12,000 |

### Export Buyback Rates

NZ electricity retailers vary widely — from **$0.08 to $0.17/kWh** for solar export. Check your retailer's solar buy-back plan, or consider switching. Some retailers (Contact, Mercury, Genesis) offer dedicated solar plans.

### What to Check Before Installing

1. **Roof orientation** — north-facing roofs are ideal. East/west splits can still work well
2. **Shading** — even partial shading significantly reduces output
3. **Roof condition** — replace an aging roof before adding solar panels
4. **Grid connection** — notify your lines company before installation

All solar installers must be [REW-registered electricians](/trades/electricians/).
