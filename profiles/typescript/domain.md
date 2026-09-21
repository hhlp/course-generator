# Dominio — TypeScript

## Propósito

Este curso desarrolla TypeScript desde fundamentos hasta nivel experto, con énfasis en comprender el sistema de tipos, su relación con JavaScript, el compilador y el diseño de software type-safe.

El objetivo no es aprender un framework concreto. React, Angular, Vue, NestJS y otros ecosistemas quedan fuera del núcleo para que TypeScript sea estudiado como lenguaje, herramienta de análisis estático y plataforma de diseño de APIs.

## Alcance

El curso cubre:

- fundamentos de JavaScript necesarios para comprender TypeScript;
- inferencia y anotación de tipos;
- tipos primitivos, objetos, arrays, tuples, unions e intersections;
- interfaces y aliases;
- narrowing y control-flow analysis;
- funciones, clases y orientación a objetos;
- generics y constraints;
- keyof, typeof e indexed access types;
- mapped types;
- conditional types e infer;
- template literal types;
- utility types;
- módulos ESM/CommonJS y resolución de módulos;
- declaration files y publicación de tipos;
- tsconfig y opciones estrictas;
- asincronía, iteradores y generadores;
- diseño de errores type-safe;
- type-level programming;
- diseño de APIs type-safe;
- interoperabilidad y migración desde JavaScript;
- validación de datos en runtime;
- Node.js con TypeScript;
- testing y type testing;
- tooling, linting, build y CI;
- monorepos y project references;
- creación y publicación de librerías;
- rendimiento del compilador;
- internals del compilador;
- Compiler API, AST, Symbols y TypeChecker;
- patrones, antipatrones y prácticas de Effective TypeScript;
- proyecto final integrador.

## Principios

### TypeScript no sustituye el runtime

Los tipos se comprueban principalmente durante el desarrollo y la compilación. Los datos externos continúan necesitando validación en runtime.

### Comprender JavaScript

TypeScript conserva la semántica fundamental de JavaScript. El alumno debe distinguir siempre:

- comportamiento JavaScript en runtime;
- información disponible para el compilador;
- inferencia estática;
- código emitido.

### Strict por defecto

Los ejemplos y laboratorios deben favorecer configuraciones estrictas y explicar cualquier relajación deliberada.

### Preferir modelado a assertions

Se priorizan:

- narrowing;
- discriminated unions;
- generics bien restringidos;
- unknown;
- validación en fronteras;
- exhaustiveness checking;

antes que el uso indiscriminado de `any`, assertions o non-null assertions.

### Type-level programming con propósito

Los tipos avanzados se enseñan para mejorar seguridad, expresividad y reutilización, no para maximizar complejidad.

## Fuera de alcance principal

No son objetivos centrales:

- React;
- Angular;
- Vue;
- Svelte;
- NestJS;
- frameworks frontend/backend concretos;
- CSS y diseño web;
- administración avanzada de bases de datos.

Pueden aparecer ejemplos pequeños cuando sean necesarios para explicar interoperabilidad, módulos, APIs o librerías.

## Entorno recomendado

- TypeScript estable actual.
- Node.js en una versión soportada.
- npm como referencia básica de gestión de paquetes.
- Git.
- editor con soporte de TypeScript Language Service.
- Linux/Fedora como entorno preferente para laboratorios de CLI y tooling.

## Resultado esperado

Al finalizar, el alumno debe poder leer, escribir, depurar y diseñar TypeScript avanzado; construir APIs type-safe; mantener proyectos estrictos y grandes; publicar librerías correctamente tipadas; diagnosticar problemas del compilador; y utilizar el Compiler API para inspeccionar código y tipos.
