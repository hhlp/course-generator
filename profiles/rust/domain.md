# Domain — Rust 0 → Experto en Profundidad

## Dominio

Programación en Rust moderna orientada a software seguro, concurrente, eficiente,
de sistemas y producción.

## Alcance

El curso cubre desde una persona sin conocimientos previos de Rust hasta un nivel
capaz de razonar sobre ownership, lifetimes, type system, concurrencia, atomics,
async/Futures, unsafe, FFI, performance y componentes internos del compilador, además de
integrar expresiones regulares idiomáticamente en aplicaciones Rust sin duplicar la teoría
de expresiones regulares cubierta por su PATH especializado.

## Áreas

1. Toolchain y ecosistema Rust
2. Sintaxis y fundamentos
3. Ownership, moves, borrowing y lifetimes
4. Algebraic data types y pattern matching
5. Collections, strings e I/O
6. Uso e integración de expresiones regulares desde Rust
7. Errors
8. Crates, modules y Cargo
9. Traits, generics y type system
10. Closures e iterators
11. Smart pointers e interior mutability
12. Memoria y data layout
13. Testing y documentación
14. Threads y synchronization
15. Atomics y Rust memory model
16. Async, Future y executors
17. Macros y procedural macros
18. Unsafe Rust y soundness
19. FFI
20. Diseño idiomático y type-driven design
21. Performance, benchmarking y profiling
22. Networking y systems programming
23. CLI, serialization y observability
24. Seguridad y supply chain
25. Cross compilation y no_std
26. Library/API design
27. Compiler internals
28. Debugging
29. Ingeniería profesional y proyectos

## Profundidad esperada

### Nivel inicial
Leer, escribir, compilar, probar y depurar programas sencillos entendiendo
ownership en lugar de limitarse a memorizar reglas del borrow checker.

### Nivel intermedio
Diseñar aplicaciones modulares usando traits, generics, iterators, error
handling, smart pointers, tests, threads y Cargo de manera idiomática.

### Nivel avanzado
Razonar sobre lifetimes complejos, type-driven APIs, async/Futures, atomics,
memory ordering, performance, FFI y unsafe.

### Nivel experto
Analizar soundness e invariants, construir abstracciones seguras sobre unsafe,
comprender HIR/MIR y aspectos de rustc, razonar sobre concurrencia de bajo nivel,
diseñar bibliotecas públicas estables y diagnosticar problemas de rendimiento,
memoria y concurrencia.

## Entorno recomendado

- Linux como plataforma principal
- Rust stable como toolchain predeterminado
- nightly sólo cuando una lección lo requiera explícitamente
- Cargo como sistema de build y dependencias
- rustfmt + Clippy como herramientas estándar
- rust-analyzer para soporte del editor
- Git para control de versiones

## Filosofía

El objetivo no es únicamente conseguir que el programa compile. Cada bloque debe
explicar por qué Rust acepta o rechaza el programa, qué invariantes están siendo
protegidas y qué coste temporal, espacial o arquitectónico implica cada decisión.

Safe Rust es la opción predeterminada. Unsafe debe aparecer después de dominar
ownership, borrowing, lifetimes, representación de memoria y APIs seguras.

La optimización debe estar respaldada por benchmarks y profiling.

## Política de expresiones regulares

Este PATH no sustituye al curso especializado de expresiones regulares. La sintaxis, teoría,
autómatas, construcción de patrones y dominio conceptual de regex pertenecen a ese PATH.
Aquí se enseña cómo usar ese conocimiento desde Rust: crates y APIs, compilación y reutilización
de patrones, Match/Captures, iteración, reemplazo, RegexSet, Unicode/bytes, errores, testing,
rendimiento, seguridad e integración con CLI, archivos, logs y aplicaciones reales.
