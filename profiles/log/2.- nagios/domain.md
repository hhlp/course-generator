# NAGIOS EN PROFUNDIDAD — FEDORA/RHEL

## 1. Identidad del PATH

Este PATH enseña Nagios desde fundamentos de monitorización hasta administración avanzada, arquitectura distribuida, alta disponibilidad, troubleshooting e internals de Nagios Core.

El entorno principal es Fedora Linux, utilizando RHEL y sistemas compatibles cuando resulte útil para explicar diferencias operativas o de empaquetado.

El PATH no debe tratar Nagios únicamente como una interfaz web o como un conjunto de archivos de configuración.

Debe estudiar el sistema completo:

Nagios Core
modelo de objetos
hosts
hostgroups
services
servicegroups
commands
checks
plugins
Plugin API
estados
SOFT/HARD states
scheduler
event queue
timeperiods
freshness
flapping
notifications
contacts
contactgroups
acknowledgements
scheduled downtime
event handlers
dependencies
escalations
macros
NRPE
NCPA
SSH
SNMP
passive checks
external commands
performance data
logging
state retention
CGI
systemd
SELinux
firewalld
seguridad
automatización
distributed monitoring
HA
escalabilidad
integraciones
troubleshooting
internals de Nagios Core
Event Broker
NEB
proyecto final experto

El objetivo final es que el estudiante pueda diseñar, desplegar, administrar, asegurar, automatizar, escalar y diagnosticar una plataforma Nagios Core real.


## 2. Nivel

Nivel inicial:

cero conocimientos específicos de Nagios.

Se presuponen progresivamente conocimientos generales de administración Linux, pero los conceptos específicos necesarios deben explicarse cuando aparezcan.

Nivel final:

administrador avanzado de Nagios Core capaz de comprender también una parte significativa de sus mecanismos internos.

La progresión debe ser:

fundamentos
→ operación básica
→ configuración
→ modelo de objetos
→ monitorización
→ alerting
→ monitorización remota
→ seguridad
→ automatización
→ distribución
→ HA
→ rendimiento
→ troubleshooting
→ internals.


## 3. Plataforma principal

La plataforma de referencia es Fedora Linux.

Siempre que resulte relevante deben utilizarse herramientas y conceptos reales del sistema:

dnf
rpm
systemctl
journalctl
firewall-cmd
semanage
restorecon
ausearch
sealert
ss
ip
ps
pgrep
curl
openssl
ssh
snmpget
snmpwalk

No asumir rutas, nombres de paquetes, usuarios, grupos, unidades systemd o políticas SELinux universales.

Distinguir cuando sea necesario entre:

Fedora
RHEL
derivados de RHEL
paquetes de distribución
instalación upstream desde código fuente.

Si una ruta depende del método de instalación, explicarlo explícitamente.


## 4. Nagios Core como núcleo

Nagios Core constituye el núcleo tecnológico del PATH.

Debe explicarse su arquitectura y no limitarse a enseñar recetas de configuración.

El estudiante debe comprender:

cómo Nagios carga la configuración
cómo se construye el modelo de objetos
cómo funciona el scheduler
cómo se programa un check
cómo se ejecuta un plugin
cómo se procesa su resultado
cómo cambia el estado
cómo funcionan los reintentos
cómo se obtiene un HARD state
cómo se genera una notification
cómo intervienen dependencies y escalations
cómo se ejecutan event handlers
cómo se procesan external commands
cómo se conserva estado
cómo se procesa performance data.

Cuando el PATH alcance internals, relacionar estos conceptos con la implementación de Nagios Core.


## 5. Nagios Core frente a Nagios XI

El objeto principal del PATH es Nagios Core.

Nagios XI puede mencionarse para contextualizar el ecosistema, pero no debe desplazar el estudio de Nagios Core.

No convertir las lecciones en instrucciones específicas de Nagios XI salvo que el título de la lección lo requiera explícitamente.


