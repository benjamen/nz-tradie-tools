---
title: "Asphalt Driveway Cost Calculator — NZ"
seo_title: "Free Asphalt Driveway Cost Calculator NZ 2026 — Price Per m²"
description: "Free NZ asphalt driveway cost calculator — enter your driveway size and get an instant price estimate for asphalt, chip seal or concrete. 2026 NZ rates."
tags: [asphalt, driveway, calculator, NZ, bitumen, chip seal, concrete]
author: "NZ Tradie Tools"
related_articles: [asphalt-driveway-cost-nz]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Driveway length (m)</label><input type="number" id="ad-len" placeholder="e.g. 20" oninput="calcAsphalt()"></div>
    <div class="calc-group"><label>Driveway width (m)</label><input type="number" id="ad-wid" placeholder="e.g. 4" oninput="calcAsphalt()"></div>
    <div class="calc-group"><label>Surface type</label>
      <select id="ad-type" onchange="calcAsphalt()">
        <option value="asphalt" selected>Asphalt (tarmac)</option>
        <option value="chipseal">Chip seal</option>
        <option value="concrete">Concrete</option>
      </select>
    </div>
    <div class="calc-group"><label>Existing surface condition</label>
      <select id="ad-prep" onchange="calcAsphalt()">
        <option value="good">Good base / reseal only</option>
        <option value="prep" selected>New base preparation needed</option>
        <option value="remove">Remove existing surface first</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="ad-result" style="display:none">
    <h3>Driveway Cost Estimate</h3>
    <div class="result-row"><span>Driveway area</span><span id="ad-area"></span></div>
    <div class="result-row"><span>Surface material</span><span id="ad-surface"></span></div>
    <div class="result-row"><span>Preparation cost</span><span id="ad-prep-cost"></span></div>
    <div class="result-row"><span>Surface cost</span><span id="ad-surf-cost"></span></div>
    <div class="result-row"><span>Total installed estimate</span><span id="ad-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Cost per m²</span><span id="ad-m2"></span></div>
    <p id="ad-note" style="font-size:.85rem;color:#555;margin-top:.75rem;line-height:1.5"></p>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcAsphalt(){
    var len=parseFloat(document.getElementById('ad-len').value)||0;
    var wid=parseFloat(document.getElementById('ad-wid').value)||0;
    var type=document.getElementById('ad-type').value;
    var prep=document.getElementById('ad-prep').value;
    if(!len||!wid){document.getElementById('ad-result').style.display='none';return;}
    var area=len*wid;

    // Surface rates per m² (installed, NZ 2026)
    var surfRate, surfName;
    if(type==='asphalt'){surfRate=65;surfName='Asphalt (75mm compacted)';}
    else if(type==='chipseal'){surfRate=35;surfName='Chip seal (2-coat)';}
    else{surfRate=110;surfName='Concrete (100mm, mesh reinforced)';}

    // Prep costs
    var prepCost;
    if(prep==='good'){prepCost=0;}
    else if(prep==='prep'){prepCost=area*25+800;} // subbase + compaction + mobilisation
    else{prepCost=area*45+800;} // removal + disposal + new subbase

    var surfCost=area*surfRate;
    var total=surfCost+prepCost;
    var perM2=total/area;

    var notes={
      asphalt:'Asphalt typically lasts 15–25 years in NZ with good drainage. Allow for a reseal coat ($15–25/m²) around year 10.',
      chipseal:'Chip seal is the most affordable option and common on rural driveways. Needs resealing every 7–12 years. Can be noisy on vehicles.',
      concrete:'Concrete lasts 30–40 years with minimal maintenance but costs significantly more upfront. Best for heavy vehicle use.'
    };

    document.getElementById('ad-area').textContent=area.toFixed(0)+' m²';
    document.getElementById('ad-surface').textContent=surfName;
    document.getElementById('ad-prep-cost').textContent=prepCost>0?nzd(prepCost):'Included in surface rate';
    document.getElementById('ad-surf-cost').textContent=nzd(surfCost);
    document.getElementById('ad-total').textContent=nzd(total);
    document.getElementById('ad-m2').textContent=nzd(perM2)+'/m²';
    document.getElementById('ad-note').textContent=notes[type];
    document.getElementById('ad-result').style.display='block';
  }
  </script>

calculator_js: ""
intro: |
  Use this calculator to get a ballpark cost for your new driveway in NZ. Adjust the size, surface type and site preparation to match your situation.

  Estimates are based on 2026 NZ contractor rates and include materials and labour. Get at least three quotes before proceeding — prices vary significantly by region and site access.
faq:
  - q: "How much does an asphalt driveway cost in NZ?"
    a: "A typical asphalt driveway in NZ costs $65–90/m² installed, including base preparation. A standard 4×15m driveway (60m²) runs $5,000–7,000 all up."
  - q: "Is chip seal cheaper than asphalt in NZ?"
    a: "Yes — chip seal costs around $30–45/m² vs $55–90/m² for asphalt. However, chip seal needs resealing more frequently and can be rough on bare feet."
  - q: "How long does an asphalt driveway last in NZ?"
    a: "A well-laid asphalt driveway lasts 15–25 years in NZ. UV exposure and freeze-thaw cycles in colder regions can shorten its lifespan — a reseal at year 10 extends it."
  - q: "Do I need consent for a new driveway in NZ?"
    a: "Generally no building consent is required for a residential driveway. However, if you're altering a kerb crossing or adding a new vehicle crossing you'll need approval from your local council."
  - q: "What thickness should an asphalt driveway be?"
    a: "For a residential driveway in NZ, 75mm compacted asphalt over a 150mm compacted GAP65 base is standard. Driveways used by heavy vehicles (e.g. trucks) should be 100mm+."
tags_secondary: [driveway cost, tarmac, bitumen, driveway calculator]
date: 2026-06-30
---
