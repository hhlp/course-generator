# Bibliografía — JavaScript 0 → Experto

## Principal
- David Flanagan — *JavaScript: The Definitive Guide, 7th Edition*.
- Eric Freeman, Elisabeth Robson — *Head First JavaScript Programming, Second Edition*.
- Adam D. Scott, Matthew MacDonald, Shelley Powers — *JavaScript Cookbook: Programming the Web, 3rd Edition*.

## Profundización del lenguaje y modelos mentales
- Kyle Simpson — *You Don't Know JS Yet* (serie).

La serie se utiliza transversalmente para construir modelos mentales profundos del lenguaje, especialmente en:
- tipos, valores y coerción;
- scope, lexical scope y closures;
- funciones;
- `this`;
- objetos, prototypes y clases;
- mecanismos fundamentales del lenguaje.

Su función es de profundización conceptual. No sustituye a ECMA-262 como referencia normativa. Cuando una explicación pedagógica, un libro y la especificación difieran, debe comprobarse la versión actual de ECMA-262 y la documentación oficial aplicable.

## Asincronía, concurrencia y runtime
- Thomas Hunter II, Bryan English — *Multithreaded JavaScript: Concurrency Beyond the Event Loop*.
- Para Promises, Jobs y async/await, utilizar ECMA-262 y documentación oficial del runtime; no atribuir un volumen de asincronía a la segunda edición de YDKJS Yet.
- Documentación oficial de Node.js — Event Loop, Timers, Streams, Worker Threads, Async Hooks, AsyncLocalStorage y AbortController/AbortSignal.
- ECMAScript Language Specification (ECMA-262) — Promises, Jobs, Agents, Agent Clusters y módulos.

## Aplicaciones y ecosistema
- Adam D. Scott — *JavaScript Everywhere: Building Cross-Platform Applications with GraphQL, React, React Native, and Electron*.
- Documentación oficial de npm.
- Documentación oficial de MongoDB/mongosh para los apartados donde JavaScript se aplica al ecosistema MongoDB.

## Normativa y referencia
- ECMA-262 — ECMAScript Language Specification.
- TC39 — propuestas, proceso y material normativo.
- MDN Web Docs — referencia complementaria para características estándar y APIs de host cuando corresponda.

## Motores, rendimiento y herramientas
- Documentación y material técnico oficial de V8.
- Documentación oficial de Node.js Inspector y profiling.
- ESTree — especificación/convenio de AST del ecosistema JavaScript.
- Documentación de ESLint y herramientas AST empleadas en laboratorios.

## Big O y Regex aplicados a JavaScript (sin duplicar sus paths independientes)
- ECMA-262 — especificación normativa de Array, Map, Set, String y RegExp; distinguir garantías normativas de costes dependientes del motor.
- MDN Web Docs — referencia de `RegExp`, flags, métodos `String` y colecciones JavaScript; verificar compatibilidad por versión.
- Documentación oficial de Node.js — `perf_hooks`, Inspector, CPU profiling, benchmarks, streams y Worker Threads.
- Documentación técnica oficial de V8 — rendimiento de RegExp, JIT, estructuras internas y garbage collection cuando proceda.

Los libros especializados de teoría de expresiones regulares pertenecen exclusivamente al learning path Regex y **no forman parte de la bibliografía de JavaScript**. Big O se estudia aquí aplicado al código JavaScript, sin reproducir el curso teórico independiente.

## Mapa de uso de la bibliografía
| Fuente | Función principal |
|---|---|
| *Head First JavaScript Programming* | Introducción y aprendizaje progresivo |
| *JavaScript: The Definitive Guide* | Cobertura general y referencia del lenguaje |
| *JavaScript Cookbook* | Práctica, soluciones y patrones aplicados |
| *You Don't Know JS Yet* | Profundización conceptual y modelos mentales |
| *Multithreaded JavaScript* | Asincronía avanzada, concurrencia y paralelismo |
| ECMA-262 / TC39 | Semántica normativa y evolución del lenguaje |
| Node.js docs | Comportamiento y APIs del runtime |
| V8 docs | Motor, optimización, memoria e internals |

