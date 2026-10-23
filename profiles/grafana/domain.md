# DOMAIN — GRAFANA + LOKI EN PROFUNDIDAD

## 1. Propósito del PATH

Este perfil define un curso técnico, progresivo y profundo de Grafana y Grafana Loki, orientado a pasar desde fundamentos de observabilidad hasta diseño, operación, seguridad, alta disponibilidad, troubleshooting e internals de una plataforma de observabilidad basada en:

- Grafana para visualización, exploración, correlación, administración y alerting.
- Grafana Loki para almacenamiento, indexación por metadatos, consulta y análisis de logs.
- Grafana Alloy para descubrimiento, recolección, procesamiento y envío de logs.
- Prometheus como sistema externo de métricas con el que Grafana y Loki se integran, sin volver a enseñar Prometheus en profundidad dentro de este PATH.
- Fedora Linux como plataforma principal de laboratorios y administración.

El PATH debe enseñar no sólo a utilizar las interfaces, sino a comprender arquitectura, configuración, flujo de datos, almacenamiento, seguridad, límites, rendimiento, fallos y decisiones de diseño.

El objetivo final es que el alumno pueda diseñar, desplegar, operar, automatizar, asegurar y diagnosticar una plataforma Grafana + Loki + Alloy de producción, así como correlacionarla con Prometheus.

## 2. Alcance principal

El curso cubre en profundidad:

1. Fundamentos de observabilidad.
2. Grafana OSS.
3. Arquitectura de Grafana.
4. Instalación y operación en Fedora.
5. Configuración de Grafana.
6. Data sources.
7. Dashboards.
8. Panels y visualizaciones.
9. Queries.
10. Variables y templating.
11. Transformations.
12. Annotations.
13. Links, data links y navegación.
14. Library panels.
15. Explore.
16. Usuarios, equipos, organizaciones, permisos y service accounts.
17. Autenticación y autorización.
18. Seguridad y hardening.
19. Grafana Alerting.
20. Contact points.
21. Notification policies.
22. Silences y mute timings.
23. Alert rules avanzadas.
24. Provisioning.
25. HTTP API.
26. Automatización.
27. Administración.
28. Backup, restore y upgrades.
29. Rendimiento.
30. Troubleshooting.
31. Alta disponibilidad de Grafana.
32. Fundamentos y arquitectura de Loki.
33. Write path y read path.
34. Distributor, Ingester, Querier, Query Frontend, Query Scheduler, Index Gateway, Compactor, Ruler y Ring.
35. Modos de despliegue de Loki.
36. Configuración de Loki.
37. Ingestión de logs.
38. Grafana Alloy.
39. Descubrimiento de fuentes.
40. Pipelines de procesamiento.
41. Labels.
42. Streams.
43. Structured metadata.
44. Parsing.
45. LogQL desde fundamentos hasta consultas avanzadas.
46. Metric queries derivadas de logs.
47. Optimización de LogQL.
48. TSDB.
49. Chunks.
50. Index.
51. Object storage.
52. Schema configuration.
53. Compactor.
54. Retention y eliminación.
55. Loki Ruler y recording rules.
56. Multi-tenancy.
57. Limits y rate limiting.
58. Cardinalidad.
59. Seguridad de Loki.
60. Escalado.
61. Loki monolítico.
62. Simple Scalable Deployment.
63. Distributed/Microservices deployment.
64. Alta disponibilidad.
65. Monitorización interna.
66. Troubleshooting y rendimiento.
67. Integración Grafana + Loki.
68. Correlación logs/métricas.
69. Integración con Prometheus.
70. Observabilidad como código.
71. Git y automatización.
72. Capacity planning.
73. Internals.
74. Proyecto final experto.

## 3. Límites del PATH

### 3.1 Prometheus

Prometheus NO se reenseña en profundidad en este PATH.

Aquí se utiliza para:

- configurarlo como data source de Grafana;
- consumir métricas;
- comprender la relación conceptual PromQL/LogQL;
- enlazar métricas con logs;
- construir dashboards unificados;
- investigar incidentes;
- integrar alerting cuando sea necesario;
- observar Loki, Grafana o Alloy mediante métricas Prometheus.

