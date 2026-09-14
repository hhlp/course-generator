# ELASTIC STACK EN PROFUNDIDAD — FEDORA

## 1. Identidad del dominio

Este PATH enseña Elastic Stack desde fundamentos hasta operación experta e internals, usando Fedora como plataforma Linux principal.

El dominio cubre de forma integrada:

- Elasticsearch.
- Apache Lucene en el nivel necesario para comprender los internals de Elasticsearch.
- índices, documentos, mappings, analyzers, aliases, templates y data streams.
- Query DSL, aggregations, KQL, Lucene query syntax y ES|QL.
- shards, replicas, routing, nodos, cluster state, discovery, coordinación y recuperación.
- ingest pipelines y processors.
- Logstash.
- Beats.
- Elastic Agent, Fleet y integrations.
- Elastic Common Schema (ECS).
- Kibana, Discover, Lens, Maps, dashboards y saved objects.
- alerting, rules, connectors y actions.
- TLS, autenticación, autorización, RBAC, API keys, service accounts y hardening.
- ILM, data tiers, rollover, retención, snapshots y SLM.
- CCS, CCR y arquitecturas multi-cluster.
- rendimiento, JVM, memoria, almacenamiento y capacity planning.
- monitorización y troubleshooting del propio Elastic Stack.
- integración con journald, rsyslog, syslog-ng y aplicaciones.
- logs, métricas, traces, Elastic APM y OpenTelemetry.
- APIs, automatización, upgrades y migraciones.
- internals de Lucene, Elasticsearch, Logstash, Beats, Elastic Agent, Fleet y Kibana.
- diseño, despliegue, seguridad, operación y diagnóstico de una plataforma de producción.

## 2. Objetivo pedagógico

El alumno debe progresar desde no asumir conocimientos previos de Elastic Stack hasta ser capaz de diseñar, desplegar, asegurar, automatizar, mantener, escalar y diagnosticar una plataforma Elastic Stack real.

El curso NO debe convertirse en una colección de comandos ni en una referencia superficial de opciones. Cada lección debe explicar:

1. qué problema resuelve el concepto;
2. cómo encaja en la arquitectura;
3. cómo funciona;
4. cómo se configura o utiliza;
5. cómo observar su comportamiento;
6. cómo validarlo;
7. qué puede fallar;
8. cómo diagnosticarlo;
9. qué implicaciones tiene en producción.

## 3. Plataforma

Plataforma principal: Fedora Linux.

Cuando corresponda, utilizar herramientas y convenciones reales de Fedora:

- RPM.
- systemd.
- systemctl.
- journalctl.
- firewalld.
- SELinux.
- curl.
- OpenSSL y herramientas PKI cuando proceda.
- utilidades GNU/Linux habituales.

No convertir el PATH en un curso general de Fedora. Explicar estos componentes solamente con la profundidad necesaria para operar Elastic Stack y enlazar conceptualmente con los PATH especializados correspondientes.

## 4. Política de versiones

Elastic Stack evoluciona con rapidez. No asumir que una opción, API, componente, licencia, interfaz de Kibana o procedimiento histórico continúa vigente.

Para contenido dependiente de versión:

- tomar como referencia la versión estable actual cubierta por la documentación oficial consultada durante la generación;
- indicar la versión cuando afecte al comportamiento explicado;
- comprobar nombres de APIs, parámetros, defaults, roles de nodo, mecanismos de seguridad, ILM, Fleet, Elastic Agent, integrations y funcionalidades de Kibana;
- diferenciar claramente funcionalidad vigente, heredada, deprecada y eliminada;
- evitar presentar prácticas antiguas de ELK como arquitectura recomendada actual;
- no inventar compatibilidad entre versiones.

Si existe conflicto entre un libro antiguo y la documentación oficial vigente, prevalece la documentación oficial para comportamiento actual.

## 5. Fuentes de autoridad

Orden de prioridad:

1. documentación oficial de Elastic correspondiente a la versión estudiada;
2. documentación oficial de Elasticsearch, Kibana, Logstash, Beats, Elastic Agent, Fleet, ECS y Elastic APM;
3. documentación oficial de Apache Lucene para internals relevantes;
4. documentación oficial de Fedora para integración con el sistema operativo;
5. documentación oficial de OpenTelemetry para OTLP, Collector e instrumentación;
6. libros técnicos seleccionados en bibliografy.md;
7. fuentes adicionales únicamente cuando aporten contexto y puedan contrastarse.

No usar blogs, respuestas de foros o fragmentos sin contexto como autoridad principal para comportamiento técnico.

## 6. Alcance de Elasticsearch

Explicar Elasticsearch desde tres perspectivas complementarias:

- interfaz: REST APIs, documentos, índices, mappings, búsquedas y administración;
- sistema distribuido: shards, replicas, routing, nodos, cluster state, coordinación, recovery y HA;
- internals: Lucene, segments, translog, refresh, flush, merge, checkpoints, escritura y búsqueda distribuida.

