# DOMAIN — BASH + ZSH EN PROFUNDIDAD

## 1. Propósito del PATH

Este PATH enseña Bash y Zsh desde los fundamentos del shell Unix hasta un nivel experto de uso interactivo, scripting, depuración, rendimiento, seguridad, extensibilidad e internals.

El objetivo no es memorizar comandos aislados. El alumno debe construir un modelo mental correcto de cómo un shell:

- lee y tokeniza una línea de comandos;
- analiza sintaxis;
- realiza expansiones;
- aplica quoting y word splitting;
- resuelve nombres de comandos;
- configura redirecciones y pipelines;
- crea, sustituye y espera procesos;
- maneja señales, jobs y terminales;
- ejecuta builtins, funciones y programas externos;
- mantiene entorno, variables, opciones, historial y estado interactivo.

El PATH debe permitir comprender qué comportamiento pertenece a POSIX `sh`, qué es específico de Bash y qué es específico de Zsh.

## 2. Entorno de referencia

Plataforma principal: Fedora Linux.

Los ejemplos y laboratorios deben priorizar herramientas, rutas, paquetes y convenciones disponibles en Fedora. Cuando una característica dependa de la versión instalada, debe comprobarse mediante comandos como:

```bash
bash --version
zsh --version
rpm -q bash zsh
rpm -qi bash zsh
rpm -ql bash
rpm -ql zsh
```

No debe asumirse que el comportamiento observado en otro sistema operativo o distribución es idéntico al de Fedora.

## 3. Alcance funcional

El PATH cubre de forma progresiva:

1. fundamentos de shell, terminal, TTY, procesos, entorno y file descriptors;
2. sintaxis, quoting, parámetros, variables y expansiones;
3. globbing, arrays, aritmética, redirecciones y pipelines;
4. condicionales, bucles, funciones, scripts y bibliotecas;
5. procesos, job control, señales y process substitution;
6. programación defensiva, seguridad, debugging, testing y logging;
7. configuración, startup, prompt, historial y completion de Bash;
8. características avanzadas e internals de Bash;
9. Zsh nativo, opciones, expansiones, globbing y arrays;
10. `fpath`, `autoload`, hooks, ZLE, `compsys`, módulos y plugins de Zsh;
11. rendimiento interactivo y de scripting;
12. portabilidad POSIX/Bash/Zsh;
13. integración con systemd, SSH, contenedores, automatización y CI;
14. internals, código fuente, tracing y profiling;
15. diseño de CLIs, librerías, dotfiles, frameworks y toolkits de producción.

## 4. Política de dialectos

Toda lección debe distinguir explícitamente entre:

- POSIX shell (`sh`);
- Bash;
- Zsh.

Nunca debe enseñarse una extensión de Bash o Zsh como si fuera una propiedad universal del shell.

Cuando proceda, debe indicarse:

- si la sintaxis es POSIX;
- si requiere Bash;
- si requiere Zsh;
- si Zsh la implementa únicamente bajo determinado modo u opción;
- si Bash cambia su comportamiento en modo POSIX;
- si existen diferencias de indexación, splitting, globbing o expansión.

Ejemplos especialmente sensibles:

- `[[ ... ]]`;
- arrays y associative arrays;
- process substitution;
- `=~`;
- `shopt`;
- `extglob`;
- `globstar`;
- `nullglob`/`failglob`;
- `coproc`;
- `declare -n`;
- Zsh parameter expansion flags;
- Zsh glob qualifiers;
- `setopt`/`unsetopt`;
- `autoload` y `fpath`;
- ZLE y `compsys`.

## 5. Modelo mental obligatorio

Las explicaciones deben enseñar el orden conceptual de operación del shell y no reducirlo a recetas.

Cuando sea relevante, una lección debe relacionar el tema con esta secuencia:

```text
input
→ token recognition
→ parsing
→ expansions
→ redirections
→ command resolution
→ execution
→ exit status
```

Debe explicarse que el orden exacto y las excepciones dependen del dialecto y del contexto sintáctico.

## 6. Quoting, expansión y argv

Quoting y expansión son conceptos centrales del PATH.

El alumno debe aprender a razonar sobre el `argv` final recibido por un comando y distinguir:

- texto escrito en el shell;
- tokens sintácticos;
- parámetros del shell;
- resultados de expansiones;
- word splitting;
- pathname expansion;
- argumentos finales.

Debe evitarse la explicación simplista de que "el shell sustituye variables".

## 7. Globbing frente a expresiones regulares

Los patrones de pathname del shell no deben confundirse con expresiones regulares.

Cuando una lección necesite regex, debe limitarse a la integración necesaria con el shell, por ejemplo `[[ string =~ regex ]]` en Bash.