Pertenecen al PATH específico de Prometheus:

- arquitectura completa de Prometheus;
- exporters en profundidad;
- service discovery en profundidad;
- PromQL completo;
- recording rules de Prometheus;
- alerting rules de Prometheus;
- federation;
- remote write/read en profundidad;
- HA de Prometheus;
- internals del TSDB de Prometheus.

Cuando una lección de Grafana/Loki necesite uno de estos conceptos, se explicará sólo lo imprescindible y se indicará que su estudio profundo pertenece al PATH Prometheus.

### 3.2 OpenTelemetry

OpenTelemetry puede aparecer como integración o contexto, pero este PATH no debe transformarse en un curso completo de OpenTelemetry.

### 3.3 Kubernetes y cloud

Kubernetes, S3, GCS, Azure Blob y servicios cloud pueden utilizarse para explicar despliegue distribuido, object storage y patrones de producción.

Sin embargo:

- Fedora Linux sigue siendo la plataforma base del curso;
- no debe suponerse Kubernetes como requisito para aprender Grafana/Loki;
- los laboratorios iniciales e intermedios deben poder realizarse en Fedora cuando sea razonable;
- Kubernetes y cloud se introducen cuando aportan valor arquitectónico real.

### 3.4 Grafana Enterprise y Grafana Cloud

Grafana OSS es la base del PATH.

Enterprise y Cloud se mencionan cuando:

- una funcionalidad difiere;
- existen capacidades exclusivas;
- es necesario explicar arquitectura, operación o licenciamiento;
- ayudan a distinguir qué puede reproducirse localmente.

No presentar una capacidad Enterprise/Cloud como disponible en Grafana OSS si no lo está.

## 4. Plataforma principal

La plataforma preferente es Fedora Linux.

Las lecciones prácticas deben favorecer, cuando sea aplicable:

- dnf
- rpm
- systemctl
- journalctl
- systemd
- firewalld
- SELinux
- curl
- jq
- tar
- gzip
- shell POSIX o Bash
- herramientas estándar de GNU/Linux

Cuando se instale software:

1. identificar la procedencia del paquete o binario;
2. mostrar cómo localizar archivos instalados;
3. identificar usuario/grupo de servicio;
4. identificar configuración;
5. identificar datos persistentes;
6. identificar logs;
7. explicar la unidad systemd;
8. verificar estado;
9. verificar puertos;
10. considerar firewalld;
11. considerar SELinux;
12. considerar persistencia y backup.

No desactivar SELinux ni firewalld como solución genérica.

## 5. Modelo conceptual de Grafana

Grafana debe enseñarse como una aplicación con varias capas, no sólo como una interfaz de dashboards.

El alumno debe comprender:

- frontend;
- backend;
- grafana-server;
- configuración;
- base de datos interna;
- data proxy;
- plugins;
- data sources;
- dashboards y JSON model;
- Explore;
- alerting;
- provisioning;
- HTTP API;
- autenticación;
- autorización;
- almacenamiento de estado;
- HA.

Debe distinguirse siempre entre:

- datos almacenados por Grafana;
- datos consultados en data sources externos;
- configuración de Grafana;
- recursos provisionados;
- estado operativo;
- secretos.

## 6. Dashboards

El curso debe evitar reducir dashboards a “crear gráficos”.

Debe enseñar:

- intención operacional del dashboard;
- selección correcta de visualización;
- jerarquía de información;
- time range;
- refresh;
- queries;
- variables;
- transformations;
- overrides;
- thresholds;
- mappings;
- annotations;
- links;
- reutilización;
- JSON model;
- UID;
- import/export;
- versionado;
- provisioning;
- rendimiento;
- anti-patterns.

Un dashboard experto debe permitir responder preguntas operacionales concretas.

## 7. Explore

Explore debe enseñarse como herramienta de investigación interactiva y troubleshooting.

Debe quedar clara la diferencia entre:

- dashboard: observación repetible y preparada;
- Explore: investigación dinámica;
- alerting: evaluación automática de condiciones.

Los laboratorios deben utilizar Explore para pasar de síntomas a evidencia.

