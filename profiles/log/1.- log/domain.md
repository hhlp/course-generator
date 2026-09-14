# DOMAIN — LOGGING EN LINUX — FEDORA

## Identidad del PATH

Este PATH enseña logging en Linux sobre Fedora desde fundamentos hasta nivel experto, con énfasis en comprender, operar, diseñar, asegurar y diagnosticar pipelines reales de logging.

El foco principal es el stack nativo y tradicional de logging en Fedora:

- systemd-journald
- journalctl
- protocolo Syslog
- rsyslog
- syslog-ng
- logging remoto
- TLS
- RELP
- parsing y normalización
- colas, buffers y backpressure
- logging estructurado
- logrotate
- integración con systemd
- integración con SELinux
- integración con firewalld
- troubleshooting extremo a extremo
- internals

El PATH debe permitir que el alumno comprenda no solo cómo ejecutar comandos, sino cómo fluye un evento desde que una aplicación o el kernel lo genera hasta que se almacena local o remotamente.

## Plataforma de referencia

La plataforma principal es Fedora Linux actual.

Cuando sea relevante:

- utilizar paquetes, rutas, servicios y comportamiento reales de Fedora;
- preferir systemd y sus herramientas nativas;
- explicar diferencias históricas solo cuando ayuden a entender el presente;
- mencionar RHEL compatibles cuando aporten contexto, sin convertir el curso en un PATH genérico de distribuciones;
- evitar instrucciones específicas de Debian/Ubuntu salvo comparaciones puntuales claramente marcadas.

## Nivel del curso

El curso comienza desde cero y progresa hasta administración, diseño, seguridad, rendimiento, resiliencia, troubleshooting e internals.

No asumir experiencia previa con journald, Syslog, rsyslog, syslog-ng o logrotate.

Sí se puede asumir conocimiento básico de Linux al avanzar hacia bloques intermedios y avanzados, pero cualquier concepto imprescindible para comprender el logging debe explicarse dentro de la propia lección.

## Objetivo global

Al finalizar el PATH, el alumno debe poder:

- explicar la arquitectura completa de logging de Fedora;
- distinguir stdout, stderr, kernel logging, journald y Syslog;
- consultar y analizar el journal con journalctl;
- configurar persistencia, límites, namespaces, rate limiting y forwarding de journald;
- interpretar correctamente facility, severity, PRI, RFC 3164, RFC 5424, RFC 5425 y RFC 6587;
- configurar rsyslog en profundidad;
- configurar syslog-ng en profundidad;
- construir logging remoto sobre UDP, TCP, TLS y RELP;
- diseñar filtros, routing, parsing, templates y normalización;
- entender queues, disk buffers, flow-control y backpressure;
- minimizar pérdida, duplicación y retrasos de eventos;
- diseñar políticas de rotación y retención con logrotate;
- integrar logging con systemd, SELinux y firewalld;
- dimensionar almacenamiento, red, memoria y colas;
- diagnosticar fallos extremo a extremo;
- comprender los internals fundamentales del pipeline;
- construir una plataforma centralizada y segura de logging para múltiples hosts Fedora.

## Alcance conceptual

El PATH cubre el flujo:

productor → stdout/stderr/syslog/kernel → systemd-journald → journal → rsyslog/syslog-ng → procesamiento → queues/buffers → transporte → collector → archivos/almacenamiento → logrotate

También debe estudiar:

- identificación del productor;
- metadatos;
- timestamps;
- contexto de proceso y unidad systemd;
- estructura de mensajes;
- persistencia;
- filtrado;
- transformación;
- parsing;
- enriquecimiento;
- routing;
- seguridad;
- fiabilidad;
- recuperación;
- capacidad;
- diagnóstico.

## Frontera con otros PATH

Este PATH NO debe convertirse en un curso de observabilidad general.

### Loki / Grafana

Puede explicarse cómo entregar logs a componentes externos o qué requisitos debe cumplir un pipeline, pero no desarrollar en profundidad:

- Loki
- Promtail o agentes equivalentes
- LogQL
- dashboards de Grafana
- alertas de Grafana

Eso pertenece al PATH Grafana + Loki.

### Elastic Stack

No desarrollar en profundidad:

- Elasticsearch
- mappings
- shards
- replicas
- ingest pipelines de Elasticsearch
- Logstash
- Beats / Elastic Agent
- Kibana
- ILM

Solo pueden aparecer como destinos o integraciones conceptuales.