Relacionar siempre las abstracciones visibles con sus consecuencias operacionales.

## 7. Lucene

Lucene se estudia para comprender Elasticsearch, no para convertir el PATH en un curso independiente de programación con Lucene.

Cubrir con profundidad conceptual:

- inverted index;
- terms y term dictionary;
- postings;
- segments;
- stored fields;
- doc values;
- norms;
- points;
- FST cuando sea relevante;
- scoring y BM25;
- merges;
- deleted documents;
- relación entre refresh, segments y visibilidad de documentos.

Conectar cada estructura con fenómenos observables en Elasticsearch.

## 8. Ingestión

Comparar y relacionar:

- ingest pipelines de Elasticsearch;
- Logstash;
- Beats;
- Elastic Agent;
- Fleet;
- integrations;
- productores Syslog;
- journald;
- aplicaciones;
- OpenTelemetry cuando corresponda.

No enseñar que todos los componentes deben utilizarse simultáneamente. Explicar criterios de selección, complejidad, procesamiento, buffering, fiabilidad, administración y coste operacional.

## 9. Logstash

Tratar Logstash como un motor de procesamiento de eventos completo.

Cubrir:

- pipeline input → filter → output;
- plugins y codecs;
- Grok y Dissect;
- transformación y enriquecimiento;
- conditionals;
- múltiples pipelines;
- persistent queues;
- dead letter queues;
- back pressure;
- delivery semantics;
- monitorización;
- tuning;
- troubleshooting.

Diferenciar con claridad qué procesamiento puede realizarse en Elasticsearch ingest pipelines y cuándo Logstash aporta valor.

## 10. Beats, Elastic Agent y Fleet

Explicar tanto el modelo histórico de Beats como la dirección moderna basada en Elastic Agent/Fleet.

No asumir que Beats y Elastic Agent son equivalentes. Comparar:

- arquitectura;
- configuración;
- administración;
- integrations;
- despliegue;
- upgrades;
- seguridad;
- observabilidad;
- migración.

Cuando una funcionalidad haya cambiado de estado en versiones recientes, verificarla en documentación oficial.

## 11. ECS

Elastic Common Schema debe funcionar como hilo transversal del PATH.

No limitar ECS a memorizar nombres de campos. Enseñar:

- normalización;
- field sets;
- semántica;
- compatibilidad;
- extensiones;
- custom fields;
- mappings;
- correlación entre fuentes;
- consecuencias de un esquema incoherente.

Los laboratorios de logging deben intentar producir eventos coherentes con ECS cuando sea apropiado.

## 12. Kibana

Kibana no debe tratarse solamente como una GUI.

Cubrir:

- Data Views;
- Discover;
- KQL;
- ES|QL;
- visualizaciones;
- Lens;
- Maps;
- dashboards;
- saved objects;
- Spaces;
- Dev Tools;
- APIs;
- seguridad;
- alerting;
- administración y troubleshooting.

Los dashboards deben construirse a partir de preguntas operacionales concretas, no por decoración.

## 13. Seguridad

La seguridad es transversal y no debe aparecer únicamente en el bloque específico.

Aplicar cuando corresponda:

- TLS en HTTP y transporte;
- CA y certificados;
- autenticación;
- roles y privilegios;
- RBAC;
- API keys;
- service accounts;
- secrets/keystores;
- mínimo privilegio;
- protección de Kibana;
- protección de APIs;
- auditoría;
- firewalld;
- SELinux.

No recomendar desactivar TLS, autenticación, SELinux o firewall como solución permanente a problemas de configuración.

## 14. Ciclo de vida y almacenamiento

Explicar conjuntamente las relaciones entre:

- data streams;
- rollover;
- ILM;
- data tiers;
- hot/warm/cold/frozen;
- searchable snapshots cuando correspondan;
- retención;
- SLM;
- snapshots;
- restore;
- capacity planning.

Diferenciar lifecycle de backup: ILM o retención NO sustituyen snapshots.

## 15. Alta disponibilidad

Evitar afirmaciones simplistas como «tener replicas significa tener backup».

Enseñar:

- fault domains;
- master-eligible nodes;
- quorum y coordinación;
- replicas;
- allocation awareness;
- recovery;
- snapshots;
- CCR cuando sea apropiado;
- pruebas reales de fallo.

## 16. Rendimiento

No ofrecer valores mágicos universales.

Relacionar tuning con medición:

- workload;
- tamaño y cantidad de shards;
- heap;
- filesystem cache;
- CPU;
- almacenamiento;
- IOPS;
- red;
- refresh;
- bulk;
- merges;
- thread pools;
- queues;
- circuit breakers;
- caches;
- retención.

Toda recomendación de rendimiento debe explicar el trade-off.

## 17. Troubleshooting

Usar una metodología basada en evidencia:

