# BIBLIOGRAFÍA — NAGIOS EN PROFUNDIDAD — FEDORA/RHEL

## 1. Política bibliográfica

La documentación primaria tiene prioridad sobre libros, artículos y tutoriales.

Orden general de autoridad:

1. documentación oficial del componente
2. código fuente oficial
3. documentación Fedora/RHEL
4. manuales de herramientas del sistema
5. libros técnicos
6. fuentes comunitarias de calidad.

Cuando existan diferencias entre una fuente secundaria y la documentación correspondiente a la versión utilizada, prevalece la documentación primaria.


# 2. NAGIOS CORE — FUENTE PRINCIPAL

## Documentación oficial de Nagios Core

Fuente principal para:

arquitectura
configuración
objects
hosts
services
commands
checks
active checks
passive checks
state types
timeperiods
notifications
event handlers
dependencies
escalations
freshness
flapping
macros
external commands
performance data
retention
CGI
distributed monitoring
security
tuning.

Sitio oficial:

https://www.nagios.org/

Documentación:

https://assets.nagios.com/downloads/nagioscore/docs/

Debe consultarse la documentación correspondiente a la versión estudiada.


# 3. NAGIOS CORE — CÓDIGO FUENTE

Repositorio oficial de Nagios Core:

https://github.com/NagiosEnterprises/nagioscore

Fuente prioritaria para los bloques de internals.

Utilizar para estudiar:

startup
configuration parsing
object structures
scheduler
event queue
timed events
workers
check processing
state processing
notifications
event handlers
dependencies
escalations
macro processing
external commands
retention
logging
performance data
Event Broker
NEB
CGI.

El código fuente complementa la documentación; no debe sustituir innecesariamente las explicaciones conceptuales.


# 4. NAGIOS PLUGINS

Proyecto Nagios Plugins:

https://www.nagios-plugins.org/

Documentación:

https://www.nagios-plugins.org/doc/

Repositorio:

https://github.com/nagios-plugins/nagios-plugins

Fuente principal para:

plugin API
exit codes
thresholds
performance data
check_disk
check_load
check_http
check_ping
check_procs
check_users
check_swap
check_tcp
check_dns
check_ssh
otros plugins estándar.


# 5. NAGIOS PLUGIN DEVELOPMENT GUIDELINES

Nagios Plugin Development Guidelines.

Fuente fundamental para comprender:

return codes
stdout
output format
thresholds
ranges
performance data
timeouts
argument handling
plugin conventions.

Debe utilizarse especialmente en:

Plugin API
desarrollo básico de plugins
troubleshooting de plugins.


# 6. NRPE

Repositorio oficial:

https://github.com/NagiosEnterprises/nrpe

Utilizar para:

arquitectura NRPE
check_nrpe
daemon
configuración
allowed hosts
commands
SSL/TLS
seguridad
compilación
troubleshooting.

La documentación debe contrastarse con la versión concreta de NRPE utilizada.


# 7. NCPA

Documentación oficial:

https://www.nagios.org/ncpa/

Documentación técnica:

https://www.nagios.org/ncpa/help/

Repositorio:

https://github.com/NagiosEnterprises/ncpa

Fuente principal para:

arquitectura NCPA
listener
API
tokens
TLS
checks
métricas
passive component
integración Nagios
troubleshooting.


# 8. FEDORA

Fedora Documentation:

https://docs.fedoraproject.org/

Fedora Packages:

https://packages.fedoraproject.org/

Fedora Package Sources:

https://src.fedoraproject.org/

Utilizar para:

paquetes
versiones
archivos instalados
systemd
SELinux
firewalld
Apache
RPM
DNF
integración con Fedora.

Las rutas y características proporcionadas por los paquetes Fedora deben verificarse frente al paquete real cuando sea necesario.


# 9. RPM Y DNF

RPM:

https://rpm.org/

DNF:

https://dnf.readthedocs.io/

Utilizar para:

instalación
consulta de paquetes
archivos
configuración empaquetada
dependencias
descubrimiento del entorno.


# 10. SYSTEMD

Documentación oficial:

https://systemd.io/

Man pages:

systemd(1)
systemctl(1)
systemd.service(5)
systemd.unit(5)
journalctl(1)
journald.conf(5)

Utilizar para:

servicio Nagios
lifecycle
logging
dependencias
overrides
hardening.


# 11. SELINUX

Fedora SELinux documentation:

https://docs.fedoraproject.org/

Red Hat SELinux documentation:

https://docs.redhat.com/

SELinux Project:

https://selinuxproject.org/

Man pages relevantes:

selinux(8)
semanage(8)
restorecon(8)
ausearch(8)

Utilizar para:

contexts
domains
types
ports
AVC
troubleshooting
políticas
hardening.

Nunca utilizar "desactivar SELinux" como procedimiento normal de resolución.


# 12. FIREWALLD

Documentación oficial:

https://firewalld.org/

Utilizar para:

zones
services
ports
sources
rich rules
runtime/permanent
NRPE
NCPA
SNMP
SSH
web UI
monitorización distribuida.


# 13. APACHE HTTP SERVER

Documentación oficial:

https://httpd.apache.org/docs/

Utilizar para:

interfaz web
CGI
authentication
authorization
TLS
logging
seguridad.


# 14. OPENSSH

OpenSSH:

https://www.openssh.com/

Man pages:

ssh(1)
sshd(8)
ssh_config(5)
sshd_config(5)
ssh-keygen(1)
authorized_keys(5)

Utilizar especialmente para check_by_ssh y monitorización remota segura.


# 15. SNMP

Net-SNMP:

https://www.net-snmp.org/

Man pages:

snmpget(1)
snmpwalk(1)
snmpcmd(1)

