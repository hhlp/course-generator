# BIBLIOGRAPHY — OPENSEARCH STACK EN PROFUNDIDAD

## Principal

### OpenSearch Documentation
Documentación oficial del proyecto OpenSearch.

Uso: fuente principal para OpenSearch, APIs, índices, mappings, Query DSL, agregaciones, clustering, seguridad, administración, plugins, observabilidad y capacidades de búsqueda.

https://docs.opensearch.org/

### Data Prepper Documentation
Documentación oficial de Data Prepper.

Uso: arquitectura de pipelines, sources, processors, sinks, buffers, routes, acknowledgements, OpenTelemetry, configuración, operación y troubleshooting.

https://docs.opensearch.org/latest/data-prepper/

## OpenSearch Dashboards

### OpenSearch Dashboards Documentation
Utilizar la documentación oficial de OpenSearch para Dashboards y sus aplicaciones.

Uso: Discover, visualizaciones, dashboards, Dev Tools, observabilidad, seguridad y administración.

https://docs.opensearch.org/latest/dashboards/

## Seguridad

### Security
Documentación oficial del Security plugin.

Uso: TLS, certificados, usuarios, roles, role mappings, autenticación, autorización, DLS, FLS, multi-tenancy y audit logging.

https://docs.opensearch.org/latest/security/

## Alerting y análisis

### Alerting
Uso: monitors, triggers, alerts y automatización.

https://docs.opensearch.org/latest/observing-your-data/alerting/

### Anomaly Detection
Uso: Random Cut Forest, detectors, features, resultados y operación.

https://docs.opensearch.org/latest/observing-your-data/ad/

### Security Analytics
Uso: detectors, findings, detection rules y análisis de eventos de seguridad.

https://docs.opensearch.org/latest/security-analytics/

## Gestión de datos

### Index State Management
Uso: policies, states, transitions, rollover, retención y automatización del ciclo de vida.

Consultar la sección Index State Management de la documentación oficial de OpenSearch.

### Snapshot and Restore
Uso: repositories, snapshots, restore, backup y disaster recovery.

Consultar la documentación oficial actual de Snapshot/Restore y Snapshot Management.

## Búsqueda avanzada

### k-NN / Vector Search
Uso: vectores, ANN, HNSW, semantic search y rendimiento.

Consultar la documentación oficial actual de Vector Search de OpenSearch.

### ML Commons
Uso: modelos, connectors, deployment, inference y capacidades ML/AI.

Consultar la documentación oficial actual de ML Commons.

## OpenTelemetry

### OpenTelemetry Documentation
Uso: OTLP, signals, Collector, semantic conventions, traces, metrics, logs y context propagation.

https://opentelemetry.io/docs/

### OpenTelemetry Specification
Uso: detalles normativos de OTLP, modelo de datos y propagación.

https://opentelemetry.io/docs/specs/

## Internals

### Apache Lucene
Documentación y código fuente oficial.

Uso: inverted index, segments, postings, doc values, FST, BKD trees, scoring y estructuras internas que sustentan OpenSearch.

https://lucene.apache.org/

### OpenSearch source code
Uso: internals, arquitectura, plugins, transport, cluster, index y search layers.

https://github.com/opensearch-project/OpenSearch

### OpenSearch Dashboards source code

https://github.com/opensearch-project/OpenSearch-Dashboards

### Data Prepper source code

https://github.com/opensearch-project/data-prepper

## Fedora

### Fedora Documentation
Uso: RPM, systemd, SELinux, firewalld, Podman y administración del host.

https://docs.fedoraproject.org/

## Complementaria

Para fundamentos que OpenSearch comparte con sistemas de recuperación de información y motores basados en Lucene pueden utilizarse textos técnicos sobre information retrieval, sistemas distribuidos, JVM y Lucene.

La bibliografía complementaria nunca debe utilizarse para asumir compatibilidad exacta con APIs o funcionalidades de OpenSearch.

## Regla de actualización

Antes de generar una lección dependiente de versión, contrastar conceptos, nombres de APIs, plugins y opciones con la documentación oficial de la versión contemporánea.

Las referencias a Elasticsearch pueden utilizarse únicamente como contexto histórico o comparación explícita, nunca como autoridad primaria sobre el comportamiento actual de OpenSearch.


## Bibliografía complementaria por scope (revisión ampliada)

### Information Retrieval y relevancia
- Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze — *Introduction to Information Retrieval*. Fundamentos de indexación, evaluación y recuperación. https://nlp.stanford.edu/IR-book/
- Doug Turnbull y John Berryman — *Relevant Search*. Relevancia, evaluación y ajuste de búsqueda; no asumir equivalencia de APIs.

