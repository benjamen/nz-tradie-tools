---
title: "Gib & Plasterboard Calculator NZ — Sheets, Stopping & Labour Cost"
seo_title: "Gib Calculator NZ 2026 — Sheets, Stopping Coats & Cost Estimate"
description: "Free NZ gib board calculator — enter your room dimensions to get sheet count, stopping coats, scrim, materials and installed cost estimate. Includes NZ pricing."
tags: [gib, plasterboard, stopping, calculator, NZ, building]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Total wall area to gib (m²)</label><input type="number" id="gb-area" placeholder="e.g. 120" oninput="calcGib()"></div>
    <div class="calc-group"><label>Ceiling area (m²)</label><input type="number" id="gb-ceil" placeholder="e.g. 80" value="0" oninput="calcGib()"></div>
    <div class="calc-group"><label>Gib sheet size</label>
      <select id="gb-sheet" onchange="calcGib()">
        <option value="3.0">2400 × 1200 mm (2.88 m²)</option>
        <option value="3.6" selected>2400 × 1200 mm standard (2.88 m²) + 25% waste</option>
        <option value="4.32">Ceiling/large sheets (inc. waste)</option>
      </select>
    </div>
    <div class="calc-group"><label>Stopping level</label>
      <select id="gb-stop" onchange="calcGib()">
        <option value="1">Level 3 — basic (1 coat, no skim)</option>
        <option value="2" selected>Level 4 — standard (2 coats + sand)</option>
        <option value="3">Level 5 — premium smooth (3 coats + fine skim)</option>
      </select>
    </div>
    <div class="calc-group"><label>Gib type</label>
      <select id="gb-type" onchange="calcGib()">
        <option value="25" selected>Standard 10mm</option>
        <option value="30">Noiseline / Aqualine 13mm</option>
        <option value="45">Fire-rated / Braceline</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="gb-result" style="display:none">
    <h3>Gib & Plasterboard Estimate</h3>
    <div class="result-row"><span>Total area to gib</span><span id="gb-tot-area"></span></div>
    <div class="result-row"><span>Sheets required (inc. waste)</span><span id="gb-sheets"></span></div>
    <div class="result-row"><span>Scrim tape (lm)</span><span id="gb-scrim"></span></div>
    <div class="result-row"><span>Stopping compound (bags)</span><span id="gb-compound"></span></div>
    <div class="result-row"><span>Gib fixings (screws, box)</span><span id="gb-fixings"></span></div>
    <div class="result-row"><span>Materials only</span><span id="gb-mat-cost"></span></div>
    <div class="result-row"><span>Installed cost estimate</span><span id="gb-total" class="result-highlight"></span></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcGib(){
    var walls=parseFloat(document.getElementById('gb-area').value)||0;
    var ceil=parseFloat(document.getElementById('gb-ceil').value)||0;
    var sheetFactor=parseFloat(document.getElementById('gb-sheet').value);
    var stopLevel=parseInt(document.getElementById('gb-stop').value);
    var matPpm=parseFloat(document.getElementById('gb-type').value);
    if(!walls&&!ceil){document.getElementById('gb-result').style.display='none';return;}
    var total=walls+ceil;
    var sheets=Math.ceil(total/sheetFactor);
    var scrim=Math.ceil(total*2.5);
    var compound=Math.ceil(total/10*stopLevel);
    var fixings=Math.ceil(sheets/5)+1;
    var matCost=sheets*matPpm+(scrim*0.9)+(compound*18)+(fixings*22);
    var stopRatePerM2=[0,18,28,42][stopLevel];
    var labour=total*(55+stopRatePerM2);
    var total_cost=matCost+labour;
    document.getElementById('gb-tot-area').textContent=total.toFixed(1)+' m²';
    document.getElementById('gb-sheets').textContent=sheets+' sheets';
    document.getElementById('gb-scrim').textContent=scrim+' lm';
    document.getElementById('gb-compound').textContent=compound+' bags (5kg)';
    document.getElementById('gb-fixings').textContent=fixings+' boxes';
    document.getElementById('gb-mat-cost').textContent=nzd(matCost);
    document.getElementById('gb-total').textContent=nzd(total_cost)+' – '+nzd(total_cost*1.25);
    document.getElementById('gb-result').style.display='';
  }
  </script>
faqs:
  - q: 'How many sheets of gib do I need for a room?'
    a: 'Measure your total wall area (perimeter × height) and ceiling area. Divide by 2.88 m² (standard 2400×1200 sheet) and add 15–20% for waste and cuts. A typical 3.5m × 4m room with 2.4m stud is about 12–14 sheets for walls, plus 5 ceiling sheets.'
  - q: 'What is Level 4 stopping in NZ?'
    a: 'Level 4 (NZS 4334) is the standard for most NZ residential interiors — two coats of stopping compound sanded smooth, ready for paint with flat or low-sheen finish. Level 5 adds a skim coat for high-gloss or critical lighting situations. Level 3 is basic, used in garages or utility spaces.'
  - q: 'How much does gib stopping cost per m² in NZ?'
    a: 'Gib board supply and fix costs $45–$65/m² installed. Stopping adds $18–$42/m² depending on level. A full Level 4 gib, stop and sand job (supply + install) typically runs $65–$110/m² in NZ. Auckland costs 10–15% more.'
  - q: 'What is the difference between standard gib and Noiseline?'
    a: 'Standard 10mm Gib is the most common residential plasterboard. Noiseline (13mm) has improved acoustic ratings for party walls and bedroom partitions. Aqualine is moisture-resistant for bathrooms. Braceline provides additional racking resistance for earthquake zones. All are made by Winstone Wallboards in NZ.'
  - q: 'Does gibbing require a building consent?'
    a: 'Internal gib replacement (like-for-like) is generally exempt from consent. New partition walls and changes to fire-rated or bracing walls may require consent. Always confirm with your local council if unsure.'
related_articles: [job-costing-guide-nz-tradies-2026]
---

## Gib & Plasterboard in NZ — What You Need to Know

**Gib** is New Zealand's dominant plasterboard brand (manufactured by Winstone Wallboards, a Fletcher Building subsidiary). In NZ trade, "gib" and "plasterboard" are used interchangeably — if a quote says "gib and stop", it means supply and install plasterboard and apply stopping compound.

### NZ Gib Sheet Types

| Type | Thickness | Use | Approx cost/sheet |
|---|---|---|---|
| Standard | 10 mm | General walls & ceilings | $18–$25 |
| Noiseline | 13 mm | Party walls, bedrooms | $28–$38 |
| Aqualine | 10 mm | Bathrooms, wet areas | $22–$30 |
| Braceline | 10 mm | Seismic bracing walls | $28–$36 |
| Fyreline | 13 mm | Fire-rated walls | $32–$42 |

### Stopping Levels Explained

| Level | Description | When used |
|---|---|---|
| Level 3 | One coat, unfilled — not ready to paint | Garages, utility areas |
| Level 4 | Two coats + sand — standard finish | All NZ residential interiors |
| Level 5 | Three coats + skim — critical finish | High-gloss paint, feature walls |

### Typical Gib & Stopping Costs NZ 2026

| Scope | Cost range (ex GST) |
|---|---|
| Gib supply and fix only | $45–$65/m² |
| Stopping Level 4 only | $25–$35/m² |
| Full gib + Level 4 stop + sand | $70–$100/m² |
| Full gib + Level 5 premium | $90–$130/m² |

All prices ex GST. Auckland 10–15% above average. Christchurch and Wellington within 5% of average. Smaller cities typically 5–10% below.