1. definir el síntoma;
2. determinar alcance;
3. comprobar salud del cluster;
4. observar nodos, índices y shards;
5. revisar métricas;
6. revisar logs;
7. consultar APIs diagnósticas;
8. formular hipótesis;
9. probar la hipótesis;
10. aplicar la corrección;
11. validar recuperación;
12. documentar causa raíz.

Priorizar herramientas como:

- cluster health;
- cat APIs;
- Cluster Allocation Explain;
- Nodes/Cluster/Index Stats;
- Tasks API;
- pending tasks;
- hot threads;
- slow logs;
- Profile API;
- Explain API;
- métricas de Logstash;
- diagnósticos de Elastic Agent/Fleet;
- journalctl.

## 18. Integración con logging Linux

Este PATH debe enlazar naturalmente con el PATH de Logging en Linux.

Explicar las fronteras entre:

- generación del evento;
- journald;
- Syslog;
- rsyslog/syslog-ng;
- transporte;
- buffering;
- agente;
- procesamiento;
- normalización;
- indexación;
- retención;
- búsqueda;
- visualización;
- alerting.

No duplicar innecesariamente un curso completo de rsyslog o syslog-ng.

## 19. Observabilidad y OpenTelemetry

Elastic Stack debe situarse dentro de una arquitectura moderna de observabilidad.

Cubrir conceptualmente:

- logs;
- metrics;
- traces;
- context propagation;
- trace IDs;
- Elastic APM;
- OpenTelemetry;
- OTLP;
- Collector;
- correlación de señales.

Cuando el PATH de OpenTelemetry cubra un tema con mayor profundidad, mantener aquí el foco en la integración con Elastic.

## 20. Internals

Las lecciones de internals deben conectar implementación con operación.

Ejemplos:

- segment → refresh y búsqueda;
- merge → I/O y rendimiento;
- translog → durabilidad y recovery;
- routing → ubicación de documentos;
- query/fetch phases → coste de búsquedas distribuidas;
- cluster state → escalabilidad del plano de control;
- queues → back pressure.

Evitar internals puramente ornamentales sin consecuencia práctica.

## 21. Laboratorios

Los laboratorios deben ser reproducibles y acumulativos.

Preferir:

- comandos reales;
- configuración mínima pero funcional;
- datos de ejemplo verificables;
- inspección antes y después;
- fallos deliberados seguros;
- diagnóstico;
- limpieza o rollback.

Cuando una operación pueda destruir datos, advertirlo explícitamente y trabajar con recursos de laboratorio.

No exigir servicios cloud de pago para completar los objetivos fundamentales del PATH.

## 22. Comandos y ejemplos

Todo comando debe:

- ser sintácticamente coherente;
- indicar contexto cuando no sea obvio;
- evitar placeholders ambiguos;
- explicar las opciones importantes;
- mostrar cómo validar el resultado.

Para REST APIs, preferir ejemplos legibles con curl o Kibana Dev Tools según el objetivo.

No inventar respuestas exactas del cluster. Cuando la salida varíe, mostrar solamente campos relevantes o una salida representativa claramente identificada.

## 23. Estructura obligatoria de cada lección

Cada lección debe comenzar con:

# 🎯 OBJETIVO

Después desarrollar el tema con profundidad y progresión pedagógica.

Usar cuando aporten valor:

- 🧪 Laboratorio / ejemplos.
- ⚠️ Errores frecuentes.
- 💡 Idea importante.

Cada lección debe terminar con:

# 🧠 QUÉ DEBES RECORDAR

Este cierre debe contener entre 3 y 7 ideas esenciales y NO limitarse a repetir el objetivo.

## 24. Estilo

- español técnico claro;
- términos oficiales en inglés cuando sean nombres propios del producto o conceptos estándar;
- definir un término antes de utilizarlo intensivamente;
- profundidad sin relleno;
- explicar causa y efecto;
- evitar marketing;
- evitar afirmaciones no verificadas;
- no presuponer experiencia previa al inicio;
- aumentar progresivamente el nivel hasta internals y producción.

## 25. Continuidad entre lecciones

Cada lección pertenece a un PATH mayor.

Debe:

- respetar lo aprendido anteriormente;
- evitar reenseñar bloques completos;
- introducir solamente los prerrequisitos necesarios;
- preparar conceptos posteriores;
- utilizar los vecinos del PATH como contexto;
- mantener terminología consistente.

## 26. Criterio de finalización

Al completar el PATH, el alumno debe poder:

- desplegar Elastic Stack sobre Fedora;
- ingerir datos desde múltiples fuentes;
- diseñar mappings, templates y data streams;
- buscar y agregar datos eficazmente;
- administrar shards, replicas y clusters;
- operar Logstash y Elastic Agent/Fleet;
- normalizar con ECS;
- construir búsquedas y dashboards útiles;
- crear alertas;
- asegurar la plataforma;
- implementar lifecycle y backups;
- dimensionar y optimizar;
- diagnosticar fallos;
- realizar upgrades;
- automatizar operaciones;
- explicar los principales internals;
- diseñar y operar una arquitectura de producción completa.
