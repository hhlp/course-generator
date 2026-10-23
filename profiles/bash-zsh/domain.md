# DOMAIN — BASH + ZSH EN PROFUNDIDAD

## 1. Propósito del PATH

Este PATH enseña Bash y Zsh desde los fundamentos del shell Unix hasta
un nivel experto de uso interactivo, scripting, depuración, rendimiento,
seguridad, extensibilidad e internals.

El objetivo no es memorizar comandos aislados. El alumno debe construir
un modelo mental correcto de cómo un shell:

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

El PATH debe permitir comprender qué comportamiento pertenece a POSIX
`sh`, qué es específico de Bash y qué es específico de Zsh.

## 2. Entorno de referencia

Plataforma principal: Fedora Linux.

Los ejemplos y laboratorios deben priorizar herramientas, rutas,
paquetes y convenciones disponibles en Fedora. Cuando una característica
dependa de la versión instalada, debe comprobarse mediante comandos
como:

``` bash
bash --version
zsh --version
rpm -q bash zsh
rpm -qi bash zsh
rpm -ql bash
rpm -ql zsh
```

No debe asumirse que el comportamiento observado en otro sistema
operativo o distribución es idéntico al de Fedora.

## 2A. Secuencia obligatoria y separación Bash/Zsh

- **Fundamentos comunes: bloques 0–1.**
- **Bash: bloques 2–69.**
- **Zsh: bloques 70–98.**
- **Integración: bloques 99–107.**

Primero se completan los fundamentos comunes y Bash; después, Zsh nativo;
por último se realizan las comparaciones y proyectos conjuntos.
Las comparaciones breves pueden señalar diferencias, pero no sustituyen
las lecciones completas del dialecto correspondiente.

Regex aplicada requiere arrays, condicionales, estados de salida y funciones.
Su teoría general y bibliografía especializada pertenecen al PATH Regex.
Readline se estudia en Bash; ZLE, compsys y zprof se estudian en Zsh.

## 3. Alcance funcional

El PATH cubre de forma progresiva:

1.  fundamentos de shell, terminal, TTY, procesos, entorno y file
    descriptors;
2.  sintaxis, quoting, parámetros, variables y expansiones;
3.  globbing y Regex aplicada a Bash/Zsh, incluyendo selección del
    motor, quoting, capturas e integración con utilities;
4.  arrays, aritmética, redirecciones y pipelines;
5.  condicionales, bucles, funciones, scripts y bibliotecas;
6.  procesos, job control, señales y process substitution;
7.  programación defensiva, seguridad, debugging, testing y logging;
8.  configuración, startup, prompt, historial y completion de Bash;
9.  características avanzadas e internals de Bash;
10. Zsh nativo, opciones, expansiones, globbing y arrays;
11. `fpath`, `autoload`, hooks, ZLE, `compsys`, módulos y plugins de
    Zsh;
12. rendimiento interactivo y de scripting;
13. portabilidad POSIX/Bash/Zsh;
14. integración con systemd, SSH, contenedores, automatización y CI;
15. internals, código fuente, tracing y profiling;
16. diseño de CLIs, librerías, dotfiles, frameworks y toolkits de
    producción.

## 4. Política de dialectos

Toda lección debe distinguir explícitamente entre:

- POSIX shell (`sh`);
- Bash;
- Zsh.

Nunca debe enseñarse una extensión de Bash o Zsh como si fuera una
propiedad universal del shell.

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

Las explicaciones deben enseñar el orden conceptual de operación del
shell y no reducirlo a recetas.

Cuando sea relevante, una lección debe relacionar el tema con esta
secuencia:

``` text
input
→ token recognition
→ parsing
→ expansions
→ redirections
→ command resolution
→ execution
→ exit status
```

Debe explicarse que el orden exacto y las excepciones dependen del
dialecto y del contexto sintáctico.

## 6. Quoting, expansión y argv

