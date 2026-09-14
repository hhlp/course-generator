# BIBLIOGRAPHY — GRAFANA + LOKI EN PROFUNDIDAD

## Criterio general

La bibliografía de este PATH prioriza documentación oficial porque Grafana, Loki, Alloy y sus interfaces evolucionan rápidamente.

Para configuración, opciones, defaults, funcionalidades disponibles, estados experimental/deprecated y procedimientos de upgrade, la documentación oficial de la versión estudiada tiene prioridad sobre cualquier libro o artículo.

Las referencias deben utilizarse por tema; no es necesario forzar una fuente bibliográfica en una lección si no aporta valor real.

---

## 1. Principal — Grafana

### Grafana Documentation
Grafana Labs.

Fuente principal para:

- instalación;
- configuración;
- administración;
- dashboards;
- panels;
- visualizaciones;
- variables;
- transformations;
- annotations;
- data links;
- Explore;
- data sources;
- Grafana Alerting;
- provisioning;
- HTTP API;
- autenticación;
- autorización;
- seguridad;
- high availability;
- troubleshooting.

Referencia web:

https://grafana.com/docs/grafana/latest/

### Grafana configuration reference

Usar para verificar:

- grafana.ini;
- variables de entorno;
- server;
- database;
- security;
- auth;
- logging;
- paths;
- feature toggles;
- parámetros cuyo default dependa de versión.

https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/

### Grafana HTTP API

Fuente normativa para endpoints, autenticación y payloads.

https://grafana.com/docs/grafana/latest/developers/http_api/

### Grafana Provisioning

Fuente principal para provisioning declarativo.

https://grafana.com/docs/grafana/latest/administration/provisioning/

### Grafana Alerting

Fuente principal para:

- alert rules;
- evaluation;
- contact points;
- notification policies;
- silences;
- mute timings;
- templates;
- provisioning;
- HA;
- meta-monitoring.

https://grafana.com/docs/grafana/latest/alerting/

---

## 2. Principal — Grafana Loki

### Grafana Loki Documentation
Grafana Labs.

Fuente principal de todo el bloque Loki.

https://grafana.com/docs/loki/latest/

Utilizar especialmente para:

- arquitectura;
- deployment modes;
- configuración;
- LogQL;
- labels;
- structured metadata;
- storage;
- TSDB;
- object storage;
- schema configuration;
- Compactor;
- retention;
- Ruler;
- multi-tenancy;
- limits;
- operations;
- troubleshooting.

### Loki Architecture

Referencia principal para comprender write path y read path.

https://grafana.com/docs/loki/latest/get-started/architecture/

### Loki Deployment Modes

Referencia principal para:

- monolithic;
- simple scalable deployment;
- microservices/distributed.

https://grafana.com/docs/loki/latest/get-started/deployment-modes/

### Loki Configuration Reference

Fuente normativa para bloques YAML, flags, defaults y opciones.

https://grafana.com/docs/loki/latest/configure/

### LogQL

Referencia principal del lenguaje.

https://grafana.com/docs/loki/latest/query/

### Loki Storage

Referencia principal del modelo de almacenamiento.

https://grafana.com/docs/loki/latest/configure/storage/

### Loki TSDB

Referencia principal para el index store TSDB.

https://grafana.com/docs/loki/latest/operations/storage/tsdb/

### Loki Retention

Referencia principal para Compactor y políticas de retención.

https://grafana.com/docs/loki/latest/operations/storage/retention/

### Loki Operations

Usar para administración, escalado, observabilidad, límites y troubleshooting.

https://grafana.com/docs/loki/latest/operations/

---

## 3. Principal — Grafana Alloy

### Grafana Alloy Documentation
Grafana Labs.

Fuente principal para el collector utilizado en el PATH.

https://grafana.com/docs/alloy/latest/

Temas:

- instalación;
- configuración;
- component model;
- discovery;
- loki.source.*;
- loki.process;
- loki.relabel;
- loki.write;
- journald;
- file logs;
- syslog;
- container logs;
- debugging;
- métricas internas;
- migración desde agentes anteriores.

### Alloy Loki Components

Referencia específica de componentes Loki.