La teoría general y profunda de expresiones regulares pertenece al PATH independiente de Regex.

## 8. Integración con otros PATHs

Este PATH puede usar herramientas externas para enseñar composición Unix, pero no debe duplicar sus cursos especializados.

Se permite introducir y usar:

- Coreutils;
- grep y ripgrep;
- sed;
- AWK;
- find/xargs;
- jq;
- herramientas del sistema.

Cuando el contenido alcance internals, sintaxis avanzada o semántica propia de esas herramientas, debe remitirse al PATH correspondiente.

El foco aquí es cómo Bash/Zsh invocan, conectan y controlan dichas herramientas.

## 9. Bash

Bash debe estudiarse en dos dimensiones:

### Uso como lenguaje de scripting

Incluye:

- sintaxis y expansión;
- variables y arrays;
- control de flujo;
- funciones;
- redirecciones;
- procesos y señales;
- robustez;
- debugging;
- testing;
- seguridad;
- diseño de scripts mantenibles.

### Uso interactivo

Incluye:

- startup files;
- Readline;
- prompt;
- history;
- aliases y functions;
- programmable completion;
- job control.

Las lecciones avanzadas deben conectar el comportamiento visible con los internals y el código fuente de Bash cuando aporte valor pedagógico.

## 10. Zsh

Zsh debe enseñarse como shell propio, no como "Bash mejorado".

Debe prestarse especial atención a:

- comportamiento nativo de Zsh;
- emulation modes;
- opciones;
- arrays e indexación;
- ausencia de `SH_WORD_SPLIT` por defecto;
- expansión de parámetros y flags `${(...)...}`;
- globbing extendido;
- glob qualifiers;
- modifiers;
- named directories;
- `fpath`;
- `autoload`;
- hooks;
- módulos `zmodload`;
- ZLE;
- sistema de completion `compsys`;
- `zstyle`;
- rendimiento de startup;
- diseño modular de configuración.

## 11. Configuración modular Zsh

El PATH debe promover una arquitectura modular y comprensible.

Una estructura válida de referencia es:

```text
~/.config/zsh/
├── .zshenv
├── .zprofile
├── .zshrc
├── modules/
├── functions/
├── completions/
├── plugins/
└── conf.d/
```

La estructura no debe imponerse como única solución, pero sí utilizarse para enseñar separación de responsabilidades, orden de carga, dependencias, `fpath`, `autoload`, lazy loading y profiling.

## 12. POSIX y portabilidad

POSIX debe utilizarse como referencia normativa para el Shell Command Language cuando el tema sea portable.

Debe distinguirse entre:

- código deliberadamente POSIX;
- scripts Bash;
- scripts Zsh;
- uso interactivo específico de Bash/Zsh.

No se debe recomendar compatibilidad POSIX cuando el objetivo real de la lección requiera explícitamente características modernas de Bash o Zsh.

La portabilidad debe ser una decisión de diseño, no una obligación automática.

## 13. Seguridad

Toda explicación que pueda introducir vulnerabilidades debe abordar sus implicaciones.

Temas obligatorios cuando correspondan:

- command injection;
- `eval`;
- quoting incorrecto;
- word splitting;
- pathname expansion accidental;
- option injection;
- nombres de archivo hostiles;
- PATH hijacking;
- environment poisoning;
- archivos temporales inseguros;
- race conditions y TOCTOU;
- symlink attacks;
- secretos en argumentos o entorno;
- privilege boundaries;
- ejecución mediante `sudo`;
- `source` de contenido no confiable;
- plugins no confiables.

Las prácticas inseguras pueden mostrarse con fines didácticos, pero deben identificarse explícitamente como tales y corregirse.

## 14. Robustez y manejo de errores

No debe presentarse `set -euo pipefail` como solución universal.

Las lecciones deben enseñar:

- semántica real de `errexit`;
- contextos donde se ignora;
- propagación de exit status;
- estado de pipelines;
- `PIPESTATUS`;
- `pipefail`;
- errores en funciones y command substitutions;
- validación explícita;
- cleanup mediante traps;
- códigos de salida documentados.

## 15. Procesos, terminal y sistema operativo

Las lecciones avanzadas deben relacionar el shell con conceptos de Linux:

- `fork`/`clone` de forma conceptual cuando proceda;
- `execve`;
- `wait`;
- pipes;
- `dup2`;
- file descriptors;
- process groups;
- sessions;
- controlling terminal;
- signals;
- `/proc`;
- TTY y PTY;
- `termios`;
- job control.

Cuando sea útil, deben observarse estos mecanismos con herramientas reales como `ps`, `pstree`, `strace`, `lsof` y `/proc`.

## 16. Herramientas de calidad

El PATH puede utilizar como herramientas auxiliares:

