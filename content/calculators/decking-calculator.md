---
title: "Decking Calculator — NZ"
description: "Calculate how many deck boards, joists, posts and screws you need for any NZ deck. Covers timber and composite."
tags: [decking, calculator, NZ, builder, outdoor]
author: "NZ Tradie Tools"
layout: calculator
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Deck length (m)</label><input type="number" id="d-len" placeholder="e.g. 6" oninput="calcDeck()"></div>
    <div class="calc-group"><label>Deck width (m)</label><input type="number" id="d-wid" placeholder="e.g. 4" oninput="calcDeck()"></div>
    <div class="calc-group"><label>Board width (mm)</label><input type="number" id="d-bw" placeholder="e.g. 140" value="140" oninput="calcDeck()"></div>
    <div class="calc-group"><label>Board gap (mm)</label><input type="number" id="d-gap" placeholder="e.g. 5" value="5" oninput="calcDeck()"></div>
    <div class="calc-group"><label>Joist spacing (mm)</label><input type="number" id="d-js" placeholder="e.g. 450" value="450" oninput="calcDeck()"></div>
    <div class="calc-group"><label>Board price per m ($)</label><input type="number" id="d-price" placeholder="e.g. 12" oninput="calcDeck()"></div>
  </div>
  <div class="calc-result" id="d-result" style="display:none">
    <h3>Result</h3>
    <div class="result-row"><span>Deck area</span><span id="d-area"></span></div>
    <div class="result-row"><span>Boards needed (deck length)</span><span id="d-boards"></span></div>
    <div class="result-row"><span>Joists needed</span><span id="d-joists"></span></div>
    <div class="result-row"><span>Screws (approx)</span><span id="d-screws"></span></div>
    <div class="result-row"><span>Estimated board cost</span><span id="d-cost"></span></div>
  </div>
  <script>
  function calcDeck(){
    var l=parseFloat(document.getElementById('d-len').value)||0,
        w=parseFloat(document.getElementById('d-wid').value)||0,
        bw=parseFloat(document.getElementById('d-bw').value)||140,
        gap=parseFloat(document.getElementById('d-gap').value)||5,
        js=parseFloat(document.getElementById('d-js').value)||450,
        price=parseFloat(document.getElementById('d-price').value)||0;
    if(!l||!w){document.getElementById('d-result').style.display='none';return;}
    var area=l*w;
    var boardSpacing=(bw+gap)/1000;
    var numBoards=Math.ceil(w/boardSpacing)+1;
    var joists=Math.ceil(l/(js/1000))+1;
    var screws=numBoards*joists*2;
    document.getElementById('d-area').textContent=area.toFixed(2)+' m²';
    document.getElementById('d-boards').textContent=numBoards+' boards × '+l+'m long';
    document.getElementById('d-joists').textContent=joists+' joists';
    document.getElementById('d-screws').textContent=screws+' screws (approx)';
    document.getElementById('d-cost').textContent=price?'$'+(numBoards*l*price).toFixed(2)+' (boards only)':'— (enter price above)';
    document.getElementById('d-result').style.display='';
  }
  </script>
---

## Decking Calculator for NZ Builders

Calculate the materials you need for any deck size — boards, joists, and fixings. Works for 90×19mm, 140×19mm, or any custom board size.

### Common NZ Decking Board Sizes

| Size | Board Width | Typical Use |
|---|---|---|
| 90×19mm | 90mm | Smaller decks, less wastage |
| 140×19mm | 140mm | Standard residential |
| 140×28mm | 140mm | Heavier commercial use |
| 90×45mm H4 | 90mm | Structural framing |

### Joist Spacing Rules (NZ)

- **19mm boards:** max 450mm joist spacing
- **28mm boards:** up to 600mm joist spacing
- **Always check NZ Building Code B1** for structural requirements

### Decking Timber Grades

In NZ, all ground-contact or external timber must be **H3.2 treated** (above ground, protected) or **H4 treated** (ground contact). Untreated timber will rot within 2–5 years.

### What Does a Deck Cost?

See our [deck building cost guide](/jobs/decking/) for typical NZ prices by city, or find a [local builder](/trades/builders/).
