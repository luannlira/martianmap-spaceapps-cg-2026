# Data

Where each dataset came from (NASA / partner agencies) and how to obtain it. Large files stay outside the repository; only links and small samples (`samples/`) are kept here.

## Sources

### NASA/JPL Mars Trek: terrain map

| Item | Value |
|------|-------|
| Portal | [trek.nasa.gov/mars](https://trek.nasa.gov/mars/) |
| Layer catalog | [trekAPI](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars) |
| Service | WMTS (tiles) |
| Layer | `Mars_Viking_MDIM21_ClrMosaic_global_232m` (Viking color mosaic) |
| Resolution | ~232 m/pixel |
| Projection | Equirectangular (EPSG:4326) |
| Downloaded region | 13–23°N, 72–82°E (~590 × 560 km) |
| Zoom | 0 to 7 (zoom 8 returns 404 on this layer) |
| Tiles | 107 (~6 MB) |
| Format | JPG, 256 × 256 |

**How to obtain it:**

```bash
python mapa/baixar_tiles.py
```

The tiles go to `os/app/assets/tiles/` and are already versioned in the repository. Details in [`../mapa/README.md`](../mapa/README.md).

**Use in the app:** downloaded once, served locally. The app **does not query NASA at runtime**.

**Attribution:** shown in the corner of the map (`NASA/JPL Mars Trek · <layer>`).

**Terms of use:** check the page of each Mars Trek product before redistributing.

## Data still missing

| Data | What for | Status |
|------|----------|--------|
| Mars Trek **elevation** (relief) layer | Route slope and Lost Mode (*Modo Perdido*) | To be chosen from the catalog |
| List of **shelters** | Destination of the route and of Lost Mode | To be defined (today there is one example) |
| Solar ephemerides for Mars | Estimating position from the Sun's angle | To be defined |
| Suit sensor limits | Alerts | Today they are team examples |
| Emergency procedures | Guide | Today they are team examples |

## Simulated data (not from real sources)

- Suit telemetry (sliders)
- Positions of "Você" (You) and the shelter, risk zone and route
- Displayed battery (94%)

## Third-party dependency

[Leaflet](https://leafletjs.com) 1.9.4 (BSD-2-Clause), in `os/app/vendor/`.

## Structure

```
data/
|-- README.md    # this file
|-- samples/     # (optional) small samples
`-- raw/         # ignored by git (.gitignore): large local files
```
