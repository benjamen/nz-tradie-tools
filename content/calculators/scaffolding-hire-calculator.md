---
title: "NZ Scaffolding Hire vs Buy Calculator"
description: "Compare the cost of hiring vs buying scaffolding for NZ tradies — roofing, painting, cladding and maintenance jobs."
tags: [scaffolding, hire, WorkSafe, roofing, painting, NZ]
author: "NZ Tradie Tools"
related_articles: [health-and-safety-guide-nz-tradies, roofer-pricing-guide-nz-2026, painter-pricing-guide-nz-2026]
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchSC('hire')">Hire Cost Calculator</button>
    <button class="calc-tab" onclick="switchSC('compare')">Hire vs Buy Comparison</button>
  </div>
  <div id="sc-hire">
    <div class="calc-grid">
      <div class="calc-group">
        <label>Building perimeter to scaffold (m)</label>
        <input type="number" id="sc-perim" placeholder="e.g. 40" oninput="calcSCHire()">
      </div>
      <div class="calc-group">
        <label>Building height (m)</label>
        <input type="number" id="sc-height" placeholder="e.g. 5.5" step="0.5" oninput="calcSCHire()">
      </div>
      <div class="calc-group">
        <label>Hire duration (weeks)</label>
        <input type="number" id="sc-weeks" placeholder="e.g. 3" oninput="calcSCHire()">
      </div>
      <div class="calc-group">
        <label>Region</label>
        <select id="sc-region" onchange="calcSCHire()">
          <option value="1.2">Auckland</option>
          <option value="1.1">Wellington</option>
          <option value="1.0">Christchurch / Hamilton</option>
          <option value="0.9">Regional NZ</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="sc-hire-result" style="display:none">
      <h3>Scaffolding Hire Estimate</h3>
      <div class="result-row"><span>Scaffold area</span><span id="sc-r-area"></span></div>
      <div class="result-row"><span>Erect &amp; dismantle cost (est.)</span><span id="sc-r-ed"></span></div>
      <div class="result-row"><span>Weekly hire rate (est.)</span><span id="sc-r-weekly"></span></div>
      <div class="result-row"><span>Hire charge (<span id="sc-r-wks"></span> weeks)</span><span id="sc-r-hire-total"></span></div>
      <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total estimated hire cost</span><span id="sc-r-total"></span></div>
      <p style="font-size:.8rem;color:#666;margin-top:.75rem">WorkSafe NZ requires scaffolding for work above 5m. Costs include basic guardrails — edge protection and full enclosure cost more. Get 3 quotes for large jobs.</p>
    </div>
  </div>
  <div id="sc-compare" style="display:none">
    <div class="calc-grid">
      <div class="calc-group">
        <label>Average hire cost per job — $</label>
        <input type="number" id="sc-avg-hire" placeholder="e.g. 2500" oninput="calcSCCompare()">
      </div>
      <div class="calc-group">
        <label>Jobs per year requiring scaffolding</label>
        <input type="number" id="sc-jobs" placeholder="e.g. 15" oninput="calcSCCompare()">
      </div>
      <div class="calc-group">
        <label>Purchase price of scaffolding set — $</label>
        <input type="number" id="sc-buy-price" placeholder="e.g. 18000" oninput="calcSCCompare()">
      </div>
      <div class="calc-group">
        <label>Years to compare</label>
        <input type="number" id="sc-years" value="5" min="1" max="15" oninput="calcSCCompare()">
      </div>
    </div>
    <div class="calc-result" id="sc-compare-result" style="display:none">
      <h3>Hire vs Buy — <span id="sc-r-cmp-years"></span>-Year Comparison</h3>
      <div class="result-row"><span>Total hire cost over period</span><span id="sc-r-cmp-hire" style="color:#c53030"></span></div>
      <div class="result-row"><span>Purchase price</span><span id="sc-r-cmp-buy"></span></div>
      <div class="result-row"><span>Estimated maintenance / storage</span><span id="sc-r-cmp-maint"></span></div>
      <div class="result-row"><span>Total ownership cost</span><span id="sc-r-cmp-own-total" style="color:#c53030"></span></div>
      <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Break-even point</span><span id="sc-r-cmp-breakeven"></span></div>
      <div id="sc-r-verdict" style="margin-top:.75rem;border-radius:6px;padding:.75rem;font-size:.85rem"></div>
    </div>
  </div>
  <script>
  function fmt(n){return "$"+Math.round(n).toLocaleString("en-NZ");}
  function switchSC(m){
    document.querySelectorAll(".calc-tab").forEach(function(b,i){b.classList.toggle("active",i===(m==="hire"?0:1));});
    document.getElementById("sc-hire").style.display=m==="hire"?"":"none";
    document.getElementById("sc-compare").style.display=m==="compare"?"":"none";
  }
  function calcSCHire(){
    var perim=parseFloat(document.getElementById("sc-perim").value)||0;
    var height=parseFloat(document.getElementById("sc-height").value)||0;
    var weeks=parseFloat(document.getElementById("sc-weeks").value)||0;
    var reg=parseFloat(document.getElementById("sc-region").value)||1.0;
    var r=document.getElementById("sc-hire-result");
    if(!perim||!height||!weeks){r.style.display="none";return;}
    var area=perim*height;
    var ed=(800+area*8)*reg;
    var weeklyRate=(300+area*4)*reg;
    var hireTotal=weeklyRate*weeks;
    var total=ed+hireTotal;
    document.getElementById("sc-r-area").textContent=area.toFixed(0)+"m²";
    document.getElementById("sc-r-ed").textContent=fmt(ed);
    document.getElementById("sc-r-weekly").textContent=fmt(weeklyRate)+"/wk";
    document.getElementById("sc-r-wks").textContent=weeks;
    document.getElementById("sc-r-hire-total").textContent=fmt(hireTotal);
    document.getElementById("sc-r-total").textContent=fmt(total);
    r.style.display="";
  }
  function calcSCCompare(){
    var avgHire=parseFloat(document.getElementById("sc-avg-hire").value)||0;
    var jobs=parseFloat(document.getElementById("sc-jobs").value)||0;
    var buyPrice=parseFloat(document.getElementById("sc-buy-price").value)||0;
    var years=parseFloat(document.getElementById("sc-years").value)||5;
    var r=document.getElementById("sc-compare-result");
    if(!avgHire||!jobs||!buyPrice){r.style.display="none";return;}
    var annualHire=avgHire*jobs;
    var totalHire=annualHire*years;
    var maint=buyPrice*0.05*years;
    var ownTotal=buyPrice+maint;
    var breakeven=buyPrice/(annualHire-buyPrice*0.05);
    document.getElementById("sc-r-cmp-years").textContent=years;
    document.getElementById("sc-r-cmp-hire").textContent=fmt(totalHire);
    document.getElementById("sc-r-cmp-buy").textContent=fmt(buyPrice);
    document.getElementById("sc-r-cmp-maint").textContent=fmt(maint);
    document.getElementById("sc-r-cmp-own-total").textContent=fmt(ownTotal);
    document.getElementById("sc-r-cmp-breakeven").textContent=breakeven>0?breakeven.toFixed(1)+" years":"Never (hire is cheaper)";
    var v=document.getElementById("sc-r-verdict");
    if(totalHire>ownTotal){
      v.style.background="#f0fff4";v.style.border="1px solid #68d391";
      v.innerHTML="<strong style="color:#22543d">Buying is cheaper</strong> over "+years+" years — you save "+fmt(totalHire-ownTotal)+" compared to hiring. Buying makes sense if you have consistent volume.";
    }else{
      v.style.background="#f0f4ff";v.style.border="1px solid #90cdf4";
      v.innerHTML="<strong>Hiring is cheaper</strong> over "+years+" years — you save "+fmt(ownTotal-totalHire)+" by hiring rather than buying. Unless volume increases, continue hiring.";
    }
    r.style.display="";
  }
  </script>