- ShellCheck;
- shfmt;
- Bats;
- ShellSpec;
- `bash -n`;
- `bash -x`;
- `zsh -n`;
- `zsh -x`;
- `zprof`;
- `time`;
- hyperfine;
- `strace`;
- `lsof`;
- `gdb` y `perf` en bloques de internals.

Estas herramientas no sustituyen la comprensión del lenguaje.

## 17. Internals y código fuente

En los bloques de internals se permite y se recomienda estudiar el código fuente upstream.

Para Bash, pueden relacionarse conceptos con archivos o subsistemas como:

- parser;
- expansión;
- ejecución;
- variables;
- builtins;
- jobs;
- señales;
- Readline.

Para Zsh:

- lexer/parser;
- ejecución;
- parámetros;
- globbing;
- jobs;
- señales;
- módulos;
- ZLE;
- completion.

No deben inventarse nombres de archivos, funciones o estructuras internas. Las referencias al source deben verificarse contra la versión utilizada.

## 18. Política de versiones

El contenido conceptual debe intentar ser estable entre versiones.

Cuando una característica dependa de versión:

1. indicar la versión mínima cuando esté verificada;
2. comprobar la versión disponible en Fedora;
3. no extrapolar comportamiento de una versión futura o antigua;
4. citar la documentación correspondiente.

El PATH no debe quedar artificialmente bloqueado a una única versión si el concepto es estable.

## 19. Fuentes y jerarquía de autoridad

Orden preferente para resolver dudas técnicas:

1. estándar POSIX cuando se trate de comportamiento POSIX;
2. manual oficial de Bash para Bash;
3. manual oficial de Zsh para Zsh;
4. documentación y código fuente upstream;
5. documentación y empaquetado Fedora para comportamiento de la distribución;
6. bibliografía técnica seleccionada;
7. herramientas de análisis y experimentación reproducible.

Una fuente secundaria nunca debe prevalecer sobre la documentación normativa o upstream cuando exista contradicción verificable.

## 20. Estructura de las lecciones

Cada lección debe comenzar siempre con:

```text
🎯 OBJETIVO
```

Debe incluir:

```text
📚 LECTURA
```

usando únicamente referencias apropiadas al tema y las categorías definidas en `bibliography.md`.

Cuando aporten valor pedagógico pueden incluirse:

```text
🧪 Laboratorio / ejemplos
⚠️ Errores frecuentes
💡 Idea importante
```

Toda lección debe terminar con:

```text
🧠 QUÉ DEBES RECORDAR
```

con entre 3 y 7 ideas esenciales.

## 21. Política de referencias por lección

No debe forzarse una referencia de cada categoría bibliográfica en todas las lecciones.

Deben seleccionarse únicamente las fuentes que realmente correspondan al tema.

Las referencias exactas a capítulos, secciones o nodos del manual solo deben incluirse cuando hayan sido verificadas.

Si no puede verificarse una sección exacta, debe citarse la obra o manual sin inventar numeración.

## 22. Laboratorios

Los laboratorios deben ser reproducibles, incrementales y observables.

Siempre que sea posible deben permitir comprobar el modelo explicado mediante:

- exit status;
- `printf`;
- `type`/`command -V`/`whence`;
- `set -x`;
- `PS4`;
- `/proc`;
- `ps`/`pstree`;
- file descriptors;
- `strace`;
- tests automatizados.

Debe preferirse comprender el comportamiento antes que copiar una solución terminada.

## 23. Proyectos

Los proyectos integradores no deben ser simples recopilaciones de ejercicios.

Deben combinar varias capacidades, por ejemplo:

- una CLI robusta;
- una biblioteca Bash;
- un entorno Zsh modular;
- completions Bash y Zsh;
- widgets ZLE;
- diagnóstico de procesos y file descriptors;
- profiling;
- testing;
- documentación;
- seguridad.

El proyecto final `bash-zsh-toolkit` debe demostrar dominio conjunto de scripting, interacción, arquitectura modular, debugging, testing, portabilidad, rendimiento y seguridad.

## 24. Criterio de nivel experto

Al terminar el PATH, el alumno debe ser capaz de:

- explicar cómo el shell transforma una línea de comandos en procesos y argumentos;
- predecir expansiones y quoting sin recurrir al ensayo-error;
- diseñar scripts robustos y seguros;
- decidir correctamente entre POSIX sh, Bash y Zsh;
- diagnosticar problemas de procesos, pipelines, señales y file descriptors;
- escribir completion Bash y Zsh;
- extender Zsh mediante funciones, hooks, ZLE y módulos disponibles;
- perfilar y optimizar configuraciones y scripts;
- leer documentación y código fuente upstream;
- construir y mantener una arquitectura Bash/Zsh de producción.
