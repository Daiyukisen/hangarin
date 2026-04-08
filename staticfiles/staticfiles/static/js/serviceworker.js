self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open('hangarin-cache-v1').then(function(cache) {
      return cache.addAll([
        '/',
        '/static/css/tabler.min.css',
        '/static/js/tabler.min.js',
        '/static/img/logo.png',
        '/static/img/logo2.png',
      ]);
    })
  );
});

self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});