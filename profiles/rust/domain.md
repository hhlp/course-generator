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


## Secuencia de estudio revisada

Se mantienen los 61 bloques (0–60) y los identificadores originales de lección.
`initial.txt` contiene la ruta completa; `profile.yaml` expresa el mismo orden
en `curriculum.study_order`. Los identificadores ordenan las referencias y no
obligan a impartir un concepto antes de sus prerrequisitos.

Lifetimes se estudia tras structs/enums. Cargo se trabaja en dos pasadas.
Regex se introduce tras testing e I/O; Big-O aplicado, tras performance.
Serialización, observabilidad, seguridad, dependencias y compilación cruzada
preceden la integración profesional CLI/TUI. RawWaker, proyección manual de Pin
y construcción con MaybeUninit se reservan a etapas con contratos unsafe.

## Cobertura reforzada

- Entorno Fedora reproducible, Rust 2024, MSRV y migración de edición revisada.
- Numéricos y overflow, slices, UTF-8, grafemas y rutas no UTF-8.
- Extracción de valores, destrucción, mutabilidad interior e inicialización única.
- Cargo avanzado: herencia de workspace, resolver 3, features aditivas, build.rs,
  diagnósticos y benchmarking estable con un harness compatible.
- Tests de compilación, propiedades, aislamiento de entorno y entradas hostiles.
- Tokio, Rayon, backpressure, cancelación y supervisión de tareas con límites.
- Macros procedurales con diagnósticos; FFI con allocator y ABI explícitos.
- Memoria, pinning, provenance y contratos de seguridad con herramientas de apoyo.
- HTTP/TLS, descriptores con ownership y persistencia SQL opcional en proyectos.
- Evolución de APIs, SemVer, supply chain, SBOM y evaluación profesional.

## Precisiones técnicas obligatorias

`regex::escape` es una función del crate; `regex::NoExpand` controla reemplazos
literales. RegexSet informa qué patrones coinciden, no las capturas de todos.
La búsqueda y la iteración de coincidencias tienen garantías distintas: consultar
la versión usada y expresar el tamaño del patrón y el del texto por separado.
HashMap combina costes esperados con detalles como capacidad de recorrido;
Clone, Drop, hashing y comparación de claves no tienen coste unitario universal.

Rust 2024 requiere atender unsafe extern, atributos unsafe, patrones y APIs del
entorno global. Configurar procesos hijos con Command::env evita mutar ese estado.
Un workspace virtual declara su resolver explícitamente. cargo verify-project se
conserva como lección histórica de un comando deprecado, con alternativas actuales.

La ejecución con Miri, Loom, sanitizers o fuzzing aporta evidencia acotada;
no sustituye la revisión de invariantes ni demuestra ausencia general de errores.
Los ejemplos de soundness separan garantías documentadas de modelos experimentales.

## Resultados y criterios de aceptación

Cada laboratorio aporta instrucciones, versiones, resultado esperado, casos
de error y criterios de aceptación. Los hitos de fundamentos, intermedio,
avanzado, profesional y experto se especifican en initial.txt y acumulan trabajo.
Los proyectos finales exigen explicar ownership, errores, límites de recursos,
seguridad, pruebas, complejidad y decisiones medidas de rendimiento.

Embedded es introductorio; no equivale a especialización experta en hardware.
El contenido de compiladores profundiza en internals sin prometer estabilidad
de formatos ni APIs internas. Persistencia SQL es una ampliación opcional que
aplica el PATH SQL, sin repetirlo. Regex y Big-O mantienen sus límites originales.

## Integración con course-generator

Se conservan las claves originales del perfil y sus referencias a domain.md,
bibliography.md y ../../config/pedagogy.md. Esta última es una dependencia externa
del repositorio; debe resolverse desde la ubicación real del perfil antes de
generar lecciones. Las nuevas políticas son metadatos: su aplicación automática
depende de que el generador las lea. La revisión estructural no ejecuta el curso.