## 8. Grafana Alerting

Debe cubrirse la arquitectura contemporánea de Grafana Alerting:

- alert rules;
- rule groups;
- evaluation;
- labels;
- annotations;
- alert instances;
- estados;
- No Data;
- Error;
- Pending;
- contact points;
- notification policies;
- grouping;
- routing;
- silences;
- mute timings;
- templates;
- provisioning;
- HA;
- troubleshooting.

Distinguir cuando corresponda:

- Grafana-managed alert rules;
- data source-managed rules;
- Loki Ruler;
- Alertmanager externo.

No confundir Grafana Alerting con Prometheus Alertmanager.

## 9. Modelo conceptual de Loki

Loki debe enseñarse como sistema distribuido de logs diseñado alrededor de streams y metadatos indexados.

Conceptos obligatorios:

- log entry;
- timestamp;
- labels;
- label set;
- stream;
- structured metadata;
- chunks;
- index;
- TSDB;
- object storage;
- ingestion;
- querying;
- tenants;
- limits;
- retention;
- LogQL.

Debe remarcarse que Loki no debe tratarse como un motor de indexación full-text tradicional.

## 10. Labels, streams y cardinalidad

Este es un eje crítico del curso.

Toda lección relevante debe reforzar la relación:

label set → stream → cardinalidad → coste operacional

El alumno debe aprender a distinguir:

### Buenos candidatos a labels

Valores con cardinalidad acotada y utilidad para seleccionar streams, por ejemplo:

- service
- application
- environment
- host
- instance
- level cuando esté justificado

### Malos candidatos a labels

Valores potencialmente únicos o de cardinalidad elevada, por ejemplo:

- request_id
- trace_id
- session_id
- UUID
- timestamp
- user_id sin control de dominio

Estos valores suelen ser mejores candidatos para structured metadata o para permanecer dentro del contenido del log, según el caso.

No convertir esta regla en dogma: explicar siempre el impacto y el caso de uso.

## 11. Grafana Alloy

Grafana Alloy es el collector preferente del PATH para nuevos laboratorios.

Debe enseñarse:

- arquitectura por componentes;
- configuración;
- descubrimiento;
- fuentes Loki;
- loki.process;
- loki.relabel cuando corresponda;
- loki.write;
- journald;
- archivos;
- syslog;
- containers;
- pipelines;
- labels;
- structured metadata;
- debugging;
- métricas internas.

Promtail se estudia principalmente como:

- tecnología histórica;
- entorno existente;
- fuente de configuraciones a migrar;
- contexto necesario para comprender documentación antigua.

No diseñar nuevos laboratorios alrededor de Promtail salvo que la lección trate expresamente de compatibilidad o migración.

## 12. LogQL

LogQL debe progresar desde selección básica hasta razonamiento de rendimiento.

La enseñanza debe incluir:

1. stream selectors;
2. matchers;
3. line filters;
4. parsers;
5. pipeline expressions;
6. extracted fields;
7. label filters;
8. line_format y label_format;
9. unwrap;
10. range aggregations;
11. vector aggregations;
12. metric queries;
13. operadores;
14. templates cuando corresponda;
15. optimización.

Los ejemplos deben partir de logs realistas y producir resultados verificables.

Debe distinguirse siempre entre:

- filtrar streams mediante labels;
- filtrar líneas;
- parsear contenido;
- convertir logs en series métricas.

## 13. Arquitectura de Loki

El alumno debe comprender write path y read path.

Componentes que deben explicarse cuando correspondan:

- Distributor
- Ingester
- Querier
- Query Frontend
- Query Scheduler
- Index Gateway
- Compactor
- Ruler
- Gateway
- Ring
- caches
- object storage

No presentar todos los componentes como procesos separados en todos los modos de despliegue.

Explicar que el mismo binario puede ejecutar distintos targets/componentes según el modo.

## 14. Modos de despliegue de Loki

Deben distinguirse claramente:

### Monolithic / single binary

Adecuado para aprendizaje, desarrollo y cargas pequeñas cuando sus límites sean aceptables.

### Simple Scalable Deployment — compatibilidad y migración

