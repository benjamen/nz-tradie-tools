---
title: "NZ Construction Retentions Calculator"
seo_title: "Free NZ Retentions Calculator 2026 — Construction Contracts"
description: "Free NZ retentions calculator — work out retention amounts, release dates and trust requirements under the Construction Contracts Act. Instant results."
tags: [retentions, construction contracts, cash flow, subcontractors, NZ]
author: "NZ Tradie Tools"
related_articles: [unpaid-invoices-options-nz-tradies, cash-flow-management-nz-tradies, tradie-contract-guide-nz]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Contract value (ex GST) — $</label>
      <input type="number" id="ret-contract" placeholder="e.g. 250000" oninput="calcRet()">
    </div>
    <div class="calc-group">
      <label>Retention percentage agreed</label>
      <select id="ret-pct" onchange="calcRet()">
        <option value="5">5%</option>
        <option value="7.5">7.5%</option>
        <option value="10">10% (maximum allowed)</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Practical completion date</label>
      <input type="date" id="ret-pc-date" oninput="calcRet()">
    </div>
    <div class="calc-group">
      <label>Defects liability period</label>
      <select id="ret-dlp" onchange="calcRet()">
        <option value="3">3 months</option>
        <option value="6">6 months (most common)</option>
        <option value="12">12 months</option>
        <option value="24">24 months</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="ret-result" style="display:none">
    <h3>Retention Summary</h3>
    <div class="result-row"><span>Contract value</span><span id="ret-r-contract"></span></div>
    <div class="result-row"><span>Retention rate</span><span id="ret-r-pct"></span></div>
    <div class="result-row"><span>Total retention held</span><span id="ret-r-total" style="color:#c53030;font-weight:700"></span></div>
    <div class="result-row"><span>Released at practical completion (50%)</span><span id="ret-r-pc"></span></div>
    <div class="result-row"><span>Remaining after PC</span><span id="ret-r-remaining"></span></div>
    <div class="result-row"><span>Final release date (end of DLP)</span><span id="ret-r-date"></span></div>
    <div class="result-row"><span>Final release amount</span><span id="ret-r-final"></span></div>
    <div id="ret-trust-note" style="display:none;margin-top:.75rem;background:#fff8e1;border:1px solid #f6c90e;border-radius:6px;padding:.75rem;font-size:.85rem"></div>
  </div>
  <script>
  function fmt(n){return "$"+Math.round(n).toLocaleString("en-NZ");}
  function calcRet(){
    var cv=parseFloat(document.getElementById("ret-contract").value)||0;
    var pct=parseFloat(document.getElementById("ret-pct").value)||5;
    var dlp=parseInt(document.getElementById("ret-dlp").value)||6;
    var pcDate=document.getElementById("ret-pc-date").value;
    var r=document.getElementById("ret-result");
    if(!cv||cv<0){r.style.display="none";return;}
    var ret=cv*(pct/100);
    var pc50=ret*0.5;
    var final50=ret*0.5;
    var finalDate="—";
    if(pcDate){
      var d=new Date(pcDate);
      d.setMonth(d.getMonth()+dlp);
      finalDate=d.toLocaleDateString("en-NZ",{day:"numeric",month:"long",year:"numeric"});
    }
    document.getElementById("ret-r-contract").textContent=fmt(cv);
    document.getElementById("ret-r-pct").textContent=pct+"%";
    document.getElementById("ret-r-total").textContent=fmt(ret);
    document.getElementById("ret-r-pc").textContent=fmt(pc50);
    document.getElementById("ret-r-remaining").textContent=fmt(final50);
    document.getElementById("ret-r-date").textContent=finalDate;
    document.getElementById("ret-r-final").textContent=fmt(final50);
    var tn=document.getElementById("ret-trust-note");
    if(ret>=20000){
      tn.innerHTML="<strong>Trust account required.</strong> This retention is $20,000 or more. Under the Construction Contracts Amendment Act 2015, retentions of $20,000+ must be held in a separate trust account by the head contractor. As a subcontractor, you can request proof of this trust account in writing.";
      tn.style.display="";
    }else{tn.style.display="none";}
    r.style.display="";
  }
  </script>
faqs:
  - q: 'What is a construction retention in NZ?'
    a: 'A retention is an amount (typically 5–10%) withheld from progress payments on construction contracts. It is held as security against defects and released at practical completion and/or end of defects liability period.'
  - q: 'What does the Construction Contracts Act 2002 say about retentions?'
    a: 'Under the CCA 2002 (as amended 2015), retention money held by a head contractor or commercial principal must be held on trust and not used for any other purpose. Trust account requirements apply to retentions over $20,000 per sub.'
  - q: 'When must retentions be released in NZ?'
    a: 'The release schedule is agreed in the contract. Typically 50% is released at practical completion and the remaining 50% at expiry of the defects liability period (usually 12 months after PC). CCA payment claim rules apply.'
  - q: 'What is the maximum retention percentage in NZ?'
    a: 'There is no statutory maximum, but 5% is the NZ standard. Some residential contracts use 10% for smaller sub-trades. Retentions above 10% are unusual and may be challenged as unreasonable under the CCA.'
---

## NZ Construction Retentions — Know Your Rights

Retentions are a percentage of each progress payment withheld by head contractors (or principals) as security against defective work. They're one of the most common sources of payment disputes in NZ construction.

### The Legal Framework

The **Construction Contracts Act 2002** governs payment in NZ construction. Key rules for retentions:

**Maximum retention rate: 10%** — no contract can legally hold more than 10% in retentions.

**Release schedule** — most contracts release 50% of retentions at practical completion and the remaining 50% at the end of the defects liability period (DLP).

**Trust accounts** — under the 2015 amendments, retentions of $20,000 or more must be held in a separate trust account by the head contractor. As a subcontractor, you have the right to request evidence of this in writing.

### Common Retention Mistakes Tradies Make

1. **Not tracking retention amounts** — on a large project, retained amounts can reach tens of thousands. Always track what's owed.

2. **Missing the final release date** — set a calendar reminder for the end of the DLP. Head contractors won't always prompt you.

3. **Not asking for trust account evidence** — if your retention is over $20,000, it's your legal right to see proof of the trust account.

4. **Accepting retention clauses over 10%** — any clause requiring more than 10% retention is unenforceable under the Construction Contracts Act.

### If Retentions Aren't Released

If a head contractor won't release retentions after the DLP ends, you can apply for adjudication under the Construction Contracts Act. This is faster and cheaper than litigation and is specifically designed for payment disputes in construction.

See our [unpaid invoices guide](/articles/unpaid-invoices-options-nz-tradies) for the full process.
