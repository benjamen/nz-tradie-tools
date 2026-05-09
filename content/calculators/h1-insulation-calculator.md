---
title: "NZ H1 Insulation Compliance Calculator (2023 Requirements)"
description: "Check minimum R-values required for your NZ climate zone under the H1 Energy Efficiency 5th edition — ceiling, walls, underfloor and slab."
tags: [H1, insulation, R-value, building code, compliance, NZ]
author: "NZ Tradie Tools"
related_articles: [healthy-homes-compliance-work-nz-tradies-2026, building-consent-reform-nz-2026-tradies-guide, do-you-need-building-consent-nz]
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group" style="grid-column:1/-1">
      <label>Select your NZ climate zone</label>
      <select id="h1-zone" onchange="calcH1()">
        <option value="">— Select zone —</option>
        <option value="1">Zone 1 — Northland (Whangarei, Kerikeri)</option>
        <option value="2">Zone 2 — Auckland, Bay of Plenty, Gisborne, Hawke's Bay</option>
        <option value="3">Zone 3 — Taranaki, Manawatū, Whanganui</option>
        <option value="4">Zone 4 — Wellington, Nelson, Marlborough, West Coast</option>
        <option value="5">Zone 5 — Canterbury, Dunedin, Invercargill</option>
        <option value="6">Zone 6 — Central Otago, Queenstown, Southland inland</option>
      </select>
    </div>
  </div>
  <div class="calc-group" style="margin-top:1rem">
    <label>Your proposed insulation (optional — check compliance)</label>
  </div>
  <div class="calc-grid">
    <div class="calc-group">
      <label>Ceiling R-value installed</label>
      <input type="number" id="h1-ceil-actual" placeholder="e.g. 3.6" step="0.1" oninput="calcH1()">
    </div>
    <div class="calc-group">
      <label>Wall R-value installed</label>
      <input type="number" id="h1-wall-actual" placeholder="e.g. 2.2" step="0.1" oninput="calcH1()">
    </div>
    <div class="calc-group">
      <label>Underfloor R-value installed</label>
      <input type="number" id="h1-floor-actual" placeholder="e.g. 1.8" step="0.1" oninput="calcH1()">
    </div>
    <div class="calc-group">
      <label>Slab perimeter R-value installed</label>
      <input type="number" id="h1-slab-actual" placeholder="e.g. 1.0" step="0.1" oninput="calcH1()">
    </div>
  </div>
  <div class="calc-result" id="h1-result" style="display:none">
    <h3 id="h1-zone-label"></h3>
    <div class="result-row" style="font-weight:600"><span>Element</span><span>Required R-value</span><span>Your R-value</span><span>Status</span></div>
    <div class="result-row"><span>Ceiling</span><span id="h1-r-ceil"></span><span id="h1-a-ceil">—</span><span id="h1-s-ceil">—</span></div>
    <div class="result-row"><span>Walls</span><span id="h1-r-wall"></span><span id="h1-a-wall">—</span><span id="h1-s-wall">—</span></div>
    <div class="result-row"><span>Underfloor</span><span id="h1-r-floor"></span><span id="h1-a-floor">—</span><span id="h1-s-floor">—</span></div>
    <div class="result-row"><span>Slab perimeter</span><span id="h1-r-slab"></span><span id="h1-a-slab">—</span><span id="h1-s-slab">—</span></div>
    <p style="font-size:.8rem;color:#666;margin-top:.75rem">R-values are minimums under NZS 4218 H1 5th edition (effective 1 Nov 2023). Always confirm with your BCA and check BRANZ for the latest values.</p>
  </div>
  <script>
  var H1={
    1:{ceil:3.3,wall:1.9,floor:1.3,slab:0.7,label:'Zone 1 — Northland'},
    2:{ceil:3.3,wall:1.9,floor:1.3,slab:0.7,label:'Zone 2 — Auckland & Bay of Plenty'},
    3:{ceil:4.0,wall:2.0,floor:1.3,slab:0.7,label:'Zone 3 — Taranaki & Manawatū'},
    4:{ceil:4.0,wall:2.0,floor:1.3,slab:1.0,label:'Zone 4 — Wellington & Nelson'},
    5:{ceil:6.6,wall:2.4,floor:2.0,slab:1.4,label:'Zone 5 — Canterbury & Dunedin'},
    6:{ceil:6.6,wall:2.4,floor:2.0,slab:1.4,label:'Zone 6 — Central Otago & Queenstown'}
  };
  function status(actual,req){
    if(!actual||isNaN(actual))return'—';
    return actual>=req?'<span style="color:#22543d;font-weight:600">✓ Pass</span>':'<span style="color:#c53030;font-weight:600">✗ Fail</span>';
  }
  function calcH1(){
    var z=parseInt(document.getElementById('h1-zone').value);
    var r=document.getElementById('h1-result');
    if(!z){r.style.display='none';return;}
    var d=H1[z];
    document.getElementById('h1-zone-label').textContent=d.label+' — Minimum R-values';
    var vals={ceil:'h1-ceil-actual',wall:'h1-wall-actual',floor:'h1-floor-actual',slab:'h1-slab-actual'};
    var keys={ceil:d.ceil,wall:d.wall,floor:d.floor,slab:d.slab};
    var ids={ceil:'ceil',wall:'wall',floor:'floor',slab:'slab'};
    ['ceil','wall','floor','slab'].forEach(function(k){
      document.getElementById('h1-r-'+k).textContent='R'+keys[k].toFixed(1);
      var av=parseFloat(document.getElementById('h1-'+k+'-actual').value);
      document.getElementById('h1-a-'+k).textContent=isNaN(av)?'—':'R'+av.toFixed(1);
      document.getElementById('h1-s-'+k).innerHTML=isNaN(av)?'—':status(av,keys[k]);
    });
    r.style.display='';
  }
  </script>
