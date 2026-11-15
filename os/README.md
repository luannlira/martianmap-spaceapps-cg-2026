# S.O. / distro

Sistema operacional leve de sobrevivência: simples de manipular, funcional offline, pensado para dispositivo pequeno. *Ideia: Euler.*

## Status

- [x] **Protótipo:** app web instalável (PWA) que simula a interface do Survival OS ([`app/`](app))
- [ ] **Distro dedicada:** é visão de produto, não existe ainda
- [ ] [Modo Perdido](../docs/modo-perdido.md)

## O que o protótipo tem

- Três telas, com navegação por abas: **Mapa**, **Guia** e **Traje**
- Mapa real de Marte (tiles do Mars Trek) salvo no dispositivo
- Alerta em tela cheia + vibração quando um sensor simulado passa do limite
- Funcionamento offline (service worker) e instalação como app (manifest)
- Tema claro/escuro automático, alvos de toque grandes

## Arquivos

| Arquivo | Função |
|---------|--------|
| `app/index.html` | Telas, estilos e lógica (HTML + CSS + JS em um arquivo) |
| `app/sw.js` | Service worker, cache-first: guarda o app e todos os tiles |
| `app/manifest.webmanifest` | Nome, ícones e modo de tela cheia do app instalado |
| `app/vendor/` | Leaflet 1.9.4 (local, sem CDN) |
| `app/icons/` | Ícones do app |
| `app/assets/tiles/` | Tiles do Mars Trek + `lista.json` |

`app/assets/terreno.jpg` não é usado hoje pelo app (resto de uma versão anterior); pode ser removido.

## Como rodar

Na **raiz do repositório**:

```bash
python -m http.server 8000
```

Abra **http://localhost:8000/os/app/**. Não abra o arquivo com duplo clique: o service worker não funciona em `file://`. Passo a passo e teste offline em [Como rodar](../README.md#como-rodar).

## Como mexer

- Mudou qualquer arquivo em `app/`? **Aumente `VERSAO` em `sw.js`**, senão quem já abriu vê a versão antiga.
- Para a lógica, veja os blocos de `index.html`: *Mapa*, *Dados* (`GUIAS`, `SENS`), *Abas*, *Alertas*, *Satélite/offline*.
- Nova região de mapa: ver [`../mapa/README.md`](../mapa/README.md).
- Dados fixos usam `innerHTML`. Se algum dia vierem de fora (traje, rede), troque por `textContent`.

## Do protótipo à distro (visão)

1. Manter o app como a interface do sistema.
2. Rodar sobre uma base Linux mínima em hardware pequeno, abrindo direto no app.
3. Medir consumo e ajustar.

Detalhes e decisões em [`../docs/arquitetura.md`](../docs/arquitetura.md).

## Limitações

- Telemetria, posições, rota e guia são de **exemplo**.
- O botão "Satélite" só alterna um estado na tela.
- Acessibilidade por teclado incompleta (foco preso no alerta, setas nas abas).
- Nunca testado em hardware pequeno nem com luvas.