---

## Scaffolding for NZ Tradies — When You Need It and What It Costs

Scaffolding is a significant cost on roofing, painting, and cladding jobs — and one that's frequently underquoted.

### WorkSafe NZ Requirements

Under the **Health and Safety at Work Act 2015** and **WorkSafe NZ guidelines**, scaffolding is required for work at height over **5 metres** where a person could fall. This covers:

- Full re-roofing work on two-storey homes
- Exterior painting above the first storey
- Cladding installation and repair on multi-storey buildings
- Fascia and gutter work on tall buildings

Working above 5m without compliant edge protection is a notifiable event if someone falls — and prosecution under the HSWA can result in significant fines.

### Typical Scaffolding Hire Costs in NZ (2026)

| Building size | Erect/dismantle | Per week hire | 2-week total |
|---|---|---|---|
| Small single storey (perimeter ~30m) | $600–$900 | $350–$500 | $1,300–$1,900 |
| Standard 2-storey (perimeter ~50m) | $1,200–$1,800 | $600–$900 | $2,400–$3,600 |
| Large 2-storey (perimeter ~70m) | $1,800–$2,800 | $900–$1,400 | $3,600–$5,600 |

### Buying vs Hiring

Buying scaffolding makes sense if you do more than 8–12 scaffold jobs per year consistently. Below that threshold, hire costs are typically lower once you factor in storage space, maintenance, and the capital tied up in equipment.

A used scaffold set suitable for residential work can be purchased for $10,000–$25,000 from trade suppliers or auction sites. Factor in annual inspection costs (required under the Health and Safety at Work (General Risk and Workplace Management) Regulations 2016) and storage.