Separación funcional en read, write y backend. Este modo está deprecado y su retirada está anunciada para Loki 4.0. Estudiarlo para operar instalaciones existentes y preparar su migración a microservices o monolítico HA; no presentarlo como destino preferente de nuevos diseños. Verificar siempre la guía de la versión elegida.

### Distributed / Microservices

Componentes desplegados y escalados de forma independiente para escenarios de mayor escala y complejidad.

Para cada modo explicar:

- propósito;
- topología;
- persistencia;
- requisitos;
- ventajas;
- limitaciones;
- escalado;
- fallos;
- cuándo elegirlo;
- cómo migrar conceptualmente.

## 15. Almacenamiento de Loki

Para instalaciones modernas, TSDB debe ser la referencia principal.

Debe explicarse:

- schema_config;
- store: tsdb;
- object_store;
- index;
- chunks;
- tsdb_shipper;
- active index;
- cache;
- object storage;
- schema periods;
- cambios de schema;
- compatibilidad.

BoltDB Shipper y backends legacy sólo deben estudiarse para comprender instalaciones existentes, migración o historia técnica.

No recomendar Table Manager para instalaciones nuevas.

## 16. Retention y Compactor

La retención moderna debe enseñarse alrededor del Compactor.

Conceptos:

- compaction;
- retention_enabled;
- retention period;
- delete request store;
- retention delete delay;
- sweeper;
- marker files;
- políticas por tenant/stream cuando correspondan;
- interacción con object storage lifecycle;
- eliminación solicitada;
- persistencia operacional del Compactor.

Debe distinguirse entre:

- retención de Loki;
- delete requests;
- lifecycle del object store.

No presentar reglas de lifecycle del bucket como sustituto directo y ciego del modelo de retención de Loki.

## 17. Multi-tenancy

Debe comprenderse:

- tenant;
- X-Scope-OrgID;
- aislamiento lógico;
- autenticación externa;
- autorización;
- gateway;
- límites por tenant;
- retención por tenant;
- riesgos de seguridad.

No asumir que Loki proporciona por sí solo una solución completa de autenticación de usuarios finales.

## 18. Seguridad

El curso debe aplicar seguridad desde la arquitectura.

Grafana:

- cuentas administrativas;
- autenticación;
- autorización;
- RBAC donde corresponda;
- service accounts;
- tokens;
- TLS;
- secrets;
- cookies;
- reverse proxy;
- plugins;
- filesystem;
- base de datos;
- mínimo privilegio.

Loki:

- exposición de API;
- autenticación externa;
- multi-tenancy;
- TLS;
- gateway;
- secrets;
- object storage;
- separación de red;
- límites.

Alloy:

- permisos sobre logs;
- journald;
- secretos;
- endpoints;
- TLS;
- privilegios mínimos.

Fedora:

- systemd hardening;
- firewalld;
- SELinux;
- ownership;
- permissions.

## 19. Provisioning y observabilidad como código

La GUI debe utilizarse para aprender y explorar, pero el alumno debe avanzar hacia configuración reproducible.

Debe cubrir:

- provisioning de data sources;
- provisioning de dashboards;
- provisioning de alerting;
- JSON de dashboards;
- YAML;
- Loki configuration;
- Alloy configuration;
- HTTP API;
- Git;
- revisión de cambios;
- CI/CD conceptual/práctico cuando corresponda;
- rollback;
- secretos fuera del repositorio.

No enseñar “copiar a mano en la GUI” como estrategia de producción.

## 20. Correlación logs/métricas

La integración con Prometheus debe seguir el flujo:

síntoma métrico → contexto → navegación → logs → LogQL → causa probable → verificación

Conceptos importantes:

- labels compartidos;
- service;
- instance;
- host;
- environment;
- time range;
- data links;
- dashboard links;
- Explore;
- derived fields;
- variables compartidas.

El curso debe enseñar que correlación no significa que logs y métricas sean el mismo modelo de datos.

## 21. Rendimiento

Grafana:

- número de panels;
- frecuencia de refresh;
- variables;
- queries;
- transformations;
- data source latency;
- backend;
- database;
- caching donde corresponda.

