# BIBLIOGRAFÍA — ELASTIC STACK EN PROFUNDIDAD

## Principal

### Documentación oficial de Elastic

Fuente principal y normativa para comportamiento actual del producto.

Utilizar la documentación oficial correspondiente a la versión estable estudiada para:

- Elasticsearch Reference.
- Kibana Guide.
- Logstash Reference.
- Beats documentation.
- Elastic Agent.
- Fleet and Elastic Agent Guide.
- Elastic Common Schema (ECS).
- Elastic Observability.
- Elastic APM.
- Elasticsearch REST APIs.
- Elasticsearch security.
- Index Lifecycle Management.
- Snapshot and Restore.
- Snapshot Lifecycle Management.
- Cross-Cluster Search.
- Cross-Cluster Replication.
- Upgrade and migration guidance.

La documentación oficial prevalece sobre libros cuando existan diferencias causadas por evolución de versiones.

## Complementaria

### Clinton Gormley, Zachary Tong — Elasticsearch: The Definitive Guide

Uso:

- fundamentos conceptuales de Elasticsearch;
- búsqueda;
- análisis;
- mappings;
- arquitectura distribuida;
- shards y replicas;
- explicación pedagógica de internals históricos.

Advertencia:

Es una obra valiosa para fundamentos, pero describe generaciones antiguas de Elasticsearch. No copiar APIs, tipos, defaults ni procedimientos sin contrastarlos con documentación oficial actual.

### Radu Gheorghe, Matthew Lee Hinman, Roy Russo — Elasticsearch in Action

Uso:

- modelo mental de búsqueda;
- indexación;
- Query DSL;
- relevancia;
- análisis;
- diseño de búsquedas.

Contrastar detalles dependientes de versión con la documentación oficial.

### Bharvi Dixit — Mastering Elasticsearch

Uso:

- profundización conceptual;
- administración;
- rendimiento;
- búsqueda;
- arquitectura.

Usar como apoyo y verificar cualquier comportamiento dependiente de versión.

## Profundización

### Apache Lucene — documentación oficial

Uso:

- inverted index;
- segments;
- postings;
- doc values;
- scoring;
- BM25;
- estructuras internas;
- comportamiento del motor subyacente.

La finalidad es comprender Elasticsearch, no desarrollar una aplicación Lucene completa.

### Michael McCandless, Erik Hatcher, Otis Gospodnetic — Lucene in Action

Uso:

- fundamentos de indexación y búsqueda;
- análisis de texto;
- scoring;
- estructuras conceptuales de Lucene.

Por su antigüedad, usar para fundamentos, no como referencia de APIs actuales.

## Logstash e ingestión

### Documentación oficial de Logstash

Fuente principal para:

- pipeline model;
- inputs;
- filters;
- outputs;
- codecs;
- Grok;
- Dissect;
- persistent queues;
- dead letter queues;
- multiple pipelines;
- monitoring;
- performance tuning;
- plugin behavior.

### Documentación oficial de Beats

Fuente principal para:

- Filebeat;
- Metricbeat;
- Auditbeat;
- Heartbeat;
- Packetbeat cuando sea relevante;
- modules;
- inputs;
- processors;
- outputs;
- registry;
- monitoring.

### Documentación oficial de Elastic Agent y Fleet

Fuente principal para:

- Elastic Agent;
- Fleet Server;
- agent policies;
- integration policies;
- enrolment;
- upgrades;
- diagnostics;
- integrations;
- migración desde Beats.

## Kibana

### Documentación oficial de Kibana

Fuente principal para:

- Data Views;
- Discover;
- KQL;
- ES|QL dentro de Kibana;
- Lens;
- dashboards;
- Maps;
- saved objects;
- Spaces;
- Dev Tools;
- alerting;
- connectors;
- seguridad;
- APIs.

## Esquema de datos

### Elastic Common Schema — documentación oficial

Fuente principal para:

- field sets;
- semántica de campos;
- normalización;
- custom fields;
- compatibilidad;
- versionado;
- integración de fuentes heterogéneas.

## Fedora y Linux

### Fedora Documentation

Uso:

- instalación y administración del sistema;
- systemd;
- servicios;
- seguridad del host;
- networking cuando corresponda.

### systemd manual pages

Uso:

- systemctl;
- journalctl;
- unidades de servicio;
- logs de servicios.

### firewalld documentation

Uso:

