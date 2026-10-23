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


## Requisitos de profundidad por bloque — revisión 7
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

## Nota sobre los lenguajes de instrumentación

OpenTelemetry {Python, C++, Go, JavaScript, Java} designa las variantes
por lenguaje de la API, el SDK y las bibliotecas de instrumentación.
Son referencias para aplicar los conceptos comunes del PATH, no cinco
itinerarios obligatorios ni cursos de programación independientes.

En cada ejemplo de instrumentación se indicará el lenguaje utilizado.
El estudiante podrá escoger el que corresponda a su aplicación; no será
necesario repetir los laboratorios en todos los lenguajes. Python no es
un requisito ni el lenguaje principal obligatorio.

El núcleo del PATH sigue siendo OpenTelemetry: señales, contexto, OTLP,
Collector, pipelines, OTTL, despliegue, seguridad y diagnóstico.
Las diferencias de soporte, configuración y estabilidad entre lenguajes
se consultarán en la documentación upstream de las versiones elegidas.

## Aplicación de la revisión 7

Se conservan los 184 bloques, sus identificadores y la cobertura original.
Las ampliaciones específicas de initial.txt desarrollan mecanismos que los
títulos generales no detallaban. El generador debe vincular cada explicación
a dichos mecanismos, sin reproducir párrafos genéricos intercambiables.
Las correcciones puntuales de precisión conservan el objetivo técnico y
quedan registradas en validation.json. No interpretar preservación como una
obligación de perpetuar una afirmación técnicamente incorrecta.

### Profundidad y delimitación de bloques

Cada lección general debe aportar un objeto de estudio propio: entradas,
estado, salidas, invariantes, límites, configuración aplicable y evidencias.
No inventar una configuración o valor por defecto para un concepto abstracto.
En fundamentos, gobernanza o contribución, los ejercicios son análisis de
incidentes, revisión de contratos o contribuciones reproducibles cuando no
corresponda desplegar un componente. Las relaciones con cada señal se explican
solo cuando exista una relación técnica real; se debe justificar la ausencia
cuando no aplique. Las nuevas lecciones no eximen de desarrollar las originales.

Separar arquitectura del proceso (32) de internals de implementación (162);
catálogo de componentes (60–64) de construcción y distribución (65–66, 179);
modelo de correlación (19), enlaces concretos (152–154) y validación entre
señales (155); requisitos de seguridad (113–121) de su diagnóstico operativo.
El bloque 93 proporciona la visión Kubernetes completa y los bloques 94–98
profundizan patrones, metadata y descubrimiento mediante casos diferentes.

### Progresión sin cambiar identificadores

1. Leer fundamentos y arquitectura (0–2). Usar las ampliaciones de 0, 1 y 31
   para un circuito local sintético antes de instrumentar código. Consultar
   123–127 como guía de preparación Fedora/RHEL según se necesite.
2. Estudiar modelo y contexto (3–23), API/SDK e instrumentación (24–30).
   Completar el camino de una sola aplicación en el lenguaje elegido.
3. Construir pipelines y operar Collector (31–49). Estudiar head sampling
   (51–52) antes de tail sampling (50) y políticas combinadas (53).
4. Desarrollar procesamiento (54–66), integraciones (67–79), instrumentación
   aplicada (80–89) y plataformas (90–105).
5. Trabajar cardinalidad, costes, diseño, seguridad y despliegue (106–127).
   Incorporar estos controles desde los primeros laboratorios que los requieran.
6. Dominar autoobservabilidad y diagnóstico (128–149), correlación,
   arquitectura y escalado (150–161).
7. Abordar internals y desarrollo de componentes (162–180) con conocimientos
   previos de Go para modificar el Collector. Este requisito es distinto de
   la elección de lenguaje de la aplicación. Finalizar 181–183.

### Contratos técnicos que deben verificarse

- Propagación: W3C traceparent/tracestate, carriers, extracción/inyección,
  attach/detach, asincronía, baggage y fronteras de confianza.
- Métricas: instrumentos, callbacks, Views, agregaciones, temporality,
  escritor único, timestamps, resets, histogramas y exemplars.
- OTLP: endpoints por señal, serialización, aceptación parcial, límites,
  errores recuperables/permanentes y diferencia entre recepción y durabilidad.
- SDK: no confundir API no-op con inicialización, exportación y shutdown del
  SDK. La configuración declarativa no implica una precedencia universal de
  variables de entorno; consultar reglas de implementación y versión.
- Collector: estado por componente, fan-out, mutabilidad, memoria, colas,
  reintentos y condiciones reales de pérdida y duplicación. No prometer
  exactly-once ni durabilidad extremo a extremo por activar una cola local.
- Grafana OSS: visualización mediante datasources que consultan backends.
  Grafana Cloud: especificar endpoint de ingestión, señal y autenticación.
- Profiles: fundamentos, correlación y matriz de soporte por versión. Separar
  profiling de diagnóstico con pprof y transporte de la señal profiles.
  No asumir igualdad de estabilidad o soporte con traces, metrics y logs.
- Componentes: comprobar nombres, aliases, feature gates y señales soportadas
  en la distribución concreta. Consultar changelogs antes de actualizar.

### Laboratorios y alcance de los archivos

Estos cuatro archivos definen el currículo y las instrucciones de generación.
No contienen por sí mismos un laboratorio desplegado ni resultados de ejecución.
Al desarrollar cada laboratorio, entregar todos los archivos que requiera:
configuración, código de aplicación cuando proceda, dependencias fijadas,
unidades systemd o manifiestos, comandos, fixtures, comprobaciones, resultados
esperados, casos negativos, diagnóstico y limpieza. Diferenciar resultados
esperados de resultados realmente medidos. Elegir un backend principal para
la práctica y probar alternativas en sus bloques; no exigir desplegar todos
los backends a la vez. Mantener operación local sin exposición pública como
entorno base y usar datos sintéticos sin secretos.
