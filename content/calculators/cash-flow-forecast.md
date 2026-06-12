---
title: "Cash Flow Forecast Calculator — 12-Week Tradie Business Planner"
description: "Plan your tradie business cash flow 12 weeks ahead — track expected income, expenses, tax reserve, and running balance to spot cash gaps before they hit."
tags: [cash flow, forecast, business, planning, NZ, tradie]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Opening bank balance ($)</label><input type="number" id="cf-open" placeholder="e.g. 5000" value="5000" oninput="buildCF()"></div>
    <div class="calc-group"><label>Expected weekly income ($)</label><input type="number" id="cf-income" placeholder="e.g. 3500" oninput="buildCF()"></div>
    <div class="calc-group"><label>Weekly wages / subbie payments ($)</label><input type="number" id="cf-wages" placeholder="e.g. 0" value="0" oninput="buildCF()"></div>
    <div class="calc-group"><label>Weekly materials / supplies ($)</label><input type="number" id="cf-mats" placeholder="e.g. 400" value="0" oninput="buildCF()"></div>
    <div class="calc-group"><label>Weekly overheads (fuel, phone, etc.) ($)</label><input type="number" id="cf-overheads" placeholder="e.g. 200" value="0" oninput="buildCF()"></div>
    <div class="calc-group"><label>Set-aside for tax &amp; GST (%)</label><input type="number" id="cf-tax-pct" placeholder="e.g. 28" value="28" oninput="buildCF()"></div>
    <div class="calc-group">
      <label>Large payments (week &amp; amount)</label>
      <div style="display:flex;gap:.5rem;align-items:center;flex-wrap:wrap">
        <input type="number" id="lp1-wk" placeholder="Wk #" style="width:60px" oninput="buildCF()">
        <input type="number" id="lp1-amt" placeholder="$" style="width:100px" oninput="buildCF()">
        <input type="number" id="lp2-wk" placeholder="Wk #" style="width:60px" oninput="buildCF()">
        <input type="number" id="lp2-amt" placeholder="$" style="width:100px" oninput="buildCF()">
      </div>
      <small style="color:#888;font-size:.78rem">e.g. IRD provisional tax, equipment purchase</small>
    </div>
  </div>
  <div id="cf-result" style="display:none;margin-top:1rem">
    <h3 style="margin-bottom:.5rem">12-Week Cash Flow Forecast</h3>
    <div style="overflow-x:auto">
      <table class="calc-table" id="cf-table" style="font-size:.82rem;width:100%;border-collapse:collapse">
        <thead>
          <tr style="background:#1b2a4a;color:#fff">
            <th style="padding:.4rem .5rem;text-align:left">Week</th>
            <th style="padding:.4rem .5rem;text-align:right">Income</th>
            <th style="padding:.4rem .5rem;text-align:right">Expenses</th>
            <th style="padding:.4rem .5rem;text-align:right">Tax Reserve</th>
            <th style="padding:.4rem .5rem;text-align:right">Net</th>
            <th style="padding:.4rem .5rem;text-align:right">Balance</th>
          </tr>
        </thead>
        <tbody id="cf-tbody"></tbody>
      </table>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.75rem;margin-top:1rem">
      <div style="background:#f0f4f8;padding:.75rem;border-radius:4px">
        <div style="font-size:.75rem;color:#666;text-transform:uppercase;letter-spacing:.04em">Closing Balance</div>
        <div style="font-size:1.2rem;font-weight:700" id="cf-close"></div>
      </div>
      <div style="background:#f0f4f8;padding:.75rem;border-radius:4px">
        <div style="font-size:.75rem;color:#666;text-transform:uppercase;letter-spacing:.04em">Lowest Balance</div>
        <div style="font-size:1.2rem;font-weight:700" id="cf-low"></div>
      </div>
      <div style="background:#f0f4f8;padding:.75rem;border-radius:4px">
        <div style="font-size:.75rem;color:#666;text-transform:uppercase;letter-spacing:.04em">Tax Reserve Built</div>
        <div style="font-size:1.2rem;font-weight:700" id="cf-taxres"></div>
      </div>
    </div>
  </div>
  <script>
  function nzd(n,c){var s=(c||'$')+Math.abs(n).toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');return n<0?'('+s+')':s;}
  function buildCF(){
    var open=parseFloat(document.getElementById('cf-open').value)||0;
    var inc=parseFloat(document.getElementById('cf-income').value)||0;
    var wages=parseFloat(document.getElementById('cf-wages').value)||0;
    var mats=parseFloat(document.getElementById('cf-mats').value)||0;
    var oh=parseFloat(document.getElementById('cf-overheads').value)||0;
    var taxPct=(parseFloat(document.getElementById('cf-tax-pct').value)||28)/100;
    var lp1wk=parseInt(document.getElementById('lp1-wk').value)||0;
    var lp1amt=parseFloat(document.getElementById('lp1-amt').value)||0;
    var lp2wk=parseInt(document.getElementById('lp2-wk').value)||0;
    var lp2amt=parseFloat(document.getElementById('lp2-amt').value)||0;
    if(!inc){document.getElementById('cf-result').style.display='none';return;}
    var bal=open;
    var minBal=open;
    var totalTax=0;
    var tbody=document.getElementById('cf-tbody');
    tbody.innerHTML='';
    for(var w=1;w<=12;w++){
      var taxRes=inc*taxPct;
      var netInc=inc-taxRes;
      var exp=wages+mats+oh;
      if(w===lp1wk) exp+=lp1amt;
      if(w===lp2wk) exp+=lp2amt;
      var net=netInc-exp;
      bal+=net;
      totalTax+=taxRes;
      if(bal<minBal) minBal=bal;
      var neg=bal<0;
      var tr=document.createElement('tr');
      tr.style.background=neg?'#fee2e2':(w%2===0?'#f4f6f8':'#fff');
      tr.innerHTML='<td style="padding:.35rem .5rem">Wk '+w+'</td>'+
        '<td style="padding:.35rem .5rem;text-align:right;color:#166534">'+nzd(inc)+'</td>'+
        '<td style="padding:.35rem .5rem;text-align:right;color:#7f1d1d">'+nzd(exp)+'</td>'+
        '<td style="padding:.35rem .5rem;text-align:right;color:#713f12">'+nzd(taxRes)+'</td>'+
        '<td style="padding:.35rem .5rem;text-align:right;font-weight:600;color:'+(net>=0?'#166534':'#c0392b')+'">'+nzd(net)+'</td>'+
        '<td style="padding:.35rem .5rem;text-align:right;font-weight:700;color:'+(bal>=0?'#1b2a4a':'#c0392b')+'">'+nzd(bal)+'</td>';
      tbody.appendChild(tr);
    }
    document.getElementById('cf-close').textContent=nzd(bal);
    document.getElementById('cf-close').style.color=bal>=0?'#166534':'#c0392b';
    document.getElementById('cf-low').textContent=nzd(minBal);
    document.getElementById('cf-low').style.color=minBal>=0?'#166534':'#c0392b';
    document.getElementById('cf-taxres').textContent=nzd(totalTax);
    document.getElementById('cf-result').style.display='';
  }
  </script>
related_articles: [cash-flow-management-nz-tradies, provisional-tax-nz-tradies]
faqs:
  - q: 'How do I do a cash flow forecast for my tradie business?'
    a: 'List all expected income by week or month (jobs invoiced, deposits received). Then list all expected outgoings (wages, materials, insurance, ACC, GST payments). The difference each period is your net cash position.'
  - q: 'How far ahead should I forecast cash flow?'
    a: 'Most small tradie businesses forecast 3–6 months ahead. This is far enough to spot cash shortfalls before they hit, but close enough that numbers remain useful. Update it monthly.'
  - q: 'What causes cash flow problems for NZ tradies?'
    a: 'The most common causes are: slow-paying clients (30–60 day terms), GST and provisional tax not set aside, uneven work flow (feast and famine), and materials costs paid before jobs are invoiced.'
  - q: 'How can I improve cash flow as a tradie?'
    a: 'Require a deposit upfront (20–30%), invoice immediately on job completion, offer payment by credit card, chase overdue invoices within 7 days, and hold a GST reserve account separate from operating funds.'
---

## Using the Cash Flow Forecast

Enter your expected weekly income and regular expenses. Red rows show weeks where your bank balance goes negative — a warning sign to act before it happens.

### Tips for Accurate Forecasting

**Income:** Be conservative. If you expect $4,000 but clients sometimes pay late, use $3,000–$3,500. The point of forecasting is to spot problems early.

**Tax reserve:** The calculator sets aside the % you specify from income each week into an imaginary "tax account." This models the good habit of ring-fencing tax money as it arrives. 25–30% is typical for a GST-registered sole trader.

**Large payments:** Use these fields for known one-off outgoings — an IRD provisional tax instalment, vehicle registration, annual insurance premium, or a large materials order.

### Warning Signs to Watch

- **Negative balance weeks** — you'll need overdraft, a credit card, or to bring forward an invoice
- **Closing balance below 1 month expenses** — insufficient buffer for unexpected delays
- **Tax reserve lower than expected IRD bill** — increase the reserve % immediately

### Building a Cash Buffer

Aim for a minimum **4-week buffer** in your business account (4 × total weekly expenses). This absorbs a bad week, a slow client, or an unexpected cost without causing a crisis.

Use our [Job Cost Calculator](/calculators/job-cost-calculator) to check whether individual jobs are contributing enough margin to fund this buffer.