## 6. Modelo de objetos

El modelo de objetos es fundamental.

Explicar con profundidad:

host
service
command
contact
contactgroup
hostgroup
servicegroup
timeperiod
hostdependency
servicedependency
hostescalation
serviceescalation.

Explicar también:

templates
use
name
register
herencia
resolución de objetos
additive inheritance
relaciones entre objetos.

No enseñar configuraciones aisladas sin explicar cómo se relacionan dentro del object model.


## 7. Hosts y services

Distinguir rigurosamente entre host checks y service checks.

Explicar:

estado de hosts
estado de services
relaciones padre/hijo
reachability
check commands
intervalos
reintentos
check periods
notification periods
performance data
freshness
flapping
event handlers.

Cuando se muestren configuraciones, explicar cada directiva relevante y su efecto operativo.


## 8. Checks

Distinguir:

active checks
passive checks
host checks
service checks
local checks
remote checks.

Seguir cuando resulte útil el flujo:

scheduler
→ ejecución
→ plugin
→ exit status
→ plugin output
→ check result
→ state processing
→ SOFT/HARD
→ notification/event handler/performance data.


## 9. Plugins

Los plugins son programas externos ejecutados por Nagios.

El estudiante debe dominar:

localización
instalación
ejecución manual
argumentos
thresholds
timeouts
exit status
stdout
performance data
permisos
ejecución como usuario Nagios
diagnóstico.

Cubrir plugins habituales como:

check_ping
check_http
check_tcp
check_dns
check_ssh
check_load
check_disk
check_swap
check_users
check_procs
check_by_ssh
check_nrpe
check_snmp.

No limitar la explicación a copiar comandos.


## 10. Plugin API

Explicar rigurosamente el contrato entre Nagios y los plugins.

Estados:

0 = OK
1 = WARNING
2 = CRITICAL
3 = UNKNOWN.

Explicar:

short output
long output
performance data
threshold ranges
labels
values
warn
crit
min
max.

Relacionar siempre el código de salida del proceso con el estado que interpreta Nagios.


## 11. Desarrollo de plugins

El PATH no es principalmente un curso de programación de plugins.

El objetivo es comprender suficientemente la interfaz para:

evaluar plugins
depurarlos
modificarlos cuando sea necesario
crear plugins sencillos.

Puede utilizarse shell y Python para ejemplos didácticos.

Priorizar:

contrato
validación
timeouts
exit codes
mensajes
performance data
seguridad.

No convertir esta sección en un curso avanzado de Python o shell.


## 12. Estados

Explicar con especial profundidad la máquina de estados.

Hosts:

UP
DOWN
UNREACHABLE.

Services:

OK
WARNING
CRITICAL
UNKNOWN.

Explicar:

state
state type
state change
SOFT
HARD
max_check_attempts
retry_interval
recovery.

El estudiante debe poder reconstruir una transición de estado paso a paso.


## 13. Scheduling

El scheduler debe tratarse como una pieza central de Nagios.

Explicar:

event queue
active checks
check intervals
retry intervals
rescheduling
inter-check delay
interleave
concurrency
latency
execution time
timeouts
carga.

No reducir scheduling a explicar check_interval.


## 14. Notifications

Explicar el pipeline completo:

estado
→ HARD state
→ reglas de notificación
→ timeperiod
→ acknowledgements
→ downtime
→ dependencies
→ escalations
→ contact/contactgroup
→ notification command
→ entrega.

Diferenciar claramente detección de problemas y notificación de problemas.


## 15. Event handlers

Explicar event handlers como mecanismo de reacción y posible remediación.

Incluir:

SOFT states
HARD states
global handlers
host handlers
service handlers
macros
permisos
sudo
idempotencia
loops
seguridad.

No recomendar autorremediación indiscriminada.


## 16. Freshness y flapping

Freshness debe relacionarse especialmente con passive checks y datos obsoletos.

