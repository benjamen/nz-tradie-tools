/**
 * quote-form.js — "Get a Quote" modal shared by /find/ and city+trade pages
 * Exposes: window.ttQuote(tradieId, tradieName, tradeLabel, regionHint)
 */
(function () {
  const API = 'https://tradietools.optified.nz/api/method/tradietools.api.submit_lead';

  function esc(s) {
    return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function friendlyError(raw) {
    const msg = String(raw).replace(/^[\w.]+Error:\s*/i,'').replace(/^frappe\.\w+\.\w+:\s*/i,'').trim();
    const MAP = {
      'missing required': 'Please fill in all required fields.',
      'invalid email':    'Please enter a valid email address.',
      'tradie not found': 'This listing is no longer available.',
    };
    const lower = msg.toLowerCase();
    for (const [k, v] of Object.entries(MAP)) { if (lower.includes(k)) return v; }
    if (msg.includes('frappe') || msg.includes('Traceback')) return 'Something went wrong. Please try again.';
    return msg;
  }

  function buildModal() {
    if (document.getElementById('tt-quote-modal')) return;

    const el = document.createElement('div');
    el.id = 'tt-quote-modal';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-modal', 'true');
    el.style.cssText = 'display:none;position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.55);overflow-y:auto;padding:2rem 1rem';

    el.innerHTML = `
      <div id="tt-quote-inner" style="background:#fff;max-width:520px;margin:0 auto;padding:2rem;position:relative;font-family:var(--font,'Public Sans',system-ui,sans-serif)">
        <button id="tt-quote-close" aria-label="Close" style="position:absolute;top:.75rem;right:.85rem;background:none;border:none;font-size:1.4rem;cursor:pointer;color:#5a5a5a;line-height:1">×</button>

        <div id="tt-quote-form-area">
          <h2 id="tt-quote-title" style="font-size:1.25rem;margin:0 0 .2rem;color:var(--navy,#1b2a4a)">Get a Quote</h2>
          <p id="tt-quote-sub" style="font-size:.88rem;color:var(--muted,#5a5a5a);margin:0 0 1.5rem">Fill in the details below and we'll connect you within 24 hours.</p>

          <div id="tt-quote-alert" style="display:none;padding:.7rem 1rem;font-size:.88rem;margin-bottom:1rem;background:#fef2f2;border-left:4px solid #dc2626;color:#7f1d1d"></div>

          <div style="display:flex;flex-direction:column;gap:.9rem">
            <div>
              <label style="font-size:.82rem;font-weight:700;color:var(--text,#1b1b1b);display:block;margin-bottom:.3rem">Describe the job <span style="color:#dc2626">*</span></label>
              <textarea id="tt-job-desc" rows="3" placeholder="e.g. Rewire switchboard and install 3 new circuits in a 3-bedroom house" style="width:100%;border:1px solid var(--border,#b8b8b8);padding:.6rem .85rem;font-size:.92rem;font-family:inherit;resize:vertical;box-sizing:border-box"></textarea>
            </div>

            <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
              <div>
                <label style="font-size:.82rem;font-weight:700;color:var(--text,#1b1b1b);display:block;margin-bottom:.3rem">When do you need it? <span style="color:#dc2626">*</span></label>
                <select id="tt-timeline" style="width:100%;border:1px solid var(--border,#b8b8b8);padding:.6rem .85rem;font-size:.92rem;font-family:inherit;background:#fff;box-sizing:border-box">
                  <option value="asap">As soon as possible</option>
                  <option value="this_week">This week</option>
                  <option value="this_month">This month</option>
                  <option value="getting_quotes" selected>Just getting quotes</option>
                </select>
              </div>
              <div>
                <label style="font-size:.82rem;font-weight:700;color:var(--text,#1b1b1b);display:block;margin-bottom:.3rem">Your suburb <span style="font-weight:400;color:var(--muted,#5a5a5a)">(optional)</span></label>
                <input id="tt-suburb" type="text" placeholder="e.g. Ponsonby" style="width:100%;border:1px solid var(--border,#b8b8b8);padding:.6rem .85rem;font-size:.92rem;font-family:inherit;box-sizing:border-box">
              </div>
            </div>

            <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
              <div>
                <label style="font-size:.82rem;font-weight:700;color:var(--text,#1b1b1b);display:block;margin-bottom:.3rem">Your name <span style="color:#dc2626">*</span></label>
                <input id="tt-cust-name" type="text" placeholder="Jane Smith" autocomplete="name" style="width:100%;border:1px solid var(--border,#b8b8b8);padding:.6rem .85rem;font-size:.92rem;font-family:inherit;box-sizing:border-box">
              </div>
              <div>
                <label style="font-size:.82rem;font-weight:700;color:var(--text,#1b1b1b);display:block;margin-bottom:.3rem">Your phone <span style="font-weight:400;color:var(--muted,#5a5a5a)">(optional)</span></label>
                <input id="tt-cust-phone" type="tel" placeholder="027 123 4567" autocomplete="tel" style="width:100%;border:1px solid var(--border,#b8b8b8);padding:.6rem .85rem;font-size:.92rem;font-family:inherit;box-sizing:border-box">
              </div>
            </div>

            <div>
              <label style="font-size:.82rem;font-weight:700;color:var(--text,#1b1b1b);display:block;margin-bottom:.3rem">Your email <span style="color:#dc2626">*</span></label>
              <input id="tt-cust-email" type="email" placeholder="you@example.com" autocomplete="email" style="width:100%;border:1px solid var(--border,#b8b8b8);padding:.6rem .85rem;font-size:.92rem;font-family:inherit;box-sizing:border-box">
            </div>
          </div>

          <button id="tt-quote-submit" style="width:100%;background:var(--navy,#1b2a4a);color:#fff;border:none;padding:.85rem;font-size:1rem;font-weight:700;font-family:inherit;cursor:pointer;margin-top:1.25rem;transition:background .15s">Send Enquiry</button>
          <p style="font-size:.75rem;color:var(--muted,#5a5a5a);text-align:center;margin:.6rem 0 0">We pass your details directly to the tradie. No spam.</p>
        </div>

        <div id="tt-quote-success" style="display:none;text-align:center;padding:1.5rem 0">
          <div style="width:52px;height:52px;background:#dcfce7;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto .75rem;font-size:1.5rem">✓</div>
          <h3 id="tt-success-msg" style="font-size:1.2rem;color:var(--navy,#1b2a4a);margin:0 0 .4rem">Enquiry sent!</h3>
          <p style="color:var(--muted,#5a5a5a);font-size:.9rem;margin:0 0 1.25rem">The tradie will be in touch within 24 hours. We've sent you a confirmation email.</p>
          <button onclick="ttQuoteClose()" style="background:var(--navy,#1b2a4a);color:#fff;border:none;padding:.65rem 1.5rem;font-weight:700;font-family:inherit;cursor:pointer;font-size:.9rem">Close</button>
        </div>
      </div>
    `;

    document.body.appendChild(el);

    document.getElementById('tt-quote-close').addEventListener('click', ttQuoteClose);
    el.addEventListener('click', function(e) { if (e.target === el) ttQuoteClose(); });

    document.getElementById('tt-quote-submit').addEventListener('click', async function() {
      const btn       = this;
      const alertEl   = document.getElementById('tt-quote-alert');
      const desc      = document.getElementById('tt-job-desc').value.trim();
      const timeline  = document.getElementById('tt-timeline').value;
      const suburb    = document.getElementById('tt-suburb').value.trim();
      const custName  = document.getElementById('tt-cust-name').value.trim();
      const custPhone = document.getElementById('tt-cust-phone').value.trim();
      const custEmail = document.getElementById('tt-cust-email').value.trim();

      alertEl.style.display = 'none';

      if (!desc || !custName || !custEmail) {
        alertEl.textContent = 'Please fill in the job description, your name, and your email.';
        alertEl.style.display = 'block';
        return;
      }

      btn.disabled = true;
      btn.textContent = 'Sending…';

      try {
        const r = await fetch(API, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-Frappe-CSRF-Token': 'fetch' },
          body: JSON.stringify({
            tradie_id: el.dataset.tradieId,
            customer_name: custName,
            customer_email: custEmail,
            job_description: desc,
            customer_phone: custPhone || null,
            job_timeline: timeline,
            suburb: suburb || null,
          })
        });
        const data = await r.json();
        const msg  = data.message || data;

        if (r.ok && (msg.status === 'received' || typeof msg === 'object')) {
          document.getElementById('tt-quote-form-area').style.display = 'none';
          const successEl = document.getElementById('tt-quote-success');
          successEl.style.display = 'block';
          document.getElementById('tt-success-msg').textContent =
            'Enquiry sent to ' + (el.dataset.tradieName || 'the tradie') + '!';
        } else {
          const raw = msg.exception || msg.message || 'Submission failed';
          throw new Error(friendlyError(raw));
        }
      } catch(err) {
        alertEl.textContent = err.message || 'Something went wrong. Please try again.';
        alertEl.style.display = 'block';
        btn.disabled = false;
        btn.textContent = 'Send Enquiry';
      }
    });
  }

  window.ttQuoteClose = function() {
    const el = document.getElementById('tt-quote-modal');
    if (!el) return;
    el.style.display = 'none';
    document.body.style.overflow = '';
    // Reset for next open
    document.getElementById('tt-quote-form-area').style.display = 'block';
    document.getElementById('tt-quote-success').style.display = 'none';
    document.getElementById('tt-quote-alert').style.display = 'none';
    const btn = document.getElementById('tt-quote-submit');
    btn.disabled = false;
    btn.textContent = 'Send Enquiry';
    ['tt-job-desc','tt-suburb','tt-cust-name','tt-cust-phone','tt-cust-email'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.value = '';
    });
    document.getElementById('tt-timeline').value = 'getting_quotes';
  };

  window.ttQuote = function(tradieId, tradieName, tradeLabel, regionHint) {
    buildModal();
    const el = document.getElementById('tt-quote-modal');
    el.dataset.tradieId   = tradieId   || '';
    el.dataset.tradieName = tradieName || '';

    document.getElementById('tt-quote-title').textContent =
      'Get a Quote from ' + (tradieName || 'this tradie');
    document.getElementById('tt-quote-sub').textContent =
      'Fill in the details below and ' + (tradieName || 'the tradie') + ' will be in touch within 24 hours.';

    if (regionHint) {
      const suburbInput = document.getElementById('tt-suburb');
      if (suburbInput && !suburbInput.value) suburbInput.placeholder = 'e.g. ' + regionHint;
    }

    el.style.display = 'block';
    document.body.style.overflow = 'hidden';
    setTimeout(() => { const d = document.getElementById('tt-job-desc'); if (d) d.focus(); }, 100);
  };

  // Close on Escape
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      const el = document.getElementById('tt-quote-modal');
      if (el && el.style.display !== 'none') ttQuoteClose();
    }
  });
})();
