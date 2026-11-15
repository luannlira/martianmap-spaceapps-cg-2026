# Dados

De onde veio cada dado (NASA / agências parceiras) e como obtê-lo. Arquivos grandes ficam fora do repositório; aqui só links e amostras pequenas (`samples/`).

## Fontes

### NASA/JPL Mars Trek: mapa de terreno

| Item | Valor |
|------|-------|
| Portal | [trek.nasa.gov/mars](https://trek.nasa.gov/mars/) |
| Catálogo de camadas | [trekAPI](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars) |
| Serviço | WMTS (tiles) |
| Camada | `Mars_Viking_MDIM21_ClrMosaic_global_232m` (mosaico colorido do Viking) |
| Resolução | ~232 m/pixel |
| Projeção | Equiretangular (EPSG:4326) |
| Região baixada | 13–23°N, 72–82°E (~590 × 560 km) |
| Zoom | 0 a 7 (o zoom 8 dá 404 nessa camada) |
| Tiles | 107 (~6 MB) |
| Formato | JPG, 256 × 256 |

**Como obter:**

```bash
python mapa/baixar_tiles.py
```

Os tiles vão para `os/app/assets/tiles/` e já estão versionados no repositório. Detalhes em [`../mapa/README.md`](../mapa/README.md).

**Uso no app:** baixados uma vez, servidos localmente. O app **não consulta a NASA em tempo de uso**.

**Atribuição:** aparece no canto do mapa (`NASA/JPL Mars Trek · <camada>`).

**Termos de uso:** confirme na página de cada produto do Mars Trek antes de redistribuir.

## Dados que ainda faltam

| Dado | Para quê | Estado |
|------|----------|--------|
| Camada de **elevação** (relevo) do Mars Trek | Declividade da rota e Modo Perdido | A escolher no catálogo |
| Lista de **abrigos** | Destino da rota e do Modo Perdido | A definir (hoje há um de exemplo) |
| Efemérides do Sol para Marte | Estimar posição pelo ângulo do Sol | A definir |
| Limites de sensores do traje | Alertas | Hoje são exemplos da equipe |
| Procedimentos de emergência | Guia | Hoje são exemplos da equipe |

## Dados simulados (não vêm de fontes reais)

- Telemetria do traje (controles deslizantes)
- Posições de "Você" e do abrigo, zona de risco e rota
- Bateria exibida (94 %)

## Dependência de terceiros

[Leaflet](https://leafletjs.com) 1.9.4 (BSD-2-Clause), em `os/app/vendor/`.

## Estrutura

```
data/
|-- README.md    # este arquivo
|-- samples/     # (opcional) amostras pequenas
`-- raw/         # ignorado pelo git (.gitignore): arquivos grandes locais
```