Loki:

- ingestion rate;
- número de streams;
- cardinalidad;
- chunk behavior;
- TSDB;
- object storage;
- query selectivity;
- parsers;
- regex;
- query splitting;
- parallelism;
- caches;
- limits.

Toda optimización debe partir de medición y explicación causal.

## 22. Capacity planning

Debe enseñar a razonar, no sólo a copiar tamaños.

Variables:

- bytes de logs por segundo;
- eventos por segundo;
- número de streams;
- cardinalidad;
- compresión;
- retention;
- crecimiento;
- object storage;
- CPU;
- RAM;
- red;
- query concurrency;
- usuarios;
- tenants;
- HA;
- margen operacional.

Cuando no exista una fórmula universal, explicarlo y enseñar cómo medir.

## 23. Troubleshooting

Metodología preferida:

1. definir síntoma;
2. delimitar componente;
3. comprobar proceso/servicio;
4. comprobar configuración efectiva;
5. comprobar red y DNS;
6. comprobar TLS;
7. comprobar permisos;
8. comprobar SELinux;
9. comprobar ingestión;
10. comprobar labels/streams;
11. comprobar almacenamiento;
12. comprobar query path;
13. comprobar límites;
14. comprobar recursos;
15. comprobar métricas y logs internos;
16. reproducir;
17. formular hipótesis;
18. validar;
19. corregir;
20. verificar.

Los laboratorios deben provocar fallos controlados y demostrar el diagnóstico.

## 24. Internals

Las secciones internas deben conectar el comportamiento observado con la implementación.

Grafana:

- repositorio;
- backend;
- frontend;
- servicios;
- API;
- data proxy;
- provisioning;
- alerting;
- persistencia;
- request lifecycle.

Loki:

- módulos;
- targets;
- ring;
- hashing;
- distributor;
- ingester;
- WAL;
- chunk lifecycle;
- TSDB;
- query engine;
- LogQL parser;
- query frontend;
- scheduler;
- compactor;
- ruler.

No convertir internals en una lectura lineal del código fuente. Elegir recorridos que expliquen comportamientos concretos.

## 25. Política de versiones

Grafana, Loki y Alloy evolucionan con rapidez.

Por ello:

- priorizar documentación oficial de la versión estable actual;
- indicar versión cuando una opción, interfaz o comportamiento dependa de ella;
- no fijar números de versión en explicaciones permanentes salvo necesidad;
- distinguir funcionalidad estable, experimental, deprecated y eliminada;
- comprobar documentación actual antes de afirmar defaults o soporte exacto;
- no asumir que una captura o tutorial antiguo representa la UI actual.

## 26. Política de documentación

Orden de autoridad recomendado:

1. documentación oficial del proyecto relevante;
2. referencia de configuración/API oficial;
3. release notes y upgrade guides oficiales;
4. documentación de Fedora para integración del sistema;
5. documentación de Prometheus sólo para los puntos de integración;
6. libros técnicos;
7. artículos externos únicamente como apoyo.

Para detalles de configuración cambiantes, la documentación oficial prevalece sobre libros y tutoriales.

## 27. Laboratorios

Los laboratorios deben ser acumulativos y verificables.

Preferir:

- comandos reales;
- configuraciones pequeñas;
- logs reales;
- consultas reproducibles;
- fallos deliberados;
- observaciones concretas;
- validación antes/después.

Un laboratorio debe indicar qué observar y qué conclusión técnica extraer.

No exigir un proyecto nuevo para cada lección.

## 28. Artefactos

Cuando una lección lo justifique pueden generarse:

- grafana.ini;
- provisioning YAML;
- dashboard JSON;
- Loki YAML;
- Alloy configuration;
- systemd drop-ins;
- scripts Bash;
- curl requests;
- jq filters;
- ejemplos LogQL;
- alert rules;
- runbooks;
- diagramas textuales;
- repositorios de ejemplo.

Los artefactos deben extender proyectos anteriores cuando exista continuidad lógica.

## 29. Proyecto final

El proyecto final debe integrar, como mínimo:

