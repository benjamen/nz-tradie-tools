---
title: "NZ Hot Water Cylinder Sizing Calculator"
description: "Calculate the right hot water cylinder size for a NZ home or rental — including Healthy Homes Standards compliance for rental properties."
tags: [plumbing, hot water, Healthy Homes, cylinder sizing, NZ]
author: "NZ Tradie Tools"
related_articles: [healthy-homes-compliance-work-nz-tradies-2026, new-plumbing-self-certification-nz, new-lead-free-plumbing-standards-nz]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Number of occupants</label>
      <input type="number" id="hw-people" value="3" min="1" max="12" oninput="calcHW()">
    </div>
    <div class="calc-group">
      <label>Property type</label>
      <select id="hw-type" onchange="calcHW()">
        <option value="res">Owner-occupied residential</option>
        <option value="rental">Rental (Healthy Homes compliance)</option>
        <option value="commercial">Small commercial / office</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Usage pattern</label>
      <select id="hw-usage" onchange="calcHW()">
        <option value="1.0">Average (1–2 showers/day)</option>
        <option value="1.3">High (bathtubs, long showers)</option>
        <option value="0.8">Low (short showers, small household)</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Heat source</label>
      <select id="hw-heat" onchange="calcHW()">
        <option value="electric">Electric (mains pressure)</option>
        <option value="heatpump">Heat pump water heater</option>
        <option value="solar">Solar (with electric boost)</option>
        <option value="gas">Gas continuous flow</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="hw-result" style="display:none">
    <h3>Cylinder Recommendation</h3>
    <div class="result-row"><span>Recommended cylinder size</span><span id="hw-size" style="font-size:1.2rem;font-weight:700;color:#0055a5"></span></div>
    <div class="result-row"><span>Daily hot water demand (est.)</span><span id="hw-demand"></span></div>
    <div id="hw-rental-note" style="display:none;margin-top:.75rem;background:#f0fff4;border:1px solid #68d391;border-radius:6px;padding:.75rem;font-size:.85rem;color:#22543d"></div>
    <div id="hw-gas-note" style="display:none;margin-top:.75rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem"></div>
    <div style="margin-top:.75rem;background:#fff8e1;border:1px solid #f6c90e;border-radius:6px;padding:.75rem;font-size:.85rem">
      <strong>Next available sizes:</strong> Cylinders are typically sold in 135L, 180L, 250L, 300L and 400L. Always size up to the next standard size.
    </div>
  </div>
  <script>
  function calcHW(){
    var people=parseInt(document.getElementById("hw-people").value)||1;
    var type=document.getElementById("hw-type").value;
    var usage=parseFloat(document.getElementById("hw-usage").value)||1.0;
    var heat=document.getElementById("hw-heat").value;
    var r=document.getElementById("hw-result");
    if(people<1){r.style.display="none";return;}
    var basePerPerson=55;
    if(heat==="heatpump")basePerPerson=50;
    if(heat==="solar")basePerPerson=60;
    var demand=people*basePerPerson*usage;
    var sizes=[135,180,250,300,400];
    var rec=sizes.find(function(s){return s>=demand;})||400;
    if(type==="rental"&&rec<180)rec=180;
    document.getElementById("hw-size").textContent=rec+"L";
    document.getElementById("hw-demand").textContent=Math.round(demand)+"L/day";
    var rn=document.getElementById("hw-rental-note");
    if(type==="rental"){
      rn.innerHTML="<strong>Healthy Homes compliance:</strong> Rental properties must have hot water capable of delivering water at 55°C within 60 seconds at the tap (AS/NZS 3500). Minimum recommended size for rentals is 180L. Ensure thermostat is set to at least 60°C (to kill legionella) with a tempering valve to 55°C at outlets.";
      rn.style.display="";
    }else{rn.style.display="none";}
    var gn=document.getElementById("hw-gas-note");
    if(heat==="gas"){
      gn.innerHTML="<strong>Gas continuous flow:</strong> No cylinder needed — the unit heats on demand. Size the unit by flow rate (L/min) rather than volume. A typical NZ home needs 16–26 L/min capacity.";
      gn.style.display="";
    }else{gn.style.display="none";}
    r.style.display="";
  }
  calcHW();
  </script>
faqs:
  - q: 'What size hot water cylinder do I need in NZ?'
    a: 'A common rule is 45–55 litres per person. So a household of 4 needs a 180–220 litre cylinder. Large families, frequent bathers, or high hot water demand may need 250–300 litres.'
  - q: 'Does a hot water cylinder need Healthy Homes compliance?'
    a: 'Healthy Homes Standards do not directly regulate hot water systems in rentals. However, the hot water cylinder must have a functioning pressure relief valve and comply with NZOSHA and plumbing regulations.'
  - q: 'What temperature should a hot water cylinder be set to in NZ?'
    a: 'NZS 4305 recommends storing hot water at 60°C minimum to prevent Legionella bacteria growth. Tempering valves are required at point-of-use for showers to limit temperature to 45°C for safety.'
  - q: 'Should I get a heat pump hot water system in NZ?'
    a: 'Heat pump water heaters are 3–4× more energy efficient than electric resistance elements and can reduce water heating costs by 60–70%. EECA estimates payback of 3–5 years at current power prices in NZ.'
---

## Hot Water Cylinder Sizing for NZ Plumbers

Sizing a hot water cylinder correctly is one of the most practical jobs a plumber does. Too small and the household runs cold; too large and you're paying to heat water that's never used.

### NZ Rule of Thumb

The standard NZ guide is **50–60 litres per person** for a mains pressure electric cylinder. This accounts for a daily shower, hand washing, and dishwashing.

| Household | Recommended size |
|---|---|
| 1–2 people | 135L |
| 2–3 people | 180L |
| 3–4 people | 250L |
| 4–5 people | 300L |
| 6+ people | 400L |

### Healthy Homes Standards for Rentals

Under the Healthy Homes Standards, rental properties must have a hot water system that:
- Delivers water at **55°C within 60 seconds** at the point of use
- Has a thermostat set to at least **60°C** (to prevent legionella growth)
- Uses a **tempering valve** to reduce to 55°C at taps

The minimum practical size for a rental is **180L** — a 135L cylinder often can't maintain adequate temperature with multiple occupants.

### Heat Pump Water Heaters

Heat pump water heaters (e.g. Stiebel Eltron, Reclaim, Rheem) are increasingly popular in NZ. They use 60–70% less electricity than standard electric cylinders. They work best in garages or utility rooms where they can draw heat from ambient air. Allow for noise (similar to a heat pump unit) when selecting location.

### Compliance

All hot water work must comply with **AS/NZS 3500** (Plumbing and Drainage) and be carried out by a registered plumber. Temperature and pressure relief valves must be installed and discharged safely.