### OpenSearch

No desarrollar OpenSearch, Data Prepper ni OpenSearch Dashboards salvo referencias de integración.

### Prometheus

No desarrollar:

- exporters
- PromQL
- recording rules
- alerting rules
- Alertmanager
- remote write/read

El PATH debe mantener clara la diferencia entre logs y métricas.

### OpenTelemetry

Puede mencionarse como integración moderna y como fuente/destino de eventos, pero su arquitectura completa, OTLP, Collector, processors, exporters y context propagation pertenecen al PATH OpenTelemetry.

### Zabbix / Nagios

No desarrollar plataformas de monitorización completas. Solo mencionar integración cuando ayude a situar logging dentro de observabilidad.

## Reglas pedagógicas obligatorias

Cada lección debe comenzar siempre con:

## 🎯 OBJETIVO

El objetivo debe indicar de forma concreta qué comprenderá o será capaz de hacer el alumno al terminar la lección.

El desarrollo debe ser completo, profundo, didáctico y progresivo. No producir un simple resumen de documentación.

Cuando aporten valor, utilizar:

- ## 🧪 Laboratorio / ejemplos
- ## ⚠️ Errores frecuentes
- ## 💡 Idea importante

Cada lección debe terminar siempre con:

## 🧠 QUÉ DEBES RECORDAR

Debe contener entre 3 y 7 ideas clave realmente útiles para retener la lección. No repetir literalmente el objetivo.

## Estilo

- Español técnico claro.
- Explicar primero el concepto y después la sintaxis.
- No introducir comandos sin explicar qué inspeccionan o modifican.
- Diferenciar observación, configuración y mutación del sistema.
- Mostrar rutas y unidades reales cuando correspondan.
- Preferir ejemplos reproducibles en Fedora.
- Evitar relleno, frases vagas o consejos genéricos.
- No asumir que ejecutar un comando implica comprender el mecanismo.
- Relacionar continuamente cada herramienta con la posición que ocupa dentro del pipeline.

## Comandos y privilegios

Distinguir claramente cuándo un comando:

- puede ejecutarse como usuario normal;
- requiere pertenecer a un grupo concreto;
- requiere sudo o root;
- puede modificar persistencia o seguridad;
- puede interrumpir o recargar un servicio.

No anteponer sudo indiscriminadamente a todos los comandos.

## Configuración

Cuando se modifique configuración:

1. mostrar el archivo o drop-in apropiado;
2. explicar la precedencia;
3. validar la configuración si existe una herramienta de validación;
4. aplicar o recargar el servicio de forma correcta;
5. comprobar el resultado;
6. indicar cómo revertir el cambio cuando sea útil.

Evitar editar archivos vendor cuando exista un mecanismo de drop-ins o configuración administrativa más apropiado.

## journald

Debe tratarse como una base de eventos estructurados, no solo como una alternativa a archivos de texto.

Explicar con especial cuidado:

- campos trusted frente a campos aportados por usuarios;
- _TRANSPORT;
- _SYSTEMD_UNIT;
- _BOOT_ID;
- _MACHINE_ID;
- timestamps realtime y monotonic;
- filtros por campos;
- salida JSON/export;
- runtime journal frente a persistent journal;
- vacuum y límites;
- namespaces;
- rate limiting;
- Forward Secure Sealing;
- interacción con rsyslog/syslog-ng.

## Syslog

Separar claramente:

- Syslog como arquitectura;
- Syslog como formato/protocolo;
- implementaciones concretas.

Distinguir RFC 3164, RFC 5424, RFC 5425 y RFC 6587 cuando corresponda.

No tratar UDP, TCP, TLS o RELP como equivalentes.

## rsyslog

La enseñanza debe cubrir el modelo moderno de configuración además de la sintaxis histórica.

Dar prioridad a:

- input();
- ruleset();
- action();
- template();
- RainerScript;
- imjournal;
- imuxsock;
- imudp;
- imtcp;
- imfile;
- omfile;
- omfwd;
- imrelp / omrelp cuando estén disponibles;
- main queue;
- action queues;
- disk-assisted queues;
- parsing y normalización;
- estadísticas y troubleshooting.

Las reglas clásicas facility.priority pueden enseñarse por compatibilidad y fundamentos, pero no deben eclipsar el modelo moderno.

## syslog-ng

Explicar explícitamente su modelo de pipeline:

source → parser/filter/rewrite → log path → destination

Cubrir:

