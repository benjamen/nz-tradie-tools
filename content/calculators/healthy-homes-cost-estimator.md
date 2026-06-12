---
title: "NZ Healthy Homes Cost Estimator"
description: "Estimate the cost to bring a rental property to Healthy Homes Standards — covering all 5 standards: heating, insulation, ventilation, moisture and draught-stopping."
tags: [Healthy Homes, rental, compliance, insulation, heating, NZ]
author: "NZ Tradie Tools"
related_articles: [healthy-homes-compliance-work-nz-tradies-2026, h1-insulation-calculator, heat-pump-sizing-calculator]
layout: calculator
calculator_html: |
  <p style="font-size:.88rem;color:#555;margin-bottom:1rem">Tick the work needed — the estimator shows typical NZ trade costs for each standard.</p>
  <div style="display:grid;gap:.75rem">
    <div style="border:1px solid #e2e8f0;border-radius:8px;padding:1rem">
      <strong>1. Heating Standard</strong>
      <p style="font-size:.82rem;color:#555;margin:.25rem 0 .5rem">A fixed heater capable of heating the main living room to 18°C is required.</p>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem">
        <input type="checkbox" id="hh-heat" onchange="calcHH()"> Install heat pump / fixed heater
      </label>
      <div id="hh-heat-extra" style="display:none;margin-top:.5rem">
        <label style="font-size:.82rem">Living area size (m²)</label>
        <input type="number" id="hh-heat-size" value="25" style="width:80px;padding:.3rem;border:1px solid #ccc;border-radius:4px;margin-left:.5rem" oninput="calcHH()">
      </div>
    </div>
    <div style="border:1px solid #e2e8f0;border-radius:8px;padding:1rem">
      <strong>2. Insulation Standard</strong>
      <p style="font-size:.82rem;color:#555;margin:.25rem 0 .5rem">Ceiling R2.9 min, underfloor R1.3 min (or as per H1 for new builds).</p>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem;margin-bottom:.4rem">
        <input type="checkbox" id="hh-ceil" onchange="calcHH()"> Install / top up ceiling insulation
      </label>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem">
        <input type="checkbox" id="hh-floor" onchange="calcHH()"> Install underfloor insulation
      </label>
      <div style="margin-top:.5rem">
        <label style="font-size:.82rem">Floor area (m²)</label>
        <input type="number" id="hh-floor-size" value="100" style="width:80px;padding:.3rem;border:1px solid #ccc;border-radius:4px;margin-left:.5rem" oninput="calcHH()">
      </div>
    </div>
    <div style="border:1px solid #e2e8f0;border-radius:8px;padding:1rem">
      <strong>3. Ventilation Standard</strong>
      <p style="font-size:.82rem;color:#555;margin:.25rem 0 .5rem">Extractor fans required in kitchen and bathrooms.</p>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem;margin-bottom:.4rem">
        <input type="checkbox" id="hh-kitchen-fan" onchange="calcHH()"> Kitchen extractor fan
      </label>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem">
        <input type="checkbox" id="hh-bath-fan" onchange="calcHH()"> Bathroom extractor fan(s)
      </label>
    </div>
    <div style="border:1px solid #e2e8f0;border-radius:8px;padding:1rem">
      <strong>4. Moisture &amp; Drainage</strong>
      <p style="font-size:.82rem;color:#555;margin:.25rem 0 .5rem">Ground moisture barrier required under suspended timber floors.</p>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem">
        <input type="checkbox" id="hh-moisture" onchange="calcHH()"> Install ground moisture barrier
      </label>
    </div>
    <div style="border:1px solid #e2e8f0;border-radius:8px;padding:1rem">
      <strong>5. Draught Stopping</strong>
      <p style="font-size:.82rem;color:#555;margin:.25rem 0 .5rem">Seal gaps in walls, floors, ceilings, windows and doors.</p>
      <label style="display:flex;align-items:center;gap:.5rem;font-size:.88rem">
        <input type="checkbox" id="hh-draught" onchange="calcHH()"> Draught stopping work
      </label>
    </div>
  </div>
  <div class="calc-result" id="hh-result" style="display:none;margin-top:1.25rem">
    <h3>Estimated Compliance Costs</h3>
    <div id="hh-lines"></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total estimated cost</span><span id="hh-total"></span></div>
    <p style="font-size:.8rem;color:#666;margin-top:.75rem">Estimates are NZ trade averages (2026). Costs vary by property age, size, and location. Get 3 quotes before proceeding.</p>
  </div>
  <script>
  function fmt(n){return '$'+Math.round(n).toLocaleString('en-NZ');}
  function fmtR(lo,hi){return '$'+lo.toLocaleString('en-NZ')+' – $'+hi.toLocaleString('en-NZ');}
  function calcHH(){
    var lines=[];
    var total=0;
    var heatOn=document.getElementById('hh-heat').checked;
    document.getElementById('hh-heat-extra').style.display=heatOn?''':''';
    if(heatOn){
      var sz=parseFloat(document.getElementById('hh-heat-size').value)||25;
      var kw=sz*0.1;
      var cost=1200+kw*120;
      lines.push({label:'Heat pump / fixed heater ('+(sz)+'m²)',lo:1200,hi:2800});
      total+=cost;
    }
    var floorSz=parseFloat(document.getElementById('hh-floor-size').value)||100;
    if(document.getElementById('hh-ceil').checked){
      var c=floorSz*12+300;lines.push({label:'Ceiling insulation ('+floorSz+'m²)',lo:Math.round(floorSz*10),hi:Math.round(floorSz*18+400)});total+=c;
    }
    if(document.getElementById('hh-floor').checked){
      var c=floorSz*14+400;lines.push({label:'Underfloor insulation ('+floorSz+'m²)',lo:Math.round(floorSz*12),hi:Math.round(floorSz*20+500)});total+=c;
    }
    if(document.getElementById('hh-kitchen-fan').checked){lines.push({label:'Kitchen extractor fan (supply + install)',lo:250,hi:550});total+=380;}
    if(document.getElementById('hh-bath-fan').checked){lines.push({label:'Bathroom extractor fan(s)',lo:200,hi:500});total+=320;}
    if(document.getElementById('hh-moisture').checked){lines.push({label:'Ground moisture barrier',lo:600,hi:1800});total+=1100;}
    if(document.getElementById('hh-draught').checked){lines.push({label:'Draught stopping',lo:200,hi:800});total+=480;}
    var r=document.getElementById('hh-result');
    if(!lines.length){r.style.display='none';return;}
    var html='<div class="result-row" style="font-weight:600"><span>Item</span><span>Typical range</span></div>';
    lines.forEach(function(l){html+='<div class="result-row"><span>'+l.label+'</span><span>'+fmtR(l.lo,l.hi)+'</span></div>';});
    document.getElementById('hh-lines').innerHTML=html;
    document.getElementById('hh-total').textContent=fmt(total)+' (mid estimate)';
    r.style.display='';
  }
  </script>
