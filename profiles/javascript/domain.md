# Domain — JavaScript 0 → Experto

## Alcance
Curso profundo de JavaScript moderno centrado en el lenguaje y en su ejecución fuera del navegador, con Node.js como runtime principal. Parte desde cero y termina en semántica ECMAScript, asincronía, concurrencia y paralelismo avanzados, memoria compartida, motores, AST, profiling, seguridad y diseño de software.

## Objetivos de dominio
El alumno debe poder:
- razonar sobre tipos, coerción, scope, closures, prototypes, clases, módulos e iteración;
- construir modelos mentales correctos de los mecanismos fundamentales de JavaScript;
- leer y utilizar Promises, async/await, async iterators y streams correctamente;
- explicar Event Loop, Jobs, microtasks y diferencias entre lenguaje y host;
- distinguir asincronía, concurrencia y paralelismo;
- diseñar cancelación, timeouts, límites de concurrencia, queues, producer/consumer y backpressure;
- utilizar Worker Threads, message passing, transferables, SharedArrayBuffer y Atomics;
- reconocer race conditions, starvation, deadlock/livelock y problemas CPU-bound;
- comprender Node.js, V8/libuv y mecanismos de contexto/diagnóstico asíncrono;
- leer ECMA-262 y conectar sintaxis con abstract operations, execution contexts, Jobs y Agents;
- trabajar con binary data, memoria, GC, V8, JIT, profiling y deoptimization;
- analizar y transformar JavaScript mediante AST;
- escribir, probar, depurar, perfilar y asegurar proyectos JavaScript reales.

## Eje conceptual del lenguaje
El curso debe distinguir tres niveles de explicación:
1. Modelo pedagógico: intuiciones y explicaciones que facilitan comprender el comportamiento.
2. Modelo conceptual profundo: especialmente apoyado por *You Don't Know JS Yet* para scope, closures, `this`, objetos, prototypes, tipos, coerción y otros mecanismos fundamentales.
3. Modelo normativo: ECMA-262 define formalmente el comportamiento del lenguaje.

Los modelos pedagógicos no deben presentarse como si fueran mecanismos literales de la especificación. En niveles avanzados se debe conectar progresivamente la intuición con los conceptos normativos reales.

## Eje especial: asincronía y concurrencia
La materia no termina en async/await. La progresión requerida es:
callbacks → Promises → async/await → composición concurrente → Event Loop → cancelación/timeouts → concurrency limits → queues/backpressure → workers → message passing → shared memory/Atomics → problemas clásicos de concurrencia → Agents/Agent Clusters → diagnóstico y profiling.

Los bloques 14 y 15 constituyen el núcleo. Los bloques 11, 12, 13, 17, 18, 20, 22, 26 y 29 refuerzan el tema desde protocolos, módulos, errores, memoria, Node.js, testing, especificación, rendimiento y proyecto final.

## Eje especial: Big O aplicado a JavaScript
El Bloque 27 analiza complejidad temporal y espacial sobre código y APIs reales de JavaScript. No sustituye ni repite el learning path general de Big O. Debe distinguir complejidad asintótica, garantías de ECMAScript, costes esperados de implementación y medidas empíricas en Node.js/V8. Se incluyen bucles, recursión, colecciones, strings, algoritmos, memoria, benchmarks, profiling y laboratorios de refactorización.

## Eje especial: Regex aplicado a JavaScript
Las lecciones 6.15–6.45 se centran en la API `RegExp`, integración con `String`, flags, estado `lastIndex`, Unicode, construcción segura, testing, procesamiento de logs y rendimiento/ReDoS. Los fundamentos matemáticos y la teoría general de regex corresponden al path independiente. No incorporar sus libros especializados a esta bibliografía. Verificar disponibilidad de flags y métodos en el Node.js objetivo; no asumir compatibilidad universal.

## Estrategia bibliográfica
- *Head First JavaScript Programming*: introducción pedagógica.
- *JavaScript: The Definitive Guide*: cobertura general y referencia.
- *JavaScript Cookbook*: práctica y resolución de problemas.
- *You Don't Know JS Yet*: profundización conceptual y modelos mentales.
- *Multithreaded JavaScript*: concurrencia y paralelismo.
- ECMA-262/TC39: autoridad normativa.
- Node.js: comportamiento y APIs del runtime.
- V8: implementación, motor, memoria y optimización.

Una fuente conceptual nunca sustituye a la especificación cuando la lección estudia semántica normativa.

## Límites
- No convertir el curso en un curso de frontend, React u otros frameworks.
- Las APIs del navegador pueden aparecer para explicar estándares o contrastes, pero no son el eje.
- Node.js debe distinguirse claramente de ECMAScript.
- MongoDB se usa como aplicación de JavaScript; su lenguaje de consulta no debe confundirse con la semántica del lenguaje.
- TypeScript pertenece a su learning path independiente.
- Evitar micro-optimizaciones sin medición.
- Mantener separados los paths generales de Big O y Regex; estudiar aquí únicamente su aplicación a JavaScript.
- No presentar modelos pedagógicos como descripciones literales del funcionamiento interno.

## Práctica
Cada tema importante debe incluir ejemplos ejecutables y, cuando aporte valor, laboratorios. Los temas de scope, closures, `this`, prototypes y asincronía deben incluir ejercicios que confronten predicciones del alumno con el comportamiento real.

Los temas de concurrencia deben incluir experimentos observables sobre orden de ejecución, microtasks, bloqueo del Event Loop, cancelación, límites de concurrencia, backpressure, workers, race conditions y Atomics.

Los laboratorios de Big O deben exigir estimación, medición y justificación de costes; los de regex deben cubrir APIs, Unicode, estados, casos límite y ReDoS.

## Nivel experto
El dominio experto implica poder explicar un comportamiento desde varias capas:
código fuente → modelo conceptual → semántica ECMAScript → runtime/host → Event Loop/concurrencia → motor/memoria → medición y diagnóstico.
