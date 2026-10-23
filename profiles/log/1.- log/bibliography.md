# BIBLIOGRAPHY — LOGGING EN LINUX — FEDORA

## Criterio general

La documentación oficial y las páginas man instaladas en Fedora son la referencia principal para comportamiento actual, sintaxis y opciones disponibles.

La bibliografía secundaria se utiliza para aportar arquitectura, contexto histórico, patrones de diseño, administración y profundidad conceptual.

No asumir que un libro antiguo describe exactamente las versiones actuales de systemd, rsyslog o syslog-ng.

## Principal — documentación oficial de Fedora y componentes upstream

### Fedora Documentation

Uso principal:

- contexto específico de Fedora;
- instalación de paquetes;
- administración del sistema;
- SELinux;
- firewalld;
- systemd;
- prácticas recomendadas del ecosistema Fedora.

Sitio:

- Fedora Documentation

## systemd / journald

### systemd upstream documentation

Documentación esencial para:

- systemd-journald
- journalctl
- journald.conf
- systemd.journal-fields
- systemd.service
- systemd.exec
- namespaces de logging
- Forward Secure Sealing
- almacenamiento y rotación del journal

Páginas man prioritarias:

- systemd-journald.service(8)
- journalctl(1)
- journald.conf(5)
- systemd.journal-fields(7)
- systemd.journal-remote(8), cuando se mencione como integración
- systemd.journal-upload(8), cuando proceda
- systemd.service(5)
- systemd.exec(5)
- systemd-system.conf(5)
- systemd-cat(1)
- logger(1)

Uso por bloques:

- bloques 2–11
- bloque 37
- bloque 38
- troubleshooting
- internals

## Syslog — estándares

### RFC 3164 — The BSD Syslog Protocol

Uso:

- formato tradicional de Syslog;
- limitaciones históricas;
- comparación con RFC 5424.

Nota:

RFC 3164 es histórica/informativa y no debe presentarse como el estándar moderno principal.

### RFC 5424 — The Syslog Protocol

Referencia central para:

- PRI
- VERSION
- TIMESTAMP
- HOSTNAME
- APP-NAME
- PROCID
- MSGID
- STRUCTURED-DATA
- MSG
- NILVALUE

Uso principal:

- bloques 12–14
- parsing
- logging estructurado

### RFC 5425 — Transport Layer Security (TLS) Transport Mapping for Syslog

Uso:

- Syslog sobre TLS;
- autenticación;
- integridad;
- confidencialidad;
- transporte seguro.

### RFC 6587 — Transmission of Syslog Messages over TCP

Uso:

- framing sobre TCP;
- octet counting;
- non-transparent framing.

## rsyslog

### rsyslog official documentation

Referencia principal para rsyslog moderno.

Temas prioritarios:

- RainerScript
- input()
- ruleset()
- action()
- template()
- property replacer
- imjournal
- imuxsock
- imudp
- imtcp
- imfile
- omfile
- omfwd
- queues
- disk-assisted queues
- TLS
- statistics / impstats
- parsing
- mmnormalize
- mmjsonparse
- RELP

Uso principal:

- bloques 15–24
- bloque 31
- bloques 39–44

### Rainer Gerhards / rsyslog knowledge base and whitepapers

Uso complementario:

- arquitectura interna;
- diseño de queues;
- reliability;
- performance;
- semánticas de forwarding;
- explicación conceptual de RainerScript.

## RELP

### librelp / RELP upstream documentation

Uso:

- Reliable Event Logging Protocol;
- sesiones y acknowledgements;
- imrelp / omrelp;
- RELP sobre TLS;
- límites reales de entrega.

No describir RELP como exactamente-once extremo a extremo.

## syslog-ng

### syslog-ng Open Source Edition documentation

Referencia principal para:

- source()
- destination()
- filter()
- parser()
- rewrite()
- template()
- log paths
- junctions
- channels
- flow-control
- disk-buffer
- networking
- TLS
- macros
- structured data

Uso principal:

- bloques 25–30
- bloque 31
- bloques 39–44

### syslog-ng Administration Guide

Uso:

- arquitectura;
- configuración completa;
- patterns de routing;
- parsing;
- buffering;
- troubleshooting.

## logrotate

### logrotate upstream documentation

Fuentes principales:

- logrotate(8)
- logrotate.conf(5), si está disponible como página separada en la versión instalada
- README / documentación upstream

Temas:

- rotate
- size
- minsize
- maxsize
- compress
- delaycompress
- create
- su
- dateext
- olddir
- copy
- copytruncate
- renamecopy
- prerotate
- postrotate
- firstaction
- lastaction
- sharedscripts
- state file

Uso principal:

- bloques 34–36
- troubleshooting
- proyecto final

## Linux y administración de sistemas

### Michael Kerrisk — The Linux Programming Interface

Profundización para:

- file descriptors;
- open/read/write;
- rename/unlink;
- pipes;
- Unix domain sockets;
- sockets TCP/UDP;
- signals;
- filesystem;
- process model;
- kernel interfaces.

