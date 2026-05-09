---
title: "NZ Equipment Finance & Loan Calculator for Tradies"
description: "Calculate weekly repayments, total interest and true cost of financing tools, vehicles or equipment for your NZ tradie business."
tags: [equipment finance, loan, ute, tools, cash flow, NZ]
author: "NZ Tradie Tools"
related_articles: [nz-tradie-investment-boost-deduction-2026, vehicle-expenses-nz-tradies-ird, depreciation-calculator]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Purchase price (inc GST) — $</label>
      <input type="number" id="ef-price" placeholder="e.g. 55000" oninput="calcEF()">
    </div>
    <div class="calc-group">
      <label>Deposit / trade-in value — $</label>
      <input type="number" id="ef-deposit" value="0" oninput="calcEF()">
    </div>
    <div class="calc-group">
      <label>Interest rate (% p.a.)</label>
      <input type="number" id="ef-rate" placeholder="e.g. 9.5" step="0.1" oninput="calcEF()">
      <small>Typical NZ equipment finance: 7–14% p.a. depending on lender and credit.</small>
    </div>
    <div class="calc-group">
      <label>Loan term</label>
      <select id="ef-term" onchange="calcEF()">
        <option value="12">1 year</option>
        <option value="24">2 years</option>
        <option value="36" selected>3 years</option>
        <option value="48">4 years</option>
        <option value="60">5 years</option>
        <option value="84">7 years</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Repayment frequency</label>
      <select id="ef-freq" onchange="calcEF()">
        <option value="52">Weekly</option>
        <option value="26">Fortnightly</option>
        <option value="12">Monthly</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Balloon / residual payment — $</label>
      <input type="number" id="ef-balloon" value="0" oninput="calcEF()">
      <small>Some commercial leases include a final lump-sum payment.</small>
    </div>
  </div>
  <div class="calc-result" id="ef-result" style="display:none">
    <h3>Finance Summary</h3>
    <div class="result-row"><span>Amount financed</span><span id="ef-r-financed"></span></div>
    <div class="result-row"><span>Interest rate</span><span id="ef-r-rate"></span></div>
    <div class="result-row"><span id="ef-r-freq-label">Repayment</span><span id="ef-r-payment" style="font-size:1.2rem;font-weight:700;color:#0055a5"></span></div>
    <div class="result-row"><span>Total repayments</span><span id="ef-r-total-rep"></span></div>
    <div class="result-row"><span>Total interest paid</span><span id="ef-r-interest" style="color:#c53030"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>True total cost</span><span id="ef-r-true"></span></div>
    <div style="margin-top:1rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
      <strong>Tax tip:</strong> Interest on business equipment loans is generally deductible. The equipment itself is depreciated using IRD's diminishing value rates. Use our <a href="/calculators/depreciation-calculator.html">depreciation calculator</a> to estimate your annual deduction.
    </div>
  </div>
  <script>
  function fmt(n){return "$"+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,",");}
  function calcEF(){
    var price=parseFloat(document.getElementById("ef-price").value)||0;
    var deposit=parseFloat(document.getElementById("ef-deposit").value)||0;
    var annualRate=parseFloat(document.getElementById("ef-rate").value)||0;
    var termMonths=parseInt(document.getElementById("ef-term").value)||36;
    var freq=parseInt(document.getElementById("ef-freq").value)||12;
    var balloon=parseFloat(document.getElementById("ef-balloon").value)||0;
    var r=document.getElementById("ef-result");
    if(!price||!annualRate){r.style.display="none";return;}
    var principal=price-deposit;
    if(principal<=0){r.style.display="none";return;}
    var n=termMonths/12*freq;
    var rPer=annualRate/100/freq;
    var pv=principal-balloon/Math.pow(1+rPer,n);
    var payment;
    if(rPer===0){payment=pv/n;}
    else{payment=pv*rPer/(1-Math.pow(1+rPer,-n));}
    var totalRep=payment*n+balloon;
    var totalInt=totalRep-principal;
    var freqLabel=freq===52?"Weekly payment":freq===26?"Fortnightly payment":"Monthly payment";
    document.getElementById("ef-r-financed").textContent=fmt(principal);
    document.getElementById("ef-r-rate").textContent=annualRate+"% p.a.";
    document.getElementById("ef-r-freq-label").textContent=freqLabel;
    document.getElementById("ef-r-payment").textContent=fmt(payment);
    document.getElementById("ef-r-total-rep").textContent=fmt(totalRep);
    document.getElementById("ef-r-interest").textContent=fmt(totalInt);
    document.getElementById("ef-r-true").textContent=fmt(price-deposit+totalInt);
    r.style.display="";
  }
  </script>
---

## Financing Tools and Equipment for NZ Tradies

Most tradespeople finance at least some of their equipment — a work ute, a new compressor, or a set of power tools. Understanding the true cost of that finance helps you make better purchasing decisions.

### Types of Equipment Finance in NZ

**Hire purchase** — you own the asset from day one. Interest and depreciation are both deductible. Most common for tools and plant.

**Finance lease** — you don't own the asset; you lease it for an agreed term with a balloon payment at the end. The lease payments are fully deductible. Common for vehicles.

**Chattel mortgage** — similar to hire purchase, but the lender holds a mortgage over the asset. Common for larger equipment.

**Personal loan / overdraft** — higher interest rate, but more flexibility. Generally only suitable for smaller purchases.

### NZ Lenders for Trade Equipment

- **Heartland Bank** — popular for trade vehicles and equipment
- **UDC Finance** — vehicle and equipment specialists
- **HSBC / BNZ / ANZ** — business loans, better rates for established businesses
- **Dealer finance** — convenient but often higher rates; always compare

### The Investment Boost Deduction

From 22 August 2023, the NZ government introduced the **Investment Boost** deduction — an immediate 20% tax deduction on the cost of new assets (on top of normal depreciation) for the first year. This significantly improves the after-tax cost of new equipment purchases. See our [Investment Boost article](/articles/nz-tradie-investment-boost-deduction-2026.html) for details.

### Should You Buy or Finance?

If your cash flow is tight, financing spreads the cost but adds interest. If you have the cash, buying outright is cheaper overall. The break-even point is usually where the after-tax interest cost exceeds the return you could earn on that cash in your business.
