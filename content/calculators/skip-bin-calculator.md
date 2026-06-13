---
title: "NZ Skip Bin Size & Cost Estimator"
description: Estimate skip bin size and waste disposal cost for NZ construction jobs — including the NZ waste levy per tonne and recycling deductions.
tags: [waste, skip bin, demolition, disposal, NZ]
author: "NZ Tradie Tools"
related_articles: [how-to-price-a-job-nz-tradie-guide, managing-rising-material-costs-nz-2026, builder-pricing-guide-nz-2026]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Job type</label>
      <select id="sb-job" onchange="calcSB()">
        <option value="bathroom">Bathroom renovation</option>
        <option value="kitchen">Kitchen renovation</option>
        <option value="roof">Roof replacement</option>
        <option value="demo-room">Room demolition</option>
        <option value="full-reno">Full house renovation</option>
        <option value="new-build">New build site clearance</option>
        <option value="landscaping">Landscaping / earthworks</option>
        <option value="custom">Custom volume</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Floor area (m²) or quantity</label>
      <input type="number" id="sb-area" placeholder="e.g. 15" oninput="calcSB()">
    </div>
    <div class="calc-group">
      <label>Region</label>
      <select id="sb-region" onchange="calcSB()">
        <option value="1.2">Auckland</option>
        <option value="1.1">Wellington</option>
        <option value="1.0">Christchurch</option>
        <option value="0.95">Hamilton / Tauranga</option>
        <option value="0.9">Regional NZ</option>
      </select>
    </div>
    <div id="sb-custom-group" style="display:none" class="calc-group" style="grid-column:1/-1">
      <label>Volume of waste (m³)</label>
      <input type="number" id="sb-vol" placeholder="e.g. 6" oninput="calcSB()">
    </div>
  </div>
  <div class="calc-result" id="sb-result" style="display:none">
    <h3>Waste Disposal Estimate</h3>
    <div class="result-row"><span>Estimated volume</span><span id="sb-r-vol"></span></div>
    <div class="result-row"><span>Estimated weight</span><span id="sb-r-weight"></span></div>
    <div class="result-row"><span>Recommended skip size</span><span id="sb-r-skip" style="font-weight:700;color:#0055a5"></span></div>
    <div class="result-row"><span>Skip hire estimate (incl. GST)</span><span id="sb-r-hire"></span></div>
    <div class="result-row"><span>NZ waste levy (est. $60/tonne)</span><span id="sb-r-levy"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total estimated disposal cost</span><span id="sb-r-total"></span></div>
    <p style="font-size:.8rem;color:#666;margin-top:.75rem">Estimates only. Costs vary by location, waste type and current tip prices. Hazardous waste (asbestos, treated timber) has additional disposal requirements and costs.</p>
  </div>
  <script>
  function fmt(n){return "$"+Math.round(n).toLocaleString("en-NZ");}
  var JOB_DATA={
    bathroom:{vol:3,density:0.7,label:"Bathroom reno"},
    kitchen:{vol:2.5,density:0.6,label:"Kitchen reno"},
    roof:{vol:5,density:0.5,label:"Roof replacement"},
    "demo-room":{vol:6,density:0.8,label:"Room demolition"},
    "full-reno":{vol:20,density:0.7,label:"Full reno"},
    "new-build":{vol:8,density:0.6,label:"New build clearance"},
    landscaping:{vol:10,density:1.4,label:"Landscaping"},
    custom:{vol:0,density:0.7,label:"Custom"}
  };
  var SKIPS=[
    {size:"2m³ mini skip",cap:2,price:220},
    {size:"3m³ skip",cap:3,price:280},
    {size:"6m³ skip",cap:6,price:380},
    {size:"9m³ skip",cap:9,price:480},
    {size:"12m³ skip",cap:12,price:580},
    {size:"15m³ hook bin",cap:15,price:680}
  ];
  document.getElementById("sb-job").addEventListener("change",function(){
    document.getElementById("sb-custom-group").style.display=this.value==="custom"?"":"none";
  });
  function calcSB(){
    var job=document.getElementById("sb-job").value;
    var area=parseFloat(document.getElementById("sb-area").value)||1;
    var reg=parseFloat(document.getElementById("sb-region").value)||1.0;
    var jd=JOB_DATA[job];
    var r=document.getElementById("sb-result");
    var vol;
    if(job==="custom"){
      vol=parseFloat(document.getElementById("sb-vol").value)||0;
    }else{
      var areaFactor=["bathroom","kitchen","roof","demo-room"].includes(job)?area/15:area/100;
      vol=jd.vol*Math.max(0.5,areaFactor);
    }
    if(!vol||vol<0){r.style.display="none";return;}
    var weight=vol*jd.density;
    var skip=SKIPS.find(function(s){return s.cap>=vol;})||SKIPS[SKIPS.length-1];
    var levy=weight*60;
    var hire=skip.price*reg;
    var total=hire+levy;
    document.getElementById("sb-r-vol").textContent=vol.toFixed(1)+"m³";
    document.getElementById("sb-r-weight").textContent=weight.toFixed(1)+" tonnes (est.)";
    document.getElementById("sb-r-skip").textContent=skip.size;
    document.getElementById("sb-r-hire").textContent=fmt(hire);
    document.getElementById("sb-r-levy").textContent=fmt(levy);
    document.getElementById("sb-r-total").textContent=fmt(total);
    r.style.display="";
  }
  </script>
