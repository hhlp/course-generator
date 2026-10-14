# Dominio — OpenTelemetry en profundidad

PATH 0 → experto orientado a Fedora/RHEL y al ecosistema upstream de OpenTelemetry.

## Alcance
Signals, logs, metrics, traces, Resources, Attributes, Semantic Conventions, Context, Baggage, OTLP, API, SDK, Collector, receivers, processors, exporters, connectors, extensions, pipelines, instrumentación manual/automática, sampling, OTTL, resiliencia, seguridad, troubleshooting, internals y desarrollo de componentes.

Integraciones: Prometheus, Grafana, Loki, Tempo, Elastic/Elasticsearch, OpenSearch, Jaeger y Zipkin. Se estudian como integraciones; este PATH no sustituye sus PATH específicos.

## Estándar pedagógico
Cada lección comienza obligatoriamente con `🎯 OBJETIVO` y termina con `🧠 QUÉ DEBES RECORDAR` (3–7 ideas esenciales). Incluir `🧪 Laboratorio/ejemplos`, `⚠️ Errores frecuentes` y `💡 Idea importante` cuando aporten valor.

El desarrollo debe ser completo, profundo, progresivo y didáctico; nunca un mero resumen. Explicar arquitectura, flujo de datos, configuración, verificación, trade-offs, seguridad, rendimiento y diagnóstico.

## Reglas técnicas
Distinguir siempre API, SDK, OTLP, Collector y backend. Tratar estabilidad/versionado cuando proceda. Los laboratorios deben ser reproducibles y verificar resultados. Incluir Fedora, systemd, SELinux, firewalld, Podman y Kubernetes donde corresponda. Dar prioridad a la especificación y documentación upstream actuales.


## Libro principal
`Learning OpenTelemetry`, de Ted Young y Austin Parker (O'Reilly Media), es la guía bibliográfica principal y el hilo conductor pedagógico del PATH.

El generador debe aprovechar el libro para construir explicaciones progresivas, pero NO debe reducir el temario a su índice ni omitir temas del `initial.txt`. Este PATH amplía el libro con documentación y especificaciones upstream, Collector/Contrib, OTTL, internals, desarrollo de componentes, seguridad, Fedora/RHEL, contenedores, Kubernetes, HA, rendimiento, troubleshooting e integraciones.

Para información sensible a versión o evolución del proyecto, prevalece siempre el upstream actual.

## OpenTelemetry + Kubernetes
El PATH debe cubrir Kubernetes desde la perspectiva de observabilidad OpenTelemetry sin convertirse en un curso general de Kubernetes. Incluir Collector DaemonSet/Deployment/Gateway/Sidecar, OpenTelemetry Operator, OpenTelemetryCollector e Instrumentation CRDs, Target Allocator, k8sattributes, kubeletstats, k8s_cluster, filelog, service discovery, metadata enrichment, RBAC, ServiceAccounts, Secrets, NetworkPolicies, OTLP interno, Helm, recursos, memory_limiter, queues, backpressure, HA, scaling, tail sampling distribuido, multi-cluster, multi-tenancy, seguridad y troubleshooting.

La frontera pedagógica es: este PATH enseña cómo instrumentar, recopilar, procesar, transportar y diagnosticar telemetría en Kubernetes; el PATH específico de Kubernetes enseña Kubernetes en profundidad.


## Requisitos de profundidad por bloque — revisión 6
- Mantener los bloques 0–183 y todas las lecciones originales; las nuevas sublecciones amplían sin sustituirlas.
- Prohibido convertir una lección en un resumen genérico repetido: cada lección debe explicar mecanismos, contratos, límites, ejemplos y verificación propios de su tema.
- Para cada laboratorio: prerequisitos, versiones, configuración completa, comandos, salida esperada, pruebas negativas, limpieza y troubleshooting.
- Traces: context propagation, span lifecycle, links, async, head/tail sampling y sesgos.
- Metrics: temporality delta/cumulative, agregaciones, vistas, histogramas, exemplars y cardinalidad.
- Logs: LogRecord, severity, timestamps, journald/syslog/filelog, correlación y deduplicación.
- OTLP: Protobuf, gRPC/HTTP, errores parciales, TLS, compresión, límites, retries y compatibilidad.
- SDK: providers, processors/readers, flush/shutdown, instrumentación manual/automática y madurez por lenguaje.
- Collector: Core/Contrib, pdata, fan-out, queues, backpressure, memory_limiter, batching, pipelines y pruebas.
- OTTL: contextos, paths, funciones, condiciones, error_mode, pruebas y tratamiento de PII.
- Seguridad: threat modeling, mínimo privilegio, mTLS, autenticación, autorización, secretos, redaction y aislamiento multi-tenant.
- Fedora/RHEL: systemd, journald, SELinux, firewalld, Podman, permisos, hardening, upgrades y rollback.
- Kubernetes: patrones agent/gateway, Operator, Target Allocator, afinidad de traces, RBAC, NetworkPolicies, HA y scaling.
- Internals: ciclo de vida, factories, interfaces, consumer model, pdata, componentes personalizados, CI y contribuciones upstream.
- Separar estrictamente hechos normativos de decisiones de implementación, recomendaciones y aspectos dependientes de versión.

## Criterios de aceptación
1. Numeración única y continua dentro de cada bloque; sin eliminación de contenidos originales.
2. Ejemplos reproducibles, resultados comprobables y pruebas de fallos por bloque relevante.
3. Describir pérdidas y duplicados posibles; no prometer entrega exactamente una vez sin evidencia.
4. Evitar configuraciones o nombres de componentes obsoletos: comprobar siempre upstream y fijar versiones.
5. El proyecto experto debe incluir diagramas, repositorio, pruebas, métricas SLO, runbooks, seguridad y dimensionamiento.
