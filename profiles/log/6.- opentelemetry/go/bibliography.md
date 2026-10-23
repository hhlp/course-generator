# Bibliografía — OpenTelemetry con Go

Fecha de consulta del diseño: 2026-10-22. Documentación viva: consultar el tag
concreto de cada dependencia al desarrollar una lección. No tratar un enlace a
latest como una combinación de versiones ya probada.

## Fuentes primarias consultadas para esta especialización

| Fuente | Uso en el PATH |
| --- | --- |
| [OpenTelemetry Go](https://opentelemetry.io/docs/languages/go/) | Estado por señal y navegación del SDK |
| [Getting Started](https://opentelemetry.io/docs/languages/go/getting-started/) | Primer circuito y bootstrap de las señales |
| [Instrumentation](https://opentelemetry.io/docs/languages/go/instrumentation/) | Instrumentación manual y puente de logging |
| [Instrumentation libraries](https://opentelemetry.io/docs/languages/go/libraries/) | Integraciones de bibliotecas |
| [Exporters](https://opentelemetry.io/docs/languages/go/exporters/) | Salida OTLP y alternativas |
| [otelslog](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog) | Conversión de slog a LogRecords |
| [tracetest](https://pkg.go.dev/go.opentelemetry.io/otel/sdk/trace/tracetest) | Recorder y exporters de prueba |
| [SDK de métricas](https://pkg.go.dev/go.opentelemetry.io/otel/sdk/metric) | Readers, Views y agregación |
| [Zero-code Go](https://opentelemetry.io/docs/zero-code/go/) | Opciones de instrumentación sin cambios de código |
| [Choosing zero-code](https://opentelemetry.io/docs/zero-code/go/choosing-auto-instrumentation/) | Comparación de OBI y otelc |
| [Auto SDK](https://opentelemetry.io/docs/zero-code/go/autosdk/) | Compatibilidad de spans manuales y eBPF |
| [Go diagnostics](https://go.dev/doc/diagnostics) | pprof y diagnóstico del runtime |
| [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) | Contrato de nombres y atributos |

La página general de Go marca traces y metrics como estables y logs como release
candidate, mientras otras páginas conservan etiquetas experimentales para partes
de logging. Resolver estabilidad por módulo y release antes de generar ejemplos;
no equiparar automáticamente el estado del SDK, exporter y bridge.

## Referencias oficiales adicionales para desarrollar las lecciones

Estos enlaces orientan la implementación posterior; no implican que se hayan
probado todos sus ejemplos o cada integración.

- [OpenTelemetry Go, código y releases](https://github.com/open-telemetry/opentelemetry-go).
- [OpenTelemetry Go Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib).
- [API de trazas](https://pkg.go.dev/go.opentelemetry.io/otel/trace).
- [SDK de trazas](https://pkg.go.dev/go.opentelemetry.io/otel/sdk/trace).
- [API de métricas](https://pkg.go.dev/go.opentelemetry.io/otel/metric).
- [SDK de logs](https://pkg.go.dev/go.opentelemetry.io/otel/sdk/log).
- [otelhttp](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp).
- [otelgrpc](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc).
- [Especificación OpenTelemetry](https://opentelemetry.io/docs/specs/otel/).
- [Especificación OTLP](https://opentelemetry.io/docs/specs/otlp/).
- [W3C Trace Context](https://www.w3.org/TR/trace-context/).
- [W3C Baggage](https://www.w3.org/TR/baggage/).
- [Collector](https://opentelemetry.io/docs/collector/).
- [Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib).
- [Collector Builder](https://opentelemetry.io/docs/collector/custom-collector/).
- [context](https://pkg.go.dev/context), [net/http](https://pkg.go.dev/net/http)
  y [log/slog](https://pkg.go.dev/log/slog), biblioteca estándar Go.
- [Race detector](https://go.dev/doc/articles/race_detector).
- [database/sql](https://pkg.go.dev/database/sql).
- [gRPC Go](https://grpc.io/docs/languages/go/).

Para SQL, caché, brokers y frameworks: comprobar el repositorio del módulo real,
matriz de compatibilidad, mantenimiento, licencia y señales emitidas. El Registry
no convierte por sí solo una integración externa en componente oficial.

## Libros de apoyo

- **Learning OpenTelemetry**, Ted Young y Austin Parker, O'Reilly Media.
  Libro principal del tronco común y apoyo conceptual de esta especialización.
  No sustituye la documentación de las APIs Go ni delimita la profundidad.
- **Learning Go**, Jon Bodner, O'Reilly Media. Apoyo de lenguaje cuando falten
  prerrequisitos; la formación completa pertenece al PATH Go.
- **Efficient Go**, Bartłomiej Płotka, O'Reilly Media. Complemento para
  benchmarks, asignaciones, profiling y evaluación de costes.

No se exige comprar libros para realizar los laboratorios. No se atribuyen
capítulos, fragmentos ni ejemplos a un libro cuyo texto no se haya consultado.
Las diferencias entre ediciones y APIs se resuelven a favor de upstream vigente.
