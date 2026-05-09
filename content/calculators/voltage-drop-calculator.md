---
title: "NZ Voltage Drop Calculator — AS/NZS 3000 Wiring Rules"
description: "Calculate voltage drop percentage for NZ residential and commercial electrical installations per AS/NZS 3000:2018 Wiring Rules."
tags: [electrical, voltage drop, AS/NZS 3000, wiring rules, electricians, NZ]
author: "NZ Tradie Tools"
related_articles: [health-and-safety-guide-nz-tradies, how-to-get-lbp-licence-new-zealand]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group">
      <label>System voltage</label>
      <select id="vd-voltage" onchange="calcVD()">
        <option value="230">230V single phase (standard NZ)</option>
        <option value="400">400V three phase</option>
        <option value="24">24V DC (low voltage)</option>
        <option value="12">12V DC (low voltage)</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Current load (Amps)</label>
      <input type="number" id="vd-amps" placeholder="e.g. 16" step="0.1" oninput="calcVD()">
    </div>
    <div class="calc-group">
      <label>Cable run length (one way, metres)</label>
      <input type="number" id="vd-length" placeholder="e.g. 25" oninput="calcVD()">
    </div>
    <div class="calc-group">
      <label>Cable size</label>
      <select id="vd-cable" onchange="calcVD()">
        <option value="0.0183">1.0mm² twin &amp; earth</option>
        <option value="0.0115">1.5mm² twin &amp; earth</option>
        <option value="0.00727">2.5mm² twin &amp; earth</option>
        <option value="0.00464">4mm² twin &amp; earth</option>
        <option value="0.00292">6mm² twin &amp; earth</option>
        <option value="0.00183">10mm² cable</option>
        <option value="0.00115">16mm² cable</option>
      </select>
    </div>
    <div class="calc-group">
      <label>Installation type</label>
      <select id="vd-install" onchange="calcVD()">
        <option value="final">Final sub-circuit (3% max allowed)</option>
        <option value="mains">Mains / sub-mains (1% max allowed)</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="vd-result" style="display:none">
    <h3>Voltage Drop Result</h3>
    <div class="result-row"><span>Voltage drop</span><span id="vd-r-volts"></span></div>
    <div class="result-row"><span>Voltage drop %</span><span id="vd-r-pct" style="font-weight:700;font-size:1.1rem"></span></div>
    <div class="result-row"><span>Maximum allowed</span><span id="vd-r-max"></span></div>
    <div class="result-row"><span>Compliance</span><span id="vd-r-comply"></span></div>
    <div id="vd-upgrade" style="display:none;margin-top:.75rem;background:#fff8e1;border:1px solid #f6c90e;border-radius:6px;padding:.75rem;font-size:.85rem"></div>
  </div>
  <script>
  function calcVD(){
    var V=parseFloat(document.getElementById("vd-voltage").value)||230;
    var I=parseFloat(document.getElementById("vd-amps").value)||0;
    var L=parseFloat(document.getElementById("vd-length").value)||0;
    var R=parseFloat(document.getElementById("vd-cable").value)||0.00727;
    var install=document.getElementById("vd-install").value;
    var r=document.getElementById("vd-result");
    if(!I||!L){r.style.display="none";return;}
    var vd=2*I*L*R;
    var pct=(vd/V)*100;
    var maxPct=install==="final"?3:1;
    var pass=pct<=maxPct;
    document.getElementById("vd-r-volts").textContent=vd.toFixed(2)+"V";
    document.getElementById("vd-r-pct").textContent=pct.toFixed(2)+"%";
    document.getElementById("vd-r-max").textContent=maxPct+"% (AS/NZS 3000 limit)";
    document.getElementById("vd-r-comply").innerHTML=pass
      ?"<span style="color:#22543d;font-weight:600">✓ Compliant</span>"
      :"<span style="color:#c53030;font-weight:600">✗ Exceeds limit — upsize cable</span>";
    var up=document.getElementById("vd-upgrade");
    if(!pass){
      var newL=maxPct/100*V/(2*I*R);
      up.innerHTML="<strong>Options:</strong> Upsize cable to next size, or reduce run length to "+newL.toFixed(0)+"m for this cable size. Consider adding an intermediate distribution board.";
      up.style.display="";
    }else{up.style.display="none";}
    r.style.display="";
  }
  </script>
faqs:
  - q: 'What is voltage drop and why does it matter in NZ electrical installations?'
    a: 'Voltage drop is the reduction in voltage along a cable due to resistance. AS/NZS 3000:2018 limits voltage drop to 5% from the supply point to the point of use. Excessive voltage drop causes poor equipment performance and motor overheating.'
  - q: 'How do I calculate voltage drop for a NZ electrical circuit?'
    a: 'Vd = 2 × I × L × R/1000, where I = current (A), L = cable length (m), R = resistance of cable conductor (Ω/km from AS/NZS 3008). For a 20 A circuit, 30 m of 2.5 mm² cable: Vd = 2 × 20 × 30 × 7.41/1000 = 8.9 V (4.0% of 230 V).'
  - q: 'When does voltage drop require upsizing the cable in NZ?'
    a: 'If calculated voltage drop exceeds 5% (11.5 V on a 230 V supply), you must use a larger cable cross-section. Increase to the next standard size (e.g. 2.5 mm² to 4 mm²) and recalculate until within limit.'
  - q: 'Does AS/NZS 3000 voltage drop apply to solar PV circuits in NZ?'
    a: 'Yes. DC wiring from solar panels to the inverter should also be designed for less than 3% voltage drop (some designers use 1–2%) to minimise energy losses. AC output circuits follow the standard 5% limit.'
---

## Voltage Drop in NZ Electrical Installations

Voltage drop occurs when current flows through a cable — the cable's resistance causes a reduction in voltage at the far end. Too much drop means appliances don't get sufficient voltage to operate correctly, and in commercial settings can cause equipment failure.

### NZ Compliance — AS/NZS 3000:2018

New Zealand follows the **AS/NZS 3000:2018 Wiring Rules** (the "Wiring Rules"). Maximum allowed voltage drop:

| Circuit type | Maximum voltage drop |
|---|---|
| Final sub-circuits | 3% of supply voltage |
| Mains and sub-mains | 1% of supply voltage |

For a 230V single-phase supply:
- Final circuits: max **6.9V** drop
- Mains: max **2.3V** drop

### Formula Used

This calculator uses the standard resistive formula:

**Vd = 2 × I × L × R**

Where I = current (amps), L = one-way cable length (metres), R = resistance per metre of conductor (Ω/m).

Note: this is a simplified resistive calculation. For large cable sizes or long runs, reactance also plays a role — refer to AS/NZS 3008.1.1 for full de-rating tables.

### All Electrical Work Must Be Done by a Registered Electrician

In New Zealand, electrical installation work must be carried out by a licensed electrician and covered by a Certificate of Compliance (CoC). WorkSafe NZ enforces this under the Electricity Act 1992.