### Apache Lucene e internals
- Michael McCandless, Erik Hatcher y Otis Gospodnetic — *Lucene in Action*, 2.ª edición. Fundamentos históricos de Lucene; validar internals contemporáneos en fuentes oficiales.
- Documentación de Apache Lucene: https://lucene.apache.org/

### Sistemas distribuidos
- Martin Kleppmann — *Designing Data-Intensive Applications*. Replicación, consistencia, particionado y tolerancia a fallos.

### Observabilidad y SRE
- Charity Majors, Liz Fong-Jones y George Miranda — *Observability Engineering*. Instrumentación, señales y diagnóstico.
- Google — *Site Reliability Engineering*. SLO, incidentes y operación. https://sre.google/books/

### Benchmarking y Search AI
- OpenSearch Benchmark: https://docs.opensearch.org/latest/benchmark/quickstart/
- Documentación oficial de OpenSearch: Neural Search, ML Commons, Vector Search, Search Pipelines y evaluación de relevancia. https://docs.opensearch.org/

### Data Streams, almacenamiento y migraciones
- Documentación oficial de OpenSearch sobre Data Streams, segment replication, remote-backed storage, snapshots, cross-cluster replication y upgrades. https://docs.opensearch.org/

### IaC y plataforma
- Documentación oficial de Terraform, Ansible, Fedora, systemd, SELinux y Podman; confirmar módulos y providers compatibles antes de utilizarlos.

**Criterio:** los libros externos explican principios generales; para configuración, endpoints, versiones y disponibilidad prevalece la documentación oficial de OpenSearch.


## Referencias específicas de la ampliación y correcciones

Estas entradas complementan las fuentes anteriores. Seleccionar la versión de
documentación que coincida con el laboratorio, registrar fecha de consulta y
comprobar prerrequisitos, plugins y restricciones antes de ejecutar.

### Bloque 61 — Data Streams
https://docs.opensearch.org/latest/opensearch/data-streams/

Uso: timestamps, backing indices, operaciones admitidas, templates y rollover.

### Bloque 62 — Replicación y almacenamiento
https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/segment-replication/index/
https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/remote-store/migrating-to-remote/
https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/remote-store/remote-cluster-state/
https://docs.opensearch.org/latest/tuning-your-cluster/separate-index-and-search-workloads/

Uso: estrategias de replicación, requisitos de almacenamiento remoto y recuperación.
Distinguir durabilidad remota, réplicas y backups recuperables en el tiempo.

### Bloque 63 — Relevancia y RAG
https://opensearch.org/platform/search-relevance/
https://docs.opensearch.org/latest/tutorials/gen-ai/rag/index/
https://docs.opensearch.org/latest/search-plugins/search-pipelines/rag-processor/

Uso: evaluación de recuperación, búsqueda híbrida y conexión con generación.
La evaluación de las respuestas requiere un protocolo distinto de las métricas ANN.

### Bloque 64 — SRE y rendimiento
https://sre.google/books/
https://docs.opensearch.org/latest/benchmark/quickstart/
https://docs.opensearch.org/latest/benchmark/reference/commands/run/
https://github.com/opensearch-project/opensearch-benchmark-workloads

Uso: objetivos de servicio, carga reproducible, métricas y ejercicios de recuperación.

### Bloque 65 — IaC
https://developer.hashicorp.com/terraform/docs
https://docs.ansible.com/
https://docs.fedoraproject.org/

Uso: ciclo de estado, idempotencia, configuración del host y automatización.
Documentar el provider, colección u operador elegido y su compatibilidad; no
presuponer que un provider de un servicio administrado administra cualquier cluster.

### Bloque 66 — Migraciones
https://docs.opensearch.org/latest/migration-assistant/
https://docs.opensearch.org/latest/migration-assistant/migration-phases/
https://github.com/opensearch-project/opensearch-migrations
https://docs.opensearch.org/latest/migration-assistant/migration-phases/migrate-metadata/transform-flattened-flat-object/

Uso: evaluación de compatibilidad, migración de metadatos, backfill y transición.
Comprobar la edición y versión de Migration Assistant: sus dependencias y alcance
no deben confundirse con los de la migración manual mediante APIs.

### Correcciones en bloques 6, 8 y 20
https://docs.opensearch.org/latest/field-types/flat-object/
https://docs.opensearch.org/latest/mappings/supported-field-types/derived/
https://docs.opensearch.org/latest/security/multi-tenancy/tenant-index/
https://docs.opensearch.org/latest/dashboards/workspace/workspace/

Uso: nombres y semántica propios de OpenSearch, límites de campos calculados,
aislamiento de objetos y organización por equipos.
