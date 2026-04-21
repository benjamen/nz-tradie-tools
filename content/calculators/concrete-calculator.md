---
title: "Concrete Calculator — NZ"
description: "Calculate how much concrete you need in m³ and 20kg bags. Covers slabs, footings, posts, and pathways."
tags: [concrete, calculator, NZ, building]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchCTab('slab')">Slab / Path</button>
    <button class="calc-tab" onclick="switchCTab('footing')">Strip Footing</button>
    <button class="calc-tab" onclick="switchCTab('post')">Post Holes</button>
  </div>
  <div id="ctab-slab">
    <div class="calc-grid">
      <div class="calc-group"><label>Length (m)</label><input type="number" id="s-len" placeholder="e.g. 6" oninput="calcSlab()"></div>
      <div class="calc-group"><label>Width (m)</label><input type="number" id="s-wid" placeholder="e.g. 4" oninput="calcSlab()"></div>
      <div class="calc-group"><label>Depth (mm)</label><input type="number" id="s-dep" placeholder="e.g. 100" oninput="calcSlab()"></div>
      <div class="calc-group"><label>Wastage %</label><input type="number" id="s-waste" placeholder="10" value="10" oninput="calcSlab()"></div>
    </div>
    <div class="calc-result" id="s-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Volume required</span><span id="s-m3"></span></div>
      <div class="result-row"><span>With wastage</span><span id="s-m3w"></span></div>
      <div class="result-row"><span>20kg bags (if mixing)</span><span id="s-bags"></span></div>
      <div class="result-row"><span>Estimated cost (ready-mix)</span><span id="s-cost"></span></div>
    </div>
  </div>
  <div id="ctab-footing" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Total length (m)</label><input type="number" id="f-len" placeholder="e.g. 20" oninput="calcFooting()"></div>
      <div class="calc-group"><label>Width (mm)</label><input type="number" id="f-wid" placeholder="e.g. 400" oninput="calcFooting()"></div>
      <div class="calc-group"><label>Depth (mm)</label><input type="number" id="f-dep" placeholder="e.g. 400" oninput="calcFooting()"></div>
    </div>
    <div class="calc-result" id="f-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Volume required</span><span id="f-m3"></span></div>
      <div class="result-row"><span>With 10% wastage</span><span id="f-m3w"></span></div>
      <div class="result-row"><span>20kg bags (if mixing)</span><span id="f-bags"></span></div>
    </div>
  </div>
  <div id="ctab-post" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Number of holes</label><input type="number" id="p-num" placeholder="e.g. 10" oninput="calcPost()"></div>
      <div class="calc-group"><label>Hole diameter (mm)</label><input type="number" id="p-dia" placeholder="e.g. 300" oninput="calcPost()"></div>
      <div class="calc-group"><label>Hole depth (mm)</label><input type="number" id="p-dep" placeholder="e.g. 600" oninput="calcPost()"></div>
    </div>
    <div class="calc-result" id="p-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Total volume</span><span id="p-m3"></span></div>
      <div class="result-row"><span>20kg bags total</span><span id="p-bags"></span></div>
      <div class="result-row"><span>Bags per hole</span><span id="p-bph"></span></div>
    </div>
  </div>
  <script>
  var READY_MIX_PRICE=280;
  function fmt(n){return n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function switchCTab(t){
    ['slab','footing','post'].forEach(function(id){document.getElementById('ctab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['slab','footing','post'][i]===t);});
  }
  function calcSlab(){
    var l=parseFloat(document.getElementById('s-len').value)||0,
        w=parseFloat(document.getElementById('s-wid').value)||0,
        d=parseFloat(document.getElementById('s-dep').value)||0,
        waste=(parseFloat(document.getElementById('s-waste').value)||10)/100;
    if(!l||!w||!d){document.getElementById('s-result').style.display='none';return;}
    var m3=l*w*(d/1000), m3w=m3*(1+waste), bags=Math.ceil(m3w/0.01);
    document.getElementById('s-m3').textContent=fmt(m3)+' m³';
    document.getElementById('s-m3w').textContent=fmt(m3w)+' m³';
    document.getElementById('s-bags').textContent=bags+' × 20kg bags';
    document.getElementById('s-cost').textContent='$'+fmt(m3w*READY_MIX_PRICE)+' (est. ready-mix, ex GST)';
    document.getElementById('s-result').style.display='';
  }
  function calcFooting(){
    var l=parseFloat(document.getElementById('f-len').value)||0,
        w=parseFloat(document.getElementById('f-wid').value)||0,
        d=parseFloat(document.getElementById('f-dep').value)||0;
    if(!l||!w||!d){document.getElementById('f-result').style.display='none';return;}
    var m3=l*(w/1000)*(d/1000), m3w=m3*1.1, bags=Math.ceil(m3w/0.01);
    document.getElementById('f-m3').textContent=fmt(m3)+' m³';
    document.getElementById('f-m3w').textContent=fmt(m3w)+' m³';
    document.getElementById('f-bags').textContent=bags+' × 20kg bags';
    document.getElementById('f-result').style.display='';
  }
  function calcPost(){
    var n=parseFloat(document.getElementById('p-num').value)||0,
        dia=parseFloat(document.getElementById('p-dia').value)||0,
        dep=parseFloat(document.getElementById('p-dep').value)||0;
    if(!n||!dia||!dep){document.getElementById('p-result').style.display='none';return;}
    var r=dia/2/1000, vol=Math.PI*r*r*(dep/1000), total=vol*n, bags=Math.ceil(total/0.01), bph=Math.ceil(vol/0.01);
    document.getElementById('p-m3').textContent=fmt(total)+' m³';
    document.getElementById('p-bags').textContent=bags+' × 20kg bags';
    document.getElementById('p-bph').textContent=bph+' bags per hole';
    document.getElementById('p-result').style.display='';
  }
  </script>
---

## Concrete Calculator for NZ Builders & Tradies

Use this calculator to work out how much concrete you need for slabs, paths, strip footings, or post holes. Enter your dimensions and get the volume in m³ plus the equivalent number of 20kg bags.

### Concrete Rules of Thumb

- **Slabs & paths:** 100mm deep is standard for pedestrian areas; 150mm for vehicle traffic
- **Ready-mix vs bagged:** Ready-mix is more economical for anything over 0.5 m³ — typically $260–$320/m³ in NZ
- **One 20kg bag** of dry-mix concrete yields approximately 0.01 m³
- **Always add 10% wastage** to account for uneven subgrade and spillage

### Concrete Strength Grades (NZ)

| Grade | Common Use | Typical Compressive Strength |
|---|---|---|
| 17.5 MPa | Non-structural fills | Low-load paths |
| 25 MPa | Residential slabs, paths | Standard residential |
| 30 MPa | Driveways, structural | Vehicle loads |
| 40 MPa | Commercial, structural | Heavy loads |

### Hiring a Concrete Contractor?

Check our [driveway cost guide](/jobs/driveway/) for typical NZ prices, or find a [local builder or concreter](/trades/builders/) for quotes.