- Fedora;
- Grafana;
- Loki;
- Grafana Alloy;
- journald y/o logs de servicios;
- diseño de labels;
- structured metadata;
- LogQL;
- TSDB;
- object storage o equivalente reproducible;
- Compactor;
- retention;
- dashboards;
- variables;
- transformations;
- annotations;
- navegación;
- Grafana Alerting;
- provisioning;
- seguridad;
- Git;
- backup/restore;
- generación de fallos;
- troubleshooting;
- capacity planning;
- integración con un Prometheus ya existente o desplegado como dependencia del laboratorio.

Debe culminar en un flujo de incidente:

métrica anómala → dashboard → Explore → logs → consulta LogQL → causa raíz → corrección → verificación → documentación/runbook.

## 30. Reglas pedagógicas específicas

1. No producir resúmenes superficiales.
2. No explicar sólo botones de interfaz.
3. No convertir cada lección en una lista de opciones.
4. Explicar causa, efecto, límites y trade-offs.
5. Usar terminología oficial.
6. Mantener nombres técnicos originales cuando su traducción genere ambigüedad.
7. Explicar comandos y configuración antes de pedir memorizarlos.
8. No inventar defaults.
9. No inventar métricas.
10. No inventar claves YAML.
11. No inventar endpoints de API.
12. No inventar referencias bibliográficas.
13. Mostrar diferencias de versión cuando sean relevantes.
14. Separar claramente Grafana OSS, Enterprise y Cloud cuando aplique.
15. Separar claramente Grafana Alerting, Loki Ruler y Alertmanager.
16. Separar claramente labels y structured metadata.
17. Tratar cardinalidad como concepto transversal.
18. Relacionar arquitectura con troubleshooting.
19. Relacionar almacenamiento con retención y coste.
20. Relacionar provisioning con reproducibilidad.
21. Mantener Prometheus como integración, no como segundo curso dentro del PATH.

## 31. Resultado esperado

Al finalizar el PATH, el alumno debe poder:

- administrar Grafana en Fedora;
- diseñar dashboards útiles y mantenibles;
- configurar y administrar data sources;
- dominar variables, transformations y Explore;
- configurar Grafana Alerting;
- automatizar Grafana mediante provisioning y API;
- desplegar y administrar Loki;
- diseñar correctamente labels y streams;
- utilizar structured metadata;
- escribir y optimizar LogQL;
- operar TSDB/object storage;
- configurar Compactor y retention;
- comprender Loki Ruler;
- operar multi-tenancy y limits;
- diagnosticar cardinalidad;
- comprender modos de despliegue y HA;
- recolectar logs con Grafana Alloy;
- correlacionar logs y métricas;
- asegurar la plataforma;
- hacer capacity planning;
- diagnosticar fallos extremo a extremo;
- leer internals con un objetivo operacional;
- diseñar una plataforma de observabilidad reproducible y mantenible.


## 32. Ampliación experta — criterios obligatorios de profundidad

Los bloques 111–121 amplían el temario sin sustituir ni renumerar los bloques 0–110. El bloque 110 conserva su condición de proyecto integrador original; el bloque 121 aporta una evaluación adicional de incidentes.

Para cada procedimiento técnico relevante, enseñar: propósito, arquitectura, prerequisitos, instalación o configuración, significado de opciones, rutas y permisos, comandos de validación, resultado esperado, logs y métricas de diagnóstico, fallos deliberados, seguridad, rendimiento, compatibilidad de versiones y procedimiento de recuperación. No exigir un laboratorio artificial en cada lección conceptual; sí laboratorios verificables en operaciones significativas.

### 32.1 Fedora y despliegue

Grafana, Loki y Alloy deben tener prácticas nativas en Fedora con systemd, journalctl, firewalld, SELinux, gestión de secretos, verificación de procedencia de paquetes/binarios y comprobación de puertos. No asumir que Loki o Alloy dispongan de un RPM oficial para una versión concreta: comprobar métodos de distribución disponibles antes de documentarlos. Mantener SELinux activo.

### 32.2 Ingestión fiable y datos sensibles

