---
title: "Kitchen Renovation Cost Calculator — NZ"
description: "Estimate kitchen renovation costs in New Zealand — cabinetry, benchtops, appliances, plumbing, and labour."
tags: [kitchen, renovation, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Kitchen length (m)</label><input type="number" id="k-len" placeholder="e.g. 4" oninput="calcKitchen()"></div>
    <div class="calc-group"><label>Layout</label>
      <select id="k-layout" onchange="calcKitchen()">
        <option value="1">Single run / galley</option>
        <option value="1.4" selected>L-shape</option>
        <option value="1.7">U-shape</option>
        <option value="2">Island kitchen</option>
      </select>
    </div>
    <div class="calc-group"><label>Cabinet quality</label>
      <select id="k-cab" onchange="calcKitchen()">
        <option value="600">Budget flatpack (Kaboodle etc)</option>
        <option value="1100" selected>Mid-range semi-custom</option>
        <option value="1900">Custom cabinetmaker</option>
        <option value="2800">Premium (handleless, soft-close)</option>
      </select>
    </div>
    <div class="calc-group"><label>Benchtop material</label>
      <select id="k-bench" onchange="calcKitchen()">
        <option value="400">Laminate</option>
        <option value="900" selected>Engineered stone (Caesarstone etc)</option>
        <option value="1400">Porcelain / Dekton</option>
        <option value="1800">Solid stone / granite</option>
      </select>
    </div>
    <div class="calc-group"><label>Appliance package</label>
      <select id="k-app" onchange="calcKitchen()">
        <option value="1500">Basic (Bunnings-spec)</option>
        <option value="3500" selected>Mid-range (Fisher & Paykel, Bosch)</option>
        <option value="7000">Premium (Miele, SMEG, V-ZUG)</option>
      </select>
    </div>
    <div class="calc-group"><label>Splashback</label>
      <select id="k-splash" onchange="calcKitchen()">
        <option value="300">Tile (budget)</option>
        <option value="800" selected>Glass splashback</option>
        <option value="1200">Stone / matching benchtop</option>
      </select>
    </div>
    <div class="calc-group"><label>Move plumbing / gas?</label>
      <select id="k-plumb" onchange="calcKitchen()">
        <option value="0">No — same location</option>
        <option value="1200" selected>Minor shift (&lt;1m)</option>
        <option value="3000">Major relocation</option>
      </select>
    </div>
    <div class="calc-group"><label>New flooring?</label>
      <select id="k-floor" onchange="calcKitchen()">
        <option value="0">No</option>
        <option value="800" selected>Yes</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="k-result" style="display:none">
    <h3>Estimated Kitchen Cost</h3>
    <div class="result-row"><span>Cabinetry (supply + install)</span><span id="k-cab-out"></span></div>
    <div class="result-row"><span>Benchtop</span><span id="k-bench-out"></span></div>
    <div class="result-row"><span>Appliances</span><span id="k-app-out"></span></div>
    <div class="result-row"><span>Splashback</span><span id="k-splash-out"></span></div>
    <div class="result-row"><span>Plumbing &amp; electrical</span><span id="k-pe-out"></span></div>
    <div class="result-row"><span>Flooring &amp; sundries</span><span id="k-floor-out"></span></div>
    <div class="result-row"><span>Total estimate (excl. GST)</span><span id="k-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Total incl. 15% GST</span><span id="k-gst"></span></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcKitchen(){
    var len=parseFloat(document.getElementById('k-len').value);
    if(!len||len<1){document.getElementById('k-result').style.display='none';return;}
    var layout=parseFloat(document.getElementById('k-layout').value);
    var cab=parseFloat(document.getElementById('k-cab').value);
    var bench=parseFloat(document.getElementById('k-bench').value);
    var app=parseFloat(document.getElementById('k-app').value);
    var splash=parseFloat(document.getElementById('k-splash').value);
    var plumb=parseFloat(document.getElementById('k-plumb').value);
    var floor=parseFloat(document.getElementById('k-floor').value);
    var runLen=len*layout;
    var cabTotal=runLen*cab;
    var benchTotal=runLen*bench*0.7;
    var pe=plumb+1400;
    var floorTotal=floor?(len*layout*0.8*90+400):0;
    var total=cabTotal+benchTotal+app+splash+pe+floorTotal;
    document.getElementById('k-cab-out').textContent=nzd(cabTotal);
    document.getElementById('k-bench-out').textContent=nzd(benchTotal);
    document.getElementById('k-app-out').textContent=nzd(app);
    document.getElementById('k-splash-out').textContent=nzd(splash);
    document.getElementById('k-pe-out').textContent=nzd(pe);
    document.getElementById('k-floor-out').textContent=nzd(floorTotal);
    document.getElementById('k-total').textContent=nzd(total);
    document.getElementById('k-gst').textContent=nzd(total*1.15);
    document.getElementById('k-result').style.display='';
  }
  </script>
---

## Kitchen Renovation Costs in New Zealand

Kitchens are the most value-adding renovation in any NZ home — and the most complex to price. Budget anywhere from **$15,000 for a basic refresh** to **$80,000+ for a full high-end rebuild with island**.

### Key Cost Drivers

- **Cabinetry** — the single biggest variable. Flatpack (Kaboodle/DIY) saves $5,000–$15,000 vs custom
- **Benchtops** — engineered stone is now the NZ standard at $900–$1,400/m. Laminate is cheapest; porcelain slab is the premium choice
- **Appliances** — don't skimp on the rangehood; cheap ones cause ventilation issues. Budget $3,500–$7,000 for a quality package
- **Plumbing moves** — keeping sink in the same location saves $1,500–$3,000. Moving gas is even more expensive

### Typical Cost Ranges

| Kitchen size | Budget | Mid-range | Premium |
|---|---|---|---|
| Small (under 10m²) | $15,000–$22,000 | $25,000–$38,000 | $40,000–$65,000 |
| Medium (10–18m²) | $20,000–$32,000 | $35,000–$55,000 | $55,000–$90,000 |
| Large / island (18m²+) | $28,000–$45,000 | $48,000–$75,000 | $75,000–$130,000+ |

### LBP Requirement

If your kitchen renovation involves structural changes (removing walls), you need an [LBP-licensed builder](/trades/builders/). Check our [quotes guide](/articles/how-to-write-a-quote-that-wins-jobs-nz.html) before signing anything.
