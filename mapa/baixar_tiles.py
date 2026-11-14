#!/usr/bin/env python3
"""
Baixa tiles do Mars Trek (NASA/JPL) de uma região pequena, para uso offline no app.

Uso (a partir da raiz do repositório):
    python mapa/baixar_tiles.py --contar     # só conta quantos tiles e estima o tamanho (não baixa)
    python mapa/baixar_tiles.py              # baixa de verdade

Os tiles vão para  os/app/assets/tiles/{z}/{y}/{x}.{ext}
No fim, o script imprime as constantes para colar no app.js e grava lista.json
(lista de arquivos, útil para o service worker do PWA).

Sem dependências externas (só a biblioteca padrão do Python 3).
"""
import argparse
import json
import math
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# ------------------------- CONFIGURE AQUI -------------------------
# Camada do catálogo: https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars
CAMADA = "Mars_Viking_MDIM21_ClrMosaic_global_232m"

# Região (graus). Exemplo: área ao redor da cratera Jezero.
SUL, OESTE, NORTE, LESTE = 13, 72, 23, 82

# Zoom máximo a baixar (o máximo real depende da camada; tiles que não existem são ignorados).
ZOOM_MAX = 8
# ------------------------------------------------------------------

URL = ("https://trek.nasa.gov/tiles/Mars/EQ/{camada}/1.0.0/default/default028mm/"
       "{z}/{y}/{x}.{ext}")
DESTINO = Path(__file__).resolve().parents[1] / "os" / "app" / "assets" / "tiles"
KB_POR_TILE = 25  # ESTIMATIVA média de um tile 256x256 em JPG; o valor real varia por camada


def faixa(z, sul, oeste, norte, leste):
    """Índices (x0, x1, y0, y1) dos tiles que cobrem a região no zoom z.

    Grade equiretangular: no zoom 0 há 2 colunas x 1 linha; cada tile cobre 180/2^z graus.
    Linhas contam a partir do norte; colunas, a partir de -180 de longitude.
    """
    graus = 180 / 2 ** z
    linhas = 2 ** z
    colunas = 2 ** (z + 1)
    x0 = max(0, math.floor((oeste + 180) / graus))
    x1 = min(colunas - 1, math.floor((leste + 180) / graus))
    y0 = max(0, math.floor((90 - norte) / graus))
    y1 = min(linhas - 1, math.floor((90 - sul) / graus))
    return x0, x1, y0, y1


def lista_de_tiles(zoom_max):
    for z in range(zoom_max + 1):
        x0, x1, y0, y1 = faixa(z, SUL, OESTE, NORTE, LESTE)
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                yield z, y, x


def pegar(url, tentativas=2):
    """Devolve os bytes do tile, ou None se o servidor responder 404 (sem cobertura)."""
    req = urllib.request.Request(url, headers={"User-Agent": "martianmap-hackathon/1.0"})
    for t in range(tentativas):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if t == tentativas - 1:
                raise
        except urllib.error.URLError:
            if t == tentativas - 1:
                raise
        time.sleep(1)


def detectar_extensao():
    """Alguns produtos usam .jpg e outros .png: testa o tile global 0/0/0."""
    for ext in ("jpg", "png"):
        if pegar(URL.format(camada=CAMADA, z=0, y=0, x=0, ext=ext)):
            return ext
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--contar", action="store_true", help="só conta os tiles e estima o tamanho")
    ap.add_argument("--zoom-max", type=int, default=ZOOM_MAX)
    args = ap.parse_args()

    tiles = list(lista_de_tiles(args.zoom_max))
    print(f"Região: S={SUL} O={OESTE} N={NORTE} L={LESTE}  |  camada: {CAMADA}")
    for z in range(args.zoom_max + 1):
        n = sum(1 for t in tiles if t[0] == z)
        print(f"  zoom {z}: {n} tile(s)")
    print(f"Total: {len(tiles)} tiles  (~{len(tiles) * KB_POR_TILE / 1024:.1f} MB, estimativa de {KB_POR_TILE} KB/tile)")
    if args.contar:
        return

    ext = detectar_extensao()
    if not ext:
        sys.exit("Não consegui baixar o tile global 0/0/0 (nem .jpg nem .png).\n"
                 "Confira a internet e o nome da camada no catálogo do Mars Trek.")
    print(f"Extensão detectada: .{ext}\nBaixando para {DESTINO} ...")

    baixados, ausentes, ja_existiam, arquivos = 0, 0, 0, []
    for z, y, x in tiles:
        arq = DESTINO / str(z) / str(y) / f"{x}.{ext}"
        rel = f"assets/tiles/{z}/{y}/{x}.{ext}"
        if arq.exists():
            ja_existiam += 1
            arquivos.append(rel)
            continue
        dados = pegar(URL.format(camada=CAMADA, z=z, y=y, x=x, ext=ext))
        if dados is None:
            ausentes += 1  # sem cobertura de dados nessa área
            continue
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_bytes(dados)
        arquivos.append(rel)
        baixados += 1
        time.sleep(0.1)  # pega leve com o servidor

    DESTINO.mkdir(parents=True, exist_ok=True)
    (DESTINO / "lista.json").write_text(json.dumps(arquivos, indent=1), encoding="utf-8")
    total_mb = sum((DESTINO.parent.parent / a).stat().st_size for a in arquivos) / 1e6
    print(f"\nBaixados: {baixados} | já existiam: {ja_existiam} | sem dados (404): {ausentes}")
    print(f"Tamanho real: {total_mb:.2f} MB  |  lista de arquivos: {DESTINO / 'lista.json'}")
    print("\n--- Cole no app.js ---")
    print(f"const TILE_EXT = '{ext}';")
    print(f"const Z_MAX = {args.zoom_max};")
    print(f"const BOUNDS = [[{SUL}, {OESTE}], [{NORTE}, {LESTE}]];  // [sul, oeste], [norte, leste]")
    print(f"const CAMADA = '{CAMADA}';")


if __name__ == "__main__":
    main()
