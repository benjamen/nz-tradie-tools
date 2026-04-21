---
title: "Paint Calculator — NZ"
description: "Calculate how many litres of paint you need for walls, ceilings, and exteriors. Works for any NZ room or house."
tags: [paint, calculator, NZ, painting, decorator]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchPTab('room')">Room / Interior</button>
    <button class="calc-tab" onclick="switchPTab('exterior')">House Exterior</button>
  </div>
  <div id="ptab-room">
    <div class="calc-grid">
      <div class="calc-group"><label>Room length (m)</label><input type="number" id="r-len" placeholder="e.g. 5" oninput="calcRoom()"></div>
      <div class="calc-group"><label>Room width (m)</label><input type="number" id="r-wid" placeholder="e.g. 4" oninput="calcRoom()"></div>
      <div class="calc-group"><label>Ceiling height (m)</label><input type="number" id="r-h" placeholder="e.g. 2.4" oninput="calcRoom()"></div>
      <div class="calc-group"><label>Number of coats</label><input type="number" id="r-coats" placeholder="2" value="2" oninput="calcRoom()"></div>
      <div class="calc-group"><label>Doors (deduct 1.8m² each)</label><input type="number" id="r-doors" placeholder="1" value="1" oninput="calcRoom()"></div>
      <div class="calc-group"><label>Windows (deduct 1.4m² each)</label><input type="number" id="r-wins" placeholder="1" value="1" oninput="calcRoom()"></div>
      <div class="calc-group"><label>Wall coverage (m²/L)</label><input type="number" id="r-cov" placeholder="10" value="10" oninput="calcRoom()"></div>
    </div>
    <div class="calc-result" id="r-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Total wall area</span><span id="r-area"></span></div>
      <div class="result-row"><span>Net paintable area</span><span id="r-net"></span></div>
      <div class="result-row"><span>Litres needed (walls)</span><span id="r-litres"></span></div>
      <div class="result-row"><span>Ceiling area</span><span id="r-ceil-area"></span></div>
      <div class="result-row"><span>Litres needed (ceiling)</span><span id="r-ceil-litres"></span></div>
    </div>
  </div>
  <div id="ptab-exterior" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>House perimeter (m)</label><input type="number" id="e-per" placeholder="e.g. 40" oninput="calcExt()"></div>
      <div class="calc-group"><label>Wall height (m)</label><input type="number" id="e-h" placeholder="e.g. 6" oninput="calcExt()"></div>
      <div class="calc-group"><label>Number of coats</label><input type="number" id="e-coats" placeholder="2" value="2" oninput="calcExt()"></div>
      <div class="calc-group"><label>Coverage (m²/L)</label><input type="number" id="e-cov" placeholder="8" value="8" oninput="calcExt()"></div>
      <div class="calc-group"><label>Deduct for windows/doors (m²)</label><input type="number" id="e-ded" placeholder="20" value="20" oninput="calcExt()"></div>
    </div>
    <div class="calc-result" id="e-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Gross wall area</span><span id="e-gross"></span></div>
      <div class="result-row"><span>Net paintable area</span><span id="e-net"></span></div>
      <div class="result-row"><span>Litres needed</span><span id="e-litres"></span></div>
      <div class="result-row"><span>Estimated cost (mid-range paint)</span><span id="e-cost"></span></div>
    </div>
  </div>
  <script>
  function switchPTab(t){
    document.getElementById('ptab-room').style.display=t==='room'?'':'none';
    document.getElementById('ptab-exterior').style.display=t==='exterior'?'':'none';
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',i===(t==='room'?0:1));});
  }
  function fmt(n){return n.toFixed(1);}
  function calcRoom(){
    var l=parseFloat(document.getElementById('r-len').value)||0,
        w=parseFloat(document.getElementById('r-wid').value)||0,
        h=parseFloat(document.getElementById('r-h').value)||2.4,
        coats=parseFloat(document.getElementById('r-coats').value)||2,
        doors=parseFloat(document.getElementById('r-doors').value)||0,
        wins=parseFloat(document.getElementById('r-wins').value)||0,
        cov=parseFloat(document.getElementById('r-cov').value)||10;
    if(!l||!w){document.getElementById('r-result').style.display='none';return;}
    var wallArea=2*(l+w)*h, deduct=doors*1.8+wins*1.4, net=Math.max(0,wallArea-deduct);
    var litres=net*coats/cov, ceilArea=l*w, ceilLitres=ceilArea*coats/(cov*1.1);
    document.getElementById('r-area').textContent=fmt(wallArea)+' m²';
    document.getElementById('r-net').textContent=fmt(net)+' m²';
    document.getElementById('r-litres').textContent=Math.ceil(litres)+' L ('+coats+' coats)';
    document.getElementById('r-ceil-area').textContent=fmt(ceilArea)+' m²';
    document.getElementById('r-ceil-litres').textContent=Math.ceil(ceilLitres)+' L ('+coats+' coats)';
    document.getElementById('r-result').style.display='';
  }
  function calcExt(){
    var per=parseFloat(document.getElementById('e-per').value)||0,
        h=parseFloat(document.getElementById('e-h').value)||0,
        coats=parseFloat(document.getElementById('e-coats').value)||2,
        cov=parseFloat(document.getElementById('e-cov').value)||8,
        ded=parseFloat(document.getElementById('e-ded').value)||20;
    if(!per||!h){document.getElementById('e-result').style.display='none';return;}
    var gross=per*h, net=Math.max(0,gross-ded), litres=net*coats/cov;
    document.getElementById('e-gross').textContent=fmt(gross)+' m²';
    document.getElementById('e-net').textContent=fmt(net)+' m²';
    document.getElementById('e-litres').textContent=Math.ceil(litres)+' L';
    document.getElementById('e-cost').textContent='$'+(Math.ceil(litres)*12).toLocaleString()+'–$'+(Math.ceil(litres)*22).toLocaleString()+' approx.';
    document.getElementById('e-result').style.display='';
  }
  </script>
---

## Paint Calculator for NZ Painters & Homeowners

Calculate how many litres of paint you need for any room, ceiling, or exterior. Coverage rates vary by product — always check the tin, but 10 m²/L is a safe average for interior walls and 8 m²/L for exteriors.

### Coverage Guide by Paint Type

| Paint Type | Typical Coverage | Notes |
|---|---|---|
| Interior walls (water-based) | 10–14 m²/L | Per coat |
| Interior ceiling | 11–15 m²/L | Flat white, per coat |
| Exterior (texture) | 4–8 m²/L | Rough surfaces use more |
| Exterior (smooth) | 8–12 m²/L | Weatherboard, per coat |
| Primer/undercoat | 8–10 m²/L | Always prime bare timber |

### How Many Coats?

- **New surfaces:** 1 coat primer + 2 coats topcoat minimum
- **Repaints (same colour):** 2 coats
- **Colour change (dark to light):** 3 coats often needed
- **Bare timber exterior:** Primer + 2–3 topcoats

### Hiring a Painter?

See typical [painting costs in NZ](/jobs/painting/) or find a [local painter](/trades/painters/) to get a free quote.
