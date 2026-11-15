# Visão geral

> Equipe **JEKLL** (João, Euler, Kauã, Luann e Lucas) · NASA Space Apps Challenge 2026, Campina Grande
> Desafio: **Interplanetary Survival Guide: Martian Map**

## Problema

Um explorador sozinho em Marte, a quilômetros da base, não pode contar com a Terra nem com infraestrutura de navegação:

- **Comunicação com atraso.** O sinal leva de cerca de 3 a 22 minutos para ir de Marte à Terra (depende da posição dos dois planetas), e outro tanto para a resposta. Um alerta no traje não pode esperar ajuda de lá.
- **Sem GPS e sem bússola.** Marte não tem rede de navegação por satélite como a nossa, e não tem campo magnético global, então a bússola magnética não serve para se orientar.
- **Superfície enorme.** Marte tem cerca de 144 milhões de km², quase o mesmo que toda a terra firme da Terra.
- **Tempestades de poeira.** Elas podem cobrir o planeta inteiro. Em 2018, uma delas levou ao fim da missão do rover Opportunity.
- **Sem plano B.** Se o sistema principal falha, o astronauta fica sem mapa, sem guia e sem noção de onde está.

> Os números acima vêm do pitch. Antes de apresentar, confira cada um no site da NASA e fale só o que dominar.

## Solução

O **Martian Map** é uma **segunda via de sobrevivência**: um sistema operacional leve, em um dispositivo pequeno que pode ser operado com luvas de traje. Ele reúne:

1. **Guia de sobrevivência offline**: procedimentos e checklists para emergências.
2. **Mapa com locais seguros**, salvo no dispositivo antes da missão.
3. **Integração com o traje**, para detectar situações críticas e alertar na hora.
4. **Bateria projetada para semanas** (meta de projeto, ainda não medida).

### Destaque: Modo Perdido

O astronauta aperta **um único botão**. O sistema:

1. estima a posição combinando **três fontes** (satélites, relevo e ângulo do Sol);
2. mostra o **nível de confiança** dessa estimativa;
3. indica o **abrigo mais seguro**, considerando o oxigênio restante;
4. ativa a **trilha de volta**.

Especificação completa (e o que ainda é hipótese) em [`modo-perdido.md`](modo-perdido.md).

## Para quem

- **Astronautas e exploradores** em missões de superfície.
- **Resgate e exploração na Terra**: desertos e regiões polares têm o mesmo problema (pouca ou nenhuma infraestrutura, comunicação ruim, terreno que confunde). A mesma lógica serve, com o guia atualizado a cada missão.

## Diferencial

| Diferencial | Por quê importa |
|-------------|-----------------|
| **Offline primeiro**: funciona sem sinal e só depois sincroniza | A navegação de hoje depende de satélites e internet; em Marte o sinal é justamente o que falta |
| **Simples sob estresse**: um botão, alvos grandes, uso com luvas | Em emergência não há atenção nem destreza para menus |
| **Honesto sobre a incerteza**: mostra o nível de confiança da posição | Uma posição errada apresentada como certa é pior do que nenhuma |
| **Três fontes de localização combinadas** | Se uma falha (por exemplo, tempestade de poeira cobrindo o Sol), as outras seguem |

## Inovação e sustentabilidade

- **Inovação:** invertemos a lógica da navegação atual. Em vez de depender de satélite e internet e usar o offline como exceção, o sistema **funciona primeiro sem sinal** e só depois sincroniza.
- **Sustentabilidade (meta de projeto):** sistema leve, de baixo consumo de energia, que reduz a dependência de infraestrutura e de operações de resgate caríssimas, e que pode ser reaproveitado na Terra. O consumo ainda **não foi medido**; trate como objetivo, não como resultado.

## Dados

Usamos dados abertos da NASA, do portal **Mars Trek** (NASA/JPL), que reúne mapas e relevo de Marte. Detalhes em [`../data/README.md`](../data/README.md).

## Estado atual (validação)

| Item | Estado |
|------|--------|
| Download de tiles do Mars Trek com área configurável, guardados para uso offline | **Pronto** ([`mapa/baixar_tiles.py`](../mapa/baixar_tiles.py)) |
| App web instalável (PWA) com mapa offline, guia e alertas de traje **simulados** | **Protótipo pronto** ([`os/app/`](../os/app)) |
| **Modo Perdido** | Próximo passo (não implementado) |
| Integração real com traje | Próximo passo (hoje é simulação) |
| Bateria de semanas, hardware, distro | Meta de projeto (não medido, não construído) |

## Roadmap

1. **Agora (hackathon):** tiles offline + PWA de demonstração.
2. **Próximo:** camada de elevação do Mars Trek; abrigos reais cadastrados; Modo Perdido em versão simplificada (estimativa de posição + confiança + abrigo mais próximo) sobre o mapa offline.
3. **Depois:** protocolo de telemetria do traje; sincronização quando houver link; protótipo em hardware pequeno e medição de consumo.
4. **Validação externa:** simulações de missão e áreas remotas na Terra (é o que buscamos em parcerias).

## Documentação relacionada

- [Arquitetura](arquitetura.md)
- [Modo Perdido](modo-perdido.md)
- [Pitch](pitch.md)
- [Uso de IA](uso-de-ia.md)
