# BIBLIOGRAPHY — ZABBIX EN PROFUNDIDAD

## Propósito

Esta bibliografía define las fuentes de referencia del PATH **ZABBIX EN PROFUNDIDAD**.

La documentación de Zabbix es sensible a versión.

Por tanto, una referencia técnicamente correcta para una versión antigua no debe utilizarse automáticamente para describir el comportamiento de una versión actual.

Orden general de preferencia:

1. documentación oficial Zabbix de la versión estudiada;
2. código fuente oficial de Zabbix;
3. documentación oficial de las tecnologías integradas;
4. especificaciones y RFC;
5. libros;
6. fuentes secundarias.

---

# 1. PRINCIPAL — Zabbix 7.4 Documentation

**Zabbix Documentation — 7.4**

Fuente principal para el PATH.

Utilizar prioritariamente para:

- introducción;
- arquitectura;
- Zabbix Server;
- Server HA;
- Agent;
- Agent 2;
- Proxy;
- Java Gateway;
- instalación;
- configuración;
- frontend;
- hosts;
- items;
- item types;
- item keys;
- preprocessing;
- triggers;
- events;
- problems;
- actions;
- notifications;
- templates;
- macros;
- discovery;
- LLD;
- autoregistration;
- SNMP;
- IPMI;
- JMX;
- HTTP Agent;
- web monitoring;
- calculated items;
- dependent items;
- dashboards;
- maps;
- services;
- SLA;
- API;
- seguridad;
- encryption;
- monitoring;
- troubleshooting;
- internals documentados;
- protocolos;
- appendices.

Referencia documental:

`Zabbix Documentation → 7.4`

La lección debe localizar dentro del manual la sección específica correspondiente al tema.

No citar simplemente “Zabbix Manual” cuando pueda identificarse una sección más concreta.

---

# 2. LTS — Zabbix 7.0 Documentation

**Zabbix Documentation — 7.0 LTS**

Utilizar para:

- instalaciones basadas en LTS;
- diferencias de comportamiento;
- diferencias de frontend;
- diferencias de parámetros;
- funcionalidades introducidas posteriormente;
- compatibilidad;
- upgrade desde/hacia LTS;
- operaciones empresariales que permanezcan sobre 7.0.

No mezclar silenciosamente comportamiento 7.0 y 7.4.

Cuando sea relevante:

```text
Zabbix 7.0 LTS:
...

Zabbix 7.4:
...
```

---

# 3. RELEASE NOTES Y WHAT'S NEW

## Zabbix What's New

Utilizar para determinar:

- cuándo apareció una funcionalidad;
- cambios funcionales;
- nuevos item types;
- cambios de Agent 2;
- cambios de Proxy;
- mejoras de LLD;
- cambios de preprocessing;
- cambios de API;
- cambios de HA;
- cambios de frontend;
- deprecations.

Consultar la rama/version correspondiente.

No utilizar What's New como sustituto del manual funcional.

---

# 4. UPGRADE NOTES

## Zabbix Upgrade Procedure / Upgrade Notes

Fuente esencial para los bloques:

- upgrade;
- migration;
- database schema upgrades;
- compatibility;
- Proxy compatibility;
- Agent compatibility;
- frontend;
- rollback planning.

Comprobar siempre las notas correspondientes a:

```text
versión origen
→
versión destino
```

---

# 5. CÓDIGO FUENTE OFICIAL

## Zabbix source code

Código fuente oficial del proyecto Zabbix.

Usar principalmente en bloques:

- Server internals;
- process model;
- pollers;
- trappers;
- preprocessing;
- history;
- event processing;
- Proxy internals;
- Agent internals;
- Agent 2 internals;
- protocol implementation;
- runtime control;
- source tree;
- database layer.

La documentación del usuario sigue siendo prioritaria para explicar la interfaz pública.

El código fuente se utiliza para profundizar en implementación.

---

# 6. SOURCE TREE

Para lecciones de internals estudiar según versión las áreas relacionadas con:

```text
src/
include/
database/
templates/
ui/
```

y cualquier reorganización que tenga la versión estudiada.

