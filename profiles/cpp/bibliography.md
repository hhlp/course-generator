# Bibliografía — C++ EN PROFUNDIDAD

## 1. Propósito

Esta bibliografía define las fuentes que debe utilizar el generador para el PATH **C++ EN PROFUNDIDAD**.

El PATH cubre progresivamente:

- fundamentos de C++;
- modelo de objetos y semántica de valores;
- C++ moderno;
- C++20 y C++23;
- templates y programación genérica;
- concurrencia y modelo de memoria;
- compilación, linking, ABI y debugging;
- ingeniería de proyectos C++.

La plataforma práctica principal es **Fedora Linux**, utilizando preferentemente GCC y Clang con C++23.

Las fuentes no deben utilizarse de forma indiscriminada. Cada una tiene un papel pedagógico concreto.

## 2. Bibliografía principal

### Programming: Principles and Practice Using C++ — Third Edition

**Autor:** Bjarne Stroustrup
**Edición:** 3rd Edition
**Rol:** Principal para el Bloque 1.

Debe priorizarse especialmente para:

- introducción al lenguaje;
- compilación de programas;
- objetos, valores y tipos;
- variables;
- expresiones;
- control de flujo;
- funciones;
- errores;
- debugging inicial;
- `std::string`;
- `std::vector`;
- arrays;
- referencias;
- punteros;
- clases;
- constructores;
- invariantes;
- I/O;
- archivos;
- STL;
- templates introductorios;
- herencia;
- polimorfismo;
- excepciones;
- RAII;
- gestión de recursos.

### Uso por bloques

**Bloque 1:** fuente principal.

**Bloques posteriores:** consulta pedagógica cuando resulte útil, pero deja de ser la fuente técnica principal.

## 3. Bibliografía complementaria

### A Tour of C++ — Third Edition

**Autor:** Bjarne Stroustrup
**Edición:** 3rd Edition
**Rol:** Complementaria, especialmente Bloques 1–4.

Especialmente útil para:

- tipos y objetos;
- clases;
- templates;
- STL;
- move semantics;
- smart pointers;
- lambdas;
- concepts;
- ranges;
- concurrencia;
- C++20;
- características modernas del lenguaje.

## 4. Bibliografía de profundización

### C++ Primer — Fifth Edition

**Autores:** Stanley B. Lippman, Josée Lajoie, Barbara E. Moo
**Edición:** 5th Edition
**Rol:** Profundización para los Bloques 1–3.

Debe utilizarse para profundizar en:

- tipos;
- expresiones;
- funciones;
- clases;
- referencias;
- punteros;
- `const`;
- scope;
- linkage;
- copy control;
- templates;
- STL;
- iteradores;
- algoritmos;
- herencia;
- virtual functions;
- object-oriented programming.

Aunque está basado en una versión anterior del estándar, sigue siendo especialmente útil para explicar los fundamentos semánticos del lenguaje.

No debe utilizarse para afirmar que una característica moderna no existe simplemente porque el libro sea anterior a C++17/C++20/C++23.

## 5. Referencia transversal

### The C++ Programming Language — Fourth Edition

**Autor:** Bjarne Stroustrup
**Edición:** 4th Edition
**Rol:** Consulta técnica transversal.

Debe utilizarse como referencia conceptual para:

- modelo del lenguaje;
- tipos;
- clases;
- object model;
- templates;
- excepciones;
- jerarquías;
- gestión de recursos;
- concurrencia;
- biblioteca estándar.

## 6. C++ moderno

### C++17 — The Complete Guide

**Autor:** Nicolai M. Josuttis
**Rol:** Referencia especializada del Bloque 3.

Debe priorizarse para:

- structured bindings;
- `if constexpr`;
- fold expressions;
- class template argument deduction;
- deduction guides;
- `std::optional`;
- `std::variant`;
- `std::any`;
- `std::string_view`;
- filesystem;
- mejoras de lambdas;
- mejoras de templates;
- mejoras de la biblioteca estándar.

### C++20 — The Complete Guide

**Autor:** Nicolai M. Josuttis
**Rol:** Referencia especializada del Bloque 4.

