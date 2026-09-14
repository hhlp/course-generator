# domain.md — Prometheus

## Dominio

Este PATH enseña Prometheus desde nivel inicial hasta nivel experto, con orientación principal a administración, operación, arquitectura, diagnóstico e internals en sistemas Linux, especialmente Fedora.

El objetivo no es formar principalmente a un desarrollador de exporters o de Prometheus, sino a un administrador/ingeniero capaz de comprender, desplegar, mantener, asegurar, diagnosticar, escalar y diseñar una plataforma Prometheus de producción.

## Alcance principal

El curso debe cubrir con profundidad:

- fundamentos de monitorización y observabilidad;
- arquitectura de Prometheus;
- instalación y operación en Fedora;
- configuración de Prometheus;
- modelo dimensional y modelo de datos;
- exposición de métricas y scraping;
- exporters;
- targets;
- service discovery;
- relabeling y metric relabeling;
- PromQL desde fundamentos hasta nivel avanzado;
- recording rules;
- alerting rules;
- Alertmanager;
- HTTP API;
- TSDB;
- federation;
- remote write y remote read;
- Prometheus Agent Mode;
- alta disponibilidad;
- escalabilidad y rendimiento;
- seguridad;
- troubleshooting;
- testing de reglas;
- diseño de monitorización;
- integración mínima con Grafana;
- integración con el ecosistema de observabilidad;
- internals de scraping, TSDB, PromQL, rules, alerting y remote;
- lectura orientativa del código fuente;
- arquitecturas avanzadas;
- operación en producción;
- proyecto final completo.

## Enfoque de Exporters

El bloque de exporters debe enseñar:

- qué es un exporter y por qué existe;
- cómo descubrir exporters disponibles;
- cómo distinguir exporters oficiales, mantenidos por proyectos y comunitarios;
- cómo evaluar mantenimiento, seguridad, compatibilidad y calidad;
- cómo instalar y ejecutar exporters;
- cómo integrarlos en systemd;
- cómo añadirlos a Prometheus;
- cómo revisar sus métricas y collectors;
- cómo limitar collectors o métricas cuando sea necesario;
- cómo diagnosticar exporters;
- cómo estimar su impacto de cardinalidad;
- cuándo usar instrumentación nativa;
- cuándo usar Pushgateway;
- cuándo tendría sentido escribir un exporter propio.

No debe convertirse en un curso de programación de exporters. La implementación en Go u otros lenguajes se estudia solo en el nivel necesario para comprender su arquitectura interna y poder leer documentación o código fuente.

## Enfoque Fedora

Cuando sea relevante, las lecciones deben utilizar Fedora como sistema de referencia e integrar:

- RPM;
- systemd;
- journalctl;
- firewalld;
- SELinux;
- permisos y usuarios de servicio;
- filesystem;
- herramientas de red;
- TLS;
- troubleshooting del sistema.

No se deben inventar paquetes RPM si una versión concreta de Fedora no los ofrece. Cuando corresponda, explicar la diferencia entre paquetes de la distribución y binarios oficiales upstream.

## PromQL

PromQL es una competencia central del PATH.

Debe enseñarse progresivamente y con profundidad, incluyendo:

- selectors;
- instant vectors;
- range vectors;
- scalars;
- operadores;
- agregaciones;
- funciones;
- counters;
- rate, irate e increase;
- range functions;
- subqueries;
- vector matching;
- on e ignoring;
- group_left y group_right;
- histogramas clásicos;
- native histograms;
- histogram_quantile;
- consultas RED;
- consultas USE;
- Golden Signals;
- SLI/SLO;
- burn rates;
- optimización;
- cardinalidad;
- anti-patterns.

Las expresiones deben explicarse paso a paso, no presentarse como recetas opacas.

## Alertas y Alertmanager

Prometheus y Alertmanager deben distinguirse claramente.

Prometheus:

- evalúa alerting rules;
- mantiene estados inactive/pending/firing;
- envía alertas.

Alertmanager:

- agrupa;
- deduplica;
- enruta;
- inhibe;
- silencia;
- entrega notificaciones.

Debe enseñarse el flujo completo y su troubleshooting.

## TSDB

La TSDB debe cubrir tanto administración como internals:

- Head;
- WAL;
- checkpoints;
- chunks;
- blocks;
- index;
- postings;
- tombstones;
- compaction;
- retention;
- snapshots;
- backup;
- restore;
- corrupción;
- recovery;
- cardinalidad;
- churn;
- capacidad y rendimiento.

## Internals

Los bloques avanzados deben explicar cómo funciona Prometheus internamente sin exigir convertirse en desarrollador del proyecto.

Se debe poder seguir conceptualmente:

exporter → service discovery → target → relabeling → scrape loop → parser → sample validation → TSDB Head/WAL → blocks → query engine → recording/alerting rules → notifier → Alertmanager → remote write.

## Grafana

Grafana solo se cubre como integración básica con Prometheus.

La creación avanzada de dashboards, variables, transformations, provisioning, alerting de Grafana, Loki y operación de Grafana pertenecen a su PATH independiente.

## Seguridad

La seguridad debe incluir:

- exposición de endpoints;
- autenticación;
- TLS;
- reverse proxies;
- web config;
- secretos;
- credenciales de service discovery;
- remote write;
- exporters;
- usuario sin privilegios;
- filesystem;
- systemd hardening;
- SELinux;
- firewalld;
- segmentación de red;
- principio de mínimo privilegio.

## Troubleshooting

El curso debe enseñar diagnóstico sistemático, no solo listas de errores.

Se deben utilizar cuando corresponda:

- systemctl;
- journalctl;
- promtool;
- amtool;
- curl;
- jq;
- ss;
- herramientas DNS;
- herramientas TLS;
- tcpdump;
- endpoints /targets, /rules, /alerts y /status;
- métricas internas de Prometheus;
- análisis de TSDB;
- análisis de remote write.

## Formato pedagógico obligatorio

Cada lección debe comenzar con:

🎯 OBJETIVO

El desarrollo debe ser profundo, didáctico y autocontenido.

Cuando aporten valor pueden incluirse:

🧪 Laboratorio/ejemplos
⚠️ Errores frecuentes
💡 Idea importante

Cada lección debe terminar con:

🧠 QUÉ DEBES RECORDAR

Esta sección debe contener de 3 a 7 ideas esenciales de la lección y no limitarse a repetir el objetivo.

## Nivel de profundidad

No producir resúmenes superficiales.

Cada lección debe explicar:

- qué es;
- por qué existe;
- cómo funciona;
- dónde encaja;
- cómo se configura o utiliza;
- cómo verificarlo;
- cómo diagnosticarlo;
- riesgos o errores frecuentes;
- relación con conceptos anteriores y posteriores.

Cuando se estudie un comando o una opción, explicar su propósito y cómo comprobar su efecto.

## Proyecto final

El proyecto final debe integrar una plataforma Prometheus operativa y diagnosticable, incluyendo:

Prometheus + exporters + service discovery + relabeling + PromQL + recording rules + alerting rules + Alertmanager + TSDB + HA/remote cuando corresponda + seguridad + testing + troubleshooting + documentación + runbooks.

El alumno debe ser capaz de reconstruir y explicar el flujo completo de una métrica desde su origen hasta una consulta o alerta.
