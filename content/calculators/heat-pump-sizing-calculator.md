---
title: "Heat Pump Sizing Calculator — NZ"
description: "Calculate the right heat pump size (kW) for your NZ room or home. Get recommended capacity, running costs, and brand comparisons."
tags: [heat pump, sizing, calculator, NZ, HVAC]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchHPTab('room')">Single Room</button>
    <button class="calc-tab" onclick="switchHPTab('whole')">Whole Home</button>
  </div>
  <div id="hptab-room">
    <div class="calc-grid">
      <div class="calc-group"><label>Room length (m)</label><input type="number" id="rp-len" placeholder="e.g. 5" oninput="calcHP()"></div>
      <div class="calc-group"><label>Room width (m)</label><input type="number" id="rp-wid" placeholder="e.g. 4" oninput="calcHP()"></div>
      <div class="calc-group"><label>Ceiling height (m)</label><input type="number" id="rp-ch" placeholder="e.g. 2.4" value="2.4" oninput="calcHP()"></div>
      <div class="calc-group"><label>Climate zone</label>
        <select id="rp-zone" onchange="calcHP()">
          <option value="0.8">Auckland / Northland (mild)</option>
          <option value="1.0" selected>Wellington / Hamilton (moderate)</option>
          <option value="1.2">Christchurch / Otago (cold)</option>
          <option value="1.4">Southland / Alpine (very cold)</option>
        </select>
      </div>
      <div class="calc-group"><label>Insulation level</label>
        <select id="rp-ins" onchange="calcHP()">
          <option value="1.3">Poor (pre-1978, minimal)</option>
          <option value="1.1" selected>Average (some ceiling/floor)</option>
          <option value="0.9">Good (meets current code)</option>
          <option value="0.75">Excellent (high performance)</option>
        </select>
      </div>
      <div class="calc-group"><label>Room use</label>
        <select id="rp-use" onchange="calcHP()">
          <option value="0.9">Bedroom / occasional</option>
          <option value="1.0" selected>Living room / main area</option>
          <option value="1.15">Open plan / drafty</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="hp-result" style="display:none">
      <h3>Heat Pump Recommendation</h3>
      <div class="result-row"><span>Room volume</span><span id="hp-vol"></span></div>
      <div class="result-row"><span>Recommended capacity</span><span id="hp-kw" class="result-highlight"></span></div>
      <div class="result-row"><span>Suggested unit</span><span id="hp-unit"></span></div>
      <div class="result-row"><span>Estimated supply + install</span><span id="hp-install"></span></div>
      <div class="result-row"><span>Approx running cost (winter)</span><span id="hp-run"></span></div>
    </div>
  </div>
  <div id="hptab-whole" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Total floor area (m²)</label><input type="number" id="wh-area" placeholder="e.g. 150" oninput="calcWholeHome()"></div>
      <div class="calc-group"><label>Storeys</label>
        <select id="wh-stor" onchange="calcWholeHome()">
          <option value="1" selected>Single storey</option>
          <option value="1.3">Two storey</option>
        </select>
      </div>
      <div class="calc-group"><label>Climate zone</label>
        <select id="wh-zone" onchange="calcWholeHome()">
          <option value="0.8">Auckland / Northland</option>
          <option value="1.0" selected>Wellington / Hamilton</option>
          <option value="1.2">Christchurch / Otago</option>
          <option value="1.4">Southland / Alpine</option>
        </select>
      </div>
    </div>
    <div class="calc-result" id="wh-result" style="display:none">
      <h3>Whole-Home Heat Pump</h3>
      <div class="result-row"><span>Recommended capacity</span><span id="wh-kw" class="result-highlight"></span></div>
      <div class="result-row"><span>Estimated install cost</span><span id="wh-cost"></span></div>
      <div class="result-row"><span>Multi-split option</span><span id="wh-split"></span></div>
    </div>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function switchHPTab(t){
    document.getElementById('hptab-room').style.display=t==='room'?'':'none';
    document.getElementById('hptab-whole').style.display=t==='whole'?'':'none';
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['room','whole'][i]===t);});
  }
  function calcHP(){
    var len=parseFloat(document.getElementById('rp-len').value)||0;
    var wid=parseFloat(document.getElementById('rp-wid').value)||0;
    var ch=parseFloat(document.getElementById('rp-ch').value)||2.4;
    var zone=parseFloat(document.getElementById('rp-zone').value);
    var ins=parseFloat(document.getElementById('rp-ins').value);
    var use=parseFloat(document.getElementById('rp-use').value);
    if(!len||!wid){document.getElementById('hp-result').style.display='none';return;}
    var vol=len*wid*ch;
    var kw=vol*0.065*zone*ins*use;
    kw=Math.max(2.5,kw);
    var sizes=[2.5,3.5,4.2,5.0,6.0,7.0,8.0,9.0];
    var sz=sizes.find(function(s){return s>=kw;})||9.0;
    var units={2.5:'Mitsubishi MSZ-AP25 / Panasonic CS-Z25',3.5:'Mitsubishi MSZ-AP35 / Fujitsu SET35',4.2:'Panasonic CS-Z42',5.0:'Mitsubishi MSZ-AP50 / Daikin FTXM50',6.0:'Mitsubishi MSZ-AP60 / Daikin FTXM60',7.0:'Mitsubishi MSZ-AP71 / Fujitsu SET71',8.0:'Daikin FTXM85 / LG Art Cool 8kW',9.0:'Multi-split or ducted system recommended'};
    var installCost=sz*650+1200;
    var runPerHr=sz/4.5*0.32;
    document.getElementById('hp-vol').textContent=vol.toFixed(1)+' m³';
    document.getElementById('hp-kw').textContent=sz+' kW (min '+kw.toFixed(1)+' kW required)';
    document.getElementById('hp-unit').textContent=units[sz]||'Consult installer';
    document.getElementById('hp-install').textContent=nzd(installCost)+' – '+nzd(installCost*1.25);
    document.getElementById('hp-run').textContent='~$'+runPerHr.toFixed(2)+'/hr (at $0.32/kWh, COP 3.5)';
    document.getElementById('hp-result').style.display='';
  }
  function calcWholeHome(){
    var area=parseFloat(document.getElementById('wh-area').value)||0;
    var stor=parseFloat(document.getElementById('wh-stor').value);
    var zone=parseFloat(document.getElementById('wh-zone').value);
    if(!area){document.getElementById('wh-result').style.display='none';return;}
    var kw=area*0.075*zone*stor;
    var cost=kw*900+2500;
    var splits=Math.ceil(kw/5.5);
    document.getElementById('wh-kw').textContent=kw.toFixed(1)+' kW total';
    document.getElementById('wh-cost').textContent=nzd(cost)+' – '+nzd(cost*1.4);
    document.getElementById('wh-split').textContent=splits+' x head unit multi-split system';
    document.getElementById('wh-result').style.display='';
  }
  </script>
---

## Heat Pump Sizing Guide for NZ Homes

Getting the right sized heat pump matters — undersized units run constantly, oversized units short-cycle and waste energy.

### Rule of Thumb

For a standard NZ home: **approximately 75W per m² of floor area** for an average insulated, moderate climate home. Adjust for climate zone and insulation quality.

### Typical NZ Heat Pump Costs (Installed)

| Size | Typical unit | Supply + install |
|---|---|---|
| 2.5 kW | Small bedroom | $2,000–$2,800 |
| 3.5 kW | Medium bedroom / small lounge | $2,500–$3,500 |
| 5.0 kW | Large lounge / open plan | $3,200–$4,500 |
| 7.0 kW | Large open-plan living | $4,500–$6,500 |
| Multi-split | Whole home | $8,000–$18,000+ |

### Top NZ Brands

- **Mitsubishi Electric** — most popular in NZ, excellent cold-climate performance
- **Fujitsu** — reliable, good warranty support
- **Panasonic** — strong inverter tech
- **Daikin** — premium build quality
- **LG** — Art Cool designer range

All heat pump installers must be [REW-registered electricians](/trades/electricians/) and ideally HVAC-certified.
