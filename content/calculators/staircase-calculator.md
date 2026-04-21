---
title: "Staircase Calculator — NZ (Rise, Run & Dimensions)"
description: "Calculate staircase dimensions for NZ Building Code compliance — number of steps, rise, going, and total run."
tags: [staircase, stairs, calculator, NZ, building code]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Floor-to-floor height (mm)</label><input type="number" id="st-h" placeholder="e.g. 2700" oninput="calcStair()"></div>
    <div class="calc-group"><label>Preferred rise per step (mm)</label><input type="number" id="st-r" placeholder="e.g. 175" value="175" oninput="calcStair()"></div>
    <div class="calc-group"><label>Going (tread depth, mm)</label><input type="number" id="st-g" placeholder="e.g. 255" value="255" oninput="calcStair()"></div>
    <div class="calc-group"><label>Stair width (mm)</label><input type="number" id="st-w" placeholder="e.g. 900" value="900" oninput="calcStair()"></div>
    <div class="calc-group"><label>Timber type</label>
      <select id="st-mat" onchange="calcStair()">
        <option value="180" selected>Pine (treated)</option>
        <option value="320">Rimu / matai</option>
        <option value="420">Oak / engineered hardwood</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="st-result" style="display:none">
    <h3>Staircase Dimensions</h3>
    <div class="result-row"><span>Number of risers</span><span id="st-nris"></span></div>
    <div class="result-row"><span>Actual rise per step</span><span id="st-arise"></span></div>
    <div class="result-row"><span>Total run (horizontal)</span><span id="st-run"></span></div>
    <div class="result-row"><span>Pitch angle</span><span id="st-pitch"></span></div>
    <div class="result-row"><span id="st-code-label">NZ Building Code (2R+G check)</span><span id="st-code"></span></div>
    <div class="result-row"><span>Stringer length</span><span id="st-string"></span></div>
    <div class="result-row"><span>Treads required</span><span id="st-treads"></span></div>
    <div class="result-row"><span>Estimated material cost</span><span id="st-mat-cost" class="result-highlight"></span></div>
  </div>
  <div id="st-warn" style="display:none;background:#fff3cd;border:1px solid #ffc107;padding:.75rem 1rem;margin-top:.75rem;font-size:.88rem;border-radius:4px"></div>
  <script>
  function calcStair(){
    var h=parseFloat(document.getElementById('st-h').value)||0;
    var r=parseFloat(document.getElementById('st-r').value)||175;
    var g=parseFloat(document.getElementById('st-g').value)||255;
    var w=parseFloat(document.getElementById('st-w').value)||900;
    var matPpm=parseFloat(document.getElementById('st-mat').value);
    if(!h){document.getElementById('st-result').style.display='none';return;}
    var nRis=Math.round(h/r);
    var aRise=h/nRis;
    var nTreads=nRis-1;
    var totalRun=nTreads*g;
    var pitch=Math.atan(h/totalRun)*180/Math.PI;
    var stringLen=Math.sqrt(h*h+totalRun*totalRun)/1000;
    var rg2=2*aRise+g;
    var codeOk=aRise>=150&&aRise<=220&&g>=220&&g<=355&&rg2>=550&&rg2<=700;
    var warns=[];
    if(aRise<150||aRise>220)warns.push('Rise '+aRise.toFixed(1)+'mm is outside NZ code range (150–220mm)');
    if(g<220||g>355)warns.push('Going '+g+'mm is outside NZ code range (220–355mm)');
    if(rg2<550||rg2>700)warns.push('2R+G='+rg2.toFixed(0)+' is outside NZ comfort range (550–700mm)');
    var matCost=nTreads*(w/1000*0.6*matPpm)+stringLen*2*matPpm*0.05*2;
    document.getElementById('st-nris').textContent=nRis+' risers ('+nTreads+' treads)';
    document.getElementById('st-arise').textContent=aRise.toFixed(1)+' mm';
    document.getElementById('st-run').textContent=(totalRun/1000).toFixed(2)+' m ('+totalRun+' mm)';
    document.getElementById('st-pitch').textContent=pitch.toFixed(1)+'°';
    document.getElementById('st-code').textContent=(codeOk?'✓ Compliant':'✗ Non-compliant')+' (2R+G = '+rg2.toFixed(0)+'mm)';
    document.getElementById('st-code').style.color=codeOk?'#16a34a':'#dc2626';
    document.getElementById('st-string').textContent=stringLen.toFixed(2)+' m per stringer';
    document.getElementById('st-treads').textContent=nTreads+' treads @ '+w+'mm wide';
    document.getElementById('st-mat-cost').textContent='$'+Math.round(matCost).toLocaleString()+' – $'+Math.round(matCost*1.4).toLocaleString()+' (materials only)';
    document.getElementById('st-result').style.display='';
    var warnEl=document.getElementById('st-warn');
    if(warns.length){warnEl.innerHTML='<strong>⚠ Code warnings:</strong><ul style="margin:.3rem 0 0 1.2rem">'+warns.map(function(w){return'<li>'+w+'</li>';}).join('')+'</ul>';warnEl.style.display='';}
    else{warnEl.style.display='none';}
  }
  calcStair();
  </script>
---

## NZ Building Code Staircase Requirements

All staircases in NZ homes must comply with **NZ Building Code Clause D1** (Access Routes). Key requirements:

### Domestic Staircase Dimensions

| Dimension | Minimum | Maximum |
|---|---|---|
| Rise (riser height) | 150mm | 220mm |
| Going (tread depth) | 220mm | 355mm |
| 2R+G comfort formula | 550mm | 700mm |
| Stair width (domestic) | 800mm | — |
| Handrail height | 900mm | 1,000mm |

### The 2R+G Formula

The comfort formula **2 × Rise + Going = 550–700mm** ensures a natural walking stride. A rise of 175mm and going of 255mm gives 2(175)+255 = 605mm — near perfect.

### Typical Staircase Costs

| Type | Estimated cost |
|---|---|
| Straight pine staircase (supply + install) | $3,500–$6,000 |
| Straight hardwood (rimu, oak) | $6,000–$12,000 |
| Quarter-turn / L-shaped | $7,000–$15,000 |
| Floating/open tread (architectural) | $15,000–$35,000+ |

All staircase work requiring building consent needs an [LBP-licensed builder](/trades/builders/).
