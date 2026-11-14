/* Service worker do Martian Map.
 * Estratégia: cache-first. Na instalação guarda o app, o Leaflet, os ícones e TODOS os tiles
 * listados em assets/tiles/lista.json (gerado por mapa/baixar_tiles.py).
 * Ao mudar qualquer arquivo do app, aumente VERSAO para os aparelhos pegarem a atualização. */
const VERSAO = 'martianmap-v1';

const APP = [
  './',
  'index.html',
  'manifest.webmanifest',
  'vendor/leaflet.css',
  'vendor/leaflet.js',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/icon-maskable-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(VERSAO);
    await cache.addAll(APP);                       // o essencial: se falhar, a instalação falha
    try {                                          // os tiles: melhor esforço
      const lista = await (await fetch('assets/tiles/lista.json', { cache: 'no-cache' })).json();
      await cache.addAll(lista);
    } catch (e) { console.warn('SW: não consegui guardar os tiles', e); }
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== VERSAO) await caches.delete(k);
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  event.respondWith((async () => {
    const cache = await caches.open(VERSAO);
    const salvo = await cache.match(req, { ignoreSearch: true });
    if (salvo) return salvo;
    try {
      const res = await fetch(req);
      if (res.ok) cache.put(req, res.clone());
      return res;
    } catch (e) {
      if (req.mode === 'navigate') return cache.match('index.html');   // abriu offline em outra URL
      return new Response('', { status: 504, statusText: 'Offline' });
    }
  })());
});