Enseñar la diferencia entre un origen que no genera logs, un collector que no los lee, una transmisión fallida, un rechazo por límites y una consulta incorrecta. Medir pérdidas, duplicados, latencia y reintentos cuando las capacidades de la versión lo permitan. Evitar indexar identificadores de alta cardinalidad y redactar datos sensibles antes de su persistencia.

### 32.3 Automatización y pruebas

Añadir Terraform Provider de Grafana, Ansible y GitOps como aplicación al stack, sin reenseñar los PATH completos de esas herramientas. Validar configuración y esquema, mantener secretos fuera de Git, ensayar drift, upgrades y rollback; verificar qué recursos son compatibles con cada proveedor/versión.

### 32.4 Resiliencia

Explicar RPO/RTO, WAL, backups de configuración, almacenamiento de objetos, retención, restauración, degradación parcial, alta disponibilidad y pruebas de desastre. Distinguir expresamente entre persistencia de logs y backup de la base de datos interna de Grafana.

### 32.5 Criterios de aceptación

Cada laboratorio operacional debe definir estado inicial, pasos reproducibles, comandos o consultas de verificación, evidencia observable, fallo o variación cuando proceda, limpieza y criterios de éxito. En benchmarks registrar dataset, hardware, versiones, configuración, carga, métricas y límites de validez de las conclusiones.

### 32.6 Límites y versiones

Distinguir siempre Grafana OSS, Enterprise y Cloud. Confirmar disponibilidad real de OIDC, RBAC, APIs, inhibición de alertas, componentes Alloy y opciones de Loki en la versión estudiada. No inventar defaults, rutas, nombres de métricas ni garantías de entrega.


## 33. Recorrido pedagógico y prerrequisitos operacionales

Los identificadores de bloques y lecciones son estables. El orden numérico conserva compatibilidad con el temario anterior; el recorrido recomendado que sigue define las dependencias pedagógicas. Si el generador sólo procesa orden numérico, realizar primero las prácticas indicadas como prerrequisito o generar los bloques seleccionados por separado. No afirmar que un campo YAML personalizado reordena el generador sin comprobar su implementación.

Recorrido completo: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22 → 23 → 24 → 25 → 26 → 27 → 28 → 29 → 30 → 31 → 32 → 33 → 34 → 35 → 36 → 37 → 38 → 39 → 111 → 40 → 41 → 112 → 113 → 42 → 43 → 44 → 45 → 46 → 47 → 48 → 49 → 50 → 51 → 52 → 53 → 54 → 55 → 56 → 57 → 58 → 59 → 60 → 61 → 62 → 63 → 64 → 65 → 66 → 67 → 68 → 69 → 70 → 71 → 72 → 73 → 74 → 75 → 76 → 77 → 78 → 79 → 80 → 81 → 82 → 83 → 84 → 85 → 86 → 87 → 88 → 89 → 90 → 91 → 92 → 93 → 94 → 95 → 96 → 97 → 114 → 115 → 98 → 99 → 100 → 101 → 102 → 116 → 119 → 103 → 104 → 105 → 106 → 117 → 118 → 120 → 107 → 108 → 109 → 110 → 121.

- Antes del laboratorio de configuración de Loki (39), preparar los archivos mínimos; ejecutarlo después de completar la instalación 111. En 35–38 los recorridos son conceptuales o utilizan una instancia preparada y documentada.
- El bloque 111 proporciona la primera instalación de Loki; 77 analiza después los límites, HA y decisiones del modo monolítico.
- El bloque 40 presenta fuentes y requisitos. La configuración de Alloy del bloque 41 se prepara como texto; su ejecución se realiza tras 112. Los bloques 112 y 113 preceden a los laboratorios 42–58.
- El entorno persistente de laboratorio empieza con Loki monolítico, Alloy y logs de prueba; indicar versión, rutas, puertos, dataset y limpieza. No exigir object storage para la primera prueba local.
- Para los bloques 6–34 utilizar TestData o fuentes preparadas cuando permitan demostrar el objetivo. Todo laboratorio que requiera Loki/Prometheus debe identificar esa dependencia y ofrecer su preparación o remitir al bloque correspondiente.
- Los bloques 114–120 se completan antes del proyecto 110; 121 evalúa el diagnóstico después de integrar la plataforma.
- El recorrido es una guía de estudio; no es una garantía de soporte de selección u ordenación en course-generator.

