# TypeScript — Domain

## Propósito

Este curso lleva TypeScript desde fundamentos hasta un nivel experto, sin tratarlo como un lenguaje aislado de JavaScript. El alumno debe comprender simultáneamente el sistema de tipos estático, el compilador y el runtime JavaScript que finalmente ejecuta el programa.

## Objetivo global

Dominar TypeScript desde la semántica de JavaScript y ECMAScript hasta su sistema de tipos, Node.js, asincronía, concurrencia, paralelismo, memoria y runtime, diseño type-safe, compilador, AST, TypeChecker, Compiler API, rendimiento y seguridad, comprendiendo tanto compile time como runtime.

## Principios del dominio

- TypeScript añade análisis estático; no sustituye la semántica de JavaScript.
- Los tipos se eliminan durante la compilación salvo construcciones con efecto de emit.
- Compile time y runtime deben estudiarse como capas diferentes.
- El código JavaScript emitido debe inspeccionarse durante el aprendizaje.
- La seguridad de tipos no equivale a validación ni seguridad en runtime.
- Asincronía, concurrencia y paralelismo son conceptos diferentes.
- El rendimiento del type checker y el rendimiento del programa son problemas diferentes.
- El nivel experto incluye comprender compiler internals, AST, TypeChecker, Language Service y Compiler API.

## Ejes de aprendizaje

### Lenguaje y tipos
Inferencia, anotaciones, objetos, funciones, clases, narrowing, generics, mapped types, conditional types, template literal types, utility types y type-level programming.

### JavaScript y ECMAScript
Semántica JavaScript relevante, ECMAScript, TC39, target, lib, downleveling, interoperabilidad y análisis del JavaScript emitido.

### Runtime y Node.js
Node.js, módulos, streams, events, buffers, procesos, HTTP, event loop y comportamiento real del runtime.

### Asincronía, concurrencia y paralelismo
Promises, async/await, microtasks, libuv, worker threads, Web Workers, message passing, SharedArrayBuffer, Atomics, sincronización, backpressure y cancelación.

### Memoria y motores
Stack, heap, allocation, reachability, garbage collection, memory leaks, V8, JIT, hidden classes, inline caches, optimización y deoptimization.

### Compilador e internals
Scanner, parser, AST, binder, symbols, type checker, control-flow analysis, transformations, emit, Language Service y tsserver.

### Compiler API y tooling
Traversal de AST, TypeChecker API, diagnostics, transformations, code generation, linters, codemods y herramientas estáticas.

### Rendimiento
Performance del compilador, complejidad de tipos, tracing, profiling CPU/heap, event-loop metrics, benchmarking y optimización basada en mediciones.

### Seguridad
Trust boundaries, unknown, runtime validation, injections, prototype pollution, XSS, CSRF, SSRF, path traversal, ReDoS, dependencias y supply chain.

### Arquitectura
Diseño de APIs type-safe, domain modeling, librerías, monorepos, boundaries, compatibilidad, versionado y evolución de sistemas grandes.

## Relación con el curso de JavaScript

El curso de JavaScript es la referencia principal para estudiar exhaustivamente la semántica y el runtime del lenguaje. Este curso recupera y profundiza los aspectos JavaScript que afectan directamente al diseño, compilación, ejecución, depuración, rendimiento y seguridad de programas TypeScript, evitando convertir TypeScript en una simple repetición del curso JavaScript.

## Resultado esperado

Al terminar, el alumno debe ser capaz de:

- Diseñar software TypeScript estricto y mantenible.
- Razonar sobre inferencia, assignability y control-flow analysis.
- Construir tipos y APIs avanzadas sin complejidad accidental.
- Diferenciar garantías estáticas de garantías de runtime.
- Comprender el JavaScript generado y su ejecución.
- Diseñar aplicaciones Node.js asíncronas y concurrentes.
- Utilizar workers cuando exista trabajo CPU-bound paralelizable.
- Diagnosticar problemas de memoria y rendimiento.
- Analizar el compilador y utilizar Compiler API, AST y TypeChecker.
- Diseñar y publicar librerías TypeScript.
- Trabajar con monorepos y proyectos de gran escala.
- Diseñar fronteras de seguridad y validar datos externos.
- Construir herramientas propias de análisis estático.
