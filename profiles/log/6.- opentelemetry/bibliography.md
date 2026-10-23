# Bibliografía — OpenTelemetry en profundidad

## Principal
1. Learning OpenTelemetry — Ted Young, Austin Parker — O'Reilly Media.
   - Libro principal y guía pedagógica del PATH.
   - Usar para fundamentos, arquitectura, señales, instrumentación, API/SDK, propagación de contexto, OTLP, Collector y diseño de observabilidad.
   - No limitar el contenido del curso al alcance del libro.

2. OpenTelemetry Documentation.
   - Referencia técnica principal para el estado actual del proyecto.

3. OpenTelemetry Specification.
   - Autoridad normativa para APIs, SDKs, modelo de datos, propagación y comportamiento.

4. OpenTelemetry Protocol (OTLP) Specification.
5. OpenTelemetry Semantic Conventions.
6. OpenTelemetry Collector Documentation.
7. OpenTelemetry Collector Contrib.

## Internals y desarrollo
8. open-telemetry/opentelemetry-collector.
9. open-telemetry/opentelemetry-collector-contrib.
10. OpenTelemetry Proto.
11. OpenTelemetry Collector Builder.
12. OpenTelemetry Registry.
13. Repositorios oficiales de instrumentación OpenTelemetry por lenguaje.

## Integraciones
14. Prometheus Documentation.
15. Grafana Documentation.
16. Grafana Loki Documentation.
17. Grafana Tempo Documentation.
18. Elastic Observability Documentation.
19. OpenSearch Observability y Data Prepper Documentation.
20. Jaeger Documentation.
21. Zipkin Documentation.

## Plataforma
22. Fedora Documentation.
23. systemd documentation y manual pages.
24. SELinux/Fedora SELinux documentation.
25. firewalld Documentation.
26. Podman Documentation.
27. Kubernetes Documentation.

## Política bibliográfica
Para aspectos sujetos a evolución —estabilidad de señales, APIs, semantic conventions, Collector y componentes Contrib— prevalecen la especificación y documentación upstream de la versión estudiada.


## Jerarquía de fuentes
28. `Learning OpenTelemetry` actúa como guía pedagógica principal.
29. La documentación oficial actual complementa y actualiza el libro.
30. La OpenTelemetry Specification prevalece en cuestiones normativas.
31. OTLP Specification y Semantic Conventions prevalecen en sus respectivos dominios.
32. Collector/Collector Contrib documentation y código fuente se utilizan para operación avanzada e internals.
33. Cuando el libro y el upstream actual difieran por evolución del proyecto, enseñar el comportamiento actual e indicar la diferencia histórica cuando sea pedagógicamente útil.

## Kubernetes y OpenTelemetry
- OpenTelemetry Kubernetes documentation.
- OpenTelemetry Operator for Kubernetes documentation y repositorio upstream.
- OpenTelemetry Collector Kubernetes deployment documentation.
- OpenTelemetry Helm Charts.
- Kubernetes Documentation.
- Prometheus Receiver y Target Allocator documentation.
- Documentación upstream de k8sattributes, kubeletstats, k8s_cluster y filelog.

Para Operator, CRDs, Target Allocator y componentes Kubernetes prevalece siempre la documentación upstream actual sobre material impreso cuando existan diferencias de versión.

## Scopes de consulta — revisión profunda 7
### Fundamentos, modelo de datos y normas
- Learning OpenTelemetry (Young y Parker): hilo pedagógico; contrastar con upstream.
- OpenTelemetry Specification: Trace, Metrics, Logs, Context, Baggage, Resource y SDK.
- OpenTelemetry Semantic Conventions y schema files: estabilidad, atributos y migraciones.
- OpenTelemetry Proto y OTLP Specification: wire format, transporte y errores.

### Collector, rendimiento e internals
- OpenTelemetry Collector y Collector Contrib: código, componentes, changelogs y guías operativas.
- OpenTelemetry Collector Builder: distribución personalizada, manifest y build reproducible.
- OpenTelemetry Collector OTTL: sintaxis, funciones y ejemplos upstream.
- OpenTelemetry Collector testing y component interfaces: pruebas, factories, pdata y lifecycle.

### Instrumentación por lenguaje
- Repositorios upstream de OpenTelemetry Python, Go, Java, JavaScript y C++: API/SDK, estabilidad y autoinstrumentación según versión.

