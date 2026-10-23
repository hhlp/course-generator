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


## Enlaces operativos concretos y control de versiones

- [Chrony — documentación por versión](https://chrony-project.org/documentation.html).
  Elegir la versión instalada; `latest` es una referencia móvil.
- [chrony.conf](https://chrony-project.org/doc/latest/chrony.conf.html): fuentes,
  selección, `minsamples`, `maxsamples`, `local`, `orphan`, NTS y refclocks.
- [chronyc](https://chrony-project.org/doc/latest/chronyc.html): `waitsync`,
  `authdata`, `selectdata`, métricas y códigos de salida.
- [chronyd](https://chrony-project.org/doc/latest/chronyd.html): opciones de
  inicio, impresión de configuración y medición sin ajustar el reloj.
- [Chrony FAQ](https://chrony-project.org/faq.html): número de fuentes,
  precisión, NTS, virtualización y diagnóstico.
- [RHEL 9 — Configuring time synchronization](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/configuring-time-synchronization_configuring-basic-system-settings).
  Referencia de una versión concreta; contrastar paquetes y defaults con el
  RHEL del laboratorio y comprobar los puertos en el manual upstream.
- [Fedora Docs](https://docs.fedoraproject.org/): consultar la edición utilizada.

## Protocolos y APIs: referencias enlazadas

- [RFC 5905 — NTPv4](https://www.rfc-editor.org/rfc/rfc5905.html).
- [RFC 8915 — NTS](https://www.rfc-editor.org/rfc/rfc8915.html).
- [RFC 8633 — NTP Best Current Practices](https://www.rfc-editor.org/rfc/rfc8633.html).
- [RFC 4120 — Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120.html):
  relación entre hora, tickets y comprobaciones de desfase.
- [Linux time namespaces](https://man7.org/linux/man-pages/man7/time_namespaces.7.html):
  relojes virtualizados y ausencia de virtualización de CLOCK_REALTIME.
- [Linux timekeeping](https://docs.kernel.org/core-api/timekeeping.html).
- [Linux timestamping](https://docs.kernel.org/networking/timestamping.html).
- [Linux PTP Hardware Clock](https://docs.kernel.org/driver-api/ptp.html).
- [linuxptp — documentación](https://www.linuxptp.org/documentation/):
  `ptp4l`, `phc2sys` y `pmc`; relacionar opciones con la versión instalada.
- [Linux tc-netem](https://man7.org/linux/man-pages/man8/tc-netem.8.html):
  inyección y retirada de fallos de red en el laboratorio.

## Correspondencia con el currículo

| Bloques | Referencias prioritarias |
|---|---|
| 0–7 | man instalados, Fedora/RHEL, manuales Chrony |
| 8–15 | chrony.conf, chronyc, FAQ, RFC 8633 y RFC 4120 |
| 16–17 | kernel PPS/PTP y linuxptp |
| 18–20 | chronyc, documentación del exportador elegido y Ansible |
| 21–25 | kernel, Linux man-pages, RFC 5905 y manuales Chrony |
| 26 | RFC 8915, NTS en chrony.conf y chronyc authdata |
| 27–28 | kernel timestamping/PTP y linuxptp |
| 29–31 | combinación de fuentes anteriores y versiones del laboratorio |

Registrar versión y fecha de consulta al desarrollar cada lección. Los algoritmos
descritos por un RFC y los de Chrony no deben presentarse como idénticos sin
contrastar implementación y documentación. La referencia normativa IEEE 1588
se elige según perfil y equipos utilizados; linuxptp aporta la guía operativa.