No asumir que la estructura del repositorio permanece constante.

Relacionar siempre código con el comportamiento observable.

---

# 7. ZABBIX PROTOCOL DOCUMENTATION

## Zabbix protocol appendices

Referencia principal para:

- protocol framing;
- headers;
- payloads;
- JSON;
- Server-Proxy;
- Agent active checks;
- Agent passive checks;
- sender;
- trapper;
- compression;
- communication details.

Especialmente importante en:

```text
72. Protocolos internos
```

No reconstruir el protocolo por intuición.

---

# 8. SERVER-PROXY PROTOCOL

## Server-proxy data exchange protocol

Referencia específica para:

- proxy configuration synchronization;
- active Proxy;
- passive Proxy;
- history data;
- discovery data;
- autoregistration data;
- interface availability;
- configuration revisions;
- sessions;
- data sender behavior.

Utilizar también para los bloques de internals del Proxy.

---

# 9. API

## Zabbix API Documentation

Referencia principal para:

- JSON-RPC;
- methods;
- authentication;
- API tokens;
- object model;
- request parameters;
- response objects;
- filtering;
- output;
- select parameters;
- pagination;
- errors.

Métodos relevantes incluyen, entre otros:

```text
host.*
hostgroup.*
item.*
trigger.*
problem.*
event.*
template.*
usermacro.*
history.*
trend.*
discoveryrule.*
action.*
user.*
```

No asumir que los parámetros son iguales entre versiones.

---

# 10. PREPROCESSING

## Zabbix Documentation — Item value preprocessing

Referencia principal para:

- preprocessing pipeline;
- transformations;
- regular expressions;
- JSONPath;
- XPath;
- JavaScript;
- Prometheus;
- validation;
- throttling;
- discard unchanged;
- custom on fail;
- testing.

Debe utilizarse también al estudiar:

- dependent items;
- discovery preprocessing;
- SNMP preprocessing;
- HTTP responses.

---

# 11. LOW-LEVEL DISCOVERY

## Zabbix Documentation — Low-level discovery

Referencia principal para:

- discovery rules;
- LLD macros;
- item prototypes;
- trigger prototypes;
- graph prototypes;
- host prototypes;
- filters;
- overrides;
- preprocessing;
- lost resources;
- resource lifetime.

---

# 12. NETWORK DISCOVERY

## Zabbix Documentation — Network discovery

Utilizar para:

- IP ranges;
- discovery checks;
- discovered hosts;
- discovered services;
- actions;
- automatic host creation.

No confundir con LLD.

---

# 13. AUTOREGISTRATION

## Zabbix Documentation — Active agent autoregistration

Utilizar para:

- active agents;
- metadata;
- HostMetadata;
- HostMetadataItem;
- actions;
- automatic host enrollment;
- Proxy scenarios.

---

# 14. AGENT

## Zabbix Documentation — Agent

Referencia para:

```text
zabbix_agentd
zabbix_agentd.conf
```

y para:

- passive checks;
- active checks;
- item keys;
- UserParameters;
- buffers;
- TLS;
- runtime behavior.

---

# 15. AGENT 2

## Zabbix Documentation — Agent 2

Referencia principal para:

```text
zabbix_agent2
zabbix_agent2.conf
```

y:

- architecture;
- plugins;
- supported metrics;
- active checks;
- passive checks;
- persistent buffering;
- plugin configuration;
- TLS.

Consultar además documentación específica del plugin utilizado.

---

# 16. AGENT 2 PLUGINS

## Zabbix Agent 2 plugin documentation

Utilizar para plugins como corresponda a la versión estudiada:

- systemd;
- PostgreSQL;
- MySQL;
- Docker;
- containers;
- certificates;
- MQTT;
- Modbus;
- SMART;
- otros plugins oficiales.

Verificar disponibilidad y versión antes de utilizar cualquier plugin en una lección.

---

# 17. SERVER

## Zabbix Server documentation

Referencia específica para:

```text
zabbix_server
zabbix_server.conf
```

Utilizar para:

- daemon;
- configuration;
- process parameters;
- caches;
- database;
- pollers;
- preprocessors;
- history;
- TLS;
- runtime control.

