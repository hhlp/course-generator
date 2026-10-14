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
- OpenSearch Benchmark: https://opensearch.org/docs/latest/benchmark/ (comprobar ruta vigente).
- Documentación oficial de OpenSearch: Neural Search, ML Commons, Vector Search, Search Pipelines y evaluación de relevancia. https://docs.opensearch.org/

### Data Streams, almacenamiento y migraciones
- Documentación oficial de OpenSearch sobre Data Streams, segment replication, remote-backed storage, snapshots, cross-cluster replication y upgrades. https://docs.opensearch.org/

### IaC y plataforma
- Documentación oficial de Terraform, Ansible, Fedora, systemd, SELinux y Podman; confirmar módulos y providers compatibles antes de utilizarlos.

**Criterio:** los libros externos explican principios generales; para configuración, endpoints, versiones y disponibilidad prevalece la documentación oficial de OpenSearch.