faqs:
  - q: 'What size skip bin do I need for a renovation in NZ?'
    a: 'A 3 m³ skip suits a bathroom or kitchen renovation (1–2 tonnes of waste). A 6 m³ skip suits a mid-size renovation or small demolition. A 9–12 m³ skip is for large house renovations or roofing jobs. Volume and weight both matter.'
  - q: 'How much does a skip bin cost in NZ?'
    a: 'Skip bin hire in NZ costs approximately $250–$400 for a 2–3 m³ mini skip, $400–$600 for a 4–6 m³ skip, and $600–$1,000 for a 9–12 m³ large skip. Prices include delivery and pickup but not overfill or heavy material surcharges.'
  - q: 'Can concrete and bricks go in a skip bin in NZ?'
    a: 'Many skip providers in NZ do not accept heavy materials like concrete, bricks, or tiles in general waste skips due to weight limits. You may need a dedicated ''heavy waste'' or ''concrete only'' skip, which is priced separately.'
  - q: 'What is the NZ waste levy on skip bins?'
    a: 'The NZ Waste Minimisation Act levy is currently $60/tonne for waste disposed to landfill (2024). This levy is passed on to customers by skip bin operators and is included in most skip hire prices for mixed construction waste.'
---

## NZ Construction Waste Disposal Costs

Waste disposal is one of the most commonly underquoted line items in NZ construction. On a full bathroom renovation, skip hire and tip fees can easily reach $800–$1,200 — and if you've quoted a fixed price without allowing for it, that comes out of your margin.

### The NZ Waste Levy

Under the Waste Minimisation Act 2008, a levy of **$60 per tonne** applies to all waste disposed of at municipal landfills in NZ. This levy is built into tip fees charged by waste companies and skip hire operators.

The levy is increasing — check [MfE's waste levy page](https://environment.govt.nz/what-government-is-doing/areas-of-work/waste/waste-levy/) for the current rate.

### Skip Bin Sizes in NZ

| Skip size | Typical use |
|---|---|
| 2m³ mini skip | Small kitchen reno, clean-up |
| 3m³ | Bathroom strip-out, small jobs |
| 6m³ | Roof replacement, large reno rooms |
| 9m³ | Full house declutter, multi-room reno |
| 12–15m³ hook bin | New build, demolition, landscaping |

### Hazardous Waste

**Asbestos** — any suspected asbestos must be tested before disposal. Licensed asbestos removalists must handle anything above trace amounts. Disposal at approved facilities costs significantly more than standard waste.

**Treated timber (CCA)** — old timber treated with copper-chrome-arsenic cannot go to standard landfill. It must go to a consented facility. Know what you're dealing with before quoting demolition work.

Include waste disposal as a separate line item on every quote — it protects your margin and is transparent for the client.