- sources;
- destinations;
- filters;
- parsers;
- rewrites;
- templates;
- log paths;
- junctions/channels cuando aporten valor;
- flow-control;
- disk buffers;
- TLS;
- routing.

## Fiabilidad

Evitar afirmaciones simplistas de "entrega garantizada".

Explicar correctamente:

- pérdida;
- duplicación;
- reintentos;
- orden;
- buffers;
- queues;
- persistencia;
- acknowledgements;
- at-most-once;
- at-least-once;
- por qué exactly-once extremo a extremo suele no estar garantizado.

## TLS y certificados

Siempre distinguir:

- cifrado;
- autenticación del servidor;
- autenticación mutua;
- validación de CA;
- validación de nombre;
- certificados expirados;
- permisos de claves privadas;
- troubleshooting con openssl cuando proceda.

## SELinux

No recomendar desactivar SELinux como solución.

El troubleshooting debe priorizar:

- inspeccionar AVC;
- comprender el motivo del bloqueo;
- verificar labels;
- restorecon;
- semanage fcontext cuando proceda;
- distinguir problemas de SELinux de problemas de permisos Unix.

## firewalld

Cuando intervenga logging remoto:

- identificar transporte y puerto;
- comprobar listeners;
- comprobar zona/interfaz;
- abrir únicamente lo necesario;
- distinguir runtime y permanent;
- validar conectividad después del cambio.

## logrotate

Explicar la diferencia entre:

- renombrar un pathname;
- descriptor abierto;
- reapertura del archivo por el daemon;
- copytruncate;
- rotación propia de una aplicación;
- rotación interna del journal.

No presentar copytruncate como solución universal. Explicar su ventana potencial de pérdida de mensajes.

## Laboratorios

Los laboratorios deben ser verificables.

Preferir la secuencia:

1. observar estado inicial;
2. hacer un cambio controlado;
3. generar eventos de prueba;
4. observar el flujo;
5. provocar un fallo cuando sea seguro;
6. diagnosticarlo;
7. restaurar estado;
8. verificar recuperación.

Utilizar herramientas como:

- logger
- systemd-cat
- journalctl
- systemctl
- systemd-analyze cat-config
- rsyslogd -N1
- syslog-ng --syntax-only
- logrotate -d
- ss
- lsof
- tcpdump
- openssl s_client
- firewall-cmd
- ausearch
- sealert
- restorecon
- semanage
- jq

## Troubleshooting

El diagnóstico debe seguir el pipeline y evitar cambios aleatorios.

Modelo recomendado:

productor → captura local → journald → forwarding/input → parser/filter/ruleset → queue → transporte → firewall/red → TLS → collector → parser/routing → almacenamiento → rotación

En cada fase preguntar:

- ¿el evento existe?
- ¿tiene los campos esperados?
- ¿fue descartado?
- ¿está bloqueado?
- ¿está en cola?
- ¿salió por la red?
- ¿fue recibido?
- ¿se escribió?
- ¿se rotó?

## Internals

Las lecciones de internals deben explicar suficiente implementación para entender comportamiento observable y troubleshooting, incluyendo cuando corresponda:

- file descriptors;
- pipes;
- Unix sockets;
- /dev/log;
- /dev/kmsg;
- kernel buffers;
- socket buffers;
- journald sockets;
- journal binary format a nivel conceptual;
- mmap;
- page cache;
- fsync;
- queues;
- threads/workers;
- backpressure.

No convertir el PATH en un curso completo de programación interna de systemd, rsyslog o syslog-ng.

## Actualidad y versiones

El ecosistema evoluciona. Cuando una opción, módulo o comportamiento dependa de versión:

- indicar que puede variar;
- comprobar la documentación/man page instalada cuando sea la fuente más fiable;
- no inventar disponibilidad de módulos;
- enseñar al alumno a descubrir soporte localmente mediante rpm, dnf, man, --help, -V, listas de módulos o documentación instalada.

## Resultado esperado del proyecto final

El proyecto final debe producir una plataforma donde el alumno pueda demostrar:

- generación de logs desde aplicaciones y servicios;
- persistencia local en journald;
- consultas estructuradas;
- forwarding;
- transporte seguro;
- buffering/queues;
- collector central;
- parsing y routing;
- política de almacenamiento y rotación;
- integración con SELinux y firewalld;
- recuperación ante fallos;
- procedimiento de troubleshooting documentado;
- dimensionamiento básico;
- auditoría de seguridad y fiabilidad.