Debe priorizarse para:

- concepts;
- constraints;
- `requires`;
- requires-expressions;
- ranges;
- views;
- projections;
- `std::span`;
- formatting;
- chrono moderno;
- mejoras de `constexpr`;
- cambios relevantes de C++20.

Debe complementarse con documentación actual cuando se estudien modules, coroutines y soporte real de compiladores.

### C++23 — The Complete Guide

**Autor:** Nicolai M. Josuttis
**Rol:** Referencia especializada para C++23.

Debe priorizarse para:

- `std::expected`;
- `std::print`;
- `std::println`;
- `std::mdspan`;
- `ranges::to`;
- `zip_view`;
- `adjacent_view`;
- `chunk_view`;
- `slide_view`;
- `stride_view`;
- deducing `this`;
- explicit object parameters;
- `if consteval`;
- mejoras de `constexpr`;
- mejoras de la biblioteca estándar;
- cambios específicos de C++23.

Debe contrastarse con cppreference y fuentes normativas cuando el soporte dependa de la versión de GCC, Clang o libstdc++.

## 7. Diseño moderno de C++

### Effective Modern C++

**Autor:** Scott Meyers
**Rol:** Profundización para Bloques 2–3.

Especialmente relevante para:

- type deduction;
- `auto`;
- `decltype`;
- references;
- forwarding references;
- `std::move`;
- `std::forward`;
- move semantics;
- perfect forwarding;
- smart pointers;
- lambdas;
- buenas prácticas de C++ moderno.

La terminología histórica del libro debe contextualizarse cuando el estándar moderno utilice una terminología diferente.

## 8. Templates y programación genérica

### C++ Templates: The Complete Guide — Second Edition

**Autores:** David Vandevoorde, Nicolai M. Josuttis, Douglas Gregor
**Edición:** 2nd Edition
**Rol:** Fuente principal del Bloque 5.

Debe utilizarse para:

- function templates;
- class templates;
- variable templates;
- alias templates;
- template argument deduction;
- specialization;
- partial specialization;
- dependent names;
- `typename`;
- `template` keyword;
- two-phase lookup;
- variadic templates;
- parameter packs;
- pack expansion;
- SFINAE;
- type traits;
- metaprogramming;
- expression templates.

Para Concepts y `requires`, debe complementarse con fuentes posteriores a C++17.

## 9. Concurrencia

### C++ Concurrency in Action — Second Edition

**Autor:** Anthony Williams
**Edición:** 2nd Edition
**Rol:** Fuente principal del Bloque 6.

Debe utilizarse para:

- threads;
- synchronization;
- mutexes;
- condition variables;
- futures;
- promises;
- atomics;
- memory model;
- happens-before;
- acquire/release;
- sequential consistency;
- lock-free programming;
- diseño concurrente.

Para características posteriores al estándar cubierto directamente por el libro debe complementarse con cppreference y documentación normativa.

Especialmente:

- `std::jthread`;
- `std::stop_token`;
- semaphores;
- latches;
- barriers;
- atomic wait/notify.

## 10. Referencia permanente online

### cppreference

**Recurso:** cppreference.com
**Rol:** Referencia técnica permanente.

Debe consultarse durante prácticamente todo el PATH para:

- signatures;
- overloads;
- tipos;
- requisitos;
- feature-test macros;
- versiones del estándar;
- comportamiento de biblioteca;
- iterator invalidation;
- exception guarantees;
- concurrency;
- atomics;
- ranges;
- concepts;
- soporte de características modernas.

cppreference no sustituye al estándar ISO C++ como autoridad normativa.

## 11. Estándar ISO C++

### ISO/IEC 14882 — Programming Languages — C++

**Rol:** Referencia normativa.

Debe utilizarse especialmente en los Bloques 4–8 cuando sea necesario determinar con precisión:

- comportamiento normativo;
- terminology;
- object model;
- lifetime;
- value categories;
- templates;
- overload resolution;
- memory model;
- undefined behavior;
- implementation-defined behavior;
- unspecified behavior;
- library requirements.

## 12. WG21

### WG21 Papers

