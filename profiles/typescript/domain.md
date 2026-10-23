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

## Expresiones regulares aplicadas a TypeScript

Estudiar las APIs ECMAScript RegExp y String desde TypeScript: tipado de coincidencias, grupos opcionales, narrowing, Unicode, estado de RegExp, transformación de texto, validación de entradas, procesamiento de logs y pruebas. No duplicar el curso independiente de teoría y sintaxis Regex. Diferenciar siempre tipado estático de validación efectiva en runtime. Evaluar ReDoS, backtracking y mitigaciones sin presuponer que TypeScript cambia el motor Regex.

## Big O Notation aplicada a TypeScript

Analizar complejidad temporal, espacial, amortizada y de casos de algoritmos y colecciones utilizados desde TypeScript. Contrastar modelos asintóticos con mediciones reales, V8, memoria, concurrencia, workers, streams y backpressure. No duplicar el curso general de Big O: priorizar análisis de código TypeScript y del JavaScript emitido. Separar complejidad algorítmica de costes del compilador/type checker; no presentar complejidades de operaciones de colecciones como garantías normativas universales.

## Integración pedagógica transversal

Conectar Regex con los bloques 2, 24, 25, 30 y 36, y Big O con los bloques 17, 21, 27, 28, 29, 34 y 35. El proyecto final debe incorporar extracción de texto segura, pruebas de casos límite, análisis asintótico, benchmarks reproducibles y evaluación de memoria. Conservar la cobertura y los identificadores existentes; aclarar títulos repetidos y añadir prerrequisitos. Mantener la separación compile time/runtime.


## Progresión revisada y prerrequisitos

El nivel inicial es cero en TypeScript. El bloque 0 contiene un puente práctico
JavaScript para quien todavía no domina variables, control de flujo, funciones,
objetos, scope, closures, prototipos y this. El PATH de JavaScript permite ampliar
estos conocimientos, pero el alumno no debe esperar al bloque 23 para usarlos.
El bloque 23 profundiza en interoperabilidad, migración y análisis del emit.

Se conservan los bloques 0–45 y sus identificadores. El bloque 43 es el proyecto
progresivo. Los bloques 44 y 45 aportan especialización aplicada, y el bloque 46
contiene la entrega final. No presentar el bloque 43 como evaluación definitiva.

Las repeticiones deben cambiar de objetivo: introducción, aplicación, diagnóstico
o decisión de arquitectura. No generar dos explicaciones equivalentes de
sobrecargas, Awaited, project references o branded types.

## Ampliaciones del lenguaje

Estudiar varianza, límites de soundness, inferencia contextual, parámetros
const, NoInfer, ThisType, declaration merging y diferencias entre propiedades
opcionales y undefined. Mostrar con pruebas qué acepta y rechaza el compilador.
Distinguir readonly de inmutabilidad real y un branded type de una validación.

Incluir decoradores modernos y heredados como modelos distintos. Relacionar
using y await using con liberación de recursos, excepciones y cancelación;
no equiparar limpieza determinista con garbage collection.

## Compilación, resolución y ejecución

Comparar tsc, comprobación con noEmit y ejecución directa mediante eliminación
de tipos cuando la versión fijada de Node.js la soporte. La ejecución no sustituye
la comprobación estática. Registrar versiones exactas y verificar las restricciones
de sintaxis, extensiones, módulos y opciones en documentación oficial.

Elegir module y moduleResolution según el host. paths no reescribe por sí mismo
los imports emitidos. Comprobar paquetes desde consumidores ESM y CommonJS;
incluir declaraciones por formato y diagnóstico con traceResolution.

## Alcance aplicado de Regex y Big O

Cada lección del bloque 45 debe partir de código TypeScript o JavaScript emitido.
Los fundamentos generales se remiten al PATH de Big O. Árboles, heaps, grafos,
recurrencias y ordenación se conservan como aplicaciones, sin repetir cursos
teóricos. Explicitar tamaño de entrada, supuestos del motor, coste de callbacks,
trabajo total, latencia, memoria y comunicación entre workers.

En Regex comprobar capturas en runtime, estado de lastIndex, Unicode y límites
de entrada. En streams estudiar patrones que atraviesan chunks y decodificación.
No prometer que un temporizador interrumpe una regex síncrona en el mismo hilo.

## Evaluación y evidencia

Realizar checkpoints después de los bloques 6, 13, 16, 24, 30, 33, 39 y 45.
Cada checkpoint debe incluir un caso resuelto, un fallo diagnosticado y una
justificación. Usar pruebas positivas y negativas de tipos, tests runtime,
consumidores reales para paquetes y mediciones reproducibles para rendimiento.
La entrega final reúne las evidencias de los bloques 43–46.

## Convenciones de integración con course-generator

Ubicación prevista: paths/TypeScript/initial.txt y profiles/typescript/ para
profile.yaml, domain.md y bibliography.md. Desde profiles/typescript/,
../../config/pedagogy.md apunta a config/pedagogy.md en la raíz del repositorio.
Este archivo global es una dependencia existente y no se sustituye en este paquete.
Si se usa otra estructura, ajustar la ruta antes de generar.

La numeración del temario es bloque.lección, por ejemplo 7.13. Las claves
pedagógicas del perfil expresan requisitos de contenido; su carga como YAML no
prueba que el generador implemente cada clave. Verificar esa integración en el
repositorio de destino. No atribuir una ejecución del generador a esta revisión.
