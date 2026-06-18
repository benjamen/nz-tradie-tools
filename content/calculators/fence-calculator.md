---
title: "Fence Calculator — NZ"
description: "Calculate posts, rails, palings, and concrete needed for any NZ fence. Covers timber paling, post-and-rail, and Colorbond."
tags: [fencing, calculator, NZ, builder, outdoor]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Fence length (m)</label><input type="number" id="fn-len" placeholder="e.g. 30" oninput="calcFence()"></div>
    <div class="calc-group"><label>Fence height (m)</label><input type="number" id="fn-h" placeholder="e.g. 1.8" value="1.8" oninput="calcFence()"></div>
    <div class="calc-group"><label>Post spacing (m)</label><input type="number" id="fn-ps" placeholder="e.g. 2.4" value="2.4" oninput="calcFence()"></div>
    <div class="calc-group"><label>Post hole depth (m)</label><input type="number" id="fn-pd" placeholder="e.g. 0.6" value="0.6" oninput="calcFence()"></div>
    <div class="calc-group"><label>Paling width (mm)</label><input type="number" id="fn-pw" placeholder="e.g. 100" value="100" oninput="calcFence()"></div>
    <div class="calc-group"><label>Paling gap (mm)</label><input type="number" id="fn-pg" placeholder="e.g. 5" value="5" oninput="calcFence()"></div>
    <div class="calc-group"><label>Number of rails</label><input type="number" id="fn-nr" placeholder="e.g. 3" value="3" oninput="calcFence()"></div>
  </div>
  <div class="calc-result" id="fn-result" style="display:none">
    <h3>Result</h3>
    <div class="result-row"><span>Posts needed</span><span id="fn-posts"></span></div>
    <div class="result-row"><span>Rails needed</span><span id="fn-rails"></span></div>
    <div class="result-row"><span>Palings needed</span><span id="fn-palings"></span></div>
    <div class="result-row"><span>Concrete (20kg bags)</span><span id="fn-concrete"></span></div>
    <div class="result-row"><span>Post hole diameter</span><span id="fn-phdia"></span></div>
  </div>
  <script>
  function calcFence(){
    var l=parseFloat(document.getElementById('fn-len').value)||0,
        h=parseFloat(document.getElementById('fn-h').value)||1.8,
        ps=parseFloat(document.getElementById('fn-ps').value)||2.4,
        pd=parseFloat(document.getElementById('fn-pd').value)||0.6,
        pw=parseFloat(document.getElementById('fn-pw').value)||100,
        pg=parseFloat(document.getElementById('fn-pg').value)||5,
        nr=parseFloat(document.getElementById('fn-nr').value)||3;
    if(!l){document.getElementById('fn-result').style.display='none';return;}
    var posts=Math.ceil(l/ps)+1;
    var rails=Math.ceil(l/ps)*nr;
    var spacingM=(pw+pg)/1000;
    var palingsPerBay=Math.ceil(ps/spacingM);
    var palings=palingsPerBay*Math.ceil(l/ps);
    var holeDia=0.2, holeR=holeDia/2;
    var concretePerHole=Math.PI*holeR*holeR*pd;
    var bags=Math.ceil(concretePerHole*posts/0.01);
    document.getElementById('fn-posts').textContent=posts+' posts';
    document.getElementById('fn-rails').textContent=rails+' rails ('+l+'m lengths)';
    document.getElementById('fn-palings').textContent=palings+' palings';
    document.getElementById('fn-concrete').textContent=bags+' × 20kg bags';
    document.getElementById('fn-phdia').textContent=(holeDia*1000)+'mm recommended';
    document.getElementById('fn-result').style.display='';
  }
  </script>
faqs:
  - q: 'How much fencing do I need per lineal metre in NZ?'
    a: 'Measure total fence line in metres. Standard paling fences use posts every 2.4–2.7 m. A 30 m fence needs roughly 12–13 posts. Rails, palings or battens, and fixings are then calculated off this.'
  - q: 'How much does a fence cost per metre in NZ?'
    a: 'A standard 1.8 m timber paling fence in NZ costs $90–$180/lm supply and install. A metal post-and-rail lifestyle fence is $100–$200/lm. Retaining fences with structural requirements can reach $300–$500/lm.'
  - q: 'Do I need council approval for a fence in NZ?'
    a: 'Fences up to 2 m high are generally permitted without resource consent. Fences on boundary or over 2 m often require neighbour agreement and council consent. Retaining fences over 1 m usually need a building consent.'
  - q: 'What timber treatment is needed for NZ fence posts?'
    a: 'Posts in-ground require H5 treatment (CCA-treated). Rails and battens above ground require H3.2. Using the correct hazard class is mandatory under NZS 3602.'
  - q: 'Who pays for a boundary fence in NZ?'
    a: 'Under the Fencing Act 1978, neighbours generally share the cost of an adequate boundary fence equally. If you want a more expensive fence than your neighbour agrees to, you usually cover the extra. Serve a written Fencing Notice to formalise the cost split before starting.'
  - q: 'What are the boundary fence rules in NZ?'
    a: 'The Fencing Act 1978 governs shared boundary fences: neighbours can be required to contribute to a reasonable fence, with disputes resolved via the Disputes Tribunal. The Act doesn''t set a height — local council district plans and the Building Act cover height and consent limits.'
  - q: 'How much does fencing cost in NZ?'
    a: 'A standard 1.8 m timber paling fence runs $90–$180 per lineal metre supplied and installed. Lifestyle post-and-rail is $100–$200/lm, while structural retaining fences can reach $300–$500/lm. Site access, ground conditions and post type are the biggest cost drivers.'
  - q: 'Timber vs concrete fence posts — which is better?'
    a: 'H5-treated timber posts are cheaper and easier to work with but can rot or move over decades. Concrete posts cost more upfront but resist rot, borer and fire, and hold palings dead straight long-term. Concrete is popular for exposed or coastal sites; timber suits budget and standard residential jobs.'
  - q: 'How do I read the results from this fence calculator?'
    a: 'Enter your total fence length and post spacing. The calculator estimates the number of posts, rails, palings and fixings, plus an indicative cost range. Treat materials counts as a buy list and the cost as a planning guide — get a quote for the final supply-and-install price.'
related_articles: [how-to-price-a-job-nz-tradie-guide]
---

## Fence Calculator for NZ Builders & Fencers

Calculate posts, rails, palings, and concrete for timber paling fences. Useful for quoting or ordering materials.

### NZ Fencing Standards

- **Boundary fences:** Standard height is 1.8m for residential privacy
- **Pool fencing:** Minimum 1.2m, NZ Building Code F9 — must be self-closing
- **Post depth:** Bury at least 1/3 of total post length underground (min 600mm)
- **Timber treatment:** All ground-contact timber must be **H4 treated**

### Recommended Post Sizes

| Fence Height | Post Size | Post Spacing |
|---|---|---|
| Up to 1.2m | 100×75mm H4 | Up to 2.4m |
| 1.2–1.8m | 100×100mm H4 | Up to 2.4m |
| 1.8m+ | 125×125mm H4 | Up to 2.4m |

### Fencing Cost Guide

See our [fencing & gates cost guide](/jobs/fencing-and-gates/) for NZ prices by city.
