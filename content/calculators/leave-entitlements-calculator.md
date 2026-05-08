---
title: "NZ Leave Entitlements Calculator — Annual Leave, Sick Leave & Public Holidays"
description: "Calculate the full value of statutory leave entitlements for NZ employees — annual leave, sick leave, public holidays, and bereavement leave."
tags: [leave, annual leave, sick leave, employment, holidays, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchLVTab('annual')">Annual Leave</button>
    <button class="calc-tab" onclick="switchLVTab('sick')">Sick Leave</button>
    <button class="calc-tab" onclick="switchLVTab('summary')">Full Summary</button>
  </div>

  <div id="lvtab-annual">
    <div class="calc-grid">
      <div class="calc-group">
        <label>Wage type</label>
        <select id="lv-type" onchange="calcLV()">
          <option value="hourly">Hourly rate</option>
          <option value="annual">Annual salary</option>
          <option value="weekly">Weekly wage</option>
        </select>
      </div>
      <div class="calc-group"><label>Rate / salary ($)</label><input type="number" id="lv-rate" placeholder="e.g. 30" oninput="calcLV()"></div>
      <div class="calc-group"><label>Hours per week (if hourly)</label><input type="number" id="lv-hrs" placeholder="e.g. 40" value="40" oninput="calcLV()"></div>
    </div>
    <div class="calc-result" id="lv-annual-result" style="display:none">
      <h3>Annual Leave (Holidays Act 2003)</h3>
      <div class="result-row"><span>Weekly wage</span><span id="lv-weekly"></span></div>
      <div class="result-row"><span>Annual gross earnings</span><span id="lv-annual-gross"></span></div>
      <div class="result-row"><span>4 weeks annual leave value</span><span id="lv-al-val" class="result-highlight"></span></div>
      <div class="result-row"><span>8% of annual gross (alternative)</span><span id="lv-8pct"></span></div>
      <div class="result-row"><span>Leave paid at higher of the two</span><span id="lv-higher"></span></div>
      <div class="result-row"><span>Per public holiday (8 hrs)</span><span id="lv-ph-day"></span></div>
      <div class="result-row"><span>12 public holidays value/year</span><span id="lv-ph-total"></span></div>
    </div>
  </div>

  <div id="lvtab-sick" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Hourly rate ($)</label><input type="number" id="sl-rate" placeholder="e.g. 30" oninput="calcSL()"></div>
      <div class="calc-group"><label>Hours per day</label><input type="number" id="sl-hrs" placeholder="e.g. 8" value="8" oninput="calcSL()"></div>
    </div>
    <div class="calc-result" id="lv-sick-result" style="display:none">
      <h3>Sick Leave (Holidays Act 2003)</h3>
      <div class="result-row"><span>Sick leave entitlement</span><span>10 days/year</span></div>
      <div class="result-row"><span>When it starts</span><span>From first day of employment (2021 amendment)</span></div>
      <div class="result-row"><span>Maximum accrual</span><span>20 days (if not taken)</span></div>
      <div class="result-row"><span>Value per sick day</span><span id="sl-day-val"></span></div>
      <div class="result-row"><span>10 days annual value</span><span id="sl-annual-val" class="result-highlight"></span></div>
      <div class="result-row"><span>Bereavement leave (close family)</span><span>3 days paid</span></div>
      <div class="result-row"><span>Bereavement leave (other)</span><span>1 day paid</span></div>
      <div class="result-row"><span>Domestic violence leave</span><span>10 days paid/year</span></div>
    </div>
  </div>

  <div id="lvtab-summary" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Hourly rate ($)</label><input type="number" id="sum-rate" placeholder="e.g. 30" oninput="calcSUM()"></div>
      <div class="calc-group"><label>Hours per week</label><input type="number" id="sum-hrs" placeholder="e.g. 40" value="40" oninput="calcSUM()"></div>
    </div>
    <div class="calc-result" id="lv-sum-result" style="display:none">
      <h3>Total Annual Leave Cost to Employer</h3>
      <div class="result-row"><span>Annual leave (4 weeks)</span><span id="sum-al"></span></div>
      <div class="result-row"><span>Public holidays (12 days)</span><span id="sum-ph"></span></div>
      <div class="result-row"><span>Sick leave provision (10 days)</span><span id="sum-sl"></span></div>
      <div class="result-row"><span>Total leave value/year</span><span id="sum-total" class="result-highlight"></span></div>
      <div class="result-row"><span>As % of base wages</span><span id="sum-pct"></span></div>
      <div style="margin-top:.75rem;padding:.6rem;background:#e8f4fd;border-radius:4px;font-size:.85rem">
        Leave adds approximately <strong id="sum-adder"></strong> to the true cost of employment. Factor this into your labour rates and job pricing.
      </div>
    </div>
  </div>

  <script>
  function nzd(n){return '$'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
  function switchLVTab(t){
    ['annual','sick','summary'].forEach(function(id){document.getElementById('lvtab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['annual','sick','summary'][i]===t);});
  }
  function calcLV(){
    var type=document.getElementById('lv-type').value;
    var rate=parseFloat(document.getElementById('lv-rate').value)||0;
    var hrs=parseFloat(document.getElementById('lv-hrs').value)||40;
    if(!rate){document.getElementById('lv-annual-result').style.display='none';return;}
    var weekly = type==='hourly' ? rate*hrs : type==='annual' ? rate/52 : rate;
    var annual = weekly*52;
    var alVal = weekly*4;
    var pct8 = annual*0.08;
    var higher = Math.max(alVal,pct8);
    var phDay = (type==='hourly'?rate:weekly/hrs||0)*8;
    var phTotal = phDay*12;
    document.getElementById('lv-weekly').textContent=nzd(weekly)+'/week';
    document.getElementById('lv-annual-gross').textContent=nzd(annual)+'/year';
    document.getElementById('lv-al-val').textContent=nzd(alVal);
    document.getElementById('lv-8pct').textContent=nzd(pct8);
    document.getElementById('lv-higher').textContent=nzd(higher);
    document.getElementById('lv-ph-day').textContent=nzd(phDay);
    document.getElementById('lv-ph-total').textContent=nzd(phTotal);
    document.getElementById('lv-annual-result').style.display='';
  }
  function calcSL(){
    var r=parseFloat(document.getElementById('sl-rate').value)||0;
    var h=parseFloat(document.getElementById('sl-hrs').value)||8;
    if(!r){document.getElementById('lv-sick-result').style.display='none';return;}
    var dayVal=r*h;
    document.getElementById('sl-day-val').textContent=nzd(dayVal);
    document.getElementById('sl-annual-val').textContent=nzd(dayVal*10);
    document.getElementById('lv-sick-result').style.display='';
  }
  function calcSUM(){
    var r=parseFloat(document.getElementById('sum-rate').value)||0;
    var h=parseFloat(document.getElementById('sum-hrs').value)||40;
    if(!r){document.getElementById('lv-sum-result').style.display='none';return;}
    var weekly=r*h;
    var annual=weekly*52;
    var al=weekly*4;
    var ph=r*8*12;
    var sl=r*8*10;
    var total=al+ph+sl;
    var pct=total/annual*100;
    document.getElementById('sum-al').textContent=nzd(al);
    document.getElementById('sum-ph').textContent=nzd(ph);
    document.getElementById('sum-sl').textContent=nzd(sl);
    document.getElementById('sum-total').textContent=nzd(total);
    document.getElementById('sum-pct').textContent=pct.toFixed(1)+'% of base wages';
    document.getElementById('sum-adder').textContent=pct.toFixed(0)+'%';
    document.getElementById('lv-sum-result').style.display='';
  }
  </script>
related_articles: [hiring-an-apprentice-nz-tradie-guide-2026, minimum-wage-increase-april-2026-tradie-costs]
---

## NZ Statutory Leave Entitlements (Holidays Act 2003)

### Annual Leave

All NZ employees are entitled to **at least 4 weeks** paid annual leave after 12 months of continuous employment. Pay is the **greater of**:
- Their **ordinary weekly rate × 4 weeks**, or
- **8% of gross earnings** for the year

This means part-time and irregular-hours workers often benefit from the 8% calculation.

### Sick Leave

Since 2021, employees are entitled to **10 days sick leave per year** from their first day of employment. Up to 20 days can accumulate if not taken.

Sick leave is paid at the employee's ordinary rate for the hours they would have worked.

### Public Holidays

NZ has **12 public holidays** per year. Employees who work on a public holiday receive:
- **Time-and-a-half** for hours worked
- **An alternative holiday** (day off in lieu) if it was an otherwise working day

### Bereavement Leave

- **3 days** paid leave for death of a spouse/partner, parent, child, sibling, grandparent, or in-law
- **1 day** for any other person if the employee has a genuine bereavement

### What This Means for Job Pricing

Leave entitlements add approximately **17–22%** on top of base hourly wages when factored into true employment cost. Use our [Labour Cost Calculator](/calculators/labour-cost-calculator.html) and [PAYE Employee Cost Calculator](/calculators/paye-employee-calculator.html) to see the full picture.