**Rol:** Fuente avanzada.

Los papers de WG21 deben utilizarse para comprender:

- motivación de nuevas características;
- evolución del lenguaje;
- diseño de Concepts;
- Ranges;
- Coroutines;
- Modules;
- cambios de C++23;
- propuestas futuras;
- defect reports;
- evolución de la biblioteca estándar.

Cuando una característica tenga diferencias entre propuesta y estándar final, debe priorizarse el texto finalmente adoptado.

## 13. GCC

### GCC Documentation

Fuente primaria para:

- compilación;
- warnings;
- optimización;
- sanitizers;
- extensiones;
- linking;
- ABI;
- feature support;
- opciones relacionadas con C++.

El PATH utilizará normalmente:

```bash
g++ -std=c++23
```

## 14. Clang/LLVM

### Clang Documentation

Fuente primaria para:

- `clang++`;
- diagnostics;
- warnings;
- sanitizers;
- tooling;
- AST;
- static analysis;
- `clang-tidy`;
- `clang-format`;
- soporte de estándares.

## 15. ABI

### Itanium C++ ABI

Referencia principal para el estudio práctico del ABI utilizado por GCC/Clang en muchas plataformas ELF.

Especialmente relevante para:

- name mangling;
- vtables;
- RTTI;
- exception handling;
- object layout;
- virtual dispatch;
- guard variables;
- construction/destruction;
- ABI de clases.

Debe utilizarse especialmente en el Bloque 7.

## 16. ELF y toolchain

Para el Bloque 7 deben utilizarse también como documentación técnica:

- GNU Binutils;
- GNU `ld`;
- `nm`;
- `readelf`;
- `objdump`;
- `c++filt`;
- GDB;
- GCC;
- Clang/LLVM;
- glibc cuando corresponda;
- libstdc++.

## 17. Debugging y análisis dinámico

### GDB Documentation

Fuente principal para debugging, breakpoints, stack frames, templates, excepciones, threads y core dumps.

### Sanitizers

Utilizar documentación de GCC y LLVM para:

- AddressSanitizer;
- UndefinedBehaviorSanitizer;
- ThreadSanitizer.

### Valgrind

Utilizar la documentación oficial para análisis dinámico complementario.

## 18. Build systems e ingeniería

### CMake
Documentación oficial como fuente principal para CMake.

### Meson
Documentación oficial como fuente principal para Meson.

### GNU Make
GNU Make Manual como referencia para Make.

## 19. Testing

### GoogleTest

Documentación oficial para:

- test cases;
- assertions;
- fixtures;
- integración con CMake;
- CTest.

## 20. Profiling

### Linux perf

Documentación del kernel Linux y herramientas `perf`.

## 21. Fedora y RPM

Para las partes específicas de Fedora utilizar:

- Fedora Documentation;
- Fedora Packaging Guidelines;
- RPM documentation;
- GCC empaquetado por Fedora;
- Clang/LLVM empaquetado por Fedora;
- CMake;
- Meson;
- pkg-config.

## 22. Distribución de fuentes por bloques

| Bloque | Fuente principal | Complementarias |
|---|---|---|
| 1 | Programming: Principles and Practice Using C++ 3e | A Tour of C++ 3e, C++ Primer 5e |
| 2 | C++ Primer 5e / Effective Modern C++ | A Tour of C++ 3e, TC++PL |
| 3 | C++17 — The Complete Guide | Effective Modern C++, A Tour 3e |
| 4 | C++20/C++23 — The Complete Guide | A Tour 3e, cppreference, ISO C++, WG21 |
| 5 | C++ Templates 2e | cppreference, ISO C++, WG21 |
| 6 | C++ Concurrency in Action 2e | cppreference, ISO C++, WG21 |
| 7 | documentación técnica y ABI | GCC, Clang, GDB, Binutils, Itanium ABI |
| 8 | documentación oficial de herramientas | CMake, Meson, GCC, Clang, GoogleTest, perf, Fedora/RPM |

## 23. Formato 📚 LECTURA

Cada lección debe contener una sección `📚 LECTURA` con referencias específicas para esa lección.

