# Arquitetura

Como os módulos (S.O., guia, mapa, traje, hardware) se conectam. Cada seção separa o **que existe hoje** (protótipo) do **que é visão de produto**.

## Módulos

| Módulo | Pasta | Responsabilidade | Depende de |
|--------|-------|------------------|-----------|
| S.O. / interface | [`os/`](../os) | Telas, navegação, alerta em tela cheia, cache offline | todos os outros |
| Guia | [`guia-sobrevivencia/`](../guia-sobrevivencia) | Checklists e procedimentos | nada (conteúdo) |
| Mapa | [`mapa/`](../mapa) | Tiles offline, abrigos, rota | Mars Trek (só no preparo) |
| Traje | [`traje/`](../traje) | Sensores, limites, alertas | Guia (qual checklist abrir), Mapa (rota até abrigo) |
| Modo Perdido | [`modo-perdido.md`](modo-perdido.md) | Posição estimada, confiança, abrigo, trilha | Mapa, Traje (O₂), elevação |
| Hardware | [`hardware/`](../hardware) | Dispositivo, bateria, ergonomia | requisitos dos demais |

## Protótipo atual (PWA)

```
os/app/
  index.html   tudo em um arquivo: HTML, CSS e JS (Leaflet para o mapa)
  sw.js        service worker: cache-first de app + tiles
  manifest.webmanifest   instalação como app
  vendor/      Leaflet 1.9.4 local (sem CDN, para funcionar offline)
  assets/tiles/{z}/{y}/{x}.jpg + lista.json   (gerados por mapa/baixar_tiles.py)
```

### Fluxo de dados

1. **Preparo (com internet, uma vez):** `mapa/baixar_tiles.py` baixa os tiles da NASA para `os/app/assets/tiles/` e gera `lista.json`.
2. **Primeira abertura do app:** o service worker guarda no cache o app, o Leaflet, os ícones e **todos** os tiles de `lista.json`.
3. **Uso (offline):** o mapa pede `assets/tiles/{z}/{y}/{x}.jpg`; o service worker responde do cache. Nada vai à NASA em tempo de uso.

### Fluxo de alerta (simulado)

```
sliders da aba Traje (4 "sensores")
        |
        v   checar(): compara com limites (bad)
 valor fora do limite?
        |  sim
        v
 disparar(): alerta em tela cheia + vibração + banner crítico no Mapa
        |
        +--> "Ver rota até o abrigo"  -> mostra a polilinha no mapa
        +--> "Abrir checklist"        -> abre o guia correspondente
        +--> "Dispensar"              -> silencia até o valor voltar ao normal
```

Limites do protótipo (de `SENS` em `index.html`):

| Sensor | Alerta quando | Checklist |
|--------|---------------|-----------|
| Reserva de O₂ | < 20 % | Pouco oxigênio |
| Pressão do traje | < 24 kPa | Perda de pressão |
| Temperatura interna | > 30 °C | Temperatura alta |
| Poeira no ar | > 70 % | Tempestade de poeira |

Esses limites são **exemplos da equipe**, não valores oficiais.

### Estratégia offline

- **Cache-first** no service worker: se está no cache, responde direto; se não, tenta a rede; se falha, devolve `504` (ou o `index.html` em navegação).
- O app (8 arquivos) é **essencial**: se falhar ao guardar, a instalação falha. Os tiles são **melhor esforço**: falhas viram aviso no console.
- **Versão do cache:** a constante `VERSAO` em `sw.js`. Mudou qualquer arquivo do app? Aumente `VERSAO`, senão quem já abriu continua vendo a versão antiga.
- O botão "Satélite" só alterna o estado na tela; o app também reage aos eventos reais `online` e `offline` do navegador.

### Mapa e projeção

- Leaflet com `L.CRS.EPSG4326` (equiretangular), a mesma grade dos tiles do Mars Trek.
- Tiles indexados `{z}/{y}/{x}` com linhas contadas a partir do norte e colunas a partir de −180° de longitude; no zoom 0 há 2 colunas por 1 linha.
- O Leaflet assume o raio da Terra, então a **distância** é calculada à mão (haversine com raio de Marte, 3.389,5 km).

## O que o protótipo não faz

- Não lê traje, satélite nem elevação reais.
- Não implementa o Modo Perdido.
- Não calcula rota: a rota é uma linha fixa de exemplo.
- Não foi testado em hardware pequeno, nem com luvas, nem medido em consumo de energia.

## Decisões e porquês

| Decisão | Motivo | Alternativa considerada |
|---------|--------|------------------------|
| PWA em HTML/JS puro | Roda em qualquer aparelho com navegador, sem build; fácil de mostrar | Distro Linux dedicada (visão de produto) |
| Leaflet local | Sem dependência de CDN; funciona sem internet | CDN |
| Tiles pré-baixados | O app nunca precisa da NASA em campo | Consultar o Mars Trek ao vivo |
| Área de download configurável | Permite equilibrar cobertura e armazenamento em dispositivo pequeno | Mapa global fixo |
