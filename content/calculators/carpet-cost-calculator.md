---
title: "Carpet Cost Calculator — NZ"
seo_title: "Free NZ Carpet Cost Calculator 2026 — Supply & Lay Price"
description: "Free NZ carpet cost calculator — estimate supply and installation costs by room size, carpet grade and underlay. 2026 NZ rates including GST."
tags: [carpet, carpet layers, flooring, calculator, NZ, supply and lay]
author: "NZ Tradie Tools"
layout: calculator
date: 2026-06-30
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Room length (m)</label><input type="number" id="cp-len" placeholder="e.g. 5" oninput="calcCarpet()"></div>
    <div class="calc-group"><label>Room width (m)</label><input type="number" id="cp-wid" placeholder="e.g. 4" oninput="calcCarpet()"></div>
    <div class="calc-group"><label>Carpet grade</label>
      <select id="cp-grade" onchange="calcCarpet()">
        <option value="budget">Budget ($25–35/m²)</option>
        <option value="mid" selected>Mid-range ($45–65/m²)</option>
        <option value="premium">Premium ($75–110/m²)</option>
      </select>
    </div>
    <div class="calc-group"><label>Include underlay?</label>
      <select id="cp-underlay" onchange="calcCarpet()">
        <option value="yes" selected>Yes — standard underlay</option>
        <option value="premium">Yes — premium underlay</option>
        <option value="no">No (replacing underlay only)</option>
      </select>
    </div>
    <div class="calc-group"><label>Remove existing carpet?</label>
      <select id="cp-remove" onchange="calcCarpet()">
        <option value="no" selected>No</option>
        <option value="yes">Yes — remove & dispose</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="cp-result" style="display:none">
    <h3>Carpet Cost Estimate</h3>
    <div class="result-row"><span>Room area</span><span id="cp-area"></span></div>
    <div class="result-row"><span>Carpet (supply)</span><span id="cp-carpet-cost"></span></div>
    <div class="result-row"><span>Underlay (supply)</span><span id="cp-underlay-cost"></span></div>
    <div class="result-row"><span>Installation (lay & trim)</span><span id="cp-install-cost"></span></div>
    <div class="result-row"><span>Removal & disposal</span><span id="cp-remove-cost"></span></div>
    <div class="result-row"><span>Total estimate (inc GST)</span><span id="cp-total" class="result-highlight"></span></div>
    <div class="result-row"><span>Per m²</span><span id="cp-m2"></span></div>
    <p id="cp-note" style="font-size:.85rem;color:#555;margin-top:.75rem;line-height:1.5"></p>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcCarpet(){
    var len=parseFloat(document.getElementById('cp-len').value)||0;
    var wid=parseFloat(document.getElementById('cp-wid').value)||0;
    var grade=document.getElementById('cp-grade').value;
    var underlay=document.getElementById('cp-underlay').value;
    var remove=document.getElementById('cp-remove').value;
    if(!len||!wid){document.getElementById('cp-result').style.display='none';return;}

    // Add 10% waste for cutting
    var area=len*wid;
    var billable=area*1.10;

    // Carpet rates per m² (supply only, mid of range)
    var carpetRate={budget:30,mid:55,premium:90}[grade];
    var carpetCost=billable*carpetRate;

    // Underlay
    var underlayCost=0;
    if(underlay==='yes') underlayCost=billable*18;
    else if(underlay==='premium') underlayCost=billable*28;

    // Installation (lay, trim, join if needed)
    var installCost=area*18+120; // base rate + mobilisation

    // Removal
    var removeCost=remove==='yes'?(area*8+80):0;

    var total=carpetCost+underlayCost+installCost+removeCost;
    var perM2=total/area;

    var notes={
      budget:'Budget carpet suits rentals and high-traffic areas where durability matters more than feel. Typical lifespan 5–10 years.',
      mid:'Mid-range carpet is the most popular choice in NZ homes — good balance of comfort, durability and price. Expect 10–15 years.',
      premium:'Premium carpet offers superior softness and longer pile life. Worth it in bedrooms and living areas. Lifespan 15–20+ years with good underlay.'
    };

    document.getElementById('cp-area').textContent=area.toFixed(1)+' m² ('+billable.toFixed(1)+' m² billed incl. waste)';
    document.getElementById('cp-carpet-cost').textContent=nzd(carpetCost);
    document.getElementById('cp-underlay-cost').textContent=underlay==='no'?'Not included':nzd(underlayCost);
    document.getElementById('cp-install-cost').textContent=nzd(installCost);
    document.getElementById('cp-remove-cost').textContent=remove==='yes'?nzd(removeCost):'Not required';
    document.getElementById('cp-total').textContent=nzd(total);
    document.getElementById('cp-m2').textContent=nzd(perM2)+'/m² (total area)';
    document.getElementById('cp-note').textContent=notes[grade];
    document.getElementById('cp-result').style.display='block';
  }
  </script>

intro: |
  Estimate carpet supply and installation costs for any room in NZ. Enter your room size and carpet grade to get a breakdown including underlay and laying fees.

  Prices are based on 2026 NZ rates and include GST. Note that carpet is usually billed by the roll width (3.66m or 4m) so your actual invoice may differ slightly from the calculator's area estimate.

faq:
  - q: "How much does carpet cost to supply and lay in NZ?"
    a: "Carpet supply and installation in NZ typically costs $60–$130/m² all in, depending on carpet grade and underlay. A standard 20m² lounge runs $1,500–$3,000 fully fitted."
  - q: "How much do carpet layers charge to install carpet in NZ?"
    a: "Carpet layers in NZ charge $15–$25/m² for installation (laying, trimming and joining), plus a call-out/minimum fee of $80–$150. Most jobs include removal of old carpet for an additional $8–$12/m²."
  - q: "What underlay should I use for carpet in NZ?"
    a: "Standard 8mm polyurethane underlay ($15–20/m²) suits most rooms. For bedrooms or premium carpet, 10–12mm premium underlay ($22–30/m²) adds significantly more comfort and extends carpet life."
  - q: "How long does carpet last in NZ?"
    a: "Budget carpet lasts 5–10 years, mid-range 10–15 years, and premium carpet 15–20+ years with a good underlay. High-traffic areas (hallways, stairs) wear fastest."
  - q: "Can I supply my own carpet and just pay for installation?"
    a: "Yes — most NZ carpet layers will install customer-supplied carpet, though some charge a slightly higher lay rate. Make sure you order enough — typically allow 10% extra for waste and pattern matching."
---