faqs:
  - q: 'What are the NZ Healthy Homes Standards for rental properties?'
    a: 'The five Healthy Homes Standards require landlords to provide: adequate heating (heat pump or equivalent), ceiling and underfloor insulation to H1 spec, effective ventilation (extractor fans), draught stopping, and moisture ingress prevention.'
  - q: 'When do Healthy Homes Standards apply in NZ?'
    a: 'From 1 July 2024, all private rental properties must comply with all five Healthy Homes Standards. Landlords who don''t comply face fines of up to $7,200 per breach.'
  - q: 'How much does it cost to comply with Healthy Homes Standards?'
    a: 'Average compliance cost for a typical NZ rental property is $3,000–$8,000. Properties needing a new heat pump ($2,000–$5,000), full insulation ($2,000–$4,000), and extractor fans ($300–$600) are at the upper end.'
  - q: 'What heating is required under NZ Healthy Homes?'
    a: 'The heating standard requires a fixed heater capable of heating the main living room to at least 18°C on the coldest days. A heat pump is the most common solution — it must be sized correctly using the MBIE heating assessment tool.'
---

## NZ Healthy Homes Standards — What Tradies Need to Know

The Healthy Homes Standards (HHS) require all private rental properties to comply with five minimum standards. Landlords hire tradies to do this work — understanding the standards helps you scope and quote accurately.

### The Five Standards

**1. Heating** — At least one fixed heater capable of heating the main living room to 18°C. A heat pump is the most common solution. Portables don't count.

**2. Insulation** — Ceiling insulation to at least R2.9 (existing ceiling space ≥ 400mm) or R1.5 (less than 400mm). Underfloor insulation to R1.3 where accessible.

**3. Ventilation** — Extractor fans ducted to outside in kitchens and bathrooms. Openable windows required in every habitable room.

**4. Moisture and Drainage** — A ground moisture barrier (polythene sheet) must cover at least 75% of accessible subfloor area. Adequate stormwater drainage required.

**5. Draught Stopping** — No unreasonable gaps in the building envelope. Open fireplaces must have a closeable vent.

### Compliance Deadlines

All private rentals must now comply — the deadline has passed. Landlords who haven't complied face fines up to $7,200 per property under the Residential Tenancies Act 1986.

### Quoting Healthy Homes Work

When quoting for landlords, assess all five standards together — it saves the client multiple visit fees and positions you as the complete solution. Use our [H1 Insulation Calculator](/calculators/h1-insulation-calculator) to check ceiling and underfloor R-value requirements by zone.

[MBIE's Healthy Homes guidance](https://www.tenancy.govt.nz/healthy-homes/) has the full technical standards.