Formato conceptual (mismas categorías que profile.yaml):

```text
📚 LECTURA
Principal: fuente pedagógica específica del tema.
Complementaria: segunda explicación o perspectiva.
Normativa: estándar y sección verificada aplicable.
Profundización: tratamiento avanzado del tema.
Consulta: API, documentación del compilador o herramienta.
```

En YAML, «profundizacion» es el identificador de «Profundización».
Las fuentes de C++ moderno y de herramientas se incluyen en la categoría que
corresponda a su función; no constituyen categorías adicionales obligatorias.

No es obligatorio rellenar artificialmente todas las categorías.

## 24. Política bibliográfica

El generador debe:

1. elegir fuentes relacionadas directamente con la lección;
2. evitar referencias genéricas a libros completos cuando pueda identificar capítulos o secciones;
3. diferenciar material pedagógico de material normativo;
4. utilizar documentación actual para C++20 y C++23;
5. comprobar características dependientes del compilador;
6. distinguir lenguaje estándar de extensiones GCC/Clang;
7. no presentar cppreference como estándar normativo;
8. utilizar WG21 principalmente para evolución y diseño;
9. utilizar el estándar ISO cuando la precisión normativa sea importante;
10. utilizar documentación oficial para herramientas externas.

Las referencias bibliográficas deben apoyar la lección, no sustituir su explicación.

## 25. Expresiones regulares aplicadas a C++ — Bloque 9

**Alcance:** API, semántica, limitaciones, rendimiento y pruebas de regex en C++. Los fundamentos formales y las técnicas generales de patrones pertenecen al PATH independiente de Regex.

- **cppreference — Regular expressions library (`<regex>`)**: fuente de consulta principal para `std::basic_regex`, `std::regex_match`, `std::regex_search`, `std::regex_replace`, `std::match_results`, iteradores y opciones de coincidencia. Verificar firmas y requisitos por estándar.
- **ISO/IEC 14882 — C++ standard, regular expressions library**: autoridad normativa para gramáticas admitidas, comportamiento, errores y garantías.
- **GCC libstdc++ documentation y LLVM libc++ documentation**: compatibilidad, diferencias y limitaciones de implementación.
- **PCRE2 API documentation**: referencia complementaria para integrar PCRE2 como dependencia externa, distinguiendo claramente su API de `std::regex`.
- **GoogleTest documentation y CMake documentation**: pruebas y construcción del proyecto del bloque.

No atribuir a `std::regex` características de PCRE2 ni prometer soporte Unicode pleno. Las referencias exactas a capítulos/secciones solo se darán cuando estén verificadas.

## 26. Complejidad algorítmica aplicada a C++ — Bloque 10

- **Cormen, Leiserson, Rivest y Stein — Introduction to Algorithms**: referencia de profundización para análisis, estructuras de datos y algoritmos; la teoría general se estudia en el PATH independiente Big-O.
- **cppreference — Containers library y Algorithms library**: consulta principal de garantías de complejidad de operaciones y algoritmos de la STL.
- **ISO/IEC 14882 — C++ standard library requirements**: referencia normativa para requisitos de complejidad, precondiciones y garantías.
- **The C++ Programming Language (Stroustrup)** y **A Tour of C++ (Stroustrup)**: criterios de diseño y selección de contenedores.
- **GCC optimization options / Clang optimization documentation**: efectos del compilador en rendimiento real.
- **Linux perf documentation**: medición de eventos de CPU y perfiles.
- **Google Benchmark documentation**: metodología de microbenchmarks, cuando se incorpore como dependencia opcional.

Distinguir complejidad asintótica, garantías de la biblioteca, coste amortizado y rendimiento medido. No extrapolar benchmarks particulares como garantías universales.

## 27. Mapa adicional de fuentes

| Bloque | Fuente principal | Complementarias |
|---|---|---|
| 9 | cppreference `<regex>` y estándar ISO C++ | libstdc++, libc++, PCRE2, GoogleTest |
| 10 | cppreference STL y estándar ISO C++ | CLRS, Stroustrup, GCC/Clang, perf, Google Benchmark |

