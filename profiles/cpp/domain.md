# Dominio — C++ EN PROFUNDIDAD

## 1. Identidad del PATH

**Nombre:** C++ EN PROFUNDIDAD
**Lenguaje:** C++
**Estándar objetivo:** C++23
**Plataforma principal:** Fedora Linux
**Compiladores principales:** GCC y Clang
**Nivel:** desde fundamentos hasta nivel avanzado/experto
**Orientación:** lenguaje, biblioteca estándar, sistemas, toolchain e ingeniería C++.

Este PATH debe enseñar C++ como un lenguaje de sistemas moderno y multiparadigma, no únicamente como una sintaxis para programación orientada a objetos.

## 2. Objetivo global

El estudiante debe evolucionar desde la creación de sus primeros programas hasta comprender:

- semántica del lenguaje;
- modelo de objetos;
- tipos;
- valores;
- lifetime;
- ownership;
- RAII;
- copy/move semantics;
- value categories;
- templates;
- generic programming;
- STL;
- C++17;
- C++20;
- C++23;
- Concepts;
- Ranges;
- Coroutines;
- Modules;
- concurrencia;
- memory model;
- atomics;
- compilación;
- linking;
- ELF;
- ABI;
- debugging;
- sanitizers;
- profiling;
- build systems;
- testing;
- packaging;
- diseño de proyectos C++ reales.

## 3. Filosofía pedagógica

C++ debe enseñarse progresivamente.

La progresión conceptual general será:

```text
programa
→ expresiones
→ tipos
→ objetos
→ funciones
→ contenedores
→ clases
→ recursos
→ RAII
→ generic programming
→ object model
→ copy/move
→ value categories
→ C++ moderno
→ templates avanzados
→ concurrencia
→ memory model
→ compilación
→ linking
→ ABI
→ tooling
→ ingeniería de proyectos
```

## 4. C++ moderno como referencia

El PATH tiene como objetivo práctico **C++23**.

Debe evitarse enseñar patrones antiguos como práctica recomendada cuando existe una alternativa moderna claramente superior.

Preferir RAII frente a gestión manual innecesaria de recursos.

Preferir containers de la biblioteca estándar frente a arrays dinámicos manuales cuando el objetivo no sea estudiar explícitamente memoria.

Preferir smart pointers cuando realmente exista ownership dinámico.

## 5. No ocultar la complejidad del lenguaje

"C++ moderno" no significa ocultar:

- punteros;
- arrays;
- memoria;
- lifetime;
- object representation;
- undefined behavior;
- ABI;
- linking;
- ownership;
- value categories.

Estos conceptos son parte fundamental del PATH.

## 6. Bloque 1 — Fundamentos

El Bloque 1 establece el modelo mental básico y debe ser profundamente didáctico.

Fuente pedagógica principal:

**Programming: Principles and Practice Using C++ — 3rd Edition.**

Debe cubrir progresivamente:

```text
programa
→ compilación
→ valores
→ objetos
→ tipos
→ variables
→ expresiones
→ control
→ funciones
→ errores
→ strings
→ vectors
→ arrays
→ referencias
→ punteros
→ lifetime
→ clases
→ invariantes
→ encapsulación
→ I/O
→ STL
→ templates
→ herencia
→ polimorfismo
→ excepciones
→ RAII
→ recursos
```

## 7. Bloque 2 — Semántica y modelo de objetos

Debe profundizar especialmente en:

- object model;
- storage duration;
- lifetime;
- scope;
- linkage;
- `const`;
- references;
- pointers;
- copy;
- move;
- special member functions;
- Rule of Three;
- Rule of Five;
- Rule of Zero;
- value categories;
- `std::move`;
- forwarding;
- ownership;
- smart pointers;
- inheritance;
- slicing;
- virtual dispatch;
- RTTI;
- conversions;
- namespaces;
- translation units.

Debe diferenciar claramente scope, storage duration, lifetime, linkage y ownership.

## 8. Value categories

La enseñanza debe distinguir correctamente:

```text
glvalue
├── lvalue
└── xvalue

rvalue
├── prvalue
└── xvalue
```

`std::move` debe enseñarse como una conversión que habilita semántica de movimiento, no como una operación que físicamente mueve por sí misma un objeto.

## 9. Ownership

Ownership debe tratarse como concepto de diseño.

Diferenciar:

```text
owner
non-owner
borrowed access
shared ownership
weak observation
```

Relacionarlo con:

```cpp
std::unique_ptr
std::shared_ptr
std::weak_ptr
```

Un raw pointer puede representar acceso no propietario.

## 10. RAII

RAII es uno de los principios transversales del PATH.

Debe conectarse con memoria, archivos, mutexes, locks, handles, excepciones, scope y destructores.

## 11. Bloque 3 — C++ moderno

Debe estudiar las herramientas fundamentales necesarias para comprender C++ moderno:

