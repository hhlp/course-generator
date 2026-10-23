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

## Documentación oficial y especificaciones

### TypeScript Handbook
Guía oficial principal para sintaxis, tipos, narrowing, generics, type manipulation, clases, módulos y declaration files.

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


## Enlaces de documentación y correspondencia con el temario

| Fuente | Enlace | Uso principal |
| --- | --- | --- |
| TypeScript Handbook | https://www.typescriptlang.org/docs/handbook/intro.html | Bloques 0–13 y 20–24; guía oficial, no especificación completa |
| Compatibilidad de tipos | https://www.typescriptlang.org/docs/handbook/type-compatibility.html | Bloques 6–7 y 41; límites de soundness y bivarianza |
| Generics | https://www.typescriptlang.org/docs/handbook/2/generics.html | Bloque 7; inferencia y varianza |
| TSConfig | https://www.typescriptlang.org/tsconfig/ | Bloques 0, 14 y 16; opciones según versión |
| Modules Reference | https://www.typescriptlang.org/docs/handbook/modules/reference.html | Bloques 14, 25 y 33; resolución y formatos |
| TypeScript 5.0 | https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html | Decoradores y parámetros genéricos const |
| TypeScript 5.2 | https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html | using, await using y protocolos de disposición |
| TypeScript 5.4 | https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-4.html | NoInfer |
| Ejecución TS en Node.js | https://nodejs.org/api/typescript.html | Bloque 25; type stripping y restricciones |
| Node.js API | https://nodejs.org/api/ | Bloques 17–19 y 25–28; runtime y recursos |
| Compiler API | https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API | Bloques 37–39; contrastar con versión instalada |
| Rendimiento de TypeScript | https://github.com/microsoft/TypeScript/wiki/Performance | Bloques 32, 34 y 45 |
| ECMA-262 | https://tc39.es/ecma262/ | Semántica JavaScript y RegExp |
| MDN RegExp | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp | Consulta complementaria del bloque 44 |
| OWASP ReDoS | https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS | Bloques 36 y 44 |
| V8 | https://v8.dev/ | Bloques 28–29 y 35; detalles dependientes de versión |

Las notas de versiones antiguas identifican el origen de características; no
fijan la versión del curso. Registrar el compilador y runtime usados en cada
laboratorio y contrastar documentación, declaraciones instaladas y ejecución.

## Uso de los libros por etapa

- Learning TypeScript: apoyo de fundamentos y progresión inicial.
- Effective TypeScript: criterio de diseño y revisión de APIs y tipos.
- Programming TypeScript: contraste de modelos y diseño avanzado.
- TypeScript Quickly: ejercicios e integración de aplicaciones.
- Los títulos complementarios de JavaScript, concurrencia y algoritmos se usan
  solo donde aporten contexto a un laboratorio TypeScript.

No se asignan capítulos, páginas ni ediciones no verificadas. Al utilizar un
libro concreto, registrar la edición consultada y contrastar ejemplos antiguos
con el compilador fijado. La documentación oficial prevalece para comportamiento
actual; ECMA-262 es la referencia normativa de la semántica JavaScript.
