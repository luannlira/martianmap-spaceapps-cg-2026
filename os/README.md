# OS / distro

Lightweight survival operating system: simple to handle, works offline, designed for a small device. *Idea: Euler.*

## Status

- [x] **Prototype:** installable web app (PWA) that simulates the Survival OS interface ([`app/`](app))
- [ ] **Dedicated distro:** it is product vision, it does not exist yet
- [ ] [Lost Mode (*Modo Perdido*)](../docs/modo-perdido.md) (in Portuguese)

## What the prototype has

- Three screens, with tab navigation: **Mapa** (Map), **Guia** (Guide) and **Traje** (Suit)
- Real map of Mars (Mars Trek tiles) saved on the device
- Full-screen alert + vibration when a simulated sensor crosses its limit
- Offline operation (service worker) and installation as an app (manifest)
- Automatic light/dark theme, large touch targets

## Files

| File | Role |
|------|------|
| `app/index.html` | Screens, styles and logic (HTML + CSS + JS in a single file) |
| `app/sw.js` | Service worker, cache-first: stores the app and all the tiles |
| `app/manifest.webmanifest` | Name, icons and full-screen mode of the installed app |
| `app/vendor/` | Leaflet 1.9.4 (local, no CDN) |
| `app/icons/` | App icons |
| `app/assets/tiles/` | Mars Trek tiles + `lista.json` (the list of tile files) |

`app/assets/terreno.jpg` is not used by the app today (left over from an earlier version); it can be removed.

## How to run

From the **repository root**:

```bash
python -m http.server 8000
```

Open **http://localhost:8000/os/app/**. Do not open the file by double-clicking it: the service worker does not work on `file://`. Step by step and the offline test in [How to run](../README.md#how-to-run).

## How to work on it

- Changed any file in `app/`? **Increase `VERSAO` (the cache version) in `sw.js`**, otherwise anyone who has already opened the app sees the old version.
- For the logic, see the blocks in `index.html`: *Mapa* (Map), *Dados* (Data: `GUIAS`, `SENS`), *Abas* (Tabs), *Alertas* (Alerts), *Satélite/offline* (Satellite/offline).
- New map region: see [`../mapa/README.md`](../mapa/README.md).
- Fixed data uses `innerHTML`. If it ever comes from outside (suit, network), switch to `textContent`.

## From prototype to distro (vision)

1. Keep the app as the system interface.
2. Run it on a minimal Linux base on small hardware, opening straight into the app.
3. Measure power consumption and tune.

Details and decisions in [`../docs/arquitetura.md`](../docs/arquitetura.md) (in Portuguese).

## Limitations

- Telemetry, positions, route and guide are **examples**.
- The "Satélite" (Satellite) button only toggles a state on the screen.
- Keyboard accessibility is incomplete (focus trapped in the alert, arrow keys on the tabs).
- Never tested on small hardware or with gloves.