Quoting y expansión son conceptos centrales del PATH.

El alumno debe aprender a razonar sobre el `argv` final recibido por un
comando y distinguir:

- texto escrito en el shell;
- tokens sintácticos;
- parámetros del shell;
- resultados de expansiones;
- word splitting;
- pathname expansion;
- argumentos finales.

Debe evitarse la explicación simplista de que “el shell sustituye
variables”.

## 7. Globbing frente a expresiones regulares y política de Regex aplicada

Los patrones de pathname del shell no deben confundirse con expresiones
regulares.

Este PATH debe enseñar Regex **aplicada a Bash/Zsh en profundidad de
integración**, sin duplicar el PATH independiente de Regex. El alumno
debe aprender a reconocer qué motor interpreta el patrón, cómo el shell
procesa primero quoting/expansiones y cómo pasar el patrón correctamente
al motor receptor.

Cobertura obligatoria cuando corresponda:

- `[[ string =~ regex ]]` en Bash y su `BASH_REMATCH`;
- regex en `[[ ... ]]` de Zsh y sus mecanismos de captura;
- diferencias Bash/Zsh que afecten al uso real;
- POSIX BRE/ERE como dialectos relevantes para utilities;
- PCRE en Zsh cuando se habilite explícitamente y herramientas externas
  que la utilicen;
- integración con `grep`, `ripgrep`, `sed`, AWK y otras utilities sin
  enseñar de nuevo toda su semántica interna;
- quoting de patrones, patrones almacenados en variables y doble
  interpretación shell → motor regex;
- validación, extracción, exit status, capturas y testing;
- locale, seguridad, input no confiable, mantenibilidad y rendimiento;
- decisión entre glob, regex, fixed-string matching y parser
  especializado.

La teoría formal, construcción exhaustiva de expresiones, motores en
profundidad y técnicas generales avanzadas pertenecen al PATH
independiente de Regex. Aquí el objetivo es **usar Regex correctamente
desde Bash/Zsh**.

## 8. Integración con otros PATHs

Este PATH puede usar herramientas externas para enseñar composición
Unix, pero no debe duplicar sus cursos especializados.

Se permite introducir y usar:

- Coreutils;
- grep y ripgrep;
- sed;
- AWK;
- find/xargs;
- jq;
- herramientas del sistema.

Cuando el contenido alcance internals, sintaxis avanzada o semántica
propia de esas herramientas, debe remitirse al PATH correspondiente.

El foco aquí es cómo Bash/Zsh invocan, conectan y controlan dichas
herramientas.

## 8A. Expresiones idiomáticas Bash y eficiencia de la CLI

El PATH incorpora *bash Idioms* para enseñar diseño, legibilidad,
refactorización y patrones idiomáticos de Bash, sin convertirlos en reglas
universales de Zsh.

*Efficient Linux at the Command Line* apoya la composición de comandos, los pipelines observables y la productividad interactiva. Los ejemplos deben distinguir el trabajo realizado por el shell de la semántica propia de las herramientas externas. En los bloques Zsh, reescribir los ejemplos con semántica Zsh nativa cuando corresponda.

Priorizar claridad, mediciones reproducibles, control de errores, quoting
correcto y pruebas sobre trucos crípticos o microoptimizaciones. No duplicar
contenidos especializados de Coreutils, sed, awk, Regex ni administración de
Linux.

## 8B. Aplicaciones acotadas: seguridad y datos

Las lecciones de auditoría defensiva y datos se conservan como aplicaciones
opcionales de composición shell. No constituyen cursos completos de
ciberseguridad ni ciencia de datos y no requieren las dos obras excluidas
de la bibliografía. Enseñar contratos de entrada/salida, errores,
reproducibilidad, privacidad y límites de las herramientas invocadas.

Las comprobaciones intrusivas solo se realizan en laboratorios propios y
autorizados. La seguridad del propio lenguaje sigue siendo obligatoria.

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

