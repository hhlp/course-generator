# TypeScript — Bibliografía

## Bibliografía principal

### Effective TypeScript — Dan Vanderkam
Referencia principal para desarrollar criterio práctico sobre el sistema de tipos, inferencia, diseño de APIs, generics, evolución de tipos y uso efectivo de TypeScript.

### Learning TypeScript — Josh Goldberg
Base pedagógica para fundamentos, sistema de tipos, funciones, objetos, clases, narrowing, generics, declaration files y configuración del compilador.

### Programming TypeScript — Boris Cherny
Referencia para profundizar en diseño de tipos, funciones, generics, programación asíncrona y construcción de aplicaciones TypeScript.

### TypeScript Quickly — Yakov Fain y Anton Moiseev
Apoyo práctico para desarrollo de aplicaciones, tooling y adopción de TypeScript.

## Referencias normativas y oficiales

### TypeScript Handbook
Referencia normativa-práctica principal para sintaxis, tipos, narrowing, generics, type manipulation, clases, módulos y declaration files.

### TypeScript TSConfig Reference
Referencia para opciones del compilador y configuración de proyectos.

### TypeScript Compiler API / TypeScript Wiki / código fuente de TypeScript
Referencia para internals, AST, Program, SourceFile, Symbols, TypeChecker, transformations, Language Service y herramientas propias.

### ECMAScript Language Specification — ECMA-262
Referencia normativa para la semántica JavaScript subyacente.

### TC39
Referencia para propuestas y evolución de ECMAScript.

### Node.js Documentation
Referencia para runtime Node.js, event loop, streams, buffers, worker_threads, child_process, diagnostics, performance y APIs de plataforma.

### MDN Web Docs
Referencia complementaria para APIs ECMAScript y Web Platform, Promises, iterators, Web Workers, SharedArrayBuffer, Atomics y seguridad web.

## Bibliografía complementaria por dominio

### JavaScript: The Definitive Guide — David Flanagan
Apoyo para semántica JavaScript, objetos, funciones, módulos, asincronía y APIs del lenguaje.

### You Don't Know JS Yet — Kyle Simpson
Profundización conceptual en scope, closures, tipos, coerción, objetos y comportamiento del runtime JavaScript.

### Multithreaded JavaScript: Concurrency Beyond the Event Loop — Thomas Hunter II y Bryan English
Referencia complementaria para concurrencia, Worker Threads, Web Workers, SharedArrayBuffer, Atomics y paralelismo.

## Uso de las fuentes

- Los cuatro libros TypeScript constituyen la bibliografía pedagógica base.
- La documentación oficial de TypeScript prevalece para comportamiento actual del compilador y del sistema de tipos.
- ECMA-262 se usa cuando la cuestión pertenece a la semántica JavaScript.
- Node.js Documentation se usa para comportamiento específico del runtime Node.js.
- Las referencias exactas de capítulos o secciones solo deben indicarse cuando hayan sido verificadas.
- No atribuir a un libro contenido que no se haya comprobado directamente.

## Referencias específicas: Regex en TypeScript

### MDN — RegExp y métodos String de ECMAScript
Consulta de APIs `RegExp`, `test`, `exec`, `match`, `matchAll`, `replace`, `replaceAll`, `search` y `split`, flags, Unicode y comportamiento de `lastIndex`.

### ECMAScript ECMA-262 — RegExp
Referencia normativa para semántica de patrones, operaciones y coincidencias en runtime; verificar edición y compatibilidad del motor antes de afirmar soporte.

### OWASP — Regular expression Denial of Service (ReDoS)
Referencia complementaria de seguridad para backtracking, patrones vulnerables y mitigaciones.

Los libros del curso independiente de Regex no se incorporan a esta bibliografía.

## Referencias específicas: Big O aplicada a TypeScript

### Introduction to Algorithms — Cormen, Leiserson, Rivest y Stein
Consulta complementaria para notación asintótica, recurrencias, análisis amortizado, estructuras de datos y algoritmos; aplicar estos conceptos a ejemplos TypeScript, sin duplicar el path general.

### Node.js Documentation — Diagnostics y Performance
Medición de CPU, memoria, event loop, workers y benchmarking en Node.js.

### TypeScript Wiki — Performance
Diagnóstico del coste de type checking, organización de proyectos, tipos complejos y optimización del compilador.

### V8 Documentation / V8 Blog
Contexto de optimizaciones del motor, GC y efectos del runtime que no pueden deducirse únicamente de Big O.
