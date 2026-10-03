# Bibliografía — Rust 0 → Experto

## Documentación oficial — referencia permanente

- **Rust Documentation (stable)** — https://doc.rust-lang.org/stable/
  Referencia oficial durante todo el PATH.
- **The Rust Programming Language (The Book)** — fundamentos, ownership, borrowing, traits, generics, testing, concurrencia y async.
- **The Rust Reference** — semántica formal del lenguaje; especialmente niveles avanzado y experto.
- **The Cargo Book** — Cargo, manifests, workspaces, features, profiles, publicación y build scripts.
- **The Rustonomicon** — unsafe Rust, aliasing, layouts, FFI, atomics y soundness.
- **The Async Book** — Future, async/await, pinning, executors y patrones async.
- **rustc-dev-guide** — arquitectura del compilador, HIR/MIR, type checking, trait solving, borrow checking y codegen.
- **Rust API Guidelines** — diseño de bibliotecas y APIs idiomáticas.
- **The Embedded Rust Book** — `no_std` y fundamentos de embedded.

## Libros principales aportados

### The Rust Programming Language, 3rd Edition
Steve Klabnik, Carol Nichols, Chris Krycho et al.

Base pedagógica principal para 0 → intermedio. Usarlo especialmente en:
fundamentos, ownership, borrowing, structs, enums, patterns, collections, errores,
modules, generics, traits, lifetimes, tests, iterators, closures, smart pointers,
concurrencia y async.

### Programming Rust, 3rd Edition
Jim Blandy, Jason Orendorff, Leonora F. S. Tindall.

Columna vertebral técnica del curso. Su progresión incluye:
Systems Programmers Can Have Nice Things; A Tour of Rust; Fundamental Types;
Ownership and Moves; References; Expressions; Error Handling; Crates and Modules;
Structs; Enums and Patterns; Traits and Generics; Operator Overloading; Utility
Traits; Closures; Iterators; Collections; Strings and Text; Input and Output;
Threads; Asynchronous Programming; Futures; Macros; Unsafe Code; Foreign Functions.

Mapeo principal: bloques 0–32.

### Rust in Action: Systems Programming Concepts and Techniques
Timothy Samuel McNamara.

Bloques principales: memoria, representación de datos, filesystems, networking,
concurrencia y systems programming. Especialmente 23, 37, 40, 41 y proyectos.

### Effective Rust: 35 Specific Ways to Improve Your Rust Code
David Drysdale.

Usar después de dominar los fundamentos. Bloques 12, 15–22, 35, 37, 45, 46,
49 y 56. Orientado a decisiones prácticas, APIs mantenibles y código efectivo.

### Idiomatic Rust: Code like a Rustacean
Brenden Matthews.

Bloques 15–22, 35–36, 42–49 y 56. Reforzar patrones idiomáticos, diseño,
errores, iterators, traits, APIs y mantenibilidad.

### Code Like a Pro in Rust
Brenden Matthews.

Nivel intermedio → profesional. Arquitectura, calidad, testing, herramientas,
aplicaciones reales y prácticas profesionales. Bloques 35, 42–46, 49 y 56–58.

### Rust for Rustaceans: Idiomatic Programming for Experienced Developers
Jon Gjengset.

Texto central avanzado → experto. Ownership/lifetimes avanzados, traits, API
design, type system, concurrency, async, unsafe y ecosystem.
Bloques 35–36, 39, 49–54 y 56–58.

### Rust Atomics and Locks
Mara Bos.

Referencia central para bloques 26, 27 y 52:
atomics, memory ordering, happens-before, locks, synchronization, cache effects,
lock-free reasoning y construcción de primitivas de sincronización.

### Async Rust: Unleashing the Power of Fearless Concurrency
Maxwell Flitton, Caroline Morton.

Referencia especializada para bloques 28, 29 y 51:
async/await, futures, runtimes, tasks, synchronization, networking y diseño
de aplicaciones concurrentes asíncronas.

## Estrategia de lectura

0 → básico:
The Rust Programming Language + documentación oficial.

Básico → intermedio:
Programming Rust + The Rust Programming Language.

Intermedio → avanzado:
Rust in Action + Effective Rust + Idiomatic Rust + Code Like a Pro in Rust.

Avanzado → experto:
Rust for Rustaceans + Rust Atomics and Locks + Async Rust.

Experto / internals:
The Rust Reference + Rustonomicon + rustc-dev-guide + Cargo Book +
documentación estándar y RFCs relevantes.

Los libros no deben seguirse de forma estrictamente lineal. Cada lección debe
seleccionar la fuente que mejor explique el concepto y contrastarla con la
documentación oficial vigente.