## Mapeo de *You Don't Know JS Yet* al learning path
- Bloques 0–4: fundamentos, valores y funciones.
- Bloque 5: scope y closures — prioridad alta.
- Bloques 8–10: objetos, `this`, prototypes y clases — prioridad alta.
- Bloque 11: referencias conceptuales únicamente cuando el contenido del volumen utilizado las cubra. Para los bloques 14–15, priorizar ECMA-262, Node.js y Multithreaded JavaScript.
- Bloque 22: preparación conceptual para estudiar la especificación; ECMA-262 sigue siendo la autoridad normativa.

## Política de uso de fuentes
La especificación y la documentación oficial prevalecen cuando una característica haya cambiado desde la publicación de un libro.

Las referencias exactas de capítulos, secciones o páginas solo deben incluirse cuando hayan sido verificadas. No se deben atribuir contenidos a un volumen de *You Don't Know JS Yet* que no estén presentes en la edición utilizada.


## Volúmenes y estado de You Don't Know JS Yet
Usar el [índice oficial del autor](https://github.com/getify/You-Dont-Know-JS/tree/2nd-ed), comprobando su estado en la fecha de consulta:
- Get Started: fundamentos y orientación.
- Scope & Closures: referencia conceptual principal del Bloque 5.
- Objects & Classes: el índice lo identifica como borrador estable dentro de The Unbooks; relacionar con bloques 8–10.
- Types & Grammar: identificado como borrador preliminar dentro de The Unbooks; contrastar siempre con la especificación.
- Sync & Async y ES.Next & Beyond figuran cancelados. No citarlos como libros publicados de esta edición.
No confundir Async & Performance de la primera edición con un volumen de la segunda; si se utiliza en el futuro, declarar edición y contrastar contenido histórico.

## Fuentes oficiales y edición objetivo
- [ECMAScript 2025, ECMA-262, 16.ª edición](https://262.ecma-international.org/16.0/): base normativa estable.
- [Borrador vivo de ECMA-262](https://tc39.es/ecma262/): extensiones posteriores; anotar fecha de consulta y estado.
- [ECMA-402](https://tc39.es/ecma402/): Intl e internacionalización.
- [Documentación de Node.js 24.x](https://nodejs.org/docs/latest-v24.x/api/): APIs del runtime base; contrastar con la versión exacta instalada.
- [Contexto asíncrono](https://nodejs.org/docs/latest-v24.x/api/async_context.html), [Async Hooks](https://nodejs.org/docs/latest-v24.x/api/async_hooks.html) y [Diagnostics Channel](https://nodejs.org/docs/latest-v24.x/api/diagnostics_channel.html).
- [Streams](https://nodejs.org/docs/latest-v24.x/api/stream.html), [filesystem](https://nodejs.org/docs/latest-v24.x/api/fs.html), [test runner](https://nodejs.org/docs/latest-v24.x/api/test.html) y [Worker Threads](https://nodejs.org/docs/latest-v24.x/api/worker_threads.html).
- [Sparkplug](https://v8.dev/blog/sparkplug), [Maglev](https://v8.dev/blog/maglev) y [Turboshaft y evolución del compilador](https://v8.dev/blog/leaving-the-sea-of-nodes): contexto de implementación, sujeto a versión.
- [JavaScript Cookbook, 3.ª edición](https://www.oreilly.com/library/view/javascript-cookbook-3rd/9781492055747/): Adam D. Scott, Matthew MacDonald y Shelley Powers.
- [Head First JavaScript Programming, 2.ª edición](https://www.oreilly.com/library/view/head-first-javascript/9781098147938/): Eric Freeman y Elisabeth Robson.

JavaScript Everywhere se mantiene como lectura complementaria de integración. Seleccionar contenido compatible con el alcance Node.js; sus capítulos de interfaces y frameworks no son prerrequisitos de este curso.
Los ejemplos de libros centrados en navegador deben adaptarse al runtime cuando proceda, conservando la semántica y evitando introducir DOM como dependencia inicial.
