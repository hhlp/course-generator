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
48, 51 y 58. Orientado a decisiones prácticas, APIs mantenibles y código efectivo.

### Idiomatic Rust: Code like a Rustacean
Brenden Matthews.

Bloques 15–22, 35–36, 42–49, 51 y 58. Reforzar patrones idiomáticos, diseño,
errores, iterators, traits, APIs y mantenibilidad.

### Code Like a Pro in Rust
Brenden Matthews.

Nivel intermedio → profesional. Arquitectura, calidad, testing, herramientas,
aplicaciones reales y prácticas profesionales. Bloques 35, 42–46, 48–49, 51 y 57–58.

### Rust for Rustaceans: Idiomatic Programming for Experienced Developers
Jon Gjengset.

Texto central avanzado → experto. Ownership/lifetimes avanzados, traits, API
design, type system, concurrency, async, unsafe y ecosystem.
Bloques 35–36, 39, 51–55 y 58; apoyo complementario a 49 y 56–57.

### Rust Atomics and Locks
Mara Bos.

Referencia central para bloques 26, 27 y 54:
atomics, memory ordering, happens-before, locks, synchronization, cache effects,
lock-free reasoning y construcción de primitivas de sincronización.

### Async Rust: Unleashing the Power of Fearless Concurrency
Maxwell Flitton, Caroline Morton.

Referencia especializada para bloques 28, 29 y 53:
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


## Referencias primarias para la revisión

Comprobación documental: 19 de octubre de 2026. Al generar cada lección,
consultar la documentación correspondiente a sus versiones y MSRV.

- The Book: https://doc.rust-lang.org/book/
- Rust Reference: https://doc.rust-lang.org/reference/
- Cargo Book: https://doc.rust-lang.org/cargo/
- Edition Guide (2024): https://doc.rust-lang.org/edition-guide/rust-2024/
- Unsafe extern: https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-extern.html
- APIs de entorno: https://doc.rust-lang.org/edition-guide/rust-2024/newly-unsafe-functions.html
- Resolver 3: https://doc.rust-lang.org/edition-guide/rust-2024/cargo-resolver.html
- Comandos deprecados: https://doc.rust-lang.org/cargo/commands/deprecated-and-removed.html
- cargo bench: https://doc.rust-lang.org/cargo/commands/cargo-bench.html
- Costes de collections: https://doc.rust-lang.org/std/collections/
- regex (API y garantías): https://docs.rs/regex/
- regex::escape: https://docs.rs/regex/latest/regex/fn.escape.html
- Reemplazos literales: https://docs.rs/regex/latest/regex/struct.NoExpand.html
- Rustonomicon: https://doc.rust-lang.org/nomicon/
- rustc-dev-guide: https://rustc-dev-guide.rust-lang.org/
- Rust API Guidelines: https://rust-lang.github.io/api-guidelines/
- Performance Book: https://nnethercote.github.io/perf-book/
- Embedded Book: https://docs.rust-embedded.org/book/

## Herramientas para laboratorios avanzados

Las páginas siguientes son referencias de implementación que deben verificarse
al preparar el laboratorio; no todas se ejecutaron ni se auditaron en esta revisión.

| Tema | Documentación primaria | Bloques |
| --- | --- | --- |
| Runtime y tareas | https://tokio.rs/tokio/tutorial | 28, 40, 42, 53 |
| Paralelismo de datos | https://docs.rs/rayon/ | 26, 37, 54 |
| Property testing | https://proptest-rs.github.io/proptest/ | 25, 44, 59 |
| Compile-fail | https://docs.rs/trybuild/ | 25, 30, 36, 52 |
| Fuzzing | https://rust-fuzz.github.io/book/ | 25, 47, 55 |
| Model checking | https://docs.rs/loom/ | 27, 54 |
| Interleavings | https://docs.rs/shuttle/ | 54 |
| Miri | https://github.com/rust-lang/miri | 31, 55, 57 |
| Pin projection | https://docs.rs/pin-project/ | 53 |
| Procedural macros | https://docs.rs/syn/ y https://docs.rs/quote/ | 30 |
| Unix seguro | https://docs.rs/rustix/ y https://docs.rs/nix/ | 41, 42 |
| HTTP service | https://docs.rs/axum/ | 40, 59 |
| TLS | https://docs.rs/rustls/ | 40, 47 |
| SQL opcional | https://docs.rs/sqlx/ | 59, 60 |
| API compatibility | https://github.com/obi1kenobi/cargo-semver-checks | 51, 58 |
| Dependency audit | https://rustsec.org/ y https://docs.rs/cargo-deny/ | 47, 48 |
| Dependency review | https://mozilla.github.io/cargo-vet/ | 48 |
| Benchmarks | https://bheisler.github.io/criterion.rs/book/ | 14, 37, 44 |
| Fedora Rust RPM | https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/ | 42 |

## Uso de libros y ediciones

Se conservan todos los títulos y ediciones aportados por el usuario. No se ha
realizado una verificación editorial completa de cada edición, autoría o índice.
Las asignaciones por bloque son orientaciones pedagógicas, no afirmaciones de
que cada libro cubra exhaustivamente todos los temas o las APIs actuales.
Si un libro discrepa de la documentación de la versión usada, documentar la
diferencia y seguir la semántica oficial; no inventar páginas ni capítulos.

## Mapa bibliográfico complementario

- 0–13: The Book, Programming Rust y std; fundamentos y errores.
- 14, 33–34, 48–49, 58: Cargo Book, Edition Guide y documentación de herramientas.
- 15–22, 35–36, 51–52: Rust for Rustaceans, Effective Rust y API Guidelines.
- 23, 31–32, 39, 55: Reference, Rustonomicon, Miri y Rust in Action.
- 25, 30: herramientas de pruebas, macros, syn/quote y trybuild.
- 26–27 y 54: Rust Atomics and Locks, std, Rayon y Loom.
- 28–29 y 53: Async Rust, Tokio, Future/Pin y documentación del runtime usado.
- 37 y 44: garantías de std, Performance Book, Criterion y perfiles Cargo.
- 38 y 56: rustc-dev-guide y Reference; los libros no sustituyen estas fuentes.
- 40–42 y 45–47: documentación de crates, CLI Book y libros de sistemas/profesionales.
- 43: regex y std; el PATH Regex aporta la teoría externa.
- 50: Embedded Book; alcance introductorio.
- 57–60: fuentes de los subsistemas usados y evidencias del proyecto.