Uso especialmente útil en:

- bloque 36
- bloque 38
- bloque 44

No utilizarlo como fuente primaria para configuración de herramientas modernas.

### W. Richard Stevens et al. — UNIX Network Programming

Consulta avanzada para:

- sockets;
- TCP/UDP;
- buffering;
- conexión y transporte;
- comportamiento de red relevante para logging remoto.

Uso selectivo en:

- bloques 14, 23, 24, 29–31, 40–44.

## systemd — profundización

### Linux Service Management Made Easy with systemd

Uso complementario para:

- servicios;
- stdout/stderr;
- units;
- journald;
- integración de aplicaciones con systemd.

No sustituye las páginas man actuales de systemd.

## SELinux

### Sven Vermeulen — SELinux System Administration, Third Edition

Uso complementario para:

- labels;
- contexts;
- type enforcement;
- AVC;
- troubleshooting;
- semanage fcontext;
- restorecon;
- servicios de red.

Uso principal dentro de este PATH:

- bloque 39
- troubleshooting
- laboratorios de integración

La referencia definitiva para comportamiento concreto en Fedora debe seguir siendo la política y documentación instaladas/actuales.

## Redes y TLS

### OpenSSL documentation

Uso:

- certificados X.509;
- cadenas de confianza;
- inspección de certificados;
- openssl s_client;
- troubleshooting de TLS.

### RFC 5280 — Internet X.509 Public Key Infrastructure Certificate and CRL Profile

Uso de consulta avanzada cuando sea necesario explicar:

- cadenas de certificados;
- CA;
- nombres;
- validación;
- expiración.

No profundizar hasta convertir el PATH en un curso de PKI.

## JSON y datos estructurados

### RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format

Uso de consulta para:

- JSON válido;
- strings;
- números;
- arrays;
- objects;
- interoperabilidad durante parsing y logging estructurado.

## Bibliografía por nivel

### Principal

- documentación de Fedora
- systemd upstream + man pages
- rsyslog official documentation
- syslog-ng official documentation
- logrotate documentation
- RFC 5424

### Complementaria

- RFC 3164
- RFC 5425
- RFC 6587
- librelp documentation
- Linux Service Management Made Easy with systemd
- SELinux System Administration, Third Edition

### Profundización

- The Linux Programming Interface
- UNIX Network Programming
- documentación de internals de rsyslog/syslog-ng/systemd cuando sea necesaria

### Consulta

- RFC 5280
- RFC 8259
- documentación OpenSSL
- páginas man instaladas en Fedora

## Política de uso de referencias en las lecciones

Las lecciones deben priorizar fuentes en este orden:

1. documentación oficial del componente;
2. páginas man de la versión instalada;
3. documentación Fedora;
4. RFC aplicable;
5. documentación upstream de librerías relacionadas;
6. libros de profundización.

Cuando exista discrepancia entre un libro y la documentación actual, prevalece la documentación actual.

## Comandos de descubrimiento bibliográfico local

El alumno debe aprender a consultar documentación disponible en el propio sistema mediante:

- man journalctl
- man systemd-journald.service
- man journald.conf
- man systemd.journal-fields
- man systemd.exec
- man systemd.service
- man logger
- man rsyslogd
- man rsyslog.conf
- rsyslogd -v
- rsyslogd -N1
- syslog-ng --version
- syslog-ng --syntax-only
- man logrotate
- rpm -qd <paquete>
- rpm -ql <paquete>
- dnf info <paquete>

## Referencias bibliográficas específicas

- The systemd Project. systemd documentation and manual pages.
- Fedora Project. Fedora Documentation.
- Rainer Gerhards et al. rsyslog Documentation.
- syslog-ng project. syslog-ng Open Source Edition documentation, matched to the installed release. AxoSyslog documentation is a separate reference for explicitly identified comparisons.
- logrotate project. logrotate documentation and manual page.
- IETF RFC 5424. The Syslog Protocol.
- IETF RFC 5425. Transport Layer Security (TLS) Transport Mapping for Syslog.
- IETF RFC 6587. Transmission of Syslog Messages over TCP.
- RFC 3164. The BSD Syslog Protocol.
- librelp project documentation.
- Michael Kerrisk. The Linux Programming Interface. No Starch Press.
- W. Richard Stevens, Bill Fenner, Andrew Rudoff. UNIX Network Programming, Volume 1: The Sockets Networking API.
- Sven Vermeulen. SELinux System Administration, Third Edition.
- Linux Service Management Made Easy with systemd.
- IETF RFC 5280. Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List Profile.
- IETF RFC 8259. The JavaScript Object Notation (JSON) Data Interchange Format.

## Referencias ampliadas por scope — revisión profunda