- `auto`;
- `decltype`;
- type deduction;
- forwarding references;
- `std::forward`;
- lambdas;
- `constexpr`;
- `noexcept`;
- `nullptr`;
- `enum class`;
- variadic templates;
- fold expressions;
- structured bindings;
- `if constexpr`;
- `std::optional`;
- `std::variant`;
- `std::any`;
- `std::string_view`;
- filesystem;
- CTAD.

## 12. Bloque 4 — C++20 y C++23

Debe diferenciar:

```text
característica definida por el estándar
característica soportada por GCC
característica soportada por Clang
característica disponible en libstdc++
característica disponible en libc++
```

No asumir que `-std=c++23` implica soporte total de toda la biblioteca C++23.

## 13. Concepts

Progresión:

```text
template sin restricciones
→ requisitos informales
→ SFINAE
→ traits
→ enable_if
→ Concepts
→ requires
→ constrained overload resolution
```

## 14. Ranges

Explicar:

- ranges;
- range algorithms;
- views;
- adaptors;
- lazy evaluation;
- pipelines;
- projections;
- borrowed ranges;
- lifetime de views.

## 15. Coroutines

Relacionar:

```text
coroutine function
promise_type
coroutine frame
suspension
resume
co_await
co_yield
co_return
```

No presentarlas simplemente como "async/await de C++".

## 16. Modules

Modules deben enseñarse junto con translation units, preprocessing, headers, ODR, compilación, dependency graphs y build systems.

## 17. Bloque 5 — Templates

Debe cubrir:

- template declaration;
- instantiation;
- deduction;
- specialization;
- dependent names;
- two-phase lookup;
- parameter packs;
- SFINAE;
- traits;
- metaprogramming;
- constraints;
- CRTP;
- policies;
- expression templates.

## 18. Errores de templates

Cuando sea útil, los laboratorios deben mostrar cómo interpretar errores de GCC y Clang:

- substitution failures;
- dependent names;
- failed constraints;
- overload resolution;
- incomplete types;
- instantiation traces.

## 19. Bloque 6 — Concurrencia

Progresión:

```text
concurrency
→ threads
→ shared state
→ races
→ mutex
→ synchronization
→ futures
→ coordination primitives
→ cancellation
→ memory model
→ atomics
→ lock-free
```

## 20. Data race

Debe diferenciarse `race condition` de `data race`.

## 21. Memory model

Debe explicarse progresivamente:

```text
sequenced-before
synchronizes-with
happens-before
modification order
atomic operations
memory ordering
```

Después:

```text
relaxed
acquire
release
acq_rel
seq_cst
```

## 22. Lock-free programming

Debe presentarse como materia avanzada.

Explicar:

- CAS;
- compare/exchange loops;
- ABA;
- reclamación de memoria;
- cache coherency;
- false sharing;
- lock-free;
- wait-free.

## 23. Bloque 7 — Toolchain e internals

Flujo fundamental:

```text
source
↓
preprocessor
↓
compiler
↓
assembler
↓
object file
↓
linker
↓
ELF executable/shared object
↓
loader
↓
process
```

## 24. ELF y símbolos

Las lecciones deben utilizar herramientas reales de Fedora:

```bash
g++
clang++
cpp
as
ld
nm
readelf
objdump
c++filt
file
ldd
gdb
```

## 25. ABI

Relacionar construcciones C++ con su representación:

```text
class → object layout
virtual function → virtual dispatch
virtual hierarchy → vtable/vptr según ABI
function overload → mangled symbol
exception → runtime ABI
template → instantiation/symbol generation
```

No presentar detalles del Itanium ABI como requisitos universales del lenguaje.

## 26. libstdc++

Debe explicar la relación:

```text
C++ source
→ compiler
→ standard library implementation
→ libstdc++
→ runtime/ABI
```

Estudiar cuando corresponda:

- `libstdc++.so.6`;
- `GLIBCXX_*`;
- `CXXABI_*`.

## 27. Debugging

GDB debe utilizarse como herramienta práctica:

```text
compile -g
→ start/run
→ breakpoint
→ next/step
→ print
→ backtrace
→ frames
→ exceptions
→ threads
→ core dumps
```

## 28. Sanitizers

Deben diferenciarse:

- ASan;
- UBSan;
- TSan.

No afirmar que pasar sanitizers demuestra ausencia total de UB o errores de concurrencia.

## 29. Bloque 8 — Ingeniería C++

Debe cubrir:

- project layout;
- headers;
- source files;
- Make;
- CMake;
- Meson;
- warnings;
- sanitizers;
- static analysis;
- formatting;
- testing;
- profiling;
- optimization;
- libraries;
- versioning;
- packaging;
- RPM.

## 30. Warnings

Configuración pedagógica habitual:

```bash
-Wall -Wextra -Wpedantic
```

No debe asumirse que `-Wall` significa literalmente "todos los warnings".

## 31. Optimización

Diferenciar:

```text
correctness
measurement
algorithmic optimization
compiler optimization
micro-optimization
```

