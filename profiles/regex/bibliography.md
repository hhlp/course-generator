# REGEX EN PROFUNDIDAD — bibliography.md

## 1. Política bibliográfica

Esta bibliografía acompaña al PATH **REGEX EN PROFUNDIDAD**.

El curso es deliberadamente agnóstico respecto a lenguajes de programación y herramientas. Las fuentes deben utilizarse para enseñar primero el modelo conceptual de las expresiones regulares y, después, distinguir de forma explícita aquello que depende de un dialecto, motor o implementación concreta.

Prioridad recomendada:

1. bibliografía principal de Regex;
2. especificaciones normativas cuando exista comportamiento estandarizado;
3. documentación oficial del dialecto o motor cuando una característica no sea universal;
4. documentación técnica de implementaciones para internals, rendimiento y seguridad;
5. documentación local de Fedora únicamente como entorno práctico de experimentación.

No se deben inventar páginas, capítulos, nombres de secciones, restricciones de versión ni características de un motor. Las referencias exactas solo deben utilizarse cuando hayan sido verificadas.

---

## 2. Bibliografía principal

### Michael Fitzgerald — *Introducing Regular Expressions: Unraveling Regular Expressions, Step-by-Step*

Fuente principal de introducción progresiva.

Utilizar especialmente para:

- fundamentos;
- patrón, texto y match;
- literales y metacaracteres;
- clases de caracteres;
- cuantificadores;
- anclas;
- grupos y capturas;
- alternancia;
- primeras técnicas de construcción;
- lectura progresiva de patrones;
- sustitución y aplicaciones prácticas cuando corresponda.

Su función dentro del PATH es proporcionar una transición clara desde cero hacia el dominio operativo de Regex.

### Jeffrey E. F. Friedl — *Mastering Regular Expressions*

Fuente principal de profundización conceptual y de comportamiento de motores.

Utilizar especialmente para:

- semántica de matching;
- funcionamiento de motores;
- motores dirigidos por regex y por texto;
- NFA y DFA desde la perspectiva práctica;
- backtracking;
- greedy/lazy;
- capturas y backreferences;
- optimización;
- eficiencia;
- diseño de expresiones;
- diferencias entre implementaciones;
- razonamiento sobre la ejecución de patrones.

Debe utilizarse para explicar el **porqué** del comportamiento, no solamente la sintaxis.

### Jan Goyvaerts & Steven Levithan — *Regular Expressions Cookbook*

Fuente principal para técnicas, patrones y resolución sistemática de problemas.

Utilizar especialmente para:

- construcción práctica de regex;
- técnicas de matching y extracción;
- lookaround;
- grupos y backreferences;
- Unicode;
- sustitución;
- problemas clásicos;
- técnicas avanzadas;
- diferencias entre dialectos;
- portabilidad;
- soluciones alternativas a un mismo problema;
- selección consciente de características según el motor.

Debe evitarse convertir las recetas en patrones memorizados: cada solución debe explicarse desde su semántica y sus restricciones.

---

## 3. Normativa — POSIX

### The Open Group — POSIX / Base Specifications

Fuente normativa para Basic Regular Expressions y Extended Regular Expressions.

Utilizar para:

- POSIX BRE;
- POSIX ERE;
- bracket expressions;
- character classes POSIX;
- interval expressions;
- anchors;
- subexpressions;
- backreferences cuando correspondan;
- semántica POSIX;
- leftmost-longest;
- locale;
- portabilidad.

Debe distinguirse siempre entre lo definido por POSIX y las extensiones de implementaciones concretas.

---

## 4. Motor y dialecto — PCRE2

### PCRE2 Project — documentación oficial

Fuente primaria cuando el PATH estudie características modernas o específicas de PCRE2.

Utilizar para verificar:

- grupos con nombre;
- lookahead y lookbehind;
- restricciones y evolución del lookbehind;
- grupos atómicos;
- cuantificadores posesivos;
- backreferences;
- subrutinas;
- recursión;
- condicionales;
- branch-reset groups;
- duplicate names cuando estén permitidos;
- `\K`;
- `\G` cuando corresponda;
- quoting como `\Q...\E` cuando corresponda;
- control verbs;
- backtracking control verbs;
- callouts;
- Unicode;
- JIT;
- límites configurables;
- comportamiento dependiente de versión.

