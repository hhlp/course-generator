# Bibliografía — OpenTelemetry + Python

## Libro principal

**Learning OpenTelemetry: Setting Up and Operating a Modern Observability System**,
Ted Young y Austin Parker, O’Reilly Media. Guía conceptual y operativa; no es un
manual exhaustivo del SDK de Python. Complementarlo con documentación y código
upstream. No reducir el currículo al índice del libro ni inventar páginas o citas.

## Fuentes primarias

La revisión de 2026-10-22 consultó las páginas de Python, instrumentación manual,
zero-code, configuración y troubleshooting, además de la ficha editorial. El
resto constituye un catálogo de consulta para desarrollar las lecciones, no una
afirmación de que se ha verificado cada integración en ejecución.

### P01 — OpenTelemetry Python: documentación oficial

[OpenTelemetry Python: documentación oficial](https://opentelemetry.io/docs/languages/python/)

Entrada principal y enlaces a la implementación.

### P02 — Instrumentación manual de Python

[Instrumentación manual de Python](https://opentelemetry.io/docs/languages/python/instrumentation/)

API/SDK y ejemplos por señal; comprobar su estado al generar.

### P03 — Instrumentación zero-code de Python

[Instrumentación zero-code de Python](https://opentelemetry.io/docs/zero-code/python/)

Bootstrap, launcher y activación de instrumentaciones.

### P04 — Configuración del agente Python

[Configuración del agente Python](https://opentelemetry.io/docs/zero-code/python/configuration/)

Variables y opciones específicas; verificar precedencias.

### P05 — Troubleshooting de instrumentación automática

[Troubleshooting de instrumentación automática](https://opentelemetry.io/docs/zero-code/python/troubleshooting/)

Imports, arranque y precauciones de servidores prefork.

### P06 — Referencia API y SDK Python

[Referencia API y SDK Python](https://opentelemetry-python.readthedocs.io/en/latest/)

Contratos, firmas y referencias de implementación.

### P07 — Referencia Python Contrib

[Referencia Python Contrib](https://opentelemetry-python-contrib.readthedocs.io/en/latest/)

Compatibilidad y opciones de cada instrumentación.

### P08 — Repositorio OpenTelemetry Python

[Repositorio OpenTelemetry Python](https://github.com/open-telemetry/opentelemetry-python)

Código, tests, releases, metadatos y changelogs.

### P09 — Repositorio OpenTelemetry Python Contrib

[Repositorio OpenTelemetry Python Contrib](https://github.com/open-telemetry/opentelemetry-python-contrib)

Paquetes de instrumentación y sus restricciones.

### P10 — Especificación OpenTelemetry

[Especificación OpenTelemetry](https://opentelemetry.io/docs/specs/otel/)

Referencia normativa para señales, contexto y SDK.

### P11 — Especificación OTLP

[Especificación OTLP](https://opentelemetry.io/docs/specs/otlp/)

Transporte y semántica de respuestas y errores.

### P12 — Convenciones semánticas

[Convenciones semánticas](https://opentelemetry.io/docs/specs/semconv/)

Atributos y migraciones de HTTP, DB y messaging.

### P13 — Collector

[Collector](https://opentelemetry.io/docs/collector/)

Configuración auxiliar, operación y diagnóstico.

### P14 — OpenTelemetry Operator

[OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator)

Inyección y compatibilidad de Python en Kubernetes.

### P15 — Python: logging

[Python: logging](https://docs.python.org/3/library/logging.html)

Handlers, propagación y formatos.

### P16 — Python: contextvars

[Python: contextvars](https://docs.python.org/3/library/contextvars.html)

Contexto local de ejecución y copia de contexto.

### P17 — Python: asyncio

[Python: asyncio](https://docs.python.org/3/library/asyncio.html)

Tareas, cancelación, concurrencia y ciclo de vida.

### P18 — Python: multiprocessing

[Python: multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

Modelos de inicio y aislamiento de procesos.

### P19 — OpenTelemetry Demo

[OpenTelemetry Demo](https://opentelemetry.io/docs/demo/)

Referencia de aplicación distribuida; no reemplaza el lab Python.

### P20 — Learning OpenTelemetry — editorial

[Learning OpenTelemetry — editorial](https://www.oreilly.com/library/view/learning-opentelemetry/9781098147174/)

Información bibliográfica del libro principal.

## Correspondencia con el currículo

| Bloques | Referencias de partida |
|---|---|
| 0–5 | P01, P02, P06, P08, P10, P20 |
| 6–11 | P02, P06, P10, P11, P12 |
| 12–20 | P03, P04, P05, P07, P09, P12 |
| 21–26 | P02, P06, P07, P10, P15 |
| 27–32 | P05, P07, P09, P16, P17, P18 |
| 33–36 | P06, P08, P09, P10 |
| 37–40 | P04, P07, P11, P13, P14 |
| 41–46 | P05, P06, P08, P09, P12, P19 |

## Reglas de uso

1. La especificación define contratos comunes; la documentación y el código
   versionados determinan qué implementa Python realmente.
2. Consultar también la documentación oficial del framework, driver y backend
   concretos elegidos para cada laboratorio. Registrar esas versiones y enlaces.
3. Las rutas latest/stable de documentación son referencias de consulta; el
   laboratorio debe anotar release, tag o commit compatible para reproducirse.
4. No copiar sin revisión snippets antiguos ni asumir que una integración soporta
   todas las señales. Diferenciar instrumentación upstream de variantes de vendors.
5. El libro apoya la enseñanza; para defaults, estabilidad y compatibilidad
   prevalecen las fuentes primarias actualizadas.
