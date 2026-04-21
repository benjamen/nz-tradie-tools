---
title: "Timber Framing Calculator — NZ (Studs, Plates & Lintels)"
description: "Calculate timber framing quantities for NZ wall, floor, and roof framing — studs, top plates, nogs, and lintels."
tags: [timber, framing, studs, calculator, NZ, building]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchTFTab('wall')">Wall Framing</button>
    <button class="calc-tab" onclick="switchTFTab('floor')">Floor Framing</button>
  </div>
  <div id="tftab-wall">
    <div class="calc-grid">
      <div class="calc-group"><label>Wall length (m)</label><input type="number" id="wf-len" placeholder="e.g. 8" oninput="calcWallFrame()"></div>
      <div class="calc-group"><label>Wall height (m)</label><input type="number" id="wf-h" placeholder="e.g. 2.4" value="2.4" oninput="calcWallFrame()"></div>
      <div class="calc-group"><label>Stud spacing</label>
        <select id="wf-sp" onchange="calcWallFrame()">
          <option value="0.4">400mm centres</option>
          <option value="0.6" selected>600mm centres</option>
        </select>
      </div>
      <div class="calc-group"><label>Number of openings</label><input type="number" id="wf-open" placeholder="e.g. 2" value="0" oninput="calcWallFrame()"></div>
      <div class="calc-group"><label>Stud size</label>
        <select id="wf-size" onchange="calcWallFrame()">
          <option value="90x45" selected>90×45mm (standard)</option>
          <option value="140x45">140×45mm (bracing / wet areas)</option>
        </select>
      </div>
      <div class="calc-group"><label>Timber cost ($/lm)</label><input type="number" id="wf-cost" placeholder="e.g. 3.20" value="3.20" oninput="calcWallFrame()"></div>
    </div>
    <div class="calc-result" id="wf-result" style="display:none">
      <h3>Wall Framing Materials</h3>
      <div class="result-row"><span>Studs</span><span id="wf-studs"></span></div>
      <div class="result-row"><span>Top &amp; bottom plates</span><span id="wf-plates"></span></div>
      <div class="result-row"><span>Noggings (1 row @ 1.2m)</span><span id="wf-nogs"></span></div>
      <div class="result-row"><span>Total lineal metres</span><span id="wf-lm"></span></div>
      <div class="result-row"><span>Material cost estimate</span><span id="wf-cost-out" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="tftab-floor" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Floor length (m)</label><input type="number" id="ff-len" placeholder="e.g. 10" oninput="calcFloorFrame()"></div>
      <div class="calc-group"><label>Floor width (m)</label><input type="number" id="ff-wid" placeholder="e.g. 8" oninput="calcFloorFrame()"></div>
      <div class="calc-group"><label>Joist spacing</label>
        <select id="ff-sp" onchange="calcFloorFrame()">
          <option value="0.4">400mm centres</option>
          <option value="0.5" selected>500mm centres</option>
          <option value="0.6">600mm centres</option>
        </select>
      </div>
      <div class="calc-group"><label>Joist size</label>
        <select id="ff-size" onchange="calcFloorFrame()">
          <option value="190x45" selected>190×45mm (up to 4m span)</option>
          <option value="240x45">240×45mm (up to 5m span)</option>
          <option value="290x45">290×45mm (up to 6m span)</option>
        </select>
      </div>
      <div class="calc-group"><label>Timber cost ($/lm)</label><input type="number" id="ff-cost" placeholder="e.g. 8.50" value="8.50" oninput="calcFloorFrame()"></div>
    </div>
    <div class="calc-result" id="ff-result" style="display:none">
      <h3>Floor Framing Materials</h3>
      <div class="result-row"><span>Joists</span><span id="ff-joists"></span></div>
      <div class="result-row"><span>Rim joists / bearers</span><span id="ff-rim"></span></div>
      <div class="result-row"><span>Blocking pieces</span><span id="ff-block"></span></div>
      <div class="result-row"><span>Total lineal metres</span><span id="ff-lm"></span></div>
      <div class="result-row"><span>Sheet flooring (m²)</span><span id="ff-sheet"></span></div>
      <div class="result-row"><span>Material cost estimate</span><span id="ff-cost-out" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchTFTab(t){
    document.getElementById('tftab-wall').style.display=t==='wall'?'':'none';
    document.getElementById('tftab-floor').style.display=t==='floor'?'':'none';
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['wall','floor'][i]===t);});
  }
  function calcWallFrame(){
    var len=parseFloat(document.getElementById('wf-len').value)||0;
    var h=parseFloat(document.getElementById('wf-h').value)||2.4;
    var sp=parseFloat(document.getElementById('wf-sp').value);
    var open=parseFloat(document.getElementById('wf-open').value)||0;
    var cost=parseFloat(document.getElementById('wf-cost').value)||3.20;
    if(!len){document.getElementById('wf-result').style.display='none';return;}
    var studs=Math.ceil(len/sp)+1+open*4;
    var plates=len*2*1.1;
    var nogs=Math.ceil(len/sp)*0.45;
    var totalLm=studs*h+plates+nogs;
    var matCost=totalLm*cost*1.1;
    document.getElementById('wf-studs').textContent=studs+' × '+h.toFixed(1)+'m';
    document.getElementById('wf-plates').textContent=(plates).toFixed(1)+' lm (top + bottom)';
    document.getElementById('wf-nogs').textContent=nogs.toFixed(1)+' lm';
    document.getElementById('wf-lm').textContent=totalLm.toFixed(1)+' lm';
    document.getElementById('wf-cost-out').textContent=nzd(matCost)+' (supply only, +10% waste)';
    document.getElementById('wf-result').style.display='';
  }
  function calcFloorFrame(){
    var len=parseFloat(document.getElementById('ff-len').value)||0;
    var wid=parseFloat(document.getElementById('ff-wid').value)||0;
    var sp=parseFloat(document.getElementById('ff-sp').value);
    var cost=parseFloat(document.getElementById('ff-cost').value)||8.50;
    if(!len||!wid){document.getElementById('ff-result').style.display='none';return;}
    var joists=Math.ceil(len/sp)+1;
    var joistsLm=joists*wid;
    var rim=(len+wid)*2;
    var blocking=Math.ceil(len/1.8)*3;
    var totalLm=joistsLm+rim+blocking*0.45;
    var sheets=Math.ceil(len*wid/3.24)*1.05;
    var matCost=totalLm*cost+sheets*55;
    document.getElementById('ff-joists').textContent=joists+' joists × '+wid.toFixed(1)+'m = '+joistsLm.toFixed(0)+' lm';
    document.getElementById('ff-rim').textContent=rim.toFixed(1)+' lm';
    document.getElementById('ff-block').textContent=blocking+' pieces';
    document.getElementById('ff-lm').textContent=totalLm.toFixed(1)+' lm (joists + rim + blocking)';
    document.getElementById('ff-sheet').textContent=Math.ceil(sheets)+' sheets (2400×1200 F7 flooring)';
    document.getElementById('ff-cost-out').textContent=nzd(matCost)+' (framing + sheet flooring supply)';
    document.getElementById('ff-result').style.display='';
  }
  </script>
---

## Timber Framing in NZ

NZ uses **NZS 3604** (Timber-framed buildings) as the primary standard for residential construction. Most framing uses **H1.2 treated radiata pine** (formerly CCA, now usually H1.2 boron treatment).

### Standard Wall Frame Specs

- **Studs:** 90×45mm @ 600mm centres (or 400mm for bracing walls)
- **Top plate:** 90×45mm × 2 (double top plate)
- **Bottom plate:** 90×45mm × 1
- **Noggings:** 90×45mm @ mid-height (approx 1.2m)
- **Lintels:** Sized by span and load — always check NZS 3604 tables

### H Grade Treatments

| Grade | Use |
|---|---|
| H1.2 | Interior framing (boron treated) |
| H3.1 | Above-ground exterior, weatherboard |
| H3.2 | Above-ground, severe exposure |
| H4 | In-ground, not critical |
| H5 | In-ground, long service life |

All structural building work requires an [LBP-licensed builder](/trades/builders/).
