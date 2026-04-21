---
title: "Roof Area Calculator — NZ"
description: "Calculate actual roof area from your house footprint and roof pitch. Works for gable, hip, and skillion roofs."
tags: [roofing, calculator, NZ, roof area, builder]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchRTab('gable')">Gable Roof</button>
    <button class="calc-tab" onclick="switchRTab('hip')">Hip Roof</button>
    <button class="calc-tab" onclick="switchRTab('skillion')">Skillion / Flat</button>
  </div>
  <div id="rtab-gable">
    <div class="calc-grid">
      <div class="calc-group"><label>House length (m)</label><input type="number" id="g-len" placeholder="e.g. 15" oninput="calcGable()"></div>
      <div class="calc-group"><label>House width (m)</label><input type="number" id="g-wid" placeholder="e.g. 10" oninput="calcGable()"></div>
      <div class="calc-group"><label>Roof pitch (degrees)</label><input type="number" id="g-pitch" placeholder="e.g. 25" oninput="calcGable()"></div>
      <div class="calc-group"><label>Eave overhang (m)</label><input type="number" id="g-eave" placeholder="e.g. 0.6" value="0.6" oninput="calcGable()"></div>
    </div>
    <div class="calc-result" id="g-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Plan area (footprint)</span><span id="g-plan"></span></div>
      <div class="result-row"><span>Pitch multiplier</span><span id="g-mult"></span></div>
      <div class="result-row"><span>Actual roof area</span><span id="g-area"></span></div>
      <div class="result-row"><span>With 10% wastage</span><span id="g-areaw"></span></div>
    </div>
  </div>
  <div id="rtab-hip" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>House length (m)</label><input type="number" id="h-len" placeholder="e.g. 15" oninput="calcHip()"></div>
      <div class="calc-group"><label>House width (m)</label><input type="number" id="h-wid" placeholder="e.g. 10" oninput="calcHip()"></div>
      <div class="calc-group"><label>Roof pitch (degrees)</label><input type="number" id="h-pitch" placeholder="e.g. 20" oninput="calcHip()"></div>
      <div class="calc-group"><label>Eave overhang (m)</label><input type="number" id="h-eave" placeholder="e.g. 0.6" value="0.6" oninput="calcHip()"></div>
    </div>
    <div class="calc-result" id="h-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Plan area</span><span id="h-plan"></span></div>
      <div class="result-row"><span>Actual roof area</span><span id="h-area"></span></div>
      <div class="result-row"><span>With 10% wastage</span><span id="h-areaw"></span></div>
    </div>
  </div>
  <div id="rtab-skillion" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Roof length (m)</label><input type="number" id="sk-len" placeholder="e.g. 10" oninput="calcSkillion()"></div>
      <div class="calc-group"><label>Roof width (m)</label><input type="number" id="sk-wid" placeholder="e.g. 8" oninput="calcSkillion()"></div>
      <div class="calc-group"><label>Pitch (degrees, 0=flat)</label><input type="number" id="sk-pitch" placeholder="e.g. 5" oninput="calcSkillion()"></div>
    </div>
    <div class="calc-result" id="sk-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Actual roof area</span><span id="sk-area"></span></div>
      <div class="result-row"><span>With 10% wastage</span><span id="sk-areaw"></span></div>
    </div>
  </div>
  <script>
  function switchRTab(t){
    ['gable','hip','skillion'].forEach(function(id){document.getElementById('rtab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['gable','hip','skillion'][i]===t);});
  }
  function pitchMult(deg){return 1/Math.cos(deg*Math.PI/180);}
  function calcGable(){
    var l=parseFloat(document.getElementById('g-len').value)||0,
        w=parseFloat(document.getElementById('g-wid').value)||0,
        pitch=parseFloat(document.getElementById('g-pitch').value)||0,
        eave=parseFloat(document.getElementById('g-eave').value)||0.6;
    if(!l||!w){document.getElementById('g-result').style.display='none';return;}
    var lE=l+eave*2, wE=w+eave*2, plan=lE*wE, mult=pitchMult(pitch), area=plan*mult;
    document.getElementById('g-plan').textContent=plan.toFixed(1)+' m²';
    document.getElementById('g-mult').textContent=mult.toFixed(3)+' (×'+mult.toFixed(3)+')';
    document.getElementById('g-area').textContent=area.toFixed(1)+' m²';
    document.getElementById('g-areaw').textContent=(area*1.1).toFixed(1)+' m²';
    document.getElementById('g-result').style.display='';
  }
  function calcHip(){
    var l=parseFloat(document.getElementById('h-len').value)||0,
        w=parseFloat(document.getElementById('h-wid').value)||0,
        pitch=parseFloat(document.getElementById('h-pitch').value)||0,
        eave=parseFloat(document.getElementById('h-eave').value)||0.6;
    if(!l||!w){document.getElementById('h-result').style.display='none';return;}
    var lE=l+eave*2, wE=w+eave*2, plan=lE*wE, mult=pitchMult(pitch), area=plan*mult;
    document.getElementById('h-plan').textContent=plan.toFixed(1)+' m²';
    document.getElementById('h-area').textContent=area.toFixed(1)+' m²';
    document.getElementById('h-areaw').textContent=(area*1.1).toFixed(1)+' m²';
    document.getElementById('h-result').style.display='';
  }
  function calcSkillion(){
    var l=parseFloat(document.getElementById('sk-len').value)||0,
        w=parseFloat(document.getElementById('sk-wid').value)||0,
        pitch=parseFloat(document.getElementById('sk-pitch').value)||0;
    if(!l||!w){document.getElementById('sk-result').style.display='none';return;}
    var area=l*w*pitchMult(pitch);
    document.getElementById('sk-area').textContent=area.toFixed(1)+' m²';
    document.getElementById('sk-areaw').textContent=(area*1.1).toFixed(1)+' m²';
    document.getElementById('sk-result').style.display='';
  }
  </script>
---

## Roof Area Calculator for NZ Roofers & Builders

Calculate the actual roof area for quoting, ordering materials, or scoping a roofing job. The key factor is **pitch** — a steeper roof has significantly more area than the house footprint.

### Common NZ Roof Pitches

| Pitch (degrees) | Description | Area multiplier |
|---|---|---|
| 5° | Near flat (skillion/commercial) | 1.004× |
| 15° | Shallow residential | 1.04× |
| 20° | Common NZ residential | 1.06× |
| 25° | Medium pitch | 1.10× |
| 30° | Steep residential | 1.15× |
| 35° | Very steep | 1.22× |

### Materials Per m² (NZ)

- **Colorsteel/corrugate:** ~1.05 m² ordered per 1 m² area (5% lap wastage)
- **Concrete/clay tiles:** ~10–12 tiles per m² depending on tile size
- **Metal tiles:** ask supplier for coverage rate

### Roof Replacement Costs

See our [roof replacement cost guide](/jobs/roofing/) for Auckland, Wellington, Christchurch and more.
