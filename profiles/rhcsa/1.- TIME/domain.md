# Domain — TIME / NTP / Chrony — 0 a experto en profundidad

## Objetivo

Formar a un administrador/ingeniero capaz no solo de operar Chrony/NTP en
Fedora y RHEL, sino de comprender cómo Linux mide y disciplina el tiempo,
cómo NTPv4 obtiene sus estimaciones, cómo Chrony filtra y selecciona fuentes,
cómo se diagnostican anomalías a partir de evidencia y cuándo deben emplearse
NTS, PPS, hardware timestamping o PTP.

## Capas del dominio

1. Administración Linux: `date`, `timedatectl`, `hwclock`, systemd.
2. NTP: protocolo, jerarquía, timestamps, offset, delay, jitter y stratum.
3. Chrony: instalación, configuración, cliente/servidor, `chronyd`, `chronyc`.
4. Operación: firewalld, SELinux, redes aisladas, HA y multi-site.
5. Observabilidad: journald, `/var/log/chrony`, métricas y capturas.
6. Linux internals: clocksources, clockevents, vDSO, timers y clock discipline.
7. NTPv4 internals: formato, cuatro timestamps, polling, reach y selección.
8. Chrony internals: filtrado, regresión, frecuencia, skew y source selection.
9. Seguridad: NTS y análisis de su flujo.
10. Precisión avanzada: GPS/GNSS, PPS, PHC, hardware timestamping y PTP.
11. Ingeniería: monitorización, Ansible, troubleshooting forense y RCA.

## Política de logs

El diagnóstico del servicio comienza por systemd-journald:

    journalctl -u chronyd
    journalctl -u chronyd -b
    journalctl -f -u chronyd

No debe asumirse que existe `/var/log/chronyd.log`.

Chrony puede escribir logs de datos específicos cuando se habilitan categorías
mediante `log` y se configura `logdir`. En Fedora/RHEL una ubicación habitual
es `/var/log/chrony/`. Según la configuración pueden existir, entre otros:

- `measurements.log`
- `statistics.log`
- `tracking.log`
- `rtc.log`
- `tempcomp.log`

El curso debe enseñar a verificar la configuración efectiva y correlacionar
journal, archivos Chrony, `chronyc`, métricas y tráfico de red.

## Nivel experto en profundidad

El alumno debe ser capaz de explicar el porqué de una decisión de sincronización
y no limitarse a ejecutar comandos. Debe poder relacionar:

paquete NTP → measurement → filtrado → estimación estadística → selección de
source → disciplina del kernel → métricas → logs → comportamiento observado.

## Resultado final

Diseñar, desplegar, asegurar, automatizar, monitorizar y realizar RCA sobre una
infraestructura de tiempo RHEL, justificando cuándo utilizar NTP/Chrony, NTS,
PPS/hardware timestamping o PTP.
