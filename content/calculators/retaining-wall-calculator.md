---
title: "Retaining Wall Calculator — NZ"
description: "Estimate retaining wall materials and costs for NZ — concrete blocks, timber, or keystone. Includes drainage aggregate."
tags: [retaining wall, landscaping, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Wall length (m)</label><input type="number" id="rw-len" placeholder="e.g. 12" oninput="calcRetain()"></div>
    <div class="calc-group"><label>Wall height (m)</label><input type="number" id="rw-h" placeholder="e.g. 1.2" oninput="calcRetain()"></div>
    <div class="calc-group"><label>Wall type</label>
      <select id="rw-type" onchange="calcRetain()">
        <option value="block" selected>Concrete block / keystone</option>
        <option value="timber">H5 treated timber sleepers</option>
        <option value="concrete">Poured concrete</option>
        <option value="gabion">Gabion baskets</option>
      </select>
    </div>
    <div class="calc-group"><label>Include drainage aggregate?</label>
      <select id="rw-drain" onchange="calcRetain()">
        <option value="1" selected>Yes</option>
        <option value="0">No</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="rw-result" style="display:none">
    <h3>Retaining Wall Estimate</h3>
    <div class="result-row"><span>Wall area</span><span id="rw-area"></span></div>
    <div class="result-row"><span id="rw-mat-label">Main material</span><span id="rw-mat"></span></div>
    <div class="result-row"><span>Drainage aggregate (m³)</span><span id="rw-agg"></span></div>
    <div class="result-row"><span>Geotextile fabric (m²)</span><span id="rw-geo"></span></div>
    <div class="result-row"><span>Material cost estimate</span><span id="rw-mcost"></span></div>
    <div class="result-row"><span>Installed cost estimate</span><span id="rw-total" class="result-highlight"></span></div>
    <div id="rw-consent-note" style="display:none;background:#fff3cd;border:1px solid #ffc107;padding:.6rem .9rem;margin-top:.6rem;font-size:.85rem"></div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcRetain(){
    var len=parseFloat(document.getElementById('rw-len').value)||0;
    var h=parseFloat(document.getElementById('rw-h').value)||0;
    var type=document.getElementById('rw-type').value;
    var drain=parseInt(document.getElementById('rw-drain').value);
    if(!len||!h){document.getElementById('rw-result').style.display='none';return;}
    var area=len*h;
    var agg=drain?(len*(h*0.4)).toFixed(1):0;
    var geo=drain?len*(h+0.5):0;
    var matLabel, matQty, matCost, labourPerM2;
    if(type==='block'){matLabel='Keystone/concrete blocks';matQty=Math.ceil(area*10)+' blocks';matCost=area*65;labourPerM2=180;}
    else if(type==='timber'){matLabel='H5 timber sleepers (200×75mm)';matQty=Math.ceil(area/0.075*1.05)+' lm';matCost=area*90;labourPerM2=140;}
    else if(type==='concrete'){matLabel='Concrete (m³)';matQty=(area*0.25).toFixed(2)+' m³';matCost=area*110;labourPerM2=250;}
    else{matLabel='Gabion baskets';matQty=Math.ceil(len*h/0.5)+' baskets';matCost=area*120;labourPerM2=130;}
    var aggCost=drain?(parseFloat(agg)*55+geo*3.5):0;
    var labour=area*labourPerM2+800;
    var total=matCost+aggCost+labour;
    document.getElementById('rw-area').textContent=area.toFixed(2)+' m²';
    document.getElementById('rw-mat-label').textContent=matLabel;
    document.getElementById('rw-mat').textContent=matQty;
    document.getElementById('rw-agg').textContent=drain?agg+' m³':'Not included';
    document.getElementById('rw-geo').textContent=drain?geo.toFixed(0)+' m²':'Not included';
    document.getElementById('rw-mcost').textContent=nzd(matCost+aggCost);
    document.getElementById('rw-total').textContent=nzd(total)+' – '+nzd(total*1.25);
    var consentEl=document.getElementById('rw-consent-note');
    if(h>1.5){consentEl.innerHTML='<strong>⚠ Building consent required.</strong> Retaining walls over 1.5m in NZ generally require building consent. Engage a structural engineer and your local council before starting.';consentEl.style.display='';}
    else{consentEl.style.display='none';}
    document.getElementById('rw-result').style.display='';
  }
  </script>
---

## Retaining Wall Costs in NZ

Retaining wall pricing depends heavily on height, length, material, and access. Steep sites with poor access can double the labour cost.

### Consent Requirements

Under the **NZ Building Act**, retaining walls generally require building consent if:
- Height exceeds **1.5 metres** above the lowest ground level
- The wall is within 1.5m of a boundary or building

Always check with your local council — some have stricter rules.

### Cost Guide by Type

| Type | Installed cost (per m²) |
|---|---|
| Keystone / concrete block | $350–$550/m² |
| H5 timber sleepers | $280–$420/m² |
| Poured concrete | $500–$800/m² |
| Gabion baskets | $300–$500/m² |

### Drainage is Critical

All retaining walls need drainage to prevent hydrostatic pressure buildup — the #1 cause of retaining wall failure. Always include:
- 300–400mm drainage aggregate backfill
- Geotextile filter fabric
- Ag-pipe at the base with outlets every 3–4m

Use our [Earthworks Calculator](/calculators/earthworks-calculator.html) to estimate excavation volumes.
