# Pitch

> Equipe **JEKLL** · NASA Space Apps Challenge 2026 · Campina Grande · **máximo 3 minutos**
> Desafio: *Interplanetary Survival Guide: Martian Map*

Roteiro completo, com tempos. Cerca de 400 palavras, aproximadamente 2min50 em ritmo calmo.

## 1. Abertura e desafio (0:00 – 0:15)

Boa tarde! Somos a equipe JEKLL, formada pelas iniciais de João, Euler, Kauã, Luann e Lucas, de Campina Grande. Escolhemos o desafio Interplanetary Survival Guide: Martian Map.

## 2. Problema (0:15 – 0:50)

Imagine você sozinho em Marte, a quilômetros da base. Seu traje dispara um alerta. A Terra leva de 3 a 22 minutos só para receber o sinal, e o mesmo tempo para responder. *(pausa)* Marte tem 144 milhões de km², quase toda a terra firme do nosso planeta, e nenhum GPS. A bússola não funciona, porque Marte não tem campo magnético global. E as tempestades de poeira podem cobrir o planeta inteiro: em 2018, uma delas encerrou a missão do rover Opportunity. Se o sistema principal falhar, não existe plano B.

## 3. Solução (0:50 – 1:40)

Criamos o Martian Map: uma segunda via de sobrevivência. É um sistema operacional leve, em um dispositivo pequeno, que pode ser operado com luvas de traje. Tem guia de sobrevivência offline, mapa com locais seguros, integração com o traje para detectar situações críticas e bateria projetada para semanas.

Nosso destaque é o Modo Perdido: o astronauta aperta um único botão. O sistema estima a posição combinando satélites, relevo e o ângulo do Sol, mostra o nível de confiança, indica o abrigo mais seguro considerando o oxigênio restante e ativa a trilha de volta.

Usamos dados abertos da NASA, do portal Mars Trek, que reúne mapas e relevo de Marte.

## 4. Público e diferenciais (1:40 – 2:00)

Beneficia astronautas, e a mesma lógica serve para resgate em desertos e regiões polares aqui na Terra. Nosso diferencial: funciona offline, é simples de usar sob estresse e é honesto sobre a incerteza da posição.

## 5. Inovação e sustentabilidade (2:00 – 2:30)

**Inovação:** a navegação de hoje depende de satélites e internet. Nós invertemos a lógica: o Martian Map funciona primeiro sem sinal e só depois sincroniza, combinando três fontes de localização e mostrando o nível de confiança da posição.

**Sustentabilidade:** projetamos um sistema leve, com baixo consumo de energia, que reduz a dependência de infraestrutura e de operações de resgate caríssimas, e que pode ser reaproveitado na Terra, com o guia atualizado a cada missão.

## 6. Validação (2:30 – 2:48)

Já temos um protótipo funcionando: um script em Python que baixa os mapas de Marte direto do NASA Mars Trek, em blocos (tiles), e os guarda no dispositivo para uso offline. *(pausa)* Dá para escolher o tamanho da área baixada: antes da missão, a equipe carrega o mapa da região de exploração. Quanto maior a área, mais armazenamento é preciso, e esse é o equilíbrio que o sistema permite ajustar para um dispositivo pequeno. Sobre esse mapa offline, vamos construir o Modo Perdido.

## 7. Chamada para ação (2:48 – 3:00)

Hoje buscamos parcerias para testar o Martian Map em cenários reais, como simulações de missão e áreas remotas aqui na Terra. *(pausa)* Porque explorar Marte não é só chegar lá. É voltar vivo. Somos a equipe Jekll, e este é o Martian Map. Obrigado!

---

## Antes de ensaiar

