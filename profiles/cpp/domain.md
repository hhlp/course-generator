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

Integra los fundamentos del Bloque 1. Antes de desarrollarlo deben completarse
las ampliaciones 1.42–1.55, incluida la introducción a CMake y CTest.

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

Proyecto integrador de los Bloques 1–8:

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
ctest --test-dir build --output-on-failure --no-tests=error
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

## 54. Bloque 9 — Regex aplicada a C++

Este bloque enseña a utilizar expresiones regulares en programas C++23. No vuelve a impartir la teoría formal ni el catálogo general de expresiones del PATH Regex. Parte de patrones ya conocidos y explica la API de `<regex>`, sus tipos, sobrecargas, iteradores, opciones, errores y garantías.

Progresión: `std::regex` → `std::regex_match`/`search`/`replace` → capturas y `match_results` → iteradores → archivos/logs → validación y pruebas → coste, backtracking y alternativas → proyecto.

En los laboratorios se debe compilar con GCC y Clang, usar entradas válidas y malformadas, documentar la gramática empleada, medir patrones costosos sin exponer servicios públicos y evitar asumir soporte Unicode universal. Explicar por qué un parser específico o `std::from_chars` puede ser mejor opción.

Proyecto 9.30: analizador de logs, con biblioteca reutilizable, CLI, pruebas de coincidencia/extracción, manejo de errores, CMake, sanitizers y documentación.

## 55. Bloque 10 — Big-O aplicada a C++

El PATH general de Big-O proporciona la teoría matemática. Este bloque se centra en calcular y comprobar costes de código C++ real y en interpretar las garantías normativas de la STL.

Diferenciar en cada caso: coste temporal, coste espacial, promedio, peor caso, coste amortizado, invalidación de iteradores y coste real de memoria/caché. Para contenedores, comparar operaciones concretas en lugar de afirmar que un contenedor es siempre más rápido.

Progresión: análisis de funciones → contenedores y asignaciones → algoritmos STL/Ranges → estructuras y grafos → costes de compilación → benchmarks con `std::chrono`/Google Benchmark → `perf` → decisiones de diseño.

Un benchmark debe declarar hardware, compilador, versión, flags, tamaños, distribución de entradas, repeticiones y posibles fuentes de ruido; no confundir observación experimental con garantía asintótica.

Proyecto 10.41: banco de pruebas de estructuras y algoritmos, con datasets reproducibles, pruebas de corrección, CMake, mediciones comparables, profiling y análisis de resultados.

## 56. Conexiones transversales y orden de estudio

Los identificadores 1–8 permanecen intactos para conservar los proyectos y dependencias existentes. Los bloques 9 y 10 se agregan al final de `initial.txt`, pero Big-O puede estudiarse una vez adquiridos los fundamentos de contenedores y algoritmos del Bloque 1. Regex requiere strings, iteradores, archivos y manejo de errores.

Vincular Regex con parsing (1.25) y procesamiento de archivos (1.24); Big-O con algoritmos y contenedores (1.28–1.29, 3.26–3.29), Ranges (4.7–4.11), profiling (8.17–8.20) y el proyecto final (8.26).

Los bloques nuevos deben respetar las mismas secciones pedagógicas, exactitud bibliográfica, requisitos de compilación, laboratorios y validación establecidos para el resto del PATH.


## 57. Revisión de profundidad y conservación de identificadores

Se conservan las 356 lecciones originales, sus títulos e identificadores y los
10 bloques. Las ampliaciones se añaden al final de cada bloque. La posición en
el fichero no constituye por sí sola el orden pedagógico: las siguientes rutas
indican cuándo incorporar el material nuevo. Los proyectos conservan su ID.

- Bloque 1: ampliación 1.42–1.55; 55 lecciones en total.
- Bloque 2: ampliación 2.41–2.56; 56 lecciones en total.
- Bloque 3: ampliación 3.31–3.42; 42 lecciones en total.
- Bloque 4: ampliación 4.45–4.59; 59 lecciones en total.
- Bloque 5: ampliación 5.30–5.39; 39 lecciones en total.
- Bloque 6: ampliación 6.37–6.46; 46 lecciones en total.
- Bloque 7: ampliación 7.40–7.47; 47 lecciones en total.
- Bloque 8: ampliación 8.27–8.36; 36 lecciones en total.
- Bloque 9: ampliación 9.31–9.34; 34 lecciones en total.
- Bloque 10: ampliación 10.42–10.47; 47 lecciones en total.

## 58. Orden efectivo de estudio y proyectos

| Bloque | Orden recomendado |
|---|---|
| 1 | 1.1–1.40, incorporando 1.42–1.55 antes de 1.41 |
| 2 | 2.1–2.40 con las ampliaciones 2.41–2.56 |
| 3 | 3.1–3.29, después 3.31–3.42 y proyecto 3.30 |
| 4 | 4.1–4.43, después 4.45–4.59 y proyecto 4.44 |
| 5 | 5.1–5.28, después 5.30–5.39 y proyecto 5.29 |
| 6 | 6.1–6.35, después 6.37–6.46 y proyecto 6.36 |
| 7 | 7.1–7.39, después 7.40–7.47 |
| 8 | 8.1–8.25, después 8.27–8.36 y proyecto 8.26 |
| 9 | 9.1–9.29, después 9.31–9.34 y proyecto 9.30 |
| 10 | 10.1–10.40, después 10.42–10.47 y proyecto 10.41 |

En el Bloque 1 introducir 1.42–1.48 con tipos y expresiones; 1.49–1.51 con
funciones; 1.52 con streams; 1.53–1.55 antes del proyecto. No enseñar toda la
aritmética avanzada antes de que el estudiante pueda ejecutar ejemplos simples.