---

# 18. PROXY

## Zabbix Proxy documentation

Referencia específica para:

```text
zabbix_proxy
zabbix_proxy.conf
```

Utilizar para:

- active/passive mode;
- database;
- buffering;
- synchronization;
- TLS;
- Proxy groups;
- HA/failover cuando corresponda;
- performance.

---

# 19. HIGH AVAILABILITY

## Zabbix Server High Availability documentation

Utilizar para:

- native Server HA;
- nodes;
- active/standby behavior;
- heartbeat;
- failover;
- shared database;
- node status;
- configuration.

Complementar con documentación de Proxy groups para HA/distribución de proxies.

---

# 20. ZABBIX INTERNAL ITEMS

## Zabbix internal checks documentation

Fuente esencial para:

- Server health;
- process utilization;
- queue;
- caches;
- required performance;
- Proxy health;
- internal metrics.

Especialmente importante en:

```text
57. Performance tuning
58. Queue
59. Caches internas
63. Monitorización del propio Zabbix
68. Diagnóstico de Server
```

---

# 21. TEMPLATE DOCUMENTATION

## Zabbix official templates

Utilizar para:

- estudiar diseño real de templates;
- items;
- triggers;
- LLD;
- preprocessing;
- dependent items;
- macros;
- naming;
- tagging;
- best practices.

No copiar templates oficiales sin comprenderlos.

Los templates oficiales son material excelente para estudiar patrones de diseño Zabbix.

---

# 22. INTEGRATIONS AND MEDIA TYPES

## Zabbix Integrations

Referencia para:

- webhooks;
- ticketing;
- chat;
- incident management;
- third-party APIs;
- media types.

Comprobar siempre la versión de la integración.

---

# 23. POSTGRESQL — DOCUMENTACIÓN OFICIAL

## PostgreSQL Documentation

Fuente principal para el backend PostgreSQL.

Utilizar para:

- architecture;
- configuration;
- roles;
- databases;
- authentication;
- indexes;
- VACUUM;
- autovacuum;
- ANALYZE;
- WAL;
- checkpoints;
- backup;
- restore;
- performance;
- monitoring;
- partitioning.

La versión concreta debe ser compatible con la versión Zabbix utilizada.

---

# 24. POSTGRESQL STATISTICS

Utilizar documentación PostgreSQL para vistas y extensiones como:

```text
pg_stat_activity
pg_stat_database
pg_stat_bgwriter
pg_stat_wal
pg_stat_user_tables
pg_stat_user_indexes
pg_stat_statements
```

según disponibilidad en la versión PostgreSQL utilizada.

No asumir que todas las vistas conservan exactamente las mismas columnas entre versiones.

---

# 25. TIMESCALEDB

## TimescaleDB Documentation

Referencia cuando el laboratorio utilice TimescaleDB.

Estudiar:

- hypertables;
- chunks;
- compression;
- retention;
- PostgreSQL compatibility;
- storage;
- policies.

Comprobar siempre la matriz de compatibilidad:

```text
Zabbix
↔
PostgreSQL
↔
TimescaleDB
```

antes de recomendar versiones.

---

# 26. FEDORA

## Fedora Documentation

Referencia del sistema operativo principal.

Utilizar para:

- package management;
- systemd;
- networking;
- firewalld;
- SELinux;
- services;
- filesystem;
- permissions.

---

# 27. RPM Y DNF

## Fedora / RPM / DNF documentation

Utilizar para:

```bash
dnf
rpm
```

y:

- instalación;
- consulta de paquetes;
- archivos instalados;
- package ownership;
- updates;
- repositories.

---

# 28. SYSTEMD

## systemd manual pages

Referencias especialmente útiles:

```text
systemctl(1)
journalctl(1)
systemd.service(5)
systemd.exec(5)
systemd.unit(5)
journald.conf(5)
```

Utilizar para:

- lifecycle de servicios;
- logs;
- restart behavior;
- dependencies;
- security properties;
- diagnostics.

---

# 29. FIREWALLD

## firewalld Documentation

Utilizar para:

