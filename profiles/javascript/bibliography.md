# Bibliografía — JavaScript 0 → Experto

## Principal
- David Flanagan — *JavaScript: The Definitive Guide, 7th Edition*.
- Eric Freeman, Elisabeth Robson — *Head First JavaScript Programming, Second Edition*.
- Adam D. Scott, Matthew MacDonald et al. — *JavaScript Cookbook: Programming the Web, 3rd Edition*.

## Profundización del lenguaje y modelos mentales
- Kyle Simpson — *You Don't Know JS Yet* (serie).

La serie se utiliza transversalmente para construir modelos mentales profundos del lenguaje, especialmente en:
- tipos, valores y coerción;
- scope, lexical scope y closures;
- funciones;
- `this`;
- objetos, prototypes y clases;
- asincronía y composición asíncrona;
- mecanismos fundamentales del lenguaje.

Su función es de profundización conceptual. No sustituye a ECMA-262 como referencia normativa. Cuando una explicación pedagógica, un libro y la especificación difieran, debe comprobarse la versión actual de ECMA-262 y la documentación oficial aplicable.

## Asincronía, concurrencia y runtime
- Thomas Hunter II, Bryan English — *Multithreaded JavaScript: Concurrency Beyond the Event Loop*.
- Kyle Simpson — *You Don't Know JS Yet*, para los fundamentos conceptuales de asincronía cubiertos por la serie.
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
- Bloques 11–15: mecanismos relacionados con iteración y asincronía cuando correspondan al contenido publicado de la serie.
- Bloque 22: preparación conceptual para estudiar la especificación; ECMA-262 sigue siendo la autoridad normativa.

## Política de uso de fuentes
La especificación y la documentación oficial prevalecen cuando una característica haya cambiado desde la publicación de un libro.

Las referencias exactas de capítulos, secciones o páginas solo deben incluirse cuando hayan sido verificadas. No se deben atribuir contenidos a un volumen de *You Don't Know JS Yet* que no estén presentes en la edición utilizada.
