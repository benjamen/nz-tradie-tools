---
title: "Paving Calculator — NZ (Pavers, Base & Sand)"
description: "Calculate how many pavers, base course, and sand you need for a NZ paving project. Includes cost estimates."
tags: [paving, pavers, calculator, NZ, landscaping]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Length (m)</label><input type="number" id="pv-len" placeholder="e.g. 6" oninput="calcPave()"></div>
    <div class="calc-group"><label>Width (m)</label><input type="number" id="pv-wid" placeholder="e.g. 4" oninput="calcPave()"></div>
    <div class="calc-group"><label>Paver size</label>
      <select id="pv-size" onchange="calcPave()">
        <option value="25">400×400mm concrete paver (6.25/m²)</option>
        <option value="40" selected>600×600mm concrete paver (2.78/m²)</option>
        <option value="35">600×300mm paver (5.56/m²)</option>
        <option value="50">200×100mm brick paver (50/m²)</option>
        <option value="22">Natural stone 600×400mm (4.17/m²)</option>
      </select>
    </div>
    <div class="calc-group"><label>Paver cost ($/m²)</label><input type="number" id="pv-cost" placeholder="e.g. 45" value="45" oninput="calcPave()"></div>
    <div class="calc-group"><label>Wastage %</label><input type="number" id="pv-waste" value="10" oninput="calcPave()"></div>
    <div class="calc-group"><label>Base course depth (mm)</label>
      <select id="pv-base" onchange="calcPave()">
        <option value="75">75mm — pedestrian only</option>
        <option value="100" selected>100mm — standard residential</option>
        <option value="150">150mm — driveway / vehicle access</option>
        <option value="200">200mm — heavy vehicle</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="pv-result" style="display:none">
    <h3>Paving Quantities</h3>
    <div class="result-row"><span>Area</span><span id="pv-area"></span></div>
    <div class="result-row"><span>Pavers (incl. wastage)</span><span id="pv-pavers"></span></div>
    <div class="result-row"><span>Base course AP20 (m³)</span><span id="pv-bc"></span></div>
    <div class="result-row"><span>Bedding sand (m³)</span><span id="pv-sand"></span></div>
    <div class="result-row"><span>Material cost estimate</span><span id="pv-mat"></span></div>
    <div class="result-row"><span>Installed cost estimate</span><span id="pv-install" class="result-highlight"></span></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcPave(){
    var len=parseFloat(document.getElementById('pv-len').value)||0;
    var wid=parseFloat(document.getElementById('pv-wid').value)||0;
    var perM2=parseFloat(document.getElementById('pv-size').value);
    var cost=parseFloat(document.getElementById('pv-cost').value)||45;
    var waste=parseFloat(document.getElementById('pv-waste').value)||10;
    var baseMm=parseFloat(document.getElementById('pv-base').value);
    if(!len||!wid){document.getElementById('pv-result').style.display='none';return;}
    var area=len*wid;
    var pavers=Math.ceil(area*perM2*(1+waste/100));
    var base=+(area*baseMm/1000*1.15).toFixed(2);
    var sand=+(area*0.04).toFixed(2);
    var matCost=area*cost*(1+waste/100)+base*55+sand*80+area*1.5;
    var install=area*65+(baseMm>=150?area*20:0)+800;
    document.getElementById('pv-area').textContent=area.toFixed(2)+' m²';
    document.getElementById('pv-pavers').textContent=pavers.toLocaleString()+' pavers';
    document.getElementById('pv-bc').textContent=base+' m³';
    document.getElementById('pv-sand').textContent=sand+' m³ (30–40mm bedding)';
    document.getElementById('pv-mat').textContent=nzd(matCost);
    document.getElementById('pv-install').textContent=nzd(matCost+install)+' – '+nzd((matCost+install)*1.2);
    document.getElementById('pv-result').style.display='';
  }
  </script>
---

## Paving in NZ — What to Budget

Paving costs vary widely depending on material choice and access. A standard concrete paver driveway is one of the most cost-effective options; natural stone adds significant expense.

### Paver Costs by Type (NZ, 2025)

| Paver type | Material cost (m²) | Installed (m²) |
|---|---|---|
| Concrete pavers (plain) | $30–$60 | $110–$160 |
| Brick / clay pavers | $55–$95 | $140–$200 |
| Natural stone (bluestone etc) | $90–$180 | $200–$320 |
| Porcelain tiles (outdoor) | $70–$140 | $170–$260 |

### Base Course Requirements

Correct base preparation is critical — poor base = sunken, cracked pavers within 2–3 years:
- **Pedestrian paths:** 75mm AP20 compacted
- **Driveways (cars):** 100–150mm AP20 compacted
- **Driveways (trucks/heavy):** 150–200mm AP20 + geotextile

### Drainage

Always design paving to drain *away* from the house at minimum **1:100 fall** (10mm per metre). Poor drainage is the #1 cause of paving failures.

Find [licensed paving contractors](/trades/concreters/) for your project.
