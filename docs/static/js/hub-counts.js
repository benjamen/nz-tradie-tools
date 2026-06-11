/**
 * hub-counts.js — replaces static city card counts on trade hub pages
 * with live counts from the TradieTools API.
 * Works on /trades/{trade-slug}/ pages only.
 */
(function () {
  const API = 'https://tradietools.optified.nz/api/method/tradietools.api.get_directory';

  const TRADE_MAP = {
    electricians: 'electrician', plumbers: 'plumber', builders: 'builder',
    painters: 'painter', roofers: 'roofer', landscapers: 'landscaper',
    tilers: 'tiler', plasterers: 'plasterer', concreters: 'concreter',
    gasfitters: 'gasfitter', 'heat-pump-installers': 'hvac',
    'hvac-engineers': 'hvac', 'carpet-layers': 'flooring',
    'timber-floor-specialists': 'flooring', 'cabinet-makers': 'other',
    carpenters: 'other', glaziers: 'other', fencers: 'other',
    'solar-installers': 'other', scaffolders: 'other',
    arborists: 'landscaper', 'bathroom-renovators': 'builder',
    'kitchen-renovators': 'builder', 'lighting-specialists': 'electrician',
    'asphalt-contractors': 'concreter', 'irrigation-specialists': 'landscaper',
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

  async function run() {
    const parts = location.pathname.replace(/\/$/, '').split('/').filter(Boolean);
    if (parts.length !== 2 || parts[0] !== 'trades') return;
    const trade = TRADE_MAP[parts[1]];
    if (!trade) return;

    const cards = Array.from(document.querySelectorAll('.card-grid .card'));
    if (!cards.length) return;

    await Promise.all(cards.map(async function(card) {
      const href = card.getAttribute('href') || '';
      const citySlug = href.replace(/\.html$/, '').split('/').pop();
      const region = CITY_MAP[citySlug];
      if (!region) return;

      try {
        const r = await fetch(API + '?trade=' + encodeURIComponent(trade) + '&region=' + encodeURIComponent(region) + '&limit=1&offset=0');
        if (!r.ok) return;
        const data = await r.json();
        const total = (data.message && data.message.total) || 0;
        if (total <= 0) return;

        const subtitle = card.querySelectorAll('p')[0];
        if (!subtitle) return;
        subtitle.style.color = '#0055a5';
        subtitle.innerHTML = region + ' &middot; <strong>' + total + '</strong> listed';
      } catch (e) { /* fail silently */ }
    }));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