- services;
- ports;
- zones;
- rich rules cuando proceda;
- runtime/permanent;
- diagnostics.

No desactivar firewalld como solución normal.

---

# 30. SELINUX

## Fedora SELinux Documentation

## SELinux Project documentation

Utilizar para:

- contexts;
- AVC;
- booleans;
- ports;
- file labeling;
- policy;
- troubleshooting.

Herramientas relacionadas:

```text
ausearch
sealert
semanage
restorecon
ls -Z
ps -Z
```

---

# 31. NET-SNMP

## Net-SNMP Documentation

Referencia práctica principal para:

```text
snmpget
snmpwalk
snmpbulkwalk
snmptranslate
snmptrap
snmptrapd
```

Utilizar junto con los RFC correspondientes.

---

# 32. SNMP — RFC

Referencias normativas relevantes según tema:

- arquitectura SNMP;
- SMI;
- SNMPv2;
- SNMPv3;
- USM;
- VACM;
- transport mappings.

No llenar las lecciones introductorias con RFC innecesarios.

Usar la especificación exacta cuando la semántica del protocolo sea relevante.

---

# 33. JMX

## Oracle / OpenJDK JMX Documentation

Referencia para:

- JMX architecture;
- MBeans;
- ObjectName;
- attributes;
- remote management;
- connectors;
- authentication;
- security.

Utilizar conjuntamente con la documentación de Zabbix Java Gateway.

---

# 34. JAVA

## OpenJDK Documentation

Utilizar para:

- JVM;
- runtime;
- JMX;
- TLS;
- troubleshooting Java cuando sea relevante.

El PATH no debe transformarse en un curso general de Java.

---

# 35. HTTP

## HTTP Semantics

Referencia normativa cuando sea necesario comprender:

- methods;
- status codes;
- headers;
- authentication;
- request/response semantics.

Utilizar con HTTP Agent y web monitoring.

---

# 36. TLS

## OpenSSL Documentation

Utilizar para herramientas como:

```bash
openssl s_client
openssl x509
openssl verify
```

y conceptos:

- certificates;
- CA;
- chain;
- subject;
- issuer;
- expiration;
- handshake.

---

# 37. JSON

## JSON specification

Referencia para:

- Zabbix API;
- HTTP APIs;
- preprocessing;
- Server-Proxy protocol;
- trapper/sender payloads cuando corresponda.

---

# 38. JSON-RPC

## JSON-RPC 2.0 Specification

Referencia conceptual/normativa para comprender la API de Zabbix.

No asumir que conocer JSON equivale a conocer JSON-RPC.

---

# 39. JSONPath

Utilizar la documentación de Zabbix como autoridad principal sobre la implementación de JSONPath disponible en preprocessing.

No asumir que todas las implementaciones JSONPath admiten exactamente la misma sintaxis.

---

# 40. REGULAR EXPRESSIONS

Para regex dentro de Zabbix:

1. documentación Zabbix específica;
2. documentación de la implementación utilizada por la funcionalidad;
3. referencias generales únicamente como apoyo.

No asumir compatibilidad universal entre dialectos regex.

---

# 41. JAVASCRIPT EN ZABBIX

La implementación JavaScript utilizada por Zabbix debe estudiarse desde la documentación oficial correspondiente.

Utilizar para:

- preprocessing;
- Script items;
- webhooks;
- custom transformations.

No asumir que el entorno de ejecución equivale a Node.js o a un navegador.

---

# 42. PROMETHEUS

## Prometheus Documentation

Complementaria cuando se estudie:

- Prometheus pattern;
- Prometheus preprocessing;
- ingestion/integration;
- metric exposition formats.

Mantener el foco en cómo Zabbix consume o procesa estos datos.

---

# 43. GRAFANA

## Grafana Documentation

Complementaria en lecciones de integración y visualización externa.

No sustituir dashboards nativos de Zabbix por Grafana en los bloques dedicados al frontend Zabbix.

---

# 44. WIRESHARK

## Wireshark User's Guide / Display Filter Reference

Consulta para:

- protocol analysis;
- packet capture;
- TCP;
- TLS metadata;
- troubleshooting.

