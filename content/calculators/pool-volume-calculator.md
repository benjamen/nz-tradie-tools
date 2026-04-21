---
title: "Pool Volume & Chemical Calculator — NZ"
description: "Calculate your pool volume in litres, chemical doses, filter run times, and ongoing costs for NZ swimming pools."
tags: [pool, volume, chemicals, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchPTab('vol')">Volume</button>
    <button class="calc-tab" onclick="switchPTab('chem')">Chemicals</button>
    <button class="calc-tab" onclick="switchPTab('cost')">Running Costs</button>
  </div>
  <div id="ptab-vol">
    <div class="calc-grid">
      <div class="calc-group"><label>Pool shape</label>
        <select id="pl-shape" onchange="updatePoolShape()">
          <option value="rect" selected>Rectangular</option>
          <option value="round">Round / circular</option>
          <option value="oval">Oval</option>
        </select>
      </div>
      <div id="pl-rect-inputs">
        <div class="calc-grid">
          <div class="calc-group"><label>Length (m)</label><input type="number" id="pl-len" placeholder="e.g. 8" oninput="calcPool()"></div>
          <div class="calc-group"><label>Width (m)</label><input type="number" id="pl-wid" placeholder="e.g. 4" oninput="calcPool()"></div>
        </div>
      </div>
      <div id="pl-round-inputs" style="display:none">
        <div class="calc-group"><label>Diameter (m)</label><input type="number" id="pl-dia" placeholder="e.g. 6" oninput="calcPool()"></div>
      </div>
      <div class="calc-group"><label>Average depth (m)</label><input type="number" id="pl-dep" placeholder="e.g. 1.4" value="1.4" oninput="calcPool()"></div>
    </div>
    <div class="calc-result" id="pl-result" style="display:none">
      <h3>Pool Volume</h3>
      <div class="result-row"><span>Pool volume</span><span id="pl-vol" class="result-highlight"></span></div>
      <div class="result-row"><span>Surface area</span><span id="pl-surf"></span></div>
      <div class="result-row"><span>Fill time (garden hose @ 15L/min)</span><span id="pl-fill"></span></div>
      <div class="result-row"><span>Water cost to fill (@ $2.50/m³)</span><span id="pl-water"></span></div>
    </div>
  </div>
  <div id="ptab-chem" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Pool volume (litres)</label><input type="number" id="ch-vol" placeholder="e.g. 45000" oninput="calcChem()"></div>
      <div class="calc-group"><label>Current chlorine (ppm)</label><input type="number" id="ch-cl" placeholder="e.g. 0.5" oninput="calcChem()"></div>
      <div class="calc-group"><label>Target chlorine (ppm)</label><input type="number" id="ch-tgt" placeholder="e.g. 2.5" value="2.5" oninput="calcChem()"></div>
      <div class="calc-group"><label>Current pH</label><input type="number" id="ch-ph" placeholder="e.g. 7.8" oninput="calcChem()"></div>
    </div>
    <div class="calc-result" id="ch-result" style="display:none">
      <h3>Chemical Dose</h3>
      <div class="result-row"><span>Liquid chlorine to add (12.5%)</span><span id="ch-clout" class="result-highlight"></span></div>
      <div class="result-row"><span>Granular chlorine (70%)</span><span id="ch-gran"></span></div>
      <div class="result-row"><span>pH adjustment</span><span id="ch-phout"></span></div>
      <div class="result-row"><span>Ideal ranges</span><span>pH 7.2–7.6 · Cl 1.0–3.0 ppm</span></div>
    </div>
  </div>
  <div id="ptab-cost" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Pool volume (litres)</label><input type="number" id="rc-vol" placeholder="e.g. 45000" oninput="calcRunCost()"></div>
      <div class="calc-group"><label>Pump size (kW)</label><input type="number" id="rc-pump" placeholder="e.g. 0.75" value="0.75" oninput="calcRunCost()"></div>
      <div class="calc-group"><label>Pump hours/day</label><input type="number" id="rc-hrs" placeholder="e.g. 8" value="8" oninput="calcRunCost()"></div>
      <div class="calc-group"><label>Electricity rate ($/kWh)</label><input type="number" id="rc-rate" placeholder="e.g. 0.32" value="0.32" step="0.01" oninput="calcRunCost()"></div>
    </div>
    <div class="calc-result" id="rc-result" style="display:none">
      <h3>Annual Running Costs</h3>
      <div class="result-row"><span>Pump electricity (annual)</span><span id="rc-elec"></span></div>
      <div class="result-row"><span>Chemicals (est.)</span><span id="rc-chem"></span></div>
      <div class="result-row"><span>Water top-up (est. 10%/yr)</span><span id="rc-water"></span></div>
      <div class="result-row"><span>Total annual running cost</span><span id="rc-total" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchPTab(t){
    ['vol','chem','cost'].forEach(function(id){document.getElementById('ptab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['vol','chem','cost'][i]===t);});
  }
  function updatePoolShape(){
    var shape=document.getElementById('pl-shape').value;
    document.getElementById('pl-rect-inputs').style.display=shape!=='round'?'':'none';
    document.getElementById('pl-round-inputs').style.display=shape==='round'?'':'none';
    calcPool();
  }
  function calcPool(){
    var shape=document.getElementById('pl-shape').value;
    var dep=parseFloat(document.getElementById('pl-dep').value)||0;
    var vol,surf;
    if(shape==='round'){
      var dia=parseFloat(document.getElementById('pl-dia').value)||0;
      if(!dia||!dep){document.getElementById('pl-result').style.display='none';return;}
      surf=Math.PI*(dia/2)*(dia/2);
    } else {
      var len=parseFloat(document.getElementById('pl-len').value)||0;
      var wid=parseFloat(document.getElementById('pl-wid').value)||0;
      if(!len||!wid||!dep){document.getElementById('pl-result').style.display='none';return;}
      surf=shape==='oval'?Math.PI*(len/2)*(wid/2):len*wid;
    }
    vol=surf*dep*1000;
    var fillMins=vol/15;
    var fillHrs=(fillMins/60).toFixed(1);
    var waterCost=vol/1000*2.50;
    document.getElementById('pl-vol').textContent=vol.toLocaleString()+' litres ('+( vol/1000).toFixed(1)+' m³)';
    document.getElementById('pl-surf').textContent=surf.toFixed(1)+' m²';
    document.getElementById('pl-fill').textContent=fillHrs+' hours';
    document.getElementById('pl-water').textContent=nzd(waterCost);
    document.getElementById('pl-result').style.display='';
  }
  function calcChem(){
    var vol=parseFloat(document.getElementById('ch-vol').value)||0;
    var cl=parseFloat(document.getElementById('ch-cl').value)||0;
    var tgt=parseFloat(document.getElementById('ch-tgt').value)||2.5;
    var ph=parseFloat(document.getElementById('ch-ph').value)||0;
    if(!vol){document.getElementById('ch-result').style.display='none';return;}
    var needed=(tgt-cl)*vol/1000000;
    var liquid=needed/0.125*1000;
    var gran=needed/0.70*1000;
    var phTxt='';
    if(ph>7.6)phTxt='Add pH reducer (sodium bisulphate): ~'+(vol/1000000*(ph-7.4)*1.5*1000).toFixed(0)+'g';
    else if(ph<7.2)phTxt='Add pH increaser (soda ash): ~'+(vol/1000000*(7.4-ph)*1.5*1000).toFixed(0)+'g';
    else phTxt='pH OK — no adjustment needed';
    document.getElementById('ch-clout').textContent=liquid.toFixed(0)+'mL (if pH ok)';
    document.getElementById('ch-gran').textContent=gran.toFixed(0)+'g';
    document.getElementById('ch-phout').textContent=phTxt;
    document.getElementById('ch-result').style.display='';
  }
  function calcRunCost(){
    var vol=parseFloat(document.getElementById('rc-vol').value)||0;
    var pump=parseFloat(document.getElementById('rc-pump').value)||0.75;
    var hrs=parseFloat(document.getElementById('rc-hrs').value)||8;
    var rate=parseFloat(document.getElementById('rc-rate').value)||0.32;
    if(!vol){document.getElementById('rc-result').style.display='none';return;}
    var elec=pump*hrs*365*rate;
    var chem=vol/1000*12;
    var water=vol/1000*0.1*2.5*365/365*12;
    var total=elec+chem+water;
    document.getElementById('rc-elec').textContent=nzd(elec)+'/yr';
    document.getElementById('rc-chem').textContent=nzd(chem)+'/yr';
    document.getElementById('rc-water').textContent=nzd(water)+'/yr';
    document.getElementById('rc-total').textContent=nzd(total)+'/yr';
    document.getElementById('rc-result').style.display='';
  }
  </script>
---

## Pool Costs in NZ

Swimming pools are a popular addition to NZ homes — but come with significant ongoing costs. Budget well before installing.

### Pool Installation Costs (NZ 2025)

| Pool type | Typical cost (installed) |
|---|---|
| Above-ground (steel/resin) | $3,000–$10,000 |
| Fibreglass pool | $35,000–$70,000 |
| Concrete / gunite | $50,000–$120,000+ |
| Lap pool (steel panel) | $25,000–$50,000 |

### Annual Running Costs

| Pool size | Typical annual cost |
|---|---|
| Small (30,000L) | $1,200–$2,000/yr |
| Medium (50,000L) | $1,800–$3,000/yr |
| Large (80,000+L) | $2,500–$4,500/yr |

### NZ Pool Safety Requirements

Under the **Fencing of Swimming Pools Act 1987**, all residential pools must have:
- A **1.2m compliant fence** with a self-closing, self-latching gate
- Building consent for the pool and fence
- Regular inspection by your local council

Find [pool builders and fencers](/trades/pool-builders/) in your region.
