# Bibliografía: OpenTelemetry con Java

Documentación consultada el 22 de octubre de 2026. Prioridad: especificación,
documentación Java y repositorios oficiales de la versión fijada. Los enlaces
son documentación viva: registrar release/tag y fecha al generar cada práctica.

## Fuentes principales de Java

- [OpenTelemetry Java](https://opentelemetry.io/docs/languages/java/): entrada
  oficial y estado de las señales del núcleo.
- [Ecosistema de instrumentación](https://opentelemetry.io/docs/languages/java/instrumentation/):
  relación entre agente, API, Starter, instrumentación de bibliotecas y bridges.
- [Java Agent](https://opentelemetry.io/docs/zero-code/java/agent/): instalación,
  instrumentación adicional y navegación a configuración y extensiones.
- [Bibliotecas soportadas](https://opentelemetry.io/docs/zero-code/java/agent/supported-libraries/):
  comprobar cobertura exacta y versiones antes de diseñar cada integración.
- [Spring Boot Starter](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/):
  alternativa basada en autoconfiguración Spring.
- [SDK Java](https://opentelemetry.io/docs/languages/java/sdk/): componentes,
  extensibilidad y herramientas de pruebas.
- [Configuración del SDK](https://opentelemetry.io/docs/languages/java/configuration/):
  configuración programática, autoconfigure y mecanismos declarativos.

## Especificaciones y código fuente

- [Especificación OpenTelemetry](https://opentelemetry.io/docs/specs/otel/).
- [OTLP](https://opentelemetry.io/docs/specs/otlp/).
- [Convenciones semánticas](https://opentelemetry.io/docs/specs/semconv/).
- [W3C Trace Context](https://www.w3.org/TR/trace-context/).
- [W3C Baggage](https://www.w3.org/TR/baggage/).
- [SDK Java y ejemplos](https://github.com/open-telemetry/opentelemetry-java).
- [Agente, Starter y módulos de instrumentación](https://github.com/open-telemetry/opentelemetry-java-instrumentation).
- [Contribuciones Java](https://github.com/open-telemetry/opentelemetry-java-contrib).

## Documentación complementaria para las prácticas

- [Spring Boot](https://docs.spring.io/spring-boot/): consultar la versión fijada.
- [Micrometer](https://docs.micrometer.io/micrometer/reference/): Observation,
  métricas y relación con registros y bridges.
- [Project Reactor](https://projectreactor.io/docs): programación reactiva.
- [Apache Kafka](https://kafka.apache.org/documentation/): productores y consumidores.
- [JUnit](https://junit.org/): pruebas del proyecto según versión seleccionada.
- [Testcontainers Java](https://java.testcontainers.org/): pruebas de integración.
- [Collector](https://opentelemetry.io/docs/collector/): consultar el tronco común
  para administración profunda y operación de los pipelines.

## Libro de apoyo

Ted Young y Austin Parker. *Learning OpenTelemetry*. O'Reilly Media.
Marco conceptual del tronco común; no sustituye la referencia del SDK Java ni
las matrices de compatibilidad. No se asume que contenga todas las prácticas
Java del PATH. La selección de capítulos debe comprobarse en la edición usada.

## Política de uso

No usar ejemplos antiguos como autoridad de nombres semánticos, coordenadas,
propiedades, mínimos de JDK ni valores por defecto. Marcar APIs alpha y
opciones experimentales. En discrepancias prevalecen la especificación y la
documentación/código de la release elegida. Las referencias complementarias
son puntos de consulta; no se afirma haber ejecutado sus ejemplos.