Flapping debe explicarse como detección de inestabilidad de estado.

Explicar consecuencias sobre alertas y notificaciones.


## 17. Monitorización remota

Comparar mecanismos:

SSH
NRPE
NCPA
SNMP
passive checks.

Para cada mecanismo explicar:

arquitectura
flujo
autenticación
cifrado
firewall
SELinux
privilegios
ventajas
limitaciones
casos apropiados.

No presentar un único mecanismo como solución universal.


## 18. NRPE

Cubrir:

check_nrpe
daemon NRPE
configuración
allowed_hosts
commands
argument passing
TLS
systemd
firewalld
SELinux
seguridad
troubleshooting.

Tratar NRPE como tecnología importante del ecosistema Nagios pero contextualizar sus limitaciones y alternativas modernas.


## 19. NCPA

Cubrir:

arquitectura
listener
API
autenticación
tokens
TLS
checks
métricas
integración con Nagios Core
seguridad
troubleshooting.

Comparar conceptualmente con NRPE cuando aporte valor.


## 20. SNMP

No convertir el PATH en un curso completo de SNMP.

Enseñar lo necesario para monitorización Nagios:

manager
agent
MIB
OID
SNMPv2c
SNMPv3
snmpget
snmpwalk
check_snmp
autenticación
privacidad
seguridad.

Priorizar SNMPv3 para escenarios donde la seguridad sea relevante.


## 21. Passive checks

Explicar:

accept_passive_service_checks
accept_passive_host_checks
PROCESS_SERVICE_CHECK_RESULT
PROCESS_HOST_CHECK_RESULT
external command interface
timestamps
freshness
distributed monitoring.

Relacionarlos con arquitecturas push y distribuidas.


## 22. External command interface

Explicar que permite modificar el comportamiento de Nagios en ejecución.

Cubrir:

command file
formato
timestamps
acknowledgements
downtime
forced checks
enable/disable
passive results.

Prestar especial atención a permisos y seguridad.


## 23. Performance data

Distinguir estado de servicio y datos de rendimiento.

Explicar:

plugin performance data
process_performance_data
commands
files
templates
procesamiento externo
series temporales
integraciones.

Nagios Core no debe presentarse como equivalente a una TSDB moderna.


## 24. Logging

Integrar Nagios con conocimientos Linux reales.

Cubrir cuando corresponda:

Nagios log
archivos históricos
journalctl
systemd journal
rsyslog
logrotate
debug logging.

Las lecciones deben enseñar a utilizar los logs como herramienta de troubleshooting.


## 25. State retention

Explicar:

retained state
state_retention_file
retention_update_interval
program state
scheduling information
host/service state
reinicios.

Diferenciar configuración persistente y estado retenido.


## 26. Web y CGI

La interfaz web debe tratarse como una capa sobre Nagios Core, no como el núcleo del sistema.

Cubrir:

CGI
cgi.cfg
Apache
authentication
authorization
TLS
seguridad.

Explicar la separación entre engine, status information y presentación web.


## 27. systemd

Utilizar systemd de forma nativa en Fedora/RHEL.

Cubrir:

unit
start
stop
restart
reload
enable
status
journalctl
overrides
dependencias
hardening.

No recomendar scripts SysV salvo para contexto histórico.


## 28. SELinux

No recomendar desactivar SELinux para solucionar problemas.

Trabajar con SELinux enforcing.

Utilizar cuando proceda:

ls -Z
ps -eZ
semanage
restorecon
ausearch
sealert
audit2why.

Explicar dominios, tipos, labels, puertos y AVC relacionados con Nagios.

Las políticas locales deben considerarse después de comprender la causa del bloqueo.


## 29. Firewalld

No recomendar desactivar firewalld.

Enseñar a abrir únicamente las comunicaciones necesarias.

Relacionar reglas con:

web UI
NRPE
NCPA
SNMP
SSH
arquitecturas distribuidas.