- **Tempo.** Se estourar, cortem nesta ordem: a frase da tempestade de 2018 e, por último, o item 4.
- **Item 6 (validação).** O que está pronto: download de tiles do Mars Trek com área configurável e armazenamento offline. **Modo Perdido, traje e bateria são próximos passos.** Falem assim, para a banca não entender que já funcionam.
- **Dados do item 2.** Confirmem no site da NASA o atraso de sinal, a área de Marte e a tempestade de 2018, e falem só o que dominam. A camada do Mars Trek que usamos é `Mars_Viking_MDIM21_ClrMosaic_global_232m` e pode ser citada.
- **Bateria e sustentabilidade.** Falem como meta ("projetamos"); ainda não foi medido.
- **Submissão.** O pitch não substitui o envio no site do NASA Space Apps. Lá é preciso descrever o uso de IA (veja [`uso-de-ia.md`](uso-de-ia.md)).

## O que dizer sobre o que existe hoje

O pitch fala do **script de tiles**. O repositório tem, além dele, um **app web instalável (PWA)** de demonstração. Se a banca perguntar ou se houver demo, descrevam assim:

| Pode dizer | Não diga |
|-----------|----------|
| "Temos um app de demonstração que mostra a interface, com mapa real de Marte salvo no dispositivo" | "O traje já está integrado" |
| "Os alertas do traje são **simulados** para mostrar o fluxo" | "O app detecta emergências reais" |
| "O guia tem 5 checklists de exemplo, ainda a validar" | "São procedimentos oficiais da NASA" |
| "O Modo Perdido é o próximo passo" | "O Modo Perdido funciona" |

## Demo (se houver tempo e tela)

Siga [Como rodar](../README.md#como-rodar). Roteiro de 30 segundos:

1. Abrir o app em **http://localhost:8000/os/app/** e mostrar o mapa de Marte.
2. Desligar a rede (modo avião ou DevTools > Network > Offline): o app e o mapa continuam funcionando.
3. Aba **Traje**: arrastar a *Reserva de O₂* abaixo de 20 %. O alerta abre com vibração.
4. Tocar em **Ver rota até o abrigo** e mostrar a rota no mapa.

## Perguntas prováveis

**Como o Modo Perdido sabe onde estou?**
Combina três fontes: satélites, relevo e ângulo do Sol. Ainda é o próximo passo; o desenho está em [`modo-perdido.md`](modo-perdido.md). A confiança é mostrada justamente porque nenhuma fonte é perfeita sozinha.

**Por que não usar só GPS?**
Marte não tem uma rede de GPS, e depender de satélite ou internet é o que falha primeiro em uma emergência. Por isso o sistema é offline primeiro.

**O que acontece se o mapa não couber no dispositivo?**
A área baixada é configurável. Quanto maior a região e o zoom, mais armazenamento. Cada nível de zoom a mais multiplica os tiles por cerca de 4. Dá para escolher só a região de exploração da missão.

**Quanto de armazenamento isso usa?**
Na região de exemplo (cerca de 590 × 560 km, zoom 0 a 7, 107 tiles) o app inteiro tem cerca de 6 MB. É um número do protótipo, não de um dispositivo final.

**Os dados são oficiais?**
Os mapas vêm do NASA/JPL Mars Trek. Os procedimentos do guia e os limites do traje são **exemplos da equipe**, a validar com fontes da NASA.

**E a bateria de semanas?**
É uma meta de projeto. Ainda não foi medida; ela depende do hardware.

**Qual é a resolução do mapa?**
A camada usada tem cerca de 232 m/pixel. Serve para orientação geral, não para detalhe fino de terreno.

**Funciona com luvas?**
Projetamos alvos de toque grandes (44 a 72 px) e um fluxo de um botão, mas ainda **não testamos com luvas reais**.

**Como usa na Terra?**
Desertos e regiões polares têm o mesmo problema: pouca infraestrutura, comunicação ruim e terreno que confunde. Buscamos parceiros para testar nesses cenários.

## Links

- Vídeo, slides e demo: ver o final do [README](../README.md#demo-e-apresentação) (a preencher).