La optimización debe basarse preferentemente en mediciones.

## 32. Undefined behavior

El PATH debe distinguir siempre:

```text
well-defined behavior
implementation-defined behavior
unspecified behavior
undefined behavior
ill-formed program
```

## 33. Fedora

Fedora es la plataforma práctica principal.

Los ejemplos de instalación pueden utilizar `dnf` o la herramienta vigente correspondiente en Fedora.

No convertir el PATH en un curso general de administración Fedora.

## 34. GCC y Clang

GCC será el toolchain principal cuando sea razonable y Clang la segunda implementación para comparar diagnostics, verificar portabilidad y usar tooling LLVM.

## 35. Estándar objetivo

Los laboratorios utilizarán preferentemente:

```bash
g++ -std=c++23
```

o:

```bash
clang++ -std=c++23
```

Las lecciones históricas deben indicar cuándo una característica pertenece originalmente a C++98, C++03, C++11, C++14, C++17, C++20 o C++23 cuando sea relevante.

## 36. Código de ejemplo

Los ejemplos deben ser:

- compilables;
- mínimos cuando expliquen un concepto;
- suficientemente completos;
- compatibles con el estándar indicado;
- específicos de la lección.

## 37. Código incorrecto intencionado

Cuando una lección estudie errores puede mostrarse código incorrecto, pero debe marcarse claramente y explicar qué ocurre, por qué y cómo corregirlo.

## 38. Laboratorios

Los laboratorios pueden incluir:

```bash
g++
clang++
gdb
nm
readelf
objdump
c++filt
perf
cmake
ctest
meson
ninja
```

Cuando resulte apropiado deben pedir:

1. predecir;
2. compilar;
3. ejecutar;
4. observar;
5. explicar;
6. modificar;
7. volver a comprobar.

## 39. Estructura de cada lección

Toda lección comienza obligatoriamente con:

# 🎯 OBJETIVO

Después debe aparecer:

# 📚 LECTURA

El cuerpo debe desarrollar el contenido mediante headings específicos del tema.

Opcionalmente:

# 🧪 LABORATORIO

# ⚠️ ERRORES FRECUENTES

# 💡 IDEA IMPORTANTE

Toda lección termina obligatoriamente con:

# 🧠 QUÉ DEBES RECORDAR

con entre **3 y 7 ideas esenciales**.

## 40. Evitar scaffolding genérico

No producir automáticamente estructuras genéricas si no están adaptadas al tema.

## 41. Autocontención

Cada lección debe poder estudiarse individualmente siempre que el estudiante posea los prerrequisitos definidos por el PATH.

## 42. Profundidad

Cada lección debe responder, cuando sea relevante:

```text
qué es
por qué existe
cómo funciona
cómo se utiliza
qué garantías proporciona
qué costes tiene
qué errores produce
qué alternativas existen
cómo se relaciona con el resto de C++
```

## 43. Precisión normativa

Distinguir entre:

```text
requisito del lenguaje
requisito de la biblioteca estándar
detalle de implementación
extensión del compilador
detalle de ABI
```

## 44. Feature-test macros

Para características modernas debe enseñarse cuando corresponda:

```cpp
__cplusplus
```

y las feature-test macros relevantes.

## 45. Proyectos

Los proyectos definidos por `profile.yaml` son integradores.

Cada proyecto debe plantear:

- problema;
- requisitos;
- arquitectura;
- implementación;
- build;
- tests;
- validación;
- documentación.

## 46. Proyecto 1.41

`proyecto-final-ppp3`

Integra los fundamentos del Bloque 1.

## 47. Proyecto 3.30

`proyecto-cpp17`

Debe utilizar C++17 de manera natural.

## 48. Proyecto 4.44

`proyecto-cpp23`

Debe demostrar utilización razonada de C++20/C++23 y verificar soporte real del toolchain.

## 49. Proyecto 5.29

`generic-library`

Debe diseñarse como una pequeña biblioteca genérica reutilizable.

## 50. Proyecto 6.36

`proyecto-concurrente`

Debe exigir razonamiento sobre shared state, synchronization, ownership, cancellation y correctness.

## 51. Proyecto 8.26

`proyecto-cpp23-completo`

Proyecto integrador final:

```text
C++23
+ diseño
+ templates
+ STL
+ concurrencia cuando aporte valor
+ CMake
+ testing
+ warnings
+ sanitizers
+ static analysis
+ profiling
+ libraries
+ packaging
```

## 52. Validación

Cuando una lección produzca un proyecto validable:

```text
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

Un fallo de compilación o tests no debe considerarse un proyecto válido.

## 53. Principio final

El estudiante debe terminar siendo capaz de razonar desde varios niveles:

```text
código fuente
↓
semántica C++
↓
modelo de objetos
↓
lifetime y ownership
↓
templates y biblioteca
↓
concurrencia y memory model
↓
compiler
↓
object files
↓
linker
↓
ABI
↓
runtime
↓
sistema Linux
```