PCRE2 debe presentarse como un dialecto/motor concreto, no como sinónimo de Regex.

---

## 5. Motores basados en autómatas

### RE2 — documentación y código oficial

Fuente de referencia para estudiar un modelo deliberadamente distinto de los motores tradicionales de backtracking.

Utilizar para:

- matching con garantías de tiempo distintas;
- ausencia deliberada de determinadas extensiones;
- seguridad frente a expresividad;
- autómatas;
- límites de memoria;
- comparación conceptual con motores tipo PCRE.

### Rust `regex` / `regex-automata` — documentación oficial

Fuentes complementarias para estudiar implementaciones modernas basadas en múltiples estrategias de autómatas.

Utilizar cuando sea útil para comprender:

- Thompson NFA;
- PikeVM;
- DFA;
- lazy DFA;
- híbridos;
- one-pass matching cuando corresponda;
- prefiltros;
- literal extraction;
- estrategias de búsqueda;
- trade-offs entre memoria y tiempo.

El PATH no depende de Rust como lenguaje; estas fuentes se utilizan exclusivamente como documentación de motores.

---

## 6. Teoría de lenguajes y autómatas

Para las lecciones teóricas deben utilizarse fuentes académicas o documentación técnica fiable sobre:

- alfabetos;
- cadenas;
- lenguajes;
- lenguajes regulares;
- álgebra regular;
- conjunto vacío y cadena vacía;
- unión;
- concatenación;
- estrella y cierre de Kleene;
- autómatas finitos;
- NFA;
- DFA;
- construcción de Thompson;
- subset construction;
- equivalencia entre expresiones regulares clásicas y autómatas finitos;
- minimización de DFA a nivel conceptual;
- pumping lemma como herramienta conceptual;
- límites de los lenguajes regulares.

La teoría debe utilizarse para explicar comportamiento práctico, rendimiento y límites, no para transformar el PATH en un curso independiente de teoría de computación.

---

## 7. Unicode

### Unicode Consortium — Unicode Standard y Unicode Technical Standards/Reports relevantes

Fuente normativa para conceptos Unicode utilizados por Regex.

Utilizar para verificar:

- code points;
- code units;
- combining marks;
- normalization;
- general categories;
- scripts;
- properties;
- case mapping y case folding;
- grapheme clusters;
- extended grapheme clusters;
- word boundaries cuando corresponda;
- emoji y secuencias de caracteres.

Las características Regex concretas como `\p{...}` o `\X` deben verificarse además contra el motor que las implemente.

---

## 8. Rendimiento y arquitectura de motores

### Russ Cox — artículos sobre Regular Expression Matching

Fuente complementaria especialmente útil para:

- Thompson NFA;
- comparación entre enfoques basados en autómatas y backtracking;
- complejidad;
- comportamiento patológico;
- diseño de motores;
- relación entre expresividad y garantías de rendimiento.

Debe conectarse con motores reales y con las limitaciones de cada implementación.

Para bloques expertos también puede consultarse documentación primaria y literatura técnica sobre:

- regex parsing;
- AST;
- compilación de patrones;
- simplificación y optimización;
- Thompson construction;
- Pike VM;
- DFA completo;
- lazy DFA;
- motores híbridos;
- prefiltros;
- literal extraction;
- required literals;
- prefix/suffix acceleration;
- JIT;
- complejidad temporal y espacial.

---

## 9. Seguridad — ReDoS

Para catastrophic backtracking y Regular Expression Denial of Service deben priorizarse fuentes técnicas y de seguridad que permitan estudiar:

- ambigüedad;
- cuantificadores anidados;
- alternativas solapadas;
- crecimiento lineal, polinómico y exponencial;
- entradas adversarias;
- attacker-controlled input;
- límites de ejecución;
- límites de memoria;
- auditoría de patrones;
- motores con garantías distintas de complejidad;
- mitigaciones mediante rediseño, atomicidad o cuantificadores posesivos cuando proceda.

No deben construirse ejemplos peligrosos contra servicios reales; los laboratorios deben ejecutarse de forma controlada y local.

---