Aplicar mínimo privilegio y restricciones por source cuando proceda.


## 30. Seguridad

La seguridad debe ser transversal.

Aplicar:

mínimo privilegio
separación de funciones
permisos mínimos
protección de secretos
validación de argumentos
reducción de superficie de ataque
TLS
SNMPv3
SSH restringido
SELinux enforcing
firewalld
hardening systemd.

Prestar atención especial a:

plugins
commands
event handlers
external commands
NRPE arguments
resource.cfg
macros que contienen secretos.

No mostrar prácticas inseguras como solución recomendada.


## 31. Automatización

La configuración debe poder gestionarse como código.

Cubrir:

estructura modular
templates
Git
scripts
Ansible
validación
nagios -v
CI
despliegue
reload seguro
rollback conceptual.

Toda automatización debe validar la configuración antes de activarla.


## 32. Distributed monitoring

Explicar arquitecturas:

centralizadas
distribuidas
pollers
passive results
remote execution
WAN
segmentación
redundancia.

Analizar:

latencia
carga
seguridad
fallos de red
escalabilidad.


## 33. Alta disponibilidad

Nagios también debe ser monitorizado.

Explicar:

SPOF
active/passive
active/active cuando sea técnicamente apropiado
sincronización
VIP
load balancing
state
split brain
recuperación
pruebas de fallo.

Distinguir HA del engine, HA de la interfaz y redundancia de los mecanismos de checks.


## 34. Escalabilidad

Analizar rendimiento mediante:

número de hosts
número de services
frecuencia
latencia
execution time
concurrencia
plugins
red
passive checks
distribución.

No asumir que aumentar frecuencia de checks siempre mejora la monitorización.


## 35. Integraciones

Explicar integraciones únicamente con la profundidad necesaria para comprender Nagios dentro de una plataforma moderna.

Puede relacionarse con:

Grafana
Prometheus
logging
ticketing
chat
correo
SNMP traps
sistemas externos.

No convertir estas lecciones en cursos completos de dichas tecnologías.


## 36. Troubleshooting

Las lecciones de troubleshooting deben enseñar metodología, no listas de comandos.

Secuencia recomendada:

síntoma
→ alcance
→ proceso
→ configuración
→ objeto
→ command
→ plugin
→ usuario/permisos
→ red
→ agente
→ SELinux/firewalld
→ scheduler
→ estado
→ notification pipeline
→ logs
→ causa raíz
→ corrección
→ validación.

Utilizar herramientas reales:

nagios -v
systemctl
journalctl
ps
ss
curl
ssh
openssl
snmpget
snmpwalk
ausearch
firewall-cmd.


## 37. Internals

Los internals son parte obligatoria del nivel experto.

Estudiar conceptualmente y, cuando resulte útil, mediante código fuente:

startup
configuration parsing
object structures
scheduler
event queue
timed events
workers
check execution
check result processing
state processing
notifications
event handlers
dependencies
escalations
macro expansion
external commands
retention
logging
performance data
Event Broker
NEB modules
CGI.

No es necesario convertir al estudiante en desarrollador de Nagios Core.

Sí debe poder relacionar comportamiento observable con arquitectura interna.


## 38. Código fuente

Cuando una lección estudie internals:

usar preferentemente el código fuente oficial correspondiente a la versión estudiada
identificar archivos y funciones relevantes
explicar estructuras antes de fragmentos de código
seguir flujos de ejecución
evitar volcados extensos de código.

Distinguir comportamiento documentado de detalles de implementación que pueden cambiar entre versiones.


## 39. Versiones

Nagios y sus componentes evolucionan.

Cuando una característica dependa de versión:

indicarlo
no presentar comportamiento histórico como actual
consultar documentación correspondiente
diferenciar Nagios Core, plugins, NRPE y NCPA.

Las lecciones deben priorizar versiones actuales compatibles con el entorno de estudio.


