---
title: "NZ Tool & Equipment Depreciation Calculator"
description: "Calculate the annual depreciation deduction for your tools and equipment using the IRD diminishing value method."
tags: [depreciation, tools, tax, IRD, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Purchase price (ex GST) — $</label>
      <input type="number" id="price" placeholder="e.g. 5000" oninput="calcDep()">
    </div>
    <div class="calc-group">
      <label>Depreciation rate (DV%) — IRD rate</label>
      <select id="dep-rate" onchange="calcDep()">
        <option value="30">30% — Power tools, hand tools</option>
        <option value="25">25% — Ladders, scaffolding</option>
        <option value="20">20% — Work vehicles (cars/utes)</option>
        <option value="13.5">13.5% — Trailers</option>
        <option value="48">48% — Computers, tablets</option>
        <option value="67">67% — Mobile phones</option>
        <option value="custom">Custom rate</option>
      </select>
    </div>
    <div class="calc-group" id="custom-group" style="display:none">
      <label>Custom DV rate %</label>
      <input type="number" id="custom-rate" placeholder="e.g. 25" oninput="calcDep()">
    </div>
    <div class="calc-group">
      <label>Years to show</label>
      <input type="number" id="years" value="5" min="1" max="15" oninput="calcDep()">
    </div>
    <div class="calc-group">
      <label>Business use %</label>
      <input type="number" id="bus-pct" value="100" min="1" max="100" oninput="calcDep()">
    </div>
  </div>
  <div id="dep-result" style="display:none;margin-top:1.25rem">
    <div class="calc-result">
      <h3>Depreciation Schedule</h3>
      <div id="dep-table"></div>
    </div>
  </div>
  <script>
  document.getElementById('dep-rate').addEventListener('change',function(){
    document.getElementById('custom-group').style.display=this.value==='custom'?'':'none';
    calcDep();
  });
  function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function calcDep(){
    var price=parseFloat(document.getElementById('price').value);
    var sel=document.getElementById('dep-rate').value;
    var rate=sel==='custom'?parseFloat(document.getElementById('custom-rate').value):parseFloat(sel);
    var yrs=parseInt(document.getElementById('years').value)||5;
    var bus=parseFloat(document.getElementById('bus-pct').value)||100;
    var res=document.getElementById('dep-result');
    if(isNaN(price)||price<=0||isNaN(rate)||rate<=0){res.style.display='none';return;}
    var html='<div class="result-row" style="font-weight:600"><span>Year</span><span>Depreciation</span><span>Book value</span><span>Tax deduction</span></div>';
    var val=price;
    for(var y=1;y<=yrs;y++){
      var dep=val*(rate/100);
      var deduct=dep*(bus/100);
      val=val-dep;
      html+='<div class="result-row"><span>Year '+y+'</span><span>'+fmt(dep)+'</span><span>'+fmt(val)+'</span><span class="result-highlight">'+fmt(deduct)+'</span></div>';
    }
    document.getElementById('dep-table').innerHTML=html;
    res.style.display='';
  }
  </script>
---

## How Depreciation Works for NZ Tradies

When you buy tools or equipment for your business, you generally can't deduct the full cost in the year of purchase (unless it's under $1,000 — see low-value asset rule below). Instead, you claim depreciation over the asset's useful life.

### The Low-Value Asset Rule

**Good news:** Items costing $1,000 or less (ex GST) can be written off in full in the year of purchase. This covers most hand tools, drill bits, small power tools, and accessories.

For anything over $1,000, you depreciate it over time.

### IRD Depreciation Rates for Tradies

IRD publishes depreciation rates for different asset types. The **diminishing value (DV)** method is most common:

| Asset | DV rate |
|---|---|
| Power tools (drill, grinder, saw) | 30% |
| Hand tools | 30% |
| Ladders, scaffolding | 25% |
| Work vehicles (utes, vans) | 20% |
| Trailers | 13.5% |
| Computers, tablets | 48% |
| Mobile phones | 67% |

Full rate table at [ird.govt.nz/depreciation](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-income/depreciation).

### Business vs Private Use

If you use equipment for both business and private purposes (e.g. a ute you also use on weekends), you can only claim the business-use percentage. Keep a logbook to support your claim.

### Tracking Depreciation

Your accountant or a tool like [Xero](https://www.xero.com/nz/) can manage a fixed asset register that automatically calculates annual depreciation. Well worth it once you have more than a handful of assets.
