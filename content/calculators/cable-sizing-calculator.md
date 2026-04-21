---
title: "Electrical Cable Sizing Calculator — NZ"
description: "Calculate the correct cable size for NZ electrical installations — current capacity, voltage drop, and circuit breaker sizing."
tags: [electrical, cable, sizing, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-tabs">
    <button class="calc-tab active" onclick="switchCSTab('size')">Cable Size</button>
    <button class="calc-tab" onclick="switchCSTab('vd')">Voltage Drop</button>
    <button class="calc-tab" onclick="switchCSTab('cb')">Circuit Breaker</button>
  </div>
  <div id="cstab-size">
    <div class="calc-grid">
      <div class="calc-group"><label>Load (Watts)</label><input type="number" id="cs-w" placeholder="e.g. 2400" oninput="calcCableSize()"></div>
      <div class="calc-group"><label>Voltage</label>
        <select id="cs-v" onchange="calcCableSize()">
          <option value="230" selected>230V (single phase — NZ standard)</option>
          <option value="400">400V (three phase)</option>
        </select>
      </div>
      <div class="calc-group"><label>Installation method</label>
        <select id="cs-inst" onchange="calcCableSize()">
          <option value="1" selected>In conduit / wall</option>
          <option value="1.25">Open air / trunking</option>
          <option value="0.75">Buried in ground</option>
          <option value="0.7">Grouped (4+ cables)</option>
        </select>
      </div>
      <div class="calc-group"><label>Cable run length (m)</label><input type="number" id="cs-len" placeholder="e.g. 20" oninput="calcCableSize()"></div>
    </div>
    <div class="calc-result" id="cs-result" style="display:none">
      <h3>Cable Sizing</h3>
      <div class="result-row"><span>Load current</span><span id="cs-amps"></span></div>
      <div class="result-row"><span>Minimum cable size</span><span id="cs-size" class="result-highlight"></span></div>
      <div class="result-row"><span>Recommended circuit breaker</span><span id="cs-cb"></span></div>
      <div class="result-row"><span>Voltage drop (estimated)</span><span id="cs-vd"></span></div>
      <div id="cs-note" style="margin-top:.6rem;padding:.5rem .75rem;background:#dbeafe;border-left:3px solid #3b82f6;font-size:.84rem"></div>
    </div>
  </div>
  <div id="cstab-vd" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Cable cross-section (mm²)</label>
        <select id="vd-size" onchange="calcVD()">
          <option value="1.5">1.5mm²</option>
          <option value="2.5" selected>2.5mm²</option>
          <option value="4">4mm²</option>
          <option value="6">6mm²</option>
          <option value="10">10mm²</option>
          <option value="16">16mm²</option>
        </select>
      </div>
      <div class="calc-group"><label>Current (A)</label><input type="number" id="vd-a" placeholder="e.g. 15" oninput="calcVD()"></div>
      <div class="calc-group"><label>One-way length (m)</label><input type="number" id="vd-len" placeholder="e.g. 30" oninput="calcVD()"></div>
      <div class="calc-group"><label>Supply voltage (V)</label><input type="number" id="vd-v" placeholder="230" value="230" oninput="calcVD()"></div>
    </div>
    <div class="calc-result" id="vd-result" style="display:none">
      <h3>Voltage Drop</h3>
      <div class="result-row"><span>Voltage drop</span><span id="vd-drop" class="result-highlight"></span></div>
      <div class="result-row"><span>% of supply voltage</span><span id="vd-pct"></span></div>
      <div class="result-row"><span>NZ limit (AS/NZS 3000)</span><span>5% max (11.5V at 230V)</span></div>
      <div id="vd-status" style="margin-top:.5rem;padding:.5rem .75rem;font-size:.84rem;border-radius:3px;font-weight:700"></div>
    </div>
  </div>
  <div id="cstab-cb" style="display:none">
    <div class="calc-grid">
      <div class="calc-group"><label>Total load (Watts)</label><input type="number" id="cb-w" placeholder="e.g. 3600" oninput="calcCB()"></div>
      <div class="calc-group"><label>Voltage (V)</label><input type="number" id="cb-v" placeholder="230" value="230" oninput="calcCB()"></div>
      <div class="calc-group"><label>Diversity factor (%)</label><input type="number" id="cb-div" placeholder="100" value="100" oninput="calcCB()"></div>
    </div>
    <div class="calc-result" id="cb-result" style="display:none">
      <h3>Circuit Breaker Size</h3>
      <div class="result-row"><span>Design current</span><span id="cb-amps"></span></div>
      <div class="result-row"><span>Recommended MCB size</span><span id="cb-size" class="result-highlight"></span></div>
    </div>
  </div>
  <script>
  function switchCSTab(t){
    ['size','vd','cb'].forEach(function(id){document.getElementById('cstab-'+id).style.display=id===t?'':'none';});
    document.querySelectorAll('.calc-tab').forEach(function(b,i){b.classList.toggle('active',['size','vd','cb'][i]===t);});
  }
  var resistivity={1.5:12.1,2.5:7.41,4:4.61,6:3.08,10:1.83,16:1.15,25:0.727};
  function calcCableSize(){
    var w=parseFloat(document.getElementById('cs-w').value)||0;
    var v=parseFloat(document.getElementById('cs-v').value);
    var inst=parseFloat(document.getElementById('cs-inst').value);
    var len=parseFloat(document.getElementById('cs-len').value)||0;
    if(!w){document.getElementById('cs-result').style.display='none';return;}
    var amps=w/v;
    var designAmps=amps/inst;
    var sizes=[1.5,2.5,4,6,10,16,25];
    var caps={1.5:13,2.5:18,4:24,6:31,10:43,16:57,25:75};
    var sz=sizes.find(function(s){return caps[s]>=designAmps;})||25;
    var cbs=[6,10,13,16,20,25,32,40,50,63];
    var cb=cbs.find(function(c){return c>=amps;})||63;
    var vdrop=resistivity[sz]*2*len*amps/1000;
    var vdpct=vdrop/v*100;
    document.getElementById('cs-amps').textContent=amps.toFixed(1)+' A';
    document.getElementById('cs-size').textContent=sz+'mm² (capacity: '+caps[sz]+'A derated)';
    document.getElementById('cs-cb').textContent=cb+'A MCB (Type B or C)';
    document.getElementById('cs-vd').textContent=vdrop.toFixed(2)+'V ('+vdpct.toFixed(1)+'%)'+(vdpct>5?' ⚠ Exceeds 5% limit':'');
    document.getElementById('cs-note').textContent='Note: This is a guide only. All NZ electrical work must be designed and installed by a Registered Electrical Worker (REW) in accordance with AS/NZS 3000.';
    document.getElementById('cs-result').style.display='';
  }
  function calcVD(){
    var sz=parseFloat(document.getElementById('vd-size').value);
    var a=parseFloat(document.getElementById('vd-a').value)||0;
    var len=parseFloat(document.getElementById('vd-len').value)||0;
    var v=parseFloat(document.getElementById('vd-v').value)||230;
    if(!a||!len){document.getElementById('vd-result').style.display='none';return;}
    var drop=resistivity[sz]*2*len*a/1000;
    var pct=drop/v*100;
    document.getElementById('vd-drop').textContent=drop.toFixed(2)+'V';
    document.getElementById('vd-pct').textContent=pct.toFixed(2)+'%';
    var s=document.getElementById('vd-status');
    if(pct>5){s.style.background='#fef2f2';s.style.color='#991b1b';s.textContent='✗ Exceeds NZ 5% limit — increase cable size or reduce run length.';}
    else{s.style.background='#f0fdf4';s.style.color='#166534';s.textContent='✓ Within NZ AS/NZS 3000 voltage drop limit (5%).';}
    document.getElementById('vd-result').style.display='';
  }
  function calcCB(){
    var w=parseFloat(document.getElementById('cb-w').value)||0;
    var v=parseFloat(document.getElementById('cb-v').value)||230;
    var div=parseFloat(document.getElementById('cb-div').value)||100;
    if(!w){document.getElementById('cb-result').style.display='none';return;}
    var a=w/v*div/100;
    var cbs=[6,10,13,16,20,25,32,40,50,63,80,100];
    var sz=cbs.find(function(c){return c>=a;})||100;
    document.getElementById('cb-amps').textContent=a.toFixed(1)+' A';
    document.getElementById('cb-size').textContent=sz+' A MCB';
    document.getElementById('cb-result').style.display='';
  }
  </script>
---

## NZ Electrical Standards

All electrical installations in NZ must comply with **AS/NZS 3000** (Wiring Rules) as adopted under the NZ Electricity Regulations 2010.

### Common Cable Sizes

| Application | Typical cable |
|---|---|
| General power circuits | 2.5mm² TPS |
| Lighting circuits | 1.5mm² TPS |
| Hot water / stove | 4mm² or 6mm² |
| Air conditioning (large) | 6mm² or 10mm² |
| Sub-board / main feed | 16mm²+ |

### Voltage Drop Limits (AS/NZS 3000)

- **5% maximum** from supply point to any point in the installation
- At 230V: maximum 11.5V drop allowed
- Longer cable runs always need larger cable to compensate

### Important

All electrical work in NZ must be carried out by a **Registered Electrical Worker (REW)**. This calculator is a reference tool for planning purposes only. Find [licensed electricians](/trades/electricians/) in your area.
