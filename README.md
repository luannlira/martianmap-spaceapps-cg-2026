# Martian Map — Survival OS *(Segunda chance de Sobreviver)*

> NASA Space Apps Challenge 2026 · Campina Grande
> **Desafio:** Interplanetary Survival Guide: Martian Map

## A ideia

Um **sistema operacional (distro) leve**, pensado como uma **segunda via de sobrevivência** para exploradores em Marte. Ele roda em um dispositivo pequeno (ou maior, se precisar ser compatível com os trajes), de **fácil manipulação**, e reúne:

- um **guia de sobrevivência** disponível offline;
- acesso a uma **rede guiada por satélites que orbitam Marte**, para **mapear a área** e indicar **locais seguros** para deslocamento;
- integração com o **traje espacial**, que identifica **situações críticas**;
- **bateria de longa duração** como requisito (meta: semanas sem recarregar, no estilo dos celulares antigos).

## Módulos

| Módulo | O que é | Pasta | 
|--------|---------|-------|
| S.O. / distro | Sistema leve, simples de usar, que roda no dispositivo | [`os/`](os) |
| Guia de sobrevivência | Conteúdo offline: procedimentos, emergências, checklists | [`guia-sobrevivencia/`](guia-sobrevivencia) |
| Mapa e navegação | Mapeamento da área e locais seguros via satélites | [`mapa/`](mapa) | 
| Traje inteligente | Detecção de situações críticas e alertas | [`traje/`](traje) | 
| Hardware e energia | Dispositivo, formato, bateria, requisitos | [`hardware/`](hardware) |

## Requisitos (metas)

- [ ] Fácil de manipular, inclusive com luvas/traje
- [ ] Funcionar offline e sincronizar quando houver link com os satélites
- [ ] Rodar em dispositivo pequeno com poucos recursos
- [ ] Bateria de longa duração
- [ ] Alertar rapidamente em situações críticas

## Escopo do protótipo *(a definir pela equipe)*

> O que vamos entregar no hackathon: uma demonstração de como o Survival OS funciona, em formato de app web instalável.

- [ ] **Site/app que simula a interface do S.O.**: telas de Mapa, Guia e Traje, pensadas para uso com luvas e em um dispositivo pequeno
- [ ] **PWA com funcionamento offline**: guia de sobrevivência e mapa salvos no dispositivo, com alternância entre satélite e offline
- [ ] (a definir)

## Dados utilizados

| Dado | Fonte (NASA / agência parceira) | Link |
|------|---------------------------------|------|

## Como rodar

*(a preencher)*

```bash
git clone https://github.com/luannlira/martianmap-spaceapps-cg-2026.git
cd martian-map-spaceapps-cg-2026
```

## Estrutura do repositório

```
.
|-- README.md
|-- LICENSE
|-- .gitignore
|-- docs/                  # visão geral, arquitetura, pitch e imagens
|-- os/                    # sistema operacional / distro
|-- guia-sobrevivencia/    # conteúdo do guia offline
|-- mapa/                  # mapa, navegação e locais seguros
|-- traje/                 # detecção de situações críticas
|-- hardware/              # dispositivo, bateria e requisitos
`-- data/                  # dados e amostras
```

## Equipe
| Nome | GitHub |
|------|--------|
| Euler| [@Eulxrs](https://github.com/Eulxrs)|
| João | [@JoaoBatistaAlm](https://github.com/JoaoBatistaAlm)| 
| Luann| [@luannlira](https://github.com/luannlira) | 
| Kauã | [@KauaFerreira-dev-eng](https://github.com/KauaFerreira-dev-eng) |
| Lucas| [lucashenrique0](https://github.com/lucashenrique0) |

## Demo e apresentação

- Vídeo:
- Slides:
- Demo:

## Licença

MIT — veja [LICENSE](LICENSE).
