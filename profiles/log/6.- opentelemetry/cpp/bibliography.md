# Bibliografía — OpenTelemetry con C++

Revisión documental: 2026-10-22. Las fuentes oficiales determinan las APIs y
capacidades; los libros aportan explicación y contexto. Al generar código,
abrir la documentación de la **release fijada**, no copiar sin comprobar un
snippet de `main`. Los enlaces a ramas móviles sirven de entrada documental.

## Fuentes oficiales principales

1. **OpenTelemetry: C++**. Estado de señales y entrada a documentación,
   integraciones y API. Bloques 0, 4 y revisión de capacidades.
   <https://opentelemetry.io/docs/languages/cpp/>
2. **Getting Started by Example — C++**. Primer programa y montaje de un ejemplo.
   Bloques 2–5; contrastar toolchain con la release seleccionada.
   <https://opentelemetry.io/docs/languages/cpp/getting-started/>
3. **Instrumentation — C++**. Instrumentación de aplicaciones y bibliotecas,
   separación API/SDK y ejemplos. Bloques 4–18 y 21.
   <https://opentelemetry.io/docs/languages/cpp/instrumentation/>
4. **Using instrumentation libraries — C++**. Integraciones nativas y externas;
   no presupone cobertura universal. Bloques 10–12 y 21.
   <https://opentelemetry.io/docs/languages/cpp/library/>
5. **opentelemetry-cpp — repositorio oficial**. Headers, factories, ownership,
   pruebas y ejemplos son evidencia para resolver dudas de la implementación.
   <https://github.com/open-telemetry/opentelemetry-cpp>
6. **INSTALL.md**. Sistemas de construcción, dependencias y opciones. Leer el
   archivo del tag elegido. Bloques 2–3 y 25.
   <https://github.com/open-telemetry/opentelemetry-cpp/blob/main/INSTALL.md>
7. **Releases de opentelemetry-cpp**. Selección de versión y revisión de cambios.
   Bloques 3 y 31.
   <https://github.com/open-telemetry/opentelemetry-cpp/releases>
8. **Ejemplos upstream de C++**. Buscar ejemplos de cada señal y transporte en
   el checkout fijado; compilarlos antes de adaptarlos.
   <https://github.com/open-telemetry/opentelemetry-cpp/tree/main/examples>
9. **Tests upstream de C++**. Consultar los tests del componente seleccionado
   para comportamiento de buffers, callbacks, shutdown y configuración.
   <https://github.com/open-telemetry/opentelemetry-cpp/tree/main/sdk>
10. **opentelemetry-cpp-contrib** y **Registry**. Descubrimiento de integraciones;
    cada paquete requiere su propia revisión de versión y mantenimiento.
    <https://github.com/open-telemetry/opentelemetry-cpp-contrib>
    <https://opentelemetry.io/ecosystem/registry/>

## Especificaciones y arquitectura común

- **OpenTelemetry Specification**. API, SDK, contexto, signals, providers,
  Resource e instrumentation scope. Define el contrato común; no demuestra por
  sí sola que C++ implemente cada función.
  <https://opentelemetry.io/docs/specs/otel/>
- **OTLP Specification**. Transporte y semántica de intercambio; distinguir
  protocolo de opciones concretas de un exportador.
  <https://opentelemetry.io/docs/specs/otlp/>
- **Semantic Conventions**. HTTP, RPC, datos, mensajería y recursos. Fijar
  versión y distinguir convenciones estables y en desarrollo.
  <https://opentelemetry.io/docs/specs/semconv/>
- **W3C Trace Context**. `traceparent`, `tracestate` y validación de entradas.
  <https://www.w3.org/TR/trace-context/>
- **W3C Baggage**. Propagación de datos con política explícita de privacidad.
  <https://www.w3.org/TR/baggage/>
- **OpenTelemetry Collector** y **Collector Contrib**. Configuración, límites y
  componentes de la distribución utilizada; comprobar su estabilidad.
  <https://opentelemetry.io/docs/collector/>
  <https://github.com/open-telemetry/opentelemetry-collector-contrib>

## C++ y herramientas: fuentes primarias complementarias

- **C++ Core Guidelines**. RAII, ownership, errores y concurrencia; consultar
  reglas relevantes al caso de instrumentación.
  <https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines>
- **CMake — documentación oficial**. Targets, paquetes, presets y dependencias.
  <https://cmake.org/documentation/>
- **Clang — AddressSanitizer y ThreadSanitizer**. Diagnóstico de lifetimes y
  carreras en combinaciones soportadas de compilador y plataforma.
  <https://clang.llvm.org/docs/AddressSanitizer.html>
  <https://clang.llvm.org/docs/ThreadSanitizer.html>
- **gRPC C++**. APIs, flujo de ejecución y ejemplos oficiales del framework
  seleccionado. No asumir que su contexto de aplicación equivale a OTel Context.
  <https://grpc.io/docs/languages/cpp/>
- **Boost.Asio**. Contrato de executors y handlers para la vía opcional de I/O
  asíncrono. Seleccionar documentación de la versión instalada.
  <https://www.boost.org/doc/libs/release/doc/html/boost_asio.html>
- **spdlog**. Revisar su API antes de desarrollar o elegir un adaptador de logs.
  <https://github.com/gabime/spdlog>
- **systemd**. Orden de parada y entorno del proceso en unidades de servicio.
  <https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html>

## Libros de apoyo

- **Learning OpenTelemetry — Ted Young y Austin Parker, O’Reilly Media**.
  Guía conceptual principal heredada del curso general: diseño de telemetría,
  instrumentación y operación. No usar como autoridad de APIs actuales de C++.
- **Effective Modern C++ — Scott Meyers**. Ownership, move semantics, tipos y
  lambdas; apoyo a bloques 1 y 6–9. Su alcance C++11/14 no cubre todas las
  necesidades de coroutines posteriores.
- **C++ Concurrency in Action, segunda edición — Anthony Williams**.
  Concurrencia, sincronización y diseño de tareas; apoyo a bloques 8, 16 y 26.
- **A Tour of C++, tercera edición — Bjarne Stroustrup**.
  Repaso del lenguaje moderno y orientación para C++20; no sustituye practicar
  lifetimes y propagación con el SDK real.

Los libros de C++ son complementarios, no prerrequisitos que deban completarse
íntegramente. No existe aquí la suposición de que un libro genérico de OTel
sea un manual específico y actualizado de `opentelemetry-cpp`.

## Selección de backends y vigencia

Elegir un backend por señal y abrir su documentación de la versión fijada.
Posibles destinos: Prometheus para métricas, Jaeger o Tempo para trazas, y un
backend de logs compatible. Estas alternativas no implican que todas las rutas
OTLP o funciones estén disponibles en cualquier versión.

- <https://prometheus.io/docs/>
- <https://www.jaegertracing.io/docs/>
- <https://grafana.com/docs/tempo/latest/>
- <https://grafana.com/docs/loki/latest/>

La revisión de este paquete comprobó la documentación general de C++, su página
de instrumentación y las instrucciones de construcción. Las demás fuentes se
incluyen como referencias para desarrollar y validar cada lección; no se afirma
haber ejecutado todos sus ejemplos ni certificado todas las integraciones.

## Orden de autoridad

1. Especificaciones y convenciones para la semántica común.
2. Documentación, código y tests de la release C++ para soporte y comportamiento.
3. Documentación de las versiones de transportes, frameworks y backends.
4. Libros y material explicativo.

Cuando difieran especificación e implementación, explicar la diferencia y
reproducirla. No describir como funcional lo que solo está propuesto o definido
en otra implementación de OpenTelemetry.
