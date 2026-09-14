# DOMAIN — OPENSEARCH STACK EN PROFUNDIDAD

## Identidad del PATH

Este PATH enseña OpenSearch Stack desde fundamentos hasta nivel experto y de operación en producción.

El dominio principal es:

OpenSearch → documentos → índices → mappings → análisis → shards → replicas → Query DSL → relevancia → agregaciones → ingest pipelines → Data Prepper → OpenTelemetry → OpenSearch Dashboards → PPL/SQL → observabilidad → alerting → Notifications → Anomaly Detection → Security Analytics → seguridad → ISM → snapshots → clustering → HA → rendimiento → troubleshooting → internals → extensibilidad.

El PATH es específico de OpenSearch. No debe tratarse como un curso de Elasticsearch con nombres sustituidos.

## Plataforma de referencia

La plataforma Linux de referencia es Fedora.

Cuando proceda deben utilizarse:
- systemd y systemctl
- journalctl
- RPM
- SELinux
- firewalld
- Podman
- curl
- openssl
- herramientas estándar GNU/Linux

No debe asumirse que una instrucción de Elasticsearch funciona en OpenSearch sin verificar su aplicabilidad conceptual y de versión.

## Nivel

Progresión: cero → principiante → intermedio → avanzado → experto → internals/producción.

Cada entrada numerada de `initial.txt` representa una lección independiente.

No fusionar varias lecciones porque parezcan relacionadas.

## Estructura pedagógica obligatoria

Toda lección debe comenzar con:

# 🎯 OBJETIVO

Después debe desarrollar el tema de forma completa, técnica y didáctica.

Cuando aporten valor, utilizar:

# 🧪 Laboratorio / ejemplos
# ⚠️ Errores frecuentes
# 💡 Idea importante

Toda lección debe terminar con:

# 🧠 QUÉ DEBES RECORDAR

Este apartado debe contener entre 3 y 7 ideas fundamentales y no limitarse a repetir el objetivo.

## Profundidad

No generar resúmenes superficiales.

Explicar:
- qué es
- para qué sirve
- cómo funciona
- dónde encaja arquitectónicamente
- configuración y APIs relevantes
- comportamiento interno cuando ayude a comprenderlo
- implicaciones operacionales
- seguridad
- rendimiento
- diagnóstico
- ejemplos reproducibles

Introducir conceptos previos únicamente cuando sean necesarios para entender la lección, evitando invadir innecesariamente lecciones posteriores.

## Versiones y terminología

OpenSearch evoluciona rápidamente. Priorizar documentación oficial contemporánea y distinguir capacidades dependientes de versión.

Usar terminología propia de OpenSearch, por ejemplo `cluster manager` cuando corresponda, evitando perpetuar terminología histórica si la documentación actual utiliza otra.

Si una característica depende de un plugin, indicarlo.

Si una característica ha cambiado de nombre, interfaz o disponibilidad entre versiones, explicarlo explícitamente.

## OpenSearch

Cubrir profundamente:
- REST APIs
- documentos
- índices
- mappings
- analyzers
- Query DSL
- scoring
- aggregations
- shards y replicas
- routing
- cluster state
- allocation
- recovery
- JVM
- Lucene
- caches
- circuit breakers
- rendimiento

Los ejemplos deben favorecer curl y JSON para hacer visible el protocolo real.

## Data Prepper

Data Prepper es una parte de primer nivel del PATH, no una nota secundaria.

Cubrir:
- pipeline configuration
- sources
- processors
- sinks
- routes
- buffers
- batching
- backpressure
- acknowledgements
- retries
- DLQ
- OpenTelemetry
- operación
- seguridad
- escalado
- troubleshooting

Diferenciar claramente los ingest pipelines ejecutados en OpenSearch de los pipelines externos de Data Prepper.

## OpenSearch Dashboards

Debe aprenderse a utilizar y administrar Dashboards.

Cubrir:
- Discover
- visualizaciones
- dashboards
- data views/index patterns según versión
- Dev Tools
- PPL
- SQL
- Observability
- Alerting
- Anomaly Detection
- Security Analytics
- saved objects
- multi-tenancy
- seguridad
- administración
- troubleshooting

No convertir las lecciones de Dashboards en simples recorridos visuales; explicar qué consultas, índices y APIs existen por debajo cuando sea útil.

## Observabilidad

Mantener separados conceptualmente:
- logs
- metrics
- traces

Explicar correlación entre señales y la relación con OpenTelemetry.

No duplicar un PATH completo de OpenTelemetry: enseñar aquí lo necesario para integrar y operar OpenTelemetry con OpenSearch/Data Prepper.

## Seguridad

La seguridad es transversal.

Cubrir cuando corresponda:
- TLS
- PKI
- autenticación
- autorización
- RBAC
- usuarios
- roles
- role mappings
- DLS
- FLS
- audit logging
- secretos
- mínimo privilegio

No recomendar deshabilitar seguridad como solución general.

## Producción

Distinguir siempre que sea relevante entre:
- laboratorio
- desarrollo
- producción

Las configuraciones cómodas para un laboratorio no deben presentarse como recomendaciones de producción.

## Laboratorios

Los laboratorios deben ser acumulativos siempre que resulte razonable.

Favorecer datasets de logs, métricas y trazas suficientemente realistas.

Los comandos destructivos deben estar claramente identificados.

Incluir comandos para comprobar el resultado, no solamente comandos de configuración.

## Troubleshooting

Enseñar diagnóstico basado en evidencias.

Relacionar:
síntoma → API/registro/métrica → hipótesis → comprobación → causa → corrección → validación.

Favorecer:
- Cluster Health
- Nodes Stats
- Indices Stats
- cat APIs
- allocation explain
- Tasks
- hot threads
- slow logs
- Data Prepper logs/metrics
- journalctl
- curl
- openssl

## Internals

Las lecciones avanzadas deben conectar la abstracción OpenSearch con:
- Lucene
- segments
- inverted indexes
- doc values
- translog
- refresh
- flush
- merge
- cluster state
- routing
- replication
- recovery
- thread pools
- JVM

El objetivo es comprender el comportamiento, no memorizar únicamente APIs.

## Código y configuración

Todo ejemplo debe indicar el contexto cuando pueda resultar ambiguo.

Usar bloques apropiados para:
- shell
- JSON
- YAML
- PPL
- SQL

Los ejemplos deben ser coherentes entre sí y evitar credenciales reales.

## Fuentes

Prioridad:
1. documentación oficial de OpenSearch
2. documentación oficial de Data Prepper
3. documentación oficial de OpenTelemetry cuando exista integración
4. repositorios/código fuente oficiales
5. documentación de Fedora para integración con el sistema
6. bibliografía técnica complementaria

No trasladar automáticamente documentación de Elasticsearch a OpenSearch.

## Objetivo final

Al terminar el PATH, el alumno debe poder diseñar, desplegar, asegurar, administrar, observar, escalar, optimizar y diagnosticar una plataforma OpenSearch Stack de producción y comprender suficientemente sus internals para investigar problemas complejos.
