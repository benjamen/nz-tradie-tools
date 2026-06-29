(function () {
  if (!window.HUB_DATA) return;
  var tradeSlug = window.HUB_DATA.tradeSlug;
  var cityRegions = window.HUB_DATA.cityRegions; // { "auckland": "Auckland", "christchurch": "Canterbury", ... }

  // API uses singular trade values; strip trailing 's' for most NZ trades
  var apiTrade = tradeSlug.replace(/ers$/, 'er').replace(/ors$/, 'or').replace(/ers$/, 'er').replace(/s$/, '');

  // Build reverse map: lowercase region → city slug(s)
  var regionToCity = {};
  Object.keys(cityRegions).forEach(function (slug) {
    var region = (cityRegions[slug] || '').toLowerCase();
    if (!regionToCity[region]) regionToCity[region] = [];
    regionToCity[region].push(slug);
  });

  var API = 'https://tradietools.optified.nz/api/method/tradietools.api.search_listings';
  fetch(API + '?trade=' + encodeURIComponent(apiTrade) + '&limit=9999')
    .then(function (r) { return r.json(); })
    .then(function (json) {
      var listings = Array.isArray(json) ? json : (json.message || []);
      if (!Array.isArray(listings)) return;

      // Count per city slug
      var counts = {};
      listings.forEach(function (t) {
        var region = (t.region || '').toLowerCase();
        var slugs = regionToCity[region] || [];
        // Also try matching by city/suburb name directly
        if (!slugs.length) {
          var suburb = (t.suburb || '').toLowerCase();
          slugs = regionToCity[suburb] || [];
        }
        slugs.forEach(function (s) {
          counts[s] = (counts[s] || 0) + 1;
        });
      });

      // Update city card count spans
      document.querySelectorAll('[data-city]').forEach(function (el) {
        var city = el.getAttribute('data-city');
        var n = counts[city];
        var span = el.querySelector('.city-count');
        if (span && n) span.textContent = n + ' listed';
      });
    })
    .catch(function () {});
})();