## 10. Fedora como laboratorio

Fedora Linux es el entorno práctico preferido, pero no define la semántica general de Regex.

Cuando una lección necesite ejecutar o comparar motores, debe documentarse:

- herramienta utilizada;
- versión;
- dialecto;
- motor;
- flags/modos;
- locale;
- Unicode mode cuando corresponda.

Herramientas como `grep`, `rg`, `sed` o `awk` pueden utilizarse puntualmente como bancos de pruebas, pero su enseñanza exhaustiva pertenece a sus respectivos PATH.

---

## 11. Jerarquía recomendada para 📚 LECTURA

### Principal

Según la lección:

- Fitzgerald;
- Friedl;
- Goyvaerts & Levithan.

### Normativa

Según corresponda:

- POSIX;
- Unicode Standard.

### Motor

Según corresponda:

- PCRE2;
- RE2;
- Rust `regex` / `regex-automata`;
- documentación oficial de otra implementación utilizada explícitamente por la lección.

### Profundización

Según el tema:

- Friedl;
- Russ Cox;
- literatura de autómatas y lenguajes formales;
- documentación técnica/código fuente de motores.

### Consulta

Solo cuando sea relevante para un laboratorio:

- documentación local de Fedora;
- manual de la herramienta utilizada como banco de pruebas.

No es obligatorio utilizar artificialmente todas las categorías en cada lección.

---

## 12. Política de referencias exactas

Una referencia específica debe utilizarse únicamente cuando haya sido verificada.

Por tanto:

- no inventar páginas;
- no inventar capítulos;
- no inventar nombres de secciones;
- no atribuir sintaxis universal a una extensión particular;
- no asumir que PCRE2 representa a todos los motores;
- no asumir que POSIX BRE y ERE son equivalentes;
- no asumir que `\w`, `\d`, `.`, `\b`, `^` o `$` tienen semántica idéntica en todos los motores;
- no asumir soporte de lookbehind, backreferences, atomicidad, posesividad, recursión o control verbs sin verificarlo;
- no asumir que una descripción de internals corresponde a versiones distintas de la estudiada.

---

## 13. Mapa bibliográfico del PATH

| Área | Fuente prioritaria |
|---|---|
| Introducción y progresión | Fitzgerald |
| Semántica y motores | Friedl |
| Técnicas y recetas | Goyvaerts & Levithan |
| POSIX BRE/ERE | POSIX / The Open Group |
| PCRE2 | documentación oficial PCRE2 |
| Unicode | Unicode Consortium + documentación del motor |
| motores lineales/autómatas | RE2 + documentación técnica |
| motores modernos híbridos | `regex` / `regex-automata` |
| Thompson NFA y rendimiento | Friedl + Russ Cox + fuentes técnicas |
| teoría formal | literatura académica de lenguajes/autómatas |
| ReDoS | documentación técnica/seguridad + documentación del motor |
| portabilidad | POSIX + documentación de los motores comparados |
| proyecto Regex Analyzer | conjunto de las fuentes anteriores |

---

## 14. Referencias bibliográficas base

- Fitzgerald, Michael. **Introducing Regular Expressions: Unraveling Regular Expressions, Step-by-Step**.
- Friedl, Jeffrey E. F. **Mastering Regular Expressions**.
- Goyvaerts, Jan; Levithan, Steven. **Regular Expressions Cookbook**.
- The Open Group. **POSIX / Base Specifications — Regular Expressions**.
- PCRE2 Project. **PCRE2 documentation**.
- Unicode Consortium. **The Unicode Standard and relevant Unicode Technical Reports/Standards**.
- Google. **RE2 documentation and source code**.
- Rust ecosystem. **regex and regex-automata documentation**.
- Cox, Russ. **Regular Expression Matching** articles.

---

## 15. Criterio final

Cada lección debe poder responder:

1. ¿Qué significa conceptualmente esta construcción?
2. ¿Qué texto consume y qué condiciones solamente comprueba?
3. ¿Es parte del núcleo regular clásico, de POSIX o una extensión moderna?
4. ¿Qué depende del dialecto o del motor?
5. ¿Cómo afecta al backtracking, rendimiento o seguridad cuando corresponda?
6. ¿Cómo puede verificarse el comportamiento sin confundir la herramienta de prueba con Regex como concepto?

