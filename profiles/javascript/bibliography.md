# Bibliografía — JavaScript Core 0 → Experto

## Criterio

La bibliografía combina libros de lenguaje con fuentes normativas y documentación de runtime/motor. Para detalles cambiantes de ECMAScript, Node.js y V8, la documentación oficial prevalece sobre explicaciones históricas de libros.

## Principal — lenguaje

### Marijn Haverbeke — *Eloquent JavaScript*
Útil para fundamentos, funciones, objetos, estructuras de datos, programación funcional, asincronía y diseño de programas. Los capítulos orientados específicamente al navegador no forman parte de este path.

### Kyle Simpson — *You Don't Know JS Yet* (serie)
Fuente de profundización para scope, closures, tipos, coerción, objetos, clases y mecanismos del lenguaje. Contrastar terminología especialmente interna con ECMA-262 cuando sea necesario.

### David Flanagan — *JavaScript: The Definitive Guide*
Referencia general extensa del lenguaje y del ecosistema. Utilizar selectivamente las partes de JavaScript Core y Node.js; omitir DOM/browser cuando no corresponda al dominio.

## Profundización y diseño

### Douglas Crockford — *JavaScript: The Good Parts*
Fuente histórica útil para comprender decisiones de diseño y evolución de prácticas JavaScript. No tratar sus recomendaciones como descripción del JavaScript moderno ni como normativa actual.

### Eric Elliott — *Programming JavaScript Applications*
Apoyo para composición, diseño modular y arquitectura. Usar críticamente y contrastar con prácticas modernas de módulos y runtime.

## Asincronía y Node.js

### Mario Casciaro y Luciano Mammino — *Node.js Design Patterns*
Fuente de profundización para asincronía, eventos, streams, patrones y arquitectura de aplicaciones Node.js.

### Documentación oficial de Node.js
Fuente primaria para APIs del runtime, ESM/CommonJS, event loop de Node.js, streams, Buffer, worker threads, process, filesystem, test runner y tooling.

https://nodejs.org/docs/latest/api/

## Normativa — ECMAScript

### ECMA International — *ECMA-262: ECMAScript Language Specification*
Fuente normativa principal para sintaxis, tipos, abstract operations, execution contexts, environment records, objects, internal methods, modules, Promises, jobs y semántica del lenguaje.

https://tc39.es/ecma262/

### TC39 — Proposals
Fuente primaria para estudiar la evolución del lenguaje y distinguir características estandarizadas de propuestas en distintas etapas.

https://github.com/tc39/proposals

### TC39 — How We Work / proceso
Apoyo para comprender stages, especificación y evolución de ECMAScript.

https://tc39.es/

## Consulta del lenguaje

### MDN Web Docs — JavaScript Guide / JavaScript Reference
Referencia práctica para sintaxis y built-ins de JavaScript. Usar las páginas del lenguaje; no introducir DOM o Browser APIs salvo para señalar que pertenecen a otro dominio.

https://developer.mozilla.org/docs/Web/JavaScript

## Motores e internals

### V8 Documentation
Fuente primaria para arquitectura y características del motor V8.

https://v8.dev/docs

### V8 Blog
Fuente técnica para parsing, Ignition, TurboFan, garbage collection, performance y cambios internos. Los detalles descritos son de implementación y pueden cambiar.

https://v8.dev/blog

### V8 — *JavaScript engine fundamentals* y artículos técnicos relacionados
Usar para shapes/hidden classes, inline caches y optimización, siempre marcando que son detalles del motor.

### SpiderMonkey Documentation
Fuente complementaria para comparar implementaciones y evitar asumir que V8 define JavaScript.

https://firefox-source-docs.mozilla.org/js/

## Parsing y AST

### ESTree Specification
Convención ampliamente utilizada para representar AST JavaScript en tooling. No confundir ESTree con una parte normativa de ECMAScript.

https://github.com/estree/estree

### Babel Parser / Babel Handbook y documentación
Fuente práctica para parsing, traversal y transformaciones AST.

https://babeljs.io/docs/babel-parser

### ESLint Developer Documentation
Referencia práctica para reglas y análisis estático basado en AST.

https://eslint.org/docs/latest/extend/

## Testing y tooling

