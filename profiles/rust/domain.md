# Domain — Rust 0 → Experto en Profundidad

## Dominio

Programación en Rust moderna orientada a software seguro, concurrente, eficiente,
de sistemas y producción.

## Alcance

El curso cubre desde una persona sin conocimientos previos de Rust hasta un nivel
capaz de razonar sobre ownership, lifetimes, type system, concurrencia, atomics,
async/Futures, unsafe, FFI, performance y componentes internos del compilador, además de
integrar expresiones regulares idiomáticamente en aplicaciones Rust sin duplicar la teoría
de expresiones regulares cubierta por su PATH especializado, y aplicar análisis Big-O al código,
colecciones y algoritmos Rust sin sustituir el PATH general de complejidad algorítmica.

## Áreas

1. Toolchain y ecosistema Rust
2. Sintaxis y fundamentos
3. Ownership, moves, borrowing y lifetimes
4. Algebraic data types y pattern matching
5. Collections, strings e I/O
6. Uso e integración de expresiones regulares desde Rust
7. Aplicación de Big-O y análisis de complejidad en código Rust
8. Errors
9. Crates, modules y Cargo
10. Traits, generics y type system
11. Closures e iterators
12. Smart pointers e interior mutability
13. Memoria y data layout
14. Testing y documentación
15. Threads y synchronization
16. Atomics y Rust memory model
17. Async, Future y executors
18. Macros y procedural macros
19. Unsafe Rust y soundness
20. FFI
21. Diseño idiomático y type-driven design
22. Performance, benchmarking y profiling
23. Networking y systems programming
24. Desarrollo profesional de CLI/TUI en Fedora: clap, terminales, procesos, configuración, seguridad, pruebas, RPM, CI/CD
25. Serialization y observability
26. Seguridad y supply chain
27. Cross compilation y no_std
28. Library/API design
29. Compiler internals
30. Debugging
31. Ingeniería profesional y proyectos

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

## Política de Big-O

Este PATH no sustituye al curso especializado/general de Big-O. La notación, familias de
complejidad, demostraciones, recurrencias y fundamentos matemáticos pertenecen a ese PATH.
Aquí se enseña cómo aplicar ese conocimiento en Rust: analizar código y loops, considerar el
coste de ownership/Clone/allocations, razonar sobre las colecciones estándar e iterators,
detectar complejidad accidental, evaluar trade-offs tiempo/espacio y contrastar hipótesis
asintóticas mediante benchmarks y profiling sin confundir Big-O con tiempo de ejecución medido.

## Política de aplicaciones CLI/TUI en Rust

El bloque 42 enseña desarrollo profesional de herramientas de terminal, desde `std::env` hasta `clap`, entrada/salida Unix, configuración, errores, `tracing`, `ratatui`, procesos, señales, async, seguridad, testing, benchmarking, completions, man pages, RPM y CI/CD. Fedora Linux es la plataforma principal. Cada grupo incorpora ejercicios prácticos y proyectos acumulativos. Cargo (bloque 14), Regex (43), Big-O (44), sistemas (41), async (28–29), serialización (45) y observabilidad (46) se aplican por referencia, sin repetir su teoría. Las herramientas interactivas deben ofrecer un modo seguro y usable en entornos no-TTY cuando corresponda.