Ese criterio debe mantenerse desde el primer literal hasta el Regex Analyzer final.


## 16. Ediciones de trabajo y enlaces concretos

Las ediciones siguientes identifican el material de trabajo; no se presentan
como una afirmación de última edición disponible. Los libros proporcionan
fundamentos y técnicas. La sintaxis actual se contrasta con el motor utilizado.

- Michael Fitzgerald, *Introducing Regular Expressions*, O'Reilly.
  https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/
- Jeffrey E. F. Friedl, *Mastering Regular Expressions*, 3.ª edición, O'Reilly.
  https://www.oreilly.com/library/view/mastering-regular-expressions/0596528124/
- Jan Goyvaerts y Steven Levithan, *Regular Expressions Cookbook*, 2.ª edición.
  https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/
- The Open Group, POSIX.1-2024, Base Definitions, capítulo 9, Regular Expressions.
  https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap09.html
- PCRE2, sintaxis y semántica del patrón.
  https://www.pcre.org/current/doc/html/pcre2pattern.html
- PCRE2, comparación de algoritmos de matching.
  https://www.pcre.org/current/doc/html/pcre2matching.html
- PCRE2, Unicode y propiedades.
  https://www.pcre.org/current/doc/html/pcre2unicode.html
- RE2, documentación del proyecto y garantías.
  https://github.com/google/re2
- Rust regex, documentación del motor y complejidad.
  https://docs.rs/regex/latest/regex/
- Rust regex-automata, arquitectura y estrategias.
  https://docs.rs/regex-automata/latest/regex_automata/
- Unicode, UTS #18: Unicode Regular Expressions.
  https://www.unicode.org/reports/tr18/
- Unicode, UAX #15: Unicode Normalization Forms.
  https://www.unicode.org/reports/tr15/
- Unicode, UAX #29: Unicode Text Segmentation.
  https://www.unicode.org/reports/tr29/
- Russ Cox, *Regular Expression Matching Can Be Simple And Fast*.
  https://swtch.com/~rsc/regexp/regexp1.html
- Russ Cox, *Regular Expression Matching: the Virtual Machine Approach*.
  https://swtch.com/~rsc/regexp/regexp2.html
- Russ Cox, *Regular Expression Matching in the Wild*.
  https://swtch.com/~rsc/regexp/regexp3.html

Para fundamentos formales complementar Cox y regex-automata con estas fuentes
académicas primarias de acceso abierto:

- Michael Sipser, MIT OpenCourseWare, 18.404J, Theory of Computation, Fall 2020.
  Lecciones 1 a 3: autómatas, equivalencias, cierre y pumping lemma regular.
  https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/pages/lecture-notes/
- Ryan Williams, MIT, 6.1400 / 18.400, curso 2025.
  La programación identifica DFA Minimization; consultar sus materiales.
  https://people.csail.mit.edu/rrw/6.1400-2025/index.html

No inventar páginas ni atribuir temas a artículos que no los desarrollen.
No se exige una compra adicional para seguir el PATH.

## 17. Uso de fuentes en las ampliaciones

| Tema | Fuente prioritaria | Precaución |
|---|---|---|
| Selección de subcoincidencias y locale | POSIX, capítulo 9 | Separar estándar y extensión |
| Longitud de lookbehind | PCRE2 pattern y matching | Registrar versión y función |
| Atomicidad de aserciones | PCRE2 pattern | Separar evaluación y reentrada |
| UTF y UCP | PCRE2 Unicode | Son opciones diferentes |
| Equivalencia canónica | UTS #18 y UAX #15 | No asumir normalización automática |
| Segmentación y grafemas | UAX #29 y manual del motor | No equiparar toda frontera a \b |
| Complejidad y autómatas | Cox, RE2 y regex-automata | Declarar patrón y entrada |
| Recorrido de matches | Manual de la herramienta usada | Avance vacío y offsets explícitos |

Los enlaces current/latest pueden cambiar. Cada laboratorio registra la versión
real utilizada y consulta la documentación correspondiente. Este mapa no implica
que se hayan ejecutado todos los motores ni verificado todas las recetas.
