# Bibliografía — OpenTelemetry con JavaScript

Fecha de consulta de las fuentes principales: 2026-10-22.
La documentación y los repositorios oficiales determinan APIs y compatibilidad.
Los libros explican conceptos; sus ejemplos deben contrastarse con las versiones
fijadas del laboratorio. No se presupone que un plugin admita todas las versiones
de un framework.

## Guía conceptual principal

**Ted Young y Austin Parker — Learning OpenTelemetry. O'Reilly Media.**
Guía conceptual del proyecto general: instrumentación y recorrido de la
telemetría. No sustituye la documentación del SDK JavaScript ni cubre por sí
sola todo el path. No limitar el contenido del curso al índice del libro.

## Fuentes principales verificadas

1. [OpenTelemetry JavaScript](https://opentelemetry.io/docs/languages/js/).
   Referencia de alcance y estado: trazas y métricas estables; logs en desarrollo;
   navegador experimental. Revisar estado y runtimes antes de generar lecciones.
2. [Introducción con Node.js](https://opentelemetry.io/docs/languages/js/getting-started/nodejs/).
   Referencia para el primer servicio y el arranque previo a la aplicación.
   Revisar específicamente las notas de ESM antes de adoptar una receta de carga.
3. [Introducción con navegador](https://opentelemetry.io/docs/languages/js/getting-started/browser/).
   Punto de entrada para la extensión web. Conservar las advertencias de soporte
   y comprobar el contexto y la exportación con el bundle real.
4. [Instrumentación manual](https://opentelemetry.io/docs/languages/js/instrumentation/).
   Contrastar los ejemplos de API, señales y configuración durante el desarrollo
   de las lecciones de código.
5. [Uso de bibliotecas de instrumentación](https://opentelemetry.io/docs/languages/js/libraries/).
   Referencia para configurar plugins y evaluar qué proporciona la instrumentación
   de bibliotecas frente al código de negocio.
6. [Exportadores JavaScript](https://opentelemetry.io/docs/languages/js/exporters/).
   Referencia de transporte y configuración. Verificar la combinación concreta
   de exportador, señal y receptor antes de ejecutar cada práctica.
7. [Repositorio opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js).
   Consultar README, paquetes, ejemplos, releases y guías de actualización para
   resolver compatibilidad y estudiar internals.

## Referencias oficiales por consultar en cada implementación

Estas referencias amplían el trabajo por bloque; las versiones y funciones
concretas deben comprobarse al crear el laboratorio correspondiente.

| Fuente | Uso previsto |
| --- | --- |
| [opentelemetry-js-contrib](https://github.com/open-telemetry/opentelemetry-js-contrib) | README y código de cada plugin; soporte de bibliotecas y hooks |
| [Registro OpenTelemetry](https://opentelemetry.io/ecosystem/registry/) | Localizar instrumentaciones y revisar su propietario y estado |
| [Especificación OpenTelemetry](https://opentelemetry.io/docs/specs/otel/) | Contratos de API/SDK, contexto y señales |
| [OTLP](https://opentelemetry.io/docs/specs/otlp/) | Transporte, formatos y comportamiento del protocolo |
| [Convenciones semánticas](https://opentelemetry.io/docs/specs/semconv/) | Nombres y significado de atributos según versión |
| [Collector](https://opentelemetry.io/docs/collector/) | Configurar y comprobar pipelines locales |
| [Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) | Componentes adicionales y sus estados de soporte |
| [OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator) | Evaluar inyección de instrumentación Node.js en Kubernetes |
| [Node.js API](https://nodejs.org/api/) | AsyncLocalStorage, módulos, workers, procesos, HTTP y rendimiento |
| [npm CLI](https://docs.npmjs.com/cli/) | Reproducibilidad, lockfiles y resolución de dependencias |
| [TypeScript](https://www.typescriptlang.org/docs/) | Tipado y compilación de la extensión opcional |
| [W3C Trace Context](https://www.w3.org/TR/trace-context/) | Interpretación y propagación de contexto entre servicios |
| [W3C Baggage](https://www.w3.org/TR/baggage/) | Formato y límites de transporte de baggage |
| [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web) | CORS, CSP, fetch, navegación y comportamiento del navegador |
| [web-vitals](https://github.com/GoogleChrome/web-vitals) | Evaluación de métricas web en la extensión RUM |

Para Express, Fastify, NestJS, Next.js, Pino, Winston, drivers y clientes,
consultar además la documentación oficial de la versión instrumentada.
Distinguir integración propia del framework, plugin contrib y ejemplo de terceros.
Los materiales de proveedores son complementarios: no convierten una integración
particular en capacidad universal del SDK.

## Mapa de lectura

- Bloques 0–7: guía conceptual, documentación Node.js, SDK y bibliotecas.
- Bloques 8–14: contexto, especificaciones W3C, Node.js y cada plugin contrib.
- Bloques 15–22: instrumentación, convenciones, exportadores, OTLP y Collector.
- Bloques 23–27: código SDK, documentación del runtime, Operator y proveedor elegido.
- Bloques 28–31: documentación web, MDN, framework y medición web.
- Bloques 32–35: SDK/contrib, changelogs, especificaciones y evidencias del proyecto.
