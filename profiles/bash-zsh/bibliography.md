# BIBLIOGRAPHY — BASH + ZSH EN PROFUNDIDAD

## 1. Criterio bibliográfico

La bibliografía del PATH se divide en cinco categorías compatibles con `profile.yaml`:

- **Principal** — material pedagógico base para aprender Bash y Zsh.
- **Normativa** — especificaciones que definen comportamiento portable o contractual.
- **Motor** — documentación y código fuente de los propios shells para internals.
- **Profundización** — obras y guías para ampliar diseño, uso avanzado y práctica.
- **Consulta** — manuales, man pages y documentación auxiliar para resolver dudas concretas.

Las fuentes oficiales y normativas tienen prioridad sobre libros o tutoriales cuando exista una discrepancia técnica.

---

# 2. PRINCIPAL

## P1. GNU Bash Reference Manual

**Autoría:** GNU Project / Free Software Foundation; Bash mantenido por Chet Ramey y colaboradores.
**Obra:** *Bash Reference Manual*.
**Versión de referencia actual verificada:** Bash 5.3, Edition 5.3, 18 May 2025.

Uso principal:

- fundamentos del shell;
- sintaxis Bash;
- quoting;
- shell parameters;
- shell expansions;
- redirections;
- pipelines;
- compound commands;
- arrays;
- arithmetic;
- functions;
- builtins;
- shell options;
- job control;
- invocation y startup;
- programmable completion;
- Bash-specific features.

Debe ser la fuente principal para cualquier afirmación específica sobre Bash.

---

## P2. The Z Shell Manual

**Autoría original:** Paul Falstad; Zsh Development Group y colaboradores.
**Obra:** *The Z Shell Manual*.
**Versión de referencia actual verificada:** Zsh 5.9.2, updated/released 12 July 2026.

Uso principal:

- sintaxis Zsh;
- shell grammar;
- parameters;
- arrays;
- expansion;
- filename generation;
- globbing extendido;
- glob qualifiers;
- options;
- functions;
- `autoload` y `fpath`;
- modules;
- ZLE;
- completion system;
- `zstyle`;
- prompts;
- history;
- job control;
- emulation modes.

Debe ser la fuente principal para cualquier afirmación específica sobre Zsh.

---

## P3. Kiddle, Oliver; Peek, Jerry; Stephenson, Peter — From Bash to Z Shell

**Título:** *From Bash to Z Shell: Conquering the Command Line*.
**Editorial:** Apress.
**Edición:** 1st edition.
**Publicación:** 2004/2005.
**ISBN:** 978-1-59059-376-9.

Uso recomendado:

- transición conceptual Bash ↔ Zsh;
- uso interactivo;
- command-line editing;
- history;
- completion;
- expansión;
- shell functions;
- comparación de ambos shells.

Aunque la obra es anterior a las versiones actuales, sigue siendo especialmente valiosa por tratar Bash y Zsh conjuntamente. Los detalles dependientes de versión deben verificarse en los manuales upstream actuales.

---

# 3. NORMATIVA

## N1. POSIX.1-2024 — Shell Command Language

**Organización:** The Open Group / IEEE.
**Estándar:** POSIX.1-2024.
**Sección principal:** Shell Command Language.

Uso obligatorio para:

- sintaxis portable de `sh`;
- token recognition;
- quoting POSIX;
- parameter expansion POSIX;
- command substitution;
- arithmetic expansion portable;
- field splitting;
- pathname expansion;
- redirections;
- pipelines;
- lists;
- compound commands;
- functions POSIX;
- environment y command search;
- exit status;
- comportamiento de utilities shell definidas por POSIX.

No debe utilizarse POSIX para atribuir a Bash o Zsh extensiones que el estándar no define.

---

## N2. POSIX.1-2024 — Base Definitions

**Organización:** The Open Group / IEEE.

Uso recomendado para conceptos transversales:

- environment variables;
- pathname;
- process;
- terminal;
- utility conventions;
- locale;
- regular expression definitions cuando una utilidad POSIX las requiera.

---

# 4. MOTOR

## M1. GNU Bash source tree

**Proyecto:** GNU Bash.
**Fuente:** código fuente upstream correspondiente a la versión estudiada.

Uso:

- lexer/parser;
- ejecución de comandos;
- expansión;
- variables;
- builtins;
- redirecciones;
- jobs;
- señales;
- Readline integration;
- tracing de implementación.

La estructura interna puede cambiar entre versiones. Los nombres de archivos, funciones y estructuras deben verificarse contra el source utilizado antes de incluirse en una lección.

