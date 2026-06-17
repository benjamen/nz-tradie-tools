/**
 * live-listings.js — injects self-listed TradieTools members into city+trade pages
 * Parses URL path: /trades/{trade-slug}/{city-slug}.html
 * Shows a "Show more businesses" button after the static top-10.
 * On click, loads live API results with prev/next pagination (5 per page).
 */
(function () {
  const API    = 'https://tradietools.optified.nz/api/method/tradietools.api.get_directory';
  const SIGNUP = '/signup';
  const PAGE_SIZE = 5;

  const TRADE_MAP = {
    electricians: 'electrician', plumbers: 'plumber', builders: 'builder',
    painters: 'painter', roofers: 'roofer', landscapers: 'landscaper',
    tilers: 'tiler', plasterers: 'plasterer', concreters: 'concreter',
    gasfitters: 'gasfitter', 'heat-pump-installers': 'hvac',
    'hvac-engineers': 'hvac', 'carpet-layers': 'flooring',
    'timber-floor-specialists': 'flooring', 'cabinet-makers': 'other',
    carpenters: 'other', glaziers: 'other', fencers: 'other',
    'solar-installers': 'other', scaffolders: 'other',
    'demolition-contractors': 'other', waterproofers: 'other',
    'pool-builders': 'other', stonemasons: 'other', bricklayers: 'other',
    'drainage-specialists': 'other', drainlayers: 'other',
    'insulation-installers': 'other', 'cladding-installers': 'other',
    excavators: 'other', arborists: 'landscaper',
    'pest-controllers': 'other', locksmiths: 'other',
    'security-system-installers': 'other', surveyors: 'other',
    'quantity-surveyors': 'other', 'steel-fabricators': 'other',
    'asphalt-contractors': 'concreter', 'irrigation-specialists': 'landscaper',
    'lighting-specialists': 'electrician', 'interior-designers': 'other',
    'window-installers': 'other', 'bathroom-renovators': 'builder',
    'kitchen-renovators': 'builder', 'garage-door-installers': 'other',
    'commercial-cleaners': 'other', architects: 'other',
  };

  const CITY_MAP = {
    auckland: 'Auckland', wellington: 'Wellington',
    christchurch: 'Christchurch', hamilton: 'Hamilton',
    tauranga: 'Tauranga', dunedin: 'Dunedin',
    'palmerston-north': 'Palmerston North', whanganui: 'Whanganui',
    napier: 'Napier', hastings: 'Napier',
    nelson: 'Nelson', 'new-plymouth': 'New Plymouth',
    invercargill: 'Invercargill', queenstown: 'Queenstown',
    rotorua: 'Rotorua', gisborne: 'Gisborne',
    'lower-hutt': 'Wellington', 'upper-hutt': 'Wellington',
    porirua: 'Wellington', blenheim: 'Nelson',
    timaru: 'Christchurch', 'kapiti-coast': 'Wellington',
    whangarei: 'Whangarei',
  };

  const TRADE_LABEL = {
    electrician: 'Electrician', plumber: 'Plumber', builder: 'Builder / LBP',
    painter: 'Painter', roofer: 'Roofer', landscaper: 'Landscaper',
    tiler: 'Tiler', plasterer: 'Plasterer', concreter: 'Concreter',
    gasfitter: 'Gasfitter', hvac: 'HVAC / Heat Pump',
    flooring: 'Flooring Specialist', other: 'Tradie',
  };

  const TRADE_AVATAR_BG = {
    electrician: '#b45309', plumber: '#0369a1', builder: '#1e3a5f',
    painter: '#7c3aed', roofer: '#374151', landscaper: '#166534',
    hvac: '#0e7490', gasfitter: '#9a3412',
  };

  function parsePath() {
    const parts = location.pathname.replace(/\.html$/, '').split('/').filter(Boolean);
    if (parts.length !== 3 || parts[0] !== 'trades') return null;
    const trade  = TRADE_MAP[parts[1]];
    const region = CITY_MAP[parts[2]];
    if (!trade || !region) return null;
    return { trade, region, tradeSlug: parts[1], citySlug: parts[2] };
  }

  function esc(s) {
    return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function stars(r) {
    const n = Math.round(parseFloat(r) || 0);
    return '★'.repeat(n) + '☆'.repeat(5 - n);
  }

  function initials(name) {
    return (name || '?').trim().split(/\s+/).map(w => w[0]).join('').slice(0, 2).toUpperCase();
  }

  function cardHTML(t) {
    const label  = TRADE_LABEL[t.trade] || 'Tradie';
    const phone  = t.phone || '';
    const rate   = t.hourly_rate ? `$${t.hourly_rate}/hr` : '';
    const exp    = t.experience_years ? `${t.experience_years}yrs exp` : '';
    const rating = parseFloat(t.avg_rating || 0);
    const avatarBg = TRADE_AVATAR_BG[t.trade] || '#1b2a4a';
    const accentColor = t.is_premium ? '#c05600' : t.is_verified ? '#2563eb' : '#1b2a4a';
    const location = [t.suburb, t.region].filter(Boolean).join(' · ');

    const avatarEl = t.profile_photo_url
      ? `<img src="https://tradietools.optified.nz${esc(t.profile_photo_url)}" alt="${esc(t.name)}" style="width:48px;height:48px;object-fit:cover;border-radius:3px;flex-shrink:0">`
      : `<div style="width:48px;height:48px;background:${avatarBg};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1rem;flex-shrink:0;border-radius:3px">${esc(initials(t.name))}</div>`;

    const nameBadges = [
      t.is_verified ? `<span style="background:#2563eb;color:#fff;font-size:.68rem;font-weight:700;padding:.15rem .5rem;letter-spacing:.03em;border-radius:2px">✓ VERIFIED</span>` : '',
      t.is_premium && !t.is_verified ? `<span style="background:#c05600;color:#fff;font-size:.68rem;font-weight:700;padding:.15rem .5rem;border-radius:2px">PRO</span>` : '',
      t.top_tradie_badge ? `<span style="background:#7c3aed;color:#fff;font-size:.65rem;font-weight:700;padding:.15rem .5rem;border-radius:2px">🏆 TOP</span>` : '',
    ].join('');

    const metaRow = (rate || exp)
      ? `<div style="display:flex;gap:.6rem;flex-wrap:wrap;font-size:.82rem;margin-top:.2rem">
           ${exp ? `<span style="color:#5a5a5a">${esc(exp)}</span>` : ''}
           ${rate ? `<span style="color:#1b1b1b;font-weight:700">${esc(rate)}</span>` : ''}
         </div>` : '';

    const ratingRow = rating > 0
      ? `<div style="font-size:.82rem;color:#b45309;margin-top:.2rem">${stars(rating)} <span style="color:#5a5a5a">${rating.toFixed(1)} (${t.review_count || 0} reviews)</span></div>`
      : '';

    const platformBadges = (t.nocowboys_rating || t.builderscrack_rating || t.google_rating)
      ? `<div style="font-size:.72rem;color:#4a5568;margin-top:.3rem;display:flex;gap:.35rem;flex-wrap:wrap">
           ${t.nocowboys_rating ? `<span style="background:#f0fdf4;border:1px solid #bbf7d0;padding:.1rem .4rem;border-radius:3px">NC ⭐ ${parseFloat(t.nocowboys_rating).toFixed(1)}</span>` : ''}
           ${t.builderscrack_rating ? `<span style="background:#fff7ed;border:1px solid #fed7aa;padding:.1rem .4rem;border-radius:3px">BC ⭐ ${parseFloat(t.builderscrack_rating).toFixed(1)}</span>` : ''}
           ${t.google_rating ? `<span style="background:#eff6ff;border:1px solid #bfdbfe;padding:.1rem .4rem;border-radius:3px">G ⭐ ${parseFloat(t.google_rating).toFixed(1)}</span>` : ''}
         </div>` : '';

    const isFree = !t.is_verified && !t.is_premium;
    const lockedPhoneEl = isFree && phone
      ? `<div style="font-size:.8rem;color:#5a5a5a;margin-top:.1rem">🔒 Phone hidden · <a href="/signup/?upgrade=verified" style="color:#c05600;font-weight:600;text-decoration:none">Show number from $29/mo →</a></div>`
      : '';

    let actionsEl;
    if (isFree) {
      actionsEl = `<button onclick="if(typeof ttQuote==='function')ttQuote('${esc(String(t.id||''))}','${esc(t.name||'')}','${esc(label)}','${esc(t.region||'')}')" style="width:100%;background:#1b2a4a;color:#fff;border:none;padding:.6rem;font-size:.9rem;font-weight:700;cursor:pointer;font-family:inherit;text-align:center;border-radius:2px;margin-top:.25rem">Get a Quote</button>`;
    } else {
      const phoneBtn = phone
        ? `<button onclick="this.outerHTML='<a href=\\'tel:${esc(phone)}\\'style=\\'flex:1;background:#2563eb;color:#fff;padding:.6rem;font-size:.88rem;font-weight:700;text-align:center;text-decoration:none;border-radius:2px\\'>📞 ${esc(phone)}</a>'" style="flex:1;background:#2563eb;color:#fff;border:none;padding:.6rem;font-size:.88rem;font-weight:700;cursor:pointer;font-family:inherit;text-align:center;border-radius:2px">📞 Show number</button>` : '';
      const quoteBtn = `<button onclick="if(typeof ttQuote==='function')ttQuote('${esc(String(t.id||''))}','${esc(t.name||'')}','${esc(label)}','${esc(t.region||'')}')" style="flex:1;background:#1b2a4a;color:#fff;border:none;padding:.6rem;font-size:.88rem;font-weight:700;cursor:pointer;font-family:inherit;text-align:center;border-radius:2px">Get a Quote</button>`;
      actionsEl = `<div style="display:flex;gap:.5rem;margin-top:.25rem">${phoneBtn}${quoteBtn}</div>`;
    }

    return `<div style="background:#fff;padding:1.1rem 1.25rem;border-left:5px solid ${accentColor};border-bottom:1px solid #dcdcdc;display:flex;flex-direction:column;gap:.5rem">
      <div style="display:flex;align-items:flex-start;gap:.85rem">
        ${avatarEl}
        <div style="flex:1;min-width:0">
          <div style="font-weight:700;font-size:1rem;display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;color:#1b1b1b">
            ${esc(t.name || 'Unknown')}${nameBadges}
          </div>
          <div style="font-size:.85rem;color:#005ea2;font-weight:600;margin-top:.05rem">${esc(label)}</div>
          ${location ? `<div style="font-size:.82rem;color:#5a5a5a;margin-top:.05rem">${esc(location)}</div>` : ''}
        </div>
      </div>
      ${metaRow}
      ${ratingRow}
      ${platformBadges}
      ${lockedPhoneEl}
      ${actionsEl}
    </div>`;
  }

  function paginationHTML(page, totalPages) {
    const prev = page > 1
      ? `<button onclick="ttPage(${page - 1})" style="background:var(--navy,#1b2a4a);color:#fff;border:none;padding:.45rem 1rem;font-size:.85rem;font-weight:700;cursor:pointer;font-family:inherit">← Previous</button>`
      : `<button disabled style="opacity:.3;background:var(--navy,#1b2a4a);color:#fff;border:none;padding:.45rem 1rem;font-size:.85rem;font-weight:700;font-family:inherit;cursor:default">← Previous</button>`;
    const next = page < totalPages
      ? `<button onclick="ttPage(${page + 1})" style="background:var(--navy,#1b2a4a);color:#fff;border:none;padding:.45rem 1rem;font-size:.85rem;font-weight:700;cursor:pointer;font-family:inherit">Next →</button>`
      : `<button disabled style="opacity:.3;background:var(--navy,#1b2a4a);color:#fff;border:none;padding:.45rem 1rem;font-size:.85rem;font-weight:700;font-family:inherit;cursor:default">Next →</button>`;
    return `<div style="display:flex;justify-content:space-between;align-items:center;padding:.75rem 0;font-size:.82rem;color:var(--muted,#5a5a5a)">
      ${prev}
      <span>Page ${page} of ${totalPages}</span>
      ${next}
    </div>`;
  }

  let _ctx = null;
  let _total = 0;

  window.ttPage = async function(page) {
    if (!_ctx) return;
    const section = document.getElementById('tt-live-section');
    if (!section) return;

    const listDiv = section.querySelector('#tt-list');
    const pagDiv  = section.querySelector('#tt-pagination');
    if (listDiv) listDiv.innerHTML = '<div style="padding:1rem;color:var(--muted,#5a5a5a);font-size:.88rem">Loading…</div>';

    const offset = (page - 1) * PAGE_SIZE;
    try {
      const r = await fetch(`${API}?trade=${encodeURIComponent(_ctx.trade)}&region=${encodeURIComponent(_ctx.region)}&limit=${PAGE_SIZE}&offset=${offset}`);
      if (!r.ok) return;
      const data = await r.json();
      const listings = data.message?.listings || [];
      _total = data.message?.total || _total;
      const totalPages = Math.ceil(_total / PAGE_SIZE);

      if (listDiv) listDiv.innerHTML = listings.length
        ? listings.map(cardHTML).join('')
        : '<div style="padding:1rem;color:var(--muted,#5a5a5a);font-size:.88rem">No more results.</div>';

      if (pagDiv) pagDiv.innerHTML = paginationHTML(page, totalPages);

      section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch(e) {
      if (listDiv) listDiv.innerHTML = '<div style="padding:1rem;color:#dc2626;font-size:.88rem">Could not load results — please try again.</div>';
    }
  };

  function injectShowMore(ctx, total, firstPageListings) {
    const tradeLabel  = TRADE_LABEL[ctx.trade] || ctx.trade;
    const totalPages  = Math.ceil(total / PAGE_SIZE);
    _ctx   = ctx;
    _total = total;

    const listingsHTML = firstPageListings.map(cardHTML).join('');

    const html = `<div id="tt-live-section" style="margin-top:2rem">
      <h2 style="font-size:1.2rem;margin:0 0 .25rem;color:var(--navy,#1b2a4a)">More ${tradeLabel}s in ${ctx.region}</h2>
      <p style="font-size:.85rem;color:var(--muted,#5a5a5a);margin-bottom:.75rem">${total} business${total !== 1 ? 'es' : ''} listed directly on TradieTools. <a href="${SIGNUP}" style="color:var(--blue,#005ea2)">Add your business free →</a></p>
      <div id="tt-list" style="border:1px solid var(--border,#b8b8b8)">${listingsHTML}</div>
      <div id="tt-pagination">${totalPages > 1 ? paginationHTML(1, totalPages) : ''}</div>
    </div>`;

    const cta = document.getElementById('tt-get-listed-cta');
    if (cta) {
      cta.insertAdjacentHTML('beforebegin', html);
    } else {
      const main = document.querySelector('main');
      if (main) main.insertAdjacentHTML('beforeend', html);
    }
  }

  function injectCTA(ctx) {
    // No results — the template CTA already handles "get listed free", nothing extra needed
  }

  async function run() {
    const ctx = parsePath();
    if (!ctx) return;

    try {
      const url = `${API}?trade=${encodeURIComponent(ctx.trade)}&region=${encodeURIComponent(ctx.region)}&limit=${PAGE_SIZE}&offset=0`;
      const r = await fetch(url);
      if (!r.ok) return;
      const data = await r.json();
      const listings = data.message?.listings || [];
      const total    = data.message?.total    || 0;
      if (total > 0) injectShowMore(ctx, total, listings);
      // if 0 results, the template "Get listed free" CTA is already on the page
    } catch(e) { /* fail silently */ }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
