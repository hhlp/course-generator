# GREP EN PROFUNDIDAD — bibliography.md

## 1. Política bibliográfica

Esta bibliografía acompaña al PATH **GREP EN PROFUNDIDAD** sobre Fedora Linux.

Las fuentes deben priorizarse en este orden conceptual:

1. documentación oficial de la herramienta;
2. especificaciones y documentación normativa;
3. documentación oficial del motor o biblioteca implicada;
4. código fuente y documentación técnica del proyecto;
5. documentación de Fedora para integración con el sistema;
6. bibliografía de profundización;
7. fuentes auxiliares de consulta.

Las lecciones deben evitar referencias exactas no verificadas. No deben inventarse capítulos, secciones, páginas, opciones ni comportamiento de una versión concreta.

Dado que Regex dispone de un PATH independiente, la bibliografía general de expresiones regulares pertenece principalmente a ese PATH. Aquí se conservan las fuentes necesarias para entender cómo GNU grep y ripgrep implementan y utilizan sus respectivos dialectos y motores.

---

## 2. Principal — GNU grep

### GNU Project — GNU Grep Manual

Fuente principal para GNU grep.

Utilizar para:

- invocación;
- matching;
- opciones;
- BRE;
- ERE;
- fixed strings;
- salida;
- contexto;
- recursividad;
- binarios;
- locale;
- comportamiento;
- exit status;
- aspectos de rendimiento documentados;
- diferencias y extensiones GNU.

Debe ser la referencia principal en las lecciones centradas específicamente en GNU grep.

### GNU grep — código fuente oficial

Fuente primaria para las lecciones de arquitectura interna.

Utilizar para investigar:

- implementación;
- flujo de búsqueda;
- fixed-string matching;
- regex matching;
- integración con PCRE2;
- buffering;
- manejo de archivos;
- optimizaciones;
- implementación de opciones;
- evolución entre versiones.

Las explicaciones de internals deben corresponder a la versión examinada.

---

## 3. Principal — ripgrep

### BurntSushi — ripgrep

Repositorio y documentación oficial del proyecto ripgrep.

Fuente principal para:

- `rg`;
- comportamiento predeterminado;
- recursividad;
- ignore files;
- globs;
- tipos;
- hidden files;
- binarios;
- Unicode;
- multiline;
- PCRE2;
- configuración;
- salida;
- `--json`;
- rendimiento;
- arquitectura;
- decisiones de diseño.

Debe consultarse también:

- README;
- FAQ;
- GUIDE;
- CHANGELOG;
- documentación incluida en el repositorio;
- ayuda de `rg`;
- manual instalado cuando esté disponible.

### `rg --help`

Fuente operativa fundamental.

Debe utilizarse para comprobar la disponibilidad y semántica de opciones en la versión instalada.

### `man rg`

Fuente local de consulta en Fedora cuando el paquete instalado proporcione la página de manual.

---

## 4. Normativa — POSIX

### The Open Group — POSIX / Base Specifications

Referencia normativa para los aspectos portables de `grep` y expresiones regulares POSIX.

Utilizar especialmente para:

- utilidad `grep`;
- Basic Regular Expressions;
- Extended Regular Expressions;
- locale;
- clases de caracteres;
- comportamiento portable;
- exit status;
- diferencias entre POSIX y extensiones GNU.

Las lecciones deben distinguir explícitamente:

```text
POSIX
GNU extension
ripgrep-specific
PCRE2-specific
```

cuando la distinción sea relevante.

---

## 5. Motor — PCRE2

### PCRE2 Project — documentación oficial

Fuente primaria para las características PCRE2 utilizadas mediante GNU grep o ripgrep.

Utilizar para:

- sintaxis PCRE2;
- lookahead;
- lookbehind;
- backreferences;
- `\K`;
- Unicode;
- opciones del motor;
- matching;
- restricciones;
- rendimiento;
- comportamiento dependiente de versión.

No debe asumirse que toda característica documentada por PCRE2 está necesariamente expuesta de la misma manera por `grep -P` o `rg -P`.

La herramienta concreta sigue siendo responsable de su integración con PCRE2.

---

## 6. Motor — Rust regex

### Rust `regex` crate — documentación oficial

Fuente primaria para comprender el motor utilizado por ripgrep cuando corresponda.

Utilizar para:

