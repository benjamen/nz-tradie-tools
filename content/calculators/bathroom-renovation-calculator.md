---
title: "Bathroom Renovation Cost Calculator — NZ"
description: "Estimate your bathroom renovation cost in New Zealand. Covers tiling, plumbing, waterproofing, fixtures, and labour."
tags: [bathroom, renovation, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchBTab('basic')">Basic Reno</button>
    <button class="calc-tab" onclick="switchBTab('full')">Full Gut & Rebuild</button>
  </div>
  <div id="btab-basic">
    <div class="calc-grid">
      <div class="calc-group"><label>Bathroom size</label>
        <select id="b-size" onchange="calcBathBasic()">
          <option value="4">Small (up to 4m²)</option>
          <option value="7" selected>Medium (5–7m²)</option>
          <option value="12">Large (8–12m²)</option>
          <option value="20">Ensuite / Master (12m²+)</option>
        </select>
      </div>
      <div class="calc-group"><label>Quality level</label>
        <select id="b-qual" onchange="calcBathBasic()">
          <option value="0.7">Budget (Bunnings / trades pricing)</option>
          <option value="1" selected>Mid-range</option>
          <option value="1.6">High-end / Premium</option>
        </select>
      </div>
      <div class="calc-group"><label>Replace toilet?</label>
        <select id="b-toilet" onchange="calcBathBasic()">
          <option value="0">No</option>
          <option value="900" selected>Yes</option>
        </select>
      </div>
      <div class="calc-group"><label>Replace vanity?</label>
        <select id="b-vanity" onchange="calcBathBasic()">
          <option value="0">No</option>
          <option value="1200" selected>Yes</option>
        </select>
      </div>
      <div class="calc-group"><label>Replace shower / bath?</label>
        <select id="b-shower" onchange="calcBathBasic()">
          <option value="0">No</option>
          <option value="2500" selected>Yes — shower</option>
          <option value="1800">Yes — bath</option>
          <option value="4000">Yes — both</option>
        </select>
      </div>
      <div class="calc-group"><label>New tiling?</label>
        <select id="b-tiles" onchange="calcBathBasic()">
          <option value="0">No</option>
          <option value="1" selected>Floor only</option>
          <option value="2">Floor + feature wall</option>
          <option value="3">Full tile (floor + all walls)</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="b-result">
      <h3>Estimated Cost</h3>
      <div class="result-row"><span>Materials &amp; fixtures</span><span id="b-mat"></span></div>
      <div class="result-row"><span>Labour (plumber + tiler + builder)</span><span id="b-lab"></span></div>
      <div class="result-row"><span>Waterproofing &amp; prep</span><span id="b-wp"></span></div>
      <div class="result-row"><span>Total estimate (excl. GST)</span><span id="b-total" class="result-highlight"></span></div>
      <div class="result-row"><span>Total incl. 15% GST</span><span id="b-gst"></span></div>
    </div>
  </div>
  <div id="btab-full" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Floor area (m²)</label><input type="number" id="bf-area" placeholder="e.g. 7" oninput="calcBathFull()"></div>
      <div class="calc-group"><label>Wall area to tile (m²)</label><input type="number" id="bf-wall" placeholder="e.g. 18" oninput="calcBathFull()"></div>
      <div class="calc-group"><label>Tile cost ($/m²)</label><input type="number" id="bf-tcost" placeholder="e.g. 60" value="60" oninput="calcBathFull()"></div>
      <div class="calc-group"><label>Fixtures budget ($)</label><input type="number" id="bf-fix" placeholder="e.g. 4000" oninput="calcBathFull()"></div>
    </div>
    <div class="calc-result" id="bf-result" style="display:none">
      <h3>Estimated Cost</h3>
      <div class="result-row"><span>Tiles (supply + lay)</span><span id="bf-tiles"></span></div>
      <div class="result-row"><span>Waterproofing</span><span id="bf-wp"></span></div>
      <div class="result-row"><span>Fixtures</span><span id="bf-fix-out"></span></div>
      <div class="result-row"><span>Plumbing labour</span><span id="bf-plumb"></span></div>
      <div class="result-row"><span>Builder / sundries</span><span id="bf-build"></span></div>
      <div class="result-row"><span>Total estimate (excl. GST)</span><span id="bf-total" class="result-highlight"></span></div>
      <div class="result-row"><span>Total incl. GST</span><span id="bf-gst"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchBTab(t){
    document.getElementById('btab-basic').style.display=t==='basic'?'':'none';
    document.getElementById('btab-full').style.display=t==='full'?'':'none';
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['basic','full'][i]===t);});
  }
  function calcBathBasic(){
    var sz=parseFloat(document.getElementById('b-size').value);
    var ql=parseFloat(document.getElementById('b-qual').value);
    var toilet=parseFloat(document.getElementById('b-toilet').value);
    var vanity=parseFloat(document.getElementById('b-vanity').value);
    var shower=parseFloat(document.getElementById('b-shower').value);
    var tiles=parseInt(document.getElementById('b-tiles').value);
    var tileBase=[0,sz*120,sz*120+sz*0.6*140,sz*120+sz*2.5*140][tiles];
    var mat=(toilet+vanity+shower+tileBase)*ql;
    var lab=(1200+sz*180)*ql;
    var wp=sz*95*ql;
    var total=mat+lab+wp;
    document.getElementById('b-mat').textContent=nzd(mat);
    document.getElementById('b-lab').textContent=nzd(lab);
    document.getElementById('b-wp').textContent=nzd(wp);
    document.getElementById('b-total').textContent=nzd(total);
    document.getElementById('b-gst').textContent=nzd(total*1.15);
  }
  function calcBathFull(){
    var fa=parseFloat(document.getElementById('bf-area').value)||0;
    var wa=parseFloat(document.getElementById('bf-wall').value)||0;
    var tc=parseFloat(document.getElementById('bf-tcost').value)||60;
    var fix=parseFloat(document.getElementById('bf-fix').value)||0;
    if(!fa&&!wa&&!fix){return;}
    var tiles=(fa+wa)*(tc+85);
    var wp=fa*95+500;
    var plumb=fix*0.35+800;
    var build=1200+fa*150;
    var total=tiles+wp+fix+plumb+build;
    document.getElementById('bf-tiles').textContent=nzd(tiles);
    document.getElementById('bf-wp').textContent=nzd(wp);
    document.getElementById('bf-fix-out').textContent=nzd(fix);
    document.getElementById('bf-plumb').textContent=nzd(plumb);
    document.getElementById('bf-build').textContent=nzd(build);
    document.getElementById('bf-total').textContent=nzd(total);
    document.getElementById('bf-gst').textContent=nzd(total*1.15);
    document.getElementById('bf-result').style.display='';
  }
  calcBathBasic();
  </script>