Utilizar tráfico generado en laboratorio.

---

# 45. TCPDUMP

## tcpdump manual

Referencia práctica para:

```bash
tcpdump
```

Utilizar para responder preguntas concretas de conectividad y flujo.

---

# 46. LIBROS — PRINCIPAL COMPLEMENTARIO

## Zabbix 7 IT Infrastructure Monitoring Cookbook

Utilizar como material complementario cuando la edición y los ejemplos correspondan suficientemente a la versión estudiada.

Útil especialmente para:

- casos prácticos;
- templates;
- discovery;
- preprocessing;
- monitoring patterns;
- integrations;
- operations.

La documentación oficial prevalece ante diferencias de versión.

---

# 47. LIBROS — ZABBIX INFRASTRUCTURE MONITORING

Libros especializados de Zabbix pueden utilizarse para:

- visión arquitectónica;
- conceptos históricos;
- patrones de monitorización;
- casos prácticos.

No utilizar capturas, menús, parámetros o procedimientos de una edición antigua como comportamiento actual sin verificarlos.

---

# 48. PROFUNDIZACIÓN — MONITORING

Material general sobre monitoring y observability puede utilizarse para:

- monitoring design;
- alert design;
- SLO/SLA;
- failure detection;
- capacity;
- cardinality;
- noise;
- alert fatigue.

Debe mantenerse separado de la semántica específica de Zabbix.

---

# 49. PROFUNDIZACIÓN — SITE RELIABILITY ENGINEERING

## Google — Site Reliability Engineering

## Google — The Site Reliability Workbook

Complementaria para:

- monitoring philosophy;
- alerting;
- SLI;
- SLO;
- incident response;
- capacity;
- reliability.

No presentar conceptos SRE como funcionalidades nativas de Zabbix cuando no lo sean.

---

# 50. PROFUNDIZACIÓN — SYSTEMS PERFORMANCE

## Brendan Gregg — Systems Performance

Complementaria para:

- CPU;
- memory;
- disk;
- network;
- performance methodology;
- USE method;
- latency;
- saturation;
- Linux observability.

Muy útil para diseñar qué debe monitorizar Zabbix en Linux.

---

# 51. PROFUNDIZACIÓN — BPF PERFORMANCE TOOLS

## Brendan Gregg — BPF Performance Tools

Complementaria en troubleshooting avanzado de Linux.

No es una referencia principal de Zabbix.

---

# 52. POLÍTICA DE CITACIÓN EN LAS LECCIONES

La sección:

# 📚 LECTURA

debe seleccionar únicamente referencias relevantes a la lección.

Ejemplo para una lección de preprocessing:

```text
📚 LECTURA

Principal
- Zabbix Documentation 7.4 — Item value preprocessing.

LTS
- Zabbix Documentation 7.0 — Item value preprocessing.

Profundización
- Zabbix Documentation — Dependent items, cuando sea relevante.
```

No incluir toda esta bibliografía en cada lección.

---

# 53. REFERENCIAS EXACTAS

Sólo proporcionar:

- capítulo;
- sección;
- versión;
- RFC;
- página;
- opción;
- parámetro;

cuando sea verificable.

No inventar números de página.

Los manuales web cambian y normalmente es preferible citar:

```text
obra/documentación
→ sección
→ tema
```

---

# 54. JERARQUÍA FINAL DE USO

Para comportamiento de Zabbix:

```text
Zabbix Documentation
        ↓
Zabbix source
        ↓
official integration/component docs
        ↓
books
        ↓
secondary material
```

Para protocolos externos:

```text
RFC/specification
        ↓
official implementation documentation
        ↓
Zabbix documentation
        ↓
secondary material
```

Para Fedora:

```text
Fedora documentation
        ↓
upstream project documentation
        ↓
RHEL documentation cuando aporte contexto
```

Para PostgreSQL:

```text
PostgreSQL documentation
        ↓
Zabbix requirements/recommendations
        ↓
TimescaleDB documentation si aplica
        ↓
books/secondary sources
```

Esta jerarquía debe preservar exactitud técnica y evitar que el PATH quede obsoleto por depender de material secundario.