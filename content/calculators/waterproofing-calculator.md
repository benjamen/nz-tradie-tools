---
title: "Waterproofing Calculator — NZ (Bathrooms & Decks)"
description: "Calculate waterproofing membrane, primer, and tape quantities for NZ bathrooms, showers, and decks."
tags: [waterproofing, bathroom, deck, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchWPTab('bath')">Bathroom / Shower</button>
    <button class="calc-tab" onclick="switchWPTab('deck')">Deck / Balcony</button>
  </div>
  <div id="wptab-bath">
    <div class="calc-grid">
      <div class="calc-group"><label>Floor area (m²)</label><input type="number" id="wp-fa" placeholder="e.g. 4" oninput="calcWP()"></div>
      <div class="calc-group"><label>Shower floor area (m²)</label><input type="number" id="wp-sa" placeholder="e.g. 1.0" oninput="calcWP()"></div>
      <div class="calc-group"><label>Wet wall height (m)</label><input type="number" id="wp-wh" placeholder="e.g. 1.8" value="1.8" oninput="calcWP()"></div>
      <div class="calc-group"><label>Wet wall perimeter (m)</label><input type="number" id="wp-wp" placeholder="e.g. 6" oninput="calcWP()"></div>
      <div class="calc-group"><label>Product type</label>
        <select id="wp-prod" onchange="calcWP()">
          <option value="1" selected>Liquid membrane (2 coat)</option>
          <option value="0.8">Sheet membrane (Protecto-wrap etc)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="wp-result" style="display:none">
      <h3>Waterproofing Quantities</h3>
      <div class="result-row"><span>Total area to waterproof</span><span id="wp-area"></span></div>
      <div class="result-row"><span>Membrane required (2 coats)</span><span id="wp-mem" class="result-highlight"></span></div>
      <div class="result-row"><span>Primer</span><span id="wp-primer"></span></div>
      <div class="result-row"><span>Jointing tape (lm)</label></span><span id="wp-tape"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="wp-cost"></span></div>
      <div class="result-row"><span>Estimated installed cost</span><span id="wp-install"></span></div>
    </div>
  </div>
  <div id="wptab-deck" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Deck area (m²)</label><input type="number" id="dk-area" placeholder="e.g. 20" oninput="calcDeck()"></div>
      <div class="calc-group"><label>Perimeter (m)</label><input type="number" id="dk-per" placeholder="e.g. 18" oninput="calcDeck()"></div>
      <div class="calc-group"><label>Deck type</label>
        <select id="dk-type" onchange="calcDeck()">
          <option value="1" selected>Trafficable membrane (GRP/fibreglass)</option>
          <option value="0.8">TPO / torch-on membrane</option>
          <option value="0.6">Rubber deck coating</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="dk-result" style="display:none">
      <h3>Deck Waterproofing</h3>
      <div class="result-row"><span>Membrane area</span><span id="dk-area-out"></span></div>
      <div class="result-row"><span>Estimated material cost</span><span id="dk-mat"></span></div>
      <div class="result-row"><span>Estimated installed cost</span><span id="dk-install" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchWPTab(t){
    document.getElementById('wptab-bath').style.display=t==='bath'?'':'none';
    document.getElementById('wptab-deck').style.display=t==='deck'?'':'none';
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['bath','deck'][i]===t);});
  }
  function calcWP(){
    var fa=parseFloat(document.getElementById('wp-fa').value)||0;
    var sa=parseFloat(document.getElementById('wp-sa').value)||0;
    var wh=parseFloat(document.getElementById('wp-wh').value)||1.8;
    var wp=parseFloat(document.getElementById('wp-wp').value)||0;
    var prod=parseFloat(document.getElementById('wp-prod').value);
    if(!fa){document.getElementById('wp-result').style.display='none';return;}
    var wallArea=wp*wh;
    var total=(fa+sa+wallArea)*prod;
    var memL=Math.ceil(total/8)+1;
    var primer=Math.ceil(total/12)+1;
    var tape=Math.ceil((wp+sa*4)*1.1);
    var matCost=memL*85+primer*45+tape*4.5;
    var install=total*45+350;
    document.getElementById('wp-area').textContent=total.toFixed(1)+' m²';
    document.getElementById('wp-mem').textContent=memL+'L membrane (@ 0.5L/m²/coat × 2 coats)';
    document.getElementById('wp-primer').textContent=primer+'L';
    document.getElementById('wp-tape').textContent=tape+' lm';
    document.getElementById('wp-cost').textContent=nzd(matCost);
    document.getElementById('wp-install').textContent=nzd(matCost+install);
    document.getElementById('wp-result').style.display='';
  }
  function calcDeck(){
    var area=parseFloat(document.getElementById('dk-area').value)||0;
    var per=parseFloat(document.getElementById('dk-per').value)||0;
    var type=parseFloat(document.getElementById('dk-type').value);
    if(!area){document.getElementById('dk-result').style.display='none';return;}
    var mat=(area+per*0.3)*75*type;
    var install=area*90*type+800;
    document.getElementById('dk-area-out').textContent=(area+per*0.3).toFixed(1)+' m² (incl. upstands)';
    document.getElementById('dk-mat').textContent=nzd(mat);
    document.getElementById('dk-install').textContent=nzd(mat+install)+' – '+nzd((mat+install)*1.2);
    document.getElementById('dk-result').style.display='';
  }
  </script>
---

## NZ Waterproofing Requirements

Waterproofing is mandated under **NZ Building Code Clause E3** (Internal Moisture). Failing to waterproof correctly is one of the most common causes of leaky building claims in NZ.

### What Must Be Waterproofed

- **Shower floors and walls** (min 1.8m up walls in shower area)
- **Bathroom floors** (all floor area)
- **Balconies and decks** (trafficable or non-trafficable membranes)
- **Wet areas in commercial buildings**

### Approved Membrane Systems (NZ)

- **Liquid applied membranes** (Ardex, Mapei, Laticrete) — most common in bathrooms
- **Sheet membranes** (Wedi, Schluter Kerdi) — faster install in showers
- **GRP/fibreglass** — standard for trafficable decks
- **TPO/single-ply** — commercial flat roofs and large decks

### Why DIY Waterproofing Fails

NZ has strict requirements for membrane coverage, lap joints, and curing times. Defective waterproofing voids your building consent and can result in costly remediation. Always use a [licensed waterproofer](/trades/waterproofers/) or qualified tiler for wet area waterproofing.
