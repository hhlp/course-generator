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


## Expresiones regulares en Rust — referencias de integración

- **regex crate documentation (docs.rs / crate regex)** — referencia primaria para la API de `Regex`, `RegexSet`, `RegexBuilder`, `Captures`, `Match`, reemplazos y módulo `bytes`.
- **regex crate repository/documentation** — comportamiento, límites del motor, Unicode, rendimiento y decisiones de diseño.
- **Rust standard library documentation** — `LazyLock`, `String`, `str`, iterators, `Option`, `Result` y APIs de texto usadas junto con regex.

### Política bibliográfica para regex

La teoría y sintaxis completa de expresiones regulares se delega al PATH específico de Regex.
Estas referencias se usan para enseñar **cómo aplicar regex desde Rust** con profundidad: API,
ownership/borrowing, errores, iterators, Unicode/bytes, rendimiento, seguridad, testing e integración
con aplicaciones. No se duplicará el desarrollo teórico del PATH de Regex.

## Big-O en Rust — referencias de integración

- **Rust standard library documentation** — referencia primaria para las APIs y las garantías documentadas de `Vec`, `VecDeque`, `HashMap`, `HashSet`, `BTreeMap`, `BTreeSet`, `BinaryHeap`, slices, `String` e iterators.
- **The Rust Performance Book** — referencia complementaria para allocations, tipos, iterators, profiling y optimización basada en mediciones.
- **The Cargo Book** — perfiles de compilación, `cargo bench` y configuración necesaria para mediciones reproducibles.
- **Criterion.rs documentation** — benchmarking estadístico cuando se utilice Criterion en los laboratorios.
- **Programming Rust, 3rd Edition** y **Rust in Action** — conectar estructuras de datos, memoria, iterators y systems programming con decisiones de coste y rendimiento.

### Política bibliográfica para Big-O

La teoría matemática y algorítmica completa de Big-O se delega al PATH específico de Big-O.
Estas referencias se usan para enseñar **cómo aplicar Big-O desde Rust** con profundidad:
operaciones de tipos y colecciones, iterators, ownership/borrowing, allocations, complejidad
temporal/espacial, trade-offs, benchmarking y profiling. Los tiempos medidos sirven para
contrastar hipótesis de rendimiento, no para sustituir el análisis asintótico.

## Desarrollo profesional de aplicaciones CLI/TUI — bloque 42

### Documentación primaria y crates

- **Rust std** (`std::env`, `std::io`, `std::fs`, `std::path`, `std::process`) — https://doc.rust-lang.org/std/
- **Command Line Applications in Rust (CLI Book)** — https://rust-cli.github.io/book/
- **clap** — https://docs.rs/clap/ — argumentos, derive, subcommands, help y validación.
- **clap_complete** — https://docs.rs/clap_complete/ — completions de Bash, Zsh y Fish.
- **clap_mangen** — https://docs.rs/clap_mangen/ — manuales man.
- **ratatui** — https://ratatui.rs/ — interfaces de terminal.
- **crossterm** — https://docs.rs/crossterm/ — eventos y control de terminal.
- **indicatif** — https://docs.rs/indicatif/ — progreso y spinners.
- **serde** — https://serde.rs/ — serialización y configuración.
- **anyhow** y **thiserror** — https://docs.rs/anyhow/ y https://docs.rs/thiserror/ — gestión de errores.
- **tracing** y **tracing-subscriber** — https://docs.rs/tracing/ y https://docs.rs/tracing-subscriber/ — instrumentación.
- **assert_cmd**, **predicates** y **assert_fs** — https://docs.rs/assert_cmd/ , https://docs.rs/predicates/ y https://docs.rs/assert_fs/ — pruebas de binarios.
- **Tokio** y **reqwest** — https://tokio.rs/ y https://docs.rs/reqwest/ — CLI asíncronas y clientes HTTP.
- **Criterion.rs** — https://bheisler.github.io/criterion.rs/book/ — benchmarking.
- **Fedora Packaging Guidelines** — https://docs.fedoraproject.org/en-US/packaging-guidelines/ — distribución RPM.
- **GitHub Actions documentation** — https://docs.github.com/en/actions — pipelines y releases.

### Libros de apoyo existentes

*Code Like a Pro in Rust*, *Idiomatic Rust*, *Effective Rust* y *Rust in Action* apoyan arquitectura, testing, diseño, Linux y mantenimiento. **The Cargo Book** continúa como referencia del bloque 14, sin duplicar la formación de Cargo.

### Política didáctica

Explicar las APIs de cada crate con ejemplos compilables y comparar alternativas según necesidad; comprobar compatibilidad de versiones y documentación vigente al generar cada lección. Regex, Big-O, async y systems programming se reutilizan desde sus bloques especializados.