## 28. Integración transversal de Regex y Big-O

En las lecciones 1.25 (parsing), 1.28–1.29 (algoritmos y contenedores), 3.26–3.29 (STL e iteradores), 4.7–4.11 (Ranges), 8.17–8.20 (profiling y optimización) y 8.26 (proyecto final), introducir conexiones breves y referencias cruzadas a los bloques 9 y 10 sin duplicar sus contenidos.


## 29. Fuentes para las ampliaciones

| Lecciones | Fuentes y propósito |
|---|---|
| 1.42–1.52 | PPP3 y C++ Primer 5e: tipos, expresiones, funciones y streams; contrastar reglas con C++23 |
| 1.53–1.55 | Manuales oficiales GCC/Clang, CMake y CTest: primera compilación y pruebas |
| 2.41–2.56 | C++ Primer, Effective Modern C++, TC++PL y texto normativo C++23: semántica, lifetime y diseño |
| 3.31–3.42 | C++17 Complete Guide, TC++PL y especificación de biblioteca: STL, allocators y PMR |
| 4.45–4.59 | C++20/C++23 Complete Guide y documentación del toolchain: constraints, ranges, coroutines y módulos |
| 5.30–5.39 | C++ Templates 2e, C++20 Complete Guide y texto normativo: instanciación y diseño genérico |
| 6.37–6.46 | Concurrency in Action 2e y especificación C++23: sincronización, progreso y lifetime |
| 7.40–7.47 | Binutils, GCC, libstdc++, glibc, GDB y LLVM: enlace, carga, ABI y diagnóstico |
| 8.27–8.36 | CMake/CTest, GoogleTest, LLVM libFuzzer, Google Benchmark y Fedora: ingeniería reproducible |
| 9.31–9.34 | Especificación regex de C++23, libstdc++/libc++ y PCRE2: lifetime, entradas y limitaciones |
| 10.42–10.47 | Requisitos de complejidad de C++23 y Google Benchmark/perf: contratos y medición |

## 30. Referencias oficiales localizables

- Documentos WG21: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/
- Borrador N4950, referencia pública de C++23:
  https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/n4950.pdf
- CMake y CTest: https://cmake.org/cmake/help/latest/
- GCC: https://gcc.gnu.org/onlinedocs/
- libstdc++: https://gcc.gnu.org/onlinedocs/libstdc++/
- Clang: https://clang.llvm.org/docs/
- libc++: https://libcxx.llvm.org/docs/
- GNU Binutils: https://sourceware.org/binutils/docs/
- GDB: https://sourceware.org/gdb/current/onlinedocs/gdb.html
- Itanium C++ ABI: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
- GoogleTest: https://google.github.io/googletest/
- Google Benchmark: https://github.com/google/benchmark
- LLVM libFuzzer: https://llvm.org/docs/LibFuzzer.html
- PCRE2: https://www.pcre.org/current/doc/html/

Estas direcciones identifican las fuentes; antes de generar comandos dependientes
de versión, consultar la documentación correspondiente a la versión instalada.
Los enlaces latest y current evolucionan y no son una especificación congelada.

## 31. Límites normativos y bibliográficos

Para el estándar objetivo usar texto de C++23 (por ejemplo N4950 como borrador
público de referencia); no sustituirlo sin aviso por el borrador vivo, que puede
incluir características posteriores. Identificar defect reports cuando cambien
la interpretación. ISO/IEC 14882 sigue siendo la autoridad normativa publicada.

El libro C++23 — The Complete Guide de Nicolai M. Josuttis está identificado en
la web del autor: https://www.cppstd23.com/cppstd23.html . Registrar la edición
realmente consultada al citarlo, sin inventar paginación. Los libros anteriores
a C++20 necesitan complemento para las incorporaciones posteriores.

Para hazard pointers y reclamación por épocas, usar las publicaciones originales
de las técnicas y documentación de la biblioteca externa elegida; no presentar
propuestas WG21 ni APIs posteriores como parte de C++23. Para fuzzing y benchmarks,
la documentación oficial de cada herramienta define sus propias interfaces.
