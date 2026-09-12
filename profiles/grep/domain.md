# GREP EN PROFUNDIDAD — domain.md

## 1. Identidad del PATH

**Nombre:** GREP EN PROFUNDIDAD
**Plataforma principal:** Fedora Linux
**Herramientas centrales:** GNU grep y ripgrep (`rg`)
**Herramientas relacionadas:** git grep, find, shell, sed, AWK, journalctl, RPM/DNF y utilidades Unix relacionadas.

Este PATH estudia la búsqueda de texto desde el punto de vista de las herramientas que la ejecutan: selección de entrada, recorrido de archivos, filtrado, coincidencias, contexto, salida, integración Unix, robustez, rendimiento, arquitectura interna y automatización.

El objetivo final no es solamente conocer opciones de `grep` y `rg`, sino poder diseñar, explicar, diagnosticar, optimizar y automatizar búsquedas reales sobre Fedora, repositorios de código y grandes árboles de archivos.

## 2. Relación con el PATH de Regex

Las expresiones regulares constituyen un **PATH independiente** y son un prerrequisito conceptual de este curso.

Este PATH NO debe convertirse en un segundo curso completo de Regex.

Cuando aparezcan BRE, ERE, PCRE2 o el motor regex de ripgrep, deben estudiarse desde la perspectiva específica de `grep`/`rg`:

- qué dialecto o motor utiliza la herramienta;
- cómo se selecciona;
- qué características admite;
- qué características no admite;
- diferencias observables entre motores;
- portabilidad;
- implicaciones de rendimiento;
- implicaciones de Unicode y locale;
- consecuencias prácticas para una búsqueda;
- cómo diagnosticar una expresión que funciona en un motor y no en otro.

Los conceptos generales de Regex —sintaxis, teoría, construcción de patrones, lookaround, backtracking, autómatas, etc.— pueden recordarse brevemente cuando sean necesarios, pero su enseñanza exhaustiva pertenece al PATH de Regex.

Los bloques existentes sobre BRE, ERE, PCRE2 y teoría de motores deben conservarse porque explican comportamiento específico de GNU grep y ripgrep, pero evitando duplicar innecesariamente el PATH independiente de Regex.

## 3. Alcance

El PATH cubre, de cero a nivel experto:

- fundamentos Unix de entrada/salida y filtros;
- GNU grep;
- búsqueda literal;
- BRE y ERE en GNU grep;
- múltiples patrones;
- contexto;
- búsqueda recursiva;
- nombres de archivo y formatos de salida;
- archivos binarios;
- separación NUL-safe;
- integración con Bash y Zsh;
- pipelines Unix;
- integración con find;
- relación con sed y AWK;
- PCRE2 cuando GNU grep lo soporte;
- locale, UTF-8 y Unicode;
- rendimiento y benchmarking;
- ripgrep;
- motor regex predeterminado de ripgrep;
- PCRE2 en ripgrep;
- reglas `.gitignore`, `.ignore` y `.rgignore`;
- globs;
- tipos de archivo;
- archivos ocultos y especiales;
- búsquedas multilínea;
- reemplazo mostrado por ripgrep;
- descubrimiento de archivos;
- configuración de ripgrep;
- búsqueda en proyectos de código;
- Git y `git grep`;
- comparación GNU grep / ripgrep / git grep;
- logs y journal systemd;
- investigación de Fedora;
- RPM;
- búsquedas defensivas orientadas a seguridad;
- diseño eficiente de búsquedas;
- robustez frente a casos extremos;
- automatización avanzada;
- internals de GNU grep;
- internals de ripgrep;
- teoría de motores aplicada a estas herramientas;
- salida JSON de ripgrep;
- construcción de herramientas encima de `rg`;
- proyecto final `grep-rg-debugger`.

## 4. Entorno preferente

Todo el contenido práctico debe priorizar Fedora Linux.

Cuando corresponda, deben utilizarse herramientas y mecanismos reales de Fedora:

```text
rpm
dnf
dnf repoquery
journalctl
systemctl
find
grep
rg
git
zgrep
time
hyperfine
```

También deben utilizarse árboles reales cuando sean apropiados:

```text
/etc
/usr
/var
/proc
/sys
```

Debe explicarse cuándo NO es seguro o conveniente recorrer indiscriminadamente estos árboles.

## 5. GNU grep

GNU grep debe estudiarse como herramienta propia, no simplemente como una interfaz para Regex.

Las lecciones deben distinguir claramente:

```text
grep
grep -E
grep -F
grep -P
```

y explicar su semántica, portabilidad y casos de uso.

También deben cubrirse:

- exit status;
- stdin;
- múltiples archivos;
- múltiples patrones;
- archivos de patrones;
- salida;
- contexto;
- recursividad;
- include/exclude;
- binarios;
- NUL;
- locale;
- scripting;
- rendimiento;
- arquitectura interna.

Las formas históricas `egrep` y `fgrep` deben tratarse como contexto histórico y no como recomendación moderna.

## 6. ripgrep

