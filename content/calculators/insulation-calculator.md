---
title: "Insulation Calculator — NZ R-Value & Area"
description: "Calculate how much insulation you need for your NZ home — ceiling, underfloor, and wall insulation. R-values, batts, and cost estimates."
tags: [insulation, R-value, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchITab('ceil')">Ceiling</button>
    <button class="calc-tab" onclick="switchITab('floor')">Underfloor</button>
    <button class="calc-tab" onclick="switchITab('wall')">Wall</button>
  </div>
  <div id="itab-ceil">
    <div class="calc-grid">
      <div class="calc-group"><label>House floor area (m²)</label><input type="number" id="ci-area" placeholder="e.g. 120" oninput="calcCeil()"></div>
      <div class="calc-group"><label>Climate zone</label>
        <select id="ci-zone" onchange="calcCeil()">
          <option value="6.6">Zone 1 — Auckland, Northland</option>
          <option value="6.6">Zone 2 — Waikato, Bay of Plenty, Gisborne</option>
          <option value="4.0" selected>Zone 3 — Hawke's Bay, Taranaki, Manawatu, Wellington</option>
          <option value="4.0">Zone 4 — Nelson, Marlborough, West Coast</option>
          <option value="3.3">Zone 5 — Canterbury, Otago</option>
          <option value="3.3">Zone 6 — Southland, Fiordland</option>
        </select>
      </div>
      <div class="calc-group"><label>Existing insulation?</label>
        <select id="ci-exist" onchange="calcCeil()">
          <option value="0">None</option>
          <option value="1" selected>Old / thin (pre-2000)</option>
          <option value="2">Meets current code</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ci-result" style="display:none">
      <h3>Ceiling Insulation</h3>
      <div class="result-row"><span>Minimum R-value required (NZ H1)</span><span id="ci-rval"></span></div>
      <div class="result-row"><span>Area to insulate</span><span id="ci-area-out"></span></div>
      <div class="result-row"><span>Batts required (approx)</span><span id="ci-batts"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="ci-mat"></span></div>
      <div class="result-row"><span>Estimated installed cost</span><span id="ci-install" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="itab-floor" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>House floor area (m²)</label><input type="number" id="fi-area" placeholder="e.g. 120" oninput="calcFloor()"></div>
      <div class="calc-group"><label>Floor type</label>
        <select id="fi-type" onchange="calcFloor()">
          <option value="1" selected>Suspended timber (standard)</option>
          <option value="1.3">Irregular joists / old villa</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="fi-result" style="display:none">
      <h3>Underfloor Insulation</h3>
      <div class="result-row"><span>Required R-value (NZ H1)</span><span>R 1.3</span></div>
      <div class="result-row"><span>Area to insulate</span><span id="fi-area-out"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="fi-mat"></span></div>
      <div class="result-row"><span>Estimated installed cost</span><span id="fi-install" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="itab-wall" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>External wall area (m²)</label><input type="number" id="wi-area" placeholder="e.g. 80" oninput="calcWall()"></div>
      <div class="calc-group"><label>Wall construction</label>
        <select id="wi-type" onchange="calcWall()">
          <option value="1" selected>Timber framed (new build / retrofit)</option>
          <option value="1.5">Solid / brick (retrofit blown-in)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="wi-result" style="display:none">
      <h3>Wall Insulation</h3>
      <div class="result-row"><span>Required R-value (NZ H1)</span><span>R 2.0</span></div>
      <div class="result-row"><span>Area to insulate</span><span id="wi-area-out"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="wi-mat"></span></div>
      <div class="result-row"><span>Estimated installed cost</span><span id="wi-install" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchITab(t){
    ['ceil','floor','wall'].forEach(function(id){document.getElementById('itab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['ceil','floor','wall'][i]===t);});
  }
  function calcCeil(){
    var area=parseFloat(document.getElementById('ci-area').value)||0;
    var rval=parseFloat(document.getElementById('ci-zone').value);
    var exist=parseInt(document.getElementById('ci-exist').value);
    if(!area){document.getElementById('ci-result').style.display='none';return;}
    var eff=exist===2?0:area;
    var batts=Math.ceil(eff/0.56);
    var mat=eff*(exist===0?18:12);
    var install=eff*(exist===0?28:20)+350;
    document.getElementById('ci-rval').textContent='R '+rval;
    document.getElementById('ci-area-out').textContent=eff.toFixed(1)+' m²';
    document.getElementById('ci-batts').textContent=batts+' batts';
    document.getElementById('ci-mat').textContent=nzd(mat);
    document.getElementById('ci-install').textContent=nzd(install);
    document.getElementById('ci-result').style.display='';
  }
  function calcFloor(){
    var area=parseFloat(document.getElementById('fi-area').value)||0;
    var mult=parseFloat(document.getElementById('fi-type').value);
    if(!area){document.getElementById('fi-result').style.display='none';return;}
    var eff=area*mult;
    document.getElementById('fi-area-out').textContent=area.toFixed(1)+' m²';
    document.getElementById('fi-mat').textContent=nzd(eff*14);
    document.getElementById('fi-install').textContent=nzd(eff*22+300);
    document.getElementById('fi-result').style.display='';
  }
  function calcWall(){
    var area=parseFloat(document.getElementById('wi-area').value)||0;
    var mult=parseFloat(document.getElementById('wi-type').value);
    if(!area){document.getElementById('wi-result').style.display='none';return;}
    document.getElementById('wi-area-out').textContent=area.toFixed(1)+' m²';
    document.getElementById('wi-mat').textContent=nzd(area*16*mult);
    document.getElementById('wi-install').textContent=nzd(area*30*mult+400);
    document.getElementById('wi-result').style.display='';
  }
  </script>
---

## NZ Insulation Requirements (H1 2023)

The NZ Building Code clause H1 (Energy Efficiency) was significantly updated in 2023, raising minimum R-values across all climate zones. All new builds and major renovations must comply.

### NZ Climate Zones

| Zone | Cities | Min ceiling R-value |
|---|---|---|
| 1 | Northland, Auckland | R 6.6 |
| 2 | Waikato, BOP, Gisborne | R 6.6 |
| 3 | Hawke's Bay, Wellington, Taranaki | R 4.0 |
| 4 | Nelson, Marlborough, West Coast | R 4.0 |
| 5 | Canterbury, Otago | R 3.3 |
| 6 | Southland, Fiordland | R 3.3 |

### Insulation Grants

Check if you qualify for **Warmer Kiwi Homes** grants — eligible homeowners can receive up to **66% subsidy** on insulation installation. Visit [EECA Energywise](https://www.energywise.govt.nz/at-home/insulate/) for details.

### Typical Installed Costs

- Ceiling insulation: **$18–$30/m²** installed
- Underfloor insulation: **$20–$28/m²** installed  
- Wall insulation (new build): **$25–$40/m²** installed
