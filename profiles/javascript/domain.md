# JavaScript — Domain

## Alcance

Este dominio define un curso de JavaScript de 0 a experto centrado
primero en el lenguaje ECMAScript y sus modelos de ejecución, y después
en los runtimes, APIs, concurrencia, arquitectura y aplicaciones
multiplataforma.

El curso debe distinguir de forma explícita:

- ECMAScript como especificación del lenguaje.
- JavaScript como implementación/ecosistema.
- APIs del navegador como capacidades del host.
- Node.js como runtime fuera del navegador.
- Librerías y frameworks como capas construidas sobre JavaScript.

## Objetivo general

Llevar al estudiante desde sus primeros programas hasta la capacidad de
leer la especificación ECMAScript, razonar sobre el event loop, memoria
y concurrencia, diagnosticar rendimiento y diseñar sistemas JavaScript
profesionales.

## Ejes del dominio

### 1. Lenguaje

Sintaxis, tipos, coerción, operadores, control de flujo, strings,
números, arrays, objetos, colecciones, funciones, scope, closures,
prototypes, classes, iterables, generators, symbols, Proxy, Reflect,
RegExp y errores.

### 2. Modelo de ejecución

Execution contexts, lexical environments, call stack, jobs, tasks,
microtasks, event loop, Promises, async/await y scheduling.

### 3. Plataforma web

DOM, eventos, Web APIs, almacenamiento, Fetch, HTTP, CORS, WebSocket,
Server-Sent Events, Workers y seguridad del navegador.

### 4. Node.js

Runtime, V8/libuv, módulos, filesystem, buffers, events, HTTP, streams,
child processes, worker_threads, señales y aplicaciones CLI/servidor.

### 5. Concurrencia

Workers, message passing, structured clone, transferable objects,
SharedArrayBuffer, Atomics, sincronización, worker pools, backpressure y
arquitecturas asíncronas.

### 6. Internals

Especificación ECMAScript, abstract operations, realms, agents, internal
slots, motores JavaScript, parsing, bytecode, JIT, optimización,
deoptimización y garbage collection.

### 7. Ingeniería profesional

Testing, debugging, profiling, performance, seguridad, npm, tooling,
paquetes, arquitectura, diseño de APIs, observabilidad y CI/CD.

### 8. Aplicaciones

React, GraphQL, React Native y Electron se estudian como aplicación de
conocimientos JavaScript, sin sustituir el aprendizaje profundo del
lenguaje.

## Orden pedagógico

La progresión obligatoria es:

lenguaje → estructuras → funciones → objetos/prototipos → asincronía →
navegador/Node.js → event loop → concurrencia → internals → arquitectura
→ aplicaciones → proyecto experto.

No se debe adelantar React u otros frameworks antes de dominar
funciones, closures, objetos, módulos, Promises y asincronía.

## Profundidad esperada

Cada concepto debe explicar:

- qué es;
- qué problema resuelve;
- sintaxis y semántica;
- ejemplos ejecutables;
- comportamiento interno cuando sea relevante;
- errores frecuentes;
- diferencias entre alternativas;
- implicaciones de rendimiento o seguridad;
- casos de uso reales.

## Laboratorios

Los laboratorios deben favorecer JavaScript moderno y ejecutable. Cuando
una API dependa del host, indicar claramente si el ejemplo corresponde a
navegador, Node.js o ambos.

Los bloques avanzados deben incluir experimentos observables sobre event
loop, microtasks, workers, streams, memoria, garbage collection y
profiling.

## Límites con otros cursos

TypeScript se trata en un learning path separado. Aquí solo se
mencionará cuando ayude a delimitar JavaScript frente a un sistema de
tipos estático.

HTML y CSS solo se cubrirán en la medida necesaria para trabajar con DOM
y aplicaciones web. El objetivo no es convertir este curso en un curso
completo de frontend.

React, React Native, Electron y GraphQL son bloques de integración; no
deben desplazar el núcleo ECMAScript.

## Proyecto final

El proyecto debe integrar frontend, backend, asincronía, red, testing,
seguridad, rendimiento y observabilidad. Debe exigir además una
explicación técnica del event loop, memoria, concurrencia y principales
trade-offs arquitectónicos del sistema construido.
