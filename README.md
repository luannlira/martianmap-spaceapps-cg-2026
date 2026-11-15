# Martian Map — Survival OS *(Segunda chance de Sobreviver)*

> NASA Space Apps Challenge 2026 · Campina Grande
> **Desafio:** Interplanetary Survival Guide: Martian Map

## A ideia

Um **sistema operacional (distro) leve**, pensado como uma **segunda via de sobrevivência** para exploradores em Marte. Ele roda em um dispositivo pequeno (ou maior, se precisar ser compatível com os trajes), de **fácil manipulação**, e reúne:

- um **guia de sobrevivência** disponível offline;
- acesso a uma **rede guiada por satélites que orbitam Marte**, para **mapear a área** e indicar **locais seguros** para deslocamento;
- integração com o **traje espacial**, que identifica **situações críticas**;
- **bateria de longa duração** como requisito (meta: semanas sem recarregar, no estilo dos celulares antigos).

> **O que existe hoje:** um protótipo em forma de **app web instalável (PWA)** que simula a interface do Survival OS, com mapa real de Marte (dados da NASA) salvo no dispositivo. A distro, o hardware e a integração com satélites e traje reais são a **visão de produto**, e não fazem parte do protótipo. Veja [Escopo do protótipo](#escopo-do-protótipo).

## Módulos

| Módulo | O que é | Pasta | Status |
|--------|---------|-------|--------|
| S.O. / distro | Sistema leve, simples de usar, que roda no dispositivo | [`os/`](os) | Protótipo web (PWA) pronto; distro é conceito |
| Guia de sobrevivência | Conteúdo offline: procedimentos, emergências, checklists | [`guia-sobrevivencia/`](guia-sobrevivencia) | 5 checklists de exemplo (conteúdo a validar) |
| Mapa e navegação | Mapeamento da área e locais seguros via satélites | [`mapa/`](mapa) | Mapa offline com tiles reais da NASA; rota de exemplo |
| Traje inteligente | Detecção de situações críticas e alertas | [`traje/`](traje) | Telemetria **simulada**, 4 sensores e alertas |
| Hardware e energia | Dispositivo, formato, bateria, requisitos | [`hardware/`](hardware) | A definir |

## Requisitos (metas)

- [x] Fácil de manipular, inclusive com luvas/traje *(protótipo: alvos de toque de 44 a 72 px; ainda não testado com luvas reais)*
- [x] Funcionar offline *(interface, guia e mapa ficam salvos no dispositivo pelo service worker)*
- [ ] Sincronizar quando houver link com os satélites *(hoje o botão "Satélite" só simula o estado; não há sincronização real)*
- [ ] Rodar em dispositivo pequeno com poucos recursos *(o app inteiro tem cerca de 6 MB, mas ainda não foi testado em hardware real)*
- [ ] Bateria de longa duração *(requisito de hardware, ainda não validado)*
- [x] Alertar rapidamente em situações críticas *(protótipo: alerta em tela cheia + vibração, com telemetria simulada)*

## Escopo do protótipo

> O que entregamos no hackathon: uma demonstração de como o Survival OS funciona, em formato de app web instalável.

**Incluído e funcionando**

- [x] **App que simula a interface do S.O.**: telas de Mapa, Guia e Traje, pensadas para uso com luvas e em um dispositivo pequeno
- [x] **PWA com funcionamento offline**: interface, guia e mapa salvos no dispositivo (service worker + manifest)
- [x] **Mapa real de Marte**: tiles do NASA/JPL Mars Trek baixados antes e servidos localmente, com zoom e marcadores
- [x] **Alertas do traje (simulados)**: 4 sensores; ao passar do limite, abre o alerta com vibração, rota até o abrigo e o checklist certo
- [x] **Guia de sobrevivência offline**: 5 checklists marcáveis
- [x] **Distância calculada com o raio de Marte** (3.389,5 km)

**Simulado ou de exemplo (não vem de dados reais)**

- Telemetria do traje (controles deslizantes), % de bateria exibido, botão "Satélite"
- Posições de "Você" e do abrigo, a zona de risco e a rota
- Procedimentos do guia (escritos pela equipe, **não são procedimentos oficiais da NASA**)

**Fora do escopo do protótipo**

- Distro Linux, hardware e bateria, rede de satélites e traje reais
- Rota calculada por declividade (os tiles são imagens, não dados de elevação)

## Dados utilizados

| Dado | Fonte (NASA / agência parceira) | Link |
|------|---------------------------------|------|
| Mapa de terreno de Marte: mosaico colorido, ~232 m/pixel, camada `Mars_Viking_MDIM21_ClrMosaic_global_232m`. Região 13–23°N, 72–82°E (~590 × 560 km), zoom 0–7, 107 tiles (~6 MB) | NASA/JPL — **Mars Trek** (serviço de tiles WMTS) | [trek.nasa.gov/mars](https://trek.nasa.gov/mars/) · [catálogo de camadas](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars) |

Os tiles são baixados **uma vez**, com [`mapa/baixar_tiles.py`](mapa/baixar_tiles.py), e guardados em `os/app/assets/tiles/`. O app **não consulta a NASA em tempo de uso**, e é por isso que funciona offline. A atribuição aparece no canto do mapa. Confirme os termos de uso de cada produto na página do Mars Trek antes de redistribuir.

**Dependência de terceiros:** [Leaflet](https://leafletjs.com) 1.9.4 (licença BSD-2-Clause), guardado em `os/app/vendor/` para funcionar sem internet.

Detalhes de cada dado em [`data/`](data).

## Como rodar

**Pré-requisito:** Python 3 (usado só para o servidor local e para baixar tiles) e um navegador moderno (testado no Chrome).

```bash
git clone https://github.com/luannlira/martianmap-spaceapps-cg-2026.git
cd martianmap-spaceapps-cg-2026
python -m http.server 8000      # no Linux/Mac pode ser python3; no Windows, py -m http.server 8000
```

Abra **http://localhost:8000/os/app/** no navegador.

> Rode o servidor **na raiz do repositório** e mantenha o terminal aberto. Não abra o `index.html` com duplo clique: o service worker não funciona em `file://` e o mapa não carrega os tiles.

**Testar o fluxo principal**

1. Aba **Traje** → arraste a *Reserva de O₂* para menos de 20%.
2. No alerta, toque em **Ver rota até o abrigo** (a rota aparece no Mapa) ou em **Abrir checklist**.
3. Volte o O₂ ao normal: a rota some.

**Testar o modo offline**

1. Com o app aberto, aguarde um instante (o service worker guarda tudo na primeira visita).
2. Em F12 → *Application* → *Cache Storage*, confira os arquivos guardados (8 do app + 107 tiles).
3. Pare o servidor (Ctrl+C) e recarregue a página: o app, o mapa e o guia continuam abrindo.

**Instalar como app**: no Chrome, use o ícone de instalar na barra de endereço.

**Atualizou algum arquivo do app?** Aumente `VERSAO` em `os/app/sw.js`; senão quem já abriu o app continua vendo a versão antiga.

**Baixar outra região ou camada**: veja [`mapa/README.md`](mapa/README.md).

## Estrutura do repositório

```
.
|-- README.md
|-- LICENSE
|-- .gitignore
|-- .github/
|   `-- pull_request_template.md
|-- docs/                  # visão geral, arquitetura, pitch e imagens
|-- os/                    # sistema operacional / distro
|   `-- app/               # protótipo: interface do Survival OS (PWA)
|       |-- index.html     # telas, estilos e lógica
|       |-- sw.js          # service worker (cache offline)
|       |-- manifest.webmanifest
|       |-- icons/
|       |-- vendor/        # Leaflet (terceiros)
|       `-- assets/tiles/  # tiles do Mars Trek + lista.json
|-- guia-sobrevivencia/    # conteúdo do guia offline
|-- mapa/                  # mapa, navegação e locais seguros
|   `-- baixar_tiles.py    # baixa os tiles da NASA
|-- traje/                 # detecção de situações críticas
|-- hardware/              # dispositivo, bateria e requisitos
`-- data/                  # origem e documentação dos dados
```

## Tecnologias

HTML, CSS e JavaScript puro (sem framework) · [Leaflet](https://leafletjs.com) · PWA (service worker + web app manifest) · Python 3 (só para baixar os tiles) · tiles WMTS do NASA/JPL Mars Trek.

## Limitações conhecidas

- A telemetria, as posições, a rota e o guia são de **exemplo**; não há integração com traje, satélites nem dados de elevação.
- O mapa tem resolução de ~232 m/pixel (zoom máximo 7 nessa camada): serve para orientação geral, não para detalhe de terreno.
- O botão "Satélite" apenas alterna um estado visual; o app também reage a perda real de rede (modo avião), mas isso não dispara nenhuma sincronização.
- Abas e alerta ainda não têm acessibilidade completa por teclado (foco preso no alerta, navegação por setas nas abas).

## Equipe

| Nome | GitHub |
|------|--------|
| Euler | [@Eulxrs](https://github.com/Eulxrs) |
| João | [@JoaoBatistaAlm](https://github.com/JoaoBatistaAlm) |
| Luann | [@luannlira](https://github.com/luannlira) |
| Kauã | [@KauaFerreira-dev-eng](https://github.com/KauaFerreira-dev-eng) |
| Lucas | [@lucashenrique0](https://github.com/lucashenrique0) |

## Demo e apresentação

- Vídeo: *(a preencher)*
- Slides: *(a preencher)*
- Demo: *(a preencher: link do GitHub Pages, ex.: `https://luannlira.github.io/martianmap-spaceapps-cg-2026/os/app/`, depois de ativar o Pages)*
- Roteiro do pitch: [`docs/pitch.md`](docs/pitch.md)

## Documentação

- [Visão geral](docs/visao-geral.md): problema, solução, para quem e diferencial
- [Arquitetura](docs/arquitetura.md): como os módulos se conectam, fluxo de alerta e estratégia offline
- [Pitch](docs/pitch.md): roteiro, demo e perguntas prováveis

## Créditos

Dados de terreno: **NASA/JPL Mars Trek**. Mapas interativos: **Leaflet** (Vladimir Agafonkin e colaboradores).

## Licença

MIT — veja [LICENSE](LICENSE).
