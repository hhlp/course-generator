# Domain — Rust 0 → Experto en Profundidad

## Dominio

Programación en Rust moderna orientada a software seguro, concurrente, eficiente,
de sistemas y producción.

## Alcance

El curso cubre desde una persona sin conocimientos previos de Rust hasta un nivel
capaz de razonar sobre ownership, lifetimes, type system, concurrencia, atomics,
async/Futures, unsafe, FFI, performance y componentes internos del compilador.

## Áreas

1. Toolchain y ecosistema Rust
2. Sintaxis y fundamentos
3. Ownership, moves, borrowing y lifetimes
4. Algebraic data types y pattern matching
5. Collections, strings e I/O
6. Errors
7. Crates, modules y Cargo
8. Traits, generics y type system
9. Closures e iterators
10. Smart pointers e interior mutability
11. Memoria y data layout
12. Testing y documentación
13. Threads y synchronization
14. Atomics y Rust memory model
15. Async, Future y executors
16. Macros y procedural macros
17. Unsafe Rust y soundness
18. FFI
19. Diseño idiomático y type-driven design
20. Performance, benchmarking y profiling
21. Networking y systems programming
22. CLI, serialization y observability
23. Seguridad y supply chain
24. Cross compilation y no_std
25. Library/API design
26. Compiler internals
27. Debugging
28. Ingeniería profesional y proyectos

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
