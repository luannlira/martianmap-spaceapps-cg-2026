

# Smart suit

Identification of critical situations by the spacesuit and sending of alerts to the device. *Suggestion: João.*

## Status

- [x] Simulation of 4 sensors in the app, with a full-screen alert + vibration ([`os/app/index.html`](../os/app/index.html))
- [x] Each alert links to the right checklist and to the route to the shelter
- [ ] Real telemetry protocol (suit → device)
- [ ] Limits validated with NASA sources
- [ ] Test with real hardware

> The telemetry is **simulated** by sliders on the **Traje** (Suit) tab. Nothing here reads a real suit.

## Simulated sensors and limits

Defined in `SENS` (sensors) in `index.html`. They are **team examples**, not official values.

| Sensor | Range | Alert when | Checklist opened |
|--------|-------|------------|------------------|
| O₂ reserve (*Reserva de O₂*) | 0–100% | < 20% | Pouco oxigênio (Low oxygen) |
| Suit pressure (*Pressão do traje*) | 10–35 kPa | < 24 kPa | Perda de pressão (Pressure loss) |
| Internal temperature (*Temperatura interna*) | 10–45 °C | > 30 °C | Temperatura alta (High temperature) |
| Airborne dust (*Poeira no ar*) | 0–100% | > 70% | Tempestade de poeira (Dust storm) |

## Alert behavior

1. A value crosses its limit → full-screen alert, vibration (`navigator.vibrate`) and a critical banner on the Mapa (Map) tab.
2. The user chooses: **Ver rota até o abrigo** (View route to the shelter), **Abrir checklist** (Open checklist) or **Dispensar** (Dismiss).
3. Once dismissed, that sensor's alert only comes back after the value returns to normal.
4. When no sensor is out of range, the banner goes back to normal and the route disappears.

## To test

**Traje** tab → drag *Reserva de O₂* (O₂ reserve) below 20% (see [How to run](../README.md#how-to-run)).

## Ideas for the real integration (to be defined)

- Which channel connects suit and device (cable, short-range radio) and what message format travels over it.
- Minimum message per reading: sensor, value, unit, time. Alert message: sensor, level, time.
- Alert priority when more than one fires at the same time (today: the first in the list).
- The remaining oxygen feeds the shelter choice in [Lost Mode (*Modo Perdido*)](../docs/modo-perdido.md) (in Portuguese).
- Fail-safe: if the telemetry disappears, the device must warn the user, not assume everything is fine.

## Open items

- Define the limits and units of each sensor with official sources.
- Decide which other sensors to include (e.g. CO₂, radiation, heart rate).