### Linux Audit (bloque 45)
- Linux Audit upstream y páginas man instaladas: `auditd(8)`, `auditd.conf(5)`, `auditctl(8)`, `audit.rules(7)`, `ausearch(8)`, `aureport(8)`, `augenrules(8)` y `auditd-plugins(5)` cuando estén disponibles.
- Documentación Fedora/RHEL de auditoría, usada como contexto operativo y verificada frente a Fedora actual.

### Logging de aplicaciones y Podman (bloque 46)
- Documentación oficial Podman: `podman-logs(1)`, `podman-run(1)` y configuración de contenedores `containers.conf(5)`.
- `systemd.exec(5)`, `systemd-cat(1)` y `sd_journal_send(3)` para integración nativa.
- RFC 8259 para JSON; documentación de los lenguajes y frameworks empleados en laboratorios.

### Seguridad y forense (bloque 47)
- RFC 5848 — Signed Syslog Messages: referencia conceptual, no asumir implementación universal.
- NIST SP 800-92 — Guide to Computer Security Log Management (guía histórica; contrastar prácticas actuales).
- Documentación oficial de SELinux, OpenSSL y systemd journal sealing.
- RFC 3161 cuando se explique sellado de tiempo externo, sin convertir el PATH en un curso PKI.

### Operación y estadísticas (bloque 48)
- Documentación rsyslog `impstats` y páginas de queues, actions y troubleshooting.
- Documentación syslog-ng `syslog-ng-ctl`, estadísticas, persist files y disk-buffer.
- `journalctl(1)`, `journald.conf(5)`, `ss(8)`, `df(1)` y `stat(1)`.

### Resiliencia y transporte (bloque 49)
- RFC 5426 — Transmission of Syslog Messages over UDP.
- RFC 5425 y RFC 6587 para comparar TLS y framing TCP.
- Documentación upstream de rsyslog, librelp y syslog-ng sobre buffering, reconexión, fiabilidad y límites de entrega.

### Política de bibliografía por lección
Indicar scope y bloque correspondiente, separar documentación oficial vigente de bibliografía histórica, y comprobar soporte de módulos, flags y configuración en la versión Fedora instalada.

## Referencias verificables y correspondencia de versiones — 2026-10-22

La documentación latest puede describir funciones posteriores al paquete instalado. Registrar versión y consultar el manual o rama correspondiente. Si dos páginas upstream discrepan, explicitar la discrepancia y verificar el comportamiento; no inferir garantías de persistencia.

| Referencia oficial | Aplicación en el PATH |
| --- | --- |
| [Fedora Docs](https://docs.fedoraproject.org/) | Paquetes, plataforma y operación |
| [journald.conf](https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html) | Persistencia, límites, forwarding, namespaces y streams |
| [systemd-journald.service](https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html) | Captura, sockets y ciclo de vida |
| [journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) | Consultas, cursores, exportación y mantenimiento |
| [systemd.exec](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) | Integración de servicios |
| [journal-upload](https://www.freedesktop.org/software/systemd/man/latest/systemd-journal-upload.service.html) | Alternativa de transporte de journal |
| [journal-remote](https://www.freedesktop.org/software/systemd/man/latest/systemd-journal-remote.service.html) | Recepción de journal remoto |
| [rsyslog](https://docs.rsyslog.com/doc/index.html) | Configuración, módulos y colas |
| [Validación rsyslog](https://www.rsyslog.com/how-can-i-check-the-config/) | -N1; comprobar también el manual instalado |
| [imfile](https://docs.rsyslog.com/doc/configuration/modules/imfile.html) | Lectura de archivos, estados y rotación |
| [PersistStateInterval](https://docs.rsyslog.com/doc/reference/parameters/imfile-persiststateinterval.html) | Frecuencia de persistencia del estado; contrastar documentación de la versión |
| [syslog-ng OSE](https://syslog-ng.github.io/admin-guide/) | Manual del proyecto; distinguir de otros productos |
| [Opciones syslog-ng](https://syslog-ng.github.io/admin-guide/070_Destinations/300_syslog/000_syslog_destination_options.html) | Nombres y unidades de buffers por versión |
| [Buffering syslog-ng](https://syslog-ng.github.io/admin-guide/080_Log/020_Buffering/README.html) | Fiabilidad y control de flujo |
| [logrotate](https://github.com/logrotate/logrotate) | Manual upstream y comportamiento de rotación |
| [Linux Audit](https://github.com/linux-audit/audit-userspace) | auditd, reglas, consultas y rotación propia |
| [Podman](https://docs.podman.io/en/latest/) | Drivers, consulta y ciclo de vida de logs |
| [RFC 5426](https://www.rfc-editor.org/rfc/rfc5426.html) | Transporte UDP |
| [RFC 5848](https://www.rfc-editor.org/rfc/rfc5848.html) | Syslog firmado, de alcance conceptual |

Las referencias de libros se conservan como apoyo conceptual. No usar su sintaxis histórica como prueba de disponibilidad actual. Cada lección debe enlazar la referencia oficial concreta utilizada y especificar cualquier requisito de versión.
