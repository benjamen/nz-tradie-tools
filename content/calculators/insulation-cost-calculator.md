---
title: "Insulation Cost Calculator — NZ"
seo_title: "Free NZ Insulation Cost Calculator 2026 — Ceiling, Floor & Wall"
description: "Free NZ insulation cost calculator — estimate ceiling, underfloor and wall insulation costs for your home. 2026 NZ rates including labour and materials."
tags: [insulation, ceiling insulation, underfloor insulation, wall insulation, calculator, NZ]
author: "NZ Tradie Tools"
related_articles: [insulation-nz-cost-guide]
layout: calculator
date: 2026-06-30
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>House floor area (m²)</label><input type="number" id="ins-area" placeholder="e.g. 120" oninput="calcInsulation()"></div>
    <div class="calc-group"><label>Insulation type</label>
      <select id="ins-type" onchange="calcInsulation()">
        <option value="ceiling" selected>Ceiling only</option>
        <option value="floor">Underfloor only</option>
        <option value="ceiling_floor">Ceiling + underfloor</option>
        <option value="full">Ceiling + floor + walls (full retrofit)</option>
      </select>
    </div>
    <div class="calc-group"><label>Insulation grade</label>
      <select id="ins-grade" onchange="calcInsulation()">
        <option value="standard" selected>Standard (meets current code)</option>
        <option value="premium">Premium (higher R-value)</option>
      </select>
    </div>
    <div class="calc-group"><label>Existing insulation?</label>
      <select id="ins-existing" onchange="calcInsulation()">
        <option value="none" selected>None — new install</option>
        <option value="remove">Yes — needs removal first</option>
        <option value="topup">Yes — top-up only</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="ins-result" style="display:none">
    <h3>Insulation Cost Estimate</h3>
    <div class="result-row"><span>Floor area</span><span id="ins-display-area"></span></div>
    <div class="result-row"><span>Ceiling insulation</span><span id="ins-ceiling-row"></span></div>
    <div class="result-row"><span>Underfloor insulation</span><span id="ins-floor-row"></span></div>
    <div class="result-row"><span>Wall insulation</span><span id="ins-wall-row"></span></div>
    <div class="result-row"><span>Removal / disposal</span><span id="ins-removal-row"></span></div>
    <div class="result-row"><span>Total estimate</span><span id="ins-total" class="result-highlight"></span></div>
    <p id="ins-note" style="font-size:.85rem;color:#555;margin-top:.75rem;line-height:1.5"></p>
  </div>
  <script>
  function nzd(n){return n>0?'$'+Math.round(n).toLocaleString():'—';}
  function calcInsulation(){
    var area=parseFloat(document.getElementById('ins-area').value)||0;
    var type=document.getElementById('ins-type').value;
    var grade=document.getElementById('ins-grade').value;
    var existing=document.getElementById('ins-existing').value;
    if(!area){document.getElementById('ins-result').style.display='none';return;}

    var mult=grade==='premium'?1.35:1.0;
    // Rates per m² installed (NZ 2026, incl labour)
    var ceilRate=mult*(existing==='topup'?12:22);
    var floorRate=mult*28;
    var wallRate=mult*55; // wall retrofit is most expensive

    var ceilCost=0,floorCost=0,wallCost=0,removalCost=0;
    if(type==='ceiling'||type==='ceiling_floor'||type==='full'){
      ceilCost=area*ceilRate+(existing==='topup'?0:400);
    }
    if(type==='floor'||type==='ceiling_floor'||type==='full'){
      floorCost=area*floorRate+300;
    }
    if(type==='full'){
      wallCost=area*1.2*wallRate+500; // wall area ~1.2x floor area for typical home
    }
    if(existing==='remove'){
      removalCost=area*(type==='ceiling'?8:type==='floor'?10:15)+300;
    }

    var total=ceilCost+floorCost+wallCost+removalCost;

    document.getElementById('ins-display-area').textContent=area+' m²';
    document.getElementById('ins-ceiling-row').textContent=ceilCost>0?nzd(ceilCost):'Not included';
    document.getElementById('ins-floor-row').textContent=floorCost>0?nzd(floorCost):'Not included';
    document.getElementById('ins-wall-row').textContent=wallCost>0?nzd(wallCost):'Not included';
    document.getElementById('ins-removal-row').textContent=removalCost>0?nzd(removalCost):'Not required';
    document.getElementById('ins-total').textContent=nzd(total);
    document.getElementById('ins-note').textContent=
      type==='full'
        ? 'Full-house insulation retrofits may qualify for Warmer Kiwi Homes subsidies — check energyefficiency.govt.nz for eligibility before getting quotes.'
        : 'Warmer Kiwi Homes grants cover up to 80% of ceiling and underfloor insulation costs for eligible homeowners. Check energyefficiency.govt.nz.';
    document.getElementById('ins-result').style.display='block';
  }
  </script>

intro: |
  Get an instant estimate for insulating your NZ home. Prices include materials and installation. A Warmer Kiwi Homes subsidy may cover up to 80% of costs — the calculator shows the full price, but you could pay significantly less.

faq:
  - q: "How much does ceiling insulation cost in NZ?"
    a: "Ceiling insulation in NZ typically costs $1,500–$3,500 installed for a standard 100–140m² home, depending on R-value and any removal needed. The Warmer Kiwi Homes grant can cover up to 80% for eligible homes."
  - q: "What is the Warmer Kiwi Homes grant?"
    a: "A government subsidy that covers up to 80% of ceiling and underfloor insulation costs, and up to 80% of a heat pump, for eligible homeowners. Eligibility is based on Community Services Card or low-income criteria. Apply at energyefficiency.govt.nz."
  - q: "How much does underfloor insulation cost in NZ?"
    a: "Underfloor insulation costs $2,000–$4,500 installed for a typical NZ home, depending on access, area and foil vs batt product. Subfloor access is a big cost factor."
  - q: "What R-value insulation do I need in NZ?"
    a: "NZ Building Code H1 requires R2.9 in ceilings for most NZ climate zones. For better performance, R3.6–R6.6 is recommended. Older homes often have R1.6 or less and benefit significantly from upgrading."
  - q: "Is wall insulation worth it in NZ?"
    a: "Wall insulation is effective but expensive to retrofit ($5,000–$15,000+) as it usually requires removing interior linings. Most effective in new builds or full renovations. Focus on ceiling and floor first for the best return."
---
