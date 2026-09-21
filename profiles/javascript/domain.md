# JavaScript Core 0 → Experto — Dominio del curso

## Propósito

Este curso enseña JavaScript como lenguaje de programación, su estándar ECMAScript, su modelo de ejecución y sus mecanismos internos. La progresión parte de sintaxis y tipos y llega a especificación, parsing, AST, memoria, garbage collection, motores, V8, JIT, optimización y deoptimización.

El objetivo es que el estudiante pueda razonar sobre JavaScript independientemente de una interfaz web concreta y utilizarlo con solvencia en Node.js, scripting, automatización, herramientas y contextos como MongoDB.

## Principio rector

Distinguir siempre tres capas:

1. **ECMAScript / JavaScript Core**: sintaxis, tipos, objetos, funciones, módulos, Promises, semántica y algoritmos definidos por ECMA-262.
2. **Runtime/host**: capacidades proporcionadas por Node.js u otro host, como filesystem, timers, streams, procesos o networking.
3. **Motor**: implementación que analiza y ejecuta el lenguaje, como V8, SpiderMonkey o JavaScriptCore.

Nunca atribuir al lenguaje una API que pertenece al host.

## Alcance principal

- Léxico, sintaxis, statements y expressions.
- Variables, bindings, scope, hoisting y TDZ.
- Primitive values, objects, identidad, igualdad y coerción.
- Operadores y control de flujo.
- Funciones, callbacks, higher-order functions, recursion y closures.
- Strings, Unicode, Number, BigInt, Math, Date, Intl y RegExp.
- Arrays, TypedArrays y colecciones Map/Set/WeakMap/WeakSet.
- Objetos, property keys, descriptors, getters/setters y extensibilidad.
- `this`, constructor functions, prototypes, prototype chain y clases.
- Symbol, protocolos, iterables, iterators y generators.
- ECMAScript Modules.
- Error handling.
- Promises, async/await y composición asíncrona.
- Jobs, microtasks y modelo de concurrencia.
- Proxy, Reflect y metaprogramación.
- ArrayBuffer, SharedArrayBuffer, DataView y Atomics.
- Node.js como runtime de aplicación y experimentación.
- npm, paquetes y gestión básica de proyectos.
- Testing, debugging, linting y profiling.
- Diseño de librerías, CLIs y aplicaciones JavaScript.
- Lectura de ECMA-262 y abstract operations.
- Execution Contexts, Environment Records, Realms, Agents y internal methods.
- Parsing, AST, traversal, transforms, linters y codemods.
- Memory management y garbage collection.
- Motores JavaScript y arquitectura de V8.
- Ignition, bytecode, feedback, hidden classes/Maps, inline caches y TurboFan.
- JIT, optimization y deoptimization.
- Rendimiento basado en medición.
- Seguridad JavaScript/Node.js.
- JavaScript aplicado a scripting, datos y uso contextual con MongoDB.

## Node.js dentro del curso

Node.js está incluido porque proporciona un runtime práctico fuera del navegador. Se estudia como **host de JavaScript**, no como parte de ECMAScript.

Se permiten ejemplos con:

- `process`
- filesystem
- paths y URLs
- EventEmitter
- Buffer
- streams
- timers
- child processes
- worker threads
- networking y HTTP básico
- npm y package.json

Cuando una lección sea de JavaScript Core, el ejemplo debe depender de ECMAScript siempre que sea posible. Las APIs Node.js solo deben introducirse cuando la lección trate explícitamente del runtime o necesite un host para observar un comportamiento.

## MongoDB

MongoDB no es el objeto principal del curso. Puede utilizarse como contexto de aplicación para consolidar objetos, arrays, documentos, funciones, JSON/BSON y scripting.

El curso debe diferenciar con claridad:

- sintaxis y semántica JavaScript;
- sintaxis/documentos BSON;
- operadores y APIs propias de MongoDB;
- APIs de drivers o shells.

No convertir las lecciones JavaScript en un curso de MongoDB.

## Fuera de alcance

Este curso no enseña desarrollo frontend. Excluir:

- HTML como lenguaje de marcado;
- CSS;
- DOM;
- BOM;
- `window` y `document`;
- manipulación de elementos HTML;
- eventos específicos del navegador;
- formularios HTML;
- Web Storage;
- Canvas, WebGL y otras Browser APIs;
- React;
- Vue;
- Angular;
- frameworks frontend.

Si una fuente utiliza el navegador para ilustrar un concepto, adaptar el ejemplo a JavaScript Core o Node.js cuando sea técnicamente posible.

## Profundidad esperada

### Inicial

El estudiante puede escribir y ejecutar programas sencillos y comprende valores, variables, operadores, control de flujo, funciones, arrays y objetos.

### Intermedio

Comprende scope, closures, `this`, prototypes, classes, collections, modules, errors y programación asíncrona.

### Avanzado

Comprende descriptors, protocols, generators, Proxy/Reflect, concurrency, binary data, diseño, testing, profiling y seguridad.

### Experto

Puede leer secciones relevantes de ECMA-262, explicar execution contexts y environment records, trabajar con AST, razonar sobre memoria/GC y analizar el comportamiento de motores modernos sin confundir detalles de implementación con garantías del estándar.

## Reglas de precisión

- Distinguir siempre estándar de implementación.
- No presentar detalles de V8 como reglas universales de JavaScript.
- No enseñar `var` mediante el mito simplificado de que "sube la variable"; explicar bindings y fases de instanciación progresivamente.
- Diferenciar job/microtask definido o relacionado con ECMAScript de las colas y fases propias del host.
- No afirmar optimizaciones del motor sin fuente técnica o medición.
- Evitar micro-optimizaciones basadas en folklore.
- Explicar coerción mediante operaciones abstractas cuando el nivel de la lección lo permita.
- Tratar `class` en relación con el modelo prototípico.
- Diferenciar shallow copy de deep copy.
- No equiparar JSON con JavaScript ni BSON con JSON.

## Práctica y laboratorios

Priorizar programas ejecutables con Node.js, pequeños módulos ESM, tests, scripts CLI, transformaciones de datos, experimentos de asincronía, profiling y herramientas AST.

Los laboratorios avanzados deben incluir observación y explicación, no solo código: formular hipótesis, ejecutar, medir, interpretar y relacionar el resultado con ECMAScript, el runtime o el motor correspondiente.

## Proyecto final

El proyecto final debe integrar lenguaje, módulos, asincronía, streams o procesamiento incremental, testing, debugging, seguridad y profiling. Debe incluir al menos un ejercicio de AST y uno de análisis de runtime/motor, manteniendo las dependencias de host claramente separadas del JavaScript Core.

## Política de bibliografía mixta

Algunas fuentes principales del curso también cubren desarrollo web o frameworks. Esto no amplía el dominio del path. `JavaScript Cookbook, 3rd Edition` y `JavaScript Everywhere`, por ejemplo, pueden utilizarse para JavaScript Core, Node.js, arquitectura, tooling o concurrencia cuando corresponda, mientras que DOM, HTML, CSS, React y React Native permanecen fuera del alcance. El material excluido se reserva para futuros paths especializados.

`Multithreaded JavaScript` se utiliza como fuente avanzada para reforzar la progresión desde event loop y asincronía hacia worker threads, procesos, shared memory, `SharedArrayBuffer` y `Atomics`, distinguiendo las características ECMAScript de las APIs específicas del host.
