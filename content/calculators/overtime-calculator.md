---
title: "Overtime & Holiday Pay Calculator — NZ"
description: "Calculate overtime pay, time-and-a-half, double time, and public holiday rates for NZ employees and contractors."
tags: [overtime, holiday pay, wages, calculator, NZ, employment]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchOTTab('ot')">Overtime Pay</button>
    <button class="calc-tab" onclick="switchOTTab('ph')">Public Holidays</button>
    <button class="calc-tab" onclick="switchOTTab('al')">Annual Leave</button>
  </div>
  <div id="ottab-ot">
    <div class="calc-grid">
      <div class="calc-group"><label>Base hourly rate ($)</label><input type="number" id="ot-rate" placeholder="e.g. 28" oninput="calcOT()"></div>
      <div class="calc-group"><label>Standard hours worked</label><input type="number" id="ot-std" placeholder="e.g. 40" oninput="calcOT()"></div>
      <div class="calc-group"><label>Overtime hours (1.5x)</label><input type="number" id="ot-1h" placeholder="e.g. 4" value="0" oninput="calcOT()"></div>
      <div class="calc-group"><label>Double time hours (2x)</label><input type="number" id="ot-2h" placeholder="e.g. 0" value="0" oninput="calcOT()"></div>
      <div class="calc-group"><label>KiwiSaver (employer %)</label><input type="number" id="ot-ks" placeholder="3" value="3" oninput="calcOT()"></div>
    </div>
    <div class="calc-result" id="ot-result" style="display:none">
      <h3>Weekly Pay Breakdown</h3>
      <div class="result-row"><span>Standard pay</span><span id="ot-std-pay"></span></div>
      <div class="result-row"><span>Overtime (1.5x)</span><span id="ot-ot-pay"></span></div>
      <div class="result-row"><span>Double time (2x)</span><span id="ot-dt-pay"></span></div>
      <div class="result-row"><span>Gross weekly total</span><span id="ot-gross" class="result-highlight"></span></div>
      <div class="result-row"><span>Employer KiwiSaver</span><span id="ot-ks-out"></span></div>
      <div class="result-row"><span>Total cost to employer</span><span id="ot-employer"></span></div>
    </div>
  </div>
  <div id="ottab-ph" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Hourly rate ($)</label><input type="number" id="ph-rate" placeholder="e.g. 28" oninput="calcPH()"></div>
      <div class="calc-group"><label>Hours worked on public holiday</label><input type="number" id="ph-hrs" placeholder="e.g. 8" oninput="calcPH()"></div>
      <div class="calc-group"><label>Was it an otherwise working day?</label>
        <select id="ph-owd" onchange="calcPH()">
          <option value="1" selected>Yes</option>
          <option value="0">No</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="ph-result" style="display:none">
      <h3>Public Holiday Pay</h3>
      <div class="result-row"><span>Time-and-a-half payment</span><span id="ph-pay"></span></div>
      <div class="result-row"><span>TOIL day entitled</span><span id="ph-toil"></span></div>
      <div class="result-row"><span>Total entitlement</span><span id="ph-total" class="result-highlight"></span></div>
    </div>
  </div>
  <div id="ottab-al" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Annual salary or weekly rate ($)</label><input type="number" id="al-wage" placeholder="e.g. 65000" oninput="calcAL()"></div>
      <div class="calc-group"><label>Wage type</label>
        <select id="al-type" onchange="calcAL()">
          <option value="annual" selected>Annual salary</option>
          <option value="weekly">Weekly wage</option>
        </select>
      </div>
      <div class="calc-group"><label>Weeks leave to calculate</label><input type="number" id="al-wks" placeholder="e.g. 4" value="4" oninput="calcAL()"></div>
    </div>
    <div class="calc-result" id="al-result" style="display:none">
      <h3>Annual Leave Pay</h3>
      <div class="result-row"><span>Weekly rate</span><span id="al-wrate"></span></div>
      <div class="result-row"><span>Annual leave entitlement (4 weeks)</span><span id="al-ent"></span></div>
      <div class="result-row"><span>Leave pay for selected weeks</span><span id="al-pay" class="result-highlight"></span></div>
      <div class="result-row"><span>8% of gross earnings check</span><span id="al-pct"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function switchOTTab(t){
    ['ot','ph','al'].forEach(function(id){document.getElementById('ottab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['ot','ph','al'][i]===t);});
  }
  function calcOT(){
    var r=parseFloat(document.getElementById('ot-rate').value)||0;
    var std=parseFloat(document.getElementById('ot-std').value)||0;
    var ot=parseFloat(document.getElementById('ot-1h').value)||0;
    var dt=parseFloat(document.getElementById('ot-2h').value)||0;
    var ks=parseFloat(document.getElementById('ot-ks').value)||3;
    if(!r||!std){document.getElementById('ot-result').style.display='none';return;}
    var stdPay=r*std;
    var otPay=r*1.5*ot;
    var dtPay=r*2*dt;
    var gross=stdPay+otPay+dtPay;
    var ksCost=gross*ks/100;
    document.getElementById('ot-std-pay').textContent=nzd(stdPay);
    document.getElementById('ot-ot-pay').textContent=nzd(otPay)+(ot?'  ('+ot+'hrs × $'+nzd(r*1.5)+')':'');
    document.getElementById('ot-dt-pay').textContent=nzd(dtPay)+(dt?'  ('+dt+'hrs × $'+nzd(r*2)+')':'');
    document.getElementById('ot-gross').textContent=nzd(gross);
    document.getElementById('ot-ks-out').textContent=nzd(ksCost)+' ('+ks+'%)';
    document.getElementById('ot-employer').textContent=nzd(gross+ksCost);
    document.getElementById('ot-result').style.display='';
  }
  function calcPH(){
    var r=parseFloat(document.getElementById('ph-rate').value)||0;
    var hrs=parseFloat(document.getElementById('ph-hrs').value)||0;
    var owd=parseInt(document.getElementById('ph-owd').value);
    if(!r||!hrs){document.getElementById('ph-result').style.display='none';return;}
    var pay=r*1.5*hrs;
    document.getElementById('ph-pay').textContent=nzd(pay);
    document.getElementById('ph-toil').textContent=owd?'Yes — entitled to 1 extra day off':'Not entitled (not an otherwise working day)';
    document.getElementById('ph-total').textContent=nzd(pay)+(owd?' + 1 day TOIL':'');
    document.getElementById('ph-result').style.display='';
  }
  function calcAL(){
    var wage=parseFloat(document.getElementById('al-wage').value)||0;
    var type=document.getElementById('al-type').value;
    var wks=parseFloat(document.getElementById('al-wks').value)||4;
    if(!wage){document.getElementById('al-result').style.display='none';return;}
    var weekly=type==='annual'?wage/52:wage;
    var annual=weekly*4;
    var pay=weekly*wks;
    var pct=wage*(type==='annual'?1:52)*0.08;
    document.getElementById('al-wrate').textContent=nzd(weekly)+'/week';
    document.getElementById('al-ent').textContent=nzd(annual);
    document.getElementById('al-pay').textContent=nzd(pay);
    document.getElementById('al-pct').textContent=nzd(pct)+'/yr (higher of weekly rate or 8% applies)';
    document.getElementById('al-result').style.display='';
  }
  </script>
---

## NZ Employment Pay Rules for Tradies

### Overtime

The **Employment Relations Act 2000** doesn't mandate specific overtime rates — it depends on your employment agreement. However, industry standard for NZ tradies is:
- **Time-and-a-half (1.5x)** after 40 hours/week or outside agreed hours
- **Double time (2x)** for Sundays or agreed public holiday rates

### Public Holidays

Under the **Holidays Act 2003**, employees who work on a [public holiday](https://www.employment.govt.nz/leave-and-holidays/public-holidays/) are entitled to:
- **Time-and-a-half** pay for hours worked
- **An alternative holiday** (TOIL day) if it was an *otherwise working day*

NZ has **12 public holidays** per year including Waitangi Day, ANZAC Day, Christmas, Easter, and regional Anniversary Days.

### Annual Leave

All NZ employees are entitled to **at least 4 weeks** paid annual leave after 12 months. Pay is the **greater of**:
- Their ordinary weekly rate × 4 weeks, or
- 8% of gross annual earnings

Use our [PAYE Employee Cost Calculator](/calculators/paye-employee-calculator.html) to see total cost to employer.
