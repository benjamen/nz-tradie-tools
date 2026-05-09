---
title: "NZ Retaining Wall Soil Pressure Calculator"
description: "Calculate active soil pressure and surcharge loads on retaining walls — and check whether engineering sign-off is required under NZ Building Code B1."
tags: [retaining wall, soil pressure, building consent, engineers, NZ]
author: "NZ Tradie Tools"
related_articles: [do-you-need-building-consent-nz, building-consent-fee-calculator, retaining-wall-calculator]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Wall height (m)</label>
      <input type="number" id="rw-height" placeholder="e.g. 1.8" step="0.1" oninput="calcRW()">
    </div>
    <div class="calc-group">
      <label>Soil type</label>
      <select id="rw-soil" onchange="calcRW()">
        <option value="0.33">Granular / free-draining (Ka=0.33)</option>
        <option value="0.40">Silty clay (Ka=0.40)</option>
        <option value="0.50">Soft clay / fill (Ka=0.50)</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Soil unit weight (kN/m³)</label>
      <select id="rw-density" onchange="calcRW()">
        <option value="17">17 kN/m³ — dry granular</option>
        <option value="19">19 kN/m³ — moist soil (typical NZ)</option>
        <option value="20">20 kN/m³ — saturated / clay</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Surcharge load on retained area</label>
      <select id="rw-surcharge" onchange="calcRW()">
        <option value="0">None (garden / grass only)</option>
        <option value="5">Pedestrian only (5 kPa)</option>
        <option value="10">Driveway (10 kPa)</option>
        <option value="20">Parking / light vehicles (20 kPa)</option>
        <option value="50">Heavy vehicles / structure (50 kPa)</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Distance from wall to boundary / structure (m)</label>
      <input type="number" id="rw-setback" placeholder="e.g. 1.5" step="0.1" oninput="calcRW()">
    </div>
  </div>
  <div class="calc-result" id="rw-result" style="display:none">
    <h3>Soil Pressure Estimate</h3>
    <div class="result-row"><span>Active earth pressure at base (Rankine)</span><span id="rw-r-pressure"></span></div>
    <div class="result-row"><span>Surcharge lateral pressure</span><span id="rw-r-surcharge"></span></div>
    <div class="result-row"><span>Total lateral force per metre of wall</span><span id="rw-r-total"></span></div>
    <div id="rw-consent" style="margin-top:1rem;border-radius:6px;padding:.75rem;font-size:.85rem"></div>
    <p style="font-size:.8rem;color:#666;margin-top:.75rem">This is an indicative calculation only using Rankine's simplified theory. Always engage a geotechnical engineer for walls over 1.5m or near structures. This tool does not replace engineering assessment.</p>
  </div>
  <script>
  function calcRW(){
    var H=parseFloat(document.getElementById("rw-height").value)||0;
    var Ka=parseFloat(document.getElementById("rw-soil").value)||0.33;
    var g=parseFloat(document.getElementById("rw-density").value)||19;
    var q=parseFloat(document.getElementById("rw-surcharge").value)||0;
    var setback=parseFloat(document.getElementById("rw-setback").value)||0;
    var r=document.getElementById("rw-result");
    if(!H){r.style.display="none";return;}
    var Pa=0.5*Ka*g*H*H;
    var Pq=Ka*q*H;
    var total=Pa+Pq;
    document.getElementById("rw-r-pressure").textContent=Pa.toFixed(1)+" kN/m";
    document.getElementById("rw-r-surcharge").textContent=Pq.toFixed(1)+" kN/m";
    document.getElementById("rw-r-total").textContent=total.toFixed(1)+" kN/m";
    var cb=document.getElementById("rw-consent");
    var needsConsent=H>1.5||(H>1.0&&setback<1.5);
    var needsEngineer=H>2.0||q>10||(H>1.5&&q>5);
    if(needsEngineer){
      cb.style.background="#fff0f0";cb.style.border="1px solid #fc8181";
      cb.innerHTML="<strong style="color:#c53030">Engineering sign-off required.</strong> Walls over 2m high, or with significant surcharge loads, require a geotechnical or structural engineer under NZBC B1. Provide engineering calculations to your BCA with the consent application.";
    }else if(needsConsent){
      cb.style.background="#fff8e1";cb.style.border="1px solid #f6c90e";
      cb.innerHTML="<strong>Building consent likely required.</strong> Walls over 1.5m high (or over 1.0m within 1.5m of a boundary or structure) generally require building consent under the Building Act 2004. Check with your local council.";
    }else{
      cb.style.background="#f0fff4";cb.style.border="1px solid #68d391";
      cb.innerHTML="<strong style="color:#22543d">Consent may not be required.</strong> Walls under 1.5m on private property may be exempt — but check with your local council, as exemptions vary. Even exempt walls must still meet NZBC structural standards.";
    }
    r.style.display="";
  }
  </script>
---

## NZ Retaining Wall Consent Rules

Retaining walls are one of the most common jobs where consent rules catch builders and landscapers out.

### When Consent Is Required

Under **Schedule 1 of the Building Act 2004**, building consent is generally required for retaining walls that:
- Are **over 1.5m high**, or
- Are **over 1.0m high** and within 1.5m of a boundary, structure, or public place

Walls under 1.5m on open private property may qualify for an exemption — but "may" is the key word. Always confirm with your local council, as exemptions can be restricted by site conditions or district plan rules.

### When Engineering Is Required

Any wall that requires consent will also need engineering input demonstrating compliance with **NZBC B1 (Structure)**. Typically this means:
- A geotechnical site report (for walls over 2m, or on problematic soils)
- Structural engineering calculations and drawings
- Specification of materials, drainage, and construction method

The cost of engineering (typically $1,500–$5,000) should be built into your quote.

### The Soil Pressure Formula

This calculator uses **Rankine's active earth pressure theory** — the standard simplified method for estimating lateral soil loads on retaining walls:

- Active pressure: Pa = ½ × Ka × γ × H²
- Surcharge pressure: Pq = Ka × q × H

Where Ka = coefficient of active earth pressure, γ = soil unit weight (kN/m³), H = wall height (m), q = surcharge pressure (kPa).

This is indicative only — an actual engineering assessment considers drainage, seismic loads, foundation conditions, and construction method.