El formato plano de initial.txt no codifica esta ruta. Al generar en orden
numérico, los proyectos deben incluir un recordatorio autocontenido y guiado de
los prerrequisitos posteriores; el estudiante los completa después de estudiar
las ampliaciones. No presuponer que course-generator reordene las lecciones.

El proyecto 8.26 integra los Bloques 1–8. Los proyectos 9.30 y 10.41 son
integradores especializados posteriores; ninguno exige haber completado el otro.
El perfil usa standalone_project para 8.26 y conserva project_type: integrator.
No se exige reutilizar artefactos previos: artifact_dependencies permanece vacío.

## 59. Contrato de profundidad por área

- Fundamentos: explicar límites, conversiones y narrowing con predicción de
  resultados; diferenciar overflow signed y comportamiento modular unsigned.
  Separar precedencia, asociatividad y secuenciación; no deducir una de otra.
- Semántica: estudiar lookup antes de resolución de sobrecarga; incluir ADL,
  hidden friends, cv/ref qualifiers y conversiones de usuario. Distinguir la
  semántica de prvalues desde C++17 de NRVO opcional; no prometer NRVO.
- Memoria: diferenciar almacenamiento y lifetime. Analizar temporales, dangling,
  invalidación, alineación y acceso mediante tipos; limitar placement new a
  laboratorios donde se justifique y preferir RAII en código de aplicación.
- Excepciones: construir un ejemplo de rollback, explicar invariantes y
  comprobar garantías básica/fuerte/no-throw. Relacionar noexcept con movimiento.
- STL: enseñar contratos de comparadores, hash e igualdad antes de personalizar
  contenedores. std::pmr no es ownership automático: el recurso debe sobrevivir
  a sus usuarios y se debe medir su efecto antes de recomendarlo.
- Coroutines: distinguir frame, handle y objeto de retorno; asignar explícitamente
  ownership y destrucción. Una coroutine no crea un thread por sí sola.
- Ranges: inspeccionar lifetime, borrowed_range y reevaluación de pipelines.
  No suponer que todas las vistas almacenan resultados ni admiten multipass.
- Módulos: comprobar compilador, biblioteca y build system por separado;
  documentar versiones y comandos realmente probados, sin prometer portabilidad
  de artefactos compilados de módulos entre versiones o toolchains.
- Concurrencia: desarrollar un protocolo de reclamación antes de liberar nodos
  lock-free. Hazard pointers y épocas se tratan como técnicas o dependencias
  externas, sin atribuirles una API estándar de C++23.
- Regex: limitar entrada y aislar patrones patológicos en un proceso con timeout
  externo. std::regex no ofrece un mecanismo general de cancelación por timeout.
- Big-O: distinguir número de comparaciones y de incrementos de iterador;
  costes del predicado, asignaciones y copias; medición experimental y garantía.

## 60. Delimitación de lecciones próximas

4.36 conserva el título histórico «deducing this»: motivación, deducción de Self,
eliminación de sobrecargas y patrones de diseño. 4.37 desarrolla la sintaxis y
las restricciones del parámetro objeto explícito, resolución y diagnóstico.
Son dos tratamientos del mismo mecanismo, con objetivos distintos.

2.23 presenta perfect forwarding; 3.4–3.6 enseñan deducción y uso de std::forward;
el Bloque 5 evalúa restricciones y diseño genérico. Repetir solo el recordatorio
necesario, con ejercicios distintos y referencias cruzadas.

Las ampliaciones de STL, Ranges y semántica fijan contratos. El Bloque 10 aplica
esos contratos al análisis de costes. El Bloque 9 aplica regex a C++ sin repetir
la teoría general del PATH Regex ni atribuir sintaxis de PCRE2 a std::regex.

## 61. Herramientas y evidencia de validación

Los proyectos deben proporcionar CMakeLists.txt, activar pruebas con
include(CTest) o enable_testing(), y registrar al menos una prueba con add_test
o descubrimiento de GoogleTest. Un archivo tests/test_main.cpp por sí solo no
registra pruebas. En 1.41 basta un ejecutable de tests con comprobaciones
explícitas y código de salida distinto de cero al fallar; GoogleTest se enseña
después. No depender exclusivamente de assert, que puede desaparecer con NDEBUG.

La validación exige herramientas disponibles (require_tools: true) y configura,
compila y ejecuta CTest con --no-tests=error. Si faltan herramientas, no declarar
el proyecto validado; registrar la causa. El timeout es del comando de validación,
no una garantía de cancelación interna de regex o de tareas del programa.

Separar configuraciones ASan/UBSan y TSan. No mezclar resultados de builds con
flags diferentes. En CI registrar compilador, biblioteca estándar, versiones,
CMake, flags y pruebas ejecutadas. La validación sintáctica de estos cuatro
archivos no demuestra que los futuros proyectos generados compilen.

## 62. Lecturas y criterios de finalización

Las categorías canónicas son principal, complementaria, normativa,
profundizacion y consulta. Herramientas y motores se citan dentro de consulta;
material de C++ moderno se clasifica por su función en la lección. Usar solo
categorías pertinentes y no inventar números de capítulos o secciones.

Cada ampliación debe incluir un ejemplo compilable, un caso límite y una
explicación del resultado cuando proceda. Los proyectos exigen requisitos,
pruebas de corrección y documentación; las conclusiones de rendimiento exigen
mediciones reproducibles. Los ejemplos intencionadamente incorrectos se marcan
y no forman parte de los targets que deben compilar satisfactoriamente.
