---
title: "Tile Calculator — NZ"
description: "Calculate how many tiles you need for floors, walls, or splashbacks. Includes wastage and grout estimates."
tags: [tiles, calculator, NZ, tiling, flooring]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Area length (m)</label><input type="number" id="t-len" placeholder="e.g. 4" oninput="calcTile()"></div>
    <div class="calc-group"><label>Area width (m)</label><input type="number" id="t-wid" placeholder="e.g. 3" oninput="calcTile()"></div>
    <div class="calc-group"><label>Tile length (mm)</label><input type="number" id="t-tl" placeholder="e.g. 600" oninput="calcTile()"></div>
    <div class="calc-group"><label>Tile width (mm)</label><input type="number" id="t-tw" placeholder="e.g. 300" oninput="calcTile()"></div>
    <div class="calc-group"><label>Wastage %</label><input type="number" id="t-waste" placeholder="10" value="10" oninput="calcTile()"></div>
    <div class="calc-group"><label>Tile price per m² ($)</label><input type="number" id="t-price" placeholder="e.g. 45" oninput="calcTile()"></div>
  </div>
  <div class="calc-result" id="t-result" style="display:none">
    <h3>Result</h3>
    <div class="result-row"><span>Total area</span><span id="t-area"></span></div>
    <div class="result-row"><span>Area with wastage</span><span id="t-area-w"></span></div>
    <div class="result-row"><span>Tiles per m²</span><span id="t-pm2"></span></div>
    <div class="result-row"><span>Total tiles needed</span><span id="t-tiles"></span></div>
    <div class="result-row"><span>Estimated tile cost</span><span id="t-cost"></span></div>
    <div class="result-row"><span>Adhesive needed (approx)</span><span id="t-adhesive"></span></div>
  </div>
  <script>
  function calcTile(){
    var l=parseFloat(document.getElementById('t-len').value)||0,
        w=parseFloat(document.getElementById('t-wid').value)||0,
        tl=parseFloat(document.getElementById('t-tl').value)||0,
        tw=parseFloat(document.getElementById('t-tw').value)||0,
        waste=(parseFloat(document.getElementById('t-waste').value)||10)/100,
        price=parseFloat(document.getElementById('t-price').value)||0;
    if(!l||!w||!tl||!tw){document.getElementById('t-result').style.display='none';return;}
    var area=l*w, areaW=area*(1+waste);
    var tileArea=(tl/1000)*(tw/1000), pm2=1/tileArea, tiles=Math.ceil(areaW*pm2);
    document.getElementById('t-area').textContent=area.toFixed(2)+' m²';
    document.getElementById('t-area-w').textContent=areaW.toFixed(2)+' m²';
    document.getElementById('t-pm2').textContent=pm2.toFixed(1)+' tiles/m²';
    document.getElementById('t-tiles').textContent=tiles+' tiles';
    document.getElementById('t-cost').textContent=price?'$'+(areaW*price).toFixed(2)+' (materials only)':'— (enter price above)';
    document.getElementById('t-adhesive').textContent=Math.ceil(areaW/5)+' × 20kg bags tile adhesive';
    document.getElementById('t-result').style.display='';
  }
  </script>
---

## Tile Calculator for NZ Tilers & Homeowners

Work out how many tiles you need for any floor, wall, or splashback area. Always add wastage for cuts, especially with patterned layouts or diagonal installation.

### Wastage Guide

| Layout / Pattern | Recommended Wastage |
|---|---|
| Straight lay (grid) | 10% |
| Brick / running bond | 10–12% |
| Diagonal (45°) | 15–20% |
| Herringbone | 15–20% |
| Complex patterns | 20–25% |

### Popular Tile Sizes in NZ

- **600×300mm** — common floor tile, versatile
- **600×600mm** — large format, modern look
- **300×300mm** — bathroom floor, anti-slip
- **300×600mm** — wall tile, shower surrounds
- **75×300mm** — subway tile, splashbacks

### Tiling Cost Guide

Professional tiling in NZ typically costs $60–$120/m² for supply and install, depending on tile size and complexity. See our [full tiling cost guide](/jobs/tiling/) or find a [local tiler](/trades/builders/).
