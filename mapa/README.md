# Mapa e navegação

Mapa offline de Marte e indicação de locais seguros, com dados do **NASA/JPL Mars Trek**.

## Status

- [x] Download de tiles do Mars Trek com **área configurável** ([`baixar_tiles.py`](baixar_tiles.py))
- [x] Mapa offline no app (Leaflet + service worker)
- [x] Marcadores, zona de risco e rota **de exemplo** (coordenadas reais, posições inventadas)
- [x] Distância calculada com o raio de Marte
- [ ] Camada de elevação (relevo)
- [ ] Abrigos reais e rota calculada por declividade
- [ ] [Modo Perdido](../docs/modo-perdido.md)

## Baixar os tiles

Só precisa de Python 3 (biblioteca padrão) e internet **uma vez**.

```bash
python mapa/baixar_tiles.py --contar     # só conta os tiles e estima o tamanho
python mapa/baixar_tiles.py              # baixa de verdade
python mapa/baixar_tiles.py --zoom-max 6 # limita o zoom (menos tiles, menos espaço)
```

Os tiles vão para `os/app/assets/tiles/{z}/{y}/{x}.jpg` e o script gera `lista.json`, que o service worker usa para guardar tudo no cache. No fim, o script imprime as constantes (`TILE_EXT`, `Z_MAX`, `BOUNDS`, `CAMADA`) para **colar no `os/app/index.html`**. Se mudar a região ou a camada, atualize esses valores e aumente `VERSAO` em `os/app/sw.js`.

Tiles já baixados são pulados; dá para rodar de novo sem repetir o download. Se o servidor responder 404, o tile é ignorado (sem cobertura).

## Escolher a área (o equilíbrio de armazenamento)

No topo do script:

```python
CAMADA = "Mars_Viking_MDIM21_ClrMosaic_global_232m"
SUL, OESTE, NORTE, LESTE = 13, 72, 23, 82   # graus
ZOOM_MAX = 7
```

| Alavanca | Efeito |
|----------|--------|
| Dobrar a largura **e** a altura da região | ≈ 4× mais tiles |
| +1 nível de zoom | ≈ 4× mais tiles |
| Zoom máximo | Limitado pela camada (nessa, o zoom 8 dá 404) |

Contagem por zoom na região de exemplo (13–23°N, 72–82°E, ~590 × 560 km):

| Zoom | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Total |
|------|---|---|---|---|---|---|---|---|-------|
| Tiles | 1 | 1 | 1 | 2 | 4 | 9 | 25 | 64 | **107** |

> **Estimativa:** o `--contar` usa `KB_POR_TILE = 54` KB por tile, a média medida nessa camada (5,95 MB para os 107 tiles). Em outra camada ou região o valor muda; depois do primeiro download, confie no "Tamanho real" que o script imprime.

## Grade dos tiles

- Projeção equiretangular (EPSG:4326); no zoom 0 há 2 colunas × 1 linha.
- Cada tile cobre `180 / 2^z` graus.
- Linhas (`y`) contam do **norte**; colunas (`x`), a partir de **−180°** de longitude.
- URL: `https://trek.nasa.gov/tiles/Mars/EQ/{camada}/1.0.0/default/default028mm/{z}/{y}/{x}.{ext}`

## Limitações

- ~232 m/pixel: orientação geral, não detalhe fino de terreno.
- Os tiles são **imagens**, não elevação: não dá para calcular declividade com eles.
- Rota, "Você" e abrigo são **exemplos fixos** em `index.html` (`VOCE`, `ABRIGO`, `ROTA`, `RISCO`).

## Próximos passos

1. Escolher no [catálogo do Mars Trek](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars) uma camada de **elevação** para a mesma região e baixá-la com o script.
2. Cadastrar abrigos reais (lista de coordenadas).
3. Calcular a rota e penalizar terreno íngreme.
4. Base para o [Modo Perdido](../docs/modo-perdido.md).

## Dados e termos de uso

Ver [`../data/README.md`](../data/README.md). Confirme os termos de uso de cada produto na página do Mars Trek antes de redistribuir.