- sintaxis admitida;
- Unicode;
- clases;
- grupos;
- alternancia;
- cuantificadores;
- anchors;
- word boundaries;
- características deliberadamente no soportadas;
- garantías y decisiones de rendimiento.

Debe ser especialmente importante para el bloque dedicado al motor regex predeterminado de ripgrep.

### `regex-automata` — documentación oficial

Fuente de profundización para la arquitectura moderna del ecosistema regex utilizado por ripgrep.

Utilizar para:

- autómatas;
- construcción de motores;
- estrategias de búsqueda;
- DFA;
- NFA;
- híbridos;
- prefiltros;
- arquitectura interna;
- trade-offs memoria/tiempo.

Las explicaciones deben ajustarse a las versiones realmente utilizadas por la versión de ripgrep estudiada.

---

## 7. Motor — ecosistema grep de Rust

### crates `grep-*` utilizados por ripgrep

Consultar el código y documentación del ecosistema de crates empleado por ripgrep para separar responsabilidades como:

- búsqueda;
- matching;
- impresión;
- parsing;
- selección de archivos;
- decodificación;
- integración de motores.

Esta fuente es especialmente relevante para:

**44. Arquitectura interna de ripgrep**

y para:

**46. Construir herramientas sobre ripgrep**

---

## 8. Ignore y recorrido

### Rust `ignore` crate — documentación y código oficial

Fuente principal para estudiar:

- recorrido paralelo;
- `.gitignore`;
- `.ignore`;
- `.rgignore`;
- archivos ocultos;
- reglas de exclusión;
- jerarquías;
- selección de archivos.

Debe utilizarse para explicar por qué ripgrep puede no examinar un archivo que GNU grep sí examinaría bajo una invocación aparentemente similar.

---

## 9. Git

### Git Documentation — `git grep`

Fuente principal para:

- `git grep`;
- opciones;
- alcance de búsqueda;
- integración con repositorios;
- diferencias respecto a búsquedas sobre el filesystem.

### Git Documentation — `git log`

Fuente principal para:

- `git log -G`;
- `git log -S`;
- búsqueda en historial;
- diferencias entre buscar el working tree y buscar cambios históricos.

Git se utiliza como herramienta relacionada; la bibliografía general de Git queda fuera del alcance de este PATH.

---

## 10. Fedora

### Fedora Documentation

Referencia para el contexto operativo del curso.

Utilizar cuando corresponda para:

- paquetes;
- instalación;
- administración del sistema;
- journal;
- herramientas disponibles;
- integración con Fedora.

### RPM documentation

Referencia para los laboratorios que utilizan:

```text
rpm -ql
rpm -qa
rpm -q --requires
rpm -q --provides
```

y para interpretar correctamente los datos sobre los que se realizan búsquedas.

### DNF documentation

Referencia para `dnf` y `dnf repoquery` cuando se utilicen como fuentes de datos para grep/rg.

### systemd documentation / manual pages

Referencia principal para `journalctl` y para comprender correctamente los datos de los laboratorios sobre journal y unidades.

Este PATH utiliza estas herramientas como fuentes de datos; su enseñanza exhaustiva pertenece a sus respectivos PATH.

---

## 11. Shell y entorno Unix

### GNU Bash Reference Manual

Referencia auxiliar cuando una lección necesite explicar:

- quoting;
- pipelines;
- redirecciones;
- exit status;
- variables;
- command substitution;
- comportamiento del shell que afecta a grep.

### Zsh Documentation

Referencia preferente para las automatizaciones Zsh del curso.

Utilizar para:

- funciones;
- parámetros;
- arrays cuando sean necesarios;
- quoting;
- expansión;
- módulos reutilizables;
- construcción del módulo final de búsqueda.

El curso no debe transformarse en un curso completo de Bash o Zsh.

---

## 12. Herramientas Unix relacionadas

### GNU Findutils Manual

Referencia para:

- `find`;
- `-exec`;
- `-print0`;
- selección de archivos por metadata;
- integración segura con grep.

### GNU Coreutils Manual

Referencia auxiliar para herramientas utilizadas en pipelines, entre ellas:

- `sort`;
- `uniq`;
- `cut`;
- `tr`;
- otras utilidades cuando corresponda.

### GNU sed Manual

Referencia auxiliar cuando se compare filtrado con transformación o se combine grep/rg con sed.

### GNU Gawk Manual

