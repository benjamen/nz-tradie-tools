---
title: "NZ GST Calculator"
description: "Add or remove 15% GST instantly. Works for any NZ tradie invoice or quote."
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