## 40. Fuentes

Prioridad:

1. documentación oficial de Nagios Core
2. código fuente oficial
3. documentación oficial de Nagios Plugins
4. documentación oficial de NRPE
5. documentación oficial de NCPA
6. documentación Fedora
7. documentación RHEL
8. documentación oficial systemd
9. documentación SELinux
10. documentación firewalld
11. manuales y libros técnicos reconocidos.

No depender de blogs cuando exista documentación primaria adecuada.


## 41. Comandos

Todo comando debe tener propósito didáctico.

Cuando sea relevante explicar:

qué hace
qué entrada utiliza
qué salida esperar
cómo interpretarla
qué cambia en el sistema
cómo verificar el resultado.

No inventar outputs exactos dependientes del entorno.

Diferenciar claramente:

comando
salida
configuración
pseudocódigo.


## 42. Configuración

Los ejemplos deben ser técnicamente coherentes.

Cuando se modifique configuración:

mostrar contexto suficiente
explicar directivas
validar
recargar/reiniciar únicamente cuando proceda
verificar resultado.

Siempre que sea posible:

editar
→ validar con nagios -v
→ aplicar
→ comprobar.


## 43. Laboratorios

Los laboratorios deben aumentar progresivamente en dificultad.

Priorizar:

descubrimiento
configuración
observación
provocación controlada de fallos
diagnóstico
corrección
verificación.

Los laboratorios avanzados deben combinar varios subsistemas.


## 44. Proyecto final

El proyecto final debe integrar:

Fedora/RHEL
Nagios Core
hosts
services
plugins
NRPE
NCPA
SSH
SNMP
passive checks
notifications
event handlers
dependencies
escalations
performance data
logging
systemd
SELinux
firewalld
seguridad
automatización
distributed monitoring
HA
troubleshooting.

El estudiante debe terminar siendo capaz de operar y diagnosticar la plataforma, no únicamente instalarla.


## 45. Estructura pedagógica obligatoria

Cada lección debe comenzar con:

🎯 OBJETIVO

Después debe desarrollar el tema con profundidad proporcional a su complejidad.

Cuando aporten valor utilizar:

🧪 Laboratorio/ejemplos
⚠️ Errores frecuentes
💡 Idea importante

Cada lección debe finalizar obligatoriamente con:

🧠 QUÉ DEBES RECORDAR

Esta sección debe contener entre 3 y 7 ideas esenciales.

No debe ser una repetición literal del objetivo.


## 46. Profundidad

No generar fichas, resúmenes rápidos ni definiciones aisladas.

Cada lección debe explicar:

qué es
para qué sirve
cómo funciona
cómo encaja en Nagios
cómo se configura o utiliza cuando corresponda
cómo verificarlo
cómo diagnosticarlo
riesgos y errores cuando sean relevantes
relación con conceptos anteriores y posteriores.

La extensión debe adaptarse a la complejidad real de la lección.

No rellenar artificialmente una lección sencilla.

No comprimir artificialmente una lección compleja.


## 47. Regla de contexto

El título aislado de una lección nunca debe interpretarse fuera de este PATH.

Por ejemplo:

"scheduling" significa scheduling de Nagios Core.
"commands" significa command objects y mecanismos relacionados de Nagios.
"states" significa estados y state processing de Nagios.
"retention" significa state retention de Nagios.
"dependencies" significa host/service dependencies de Nagios.
"macros" significa macros de Nagios.

El contexto global de este documento debe prevalecer sobre interpretaciones genéricas.


## 48. Resultado esperado

Al completar el PATH, el estudiante debe ser capaz de explicar y seguir:

infraestructura
→ object configuration
→ scheduler
→ check command
→ plugin/agente
→ resultado
→ state processing
→ SOFT/HARD
→ notification/event handler
→ performance data/logging

y diagnosticar cualquier punto relevante de esa cadena.
