---
title: "NZ Job Cost & Quote Builder"
description: "Calculate job costs, apply your markup, and produce a quote price with GST for NZ tradie jobs."
tags: [quoting, job cost, markup, GST, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Labour cost (ex GST) — $</label>
      <input type="number" id="labour" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Materials cost (ex GST) — $</label>
      <input type="number" id="materials" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Subcontractor cost (ex GST) — $</label>
      <input type="number" id="sub" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Other costs (ex GST) — $</label>
      <input type="number" id="other" value="0" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Markup on labour %</label>
      <input type="number" id="labour-markup" value="20" oninput="calcJob()">
    </div>
    <div class="calc-group">
      <label>Markup on materials %</label>
      <input type="number" id="mat-markup" value="15" oninput="calcJob()">
    </div>
  </div>
  <div class="calc-result" id="job-result">
    <h3>Quote Summary</h3>
    <div class="result-row"><span>Labour (with markup)</span><span id="j-labour"></span></div>
    <div class="result-row"><span>Materials (with markup)</span><span id="j-mat"></span></div>
    <div class="result-row"><span>Subcontractors</span><span id="j-sub"></span></div>
    <div class="result-row"><span>Other costs</span><span id="j-other"></span></div>
    <div class="result-row"><span>Subtotal (ex GST)</span><span id="j-sub-total"></span></div>
    <div class="result-row"><span>GST (15%)</span><span id="j-gst"></span></div>
    <div class="result-row"><span>Total quote price (inc GST)</span><span id="j-total"></span></div>
    <div class="result-row"><span>Your gross profit</span><span id="j-profit" class="result-highlight"></span></div>
  </div>
  <script>
  function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function calcJob(){
    var lab=parseFloat(document.getElementById('labour').value)||0;
    var mat=parseFloat(document.getElementById('materials').value)||0;
    var sub=parseFloat(document.getElementById('sub').value)||0;
    var oth=parseFloat(document.getElementById('other').value)||0;
    var lm=parseFloat(document.getElementById('labour-markup').value)||0;
    var mm=parseFloat(document.getElementById('mat-markup').value)||0;
    var labCharge=lab*(1+lm/100);
    var matCharge=mat*(1+mm/100);
    var subtotal=labCharge+matCharge+sub+oth;
    var gst=subtotal*0.15;
    var total=subtotal+gst;
    var profit=(labCharge-lab)+(matCharge-mat);
    document.getElementById('j-labour').textContent=fmt(labCharge);
    document.getElementById('j-mat').textContent=fmt(matCharge);
    document.getElementById('j-sub').textContent=fmt(sub);
    document.getElementById('j-other').textContent=fmt(oth);
    document.getElementById('j-sub-total').textContent=fmt(subtotal);
    document.getElementById('j-gst').textContent=fmt(gst);
    document.getElementById('j-total').textContent=fmt(total);
    document.getElementById('j-profit').textContent=fmt(profit);
  }
  calcJob();
  </script>
---

## How to Build an Accurate Job Quote

Winning jobs is great, but winning profitable jobs is better. Many NZ tradies underprice their work because they forget to account for all costs and apply the right markup.

### The Difference Between Markup and Margin

This trips up many tradies:

- **Markup** — the percentage you add on top of your cost (e.g. cost $100, markup 20% = charge $120)
- **Margin** — the percentage of the selling price that is profit (e.g. sell $120, profit $20 = 16.7% margin)

A 20% markup gives you a 16.7% gross margin — not 20%.

### Typical Markup Rates for NZ Tradies

| Item | Common markup |
|---|---|
| Labour | 15–30% |
| Materials | 10–20% |
| Subcontractors | 5–15% |
| Plant/equipment hire | 10–15% |

### What to Always Include in a Quote

1. All labour time (including travel, site prep, cleanup)
2. Materials at supplier cost — then apply your markup
3. Any subcontractor or hire costs
4. A contingency for variations (5–10% on complex jobs)
5. GST clearly shown separately

### Quote Presentation Tips

- Use a professional template — [Tradify](https://www.tradifyhq.com/) and [Fergus](https://www.fergus.com/) both produce great-looking quotes
- Always specify what's **included** and what's **excluded**
- Set a quote validity period (e.g. 30 days)
- Require a deposit on large jobs (10–20% is standard)