Las lecciones avanzadas deben conectar el comportamiento visible con los
internals y el código fuente de Bash cuando aporte valor pedagógico.

## 10. Zsh

Zsh debe enseñarse como shell propio, no como “Bash mejorado”.

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

``` text
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

Crear `~/.config/zsh/` no activa su lectura automáticamente. Hay que
establecer `ZDOTDIR` antes de que Zsh busque los archivos reubicados, por
el entorno de lanzamiento o mediante un bootstrap mínimo en `~/.zshenv`.
Documentar dónde vive el bootstrap, evitar recursión y comprobar el orden
con un HOME temporal. Las rutas globales dependen de la compilación y
empaquetado: verificarlas en Fedora/RHEL antes de fijarlas en un ejemplo.

La estructura no debe imponerse como única solución, pero sí utilizarse
para enseñar separación de responsabilidades, orden de carga,
dependencias, `fpath`, `autoload`, lazy loading y profiling.

## 12. POSIX y portabilidad

POSIX debe utilizarse como referencia normativa para el Shell Command
Language cuando el tema sea portable.

Debe distinguirse entre:

- código deliberadamente POSIX;
- scripts Bash;
- scripts Zsh;
- uso interactivo específico de Bash/Zsh.

No se debe recomendar compatibilidad POSIX cuando el objetivo real de la
lección requiera explícitamente características modernas de Bash o Zsh.

La portabilidad debe ser una decisión de diseño, no una obligación
automática.

## 13. Seguridad

Toda explicación que pueda introducir vulnerabilidades debe abordar sus
implicaciones.

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

Las prácticas inseguras pueden mostrarse con fines didácticos, pero
deben identificarse explícitamente como tales y corregirse.

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

Las lecciones avanzadas deben relacionar el shell con conceptos de
Linux:

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

Cuando sea útil, deben observarse estos mecanismos con herramientas
reales como `ps`, `pstree`, `strace`, `lsof` y `/proc`.

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

En los bloques de internals se permite y se recomienda estudiar el
código fuente upstream.

Para Bash, pueden relacionarse conceptos con archivos o subsistemas
como:

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

No deben inventarse nombres de archivos, funciones o estructuras
internas. Las referencias al source deben verificarse contra la versión
utilizada.

## 18. Política de versiones

El contenido conceptual debe intentar ser estable entre versiones.

Cuando una característica dependa de versión:

1.  indicar la versión mínima cuando esté verificada;
2.  comprobar la versión disponible en Fedora;
3.  no extrapolar comportamiento de una versión futura o antigua;
4.  citar la documentación correspondiente.

El PATH no debe quedar artificialmente bloqueado a una única versión si
el concepto es estable.

## 19. Fuentes y jerarquía de autoridad

Orden preferente para resolver dudas técnicas:

1.  estándar POSIX cuando se trate de comportamiento POSIX;
2.  manual oficial de Bash para Bash;
3.  manual oficial de Zsh para Zsh;
4.  documentación y código fuente upstream;
5.  documentación y empaquetado Fedora para comportamiento de la
    distribución;
6.  bibliografía técnica seleccionada;
7.  herramientas de análisis y experimentación reproducible.

Una fuente secundaria nunca debe prevalecer sobre la documentación
normativa o upstream cuando exista contradicción verificable.

## 20. Estructura de las lecciones

Cada lección debe comenzar siempre con:

``` text
🎯 OBJETIVO
```

Debe incluir:

``` text
📚 LECTURA
```

usando únicamente referencias apropiadas al tema y las categorías
definidas en `bibliography.md`.

Cuando aporten valor pedagógico pueden incluirse:

``` text
🧪 Laboratorio / ejemplos
⚠️ Errores frecuentes
💡 Idea importante
```

Toda lección debe terminar con:

``` text
🧠 QUÉ DEBES RECORDAR
```

con entre 3 y 7 ideas esenciales.

## 21. Política de referencias por lección

No debe forzarse una referencia de cada categoría bibliográfica en todas
las lecciones.

Deben seleccionarse únicamente las fuentes que realmente correspondan al
tema.

Las referencias exactas a capítulos, secciones o nodos del manual solo
deben incluirse cuando hayan sido verificadas.

Si no puede verificarse una sección exacta, debe citarse la obra o
manual sin inventar numeración.

## 22. Laboratorios

Los laboratorios deben ser reproducibles, incrementales y observables.

Siempre que sea posible deben permitir comprobar el modelo explicado
mediante:

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

Debe preferirse comprender el comportamiento antes que copiar una
solución terminada.

## 23. Proyectos

Los proyectos integradores no deben ser simples recopilaciones de
ejercicios.

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

El proyecto final `bash-zsh-toolkit` debe demostrar dominio conjunto de
scripting, interacción, arquitectura modular, debugging, testing,
portabilidad, rendimiento y seguridad.

## 24. Criterio de nivel experto

Al terminar el PATH, el alumno debe ser capaz de:

- explicar cómo el shell transforma una línea de comandos en procesos y
  argumentos;
- predecir expansiones y quoting sin recurrir al ensayo-error;
- diseñar scripts robustos y seguros;
- decidir correctamente entre POSIX sh, Bash y Zsh;
- diagnosticar problemas de procesos, pipelines, señales y file
  descriptors;
- escribir completion Bash y Zsh;
- extender Zsh mediante funciones, hooks, ZLE y módulos disponibles;
- perfilar y optimizar configuraciones y scripts;
- leer documentación y código fuente upstream;
- construir y mantener una arquitectura Bash/Zsh de producción.

## 25. Validación por dialecto y límites de las herramientas

- Bash: `bash -n`, ShellCheck en modo Bash y pruebas reales con Bash.
- Zsh: `zsh -n`, ejecución con Zsh y ShellSpec cuando corresponda.
- POSIX: identificar la edición objetivo y probar con las implementaciones
  elegidas; un análisis estático por sí solo no demuestra portabilidad.
- No tratar Bats, ShellCheck o shfmt como herramientas universales para
  Zsh. Separar el runner de pruebas del intérprete que ejecuta el código.
- La comprobación sintáctica no valida expansiones, señales, quoting ni
  estados de salida. Añadir casos positivos, negativos y límite.
- `validation.enabled` describe configuración del generador; no significa
  que este PATH ni sus ejemplos hayan sido ejecutados automáticamente.

## 26. Portabilidad normativa y disponibilidad real

Distinguir POSIX.1-2017 de POSIX.1-2024 y del soporte implementado.
POSIX.1-2024 contempla dollar-single-quotes y pipefail; esto no garantiza
su disponibilidad en shells antiguos. Citar la edición aplicable.
Las formas `${ comando; }` y `${| comando; }` se enseñan como funciones
Bash 5.3, con detección de versión y alternativas para versiones previas.
RHEL y Fedora pueden tener versiones diferentes; comprobar cada entorno.

## 27. Controles expertos obligatorios

Desarrollar Readline, herencia de errexit y traps, estados de pipelines,
SIGPIPE, fallos de process substitution, cancelación de procesos hijos,
límites de datos binarios en Bash y ARG_MAX. En Zsh desarrollar scripting,
cleanup, debugging y testing antes de frameworks. Evitar colisiones de
variables locales, ocultación de errores por declaraciones y source
cruzado de bibliotecas incompatibles.

## 28. Integración con course-generator

Las claves editoriales de `profile.yaml` documentan intención pedagógica.
No afirmar que son funciones ejecutables, comandos o validaciones del
generador sin comprobar su implementación. Conservar la configuración de
validación del proyecto y ejecutar comprobaciones de ejemplos de acuerdo
con cada intérprete. La ruta `files.pedagogy` debe resolverse desde la
ubicación real del perfil en el repositorio.