faqs:
  - q: 'What R-value do I need under NZ Building Code H1?'
    a: 'H1 5th edition (from 2023) sets zone-dependent minimum R-values. Auckland (Zone 1) requires R2.9 underfloor, R6.6 ceiling. Queenstown (Zone 6) requires R3.6 underfloor, R9.6 ceiling. Walls range R2.0–R2.8 by zone.'
  - q: 'Which NZ climate zone am I in for insulation?'
    a: 'NZ has 6 climate zones. Zone 1 covers Northland and Auckland; Zone 2 Waikato to Bay of Plenty; Zone 3 Hawke''s Bay and Taranaki; Zone 4 Wellington and Nelson; Zone 5 inland South Island; Zone 6 alpine areas including Queenstown and Wanaka.'
  - q: 'Does H1 5th edition apply to renovations?'
    a: 'H1 5th edition applies to new builds consented after its adoption date. Renovations that alter the building envelope (e.g. reroofing, new exterior cladding) generally trigger the current H1 requirements for the altered areas.'
  - q: 'How do I meet H1 requirements in my wall assembly?'
    a: 'Typical NZ wall assemblies meet H1 using a combination of framing R-value (timber), bulk insulation batt R-value, and sometimes external rigid foam insulation. The total system R-value must meet or exceed the zone minimum.'
---

## NZ H1 Energy Efficiency — 2023 Requirements

New Zealand's Building Code Clause H1 sets minimum insulation requirements for new homes. The **H1 5th edition** significantly increased R-value requirements and became mandatory for all new building consents from **1 November 2023**.

### NZ Climate Zones

NZ is divided into 6 climate zones under NZS 4218:

| Zone | Cities/Regions |
|---|---|
| 1 | Northland, Far North |
| 2 | Auckland, Bay of Plenty, Gisborne, Hawke's Bay |
| 3 | Taranaki, Manawatū, Whanganui |
| 4 | Wellington, Nelson, Marlborough, West Coast |
| 5 | Canterbury, Otago, Invercargill |
| 6 | Central Otago, Queenstown, Southland inland |

### Why H1 Changed in 2023

The updated requirements (particularly for Zones 5 and 6, where ceiling R-values jumped to R6.6) were driven by the government's goal of reducing household energy use and carbon emissions. Builders and insulators who haven't updated their standard specifications may be under-quoting.

### Common Mistakes

- Using old R-values from pre-2023 H1 4th edition
- Confusing total R-value of the building element with the insulation batt R-value — they're different
- Forgetting slab perimeter insulation, which is now required in Zones 4–6

For the full H1 calculation method, use the [BRANZ H1 tool](https://www.branz.co.nz/energy-efficiency/). Always confirm requirements with your Building Consent Authority (BCA).