https://grafana.com/docs/alloy/latest/reference/components/loki/

### Migrate to Alloy

Utilizar para entender migración desde Promtail u otros agentes cuando corresponda.

https://grafana.com/docs/alloy/latest/set-up/migrate/

---

## 4. Integración — Prometheus

### Prometheus Documentation
Prometheus Authors / CNCF.

https://prometheus.io/docs/

Uso dentro de este PATH:

- data source Prometheus en Grafana;
- modelo de labels;
- lectura de métricas;
- correlación métricas/logs;
- integración de Grafana Alerting;
- métricas internas de Grafana/Loki/Alloy.

No utilizar esta bibliografía para reenseñar el PATH completo de Prometheus.

### PromQL

https://prometheus.io/docs/prometheus/latest/querying/basics/

Sólo como referencia cuando una lección compare PromQL con LogQL o utilice métricas Prometheus.

---

## 5. Plataforma — Fedora Linux

### Fedora Documentation

https://docs.fedoraproject.org/

Usar para:

- gestión de paquetes;
- servicios;
- integración con Fedora;
- seguridad;
- networking;
- SELinux cuando corresponda.

### systemd

Documentación del proyecto y manuales locales.

https://systemd.io/

Referencias locales preferentes:

- man systemctl
- man systemd.service
- man systemd.exec
- man journalctl
- man journald.conf

Utilizar para:

- unidades de Grafana/Loki/Alloy;
- logs;
- environment;
- credentials;
- hardening;
- restart policies;
- resource controls.

### firewalld

https://firewalld.org/documentation/

Utilizar para exponer únicamente los servicios necesarios y diseñar acceso por zonas/políticas cuando aplique.

### SELinux

Fedora SELinux documentation:

https://docs.fedoraproject.org/en-US/quick-docs/selinux-getting-started/

También utilizar las herramientas locales cuando corresponda:

- getenforce
- sestatus
- ls -Z
- ps -eZ
- ausearch
- sealert
- semanage
- restorecon

Nunca recomendar desactivar SELinux como solución normal.

---

## 6. Observabilidad — fundamentos y profundización

### Observability Engineering
Charity Majors, Liz Fong-Jones, George Miranda.
O'Reilly Media, 2022.

Uso:

- fundamentos de observabilidad;
- debugging en producción;
- alta cardinalidad;
- contexto;
- diseño de telemetría;
- investigación de sistemas complejos.

No tratar este libro como referencia normativa para configuración de Grafana/Loki.

### Site Reliability Engineering
Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.).
O'Reilly Media / Google.

https://sre.google/sre-book/table-of-contents/

Uso:

- monitoring;
- alerting;
- SLO/SLA como contexto;
- incident response;
- operación de sistemas;
- reducción de ruido.

### The Site Reliability Workbook
Betsy Beyer et al.
O'Reilly Media / Google.

https://sre.google/workbook/table-of-contents/

Uso:

- alerting práctico;
- monitoring distribuido;
- incident response;
- operational readiness.

---

## 7. Protocolos, formatos y tecnologías auxiliares

### RFC 5424 — The Syslog Protocol
IETF.

https://www.rfc-editor.org/rfc/rfc5424

Usar en lecciones de ingestión syslog.

### JSON
RFC 8259.

https://www.rfc-editor.org/rfc/rfc8259

Utilizar como referencia conceptual cuando se analicen logs JSON.

### HTTP Semantics
RFC 9110.

https://www.rfc-editor.org/rfc/rfc9110

Referencia de apoyo para APIs y comportamiento HTTP.

### TLS
Utilizar documentación del componente concreto y políticas criptográficas del sistema operativo.

No introducir configuraciones criptográficas obsoletas sólo porque aparezcan en tutoriales antiguos.

---

## 8. Código fuente — profundización e internals

### Grafana source code

https://github.com/grafana/grafana

Uso:

- arquitectura del proyecto;
- backend;
- frontend;
- plugins;
- API;
- alerting;
- provisioning;
- internals.

### Loki source code

https://github.com/grafana/loki

Uso:

- módulos;
- ring;
- distributor;
- ingester;
- WAL;
- query engine;
- LogQL;
- Compactor;
- Ruler;
- storage;
- internals.