Referencia auxiliar cuando se compare grep con procesamiento estructurado mediante AWK.

La enseñanza exhaustiva de find, Coreutils, sed y AWK pertenece a PATH independientes cuando existan.

---

## 13. Benchmarking

### `time` — documentación correspondiente a la implementación utilizada

Referencia básica para mediciones temporales.

### hyperfine — documentación oficial

Referencia recomendada para benchmarks reproducibles de comandos.

Utilizar para:

- warmup;
- múltiples ejecuciones;
- comparación de comandos;
- interpretación responsable de resultados.

Los resultados de benchmark deben acompañarse de descripción del dataset, filesystem, cache, versión de las herramientas, locale y motores utilizados cuando estos factores puedan afectar a la comparación.

---

## 14. Profundización — expresiones regulares

### Jeffrey E. F. Friedl — *Mastering Regular Expressions*

Referencia clásica de profundización para comprender:

- motores regex;
- backtracking;
- eficiencia;
- comportamiento de diferentes familias de motores.

Su contenido general pertenece principalmente al PATH de Regex. En GREP EN PROFUNDIDAD debe utilizarse cuando ayude a explicar diferencias observables entre motores utilizados por grep/rg.

### Michael Fitzgerald — *Introducing Regular Expressions: Unraveling Regular Expressions, Step-by-Step*

Referencia complementaria y progresiva para consolidar la lectura, construcción y comprensión práctica de expresiones regulares.

En GREP EN PROFUNDIDAD debe utilizarse como apoyo cuando una lección de GNU grep o ripgrep necesite recordar o aplicar conceptos de Regex sin volver a desarrollar desde cero el PATH independiente de Regex.

Es especialmente útil como puente entre el uso práctico de patrones y las particularidades que después introduce cada herramienta o motor.

### Russ Cox — artículos sobre regular expression matching

Material de profundización especialmente útil para:

- Thompson NFA;
- backtracking;
- complejidad;
- comparación conceptual de implementaciones regex.

Debe conectarse con los motores realmente estudiados y no utilizarse para sustituir su documentación oficial.

---

## 15. Profundización — algoritmos de búsqueda

Para los bloques expertos pueden consultarse textos académicos y documentación primaria sobre:

- finite automata;
- NFA;
- DFA;
- Thompson construction;
- substring search;
- Aho-Corasick;
- prefiltros;
- vectorización/SIMD;
- complejidad temporal y espacial.

Estas fuentes deben utilizarse para comprender las decisiones internas de GNU grep y ripgrep, no para convertir el PATH en un curso general de teoría de autómatas.

---

## 16. Source code archaeology

Para los bloques:

```text
43. Arquitectura interna de GNU grep
44. Arquitectura interna de ripgrep
45. grep, rg y teoría de motores regex
46. Construir herramientas sobre ripgrep
```

la bibliografía primaria debe incluir código fuente real.

El procedimiento recomendado es:

1. identificar la versión instalada;
2. identificar la versión/tag correspondiente del código;
3. localizar la opción o subsistema estudiado;
4. seguir llamadas y estructuras relevantes;
5. contrastar con documentación;
6. construir un experimento mínimo;
7. verificar el comportamiento;
8. documentar qué parte es observable y qué parte procede de la implementación.

No deben afirmarse detalles internos únicamente por intuición.

---

## 17. Documentación local en Fedora

Antes de recurrir a fuentes secundarias, el curso debe fomentar la investigación local:

```bash
grep --version
grep --help
man grep
info grep

rg --version
rg --help
man rg

rpm -qi grep
rpm -ql grep

rpm -qi ripgrep
rpm -ql ripgrep
```

También puede utilizarse:

```bash
apropos grep
man -k grep
```

cuando sea útil para descubrir documentación relacionada.

La versión instalada es importante porque opciones, motores y comportamiento pueden evolucionar.

---

## 18. Jerarquía recomendada por categoría de LECTURA

La sección `📚 LECTURA` de cada lección debe utilizar las categorías definidas por el perfil.

### Principal

Normalmente:

- GNU Grep Manual, para GNU grep;
- documentación oficial de ripgrep, para `rg`.

### Normativa

Normalmente:

- POSIX, cuando exista comportamiento estandarizado relevante.

### Motor

Según la lección:

- PCRE2;
- Rust `regex`;
- `regex-automata`;
- `ignore`;
- crates `grep-*`.

