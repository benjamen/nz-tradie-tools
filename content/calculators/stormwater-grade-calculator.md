---
title: "NZ Stormwater & Wastewater Pipe Grade Calculator"
description: "Calculate minimum pipe fall and check compliance with NZ Building Code E1/E2 and AS/NZS 3500.3 drainage standard for stormwater and foul drainage."
tags: [drainage, stormwater, plumbing, AS/NZS 3500, drainlayers, NZ]
author: "NZ Tradie Tools"
related_articles: [new-plumbing-self-certification-nz, new-lead-free-plumbing-standards-nz, drain-grade-calculator]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>Drain type</label>
      <select id="sg-type" onchange="calcSG()">
        <option value="foul">Foul / wastewater drain</option>
        <option value="storm">Stormwater drain</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Pipe diameter (mm)</label>
      <select id="sg-diameter" onchange="calcSG()">
        <option value="100">100mm</option>
        <option value="150">150mm</option>
        <option value="225">225mm</option>
        <option value="300">300mm</option>
        <option value="375">375mm</option>
        <option value="450">450mm</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Pipe material</label>
      <select id="sg-material" onchange="calcSG()">
        <option value="upvc">uPVC (smooth bore)</option>
        <option value="concrete">Concrete / vitrified clay</option>
        <option value="hdpe">HDPE</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Drain run length (m)</label>
      <input type="number" id="sg-length" placeholder="e.g. 12" oninput="calcSG()">
    </div>
    <div class="calc-group">
      <label>Proposed fall (mm drop over run)</label>
      <input type="number" id="sg-fall" placeholder="e.g. 150" oninput="calcSG()">
    </div>
  </div>
  <div class="calc-result" id="sg-result" style="display:none">
    <h3>Drain Grade Result</h3>
    <div class="result-row"><span>Proposed grade</span><span id="sg-r-grade"></span></div>
    <div class="result-row"><span>AS/NZS 3500 minimum grade</span><span id="sg-r-mingrade"></span></div>
    <div class="result-row"><span>Minimum fall over this run</span><span id="sg-r-minfall"></span></div>
    <div class="result-row"><span>Compliance</span><span id="sg-r-comply"></span></div>
    <div style="margin-top:.75rem;background:#f0f4ff;border-radius:6px;padding:.75rem;font-size:.85rem">
      <strong>Self-cleaning velocity:</strong> Grades steeper than 1:40 achieve self-cleaning velocity in most foul drains. Flat grades below 1:100 risk solids settling and blockages.
    </div>
  </div>
  <script>
  function calcSG(){
    var type=document.getElementById("sg-type").value;
    var dia=parseInt(document.getElementById("sg-diameter").value)||100;
    var mat=document.getElementById("sg-material").value;
    var len=parseFloat(document.getElementById("sg-length").value)||0;
    var fall=parseFloat(document.getElementById("sg-fall").value)||0;
    var r=document.getElementById("sg-result");
    if(!len||!fall){r.style.display="none";return;}
    var grade=len/fall;
    var minGrade;
    if(type==="foul"){
      if(dia<=100)minGrade=mat==="concrete"?55:50;
      else if(dia<=150)minGrade=mat==="concrete"?80:70;
      else if(dia<=225)minGrade=100;
      else minGrade=150;
    }else{
      if(dia<=100)minGrade=100;
      else if(dia<=150)minGrade=150;
      else if(dia<=225)minGrade=200;
      else minGrade=300;
    }
    var minFall=(len/minGrade*1000).toFixed(0);
    var pass=grade<=minGrade;
    document.getElementById("sg-r-grade").textContent="1:"+grade.toFixed(0)+" ("+((fall/len)*100).toFixed(2)+"%)";
    document.getElementById("sg-r-mingrade").textContent="1:"+minGrade+" (AS/NZS 3500.3)";
    document.getElementById("sg-r-minfall").textContent=minFall+"mm over "+len+"m";
    document.getElementById("sg-r-comply").innerHTML=pass
      ?"<span style="color:#22543d;font-weight:600">✓ Compliant — grade meets minimum</span>"
      :"<span style="color:#c53030;font-weight:600">✗ Too flat — increase fall to "+minFall+"mm minimum</span>";
    r.style.display="";
  }
  </script>
faqs:
  - q: 'What is the minimum grade for a stormwater pipe in NZ?'
    a: 'NZS 3114 and the NZ Building Code require a minimum grade of 1:100 (1%) for 100 mm stormwater pipes. Larger pipes (150 mm+) may use 1:200 in some situations. Upsize the pipe for flat sites to maintain self-cleansing velocity.'
  - q: 'How do I calculate stormwater flow for a roof in NZ?'
    a: 'Rainfall intensity in NZ varies by region. As a guide, Auckland uses 150 mm/hr for a 10-year storm. Flow = area (m²) × intensity (mm/hr) ÷ 3,600. A 200 m² roof in Auckland at 150 mm/hr produces 8.3 L/s — requiring at least 100 mm pipe.'
  - q: 'What pipe material is used for stormwater in NZ?'
    a: 'Common NZ stormwater pipe materials: uPVC (NZS 7643), corrugated HDPE (flexible), or concrete (older/larger systems). uPVC is the standard for residential sub-100 mm drainage; HDPE is used for rural and flexible-layout situations.'
  - q: 'Does stormwater need to be diverted away from foundations in NZ?'
    a: 'Yes. The NZ Building Code Clause E1 requires buildings to be designed and built so that stormwater is managed to protect the building''s structural performance. Surface drainage must direct water away from foundations.'
---

## NZ Drain Grade Standards — AS/NZS 3500.3

Minimum drain grades in NZ are specified in **AS/NZS 3500.3 Plumbing and Drainage — Stormwater Drainage**, which forms part of the NZ Building Code under clause E1 (Surface Water) and E2 (External Moisture).

### Minimum Grades for Foul Drains (Wastewater)

| Pipe size | uPVC minimum grade | Concrete/Clay minimum |
|---|---|---|
| 100mm | 1:50 | 1:55 |
| 150mm | 1:70 | 1:80 |
| 225mm | 1:100 | 1:100 |
| 300mm+ | 1:150 | 1:150 |

### Minimum Grades for Stormwater Drains

Stormwater drains can generally be flatter than foul drains:

| Pipe size | Minimum grade |
|---|---|
| 100mm | 1:100 |
| 150mm | 1:150 |
| 225mm | 1:200 |
| 300mm+ | 1:300 |

### Self-Cleaning Velocity

The minimum grades above are set to achieve **self-cleaning velocity** — typically 0.7 m/s for foul drains. At this flow rate, solids are carried along rather than settling. Drains flatter than the minimum will block repeatedly.

### When Engineering Is Required

Drains that cannot achieve minimum grades due to site constraints may require engineering solutions — pump stations, vacuum drainage, or pressure systems. Always flag this to the client before starting work, as it significantly affects cost.

All drainage work must be performed by a **registered drainlayer** and inspected by the local council before backfilling. Self-certification is being expanded but as of 2026, council inspection is still required for most buried drainage.
