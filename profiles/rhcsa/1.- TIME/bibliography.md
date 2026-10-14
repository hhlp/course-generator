# Bibliography — TIME / NTP / Chrony — en profundidad

## Referencias operativas principales

- Chrony Project — documentación oficial de `chronyd`, `chronyc` y `chrony.conf`.
- Red Hat Enterprise Linux — documentación de configuración y administración de Chrony.
- Fedora Documentation — administración de fecha/hora y servicios relacionados.
- Manuales instalados: `chrony.conf(5)`, `chronyd(8)`, `chronyc(1)`,
  `timedatectl(1)`, `hwclock(8)`, `date(1)`.

## Protocolos y seguridad

- RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification.
- RFC 8915 — Network Time Security for the Network Time Protocol.
- RFC 8633 — Network Time Protocol Best Current Practices.

## Linux internals

- Linux kernel documentation — timekeeping, clocksources, timers, PPS and PTP
  subsystems, according to the kernel version being studied.
- Linux man-pages — `clock_gettime(2)`, `adjtimex(2)`, `clock_adjtime(2)`,
  `time_namespaces(7)` and related interfaces.

## PTP / hardware timestamping

- IEEE 1588 — Precision Time Protocol.
- linuxptp — documentation for `ptp4l`, `phc2sys`, `pmc` and related tools.
- Linux kernel networking documentation — timestamping and PTP Hardware Clock.

## Uso de las fuentes

La documentación de Chrony y Fedora/RHEL es la referencia operativa. Los RFC
se utilizan para estudiar NTP/NTS en profundidad; la documentación del kernel
para Linux timekeeping; IEEE 1588 y linuxptp para PTP. Deben contrastarse los
detalles con las versiones realmente instaladas en los laboratorios.