## 34. Profundización progresiva y prevención de repeticiones

Cada segunda pasada debe utilizar un escenario y producir evidencia nuevos:

| Bloques | Primera pasada | Profundización posterior |
|---|---|---|
| 2, 107 | Arquitectura y ciclo de consulta | Recorrido de código ligado a un fallo concreto |
| 7–15, 114 | Manejo de paneles, variables y Explore | Accesibilidad, calidad de datos, regresión y coste medido |
| 19–23, 115 | Evaluación y entrega de alertas | Ausencia de series, fallos de entrega y HA comprobada |
| 24–29, 98–101, 116 | Provisioning y API por recurso | Repositorio integrado, drift y reconstrucción automatizada |
| 36–37, 108 | Write/read path y componentes | Evidencia operacional conectada con implementación |
| 44–46, 74, 118 | Labels, streams y metadata | Incidente de cardinalidad y benchmark reproducible |
| 55, 88 | Metric queries desde logs | Dashboard y recording rule con comparación de coste |
| 89–95 | Navegación y correlación | Investigación progresiva de un mismo incidente |
| 31, 117, 120 | Backup y restore básico | Desastre, upgrade y límites de reversibilidad |

No repetir listas de definiciones para justificar otro bloque. Enunciar al inicio los conocimientos previos, el problema nuevo y el resultado verificable.

## 35. Actualización de API, agentes y despliegue

Estado contrastado el 21 de octubre de 2026; fijar versiones concretas al ejecutar los laboratorios.

- Grafana: enseñar la familia vigente /apis y sus recursos/versiones junto con la compatibilidad legacy /api. La deprecación de /api comienza en Grafana 13; no significa que todas sus rutas estén deshabilitadas ni que exista sustitución exacta para cada recurso. Comprobar autenticación, permisos, namespaces y payloads por endpoint.
- Promtail: alcanzó EOL el 2 de marzo de 2026. Usarlo sólo para inventario, lectura de configuraciones antiguas y migración a Alloy. No instalarlo como collector nuevo.
- Loki SSD: modo deprecado con retirada anunciada en Loki 4.0. Los ejemplos de read/write/backend son de compatibilidad; preparar migración a microservices o monolítico HA según requisitos.
- Mantener la referencia de dashboard JSON tradicional cuando sea necesaria y distinguir el esquema de recursos de APIs nuevas. No asumir equivalencia entre formatos.

## 36. LogQL: criterios de dominio verificable

Además de la sintaxis, enseñar __error__ y su filtrado en la posición adecuada, conversiones tras unwrap, valores ausentes, absent_over_time, offset y ventanas temporales. Practicar on/ignoring, group_left/group_right y bool donde el lenguaje y la versión lo permitan. Toda operación entre vectores debe razonar sobre labels y cardinalidad de salida.

Mantener un dataset pequeño con timestamps controlados y consultas cuyo resultado pueda calcularse manualmente. Incluir errores de parsing, valores no convertibles, series que desaparecen y logs presentes pero fuera de la ventana consultada. Distinguir ausencia, cero y consulta fallida.

## 37. Validación del perfil y límites del generador

El bloque quality expresa requisitos pedagógicos de auditoría; validation.enabled permanece desactivado porque no se han definido comandos externos de validación. Son mecanismos distintos y no deben presentarse como equivalentes.

Antes de usar el perfil con course-generator, comprobar en su esquema/código qué claves acepta, cuáles aplica y qué sucede con claves desconocidas. No dar por hecho que depth_policy, lab_quality, technology_policy u output implementan controles efectivos por existir en YAML. Este paquete valida sintaxis y coherencia documental; no certifica integración con el ejecutable ni ejecuta laboratorios reales.

Los archivos se entregan con nombres canónicos initial.txt, domain.md, bibliography.md y profile.yaml. La ruta ../../config/pedagogy.md depende del repositorio del usuario y debe existir en su ubicación de destino; no se incluye ni se sustituye silenciosamente.