Utilizar para:

SNMP
MIB
OID
SNMPv2c
SNMPv3
autenticación
privacidad
troubleshooting.

Complementar con los RFC correspondientes cuando sea necesario profundizar en el protocolo.


# 16. RFC Y ESTÁNDARES

Utilizar RFC originales cuando una lección requiera profundidad protocolaria.

Priorizar:

IETF Datatracker
RFC Editor.

Especialmente relevante para:

SNMP
TLS
HTTP
SSH
protocolos de red relacionados con checks.


# 17. C

Nagios Core está implementado principalmente en C.

Para los bloques de internals puede utilizarse:

The C Programming Language
Brian W. Kernighan
Dennis M. Ritchie
2nd Edition.

Uso:

comprender código C cuando sea necesario para seguir Nagios Core.

No convertir el PATH en un curso general de C.


# 18. PROGRAMACIÓN DE SISTEMAS LINUX

The Linux Programming Interface
Michael Kerrisk
No Starch Press.

Uso complementario para:

processes
signals
files
file descriptors
IPC
timers
Linux APIs
daemon behavior.

Especialmente útil al estudiar internals.

Debe utilizarse únicamente cuando ayude a explicar mecanismos observados en Nagios.


# 19. LINUX

Linux man-pages:

https://man7.org/linux/man-pages/

Utilizar como fuente primaria/complementaria para interfaces Linux empleadas por Nagios y sus herramientas.


# 20. MONITORIZACIÓN Y SRE

Site Reliability Engineering
Google.

The Site Reliability Workbook
Google.

Utilizar como bibliografía conceptual complementaria para:

monitoring
SLI
SLO
alerting
alert fatigue
reliability
operational practices.

No trasladar conceptos de Prometheus o SRE a Nagios como si fueran mecanismos nativos de Nagios.


# 21. PROMETHEUS

Documentación oficial:

https://prometheus.io/docs/

Uso exclusivamente comparativo o de integración cuando el PATH lo requiera:

pull model
metrics
time series
exporters
alerting
integración
diferencias arquitectónicas.

No convertir las lecciones Nagios en lecciones Prometheus.


# 22. GRAFANA

Documentación oficial:

https://grafana.com/docs/

Uso complementario para integraciones y visualización cuando corresponda.


# 23. LOGGING

Utilizar las fuentes primarias correspondientes a:

systemd-journald
rsyslog
logrotate

cuando las lecciones estudien logging de Nagios.

Debe mantenerse clara la separación entre:

monitorización Nagios
logs
métricas
traces.


# 24. SEGURIDAD

Para seguridad utilizar preferentemente:

documentación oficial Nagios
Fedora Security
Red Hat Security
SELinux Project
OpenSSH
Apache
firewalld
documentación de los protocolos correspondientes.

Priorizar siempre:

mínimo privilegio
reducción de superficie de ataque
cifrado
autenticación
segmentación
protección de secretos.


# 25. CÓDIGO FUENTE COMO BIBLIOGRAFÍA

Para internals, el código fuente es bibliografía primaria.

La metodología debe ser:

documentación
→ concepto
→ componente
→ archivo fuente
→ estructura/función relevante
→ flujo de ejecución
→ comportamiento observable.

No utilizar fragmentos de código aislados sin explicar su posición en la arquitectura.


# 26. FUENTES HISTÓRICAS

Nagios posee una larga historia y abundante documentación antigua.

Las fuentes históricas pueden utilizarse para:

evolución
arquitectura histórica
conceptos que continúan vigentes.

No deben utilizarse automáticamente para afirmar comportamiento de versiones actuales.

Debe comprobarse:

versión
fecha
componente
vigencia.


# 27. FUENTES COMUNITARIAS

Foros, Stack Overflow, blogs, GitHub issues y discusiones comunitarias pueden utilizarse para:

casos reales
errores poco documentados
troubleshooting
contexto adicional.

Nunca deben sustituir una fuente primaria cuando ésta resuelva la cuestión.


# 28. PRIORIDAD POR ÁREA

Fundamentos:
documentación Nagios + SRE como complemento conceptual.

Nagios Core:
documentación oficial.

Configuración y object model:
documentación oficial Nagios Core.

Plugins:
Nagios Plugins + Plugin Development Guidelines.

NRPE:
documentación/repositorio NRPE.

NCPA:
documentación/repositorio NCPA.

Fedora:
Fedora Documentation + Fedora Packages.

systemd:
documentación y man pages systemd.

SELinux:
Fedora/Red Hat/SELinux Project.

firewalld:
documentación oficial firewalld.

SSH:
OpenSSH.

SNMP:
Net-SNMP + RFC cuando proceda.

Seguridad:
documentación primaria de cada componente.

Troubleshooting:
documentación primaria + logs + código fuente cuando sea necesario.

Internals:
código fuente Nagios Core + documentación + TLPI como apoyo.


# 29. CRITERIO DE USO

La bibliografía debe servir para aumentar precisión y profundidad.

No debe provocar:

copias extensas
enumeraciones bibliográficas innecesarias
explicaciones desconectadas de la lección
información histórica presentada como actual.

Cada fuente debe utilizarse únicamente cuando aporte valor al tema concreto.


# 30. OBJETIVO BIBLIOGRÁFICO FINAL

La combinación:

documentación oficial
+ código fuente
+ Fedora/RHEL
+ documentación Linux
+ bibliografía de sistemas

debe permitir avanzar desde:

"sé configurar un check"

hasta:

"entiendo por qué Nagios programó el check, cómo lo ejecutó, cómo procesó su resultado, por qué produjo ese estado y cómo diagnosticar el flujo cuando falla".
