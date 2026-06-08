self.addEventListener('install', function(e) {
e.waitUntil(
caches.open('projectsite-cache-v1').then(function(cache) {
return cache.addAll([
'/',
'/static/css/tabler.min.css',
'/static/js/tabler.min.js',
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