ripgrep debe estudiarse como herramienta completa y no simplemente como "`grep` más rápido".

Debe explicarse especialmente:

- recursividad predeterminada;
- reglas de ignore;
- archivos ocultos;
- binarios;
- globs;
- tipos;
- paralelismo;
- Unicode;
- motor regex predeterminado;
- PCRE2 opcional;
- multiline;
- configuración;
- salida estructurada;
- integración con repositorios;
- arquitectura interna;
- decisiones de rendimiento.

Las diferencias con GNU grep deben presentarse como diferencias de diseño, no como una clasificación simplista de herramienta mejor/peor.

## 7. git grep

`git grep` forma parte del dominio como herramienta comparativa y especializada.

Debe enseñarse:

- dónde encaja;
- qué información obtiene del repositorio;
- working tree frente a historial;
- diferencias con `rg`;
- diferencias con GNU grep;
- relación con `git log -G`;
- relación con `git log -S`.

No debe transformarse este PATH en un curso general de Git.

## 8. Shell y pipelines

El curso debe enseñar el uso correcto de grep/rg como componentes de pipelines Unix.

Debe prestarse atención a:

- quoting;
- expansión del shell;
- patrones procedentes de variables;
- argumentos que empiezan por `-`;
- `--`;
- exit status;
- `pipefail`;
- `set -e`;
- command substitution;
- NUL-safe pipelines;
- diferencias entre salida para humanos y salida para máquinas.

Zsh es el shell preferido para laboratorios de automatización avanzada, sin excluir conceptos portables de shell cuando corresponda.

Los scripts reutilizables deben preferirse como funciones Zsh modulares cuando esto sea apropiado.

## 9. Relación con find, sed y AWK

El curso debe enseñar fronteras de responsabilidad.

`find` debe utilizarse principalmente para selección por metadata y recorrido cuando sus capacidades sean necesarias.

`grep`/`rg` deben utilizarse principalmente para selección por contenido.

`sed` debe aparecer cuando se necesita transformación de streams.

AWK debe aparecer cuando se necesita procesamiento estructurado por registros/campos o lógica más compleja.

No debe duplicarse la enseñanza completa de find, sed o AWK, pues pueden disponer de PATH propios.

## 10. Datos, archivos y robustez

El alumno debe comprender que "texto" no equivale siempre a una secuencia sencilla de líneas.

Deben estudiarse:

- newline;
- NUL;
- archivos binarios;
- UTF-8;
- caracteres multibyte;
- UTF-8 inválido;
- archivos sin newline final;
- líneas enormes;
- archivos enormes;
- FIFOs;
- dispositivos;
- symlinks;
- ciclos;
- permisos;
- archivos modificados durante una búsqueda;
- nombres con espacios, tabs y newlines.

La robustez debe formar parte del diseño de los comandos, no ser un añadido posterior.

## 11. Locale y Unicode

Las lecciones deben diferenciar cuidadosamente:

- bytes;
- caracteres;
- codificación;
- UTF-8;
- locale;
- `LANG`;
- `LC_ALL`;
- `LC_CTYPE`;
- `LC_COLLATE`;
- clases POSIX;
- rangos;
- Unicode.

`LC_ALL=C` no debe recomendarse mecánicamente como optimización. Debe explicarse que puede cambiar la semántica y solo debe utilizarse cuando sea correcto para los datos y el objetivo de la búsqueda.

## 12. Rendimiento

El rendimiento debe estudiarse experimentalmente.

Deben considerarse:

- I/O;
- CPU;
- filesystem cache;
- tamaño del dataset;
- número de archivos;
- patrones literales;
- expresiones regulares;
- motor utilizado;
- locale;
- exclusiones;
- recorrido;
- paralelismo;
- cold cache;
- warm cache.

Los benchmarks deben intentar mantener equivalencia semántica entre herramientas.

Cuando se utilice `hyperfine`, `time` u otra herramienta de medición, deben explicarse las variables que pueden invalidar una comparación.

## 13. Motores Regex aplicados

El curso puede profundizar en:

- motores basados en autómatas;
- NFA;
- DFA;
- Thompson NFA;
- backtracking;
- búsqueda de literales;
- prefiltros;
- Aho-Corasick;
- SIMD;
- PCRE2;
- `regex`;
- `regex-automata`.

La teoría debe estar conectada directamente con GNU grep o ripgrep.

El PATH de Regex conserva la responsabilidad sobre la teoría general y exhaustiva de expresiones regulares.

## 14. Internals

El nivel experto incluye investigación del código fuente.

Para GNU grep se estudiarán conceptualmente:

- lectura de entrada;
- compilación de patrones;
- matching;
- fixed strings;
- regex;
- integración PCRE2;
- optimizaciones;
- candidatos;
- locale;
- buffering;
- salida;
- implementación de opciones.

Para ripgrep se estudiarán:

