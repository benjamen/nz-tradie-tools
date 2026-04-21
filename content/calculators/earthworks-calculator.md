---
title: "Earthworks & Excavation Calculator — NZ"
description: "Calculate excavation volumes, soil disposal costs, and fill requirements for NZ building sites."
tags: [earthworks, excavation, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchETab('cut')">Cut / Excavation</button>
    <button class="calc-tab" onclick="switchETab('fill')">Fill / Compaction</button>
    <button class="calc-tab" onclick="switchETab('strip')">Topsoil Strip</button>
  </div>
  <div id="etab-cut">
    <div class="calc-grid">
      <div class="calc-group"><label>Length (m)</label><input type="number" id="ec-len" placeholder="e.g. 15" oninput="calcCut()"></div>
      <div class="calc-group"><label>Width (m)</label><input type="number" id="ec-wid" placeholder="e.g. 8" oninput="calcCut()"></div>
      <div class="calc-group"><label>Average depth (m)</label><input type="number" id="ec-dep" placeholder="e.g. 0.5" oninput="calcCut()"></div>
      <div class="calc-group"><label>Soil type</label>
        <select id="ec-soil" onchange="calcCut()">
          <option value="1.15" selected>Light / sandy loam</option>
          <option value="1.3">Clay</option>
          <option value="1.5">Heavy clay / compacted</option>
          <option value="1.8">Rock / shale</option>
        </select>
      </div>
      <div class="calc-group"><label>Disposal distance</label>
        <select id="ec-disp" onchange="calcCut()">
          <option value="80">On-site (spread on property)</option>
          <option value="180" selected>Local tip run (&lt;20km)</option>
          <option value="320">Long haul (20–50km)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ec-result" style="display:none">
      <h3>Excavation Estimate</h3>
      <div class="result-row"><span>Volume (in-situ)</span><span id="ec-vol"></span></div>
      <div class="result-row"><span>Loose (truck) volume (+swell)</span><span id="ec-loose"></span></div>
      <div class="result-row"><span>Truck loads (8m³ tipper)</span><span id="ec-loads"></span></div>
      <div class="result-row"><span>Excavator hire (incl. operator)</span><span id="ec-hire"></span></div>
      <div class="result-row"><span>Disposal / cartage</span><span id="ec-disp-cost"></span></div>
      <div class="result-row"><span>Total estimate</span><span id="ec-total" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="etab-fill" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Length (m)</label><input type="number" id="ef-len" placeholder="e.g. 10" oninput="calcFill()"></div>
      <div class="calc-group"><label>Width (m)</label><input type="number" id="ef-wid" placeholder="e.g. 6" oninput="calcFill()"></div>
      <div class="calc-group"><label>Depth of fill (m)</label><input type="number" id="ef-dep" placeholder="e.g. 0.3" oninput="calcFill()"></div>
      <div class="calc-group"><label>Fill material</label>
        <select id="ef-mat" onchange="calcFill()">
          <option value="45" selected>AP20 (standard fill)</option>
          <option value="65">Crushed concrete</option>
          <option value="38">Selected fill (site material)</option>
          <option value="90">Engineered fill (granular)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ef-result" style="display:none">
      <h3>Fill Estimate</h3>
      <div class="result-row"><span>Volume required (compacted)</span><span id="ef-vol"></span></div>
      <div class="result-row"><span>Loose volume to order (+15%)</span><span id="ef-loose"></span></div>
      <div class="result-row"><span>Truck loads (8m³)</span><span id="ef-loads"></span></div>
      <div class="result-row"><span>Material cost</span><span id="ef-mat-cost"></span></div>
      <div class="result-row"><span>Placement + compaction</span><span id="ef-labour"></span></div>
      <div class="result-row"><span>Total estimate</span><span id="ef-total" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="etab-strip" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Area to strip (m²)</label><input type="number" id="es-area" placeholder="e.g. 200" oninput="calcStrip()"></div>
      <div class="calc-group"><label>Topsoil depth (mm)</label><input type="number" id="es-dep" placeholder="e.g. 150" value="150" oninput="calcStrip()"></div>
    </div>
    <div class="calc-result" id="es-result" style="display:none">
      <h3>Topsoil Strip</h3>
      <div class="result-row"><span>Topsoil volume</span><span id="es-vol"></span></div>
      <div class="result-row"><span>Dozer / scraper hire</span><span id="es-hire"></span></div>
      <div class="result-row"><span>Disposal (if off-site)</span><span id="es-disp"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchETab(t){
    ['cut','fill','strip'].forEach(function(id){document.getElementById('etab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['cut','fill','strip'][i]===t);});
  }
  function calcCut(){
    var len=parseFloat(document.getElementById('ec-len').value)||0;
    var wid=parseFloat(document.getElementById('ec-wid').value)||0;
    var dep=parseFloat(document.getElementById('ec-dep').value)||0;
    var swell=parseFloat(document.getElementById('ec-soil').value);
    var dispRate=parseFloat(document.getElementById('ec-disp').value);
    if(!len||!wid||!dep){document.getElementById('ec-result').style.display='none';return;}
    var vol=len*wid*dep;
    var loose=vol*swell;
    var loads=Math.ceil(loose/8);
    var hrs=Math.max(4,vol/15);
    var hire=hrs*185+600;
    var disp=loads*dispRate;
    var total=hire+disp;
    document.getElementById('ec-vol').textContent=vol.toFixed(2)+' m³';
    document.getElementById('ec-loose').textContent=loose.toFixed(2)+' m³';
    document.getElementById('ec-loads').textContent=loads+' loads';
    document.getElementById('ec-hire').textContent=nzd(hire);
    document.getElementById('ec-disp-cost').textContent=nzd(disp);
    document.getElementById('ec-total').textContent=nzd(total)+' – '+nzd(total*1.3);
    document.getElementById('ec-result').style.display='';
  }
  function calcFill(){
    var len=parseFloat(document.getElementById('ef-len').value)||0;
    var wid=parseFloat(document.getElementById('ef-wid').value)||0;
    var dep=parseFloat(document.getElementById('ef-dep').value)||0;
    var matRate=parseFloat(document.getElementById('ef-mat').value);
    if(!len||!wid||!dep){document.getElementById('ef-result').style.display='none';return;}
    var vol=len*wid*dep;
    var loose=vol*1.15;
    var loads=Math.ceil(loose/8);
    var matCost=loose*matRate+loads*60;
    var labour=vol*35+400;
    document.getElementById('ef-vol').textContent=vol.toFixed(2)+' m³';
    document.getElementById('ef-loose').textContent=loose.toFixed(2)+' m³';
    document.getElementById('ef-loads').textContent=loads+' loads';
    document.getElementById('ef-mat-cost').textContent=nzd(matCost);
    document.getElementById('ef-labour').textContent=nzd(labour);
    document.getElementById('ef-total').textContent=nzd(matCost+labour);
    document.getElementById('ef-result').style.display='';
  }
  function calcStrip(){
    var area=parseFloat(document.getElementById('es-area').value)||0;
    var dep=(parseFloat(document.getElementById('es-dep').value)||150)/1000;
    if(!area){document.getElementById('es-result').style.display='none';return;}
    var vol=area*dep;
    var hire=Math.max(600,area*3.5);
    var disp=Math.ceil(vol*1.2/8)*180;
    document.getElementById('es-vol').textContent=vol.toFixed(2)+' m³';
    document.getElementById('es-hire').textContent=nzd(hire);
    document.getElementById('es-disp').textContent=nzd(disp)+' (if off-site)';
    document.getElementById('es-result').style.display='';
  }
  </script>
---

## Earthworks in NZ — What to Know

### Swell Factors

When soil is excavated, it expands (swells). Always order fill by the **compacted volume** — the truck delivers loose material:

| Soil type | Swell factor |
|---|---|
| Light topsoil / sandy loam | 1.15 (15% more) |
| Clay | 1.30 (30% more) |
| Heavy clay / compacted | 1.50 (50% more) |
| Rock | 1.80 (80% more) |

### Typical Rates in NZ

- **Excavator hire (with operator):** $180–$220/hr
- **8m³ tipper truck + driver:** $100–$150/load local
- **AP20 fill (delivered):** $40–$55/m³
- **Tipping fees:** $60–$120/tonne depending on council

### Consent Requirements

Earthworks may require resource consent if:
- Volume exceeds **250m³** (some councils lower this)
- Site is in a sensitive area (flood zone, coastal, steep)
- Work is near a stream or wetland

Always check with your local council before beginning significant earthworks.
