---
title: "Irrigation System Calculator — NZ"
description: "Calculate irrigation pipe lengths, sprinkler head spacing, flow rates, and system cost for NZ gardens and lawns."
tags: [irrigation, sprinkler, calculator, NZ, landscaping]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchIRTab('lawn')">Lawn Sprinklers</button>
    <button class="calc-tab" onclick="switchIRTab('drip')">Drip Irrigation</button>
    <button class="calc-tab" onclick="switchIRTab('cost')">System Cost</button>
  </div>
  <div id="irtab-lawn">
    <div class="calc-grid">
      <div class="calc-group"><label>Lawn area (m²)</label><input type="number" id="ls-area" placeholder="e.g. 150" oninput="calcLawn()"></div>
      <div class="calc-group"><label>Sprinkler type</label>
        <select id="ls-type" onchange="calcLawn()">
          <option value="pop-up" selected>Pop-up rotary (4m radius)</option>
          <option value="fixed">Fixed spray (2.5m radius)</option>
          <option value="rotor">Hunter rotor (5m radius)</option>
        </select>
      </div>
      <div class="calc-group"><label>Water pressure (bar)</label>
        <select id="ls-press" onchange="calcLawn()">
          <option value="low">Low (1–2 bar)</option>
          <option value="med" selected>Medium (2–4 bar)</option>
          <option value="high">High (4+ bar)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ls-result" style="display:none">
      <h3>Lawn Irrigation</h3>
      <div class="result-row"><span>Sprinkler heads required</span><span id="ls-heads" class="result-highlight"></span></div>
      <div class="result-row"><span>Flow rate per zone (L/min)</span><span id="ls-flow"></span></div>
      <div class="result-row"><span>Estimated zones needed</span><span id="ls-zones"></span></div>
      <div class="result-row"><span>Pipe run estimate</span><span id="ls-pipe"></span></div>
      <div class="result-row"><span>Daily water use (15min/zone)</span><span id="ls-water"></span></div>
    </div>
  </div>
  <div id="irtab-drip" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Garden bed area (m²)</label><input type="number" id="dr-area" placeholder="e.g. 30" oninput="calcDrip()"></div>
      <div class="calc-group"><label>Emitter spacing (m)</label>
        <select id="dr-sp" onchange="calcDrip()">
          <option value="0.3">300mm (dense planting)</option>
          <option value="0.45" selected>450mm (standard)</option>
          <option value="0.6">600mm (shrubs / trees)</option>
        </select>
      </div>
      <div class="calc-group"><label>Emitter flow rate (L/hr)</label>
        <select id="dr-lhr" onchange="calcDrip()">
          <option value="2" selected>2 L/hr (standard)</option>
          <option value="4">4 L/hr</option>
          <option value="8">8 L/hr (trees)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="dr-result" style="display:none">
      <h3>Drip Irrigation</h3>
      <div class="result-row"><span>Emitters required</span><span id="dr-emit" class="result-highlight"></span></div>
      <div class="result-row"><span>Total flow rate</span><span id="dr-flow"></span></div>
      <div class="result-row"><span>Drip tape / supply line (lm)</span><span id="dr-pipe"></span></div>
      <div class="result-row"><span>Water use per hour</span><span id="dr-water"></span></div>
    </div>
  </div>
  <div id="irtab-cost" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Total lawn area (m²)</label><input type="number" id="sc-lawn" placeholder="e.g. 200" oninput="calcSysCost()"></div>
      <div class="calc-group"><label>Garden bed area (m²)</label><input type="number" id="sc-beds" placeholder="e.g. 50" value="0" oninput="calcSysCost()"></div>
      <div class="calc-group"><label>Include controller?</label>
        <select id="sc-ctrl" onchange="calcSysCost()">
          <option value="350" selected>Yes — smart WiFi controller</option>
          <option value="150">Yes — basic timer</option>
          <option value="0">No</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="sc-result" style="display:none">
      <h3>Irrigation System Cost Estimate</h3>
      <div class="result-row"><span>Materials (heads, pipe, fittings)</span><span id="sc-mat"></span></div>
      <div class="result-row"><span>Controller</span><span id="sc-ctrl-out"></span></div>
      <div class="result-row"><span>Labour (installation)</span><span id="sc-lab"></span></div>
      <div class="result-row"><span>Total estimate</span><span id="sc-total" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchIRTab(t){
    ['lawn','drip','cost'].forEach(function(id){document.getElementById('irtab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['lawn','drip','cost'][i]===t);});
  }
  function calcLawn(){
    var area=parseFloat(document.getElementById('ls-area').value)||0;
    var type=document.getElementById('ls-type').value;
    var press=document.getElementById('ls-press').value;
    if(!area){document.getElementById('ls-result').style.display='none';return;}
    var radii={popup:4,fixed:2.5,rotor:5};
    var radius=radii[type.replace('-','')]||4;
    var coverage=Math.PI*radius*radius*0.75;
    var heads=Math.ceil(area/coverage);
    var flowPerHead={low:8,med:12,high:16};
    var flow=flowPerHead[press];
    var maxPerZone=press==='low'?3:press==='med'?5:8;
    var zones=Math.ceil(heads/maxPerZone);
    var pipe=Math.sqrt(area)*4;
    var water=heads*flow*15*zones;
    document.getElementById('ls-heads').textContent=heads+' heads ('+radius+'m radius)';
    document.getElementById('ls-flow').textContent=(flow*maxPerZone)+' L/min per zone';
    document.getElementById('ls-zones').textContent=zones+' zones';
    document.getElementById('ls-pipe').textContent=pipe.toFixed(0)+' lm (approx)';
    document.getElementById('ls-water').textContent=water.toFixed(0)+' L/day';
    document.getElementById('ls-result').style.display='';
  }
  function calcDrip(){
    var area=parseFloat(document.getElementById('dr-area').value)||0;
    var sp=parseFloat(document.getElementById('dr-sp').value);
    var lhr=parseFloat(document.getElementById('dr-lhr').value);
    if(!area){document.getElementById('dr-result').style.display='none';return;}
    var emits=Math.ceil(area/(sp*sp));
    var flow=emits*lhr;
    var pipe=Math.sqrt(area)*3;
    document.getElementById('dr-emit').textContent=emits+' emitters';
    document.getElementById('dr-flow').textContent=flow.toFixed(0)+' L/hr';
    document.getElementById('dr-pipe').textContent=pipe.toFixed(0)+' lm supply line';
    document.getElementById('dr-water').textContent=flow.toFixed(0)+' L/hr run time';
    document.getElementById('dr-result').style.display='';
  }
  function calcSysCost(){
    var lawn=parseFloat(document.getElementById('sc-lawn').value)||0;
    var beds=parseFloat(document.getElementById('sc-beds').value)||0;
    var ctrl=parseFloat(document.getElementById('sc-ctrl').value);
    if(!lawn&&!beds){document.getElementById('sc-result').style.display='none';return;}
    var mat=(lawn*8)+(beds*6)+ctrl;
    var lab=(lawn+beds)*6+800;
    var total=mat+lab;
    document.getElementById('sc-mat').textContent=nzd(mat-ctrl);
    document.getElementById('sc-ctrl-out').textContent=nzd(ctrl);
    document.getElementById('sc-lab').textContent=nzd(lab);
    document.getElementById('sc-total').textContent=nzd(total)+' – '+nzd(total*1.2);
    document.getElementById('sc-result').style.display='';
  }
  </script>
---

## Irrigation in New Zealand

A well-designed irrigation system saves water, time, and keeps your garden thriving through NZ's dry summers — especially in the East Coast, Canterbury, and Central Otago regions.

### Water Use Considerations

- NZ average summer lawn water need: **25–30mm/week**
- At 25mm/week, a 200m² lawn needs **5,000 litres per week**
- Smart controllers with **soil moisture sensors** can cut water use by 30–50%

### Typical Irrigation System Costs

| System type | Cost per m² | Typical 200m² job |
|---|---|---|
| Basic pop-up lawn | $12–$18 | $2,400–$3,600 |
| Rotor system (large areas) | $10–$15 | $2,000–$3,000 |
| Drip irrigation (garden beds) | $8–$14 | per m² |
| Full smart system (wifi controller) | $18–$28 | $3,600–$5,600+ |

### Council Water Restrictions

Most NZ councils have seasonal water restriction bylaws — check before designing an irrigation system that relies on town supply. Water meters are now mandatory on all new NZ connections.

Find [irrigation specialists](/trades/irrigation-specialists/) for your project.
