---
title: "NZ Holiday Pay Calculator — Holidays Act 2003"
description: "Calculate correct annual leave payouts for NZ employees using the Holidays Act 2003 — greater of ordinary weekly pay or average weekly earnings."
tags: [holiday pay, annual leave, Holidays Act, employment, NZ]
author: "NZ Tradie Tools"
related_articles: [hiring-an-apprentice-nz-tradie-guide-2026, minimum-wage-increase-april-2026-tradie-costs, employee-total-cost-calculator]
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchHP('annual')">Annual Leave</button>
    <button class="calc-tab" onclick="switchHP('casual')">Casual / Termination Pay</button>
  </div>
  <div id="hp-annual">
    <div class="calc-grid">
      <div class="calc-group">
        <label>Ordinary weekly pay (regular weekly wage) — $</label>
        <input type="number" id="hp-owp" placeholder="e.g. 1250" oninput="calcHP()">
      </div>
      <div class="calc-group">
        <label>Total gross earnings last 12 months — $</label>
        <input type="number" id="hp-annual-gross" placeholder="e.g. 68000" oninput="calcHP()">
        <small>Include overtime, allowances, and bonuses that are regular and expected.</small>
      </div>
      <div class="calc-group">
        <label>Weeks of leave being paid</label>
        <input type="number" id="hp-weeks" value="4" min="1" max="52" oninput="calcHP()">
      </div>
    </div>
    <div class="calc-result" id="hp-annual-result" style="display:none">
      <h3>Annual Leave Payment</h3>
      <div class="result-row"><span>Ordinary weekly pay (OWP)</span><span id="hp-r-owp"></span></div>
      <div class="result-row"><span>Average weekly earnings (AWE over 12 months)</span><span id="hp-r-awe"></span></div>
      <div class="result-row"><span>Applicable rate (greater of OWP or AWE)</span><span id="hp-r-rate" style="font-weight:700;color:#0055a5"></span></div>
      <div class="result-row" style="font-weight:700;border-top:2px solid #0055a5;padding-top:.5rem"><span>Total leave payment</span><span id="hp-r-total"></span></div>
      <div style="margin-top:.75rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem" id="hp-r-note"></div>
    </div>
  </div>
  <div id="hp-casual" style="display:none">
    <div class="calc-grid">
      <div class="calc-group" style="grid-column:1/-1">
        <label>Total gross earnings for the period — $</label>
        <input type="number" id="hp-casual-gross" placeholder="e.g. 25000" oninput="calcHPCasual()">
        <small>Casual employees accrue annual leave at 8% of gross earnings.</small>
      </div>
    </div>
    <div class="calc-result" id="hp-casual-result" style="display:none">
      <h3>Casual / Termination Leave Entitlement</h3>
      <div class="result-row"><span>Gross earnings</span><span id="hpc-r-gross"></span></div>
      <div class="result-row"><span>Annual leave entitlement (8%)</span><span id="hpc-r-leave" style="font-weight:700"></span></div>
    </div>
  </div>
  <script>
  function fmt(n){return "$"+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,",");}
  function switchHP(m){
    document.querySelectorAll(".calc-tab").forEach(function(b,i){b.classList.toggle("active",i===(m==="annual"?0:1));});
    document.getElementById("hp-annual").style.display=m==="annual"?"":"none";
    document.getElementById("hp-casual").style.display=m==="casual"?"":"none";
  }
  function calcHP(){
    var owp=parseFloat(document.getElementById("hp-owp").value)||0;
    var gross=parseFloat(document.getElementById("hp-annual-gross").value)||0;
    var weeks=parseFloat(document.getElementById("hp-weeks").value)||4;
    var r=document.getElementById("hp-annual-result");
    if(!owp||!gross){r.style.display="none";return;}
    var awe=gross/52;
    var rate=Math.max(owp,awe);
    var total=rate*weeks;
    var useAWE=awe>owp;
    document.getElementById("hp-r-owp").textContent=fmt(owp)+"/wk";
    document.getElementById("hp-r-awe").textContent=fmt(awe)+"/wk";
    document.getElementById("hp-r-rate").textContent=fmt(rate)+"/wk ("+(useAWE?"AWE applies":"OWP applies")+")";
    document.getElementById("hp-r-total").textContent=fmt(total);
    document.getElementById("hp-r-note").innerHTML=useAWE
      ?"<strong>AWE applies:</strong> The employee's average weekly earnings ($"+fmt(awe)+") exceed their ordinary weekly pay ($"+fmt(owp)+"). Use the AWE rate. This often happens when an employee has worked significant overtime."
      :"<strong>OWP applies:</strong> The ordinary weekly pay ($"+fmt(owp)+") equals or exceeds the average weekly earnings ($"+fmt(awe)+"). Use the OWP rate.";
    r.style.display="";
  }
  function calcHPCasual(){
    var gross=parseFloat(document.getElementById("hp-casual-gross").value)||0;
    var r=document.getElementById("hp-casual-result");
    if(!gross){r.style.display="none";return;}
    document.getElementById("hpc-r-gross").textContent="$"+gross.toLocaleString("en-NZ");
    document.getElementById("hpc-r-leave").textContent=fmt(gross*0.08);
    r.style.display="";
  }
  </script>
---

## Holiday Pay Under the Holidays Act 2003

The Holidays Act 2003 is one of the most misunderstood pieces of employment law in NZ. Even large companies have been caught underpaying, resulting in millions in back-pay obligations.

### The Golden Rule

Annual leave must be paid at the **greater of**:
1. **Ordinary Weekly Pay (OWP)** — what the employee normally earns in a week, including regular allowances
2. **Average Weekly Earnings (AWE)** — total gross earnings over the last 52 weeks ÷ 52

This means that if an employee has worked significant overtime during the year, their leave rate must reflect that — not just their base wage.

### What's Included in Gross Earnings (for AWE)

- Regular wages and salary
- Regular overtime (if it's a consistent pattern)
- Allowances that are regular and expected
- Commission if it's part of regular remuneration

**Excluded:** genuine one-off bonuses, reimbursements, penal rates for truly occasional overtime.

### Casual Employees

Casual employees (no guaranteed hours) accrue leave differently:
- They earn **8% of gross earnings** as annual leave loading, typically included in each pay
- If 8% is included in hourly rate, it must be shown separately on payslips

### The Risk of Getting It Wrong

Underpaying leave is a breach of the Employment Relations Act. MBIE can audit any employer, and back-pay must be paid with interest. Use [Employment NZ's tools](https://www.employment.govt.nz/leave-and-holidays/annual-holidays/) to verify your calculations.
