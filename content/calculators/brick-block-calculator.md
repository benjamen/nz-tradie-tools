---
title: "Brick & Block Calculator — NZ"
description: "Calculate how many bricks or blocks you need for a wall, plus mortar and sand quantities. NZ standard brick and block sizes."
tags: [bricks, blocks, masonry, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchBBTab('brick')">Bricks</button>
    <button class="calc-tab" onclick="switchBBTab('block')">Concrete Blocks</button>
  </div>
  <div id="bbtab-brick">
    <div class="calc-grid">
      <div class="calc-group"><label>Wall length (m)</label><input type="number" id="br-len" placeholder="e.g. 10" oninput="calcBrick()"></div>
      <div class="calc-group"><label>Wall height (m)</label><input type="number" id="br-h" placeholder="e.g. 2.4" oninput="calcBrick()"></div>
      <div class="calc-group"><label>Wall thickness</label>
        <select id="br-thick" onchange="calcBrick()">
          <option value="1" selected>Single skin (110mm)</option>
          <option value="2">Double skin (220mm)</option>
        </select>
      </div>
      <div class="calc-group"><label>Wastage %</label><input type="number" id="br-waste" value="10" oninput="calcBrick()"></div>
      <div class="calc-group"><label>Openings area (m²)</label><input type="number" id="br-open" placeholder="e.g. 4" value="0" oninput="calcBrick()"></div>
    </div>
    <div class="calc-result" id="br-result" style="display:none">
      <h3>Brick Quantities</h3>
      <div class="result-row"><span>Wall area (less openings)</span><span id="br-area"></span></div>
      <div class="result-row"><span>Bricks required (incl. wastage)</span><span id="br-bricks" class="result-highlight"></span></div>
      <div class="result-row"><span>Mortar (bags @ 25kg)</span><span id="br-mortar"></span></div>
      <div class="result-row"><span>Sand (m³)</span><span id="br-sand"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="br-cost"></span></div>
    </div>
  </div>
  <div id="bbtab-block" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Wall length (m)</label><input type="number" id="bl-len" placeholder="e.g. 8" oninput="calcBlock()"></div>
      <div class="calc-group"><label>Wall height (m)</label><input type="number" id="bl-h" placeholder="e.g. 1.8" oninput="calcBlock()"></div>
      <div class="calc-group"><label>Block size</label>
        <select id="bl-size" onchange="calcBlock()">
          <option value="10" selected>Standard 390×190×190mm (10/m²)</option>
          <option value="12.5">390×190×140mm (12.5/m²)</option>
          <option value="16.7">390×190×90mm (16.7/m²)</option>
        </select>
      </div>
      <div class="calc-group"><label>Wastage %</label><input type="number" id="bl-waste" value="5" oninput="calcBlock()"></div>
    </div>
    <div class="calc-result" id="bl-result" style="display:none">
      <h3>Block Quantities</h3>
      <div class="result-row"><span>Wall area</span><span id="bl-area"></span></div>
      <div class="result-row"><span>Blocks required (incl. wastage)</span><span id="bl-blocks" class="result-highlight"></span></div>
      <div class="result-row"><span>Mortar (bags @ 25kg)</span><span id="bl-mortar"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="bl-cost"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchBBTab(t){
    document.getElementById('bbtab-brick').style.display=t==='brick'?'':'none';
    document.getElementById('bbtab-block').style.display=t==='block'?'':'none';
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['brick','block'][i]===t);});
  }
  function calcBrick(){
    var len=parseFloat(document.getElementById('br-len').value)||0;
    var h=parseFloat(document.getElementById('br-h').value)||0;
    var thick=parseInt(document.getElementById('br-thick').value);
    var waste=parseFloat(document.getElementById('br-waste').value)||10;
    var open=parseFloat(document.getElementById('br-open').value)||0;
    if(!len||!h){document.getElementById('br-result').style.display='none';return;}
    var area=(len*h-open)*thick;
    var bricksPerM2=thick===1?48:96;
    var bricks=Math.ceil(area*bricksPerM2*(1+waste/100));
    var mortarBags=Math.ceil(area*0.02*thick*42);
    var sand=+(area*0.007*thick).toFixed(2);
    var cost=bricks*0.95+mortarBags*12+sand*80;
    document.getElementById('br-area').textContent=(len*h-open).toFixed(2)+' m²';
    document.getElementById('br-bricks').textContent=bricks.toLocaleString()+' bricks';
    document.getElementById('br-mortar').textContent=mortarBags+' bags';
    document.getElementById('br-sand').textContent=sand+' m³';
    document.getElementById('br-cost').textContent=nzd(cost)+' (supply only)';
    document.getElementById('br-result').style.display='';
  }
  function calcBlock(){
    var len=parseFloat(document.getElementById('bl-len').value)||0;
    var h=parseFloat(document.getElementById('bl-h').value)||0;
    var perM2=parseFloat(document.getElementById('bl-size').value);
    var waste=parseFloat(document.getElementById('bl-waste').value)||5;
    if(!len||!h){document.getElementById('bl-result').style.display='none';return;}
    var area=len*h;
    var blocks=Math.ceil(area*perM2*(1+waste/100));
    var mortar=Math.ceil(area*0.015*42);
    var cost=blocks*4.5+mortar*12;
    document.getElementById('bl-area').textContent=area.toFixed(2)+' m²';
    document.getElementById('bl-blocks').textContent=blocks.toLocaleString()+' blocks';
    document.getElementById('bl-mortar').textContent=mortar+' bags';
    document.getElementById('bl-cost').textContent=nzd(cost)+' (supply only)';
    document.getElementById('bl-result').style.display='';
  }
  </script>
---

## NZ Brick & Block Sizes

### Standard NZ Brick
- **290mm × 90mm × 76mm** (with 10mm mortar joint = 300mm × 100mm × 86mm)
- **Approximately 48 bricks per m²** (single skin)

### Concrete Blocks (NZ Standard)
- **390mm × 190mm × 190mm** — 10 per m² (most common)
- **390mm × 190mm × 140mm** — 12.5 per m²
- **390mm × 190mm × 90mm** — 16.7 per m² (partition walls)

### Mortar Mix Ratio
Standard brickwork: **1 part cement : 5 parts sand** (by volume). One 25kg bag of cement covers approximately 0.5m² of single-skin brickwork.

### Labour Rates
A skilled bricklayer charges **$70–$100/hr** in NZ. Expect **$80–$130/m²** all-in for a single-skin brick wall (supply + lay).