### Node.js Test Runner Documentation
Fuente primaria para laboratorios de testing sin obligar al estudiante a adoptar inicialmente un framework externo.

https://nodejs.org/api/test.html

### ESLint Documentation
Referencia para análisis estático y configuración moderna.

https://eslint.org/docs/latest/

## Seguridad

### OWASP — NodeJS Security Cheat Sheet
Referencia complementaria para riesgos y controles de aplicaciones Node.js. Adaptar al alcance concreto de cada lección.

https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html

## MongoDB como contexto de aplicación

### MongoDB Documentation
Fuente oficial cuando una lección utilice JavaScript en shells, drivers o ejemplos de documentos/consultas. Las APIs MongoDB deben identificarse como APIs del producto, no como JavaScript Core.

https://www.mongodb.com/docs/

## Jerarquía de fuentes

Para cuestiones de semántica del lenguaje:

1. ECMA-262.
2. Propuestas/notas oficiales TC39 cuando proceda.
3. Documentación técnica del runtime o motor para comportamiento específico de implementación.
4. MDN y documentación de herramientas para consulta práctica.
5. Libros para explicación pedagógica, diseño y contexto.

Para Node.js, V8, ESLint, Babel o MongoDB, priorizar su documentación oficial actual cuando una funcionalidad pueda haber cambiado desde la publicación de un libro.

## Política de referencias por lección

La sección `📚 LECTURA` debe utilizar únicamente referencias que puedan asociarse de forma razonable con el contenido de la lección. No inventar capítulos, páginas o secciones exactas. Las referencias exactas solo deben darse cuando hayan sido verificadas.

## Bibliografía incorporada del plan original

### Eric Freeman y Elisabeth Robson — *Head First JavaScript Programming: A Learner's Guide to Modern JavaScript, Second Edition*
Fuente pedagógica principal para introducir y consolidar fundamentos del lenguaje, funciones, objetos, arrays, closures y programación JavaScript moderna. Utilizar sus explicaciones progresivas y ejercicios cuando encajen con JavaScript Core; cualquier contenido específico del navegador debe quedar fuera de este path.

### Adam D. Scott, Matthew MacDonald et al. — *JavaScript Cookbook: Programming the Web, Third Edition*
Fuente práctica basada en recetas. Utilizar selectivamente las recetas aplicables a JavaScript Core, estructuras de datos, módulos, asincronía, Node.js, tooling y técnicas generales del lenguaje. El título y parte del contenido están orientados a la Web: DOM, HTML, CSS y Browser APIs se reservan para el futuro path web.

### Adam D. Scott — *JavaScript Everywhere: Building Cross-Platform Applications with GraphQL, React, React Native, and Electron*
Fuente complementaria para observar JavaScript como lenguaje utilizado en distintos runtimes y arquitecturas. En este curso se permiten las partes útiles para JavaScript/Node.js, módulos, tooling, backend y arquitectura. React, React Native y demás contenido frontend quedan explícitamente fuera del alcance actual y podrán reutilizarse en paths posteriores.

### Thomas Hunter II y Bryan English — *Multithreaded JavaScript: Concurrency Beyond the Event Loop*
Fuente avanzada principal para concurrencia y paralelismo fuera del modelo asíncrono básico: worker threads, child processes, shared memory, `SharedArrayBuffer`, `Atomics` y patrones de concurrencia. Distinguir siempre las primitivas ECMAScript de las APIs proporcionadas por Node.js u otros hosts.

### David Flanagan — *JavaScript: The Definitive Guide, Seventh Edition*
Referencia principal de lenguaje y consulta. Ya forma parte de esta bibliografía y se mantiene explícitamente en su 7.ª edición. Utilizar las secciones de JavaScript Core, módulos, asincronía y Node.js que correspondan; reservar DOM y APIs del navegador para el futuro path web.

## Política de uso parcial de libros

Un libro no se elimina por contener capítulos fuera del alcance del curso. Se seleccionan únicamente las partes compatibles con JavaScript Core, ECMAScript, Node.js, concurrencia, tooling, runtime e internals. Esto permite conservar la bibliografía original sin introducir prematuramente HTML, CSS, DOM, Browser APIs o frameworks frontend.
