---
title: "NZ Provisional Tax Top-Up & Safe Harbour Calculator"
description: "Calculate whether you qualify for NZ provisional tax safe harbour, and the exact top-up needed to avoid IRD use-of-money interest (UOMI)."
tags: [provisional tax, safe harbour, UOMI, IRD, self-employed, NZ]
author: "NZ Tradie Tools"
related_articles: [provisional-tax-nz-tradies, provisional-tax-calculator, common-tax-mistakes-nz-tradies]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Prior year Residual Income Tax (RIT) — $</label>
      <input type="number" id="ptu-prior" placeholder="e.g. 9500" oninput="calcPTU()">
    </div>
    <div class="calc-group">
      <label>Provisional tax paid to date this year — $</label>
      <input type="number" id="ptu-paid" placeholder="e.g. 3000" oninput="calcPTU()">
    </div>
    <div class="calc-group">
      <label>Estimated RIT for this year — $</label>
      <input type="number" id="ptu-est" placeholder="e.g. 7500" oninput="calcPTU()">
      <small>Leave blank to use standard method (105% of prior year).</small>
    </div>
    <div class="calc-group">
      <label>Next instalment date</label>
      <select id="ptu-inst" onchange="calcPTU()">
        <option value="1">1st instalment — 28 Aug 2025</option>
        <option value="2">2nd instalment — 15 Jan 2026</option>
        <option value="3">3rd instalment — 7 May 2026</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="ptu-result" style="display:none">
    <h3>Top-Up Analysis</h3>
    <div id="ptu-safe-box" style="display:none;margin-bottom:1rem;background:#f0fff4;border:1px solid #68d391;border-radius:6px;padding:.75rem;font-size:.85rem;color:#22543d"></div>
    <div class="result-row"><span>Standard uplift total (105%)</span><span id="ptu-r-std"></span></div>
    <div class="result-row"><span>Estimated RIT this year</span><span id="ptu-r-est"></span></div>
    <div class="result-row"><span>Required by this instalment</span><span id="ptu-r-req" style="font-weight:700"></span></div>
    <div class="result-row"><span>Paid to date</span><span id="ptu-r-paid"></span></div>
    <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Top-up needed this instalment</span><span id="ptu-r-topup"></span></div>
    <div style="margin-top:.75rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
      <strong>UOMI rate:</strong> 10.91% p.a. If you miss or underpay an instalment and your final RIT is above $5,000, IRD charges UOMI on the shortfall from the instalment due date.
    </div>
  </div>
  <script>
  function fmt(n){return "$"+Math.round(Math.abs(n)).toLocaleString("en-NZ");}
  function calcPTU(){
    var prior=parseFloat(document.getElementById("ptu-prior").value)||0;
    var paid=parseFloat(document.getElementById("ptu-paid").value)||0;
    var est=parseFloat(document.getElementById("ptu-est").value)||0;
    var inst=parseInt(document.getElementById("ptu-inst").value)||1;
    var r=document.getElementById("ptu-result");
    if(!prior){r.style.display="none";return;}
    var stdTotal=prior*1.05;
    var useEst=est>0&&est<stdTotal;
    var targetTotal=useEst?est:stdTotal;
    var fraction=inst/3;
    var required=targetTotal*fraction;
    var topup=Math.max(0,required-paid);
    var safe=document.getElementById("ptu-safe-box");
    if(prior<5000){
      safe.innerHTML="<strong>Safe harbour applies.</strong> Your prior year RIT is under $5,000 — you do not need to pay any provisional tax. Your terminal tax is due 7 February 2027.";
      safe.style.display="";
    }else if(est>0&&est<5000){
      safe.innerHTML="<strong>Estimation safe harbour.</strong> Your estimated RIT is under $5,000. If correct, no provisional tax is required. Be careful — if actual RIT exceeds $5,000, UOMI applies back to the instalment dates.";
      safe.style.display="";
    }else{safe.style.display="none";}
    document.getElementById("ptu-r-std").textContent=fmt(stdTotal);
    document.getElementById("ptu-r-est").textContent=est?fmt(est):"— (using standard method)";
    document.getElementById("ptu-r-req").textContent=fmt(required)+" (by instalment "+inst+")";
    document.getElementById("ptu-r-paid").textContent=fmt(paid);
    document.getElementById("ptu-r-topup").textContent=topup>0?fmt(topup):"No top-up needed";
    r.style.display="";
  }
  </script>
faqs:
  - q: 'What happens if I underpay provisional tax in NZ?'
    a: 'If you underpay provisional tax, IRD charges use-of-money interest (UOMI) on the underpaid amount at 10.39% per year from the date the payment was due. You may also face an underestimation penalty if using the estimation method.'
  - q: 'How can I top up provisional tax before year end in NZ?'
    a: 'Log in to myIR and make a voluntary payment at any time before your final instalment date or tax return due date. Label it as a provisional tax payment for the current tax year.'
  - q: 'What is the UOMI rate in NZ for underpaid provisional tax?'
    a: 'As of 2024–25, the UOMI rate charged by IRD on underpaid tax is 10.39% per annum. IRD also pays 3.53% UOMI to taxpayers on overpayments.'
  - q: 'Should I top up provisional tax now or wait until year end?'
    a: 'Topping up early reduces UOMI from the due date. If you''re confident your year-end RIT will be higher than your instalments, making an early voluntary payment saves interest. Use your accounting software or tax agent to estimate the shortfall.'
---

## Provisional Tax Safe Harbour — The Safety Net Most Tradies Don't Know About

Safe harbour is an IRD provision that protects you from use-of-money interest (UOMI) even if you end up underpaying provisional tax during the year.

### The $5,000 Safe Harbour

If your **prior year RIT was under $5,000**, you're completely off the hook — no provisional tax required at all. Your full tax bill is simply due on 7 February after the tax year ends.

### The Standard Uplift Safe Harbour

If your prior year RIT was $5,000 or more, you qualify for safe harbour if you pay at least the **standard uplift amount** (105% of prior year RIT) across three equal instalments on time. Even if your actual RIT turns out to be higher, IRD won't charge UOMI — provided you paid the standard uplift on schedule.

This is why the standard method is the safe choice for most tradies whose income is similar year to year.

### When UOMI Applies

UOMI (currently **10.91% p.a.**) applies when:
- You use the estimation method and underestimate your RIT
- You miss or underpay instalments under the standard method
- Your final RIT is over $5,000 and you didn't pay the standard uplift

The UOMI charge runs from the instalment due date to the date you actually pay. On a $10,000 shortfall, that's roughly $1,091 per year — enough to hurt.

### Mid-Year Income Drop

If your income has dropped significantly during the year (a slow patch, injury, or loss of a major client), you can switch to the estimation method and reduce your upcoming instalment. Just be conservative — underestimating carries UOMI risk. Talk to your accountant before making this call.
