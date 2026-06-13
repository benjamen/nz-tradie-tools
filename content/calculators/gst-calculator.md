---
title: "NZ GST Calculator"
description: "Free NZ GST calculator — add or remove 15% GST instantly on any invoice, quote or expense. Get the GST-exclusive, GST-inclusive and GST amounts in seconds."
tags: [GST, tax, calculator, NZ]
author: "NZ Tradie Tools"
related_articles: [nz-tradie-tax-guide-what-you-can-claim, sole-trader-setup-guide-nz-tradies, how-to-write-a-quote-that-wins-jobs-nz]
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchTab('add')">Add GST</button>
    <button class="calc-tab" onclick="switchTab('remove')">Remove GST</button>
  </div>
  <div id="tab-add">
    <div class="calc-grid">
      <div class="calc-group" style="grid-column:1/-1">
        <label>Amount (ex GST) — $</label>
        <input type="number" id="add-amount" placeholder="e.g. 1000" oninput="calcAdd()">
      </div>
    </div>
    <div class="calc-result" id="add-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Ex-GST amount</span><span id="add-ex"></span></div>
      <div class="result-row"><span>GST (15%)</span><span id="add-gst"></span></div>
      <div class="result-row"><span>Total (inc GST)</span><span id="add-inc"></span></div>
    </div>
  </div>
  <div id="tab-remove" style="display:none">
    <div class="calc-grid">
      <div class="calc-group" style="grid-column:1/-1">
        <label>Amount (inc GST) — $</label>
        <input type="number" id="rem-amount" placeholder="e.g. 1150" oninput="calcRemove()">
      </div>
    </div>
    <div class="calc-result" id="rem-result" style="display:none">
      <h3>Result</h3>
      <div class="result-row"><span>Ex-GST amount</span><span id="rem-ex"></span></div>
      <div class="result-row"><span>GST (15%)</span><span id="rem-gst"></span></div>
      <div class="result-row"><span>Total (inc GST)</span><span id="rem-inc"></span></div>
    </div>
  </div>
  <script>
  function fmt(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function switchTab(t){
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',i===(t==='add'?0:1));});
    document.getElementById('tab-add').style.display=t==='add'?'':'none';
    document.getElementById('tab-remove').style.display=t==='remove'?'':'none';
  }
  function calcAdd(){
    var v=parseFloat(document.getElementById('add-amount').value);
    var r=document.getElementById('add-result');
    if(isNaN(v)||v<0){r.style.display='none';return;}
    var gst=v*0.15,inc=v+gst;
    document.getElementById('add-ex').textContent=fmt(v);
    document.getElementById('add-gst').textContent=fmt(gst);
    document.getElementById('add-inc').textContent=fmt(inc);
    r.style.display='';
  }
  function calcRemove(){
    var v=parseFloat(document.getElementById('rem-amount').value);
    var r=document.getElementById('rem-result');
    if(isNaN(v)||v<0){r.style.display='none';return;}
    var ex=v/1.15,gst=v-ex;
    document.getElementById('rem-ex').textContent=fmt(ex);
    document.getElementById('rem-gst').textContent=fmt(gst);
    document.getElementById('rem-inc').textContent=fmt(v);
    r.style.display='';
  }
  </script>
faqs:
  - q: 'What is the GST rate in New Zealand?'
    a: 'GST in New Zealand is 15%, applied to most goods and services. It was increased from 12.5% to 15% in October 2010.'
  - q: 'How do I add GST to a price in NZ?'
    a: 'Multiply the GST-exclusive price by 1.15. For example, $500 + GST = $500 × 1.15 = $575. To find the GST amount only: $500 × 0.15 = $75.'
  - q: 'How do I remove GST from a price in NZ?'
    a: 'Divide the GST-inclusive price by 1.15. For example, $575 ÷ 1.15 = $500 (GST-exclusive). The GST component is $575 − $500 = $75, or equivalently $575 × 3/23 = $75.'
  - q: 'When do I need to register for GST in NZ?'
    a: 'You must register for GST if your turnover exceeds (or will exceed) $60,000 in any 12-month period. You can register voluntarily below this threshold. Most tradie businesses should register once they start earning consistently.'
  - q: 'How often do I file a GST return in NZ?'
    a: 'Most small businesses file GST returns every 2 months (bi-monthly). Businesses with turnover under $500,000 can apply for 6-monthly filing. Large businesses (turnover over $24 million) file monthly.'
---

## How GST Works for NZ Tradies

New Zealand's Goods and Services Tax (GST) is a flat 15% added to most goods and services. If your business earns more than $60,000 in a 12-month period, you must register for GST with Inland Revenue (IRD).

### Key GST Rules for Tradies

- **GST registration threshold:** $60,000 turnover in any 12-month period
- **GST rate:** 15% flat (no reduced or zero rates for standard tradie work)
- **Filing frequency:** Monthly, two-monthly, or six-monthly depending on turnover
- **Tax invoices required** for any sale over $50 to a GST-registered customer

### What to Include on a GST Invoice

Your tax invoice must show:
- The words "tax invoice" clearly
- Your name and GST registration number
- Date of supply
- Description of goods or services
- Amount ex-GST, GST charged, and total inc-GST

### Common GST Mistakes Tradies Make

1. **Forgetting to add GST to quotes** — always quote ex-GST and show GST separately
2. **Claiming GST on private expenses** — you can only claim GST on business purchases
3. **Missing the registration threshold** — IRD can back-date your registration and send a bill

Use [Xero](https://www.xero.com/nz/) or [MYOB](https://www.myob.com/nz/) to automate GST filing and avoid errors.
