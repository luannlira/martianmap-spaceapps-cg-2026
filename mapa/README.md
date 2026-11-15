# Map and navigation

Offline map of Mars and indication of safe locations, using data from **NASA/JPL Mars Trek**.

## Status

- [x] Mars Trek tile download with a **configurable area** ([`baixar_tiles.py`](baixar_tiles.py))
- [x] Offline map in the app (Leaflet + service worker)
- [x] Markers, risk zone and **example** route (real coordinates, made-up positions)
- [x] Distance calculated with the radius of Mars
- [ ] Elevation (relief) layer
- [ ] Real shelters and a route calculated from slope
- [ ] [Lost Mode (*Modo Perdido*)](../docs/modo-perdido.md) (in Portuguese)

## Downloading the tiles

It only needs Python 3 (standard library) and internet **once**.

```bash
python mapa/baixar_tiles.py --contar     # only counts the tiles and estimates the size
python mapa/baixar_tiles.py              # actually downloads
python mapa/baixar_tiles.py --zoom-max 6 # limits the zoom (fewer tiles, less space)
```

(`--contar` means "count".)

The tiles go to `os/app/assets/tiles/{z}/{y}/{x}.jpg` and the script generates `lista.json` (the list of tile files), which the service worker uses to store everything in the cache. At the end, the script prints the constants (`TILE_EXT`, `Z_MAX`, `BOUNDS`, `CAMADA`) to **paste into `os/app/index.html`**. If you change the region or the layer, update those values and increase `VERSAO` (the cache version) in `os/app/sw.js`.

Tiles that were already downloaded are skipped, so you can run it again without repeating the download. If the server answers 404, the tile is ignored (no coverage).

## Choosing the area (the storage trade-off)

At the top of the script:

```python
CAMADA = "Mars_Viking_MDIM21_ClrMosaic_global_232m"   # layer
SUL, OESTE, NORTE, LESTE = 13, 72, 23, 82   # south, west, north, east (degrees)
ZOOM_MAX = 7
```

| Lever | Effect |
|-------|--------|
| Doubling the region's width **and** height | ≈ 4× more tiles |
| +1 zoom level | ≈ 4× more tiles |
| Maximum zoom | Limited by the layer (on this one, zoom 8 returns 404) |

Tile count per zoom level in the example region (13–23°N, 72–82°E, ~590 × 560 km):

| Zoom | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Total |
|------|---|---|---|---|---|---|---|---|-------|
| Tiles | 1 | 1 | 1 | 2 | 4 | 9 | 25 | 64 | **107** |

> **Estimate:** `--contar` uses `KB_POR_TILE = 54` KB per tile, the average measured on this layer (5.95 MB for the 107 tiles). On another layer or region the value changes; after the first download, trust the "real size" (*Tamanho real*) that the script prints.

## Tile grid

- Equirectangular projection (EPSG:4326); at zoom 0 there are 2 columns × 1 row.
- Each tile covers `180 / 2^z` degrees.
- Rows (`y`) count from the **north**; columns (`x`) from **−180°** longitude.
- URL: `https://trek.nasa.gov/tiles/Mars/EQ/{layer}/1.0.0/default/default028mm/{z}/{y}/{x}.{ext}`

## Limitations

- ~232 m/pixel: general orientation, not fine terrain detail.
- The tiles are **images**, not elevation: slope cannot be calculated from them.
- Route, "Você" (You) and shelter are **fixed examples** in `index.html` (`VOCE`, `ABRIGO`, `ROTA`, `RISCO` = you, shelter, route, risk zone).

## Next steps

1. Pick an **elevation** layer for the same region in the [Mars Trek catalog](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars) and download it with the script.
2. Register real shelters (a list of coordinates).
3. Calculate the route and penalize steep terrain.
4. Foundation for [Lost Mode (*Modo Perdido*)](../docs/modo-perdido.md).

## Data and terms of use

See [`../data/README.md`](../data/README.md). Check the terms of use of each product on the Mars Trek page before redistributing.
