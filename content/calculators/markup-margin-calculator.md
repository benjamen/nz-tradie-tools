---
title: "Markup vs Margin Calculator for NZ Tradies"
description: "Convert between markup percentage and gross margin percentage — a common source of confusion that can cost tradies thousands."
tags: [markup, margin, pricing, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchMM('markup')">Markup → Margin</button>
    <button class="calc-tab" onclick="switchMM('margin')">Margin → Markup</button>
    <button class="calc-tab" onclick="switchMM('price')">Cost → Price</button>
  </div>
  <div id="mm-markup">
    <div class="calc-grid">
      <div class="calc-group" style="grid-column:1/-1">
        <label>Markup % you apply</label>
        <input type="number" id="mu-pct" placeholder="e.g. 25" oninput="calcMU()">
      </div>
    </div>
    <div class="calc-result" id="mu-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Markup</span><span id="mu-out-mu"></span></div>
      <div class="result-row"><span>Equivalent gross margin</span><span id="mu-out-mg"></span></div>
      <div class="result-row"><span>Example: cost $100 → charge</span><span id="mu-out-ex"></span></div>
    </div>
  </div>
  <div id="mm-margin" style="display:none">
    <div class="calc-grid">
      <div class="calc-group" style="grid-column:1/-1">
        <label>Gross margin % you want</label>
        <input type="number" id="mg-pct" placeholder="e.g. 20" oninput="calcMG()">
      </div>
    </div>
    <div class="calc-result" id="mg-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Gross margin</span><span id="mg-out-mg"></span></div>
      <div class="result-row"><span>Required markup to achieve this</span><span id="mg-out-mu"></span></div>
      <div class="result-row"><span>Example: cost $100 → charge</span><span id="mg-out-ex"></span></div>
    </div>
  </div>
  <div id="mm-price" style="display:none">
    <div class="calc-grid">
      <div class="calc-group">
        <label>Your cost (ex GST) — $</label>
        <input type="number" id="pr-cost" placeholder="e.g. 500" oninput="calcPR()">
      </div>
      <div class="calc-group">
        <label>Markup % to apply</label>
        <input type="number" id="pr-mu" placeholder="e.g. 20" oninput="calcPR()">
      </div>
    </div>
    <div class="calc-result" id="pr-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Your cost</span><span id="pr-out-cost"></span></div>
      <div class="result-row"><span>Markup amount</span><span id="pr-out-mu"></span></div>
      <div class="result-row"><span>Price ex GST</span><span id="pr-out-ex"></span></div>
      <div class="result-row"><span>GST (15%)</span><span id="pr-out-gst"></span></div>
      <div class="result-row"><span>Price inc GST</span><span id="pr-out-inc"></span></div>
      <div class="result-row"><span>Gross margin</span><span id="pr-out-mg" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function pct(n){return n.toFixed(1)+'%';}
  function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function switchMM(t){
    var tabs=['markup','margin','price'];
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',i===tabs.indexOf(t));});
    tabs.forEach(function(id){document.getElementById('mm-'+id).style.display=id===t?'':'none';});
  }
  function calcMU(){
    var mu=parseFloat(document.getElementById('mu-pct').value);
    var r=document.getElementById('mu-result');
    if(isNaN(mu)||mu<0){r.style.display='none';return;}
    var mg=mu/(1+mu/100);
    var charge=100*(1+mu/100);
    document.getElementById('mu-out-mu').textContent=pct(mu);
    document.getElementById('mu-out-mg').textContent=pct(mg);
    document.getElementById('mu-out-ex').textContent=fmt(charge);
    r.style.display='';
  }
  function calcMG(){
    var mg=parseFloat(document.getElementById('mg-pct').value);
    var r=document.getElementById('mg-result');
    if(isNaN(mg)||mg>=100||mg<0){r.style.display='none';return;}
    var mu=mg/(1-mg/100);
    var charge=100/(1-mg/100);
    document.getElementById('mg-out-mg').textContent=pct(mg);
    document.getElementById('mg-out-mu').textContent=pct(mu);
    document.getElementById('mg-out-ex').textContent=fmt(charge);
    r.style.display='';
  }
  function calcPR(){
    var cost=parseFloat(document.getElementById('pr-cost').value);
    var mu=parseFloat(document.getElementById('pr-mu').value);
    var r=document.getElementById('pr-result');
    if(isNaN(cost)||isNaN(mu)||cost<=0){r.style.display='none';return;}
    var muAmt=cost*mu/100;
    var exGst=cost+muAmt;
    var gst=exGst*0.15;
    var inc=exGst+gst;
    var mg=muAmt/exGst*100;
    document.getElementById('pr-out-cost').textContent=fmt(cost);
    document.getElementById('pr-out-mu').textContent=fmt(muAmt);
    document.getElementById('pr-out-ex').textContent=fmt(exGst);
    document.getElementById('pr-out-gst').textContent=fmt(gst);
    document.getElementById('pr-out-inc').textContent=fmt(inc);
    document.getElementById('pr-out-mg').textContent=pct(mg)+' margin';
    r.style.display='';
  }
  </script>
---

## Markup vs Margin: Why It Matters for NZ Tradies

This is one of the most common pricing mistakes — and it can cost you thousands per year.

### The Key Difference

**Markup** is calculated on your **cost**.
**Margin** is calculated on your **selling price**.

| You apply | On a $1,000 job cost | You charge | Your profit | Markup | Margin |
|---|---|---|---|---|---|
| 20% markup | $1,000 | $1,200 | $200 | 20% | 16.7% |
| 20% margin | $1,000 | $1,250 | $250 | 25% | 20% |

If you say "I want to make 20% on this job" but calculate 20% markup, you're actually making 16.7% margin — not 20%.

### Why Tradies Get Caught Out

Many tradies quote a "25% margin" but calculate it as markup. Over a year, this can mean losing tens of thousands of dollars in expected profit.

**Example:**
- Annual materials spend: $200,000
- You think you're making 25% margin: expect $66,667 profit
- But you calculated 25% markup: you actually made $50,000
- **Shortfall: $16,667/year**

### The Formula

**To get X% margin:**
`Selling price = Cost ÷ (1 - X/100)`

**To get X% markup:**
`Selling price = Cost × (1 + X/100)`

### Recommended Margins for NZ Tradies

| Item | Target gross margin |
|---|---|
| Labour | 25–40% |
| Materials | 15–25% |
| Subcontractors | 10–15% |
| Overall job | 20–30% |

Use [Fergus](https://www.fergus.com/) or [Simpro](https://www.simprogroup.com/) to track your actual margins job by job and see where you're winning and losing.
