# Martian Map — Survival OS *(Segunda chance de Sobreviver — "Second chance to survive")*

> NASA Space Apps Challenge 2026 · Campina Grande
> **Challenge:** Interplanetary Survival Guide: Martian Map

> **Language note:** the app interface and the documents in `docs/` are in Portuguese. In this README, interface labels are kept exactly as they appear in the app, with a translation in parentheses the first time they are mentioned.

## The idea

A **lightweight operating system (distro)**, designed as a **second lifeline** for explorers on Mars. It runs on a small device (or a larger one, if it needs to be compatible with the spacesuits), **easy to handle**, and brings together:

- an **offline survival guide**;
- access to a **network guided by satellites orbiting Mars**, to **map the area** and point out **safe places** to move to;
- integration with the **spacesuit**, which identifies **critical situations**;
- **long battery life** as a requirement (goal: weeks without recharging, like old-style mobile phones).

> **What exists today:** a prototype in the form of an **installable web app (PWA)** that simulates the Survival OS interface, with a real map of Mars (NASA data) saved on the device. The distro, the hardware, and the integration with real satellites and a real suit are the **product vision** and are not part of the prototype. See [Prototype scope](#prototype-scope).

## Modules

| Module | What it is | Folder | Status |
|--------|------------|--------|--------|
| OS / distro | Lightweight, easy-to-use system that runs on the device | [`os/`](os) | Web prototype (PWA) ready; the distro is a concept |
| Survival guide | Offline content: procedures, emergencies, checklists | [`guia-sobrevivencia/`](guia-sobrevivencia) | 5 example checklists (content to be validated) |
| Map and navigation | Area mapping and safe locations via satellites | [`mapa/`](mapa) | Offline map with real NASA tiles; example route |
| Smart suit | Critical-situation detection and alerts | [`traje/`](traje) | **Simulated** telemetry, 4 sensors and alerts |
| Hardware and power | Device, form factor, battery, requirements | [`hardware/`](hardware) | To be defined |

## Requirements (goals)

- [x] Easy to handle, including with gloves/suit *(prototype: touch targets of 44 to 72 px; not yet tested with real gloves)*
- [x] Work offline *(interface, guide and map are saved on the device by the service worker)*
- [ ] Sync when there is a link to the satellites *(today the "Satélite" (Satellite) button only simulates the state; there is no real sync)*
- [ ] Run on a small device with few resources *(the whole app is about 6 MB, but it has not been tested on real hardware yet)*
- [ ] Long battery life *(a hardware requirement, not yet validated)*
- [x] Alert quickly in critical situations *(prototype: full-screen alert + vibration, with simulated telemetry)*

## Prototype scope

> What we delivered at the hackathon: a demonstration of how Survival OS works, as an installable web app.

**Included and working**

- [x] **App that simulates the OS interface**: Mapa (Map), Guia (Guide) and Traje (Suit) screens, designed for use with gloves and on a small device
- [x] **PWA with offline operation**: interface, guide and map saved on the device (service worker + manifest)
- [x] **Real map of Mars**: NASA/JPL Mars Trek tiles downloaded beforehand and served locally, with zoom and markers
- [x] **Suit alerts (simulated)**: 4 sensors; when a limit is crossed, it opens the alert with vibration, a route to the shelter and the right checklist
- [x] **Offline survival guide**: 5 checkable checklists
- [x] **Distance calculated with the radius of Mars** (3,389.5 km)

**Simulated or example data (not from real data)**

- Suit telemetry (sliders), the displayed battery %, the "Satélite" button
- Positions of "Você" (You) and the shelter, the risk zone and the route
- Guide procedures (written by the team, **not official NASA procedures**)

**Out of scope for the prototype**

- Linux distro, hardware and battery, real satellite network and real suit
- Route calculated from slope (the tiles are images, not elevation data)

## Data used

| Data | Source (NASA / partner agency) | Link |
|------|--------------------------------|------|
| Mars terrain map: color mosaic, ~232 m/pixel, layer `Mars_Viking_MDIM21_ClrMosaic_global_232m`. Region 13–23°N, 72–82°E (~590 × 560 km), zoom 0–7, 107 tiles (~6 MB) | NASA/JPL — **Mars Trek** (WMTS tile service) | [trek.nasa.gov/mars](https://trek.nasa.gov/mars/) · [layer catalog](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars) |

The tiles are downloaded **once**, with [`mapa/baixar_tiles.py`](mapa/baixar_tiles.py), and stored in `os/app/assets/tiles/`. The app **does not query NASA at runtime**, which is why it works offline. The attribution appears in the corner of the map. Check the terms of use of each product on the Mars Trek page before redistributing.

**Third-party dependency:** [Leaflet](https://leafletjs.com) 1.9.4 (BSD-2-Clause license), stored in `os/app/vendor/` so it works without internet.

Details on each dataset in [`data/`](data).

## How to run

**Prerequisites:** Python 3 (used only for the local server and for downloading tiles) and a modern browser (tested on Chrome).

```bash
git clone https://github.com/luannlira/martianmap-spaceapps-cg-2026.git
cd martianmap-spaceapps-cg-2026
python -m http.server 8000      # on Linux/Mac it may be python3; on Windows, py -m http.server 8000
```

Open **http://localhost:8000/os/app/** in your browser.

> Run the server **from the repository root** and keep the terminal open. Do not open `index.html` by double-clicking it: the service worker does not work on `file://` and the map will not load the tiles.

**Test the main flow**

1. **Traje** (Suit) tab → drag *Reserva de O₂* (O₂ reserve) below 20%.
2. In the alert, tap **Ver rota até o abrigo** (View route to the shelter) (the route appears on the Mapa tab) or **Abrir checklist** (Open checklist).
3. Bring the O₂ back to normal: the route disappears.

**Test offline mode**

1. With the app open, wait a moment (the service worker saves everything on the first visit).
2. In F12 → *Application* → *Cache Storage*, check the stored files (8 from the app + 107 tiles).
3. Stop the server (Ctrl+C) and reload the page: the app, the map and the guide still open.

**Install as an app**: in Chrome, use the install icon in the address bar.

**Changed any app file?** Increase `VERSAO` (the cache version) in `os/app/sw.js`; otherwise anyone who has already opened the app keeps seeing the old version.

**Download another region or layer**: see [`mapa/README.md`](mapa/README.md).

## Repository structure

```
.
|-- README.md
|-- LICENSE
|-- .gitignore
|-- .github/
|   `-- pull_request_template.md
|-- docs/                  # overview, architecture, pitch and images (in Portuguese)
|-- os/                    # operating system / distro
|   `-- app/               # prototype: Survival OS interface (PWA)
|       |-- index.html     # screens, styles and logic
|       |-- sw.js          # service worker (offline cache)
|       |-- manifest.webmanifest
|       |-- icons/
|       |-- vendor/        # Leaflet (third-party)
|       `-- assets/tiles/  # Mars Trek tiles + lista.json
|-- guia-sobrevivencia/    # offline guide content
|-- mapa/                  # map, navigation and safe locations
|   `-- baixar_tiles.py    # downloads the NASA tiles
|-- traje/                 # critical-situation detection
|-- hardware/              # device, battery and requirements
`-- data/                  # data sources and documentation
```

## Technologies

Plain HTML, CSS and JavaScript (no framework) · [Leaflet](https://leafletjs.com) · PWA (service worker + web app manifest) · Python 3 (only to download the tiles) · WMTS tiles from NASA/JPL Mars Trek.

## Known limitations

- The telemetry, positions, route and guide are **examples**; there is no integration with a suit, satellites or elevation data.
- The map has a resolution of ~232 m/pixel (maximum zoom 7 on this layer): it is good for general orientation, not for fine terrain detail.
- The "Satélite" (Satellite) button only toggles a visual state; the app also reacts to a real loss of network (airplane mode), but that does not trigger any sync.
- Tabs and the alert do not yet have full keyboard accessibility (focus trapped in the alert, arrow-key navigation on the tabs).

## Team

| Name | GitHub |
|------|--------|
| Euler | [@Eulxrs](https://github.com/Eulxrs) |
| João | [@JoaoBatistaAlm](https://github.com/JoaoBatistaAlm) |
| Luann | [@luannlira](https://github.com/luannlira) |
| Kauã | [@KauaFerreira-dev-eng](https://github.com/KauaFerreira-dev-eng) |
| Lucas | [@lucashenrique0](https://github.com/lucashenrique0) |

## Demo and presentation

- Video: *(to be filled in)*
- Slides: *(to be filled in)*
- Demo: *(to be filled in: GitHub Pages link, e.g. `https://luannlira.github.io/martianmap-spaceapps-cg-2026/os/app/`, after enabling Pages)*
- Pitch script: [`docs/pitch.md`](docs/pitch.md) (in Portuguese)

## Documentation

The documents below are written in Portuguese.

- [Overview](docs/visao-geral.md): problem, solution, target audience and differentiator
- [Architecture](docs/arquitetura.md): how the modules connect, the alert flow and the offline strategy
- [Lost Mode (*Modo Perdido*)](docs/modo-perdido.md): the core feature (planned, not yet implemented)
- [Pitch](docs/pitch.md): script, demo and likely questions
- [AI use](docs/uso-de-ia.md): AI use statement

## Credits

Terrain data: **NASA/JPL Mars Trek**. Interactive maps: **Leaflet** (Vladimir Agafonkin and contributors).

## License

MIT — see [LICENSE](LICENSE).
