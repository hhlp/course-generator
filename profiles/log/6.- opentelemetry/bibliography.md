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
13. Prometheus Documentation.
14. Grafana Documentation.
15. Grafana Loki Documentation.
16. Grafana Tempo Documentation.
17. Elastic Observability Documentation.
18. OpenSearch Observability y Data Prepper Documentation.
19. Jaeger Documentation.
20. Zipkin Documentation.

## Plataforma
21. Fedora Documentation.
22. systemd documentation y manual pages.
23. SELinux/Fedora SELinux documentation.
24. firewalld Documentation.
25. Podman Documentation.
26. Kubernetes Documentation.

## Política bibliográfica
Para aspectos sujetos a evolución —estabilidad de señales, APIs, semantic conventions, Collector y componentes Contrib— prevalecen la especificación y documentación upstream de la versión estudiada.


## Jerarquía de fuentes
1. `Learning OpenTelemetry` actúa como guía pedagógica principal.
2. La documentación oficial actual complementa y actualiza el libro.
3. La OpenTelemetry Specification prevalece en cuestiones normativas.
4. OTLP Specification y Semantic Conventions prevalecen en sus respectivos dominios.
5. Collector/Collector Contrib documentation y código fuente se utilizan para operación avanzada e internals.
6. Cuando el libro y el upstream actual difieran por evolución del proyecto, enseñar el comportamiento actual e indicar la diferencia histórica cuando sea pedagógicamente útil.

## Kubernetes y OpenTelemetry
- OpenTelemetry Kubernetes documentation.
- OpenTelemetry Operator for Kubernetes documentation y repositorio upstream.
- OpenTelemetry Collector Kubernetes deployment documentation.
- OpenTelemetry Helm Charts.
- Kubernetes Documentation.
- Prometheus Receiver y Target Allocator documentation.
- Documentación upstream de k8sattributes, kubeletstats, k8s_cluster y filelog.

Para Operator, CRDs, Target Allocator y componentes Kubernetes prevalece siempre la documentación upstream actual sobre material impreso cuando existan diferencias de versión.