### Plataforma, seguridad e integraciones
- Documentación Fedora/RHEL, systemd, SELinux, firewalld, Podman y Kubernetes.
- OpenTelemetry Operator, Helm Charts, Kubernetes receivers y Target Allocator.
- Documentación de seguridad del Collector, TLS/mTLS y prácticas de mínimo privilegio.
- Documentación upstream Prometheus, Grafana, Loki, Tempo, Elastic, OpenSearch, Jaeger y Zipkin.

**Regla de actualidad:** fijar versiones concretas de SDK/Collector/componentes en cada laboratorio y verificar nombres, estado de estabilidad y compatibilidad contra documentación upstream vigente.

## Referencias enlazadas y finalidad — revisión 7

Consulta de referencias principales: 22 de octubre de 2026. La consulta no
certifica todas las combinaciones de SDK, componente y backend; fijar versiones
y verificar compatibilidad al desarrollar cada laboratorio.

| Fuente | Uso en el PATH |
| --- | --- |
| [Documentación OpenTelemetry](https://opentelemetry.io/docs/) | Arquitectura y guías prácticas |
| [Especificación](https://opentelemetry.io/docs/specs/otel/) | Contratos normativos |
| [Context](https://opentelemetry.io/docs/specs/otel/context/) | Contexto y ciclo de scopes |
| [Propagadores](https://opentelemetry.io/docs/specs/otel/context/api-propagators/) | Carriers, extracción e inyección |
| [W3C Trace Context](https://www.w3.org/TR/trace-context/) | traceparent y tracestate |
| [W3C Baggage](https://www.w3.org/TR/baggage/) | Propagación de baggage |
| [Modelo de métricas](https://opentelemetry.io/docs/specs/otel/metrics/data-model/) | Streams, temporality y escritor único |
| [API de métricas](https://opentelemetry.io/docs/specs/otel/metrics/api/) | Instrumentos y callbacks |
| [SDK de métricas](https://opentelemetry.io/docs/specs/otel/metrics/sdk/) | Views, readers y agregaciones |
| [OTLP](https://opentelemetry.io/docs/specs/otlp/) | Transporte, formato y aceptación parcial |
| [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) | Atributos, nombres y estabilidad |
| [Estado de especificaciones](https://opentelemetry.io/docs/specs/status/) | Madurez por señal y componente |
| [Profiles](https://opentelemetry.io/docs/concepts/signals/profiles/) | Introducción y relación con otras señales |
| [Collector](https://opentelemetry.io/docs/collector/) | Configuración y operación |
| [Collector Core](https://github.com/open-telemetry/opentelemetry-collector) | Interfaces, pdata, lifecycle y código |
| [Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) | Componentes, OTTL y changelogs |
| [Tail sampling](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor) | Estado, afinidad y decisiones |
| [Kubernetes](https://opentelemetry.io/docs/platforms/kubernetes/) | Recolección y despliegue |
| [Operator](https://github.com/open-telemetry/opentelemetry-operator) | Reconciliación, CRDs y autoinstrumentación |
| [Helm Charts](https://github.com/open-telemetry/opentelemetry-helm-charts) | Despliegue versionado |
| [Datasources de Grafana](https://grafana.com/docs/grafana/latest/datasources/) | Consulta y visualización sobre backends |

### OpenTelemetry {Python, C++, Go, JavaScript, Java}

Estas referencias documentan variantes de instrumentación de los conceptos
comunes. El estudiante elige el lenguaje de sus ejemplos; no debe completar
cinco itinerarios ni repetir todos los laboratorios. Ninguno es obligatorio
como lenguaje principal. Comprobar API, SDK, instrumentación automática,
configuración y madurez por señal en la versión seleccionada.

- [Python](https://opentelemetry.io/docs/languages/python/).
- [C++](https://opentelemetry.io/docs/languages/cpp/).
- [Go](https://opentelemetry.io/docs/languages/go/).
- [JavaScript](https://opentelemetry.io/docs/languages/js/).
- [Java](https://opentelemetry.io/docs/languages/java/).

El desarrollo de componentes del Collector usa Go y pertenece a la etapa
experta; no convierte Go en requisito para instrumentar una aplicación.
Learning OpenTelemetry continúa como libro principal y guía pedagógica.