- organización del proyecto;
- Rust;
- recorrido paralelo;
- `ignore`;
- `regex`;
- `regex-automata`;
- crates `grep-*`;
- detección de archivos;
- decodificación;
- búsqueda;
- impresión;
- paralelismo;
- estrategias de lectura;
- memory mapping cuando corresponda;
- SIMD cuando corresponda;
- optimizaciones literales;
- integración PCRE2.

Las afirmaciones sobre internals deben contrastarse con la versión del código/documentación estudiada.

## 15. Fedora como campo de investigación

Las búsquedas prácticas deben progresar hacia investigación real del sistema:

- configuración;
- unidades systemd;
- journal;
- OpenSSH;
- firewalld;
- SELinux;
- paquetes RPM;
- SPEC;
- Requires;
- Provides;
- macros;
- scriptlets;
- logs de build;
- mock;
- rpmlint;
- Koji;
- código fuente.

Estos dominios sirven como datasets y casos de uso. El PATH no debe intentar sustituir cursos completos de RPM, SELinux, systemd, OpenSSH o firewalld.

## 16. Seguridad

Las búsquedas orientadas a seguridad son defensivas y de investigación.

Pueden incluir detección de:

- IP;
- dominios;
- URL;
- hashes;
- correos;
- posibles secretos;
- tokens;
- contraseñas accidentalmente almacenadas;
- material que parezca una clave privada.

Debe insistirse en:

- falsos positivos;
- validación;
- privacidad;
- minimización de exposición de datos;
- tratamiento responsable de resultados.

Una coincidencia textual nunca debe presentarse automáticamente como prueba de una vulnerabilidad o compromiso.

## 17. Automatización

El nivel avanzado debe enseñar a convertir búsquedas ad hoc en herramientas reproducibles.

Se incluyen:

- funciones Zsh;
- wrappers;
- parámetros;
- selección de paths;
- selección de tipos;
- patrones dinámicos;
- exit codes;
- salida machine-readable;
- `rg --json`;
- JSON Lines;
- integración con otras herramientas;
- frontends propios.

Debe distinguirse claramente una configuración interactiva personal de una ejecución reproducible en scripts.

## 18. Proyecto final

El proyecto final es:

**grep-rg-debugger — mini motor de investigación de texto para Fedora y código fuente.**

Debe integrar progresivamente los conocimientos del PATH.

Como mínimo debe poder razonar sobre:

- patrón;
- paths;
- GNU grep/ripgrep;
- literal/BRE/ERE/PCRE2 cuando corresponda;
- motores disponibles;
- archivos considerados;
- archivos ignorados;
- reglas ignore;
- hidden files;
- binarios;
- symlinks;
- tipos;
- globs;
- multiline;
- coincidencias;
- contexto;
- estadísticas;
- duración;
- comparación de herramientas;
- comparación de motores;
- patrones potencialmente caros;
- comando reproducible;
- salida humana;
- salida JSON;
- integración Zsh;
- árboles reales de Fedora;
- repositorios Git reales.

El proyecto debe ser utilizable con datos reales y no limitarse a ejemplos artificiales.

## 19. Política pedagógica

Cada lección debe ser autocontenida respecto a su objetivo concreto, pero mantener continuidad con el PATH.

Debe comenzar siempre con:

**🎯 OBJETIVO**

y terminar siempre con:

**🧠 QUÉ DEBES RECORDAR**

con entre 3 y 7 ideas esenciales.

Cuando aporten valor deben utilizarse:

- 🧪 Laboratorio/ejemplos
- ⚠️ Errores frecuentes
- 💡 Idea importante

No deben generarse scaffolds genéricos ni texto de relleno.

Los encabezados, ejemplos, comandos y explicaciones deben ser específicos del tema de la lección.

## 20. Lecturas

Cada lección requiere `📚 LECTURA`.

Las categorías son:

- Principal
- Normativa
- Motor
- Profundización
- Consulta

Solo deben indicarse capítulos, secciones o referencias exactas cuando hayan sido verificadas.

No deben inventarse números de capítulo, páginas, nombres de secciones o URLs.

## 21. Límites explícitos del dominio

Este PATH NO es:

- un curso completo de Regex;
- un curso completo de Bash/Zsh;
- un curso completo de sed;
- un curso completo de AWK;
- un curso completo de find;
- un curso completo de Git;
- un curso completo de Rust;
- un curso completo de C;
- un curso completo de administración Fedora;
- un curso completo de seguridad ofensiva.

Esos conocimientos se incorporan únicamente en la profundidad necesaria para comprender, utilizar, diagnosticar o extender GNU grep y ripgrep.

## 22. Criterio de dominio

Al finalizar, el alumno debe poder responder no solo:

> "¿Qué opción necesito?"

sino también:

> "¿Qué archivos se están examinando, qué motor interpreta el patrón, qué semántica tiene, qué datos se están excluyendo, qué efecto tienen locale/Unicode, qué coste tiene la búsqueda, qué casos extremos pueden romperla y cómo puedo reproducir y diagnosticar el resultado?"

Ese es el nivel de profundidad esperado en todo el PATH.
