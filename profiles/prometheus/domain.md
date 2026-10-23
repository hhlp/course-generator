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

El descubrimiento y el relabeling construyen los targets. El flujo de muestras sigue: exporter → scrape loop → parser → validación → TSDB (Head/WAL y bloques persistentes).

A partir de ahí se distinguen caminos relacionados:

- Consulta: almacenamiento → query engine → resultados de PromQL.
- Reglas: evaluación de PromQL → recording rules (nuevas series) o alerting rules (estados de alerta).
- Alertas: alerting rules → notifier → Alertmanager → receivers.
- Remote write: lectura del WAL → colas y shards → receptor remoto. No pasa por Alertmanager. En Agent Mode se estudian su WAL y sus diferencias respecto al servidor completo.

Este esquema describe dependencias lógicas; no impone que la consulta espere a la creación de bloques persistentes.

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


## Requisitos ampliados de profundidad (revisión 2026)

- Conservar los bloques 0–40 y todos los IDs originales. Las lecciones añadidas deben numerarse consecutivamente dentro de cada bloque.
- PromQL: demostrar semántica de staleness, ausencia frente a cero, lookback, vector matching, subqueries, anotaciones y histogramas clásicos/nativos; explicar restricciones dependientes de versión.
- Scraping: diferenciar límites de targets, samples, labels y tamaño de respuesta; comprobar el punto del pipeline donde se aplica cada límite.
- Exporters: evaluar privilegios, coste de collectors, compatibilidad, mantenimiento, seguridad y cardinalidad; priorizar instalación y operación sobre programación.
- TSDB: incluir cálculos cuantitativos de ingesta, retención, series activas, churn, RAM y almacenamiento; ejercicios de recuperación y consistencia.
- Remote Write: comparar versiones de protocolo, compatibilidad con receptores, colas, reintentos, backpressure, backlog y recuperación.
- HA: distinguir disponibilidad de scraping, ingesta, consultas y notificaciones; comparar conceptualmente Thanos, Mimir y VictoriaMetrics sin desarrollar sus cursos completos.
- Seguridad Fedora: incluir mínimo privilegio, systemd-analyze security, TLS, secretos, auditoría SELinux, firewalld y segmentación de red.
- Producción: incluir Ansible, validación de configuración, tests de reglas en CI/CD, rollout, rollback, meta-monitoring, RPO/RTO y runbooks verificables.
- Internals: seguir implementaciones en un tag/commit reproducible, con profiling y lectura guiada; no exigir desarrollar Prometheus.
- Cada laboratorio debe incluir prerrequisitos, pasos reproducibles, comandos explicados, resultados esperados, verificación, errores frecuentes, limpieza y evidencia de aprendizaje.
- No asumir que una opción, endpoint o feature flag existe en todas las versiones; contrastar con documentación oficial y `--help`.

## Límites entre PATHs

Grafana, Kubernetes, OpenTelemetry, Ansible y las plataformas de almacenamiento distribuido se tratan solo en la medida necesaria para integrar u operar Prometheus. El aprendizaje avanzado de esas tecnologías pertenece a sus respectivos PATHs.


## Contrato pedagógico de las lecciones y dependencias

Conservar todos los IDs y el orden. Una entrada breve tiene un objetivo concreto; su profundidad depende de la complejidad del concepto, sin imponer una longitud mínima artificial. No volver a desarrollar el mismo fundamento en cada lección.

Cada lección debe declarar sus prerrequisitos por ID y su aportación nueva. Referenciar explicaciones previas y reservar el contenido avanzado para su bloque. Por ejemplo, 9.24 trabaja sum y agrupación; 10.28 profundiza en el orden rate/agregación; 15 aplica esa base a recording rules. Los comandos systemd se explican con el servicio real y verificaciones específicas.

Distinguir presentación conceptual, uso operativo e internals. Los laboratorios acumulativos reutilizan el entorno y añaden una avería, medición o decisión nueva. No ejecutar recuperaciones destructivas sobre la instancia de trabajo: usar una copia aislada y documentar la pérdida potencial.

La integración con Operator del bloque 32 es opcional y requiere conocimientos previos de Kubernetes. Cubre recursos de monitorización, selección y diagnóstico de configuración generada; la administración del clúster se deriva al PATH de Kubernetes.

El perfil referencia ../../config/pedagogy.md como dependencia del repositorio de destino. No se ha facilitado ese archivo: comprobar su existencia y coherencia antes de generar. Este paquete no incluye ni sustituye esa política externa. Validar también el perfil con el esquema real de course-generator: un YAML sintácticamente válido no acredita compatibilidad con su consumidor.

## Reproducibilidad y migración

Antes de cada laboratorio, registrar versión de Fedora, Prometheus, promtool, Alertmanager, amtool y exporters utilizados; añadir receptor remoto y Operator cuando intervengan. Elegir versiones concretas de laboratorio y guardar flags efectivos, configuración y referencias correspondientes. No tomar latest o main como una versión reproducible.

La migración 2.x → 3.x se estudia mediante la guía oficial, inventario de cambios y pruebas comparativas de configuración, consultas, scraping y reglas. Las migraciones posteriores requieren sus propias notas de versión. El rollback no presupone que un binario antiguo pueda abrir una TSDB modificada: conservar copia anterior y ensayar restauración aislada.

## Proyecto final por fases y aceptación

Las entradas 40.1–40.77 conservan su significado; las lecciones añadidas definen las fases. Todas las evidencias deben incluir comandos, resultados y versiones. Se proponen estos umbrales pedagógicos, ajustables en el ADR inicial:

| Fase | Trabajo y referencias | Criterio verificable |
| --- | --- | --- |
| 1. Diseño | 40.1–40.3, 40.15–40.16, 40.23–40.24 | Inventario, ADR, versiones, presupuesto de series y SLO definidos antes del despliegue. |
| 2. Despliegue | 40.4–40.18, 40.40–40.43 | Todos los targets previstos UP durante al menos tres scrapes; verificación TLS y de accesos permitidos/denegados; segunda aplicación Ansible sin cambios no justificados. |
| 3. Consultas y alertas | 40.19–40.33, 40.46–40.47 | Validaciones de configuración y reglas sin errores; suite positiva y negativa superada; evidencia de pending/firing/resolución y recepción en un receptor de laboratorio. |
| 4. Capacidad y continuidad | 40.34–40.39, 40.44–40.54 | Medir ingesta, RAM, disco, series y backlog frente al presupuesto; ejecutar fallo de réplica si hay HA; restauración que cumpla el RPO/RTO declarado. |
| 5. Entrega | 40.55–40.77 | Repositorio, CI, runbooks e informes completos; reconstrucción en entorno limpio y trazabilidad de cada requisito a una evidencia. |

Usar un receptor de pruebas para notificaciones. Los escenarios HA y remote write deben señalar topología y componentes necesarios. Un componente fuera de alcance debe justificarse; no afirmar resiliencia que no se haya probado.
