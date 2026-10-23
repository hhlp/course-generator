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


## Relación con IAM y orden de despliegue

TIME es un servicio base que funciona sin LDAP, Kerberos o FreeIPA y no consume
identidades humanas. IAM depende de una hora suficientemente sincronizada,
especialmente para Kerberos. No se debe exigir un inicio de sesión contra IAM
para que Chrony obtenga la hora. Las identidades se administran en el PATH IAM.

Desplegar primero la base de red y una referencia temporal accesible. Si las
fuentes se definen por nombre, disponer de resolución inicial independiente del
DNS que todavía se está construyendo. Después desplegar DNS e IAM comprobando
sus requisitos. Este orden operativo no cambia el orden editorial de los PATH.
La práctica con Kerberos reutiliza un realm del curso IAM y es una extensión;
el aprendizaje y el funcionamiento de TIME no requieren desplegar IAM.

## Contrato de profundidad y progresión

Conservar los 32 bloques y las lecciones originales. Los bloques operativos
introducen uso y diagnóstico; los bloques de internals explican los algoritmos,
las hipótesis y las limitaciones mediante evidencia. No convertir la repetición
de un tema en una repetición literal de la lección. Distinguir las estimaciones
de Chrony de una medida independiente de exactitud respecto a UTC.

Las directivas de control de muestras se llaman `minsamples` y `maxsamples`.
Registrar Fedora/RHEL, kernel, Chrony y linuxptp utilizados; consultar los man
instalados antes de emplear opciones disponibles solo en algunas versiones.
La validez sintáctica del archivo no demuestra sincronización del reloj.

## Arquitectura y seguridad operativa

Dos servidores pueden aportar continuidad, pero no resuelven por sí solos una
discrepancia entre fuentes. Estudiar tres o cuatro fuentes independientes y
medir también dependencias compartidas. No presentar `prefer` como garantía
de corrección. En redes aisladas, `local` y `orphan` permiten una referencia
interna coherente; no acreditan exactitud respecto a UTC.

Separar NTP en UDP/123, NTS-KE en TCP/4460 y el protocolo de administración
chronyc, normalmente local mediante socket Unix, con UDP/323 cuando proceda.
No abrir el puerto de administración como requisito para usar NTP o NTS.
Aplicar reglas por función y red en IPv4/IPv6; comprobar permisos y SELinux.

NTS se practica con cliente y servidor, CA de laboratorio, certificados con
nombres válidos, claves restringidas y renovación verificada. Ante fallos,
comprobar hora inicial, CA, DNS, certificado, TCP/4460 y UDP/123. No enseñar
la desactivación permanente de validación TLS como solución de arranque.
NTS autentica el intercambio; no elimina el error de la fuente ni la asimetría.

## Laboratorio reproducible

Base: tres VM Fedora/RHEL, un servidor y dos clientes, red privada y snapshots.
Extensión de selección: tres o cuatro fuentes controladas y al menos un cliente;
las VM de simulación no cuentan como referencias UTC independientes si comparten
el mismo host. Documentar direcciones, rutas, resolución, configuración por nodo,
versiones, acceso externo autorizado y límites de CPU/memoria del entorno.

Cada práctica incluye objetivo, prerrequisitos, estado inicial, procedimiento,
resultado esperado, criterio medible, evidencias y recuperación. Los cambios de
hora y `netem` se ejecutan en VM/redes desechables. Un contenedor no aísla el
reloj `CLOCK_REALTIME` del host mediante time namespaces.

La variante NTS utiliza una CA propia del laboratorio y una hora inicial fiable.
PPS/GNSS/PHC requieren dispositivos compatibles. PTP por software permite
aprender protocolo y operación, sin demostrar precisión de hardware. En cada
arquitectura Chrony/PTP asignar un único proceso disciplinador a cada reloj;
evitar ajustes simultáneos del reloj del sistema por chronyd y phc2sys.

## Aceptación y evaluación

- Registrar `tracking`, `sources`, `sourcestats` y, según versión, `selectdata`,
  `authdata` y `ntpdata`; correlacionarlos con journal, logs y capturas.
- Fijar presupuesto de error y ventana de convergencia por escenario. Como
  ejemplo didáctico en LAN, esperar con `chronyc waitsync 60 0.01 1 2`
  hasta 60 comprobaciones, corrección pendiente menor de 10 ms y skew menor
  de 1 ppm, con intervalo de 2 s. Adaptar al entorno y tratar un timeout como
  fallo. Esto no certifica por sí solo una exactitud absoluta de 10 ms.
- Mostrar recuperación tras pérdida de fuente, DNS roto, bloqueo de NTP/NTS-KE
  y reinicio; preservar evidencias antes de introducir nuevas correcciones.
- Automatizar validación, despliegue gradual, espera acotada e idempotencia.
- Demostrar NTS en el laboratorio controlado. En el proyecto de arquitectura,
  justificar disponibilidad, compatibilidad y política sin fallback silencioso.
- Entregar configuraciones por nodo, inventario, runbook, métricas y RCA.
  La extensión de hardware queda condicionada a disponibilidad documentada.

Estos cuatro archivos especifican el currículo; los playbooks, configuraciones
completas y scripts ejecutables se desarrollan en sus lecciones y proyecto.
