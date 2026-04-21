---
title: "Carpet & Flooring Calculator — NZ"
description: "Calculate carpet, vinyl, and floating floor quantities and costs for NZ homes. Includes underlay and installation."
tags: [carpet, flooring, vinyl, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchFLTab('carpet')">Carpet</button>
    <button class="calc-tab" onclick="switchFLTab('vinyl')">Vinyl / LVP</button>
    <button class="calc-tab" onclick="switchFLTab('timber')">Timber / Laminate</button>
  </div>
  <div id="fltab-carpet">
    <div class="calc-grid">
      <div class="calc-group"><label>Room length (m)</label><input type="number" id="ca-len" placeholder="e.g. 5" oninput="calcCarpet()"></div>
      <div class="calc-group"><label>Room width (m)</label><input type="number" id="ca-wid" placeholder="e.g. 4" oninput="calcCarpet()"></div>
      <div class="calc-group"><label>Carpet width (m)</label>
        <select id="ca-roll" onchange="calcCarpet()">
          <option value="3.66" selected>3.66m (standard NZ roll)</option>
          <option value="4.0">4.0m roll</option>
          <option value="5.0">5.0m roll</option>
        </select>
      </div>
      <div class="calc-group"><label>Carpet quality</label>
        <select id="ca-qual" onchange="calcCarpet()">
          <option value="25">Budget (loop pile) — $25/m²</option>
          <option value="45" selected>Mid-range (cut pile) — $45/m²</option>
          <option value="75">Premium (wool blend) — $75/m²</option>
          <option value="120">Luxury (pure wool) — $120/m²</option>
        </select>
      </div>
      <div class="calc-group"><label>Underlay</label>
        <select id="ca-ul" onchange="calcCarpet()">
          <option value="8">Budget (8mm foam) — $8/m²</option>
          <option value="15" selected>Standard (10mm rebond) — $15/m²</option>
          <option value="22">Premium (12mm high density) — $22/m²</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ca-result" style="display:none">
      <h3>Carpet Estimate</h3>
      <div class="result-row"><span>Room area</span><span id="ca-area"></span></div>
      <div class="result-row"><span>Carpet needed (roll width)</span><span id="ca-carpet"></span></div>
      <div class="result-row"><span>Carpet cost</span><span id="ca-ccost"></span></div>
      <div class="result-row"><span>Underlay cost</span><span id="ca-ucost"></span></div>
      <div class="result-row"><span>Installation</span><span id="ca-lab"></span></div>
      <div class="result-row"><span>Total estimate</span><span id="ca-total" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="fltab-vinyl" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Area (m²)</label><input type="number" id="vl-area" placeholder="e.g. 20" oninput="calcVinyl()"></div>
      <div class="calc-group"><label>Wastage %</label><input type="number" id="vl-waste" value="10" oninput="calcVinyl()"></div>
      <div class="calc-group"><label>Product type</label>
        <select id="vl-type" onchange="calcVinyl()">
          <option value="35">Vinyl plank (LVP) budget — $35/m²</option>
          <option value="55" selected>LVP mid-range — $55/m²</option>
          <option value="90">LVP premium (Hybrid) — $90/m²</option>
          <option value="25">Sheet vinyl — $25/m²</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="vl-result" style="display:none">
      <h3>Vinyl / LVP Estimate</h3>
      <div class="result-row"><span>Area to cover (incl. wastage)</span><span id="vl-area-out"></span></div>
      <div class="result-row"><span>Material cost</span><span id="vl-mat"></span></div>
      <div class="result-row"><span>Installation</span><span id="vl-lab"></span></div>
      <div class="result-row"><span>Total estimate</span><span id="vl-total" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="fltab-timber" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Area (m²)</label><input type="number" id="tm-area" placeholder="e.g. 35" oninput="calcTimber()"></div>
      <div class="calc-group"><label>Wastage %</label><input type="number" id="tm-waste" value="10" oninput="calcTimber()"></div>
      <div class="calc-group"><label>Product type</label>
        <select id="tm-type" onchange="calcTimber()">
          <option value="30">Laminate (AC4 rating) — $30/m²</option>
          <option value="60" selected>Engineered timber — $60/m²</option>
          <option value="110">Solid hardwood — $110/m²</option>
          <option value="85">NZ rimu/matai (recycled) — $85/m²</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="tm-result" style="display:none">
      <h3>Timber / Laminate Estimate</h3>
      <div class="result-row"><span>Area to cover</span><span id="tm-area-out"></span></div>
      <div class="result-row"><span>Material cost</span><span id="tm-mat"></span></div>
      <div class="result-row"><span>Underlay + installation</span><span id="tm-lab"></span></div>
      <div class="result-row"><span>Total estimate</span><span id="tm-total" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchFLTab(t){
    ['carpet','vinyl','timber'].forEach(function(id){document.getElementById('fltab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['carpet','vinyl','timber'][i]===t);});
  }
  function calcCarpet(){
    var len=parseFloat(document.getElementById('ca-len').value)||0;
    var wid=parseFloat(document.getElementById('ca-wid').value)||0;
    var roll=parseFloat(document.getElementById('ca-roll').value);
    var qual=parseFloat(document.getElementById('ca-qual').value);
    var ul=parseFloat(document.getElementById('ca-ul').value);
    if(!len||!wid){document.getElementById('ca-result').style.display='none';return;}
    var area=len*wid;
    var strips=Math.ceil(wid/roll);
    var carpetM2=strips*roll*len;
    var ccost=carpetM2*qual;
    var ucost=area*ul;
    var lab=area*18+120;
    var total=ccost+ucost+lab;
    document.getElementById('ca-area').textContent=area.toFixed(2)+' m²';
    document.getElementById('ca-carpet').textContent=carpetM2.toFixed(1)+' m² ('+strips+' strip'+( strips>1?'s':'')+' @ '+roll+'m wide)';
    document.getElementById('ca-ccost').textContent=nzd(ccost);
    document.getElementById('ca-ucost').textContent=nzd(ucost);
    document.getElementById('ca-lab').textContent=nzd(lab);
    document.getElementById('ca-total').textContent=nzd(total);
    document.getElementById('ca-result').style.display='';
  }
  function calcVinyl(){
    var area=parseFloat(document.getElementById('vl-area').value)||0;
    var waste=parseFloat(document.getElementById('vl-waste').value)||10;
    var cost=parseFloat(document.getElementById('vl-type').value);
    if(!area){document.getElementById('vl-result').style.display='none';return;}
    var eff=area*(1+waste/100);
    var mat=eff*cost;
    var lab=area*25+200;
    document.getElementById('vl-area-out').textContent=eff.toFixed(2)+' m²';
    document.getElementById('vl-mat').textContent=nzd(mat);
    document.getElementById('vl-lab').textContent=nzd(lab);
    document.getElementById('vl-total').textContent=nzd(mat+lab);
    document.getElementById('vl-result').style.display='';
  }
  function calcTimber(){
    var area=parseFloat(document.getElementById('tm-area').value)||0;
    var waste=parseFloat(document.getElementById('tm-waste').value)||10;
    var cost=parseFloat(document.getElementById('tm-type').value);
    if(!area){document.getElementById('tm-result').style.display='none';return;}
    var eff=area*(1+waste/100);
    var mat=eff*cost;
    var lab=area*35+300;
    document.getElementById('tm-area-out').textContent=eff.toFixed(2)+' m²';
    document.getElementById('tm-mat').textContent=nzd(mat);
    document.getElementById('tm-lab').textContent=nzd(lab)+' (incl. underlay)';
    document.getElementById('tm-total').textContent=nzd(mat+lab);
    document.getElementById('tm-result').style.display='';
  }
  </script>
---

## Flooring Costs in NZ (2025)

Flooring is one of the highest-impact renovations for the money. Here's what to expect:

### Cost Guide

| Type | Material (m²) | Installed (m²) |
|---|---|---|
| Budget carpet | $25–$35 | $55–$70 |
| Mid-range carpet | $45–$65 | $80–$105 |
| Premium wool carpet | $75–$150 | $110–$200 |
| Sheet vinyl | $20–$40 | $45–$70 |
| LVP / Hybrid | $45–$120 | $80–$160 |
| Laminate | $25–$45 | $55–$80 |
| Engineered timber | $55–$120 | $95–$170 |
| Solid hardwood | $90–$200 | $150–$280 |

### Carpet Roll Width

NZ standard carpet rolls are **3.66m wide**. Rooms wider than this need joins — which affects price and aesthetics. For wide rooms, consider broadloom or plan seams carefully with your carpet layer.

### What to Ask Your Flooring Contractor

- Is the subfloor included in preparation?
- What's the underlay spec (thickness, density)?
- Are transitions/edging strips included?
- What's the manufacturer's warranty?

Find [carpet layers and flooring specialists](/trades/carpet-layers/) near you.
