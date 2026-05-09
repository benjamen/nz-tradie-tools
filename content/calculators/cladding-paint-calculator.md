---
title: "NZ Weatherboard & Cladding Paint Calculator"
description: "Calculate litres of primer, undercoat and topcoat needed for NZ weatherboard, Hardiplank and plaster cladding systems — using NZ supplier spread rates."
tags: [painting, cladding, weatherboard, Hardiplank, Resene, NZ]
author: "NZ Tradie Tools"
related_articles: [painter-pricing-guide-nz-2026, paint-calculator, how-to-price-a-job-nz-tradie-guide]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Cladding / surface type</label>
      <select id="cp-type" onchange="calcCP()">
        <option value="weatherboard-pine">Pine weatherboard (rough sawn)</option>
        <option value="weatherboard-smooth">Smooth pine / cedar bevel back</option>
        <option value="hardiplank">James Hardie Hardiplank</option>
        <option value="plaster">Plaster / Rockcote / GIB Aqualine</option>
        <option value="concrete-block">Concrete block / masonry</option>
        <option value="gib-interior">GIB board (interior walls)</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Total surface area (m²)</label>
      <input type="number" id="cp-area" placeholder="e.g. 180" oninput="calcCP()">
    </div>
    <div class="calc-group">
      <label>Job type</label>
      <select id="cp-job" onchange="calcCP()">
        <option value="new">New surface (full system)</option>
        <option value="repaint">Repaint (no primer needed)</option>
        <option value="partial">Spot repairs + repaint</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Number of topcoats</label>
      <select id="cp-coats" onchange="calcCP()">
        <option value="2">2 coats (standard)</option>
        <option value="3">3 coats (premium / new build)</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="cp-result" style="display:none">
    <h3>Paint Requirements</h3>
    <div class="result-row" style="font-weight:600"><span>Product</span><span>Litres needed</span><span>4L tins</span></div>
    <div id="cp-r-primer-row" class="result-row"><span>Primer / sealer</span><span id="cp-r-primer"></span><span id="cp-r-primer-tins"></span></div>
    <div id="cp-r-under-row" class="result-row"><span>Undercoat</span><span id="cp-r-under"></span><span id="cp-r-under-tins"></span></div>
    <div class="result-row"><span id="cp-r-top-label">Topcoat (x<span id="cp-r-coats">2</span>)</span><span id="cp-r-top"></span><span id="cp-r-top-tins"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total paint volume</span><span id="cp-r-total"></span><span id="cp-r-total-tins"></span></div>
    <p style="font-size:.8rem;color:#666;margin-top:.75rem">Spread rates based on NZ supplier data (Resene / Dulux trade guides). Add 10–15% for waste and touch-ups. Rough or absorbent surfaces will increase consumption.</p>
  </div>
  <script>
  var SURFACES={
    "weatherboard-pine":{primerRate:6,underRate:8,topRate:10,hasPrimer:true,hasUnder:true,label:"Pine weatherboard (rough)"},
    "weatherboard-smooth":{primerRate:8,underRate:10,topRate:12,hasPrimer:true,hasUnder:true,label:"Smooth weatherboard"},
    "hardiplank":{primerRate:10,underRate:0,topRate:10,hasPrimer:true,hasUnder:false,label:"Hardiplank (factory primed, touch-up)"},
    "plaster":{primerRate:10,underRate:0,topRate:10,hasPrimer:true,hasUnder:false,label:"Plaster / texture coat"},
    "concrete-block":{primerRate:5,underRate:7,topRate:8,hasPrimer:true,hasUnder:true,label:"Concrete block"},
    "gib-interior":{primerRate:12,underRate:0,topRate:12,hasPrimer:true,hasUnder:false,label:"GIB board interior"}
  };
  function tins(L){return Math.ceil(L/4);}
  function calcCP(){
    var st=document.getElementById("cp-type").value;
    var area=parseFloat(document.getElementById("cp-area").value)||0;
    var job=document.getElementById("cp-job").value;
    var coats=parseInt(document.getElementById("cp-coats").value)||2;
    var r=document.getElementById("cp-result");
    if(!area||!st){r.style.display="none";return;}
    var s=SURFACES[st];
    var primerL=0,underL=0,topL=0;
    if(job==="new"){
      primerL=s.hasPrimer?area/s.primerRate:0;
      underL=s.hasUnder?area/s.underRate:0;
      topL=area/s.topRate*coats;
    }else if(job==="repaint"){
      topL=area/s.topRate*coats;
    }else{
      primerL=s.hasPrimer?area*0.2/s.primerRate:0;
      topL=area/s.topRate*coats;
    }
    var total=primerL+underL+topL;
    var pr=document.getElementById("cp-r-primer-row");
    var ur=document.getElementById("cp-r-under-row");
    pr.style.display=primerL>0?"":"none";
    ur.style.display=underL>0?"":"none";
    document.getElementById("cp-r-primer").textContent=primerL.toFixed(1)+"L";
    document.getElementById("cp-r-primer-tins").textContent=tins(primerL)+" tins";
    document.getElementById("cp-r-under").textContent=underL.toFixed(1)+"L";
    document.getElementById("cp-r-under-tins").textContent=tins(underL)+" tins";
    document.getElementById("cp-r-coats").textContent=coats;
    document.getElementById("cp-r-top").textContent=topL.toFixed(1)+"L";
    document.getElementById("cp-r-top-tins").textContent=tins(topL)+" tins";
    document.getElementById("cp-r-total").textContent=total.toFixed(1)+"L";
    document.getElementById("cp-r-total-tins").textContent=tins(total)+" tins";
    r.style.display="";
  }
  </script>
---

## Paint Quantity for NZ Cladding Systems

Generic paint calculators use averaged spread rates that don't account for the significant differences between NZ cladding materials. Rough-sawn pine and smooth Hardiplank consume very different volumes of primer and topcoat.

### NZ Cladding Spread Rates

Spread rates (m² per litre) vary by surface porosity and texture. These are based on Resene and Dulux NZ trade data sheets:

| Surface | Primer | Topcoat (per coat) |
|---|---|---|
| Rough-sawn pine weatherboard | 6 m²/L | 10 m²/L |
| Smooth bevel-back / cedar | 8 m²/L | 12 m²/L |
| Hardiplank (factory primed) | Touch-up only | 10 m²/L |
| Plaster / texture coat | 10 m²/L | 10 m²/L |
| Concrete block | 5 m²/L | 8 m²/L |
| GIB board (interior) | 12 m²/L | 12 m²/L |

### Hardiplank System Notes

James Hardie Hardiplank comes factory-primed. For new installations, only touch-up priming of cut ends and fixing points is required — not a full primer coat. Two topcoats of an approved acrylic paint system then complete the system. Hardie recommends specific approved paint products — check [jameshardie.co.nz](https://www.jameshardie.co.nz) for the current approved products list.

### Coastal and Geothermal Areas

For properties within 500m of the coast or in geothermal zones (Rotorua area), use a paint system specifically rated for high-corrosion environments. Both Resene and Dulux have specific products for these conditions — standard exterior acrylic will degrade much faster.

### Primer Selection

- **Bare pine**: Resene Wood Primer or Dulux Weathershield Primer Sealer
- **Hardiplank cut ends**: Hardie Primer (specifically formulated for fibre cement)
- **Plaster**: alkali-resistant primer (standard acrylics can saponify on fresh plaster)
- **Concrete**: concrete sealer / block filler before topcoat
