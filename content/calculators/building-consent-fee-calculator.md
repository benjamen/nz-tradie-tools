---
title: "NZ Building Consent Fee Estimator"
description: "Estimate NZ building consent fees including the MBIE building levy, BRANZ levy, and council processing fees — so you can include them in your quote."
tags: [building consent, MBIE, BRANZ, fees, builders, NZ]
author: "NZ Tradie Tools"
related_articles: [do-you-need-building-consent-nz, building-consent-reform-nz-2026-tradies-guide, how-to-price-a-job-nz-tradie-guide]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group" style="grid-column:1/-1">
      <label>Estimated project value (inc materials &amp; labour) — $</label>
      <input type="number" id="bc-value" placeholder="e.g. 350000" oninput="calcBC()">
    </div>
    <div class="calc-group">
      <label>Council / region</label>
      <select id="bc-council" onchange="calcBC()">
        <option value="1.5">Auckland Council</option>
        <option value="1.1">Wellington City Council</option>
        <option value="0.9">Christchurch City Council</option>
        <option value="0.85">Hamilton City Council</option>
        <option value="0.85">Tauranga City Council</option>
        <option value="0.8">Dunedin City Council</option>
        <option value="0.75">Palmerston North CC</option>
        <option value="0.75">Napier City Council</option>
        <option value="0.75">Hastings District Council</option>
        <option value="0.75">New Plymouth DC</option>
        <option value="0.7">Other council</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Project type</label>
      <select id="bc-type" onchange="calcBC()">
        <option value="1.0">New residential build</option>
        <option value="0.8">Residential addition / alteration</option>
        <option value="1.2">New commercial build</option>
        <option value="0.7">Residential renovation (internal)</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="bc-result" style="display:none">
    <h3>Estimated Consent Fees</h3>
    <div class="result-row"><span>MBIE building levy ($1.75 per $1,000 over $65k)</span><span id="bc-mbie"></span></div>
    <div class="result-row"><span>BRANZ levy ($1.00 per $1,000 over $20k)</span><span id="bc-branz"></span></div>
    <div class="result-row"><span>Estimated council processing fee</span><span id="bc-council-fee"></span></div>
    <div class="result-row"><span>Code Compliance Certificate (est.)</span><span id="bc-ccc"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total estimated consent fees</span><span id="bc-total"></span></div>
    <p style="font-size:.8rem;color:#666;margin-top:.75rem">Council fees are estimates only — confirm the exact amount with your council before quoting. MBIE and BRANZ levies are legislated and fixed.</p>
  </div>
  <script>
  function fmt(n){return '$'+Math.round(n).toLocaleString('en-NZ');}
  function calcBC(){
    var v=parseFloat(document.getElementById('bc-value').value)||0;
    var cpct=parseFloat(document.getElementById('bc-council').value)||0.9;
    var tpct=parseFloat(document.getElementById('bc-type').value)||1.0;
    var r=document.getElementById('bc-result');
    if(!v||v<0){r.style.display='none';return;}
    var mbie=v>65001?(v-65001)*1.75/1000:0;
    var branz=v>20000?(v-20000)*1.00/1000:0;
    var council=Math.min(Math.max(v*cpct*tpct/100,800),18000);
    var ccc=Math.min(Math.max(v*0.15/100,300),2500);
    var total=mbie+branz+council+ccc;
    document.getElementById('bc-mbie').textContent=fmt(mbie);
    document.getElementById('bc-branz').textContent=fmt(branz);
    document.getElementById('bc-council-fee').textContent=fmt(council);
    document.getElementById('bc-ccc').textContent=fmt(ccc);
    document.getElementById('bc-total').textContent=fmt(total);
    r.style.display='';
  }
  </script>
---

## Why Consent Fees Matter for Builders

Building consent fees are a significant cost that many tradies forget to include in their quotes. On a $350,000 new build in Auckland, consent fees can easily reach $8,000–$12,000.

### The Two Legislated Levies

These are fixed by law and apply across all councils:

**MBIE Building Levy** — $1.75 per $1,000 of project value, for projects over $65,001. Set under the Building Act 2004.

**BRANZ Levy** — $1.00 per $1,000 of project value, for projects over $20,000. Funds building research at BRANZ.

### Council Processing Fees

On top of the legislated levies, each council charges processing fees that vary significantly:

- **Auckland** — typically the highest in NZ. A standard new build can cost $5,000–$12,000 in processing fees alone.
- **Wellington** — $3,000–$7,000 for a new build
- **Christchurch** — $2,500–$6,000
- **Regional councils** — generally $1,500–$4,000

**Always confirm the exact fee with the council before quoting.** Most councils publish fee schedules on their website.

### Code Compliance Certificate

Once the build is complete and inspections pass, a Code Compliance Certificate (CCC) is issued. This is a separate fee from the original consent — typically $300–$2,500 depending on the project.

### Include Consent Fees in Every Quote

Under the Construction Contracts Act 2002, variations after contract signing can be disputed. If consent fees aren't included in your original quote, recovering them later can be difficult. Always include them as a line item.
