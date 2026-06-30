---
title: "Locksmith Cost Calculator — NZ"
seo_title: "Free NZ Locksmith Cost Calculator 2026 — Callout & Job Fees"
description: "Free NZ locksmith cost calculator — estimate callout fees, lockout costs and lock replacement prices for 2026. Business hours vs after-hours rates."
tags: [locksmith, lockout, lock replacement, rekey, calculator, NZ]
author: "NZ Tradie Tools"
layout: calculator
date: 2026-06-30
calculator_html: |
  <div class="calc-grid">
    <div class="calc-group"><label>Job type</label>
      <select id="lk-job" onchange="calcLocksmith()">
        <option value="lockout_home" selected>House lockout (locked out)</option>
        <option value="lockout_car">Car lockout</option>
        <option value="rekey">Rekey existing lock</option>
        <option value="replace_standard">Replace lock — standard</option>
        <option value="replace_deadbolt">Replace lock — deadbolt/deadlock</option>
        <option value="broken_key">Broken key extraction</option>
        <option value="safe">Safe opening</option>
      </select>
    </div>
    <div class="calc-group"><label>Time of call</label>
      <select id="lk-time" onchange="calcLocksmith()">
        <option value="business" selected>Business hours (8am–5pm weekdays)</option>
        <option value="evening">Evening (5pm–10pm / weekends)</option>
        <option value="afterhours">After hours (10pm–8am)</option>
      </select>
    </div>
    <div class="calc-group"><label>Number of locks</label>
      <select id="lk-qty" onchange="calcLocksmith()">
        <option value="1" selected>1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4+</option>
      </select>
    </div>
  </div>
  <div class="calc-result" id="lk-result" style="display:none">
    <h3>Locksmith Cost Estimate</h3>
    <div class="result-row"><span>Callout / travel fee</span><span id="lk-callout"></span></div>
    <div class="result-row"><span>Labour (estimated)</span><span id="lk-labour"></span></div>
    <div class="result-row"><span>Parts / materials</span><span id="lk-parts"></span></div>
    <div class="result-row"><span>Total estimate</span><span id="lk-total" class="result-highlight"></span></div>
    <p id="lk-note" style="font-size:.85rem;color:#555;margin-top:.75rem;line-height:1.5"></p>
  </div>
  <script>
  function nzd(n){return '$'+Math.round(n).toLocaleString();}
  function calcLocksmith(){
    var job=document.getElementById('lk-job').value;
    var time=document.getElementById('lk-time').value;
    var qty=parseInt(document.getElementById('lk-qty').value)||1;
    if(qty===4)qty=5; // estimate for 4+

    // Callout fees by time
    var callout={business:80,evening:120,afterhours:180}[time];

    // Job base rates (labour, single unit, business hours)
    var jobDef={
      lockout_home:    {labour:100, parts:0,   note:'Standard pin tumbler lock picked or bumped. Complex locks (Abloy, high-security) cost more.'},
      lockout_car:     {labour:90,  parts:0,   note:'Most modern cars can be opened without damage. Newer key-fob or push-button cars may need a specialist.'},
      rekey:           {labour:55,  parts:15,  note:'Rekeying changes the pin configuration so old keys no longer work. Cheaper than full replacement.'},
      replace_standard:{labour:60,  parts:60,  note:'Standard knob or lever lockset replaced — Gainsborough or equivalent. Smart locks are extra.'},
      replace_deadbolt:{labour:70,  parts:90,  note:'Deadbolt or deadlock replaced. Premium brands (Lockwood, Whitco) may cost more for parts.'},
      broken_key:      {labour:80,  parts:0,   note:'Broken key extracted from lock. If the lock is damaged during extraction, replacement may be needed.'},
      safe:            {labour:180, parts:0,   note:'Safe openings vary widely — combination reset may be cheaper than full drill-out. Get a quote first.'},
    };

    var base=jobDef[job];
    // After-hours labour multiplier
    var labourMult={business:1.0,evening:1.3,afterhours:1.6}[time];
    // Multi-unit discount (after first)
    var isMulti=(job==='rekey'||job==='replace_standard'||job==='replace_deadbolt');
    var labour=base.labour*labourMult+(isMulti&&qty>1?(qty-1)*base.labour*0.7*labourMult:0);
    var parts=base.parts*qty;
    var total=callout+labour+parts;

    document.getElementById('lk-callout').textContent=nzd(callout);
    document.getElementById('lk-labour').textContent=nzd(labour);
    document.getElementById('lk-parts').textContent=parts>0?nzd(parts):'Included / nil';
    document.getElementById('lk-total').textContent=nzd(total);
    document.getElementById('lk-note').textContent=base.note;
    document.getElementById('lk-result').style.display='block';
  }
  </script>

intro: |
  Estimate locksmith costs in NZ for common jobs — lockouts, rekeying and lock replacement. After-hours and weekend callouts are significantly more expensive; if you can wait until business hours, it's usually worth it.

faq:
  - q: "How much does a locksmith cost in NZ?"
    a: "A locksmith in NZ typically charges $80–$150 callout fee plus $80–$150/hour for labour, depending on time of day. A standard house lockout during business hours costs $150–$280 all up. After-hours jobs can be $300–$500+."
  - q: "How much is a locksmith callout fee in NZ?"
    a: "Locksmith callout fees in NZ range from $80–$120 during business hours to $150–$200+ after hours and on public holidays. This is charged on top of the job labour rate."
  - q: "Is it cheaper to rekey or replace a lock in NZ?"
    a: "Rekeying is almost always cheaper — typically $70–$120 per lock vs $150–$250+ to replace. Rekeying changes the pin configuration so old keys no longer work, which is ideal when you've moved house or lost keys."
  - q: "What does a locksmith charge to change locks after moving house?"
    a: "Changing or rekeying all locks after moving house in NZ typically costs $200–$500 depending on number of locks and whether you rekey or replace. Rekeying is the cheapest option if the existing locks are in good condition."
  - q: "Do locksmiths in NZ charge more on weekends?"
    a: "Yes — most NZ locksmiths charge 25–60% more for evening, weekend and after-hours callouts. Business hours (8am–5pm weekdays) are the cheapest time to call. Public holidays attract the highest rates."
---
