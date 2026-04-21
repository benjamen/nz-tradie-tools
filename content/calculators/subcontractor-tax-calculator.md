---
title: "Subcontractor Tax & GST Calculator — NZ"
description: "Calculate GST, income tax, and net earnings for NZ subcontractors and self-employed tradies."
tags: [subcontractor, GST, tax, calculator, NZ, self-employed]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchSTTab('gst')">GST &amp; Take-Home</button>
    <button class="calc-tab" onclick="switchSTTab('tax')">Income Tax</button>
    <button class="calc-tab" onclick="switchSTTab('prov')">Provisional Tax</button>
  </div>
  <div id="sttab-gst">
    <div class="calc-grid">
      <div class="calc-group"><label>Invoice amount (incl. GST) ($)</label><input type="number" id="sg-inv" placeholder="e.g. 5750" oninput="calcSubGST()"></div>
      <div class="calc-group"><label>Expenses (excl. GST) ($)</label><input type="number" id="sg-exp" placeholder="e.g. 1800" oninput="calcSubGST()"></div>
      <div class="calc-group"><label>GST on expenses ($)</label><input type="number" id="sg-gstexp" placeholder="e.g. 270" oninput="calcSubGST()"></div>
    </div>
    <div class="calc-result" id="sg-result" style="display:none">
      <h3>GST Breakdown</h3>
      <div class="result-row"><span>Invoice excl. GST</span><span id="sg-excl"></span></div>
      <div class="result-row"><span>GST collected (15%)</span><span id="sg-gstcol"></span></div>
      <div class="result-row"><span>GST on expenses (input tax)</span><span id="sg-input"></span></div>
      <div class="result-row"><span>GST to pay IRD</span><span id="sg-pay" class="result-highlight"></span></div>
      <div class="result-row"><span>Net income (before income tax)</span><span id="sg-net"></span></div>
    </div>
  </div>
  <div id="sttab-tax" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Annual net taxable income ($)</label><input type="number" id="tx-inc" placeholder="e.g. 75000" oninput="calcTax()"></div>
      <div class="calc-group"><label>Student loan?</label>
        <select id="tx-sl" onchange="calcTax()">
          <option value="0" selected>No</option>
          <option value="1">Yes</option>
        </select>
      </div>
      <div class="calc-group"><label>KiwiSaver (voluntary %)</label>
        <select id="tx-ks" onchange="calcTax()">
          <option value="0" selected>Not enrolled</option>
          <option value="3">3%</option>
          <option value="4">4%</option>
          <option value="6">6%</option>
          <option value="8">8%</option>
          <option value="10">10%</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="tx-result" style="display:none">
      <h3>Income Tax (2025)</h3>
      <div class="result-row"><span>Taxable income</span><span id="tx-gross"></span></div>
      <div class="result-row"><span>Income tax (PAYE equivalent)</span><span id="tx-paye"></span></div>
      <div class="result-row"><span>ACC earner levy</span><span id="tx-acc"></span></div>
      <div class="result-row"><span>Student loan repayment</span><span id="tx-sl-out"></span></div>
      <div class="result-row"><span>KiwiSaver (self)</span><span id="tx-ks-out"></span></div>
      <div class="result-row"><span>Net take-home (annual)</span><span id="tx-net" class="result-highlight"></span></div>
      <div class="result-row"><span>Net take-home (weekly)</span><span id="tx-wk"></span></div>
      <div class="result-row"><span>Set aside for tax</span><span id="tx-set"></span></div>
    </div>
  </div>
  <div id="sttab-prov" style="display:none">
    <p style="font-size:.85rem;color:#555;margin-bottom:1rem">Provisional tax — paid in 3 instalments for self-employed NZers. Based on last year's residual income tax (RIT).</p>
    <div class="calc-grid">
      <div class="calc-group"><label>Last year's income tax ($)</label><input type="number" id="pv-last" placeholder="e.g. 12000" oninput="calcProv()"></div>
      <div class="calc-group"><label>Uplift method</label>
        <select id="pv-meth" onchange="calcProv()">
          <option value="1.05" selected>Standard (105% of prior year)</option>
          <option value="1.10">Estimation method (110% — use if income rising)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="pv-result" style="display:none">
      <h3>Provisional Tax Instalments</h3>
      <div class="result-row"><span>Annual provisional tax</span><span id="pv-annual"></span></div>
      <div class="result-row"><span>Instalment 1 (Aug 28)</span><span id="pv-i1" class="result-highlight"></span></div>
      <div class="result-row"><span>Instalment 2 (Jan 15)</span><span id="pv-i2" class="result-highlight"></span></div>
      <div class="result-row"><span>Instalment 3 (May 7)</span><span id="pv-i3" class="result-highlight"></span></div>
      <div class="result-row"><span>Monthly set-aside</span><span id="pv-mon"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchSTTab(t){
    ['gst','tax','prov'].forEach(function(id){document.getElementById('sttab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['gst','tax','prov'][i]===t);});
  }
  function calcSubGST(){
    var inv=parseFloat(document.getElementById('sg-inv').value)||0;
    var exp=parseFloat(document.getElementById('sg-exp').value)||0;
    var gstexp=parseFloat(document.getElementById('sg-gstexp').value)||0;
    if(!inv){document.getElementById('sg-result').style.display='none';return;}
    var excl=inv/1.15;
    var gstcol=inv-excl;
    var gstpay=gstcol-gstexp;
    var net=excl-exp;
    document.getElementById('sg-excl').textContent=nzd(excl);
    document.getElementById('sg-gstcol').textContent=nzd(gstcol);
    document.getElementById('sg-input').textContent=nzd(gstexp);
    document.getElementById('sg-pay').textContent=nzd(gstpay);
    document.getElementById('sg-net').textContent=nzd(net);
    document.getElementById('sg-result').style.display='';
  }
  function calcTax(){
    var inc=parseFloat(document.getElementById('tx-inc').value)||0;
    var sl=parseInt(document.getElementById('tx-sl').value);
    var ks=parseFloat(document.getElementById('tx-ks').value)/100;
    if(!inc){document.getElementById('tx-result').style.display='none';return;}
    var tax=0;
    if(inc<=14000)tax=inc*0.105;
    else if(inc<=48000)tax=1470+(inc-14000)*0.175;
    else if(inc<=70000)tax=7420+(inc-70000*0+inc-48000)*0.30-1;
    if(inc>48000&&inc<=70000)tax=7420+(inc-48000)*0.30;
    if(inc>70000&&inc<=180000)tax=14020+(inc-70000)*0.33;
    if(inc>180000)tax=50320+(inc-180000)*0.39;
    var acc=Math.min(inc,142283)*0.016;
    var slpay=sl?Math.max(0,(inc-22828)*0.12):0;
    var kspay=inc*ks;
    var net=inc-tax-acc-slpay-kspay;
    var setaside=(tax+acc)/inc*100;
    document.getElementById('tx-gross').textContent=nzd(inc);
    document.getElementById('tx-paye').textContent=nzd(tax);
    document.getElementById('tx-acc').textContent=nzd(acc);
    document.getElementById('tx-sl-out').textContent=sl?nzd(slpay):'N/A';
    document.getElementById('tx-ks-out').textContent=ks?nzd(kspay):'Not enrolled';
    document.getElementById('tx-net').textContent=nzd(net);
    document.getElementById('tx-wk').textContent=nzd(net/52)+'/week';
    document.getElementById('tx-set').textContent=setaside.toFixed(1)+'% of earnings ('+nzd((tax+acc)/12)+'/month)';
    document.getElementById('tx-result').style.display='';
  }
  function calcProv(){
    var last=parseFloat(document.getElementById('pv-last').value)||0;
    var meth=parseFloat(document.getElementById('pv-meth').value);
    if(!last){document.getElementById('pv-result').style.display='none';return;}
    var annual=last*meth;
    var inst=annual/3;
    document.getElementById('pv-annual').textContent=nzd(annual);
    document.getElementById('pv-i1').textContent=nzd(inst);
    document.getElementById('pv-i2').textContent=nzd(inst);
    document.getElementById('pv-i3').textContent=nzd(inst);
    document.getElementById('pv-mon').textContent=nzd(annual/12)+'/month';
    document.getElementById('pv-result').style.display='';
  }
  </script>
---

## Tax for NZ Subcontractors

### GST Registration

You **must register for GST** if your turnover exceeds **$60,000 in any 12-month period**. Most tradies earning a full-time income will be over this threshold. You can register voluntarily below this threshold.

**GST basics:**
- Charge 15% on all invoices
- Claim back 15% (input tax) on business expenses
- File GST returns every 1 or 2 months, or 6 months (if under $500k/yr)

### Tax Rates (NZ 2025)

| Income | Rate |
|---|---|
| $0 – $14,000 | 10.5% |
| $14,001 – $48,000 | 17.5% |
| $48,001 – $70,000 | 30% |
| $70,001 – $180,000 | 33% |
| $180,001+ | 39% |

### Set Aside Rule

As a self-employed tradie, **set aside 25–30% of every payment** for tax and GST. The biggest mistake new tradies make is spending their GST component before the filing date.

### Provisional Tax

If you owe more than **$5,000 residual income tax** in any year, you must pay provisional tax the following year. The standard method is 105% of the previous year's tax, paid in 3 instalments.

See our [GST Calculator](/calculators/gst-calculator.html) for quick invoice calculations.
