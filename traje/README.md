

# Traje inteligente

Identificação de situações críticas pelo traje espacial e envio de alertas ao dispositivo. *Sugestão: João.*

## Status

- [x] Simulação de 4 sensores no app, com alerta em tela cheia + vibração ([`os/app/index.html`](../os/app/index.html))
- [x] Cada alerta liga ao checklist certo e à rota até o abrigo
- [ ] Protocolo real de telemetria (traje → dispositivo)
- [ ] Limites validados com fontes da NASA
- [ ] Teste com hardware real

> A telemetria é **simulada** por controles deslizantes na aba Traje. Nada aqui lê um traje real.

## Sensores simulados e limites

Definidos em `SENS` no `index.html`. São **exemplos da equipe**, não valores oficiais.

| Sensor | Faixa | Alerta quando | Checklist aberto |
|--------|-------|---------------|------------------|
| Reserva de O₂ | 0–100 % | < 20 % | Pouco oxigênio |
| Pressão do traje | 10–35 kPa | < 24 kPa | Perda de pressão |
| Temperatura interna | 10–45 °C | > 30 °C | Temperatura alta |
| Poeira no ar | 0–100 % | > 70 % | Tempestade de poeira |

## Comportamento do alerta

1. Valor ultrapassa o limite → alerta em tela cheia, vibração (`navigator.vibrate`) e banner crítico no Mapa.
2. O usuário escolhe: **Ver rota até o abrigo**, **Abrir checklist** ou **Dispensar**.
3. Dispensado, o alerta daquele sensor só volta depois que o valor retornar ao normal.
4. Quando nenhum sensor está fora do limite, o banner volta ao normal e a rota some.

## Para testar

Aba **Traje** → arraste a *Reserva de O₂* para menos de 20 % (ver [Como rodar](../README.md#como-rodar)).

## Ideias para a integração real (a definir)

- Qual canal liga traje e dispositivo (cabo, rádio de curto alcance) e que formato de mensagem trafega.
- Mensagem mínima por leitura: sensor, valor, unidade, hora. Mensagem de alerta: sensor, nível, hora.
- Prioridade dos alertas quando mais de um dispara ao mesmo tempo (hoje: o primeiro da lista).
- O oxigênio restante alimenta a escolha do abrigo no [Modo Perdido](../docs/modo-perdido.md).
- Falha segura: se a telemetria sumir, o dispositivo deve avisar, e não assumir que está tudo bem.

## Pendências

- Definir com fontes oficiais os limites e as unidades de cada sensor.
- Decidir outros sensores a incluir (ex.: CO₂, radiação, batimentos).