---

## Bathroom Renovation Costs in NZ

A bathroom renovation is one of the most popular home improvements in New Zealand — and one of the most frequently under-budgeted. Typical costs range from **$8,000 for a basic refresh** to **$35,000+ for a full master ensuite rebuild**.

### What Drives the Cost?

- **Tiling** — tiler rates run $80–$120/hr. Full-tile bathrooms (floor + all walls) add $3,000–$8,000 in labour alone
- **Waterproofing** — mandatory under NZ Building Code E3. Budget $800–$1,500 for a standard bathroom
- **Plumbing** — moving a toilet or shower drain is expensive ($1,500–$3,000 extra). Try to keep fixtures in existing locations
- **Fixtures quality** — a Bunnings-spec toilet + vanity combo runs $1,500; a premium European set can hit $8,000+

### Cost Ranges by Bathroom Type

| Type | Budget | Mid | High-end |
|---|---|---|---|
| Small bathroom (4m²) | $8,000–$12,000 | $14,000–$20,000 | $22,000–$35,000 |
| Medium bathroom (7m²) | $12,000–$18,000 | $20,000–$30,000 | $32,000–$50,000 |
| Master ensuite (12m²+) | $18,000–$28,000 | $30,000–$45,000 | $45,000–$80,000+ |

### Always Get 3 Quotes

Bathroom quotes vary enormously. Use our [Job Cost Calculator](/calculators/job-cost-calculator.html) to sanity-check any quote before signing.