- exposición controlada de puertos;
- zonas;
- servicios;
- troubleshooting de conectividad.

### SELinux documentation y Fedora SELinux documentation

Uso:

- enforcing;
- labels;
- políticas;
- diagnóstico de denegaciones;
- integración segura con servicios.

No recomendar desactivar SELinux como procedimiento normal de instalación.

## Logging Linux

### systemd-journald y journalctl — manuales oficiales

Uso:

- journal;
- extracción y seguimiento de eventos;
- integración con la cadena de ingestión.

### Rainer Gerhards / rsyslog — documentación oficial

Uso:

- Syslog;
- forwarding;
- TCP/TLS;
- queues;
- RELP;
- integración previa a Elastic.

### syslog-ng — documentación oficial

Uso:

- sources;
- destinations;
- parsing;
- forwarding;
- TLS;
- buffering;
- integración con pipelines de logging.

## OpenTelemetry

### OpenTelemetry Documentation

Fuente principal para:

- signals;
- OTLP;
- Collector;
- receivers;
- processors;
- exporters;
- context propagation;
- instrumentación;
- integración conceptual con Elastic.

### OpenTelemetry Specification

Uso para detalles normativos del protocolo, modelo de datos y propagación cuando la lección lo requiera.

## Seguridad

Utilizar prioritariamente:

- Elastic security documentation.
- Elastic TLS documentation.
- Elasticsearch privileges and roles documentation.
- API key documentation.
- service account documentation.
- audit logging documentation.
- Fedora security documentation.
- OpenSSL documentation cuando proceda.

Toda configuración de seguridad debe verificarse contra la versión actual estudiada.

## Rendimiento y operaciones

Fuentes prioritarias:

- Elastic performance tuning documentation.
- Elastic sizing guidance.
- Elasticsearch node/cluster/index stats documentation.
- Elasticsearch troubleshooting documentation.
- Elastic JVM and memory guidance.
- Elastic shard sizing guidance.
- Elastic Rally documentation.

Evitar reglas universales de sizing sin workload y medición.

## APIs y automatización

Fuentes:

- Elasticsearch REST API documentation.
- Kibana API documentation.
- Fleet API documentation.
- curl documentation.
- jq manual cuando se utilice para inspeccionar JSON.

## Política bibliográfica por lección

La generación debe elegir las fuentes según el tema.

Orden recomendado:

1. documentación oficial específica del componente;
2. documentación de tecnologías subyacentes;
3. libro principal o complementario para explicación conceptual;
4. documentación Fedora para integración con el host;
5. otras fuentes técnicas solamente cuando aporten valor.

No forzar todas las fuentes en todas las lecciones.

## Política sobre material histórico

Elastic Stack ha cambiado de forma significativa.

Los libros antiguos pueden utilizarse para explicar conceptos estables, pero deben tratarse como material histórico cuando describan:

- mapping types;
- versiones antiguas de cluster discovery;
- antiguas configuraciones de seguridad;
- componentes retirados;
- APIs eliminadas;
- defaults obsoletos;
- arquitectura previa a Elastic Agent/Fleet;
- interfaces antiguas de Kibana.

Nunca convertir una práctica histórica en recomendación actual sin verificarla.

## Referencias bibliográficas específicas

- Elastic — Elastic Documentation.
- Elastic — Elasticsearch Reference.
- Elastic — Kibana Guide.
- Elastic — Logstash Reference.
- Elastic — Beats Documentation.
- Elastic — Fleet and Elastic Agent Guide.
- Elastic — Elastic Common Schema (ECS) Reference.
- Elastic — Elastic Observability Documentation.
- Elastic — Elasticsearch REST API Documentation.
- Apache Software Foundation — Apache Lucene Documentation.
- OpenTelemetry — OpenTelemetry Documentation and Specification.
- Fedora Project — Fedora Documentation.
- systemd — Manual Pages.
- rsyslog — Official Documentation.
- syslog-ng — Official Documentation.
- firewalld — Official Documentation.
- SELinux Project / Fedora — SELinux Documentation.
- Clinton Gormley, Zachary Tong — Elasticsearch: The Definitive Guide.
- Radu Gheorghe, Matthew Lee Hinman, Roy Russo — Elasticsearch in Action.
- Bharvi Dixit — Mastering Elasticsearch.
- Michael McCandless, Erik Hatcher, Otis Gospodnetic — Lucene in Action.
