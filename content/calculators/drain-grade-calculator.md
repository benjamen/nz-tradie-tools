---
title: "Drain Grade & Pipe Slope Calculator — NZ"
description: "Calculate pipe gradient, fall, and minimum grade for drainage pipes to NZ plumbing code requirements."
tags: [drain, pipe grade, plumbing, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchDGTab('grade')">Grade to Fall</button>
    <button class="calc-tab" onclick="switchDGTab('check')">Check My Pipe</button>
    <button class="calc-tab" onclick="switchDGTab('size')">Pipe Sizing</button>
  </div>
  <div id="dgtab-grade">
    <div class="calc-grid">
      <div class="calc-group"><label>Pipe length (m)</label><input type="number" id="dg-len" placeholder="e.g. 15" oninput="calcGrade()"></div>
      <div class="calc-group"><label>Grade (1 in X)</label><input type="number" id="dg-grade" placeholder="e.g. 60" value="60" oninput="calcGrade()"></div>
    </div>
    <div class="calc-result" id="dg-result" style="display:none">
      <h3>Pipe Fall</h3>
      <div class="result-row"><span>Total fall over pipe length</span><span id="dg-fall" class="result-highlight"></span></div>
      <div class="result-row"><span>Fall per metre</span><span id="dg-pm"></span></div>
      <div class="result-row"><span>Percentage grade</span><span id="dg-pct"></span></div>
      <div id="dg-code" style="margin-top:.6rem;padding:.5rem .75rem;border-radius:3px;font-size:.85rem"></div>
    </div>
  </div>
  <div id="dgtab-check" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Pipe diameter (mm)</label>
        <select id="ck-dia" onchange="calcCheck()">
          <option value="40">40mm (basin/tub)</option>
          <option value="50">50mm (shower/bath)</option>
          <option value="65">65mm</option>
          <option value="75">75mm</option>
          <option value="100" selected>100mm (sewer / main)</option>
          <option value="150">150mm</option>
        </select>
      </div>
      <div class="calc-group"><label>Pipe length (m)</label><input type="number" id="ck-len" placeholder="e.g. 12" oninput="calcCheck()"></div>
      <div class="calc-group"><label>Actual fall (mm)</label><input type="number" id="ck-fall" placeholder="e.g. 120" oninput="calcCheck()"></div>
    </div>
    <div class="calc-result" id="ck-result" style="display:none">
      <h3>Grade Check</h3>
      <div class="result-row"><span>Actual grade</span><span id="ck-actual"></span></div>
      <div class="result-row"><span>Minimum NZ code grade</span><span id="ck-min"></span></div>
      <div class="result-row"><span>Maximum recommended</span><span id="ck-max"></span></div>
      <div id="ck-status" style="margin-top:.6rem;padding:.5rem .75rem;border-radius:3px;font-size:.85rem;font-weight:700"></div>
    </div>
  </div>
  <div id="dgtab-size" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Number of fixture units</label><input type="number" id="ps-fu" placeholder="e.g. 6" oninput="calcPipeSize()"></div>
      <div class="calc-group"><label>Pipe gradient</label>
        <select id="ps-grade" onchange="calcPipeSize()">
          <option value="100">1:100</option>
          <option value="80" selected>1:80 (recommended)</option>
          <option value="60">1:60</option>
          <option value="40">1:40</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ps-result" style="display:none">
      <h3>Recommended Pipe Size</h3>
      <div class="result-row"><span>Recommended diameter</span><span id="ps-size" class="result-highlight"></span></div>
      <div class="result-row"><span>Fixture unit guide</span><span id="ps-note"></span></div>
    </div>
  </div>
  <script>
  function switchDGTab(t){
    ['grade','check','size'].forEach(function(id){document.getElementById('dgtab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['grade','check','size'][i]===t);});
  }
  function calcGrade(){
    var len=parseFloat(document.getElementById('dg-len').value)||0;
    var grade=parseFloat(document.getElementById('dg-grade').value)||60;
    if(!len){document.getElementById('dg-result').style.display='none';return;}
    var fall=len/grade*1000;
    var pct=(1/grade*100).toFixed(2);
    document.getElementById('dg-fall').textContent=fall.toFixed(0)+' mm';
    document.getElementById('dg-pm').textContent=(1000/grade).toFixed(1)+' mm/m';
    document.getElementById('dg-pct').textContent=pct+'%';
    var codeEl=document.getElementById('dg-code');
    if(grade<40){codeEl.style.background='#fef2f2';codeEl.style.borderLeft='3px solid #ef4444';codeEl.textContent='⚠ Grade steeper than 1:40 — may cause self-siphonage in NZ. Check with your plumber.';}
    else if(grade>100){codeEl.style.background='#fef2f2';codeEl.style.borderLeft='3px solid #ef4444';codeEl.textContent='⚠ Grade flatter than 1:100 — NZ code minimum is 1:80 for 100mm pipe. May not drain adequately.';}
    else{codeEl.style.background='#f0fdf4';codeEl.style.borderLeft='3px solid #22c55e';codeEl.textContent='✓ Grade is within NZ AS/NZS 3500 acceptable range.';}
    document.getElementById('dg-result').style.display='';
  }
  function calcCheck(){
    var dia=parseInt(document.getElementById('ck-dia').value);
    var len=parseFloat(document.getElementById('ck-len').value)||0;
    var fall=parseFloat(document.getElementById('ck-fall').value)||0;
    if(!len||!fall){document.getElementById('ck-result').style.display='none';return;}
    var actual=len*1000/fall;
    var mins={40:40,50:40,65:40,75:60,100:80,150:150};
    var min=mins[dia]||80;
    document.getElementById('ck-actual').textContent='1:'+actual.toFixed(0);
    document.getElementById('ck-min').textContent='1:'+min+' ('+dia+'mm NZ code)';
    document.getElementById('ck-max').textContent='1:40 (steeper may cause self-siphonage)';
    var statusEl=document.getElementById('ck-status');
    if(actual<40){statusEl.style.background='#fef2f2';statusEl.style.color='#991b1b';statusEl.textContent='✗ Too steep — risk of self-siphonage. Flatten grade or add air admittance valve.';}
    else if(actual>min){statusEl.style.background='#fef2f2';statusEl.style.color='#991b1b';statusEl.textContent='✗ Too flat — does not meet NZ minimum grade 1:'+min+'. Increase fall.';}
    else{statusEl.style.background='#f0fdf4';statusEl.style.color='#166534';statusEl.textContent='✓ Compliant with NZ AS/NZS 3500 drainage code.';}
    document.getElementById('ck-result').style.display='';
  }
  function calcPipeSize(){
    var fu=parseFloat(document.getElementById('ps-fu').value)||0;
    if(!fu){document.getElementById('ps-result').style.display='none';return;}
    var size=fu<=1?40:fu<=3?50:fu<=8?75:fu<=20?100:150;
    var notes={40:'1 FU = 1 hand basin',50:'3 FU = shower, or bath',75:'Up to 8 FU (2–3 fixtures)',100:'Up to 20 FU (branch drain)',150:'20+ FU (main sewer)'};
    document.getElementById('ps-size').textContent=size+'mm diameter';
    document.getElementById('ps-note').textContent=notes[size]||'';
    document.getElementById('ps-result').style.display='';
  }
  </script>
---

## NZ Drainage Pipe Grade Requirements

All drainage systems in NZ must comply with **AS/NZS 3500** (Plumbing and Drainage) as adopted by the NZ Building Code.

### Minimum Grades by Pipe Size

| Pipe diameter | Minimum grade | Minimum fall/m |
|---|---|---|
| 40–50mm (basin, shower) | 1:40 | 25mm/m |
| 65–80mm | 1:60 | 16.7mm/m |
| 100mm (main drain) | 1:80 | 12.5mm/m |
| 150mm (sewer) | 1:150 | 6.7mm/m |

### Why Grade Matters

- Too flat → solids settle, blockages, odours
- Too steep → water outruns solids (self-siphonage), trap seal loss
- Sweet spot for 100mm: **1:60 to 1:80**

### Fixture Units (NZ AS/NZS 3500)

| Fixture | Fixture units |
|---|---|
| Hand basin | 1 |
| Shower | 2 |
| Bath | 2 |
| WC | 4 |
| Kitchen sink | 2 |
| Dishwasher | 2 |

All drainage work must be done by a [licensed drainlayer](/trades/drainlayers/).
