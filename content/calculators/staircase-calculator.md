---
title: "Staircase Calculator — NZ (Rise, Run & Dimensions)"
seo_title: "Stair Calculator NZ 2026 — Step Count, Rise & Run (Free)"
description: "Free NZ staircase calculator — enter floor height to get step count, rise, going, and total run compliant with NZ Building Code. Instant results."
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
faqs:
  - q: 'What are the NZ Building Code requirements for staircase dimensions?'
    a: 'NZ Building Code Clause D1 requires: riser height 150–220 mm, tread depth (going) 220–355 mm, and the comfort formula 2R + G = 550–700 mm. Handrails are mandatory on stairs with 4+ risers, positioned 900–1,000 mm above the stairline. All dimensions must comply unless specific exemptions apply.'
  - q: 'How do I calculate the number of steps needed for my floor height?'
    a: 'Divide your floor-to-floor height (mm) by your preferred riser height (typically 175 mm). For example, 2,700 mm ÷ 175 = 15.4 risers, so round to 15 or 16. The actual riser becomes 2,700 ÷ 15 = 180 mm per step. Use this calculator to adjust dimensions until you achieve the ideal 2R + G formula.'
  - q: 'Does a staircase replacement require a building consent in NZ?'
    a: 'Like-for-like internal stair replacements (same location, dimensions, materials) are typically exempt. However, new stairs, stairs serving a new level, or stairs outside NZS 3604 parameters REQUIRE a building consent. Check with your local council or an LBP-licensed builder before starting.'
  - q: 'What timber and materials are used for NZ residential stairs?'
    a: 'Stringers use H1.2 treated pine, H3.1 hardwood, or engineered laminated beam. Treads are 44 mm dressed pine, native hardwood (rimu, matai), oak, or engineered timber flooring. Handrails are typically 45 mm diameter hardwood or stainless steel. Always use licensed timber graded for structural use.'
  - q: 'How much does a staircase cost in NZ?'
    a: 'Straight timber staircases cost $3,500–$6,000 (supply + install). Hardwood or curved stairs range $6,000–$15,000. Floating or architectural stairs cost $15,000–$35,000+. Costs vary by builder experience, material selection, and whether building consent is required. Get 3 quotes with detailed line items.'
related_articles: [carpenter-pricing-guide-nz-2026, how-to-get-lbp-licence-new-zealand, how-to-price-a-job-nz-tradie-guide]
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

## How to Use This Stair Calculator

Enter your **floor-to-floor height** (the vertical distance from finished floor to finished floor, in mm). A standard NZ storey is typically 2,550–2,700mm.

Adjust the **preferred rise** until you find a combination that satisfies the 2R+G formula (550–700mm) and fits your available floor run. The calculator flags any NZ Building Code Clause D1 violations in red.

**Typical inputs for a standard NZ house:**
- Floor height: 2,700mm
- Rise: 175mm → 15 risers, actual rise 180mm
- Going: 255mm → 2R+G = 2(180)+255 = 615mm ✓
- Total run: 14 treads × 255mm = 3,570mm (about 3.6m of floor space)

## Common NZ Staircase Configurations

### Straight Staircase
The simplest and most common. One uninterrupted flight from bottom to top. Requires continuous floor space of approximately 3.2–4.0m depending on floor height. Easiest to build, lowest cost.

### L-Shaped (Quarter Turn)
Changes direction 90° at a landing or winder steps. Useful when floor space doesn't allow a straight run. The landing interrupts the climb — often more comfortable for elderly users.

### U-Shaped (Half Turn / Switchback)
Changes direction 180° — the staircase goes up, turns, and comes back the other way. Common in two-storey NZ homes where the stair must fit within a compact stair well.

### Winder Stairs
Triangular or trapezoidal steps that allow a turn without a landing. More complex to build, require careful calculation to ensure the 2R+G formula is met on the walking line (typically measured 270mm from the narrow end per NZS 3604).

### Spiral Staircase
A central pole with radiating treads. NZ Building Code allows spiral stairs as secondary access (e.g., to a loft or mezzanine) but they cannot serve as the sole means of escape. Minimum going at the walking line (not the narrow end) must still comply.

## Do You Need Building Consent for a Staircase in NZ?

| Scenario | Consent required? |
|---|---|
| Replace existing stair like-for-like (same location, same dimensions) | Generally no |
| New stair in an existing opening | Yes |
| Stair to a new floor or loft | Yes |
| Deck stair (under 1.5m deck height, Schedule 1) | Generally no |
| Change stair configuration (straight to L-shape) | Yes |
| Stair that doesn't comply with NZS 3604 | Yes — engineering required |

When in doubt, call your council's duty planner — it's a free 10-minute call and gives you certainty before you start.

## Staircase DIY vs Licensed Builder

Under the Building Act 2004, stair work that requires a building consent is **restricted building work** — it must be done by or under the supervision of a [Licensed Building Practitioner (LBP)](/trades/builders/).

What you CAN DIY:
- Like-for-like replacement of treads or handrails on an existing compliant stair (maintenance)
- Painting or finishing an existing staircase
- External deck stairs under Schedule 1 exemption heights

What requires an LBP:
- Any consented stair work (new stair, new configuration)
- Structural elements (stringers, structural landing)

**Find LBP builders near you:** [Builders NZ](/trades/builders/) | [Post a Staircase Job Free](/post-job/)