---

## M2. Zsh source tree

**Proyecto:** Zsh.
**Fuente:** código fuente upstream correspondiente a la versión estudiada.

Uso:

- lexer/parser;
- execution engine;
- parameter subsystem;
- globbing;
- jobs;
- signals;
- modules;
- ZLE;
- completion internals.

Al igual que en Bash, las referencias concretas al source deben verificarse contra la versión real.

---

## M3. Bash CHANGES / NEWS / release documentation

Uso:

- determinar cuándo apareció una característica;
- comprobar cambios incompatibles;
- identificar comportamiento dependiente de versión;
- estudiar evolución del shell.

No sustituye al Reference Manual para describir el comportamiento vigente.

---

## M4. Zsh NEWS / ChangeLog / release documentation

Uso equivalente para:

- cambios entre versiones;
- nuevas opciones;
- cambios en completion, ZLE, globbing o módulos;
- compatibilidad.

---

# 5. PROFUNDIZACIÓN

## D1. Newham, Cameron — Learning the bash Shell, 3rd Edition

**Título:** *Learning the bash Shell, Third Edition*.
**Autor:** Cameron Newham.
**Editorial:** O'Reilly Media.
**Publicación:** March 2005.
**ISBN:** 978-0-596-00965-6.

Uso recomendado:

- introducción pedagógica a Bash;
- uso interactivo;
- shell programming;
- variables;
- control structures;
- processes;
- customization;
- debugging.

La edición cubre una generación anterior de Bash; cualquier detalle específico de versión debe contrastarse con el GNU Bash Reference Manual actual.

---

## D2. Albing, Carl; Vossen, JP — bash Cookbook, 2nd Edition

**Título:** *bash Cookbook, 2nd Edition*.
**Autores:** Carl Albing, JP Vossen.
**Editorial:** O'Reilly Media.
**Publicación:** October 2017.

Uso recomendado:

- patrones prácticos;
- administración y automatización;
- quoting;
- procesos;
- entrada/salida;
- CLI;
- scripting real;
- recetas que después deben explicarse desde el modelo formal del shell.

No debe convertirse en fuente normativa cuando contradiga documentación upstream.

---

## D3. Kochan, Stephen G.; Wood, Patrick — Shell Programming in Unix, Linux and OS X, 4th Edition

**Editorial:** Addison-Wesley Professional.
**Edición:** 4th.
**Publicación:** 2016.
**ISBN-13:** 978-0-13-449668-9 (eBook) / 978-0-13-449600-9 (print).

Uso recomendado:

- fundamentos de programación shell;
- POSIX shell;
- modelo Unix;
- scripts portables;
- debugging;
- relación entre shell y utilities.

Útil especialmente en bloques de portabilidad y fundamentos previos a extensiones Bash/Zsh.

---

## D4. Stephenson, Peter — A User's Guide to the Z-Shell

**Autor:** Peter Stephenson.
**Obra:** *A User's Guide to the Z-Shell*.
**Fecha:** 2003.

Uso recomendado:

- startup files;
- opciones;
- parámetros;
- arrays;
- history;
- prompts;
- aliases;
- features interactivas;
- explicación pedagógica de Zsh.

Es una guía histórica muy valiosa pero no reemplaza al manual Zsh 5.9.2 para comportamiento actual.

---

# 6. CONSULTA

## C1. `man bash`

Referencia local de la versión instalada de Bash.

Debe consultarse especialmente cuando se quiera contrastar el manual upstream con el binario y documentación realmente instalados en Fedora.

Comandos útiles:

```bash
man bash
info bash
help
help <builtin>
type <name>
```

---

## C2. `man zsh` y manuales Zsh por sección

Zsh distribuye su documentación en varias páginas de manual especializadas.

Consultar según disponibilidad de la versión instalada, por ejemplo:

```bash
man zsh
man zshmisc
man zshexpn
man zshparam
man zshoptions
man zshbuiltins
man zshmodules
man zshzle
man zshcompsys
man zshcompwid
```

La lista exacta debe comprobarse mediante el paquete instalado.

---

## C3. Fedora Packages — bash

Uso:

- versión empaquetada en Fedora;
- subpaquetes;
- mantenedores;
- metadatos del paquete;
- relación con `bash-doc`.

Comandos locales complementarios:

```bash
rpm -q bash
rpm -qi bash
rpm -ql bash
rpm -q bash-doc
```

---

## C4. Fedora Packages — zsh

Uso:

- versión empaquetada;
- documentación disponible;
- subpaquete `zsh-html`;
- diferencias entre Fedora estable y Rawhide cuando sean relevantes.