### Grafana Alloy source code

https://github.com/grafana/alloy

Uso:

- component model;
- collectors;
- discovery;
- Loki pipeline;
- internals cuando una lección lo requiera.

---

## 9. Fuentes históricas / compatibilidad

### Promtail documentation

Promtail puede aparecer para comprender instalaciones existentes y migraciones.

No debe ser la herramienta preferida para nuevos laboratorios del PATH.

Consultar documentación oficial de Loki/Grafana sobre estado de soporte y migración antes de enseñar procedimientos actuales.

### BoltDB Shipper / legacy index stores

Estudiar sólo cuando:

- se analice una instalación antigua;
- se estudie evolución de Loki;
- sea necesario preparar una migración.

Para nuevos diseños, utilizar la recomendación actual de la documentación oficial.

### Table Manager

Considerarlo tecnología legacy/deprecated para nuevos despliegues.

No utilizarlo como solución principal de retención en una instalación moderna basada en TSDB.

---

## 10. Política de lectura por lección

La sección 📚 LECTURA, cuando sea requerida por el perfil, debe seleccionar sólo referencias relevantes.

Categorías recomendadas:

### Principal

Documentación oficial del producto que constituye el tema de la lección.

Ejemplos:

- Grafana Docs
- Loki Docs
- Alloy Docs

### Normativa / Referencia

Configuración, API, RFC o manual que define el comportamiento exacto.

Ejemplos:

- Configuration Reference
- HTTP API
- RFC 5424
- systemd man pages

### Profundización

Fuentes que explican arquitectura, operaciones o principios de observabilidad con mayor contexto.

Ejemplos:

- Observability Engineering
- SRE Book
- código fuente

### Consulta

Documentación auxiliar útil para el laboratorio.

Ejemplos:

- Fedora Docs
- firewalld
- SELinux
- systemd
- Prometheus Docs

---

## 11. Política de referencias exactas

1. No inventar capítulos, secciones, páginas o anchors.
2. Sólo indicar una referencia exacta cuando haya sido verificada.
3. Para documentación web cambiante, es preferible citar título de sección y URL estable.
4. Si una opción de configuración puede haber cambiado, verificar la versión actual antes de afirmarla.
5. Indicar cuando una funcionalidad sea:
   - experimental;
   - preview;
   - deprecated;
   - legacy;
   - Enterprise;
   - Grafana Cloud;
   - no disponible en OSS.
6. Las referencias bibliográficas deben ayudar a estudiar el tema, no rellenar una plantilla.

---

## 12. Mapa bibliográfico por áreas

| Área | Fuente principal | Complementaria |
|---|---|---|
| Grafana | Grafana Documentation | código fuente Grafana |
| Dashboards | Grafana Dashboards docs | Grafana source |
| Data sources | Grafana Data sources docs | documentación del backend concreto |
| Explore | Grafana Explore docs | Loki/Prometheus docs |
| Alerting | Grafana Alerting docs | SRE Book / Workbook |
| Provisioning | Grafana Provisioning docs | HTTP API |
| API | Grafana HTTP API | curl/jq docs |
| Loki | Loki Documentation | Loki source |
| LogQL | Loki LogQL docs | Loki source |
| Arquitectura Loki | Loki Architecture docs | Loki source |
| Deployment modes | Loki Deployment Modes | operations docs |
| Storage | Loki Storage docs | TSDB docs |
| Retention | Loki Retention docs | Compactor config reference |
| Alloy | Alloy Documentation | Alloy source |
| Journald | Alloy + systemd docs | Fedora docs |
| Syslog | Alloy + RFC 5424 | syslog implementation docs |
| Seguridad | docs oficiales + Fedora | systemd/firewalld/SELinux |
| HA | Grafana/Loki operations docs | SRE material |
| Capacity planning | operations + métricas reales | SRE material |
| Internals | código fuente | architecture docs |

---

## 13. Regla final

En caso de conflicto entre un libro, tutorial, ejemplo antiguo y documentación oficial vigente:

**prevalece la documentación oficial de la versión que se está utilizando.**
