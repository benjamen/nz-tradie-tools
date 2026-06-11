/**
 * live-listings.js — injects self-listed TradieTools members into city+trade pages
 * Works by parsing the URL path: /trades/{trade-slug}/{city-slug}.html
 * Zero build-system dependency.
 */
(function () {
  const API = 'https://tradietools.optified.nz/api/method/tradietools.api.get_directory';
  const SIGNUP = '/signup';

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
    christchurch: 'Canterbury', hamilton: 'Waikato',
    tauranga: 'Bay of Plenty', dunedin: 'Otago',
    'palmerston-north': 'Manawatu-Whanganui', whanganui: 'Manawatu-Whanganui',
    napier: "Hawke's Bay", hastings: "Hawke's Bay",
    nelson: 'Nelson-Marlborough', 'new-plymouth': 'Taranaki',
    invercargill: 'Southland', queenstown: 'Otago',
    rotorua: 'Bay of Plenty', gisborne: 'Gisborne',
    'lower-hutt': 'Wellington', 'upper-hutt': 'Wellington',
    porirua: 'Wellington', blenheim: 'Nelson-Marlborough',
    timaru: 'Canterbury', 'kapiti-coast': 'Wellington',
  };

  const TRADE_LABEL = {
    electrician: 'Electrician', plumber: 'Plumber', builder: 'Builder / LBP',
    painter: 'Painter', roofer: 'Roofer', landscaper: 'Landscaper',
    tiler: 'Tiler', plasterer: 'Plasterer', concreter: 'Concreter',
    gasfitter: 'Gasfitter', hvac: 'HVAC / Heat Pump',
    flooring: 'Flooring Specialist', other: 'Tradie',
  };

  function parsePath() {
    const parts = location.pathname.replace(/\.html$/, '').split('/').filter(Boolean);
    // Expect: ['trades', '{trade-slug}', '{city-slug}']
    if (parts.length !== 3 || parts[0] !== 'trades') return null;
    const trade = TRADE_MAP[parts[1]];
    const region = CITY_MAP[parts[2]];
    if (!trade || !region) return null;
    return { trade, region, tradeSlug: parts[1], citySlug: parts[2] };
  }

  function esc(s) {
    return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function stars(r) {
    const n = Math.round(parseFloat(r) || 0);
    return '★'.repeat(n) + '☆'.repeat(5 - n);
  }

  function initials(name) {
    return (name || '?').trim().split(/\s+/).map(w => w[0]).join('').slice(0, 2).toUpperCase();
  }

  function cardHTML(t) {
    const label = TRADE_LABEL[t.trade] || 'Tradie';
    const phone = t.phone || '';
    const email = t.contact_email || '';
    const rate = t.hourly_rate ? `$${t.hourly_rate}/hr` : '';
    const exp = t.experience_years ? `${t.experience_years}yrs exp` : '';
    const rating = parseFloat(t.avg_rating || 0);

    return `<div style="background:#fff;padding:1.1rem 1.25rem;border-left:4px solid ${t.is_premium ? 'var(--orange,#c05600)' : 'var(--blue,#005ea2)'};border-bottom:1px solid var(--border-lt,#dcdcdc);display:flex;flex-direction:column;gap:.6rem">
      <div style="display:flex;align-items:flex-start;gap:.75rem">
        <div style="width:40px;height:40px;background:var(--navy,#1b2a4a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0">${esc(initials(t.name))}</div>
        <div style="flex:1;min-width:0">
          <div style="font-weight:700;font-size:.95rem;display:flex;align-items:center;gap:.4rem;flex-wrap:wrap">
            ${esc(t.name || 'Unknown')}
            ${t.is_verified ? '<span style="background:var(--blue,#005ea2);color:#fff;font-size:.68rem;font-weight:700;padding:.12rem .45rem;letter-spacing:.02em">✓ VERIFIED</span>' : ''}
            ${t.is_premium && !t.is_verified ? '<span style="background:var(--orange,#c05600);color:#fff;font-size:.68rem;font-weight:700;padding:.12rem .45rem">PREMIUM</span>' : ''}
          </div>
          <div style="font-size:.82rem;color:var(--blue,#005ea2);font-weight:600;margin-top:.1rem">${esc(label)}</div>
          ${rating > 0 ? `<div style="font-size:.82rem;color:#b45309;margin-top:.1rem">${stars(rating)} <span style="color:var(--muted,#5a5a5a)">${rating.toFixed(1)} (${t.review_count || 0} reviews)</span></div>` : ''}
          ${rate || exp ? `<div style="font-size:.8rem;color:var(--muted,#5a5a5a);margin-top:.1rem">${[exp, rate].filter(Boolean).join(' · ')}</div>` : ''}
        </div>
      </div>
      <div style="display:flex;gap:.5rem">
        ${phone ? `<button onclick="this.outerHTML='<a href=\\'tel:${esc(phone)}\\'style=\\'flex:1;background:var(--blue,#005ea2);color:#fff;padding:.5rem;font-size:.85rem;font-weight:700;text-align:center;text-decoration:none\\'>${esc(phone)}</a>'" style="flex:1;background:var(--blue,#005ea2);color:#fff;border:none;padding:.5rem;font-size:.85rem;font-weight:700;cursor:pointer;font-family:inherit;text-align:center">Show number</button>` : ''}
        ${email ? `<a href="mailto:${esc(email)}" style="flex:1;background:#fff;color:var(--blue,#005ea2);border:2px solid var(--blue,#005ea2);padding:.5rem;font-size:.85rem;font-weight:700;text-align:center;text-decoration:none">Email</a>` : ''}
        ${!phone && !email ? `<span style="font-size:.82rem;color:var(--muted,#5a5a5a);align-self:center">Contact details private</span>` : ''}
      </div>
    </div>`;
  }

  function inject(ctx, listings) {
    const tradeLabel = TRADE_LABEL[ctx.trade] || ctx.trade;
    const cityName = ctx.region.replace('-', ' ').replace(/\b\w/g, c => c.toUpperCase());

    let html;
    if (listings.length > 0) {
      html = `<div id="tt-live-section" style="margin-top:2rem">
        <h2 style="font-size:1.2rem;margin:0 0 .25rem;color:var(--navy,#1b2a4a)">Self-Listed ${tradeLabel}s in ${cityName}</h2>
        <p style="font-size:.85rem;color:var(--muted,#5a5a5a);margin-bottom:.75rem">These ${tradeLabel.toLowerCase()}s have listed directly on TradieTools. <a href="${SIGNUP}" style="color:var(--blue,#005ea2)">Add your business free →</a></p>
        <div style="border:1px solid var(--border,#b8b8b8)">
          ${listings.map(cardHTML).join('')}
        </div>
      </div>`;
    } else {
      html = `<div id="tt-live-section" style="margin-top:2rem;background:var(--bg,#f6f6f6);border-left:4px solid var(--orange,#c05600);padding:1rem 1.25rem">
        <strong>Are you a ${tradeLabel.toLowerCase()} in ${cityName}?</strong>
        List your business free on TradieTools and appear on this page.
        <a href="${SIGNUP}" style="display:inline-block;margin-top:.5rem;color:var(--blue,#005ea2);font-weight:600">Create free listing →</a>
      </div>`;
    }

    const main = document.querySelector('main');
    if (main) {
      main.insertAdjacentHTML('beforeend', html);
    }
  }

  async function run() {
    const ctx = parsePath();
    if (!ctx) return;

    try {
      const url = `${API}?trade=${encodeURIComponent(ctx.trade)}&region=${encodeURIComponent(ctx.region)}&limit=10`;
      const r = await fetch(url);
      if (!r.ok) return;
      const data = await r.json();
      const listings = data.message?.listings || [];
      inject(ctx, listings);
    } catch (e) {
      // Fail silently — never break the static page
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
