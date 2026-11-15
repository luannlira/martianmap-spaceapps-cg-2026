# Modo Perdido

> **Status: planejado, não implementado.** Este documento descreve a intenção e um desenho inicial. O protótipo atual **não** estima posição: as posições de "Você" e do abrigo em `os/app/index.html` são valores de exemplo.

## O que é

O recurso central do Martian Map. Com **um único botão**, um astronauta que não sabe onde está recebe:

1. uma **posição estimada**;
2. o **nível de confiança** dessa posição;
3. o **abrigo mais seguro**, levando em conta o oxigênio restante;
4. a **trilha de volta** ativada no mapa.

## Por que um botão só

Em estresse (e com luvas), cada toque a mais é um risco. O fluxo inteiro é uma ação do usuário; todo o resto é automático e exibido em tela simples, com alvos grandes.

## Três fontes de localização

| Fonte | Como ajuda | Limite conhecido | Estado |
|-------|-----------|------------------|--------|
| **Satélites** | Posição ou referência vinda do link orbital, quando houver | Pode não haver link (por isso o modo é offline primeiro) | Hipótese; sem integração |
| **Relevo** | Comparar o terreno visível/medido com o mapa de elevação salvo para achar onde o perfil "encaixa" | Exige camada de elevação baixada e sensor para observar o terreno; os tiles atuais são imagens, não elevação | Hipótese; camada ainda não escolhida |
| **Ângulo do Sol** | Altura do Sol no céu + hora local dão uma linha de posição (latitude aproximada) | Tempestade de poeira prejudica a medição; precisa de relógio confiável e efemérides | Hipótese; sem implementação |

A ideia é **combinar** as três. Se uma está indisponível, as outras continuam e a confiança cai de forma visível.

## Nível de confiança

Princípio de projeto: **ser honesto sobre a incerteza**. A tela deve mostrar:

- a posição estimada **com uma área de incerteza** (círculo no mapa), não só um ponto;
- um rótulo simples de confiança (por exemplo, Alta / Média / Baixa), derivado de quantas fontes concordam e do tamanho da área;
- **quais fontes** foram usadas.

Os limiares que separam Alta, Média e Baixa **ainda não foram definidos**. Devem sair de testes, não de palpite.

## Abrigo mais seguro e oxigênio

Escolha do abrigo = quanto oxigênio resta **versus** a distância até cada abrigo candidato, considerando a rota.

Rascunho do critério:

```
para cada abrigo candidato:
    distância  = comprimento da rota (km, usando raio de Marte = 3.389,5 km)
    tempo      = distância / velocidade de caminhada estimada
    consumo    = tempo * taxa de consumo de O2 (vinda do traje)
    viável     = consumo + margem de segurança <= O2 restante
escolher o viável com menor risco (rota e terreno); se nenhum for viável,
avisar isso claramente e mostrar o mais próximo.
```

Pendências: taxa de consumo e velocidade realistas (dependem do traje), margem de segurança e como penalizar terreno íngreme (precisa de elevação).

## Trilha de volta

- Ativa a rota até o abrigo escolhido sobre o mapa offline.
- O protótipo já desenha uma rota de exemplo e calcula o comprimento com o raio de Marte (`distKm` em `os/app/index.html`).
- Falta: rota calculada de verdade (hoje é uma linha fixa) e ajuste por declividade.

## Fluxo (visão)

```
[Botão "Estou perdido"]
        |
        v
 coletar fontes disponíveis (satélite, relevo, Sol)
        |
        v
 combinar -> posição + área de incerteza + confiança
        |
        v
 escolher abrigo viável com o O2 restante
        |
        v
 mostrar no mapa offline: você, abrigo, trilha de volta
```

## Plano de implementação

1. Definir **abrigos** reais (lista de coordenadas) para a região baixada.
2. Baixar uma **camada de elevação** do Mars Trek para a mesma região (ver [`../data/README.md`](../data/README.md)).
3. Versão simplificada: tela com botão, posição de entrada manual ou de teste, círculo de incerteza e abrigo viável mais próximo.
4. Acrescentar a estimativa por Sol e depois por relevo.
5. Testar com cenários conhecidos (posição verdadeira conhecida) e medir o erro, para então calibrar os rótulos de confiança.

## Como falar disto no pitch

Diga que o Modo Perdido é **o próximo passo** que será construído sobre o mapa offline. O que está pronto hoje é o mapa offline com tiles do Mars Trek (e o app de demonstração). Veja [`pitch.md`](pitch.md).