Comandos locales:

```bash
rpm -q zsh
rpm -qi zsh
rpm -ql zsh
rpm -q zsh-html
```

---

## C5. ShellCheck documentation

**Proyecto:** ShellCheck, Vidar Holen y colaboradores.

Uso:

- análisis estático de `sh` y Bash;
- quoting;
- errores semánticos frecuentes;
- robustness;
- portability;
- integración con CI.

Limitación importante:

ShellCheck no es una especificación del lenguaje y su soporte se centra en dialectos Bourne-style como `sh`, Bash, Dash, Ksh y BusyBox. No debe utilizarse como autoridad general sobre semántica nativa de Zsh.

---

## C6. `help`, `type`, `command`, `whence` y experimentación controlada

La introspección del propio shell forma parte de las fuentes de consulta práctica.

Bash:

```bash
help
type -a name
command -V name
shopt
set -o
```

Zsh:

```zsh
whence -va name
which -a name
setopt
zmodload
```

Los experimentos deben utilizarse para verificar y comprender, no para sustituir documentación cuando el comportamiento esté formalmente definido.

---

# 7. HERRAMIENTAS AUXILIARES

Estas fuentes/herramientas son complementarias y no forman la autoridad normativa del PATH:

- ShellCheck;
- shfmt;
- Bats;
- ShellSpec;
- hyperfine;
- `strace`;
- `lsof`;
- `perf`;
- `gdb`;
- `ps` / `pstree`;
- `/proc`;
- Git para inspección del código fuente y evolución histórica.

---

# 8. ASIGNACIÓN DE FUENTES POR ÁREA

| Área | Fuente prioritaria |
|---|---|
| Fundamentos del shell | POSIX + GNU Bash Manual + Zsh Manual |
| Sintaxis portable | POSIX.1-2024 |
| Bash básico/avanzado | GNU Bash Reference Manual |
| Bash interactivo | GNU Bash Manual + `man bash` |
| Zsh básico/avanzado | The Z Shell Manual |
| Zsh interactivo | Zsh Manual + User's Guide |
| Comparación Bash/Zsh | From Bash to Z Shell + manuales actuales |
| Portabilidad | POSIX + ShellCheck como herramienta auxiliar |
| Seguridad | manuales upstream + análisis explícito del contexto |
| Internals Bash | source tree Bash + documentación de release |
| Internals Zsh | source tree Zsh + documentación de release |
| Fedora | Fedora Packages + RPM local |
| Completion Bash | Bash Manual + bash-completion cuando corresponda |
| Completion Zsh | Zsh `compsys`/`compwid` manual |
| ZLE | Zsh ZLE manual |
| Testing | Bats / ShellSpec + herramientas estándar |
| Profiling | `time`, hyperfine, zprof, perf/strace según nivel |

---

# 9. POLÍTICA DE REFERENCIAS EN LAS LECCIONES

La sección `📚 LECTURA` debe elegir solo fuentes relevantes.

Ejemplo conceptual para una lección Bash:

```text
📚 LECTURA

Principal:
GNU Bash Reference Manual — sección verificada correspondiente

Normativa:
POSIX.1-2024 — solo si el comportamiento estudiado es POSIX

Motor:
GNU Bash source — únicamente en lecciones de implementación/internals

Profundización:
bash Cookbook / Learning the bash Shell — cuando aporte contexto pedagógico

Consulta:
man bash / help builtin
```

Ejemplo conceptual para Zsh:

```text
📚 LECTURA

Principal:
The Z Shell Manual — sección verificada correspondiente

Normativa:
POSIX.1-2024 — únicamente para comparar comportamiento portable

Motor:
Zsh source tree — en internals

Profundización:
From Bash to Z Shell / A User's Guide to the Z-Shell

Consulta:
man zsh... correspondiente
```

No se deben inventar números de capítulo, nodos o secciones para completar artificialmente una referencia.

---

# 10. POLÍTICA DE ACTUALIZACIÓN

Antes de generar un bloque cuya precisión dependa de versión:

1. identificar la versión de Bash/Zsh objetivo;
2. comprobar documentación upstream;
3. comprobar la versión empaquetada por Fedora si el laboratorio depende de ella;
4. preferir conceptos estables cuando no sea necesaria una versión concreta;
5. registrar cambios relevantes de versión en la propia lección.

La bibliografía puede actualizarse sin modificar la arquitectura pedagógica del PATH cuando aparezcan nuevas versiones de Bash, Zsh o POSIX.
