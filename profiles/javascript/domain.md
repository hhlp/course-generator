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

Los bloques 14 y 15 constituyen el núcleo. Los bloques 11, 12, 13, 17, 18, 20, 22, 26, 29 y 30 refuerzan el tema desde protocolos, módulos, errores, memoria, Node.js, testing, especificación, rendimiento y proyecto final.

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


## Base reproducible y versiones
- Runtime base: Node.js 24.x. Cada ejecución debe registrar versión exacta de Node.js, npm, V8, sistema y arquitectura. No fijar un parche inventado ni asumir que todos los 24.x incluyen las mismas APIs.
- Referencia normativa estable: ECMAScript 2025 (ECMA-262, 16.ª edición). El borrador vivo se consulta para extensiones posteriores y se identifica expresamente como tal.
- Para cada característica moderna: registrar edición o estado TC39, versión mínima verificada del runtime, soporte nativo o necesidad de flags y alternativa si falta soporte. Una entrada en la especificación no acredita disponibilidad en Node.js.
- Intl se contrasta con ECMA-402 y con los datos ICU del runtime. Las APIs de host se contrastan con Node.js y sus estándares aplicables.
- Iterator helpers, operaciones modernas de Set, groupBy, Promise.withResolvers/try, RegExp.escape, buffers redimensionables y disposición explícita se enseñan con esta política de compatibilidad.

## Orden pedagógico y prerrequisitos
Se conservan los bloques 0–30 y los identificadores originales. La numeración es un índice temático; las siguientes segundas pasadas son obligatorias:
- 6.38 y 6.44 se introducen como diseño; su práctica completa se realiza en el Bloque 18, después de archivos, streams y decodificación incremental.
- 6.39–6.40 anticipan criterios; los benchmarks se realizan en el Bloque 26. Los patrones adversariales se ejecutan con aislamiento y límites en el Bloque 28.
- 6.42 introduce casos de prueba; el fuzzing se realiza después de aprender testing en el Bloque 20.
- 11.13–11.15 son un panorama inicial. La implementación se retoma al final del Bloque 14 tras Promises y async/await.
- 12.14 introduce sintaxis; la evaluación de ciclos con top-level await se retoma después del Bloque 14.
- Antes de 15.35–15.42, estudiar 17.1–17.5 y las lecciones de vistas y representación binaria del Bloque 17; regresar después al bloque 15 para sincronización.
- El Bloque 15 es propietario del desarrollo de coordinación, carreras y Atomics. El 17 desarrolla representación, vistas, endianness y copias; utiliza enlaces al 15 para evitar repetir explicaciones.
- Los errores de ASI, igualdad, paso por valor, serialización y recursos deben aparecer explícitamente en ejemplos y evaluación.

## Diagnóstico y evolución del motor
Priorizar AsyncLocalStorage y Diagnostics Channel para contexto y diagnóstico de aplicaciones. Los hooks de bajo nivel se estudian para comprender y diagnosticar sistemas existentes, explicando las advertencias de la documentación oficial.
En V8, estudiar Ignition, Sparkplug, Maglev y el nivel optimizador superior con TurboFan/Turboshaft, registrando versión, plataforma y flags. No afirmar que toda función recorre todos los niveles.
WeakRef y FinalizationRegistry no ofrecen cierre determinista. La gestión explícita de recursos se estudia aparte, con limpieza, propagación de fallos y comprobación de soporte.

## Proyectos intermedios y evaluación
- Bloque 5: gestor de estado con factories y closures; justificar bindings, identidad y mutaciones.
- Bloque 12: biblioteca ESM; retomar su validación automatizada en el Bloque 20.
- Bloque 14: pipeline asíncrono; comprobar resultados, propagación de errores y límites antes de profundizar en cancelación.
- Bloque 18: CLI de archivos; manejar chunks, Unicode, backpressure, señales, fallos y cierre.
- Bloque 20: checkpoint de pruebas de biblioteca y CLI, con aislamiento y recursos liberados.
- Bloque 30: proyecto final integrador. Rúbrica de 100 puntos: corrección 25; diseño y explicación 15; pruebas 20; gestión de recursos y concurrencia 15; medición y complejidad 10; seguridad 10; reproducibilidad y documentación 5. Exigir al menos 80 y corregir fallos críticos de corrección o seguridad antes de aprobar.
Los laboratorios son obligatorios en los temas que los requieren; no todas las lecciones necesitan un laboratorio independiente. Las lecturas sí son obligatorias, con enlaces o referencias verificadas y sin inventar páginas.