### Profundización

Según el tema:

- código fuente;
- Friedl;
- Russ Cox;
- literatura de algoritmos/autómatas;
- documentación de implementación.

### Consulta

Según el laboratorio:

- Fedora;
- RPM;
- DNF;
- systemd;
- Git;
- Zsh;
- Bash;
- Findutils;
- Coreutils;
- sed;
- Gawk;
- hyperfine.

No es obligatorio rellenar artificialmente todas las categorías con fuentes irrelevantes. La selección debe ser específica de la lección.

---

## 19. Política de referencias exactas

El generador debe aplicar la siguiente regla:

> Una referencia específica es mejor que una referencia genérica solamente cuando ha sido verificada.

Por tanto:

- no inventar páginas;
- no inventar capítulos;
- no inventar nombres de secciones;
- no atribuir una característica a una versión sin comprobarla;
- no asumir que GNU grep y POSIX grep son equivalentes;
- no asumir que `grep -P` equivale directamente a invocar PCRE2;
- no asumir que el motor predeterminado de ripgrep admite características de PCRE2;
- no asumir que una descripción antigua de los internals sigue siendo válida.

Cuando no pueda verificarse una referencia más precisa, debe citarse honestamente la fuente a un nivel más general.

---

## 20. Mapa bibliográfico del PATH

| Área | Fuente prioritaria |
|---|---|
| GNU grep | GNU Grep Manual |
| grep portable | POSIX |
| BRE/ERE en grep | GNU Grep Manual + POSIX |
| `grep -P` | GNU grep + PCRE2 |
| ripgrep | documentación oficial de ripgrep |
| regex predeterminado de rg | Rust `regex` |
| internals regex de rg | `regex-automata` |
| ignores/recorrido rg | `ignore` crate + ripgrep |
| PCRE2 en rg | ripgrep + PCRE2 |
| Git | Git Documentation |
| Fedora | Fedora Documentation |
| RPM | RPM documentation |
| DNF | DNF documentation |
| journal | systemd documentation |
| find | GNU Findutils |
| pipelines | manuales GNU + shell |
| Zsh | Zsh Documentation |
| benchmarking | hyperfine + `time` |
| teoría regex | PATH Regex + Friedl + Russ Cox |
| internals GNU grep | código fuente GNU grep |
| internals ripgrep | código fuente ripgrep y crates asociados |
| proyecto final | conjunto de las fuentes anteriores |

---

## 21. Referencias bibliográficas base

- GNU Project. **GNU Grep Manual**.
- GNU Project. **GNU grep source code and project documentation**.
- The Open Group. **POSIX / The Open Group Base Specifications**.
- BurntSushi. **ripgrep — official project documentation and source code**.
- Rust ecosystem. **regex crate documentation**.
- Rust ecosystem. **regex-automata documentation**.
- Rust ecosystem. **ignore crate documentation**.
- PCRE2 Project. **PCRE2 documentation**.
- Git Project. **Git Documentation**.
- Fedora Project. **Fedora Documentation**.
- RPM Project. **RPM documentation**.
- DNF Project. **DNF documentation**.
- systemd Project. **systemd manual pages and documentation**.
- GNU Project. **GNU Findutils Manual**.
- GNU Project. **GNU Coreutils Manual**.
- GNU Project. **GNU sed Manual**.
- GNU Project. **GNU Gawk Manual**.
- GNU Project. **GNU Bash Reference Manual**.
- Zsh Project. **Zsh Documentation**.
- Fitzgerald, Michael. **Introducing Regular Expressions: Unraveling Regular Expressions, Step-by-Step**.
- Friedl, Jeffrey E. F. **Mastering Regular Expressions**.
- Cox, Russ. **Regular Expression Matching** articles.
- hyperfine project. **Official documentation**.

---

## 22. Criterio final

La bibliografía debe permitir que cada lección pueda responder tres preguntas:

1. **¿Qué comportamiento documenta oficialmente la herramienta?**
2. **¿Qué parte procede de una norma, motor, biblioteca o implementación concreta?**
3. **¿Cómo podemos verificar ese comportamiento en Fedora y, cuando sea necesario, en el código fuente?**

Ese criterio debe mantenerse desde las primeras búsquedas con `grep` hasta el proyecto final `grep-rg-debugger`.
