# DOMAIN — COREUTILS EN PROFUNDIDAD

## Identidad del PATH

Nombre: COREUTILS EN PROFUNDIDAD
Plataforma principal: Fedora Linux
Nivel: desde fundamentos hasta nivel experto
Orientación: administración y uso avanzado de herramientas GNU/Unix, composición de comandos, automatización y análisis de internals.
Lenguajes de programación: no forman parte del alcance base.
Entorno preferido: Fedora Linux.

## Alcance

Este PATH estudia GNU Coreutils como núcleo de las herramientas de user space utilizadas para manipular archivos, directorios, texto, procesos, identidad, fechas, almacenamiento y flujos de datos.

El recorrido amplía deliberadamente el ecosistema con GNU Findutils, bc y rsync porque permiten construir workflows reales alrededor de Coreutils:

- GNU Coreutils: manipulación, inspección y transformación fundamental.
- GNU Findutils: selección, recorrido y ejecución sobre árboles de archivos.
- bc: cálculo numérico y precisión arbitraria desde shell y pipelines.
- rsync: copia, sincronización, transferencia y backups.
- shell: medio de composición; no constituye un curso de Bash o Zsh.
- Fedora Linux: plataforma de referencia para paquetes, paths, SELinux, systemd y comportamiento del sistema.

El objetivo final es comprender las herramientas individualmente y también su composición en workflows robustos, seguros, reproducibles y diagnosticables.

## Principios del dominio

### GNU frente a POSIX

Distinguir siempre entre:

- comportamiento especificado por POSIX;
- comportamiento de GNU Coreutils;
- extensiones GNU;
- comportamiento específico de GNU Findutils;
- comportamiento específico de rsync;
- comportamiento proporcionado por builtins del shell;
- herramientas externas relacionadas que no pertenecen a Coreutils.

No presentar una extensión GNU como si fuese portable por definición.

### Coreutils frente a builtins del shell

Cuando un nombre pueda existir tanto como builtin como ejecutable externo, distinguir explícitamente ambos casos.

Ejemplos relevantes:

- printf;
- test y `[`;
- pwd;
- echo cuando aparezca como herramienta relacionada.

Utilizar `type`, `command`, rutas de ejecutables y consultas RPM cuando sea útil para demostrar qué implementación se está ejecutando.

### Fedora como plataforma

Las lecciones deben usar Fedora Linux como entorno principal.

Cuando corresponda, integrar:

- `rpm -q`, `rpm -qi`, `rpm -ql`, `rpm -qf`;
- `dnf`;
- layout `/usr/bin`, `/usr/sbin`, `/usr/libexec`;
- sistemas usr-merged;
- SELinux;
- ACL y extended attributes;
- Linux capabilities;
- systemd;
- OpenSSH;
- filesystems habituales en Linux.

No convertir el PATH en un curso general de Fedora: estos elementos deben aparecer cuando expliquen el comportamiento de las herramientas estudiadas.

## Modelo Unix

Explicar las herramientas dentro del modelo de composición Unix:

entrada -> selección -> transformación -> salida

Tratar de forma explícita:

- stdin;
- stdout;
- stderr;
- file descriptors;
- pipes;
- redirecciones;
- exit status;
- señales cuando correspondan;
- variables de entorno;
- locale;
- quoting;
- expansión del shell;
- globbing.

No confundir comportamiento del shell con comportamiento de la utilidad.

## Filenames arbitrarios

El PATH debe enseñar desde etapas tempranas que los nombres de archivo pueden contener espacios, tabs, saltos de línea y caracteres que pueden interpretarse como opciones.

Cuando corresponda, explicar:

- `--`;
- delimitación NUL;
- `find -print0`;
- `xargs -0`;
- opciones `-z`, `-0`, `--zero` y `--files0-from`;
- quoting;
- option injection;
- word splitting;
- por qué no se debe parsear `ls`.

Los ejemplos avanzados deben ser correctos ante nombres hostiles siempre que la herramienta permita construir una solución segura.

## Filesystems y metadata

Distinguir claramente:

- pathname;
- directory entry;
- inode;
- hard link;
- symbolic link;
- file descriptor;
- archivo abierto;
- filesystem;
- mount point.

Cuando corresponda, estudiar:

- mode;
- UID/GID;
- ownership;
- timestamps;
- ACL;
- xattrs;
- SELinux contexts;
- capabilities;
- sparse files;
- reflinks;
- CoW;
- hard links;
- symlinks.

No asumir que todos los filesystems soportan las mismas propiedades.

## Tiempo y locale

El comportamiento dependiente del locale debe indicarse explícitamente, especialmente en:

- `sort`;
- `tr`;
- `printf`;
- `date`;
- clasificación y clases de caracteres.

Distinguir `LANG`, `LC_ALL`, categorías `LC_*` y `TZ`.

Explicar cuándo `LC_ALL=C` es útil para obtener comportamiento reproducible, sin presentarlo como requisito universal.

## Seguridad

Las operaciones destructivas deben enseñarse con un workflow seguro:

inspeccionar -> seleccionar -> mostrar -> simular -> confirmar -> ejecutar -> verificar -> registrar -> recuperar

Tratar cuando corresponda:

- mínimo privilegio;
- option injection;
- command injection;
- symlink attacks;
- TOCTOU;
- archivos temporales seguros;
- `mktemp`;
- operaciones como root;
- `rm`;
- `chown`;
- `chmod`;
- `find -exec` y `-execdir`;
- `xargs`;
- `rsync --delete`;
- `rsync --remove-source-files`.

Los laboratorios destructivos deben usar árboles de prueba controlados.

## Rendimiento

No optimizar por intuición.

Explicar y medir cuando corresponda:

- coste de creación de procesos;
- builtins frente a ejecutables;
- buffering;
- page cache;
- metadata;
- tamaños de bloque;
- external sorting;
- memoria de `sort`;
- paralelismo;
- `xargs -P`;
- optimizer de `find`;
- archivos pequeños frente a grandes;
- filesystem local frente a remoto;
- CPU frente a ancho de banda en rsync.

Separar corrección, seguridad y rendimiento.

## GNU Findutils

Tratar `find` como un lenguaje de expresiones y no como una simple colección de flags.

Desarrollar:

- starting points;
- tests;
- actions;
- operators;
- precedencia;
- short-circuit;
- traversal;
- profundidad;
- filesystem boundaries;
- symlink handling;
- `-exec`;
- `-execdir`;
- `-delete`;
- `-printf`;
- optimizer;
- debug;
- seguridad y TOCTOU.

Para regex, distinguir los dialectos admitidos por GNU find y no convertir el bloque en un curso general de expresiones regulares.

## xargs

Explicar:

- construcción de argumentos;
- parsing;
- delimitación NUL;
- `ARG_MAX`;
- batching;
- paralelismo;
- exit status;
- interacción con señales;
- diferencias con `find -exec ... {} +`.

No usar `xargs` como sustituto automático de `-exec`; enseñar cuándo corresponde cada mecanismo.

## bc

bc se estudia como herramienta de cálculo de precisión arbitraria y como componente de pipelines.

Cubrir:

- lenguaje;
- `scale`;
- `ibase`;
- `obase`;
- control de flujo;
- funciones;
- biblioteca matemática;
- integración con shell.

Distinguir bc de la aritmética del shell, awk y lenguajes de propósito general.

## rsync

Rsync se estudia como herramienta independiente relacionada e integrada con Coreutils/Findutils.

Desarrollar:

- quick check;
- archive mode;
- metadata;
- filtros;
- delete;
- `--files-from`;
- transferencia SSH;
- daemon;
- algoritmo delta;
- checksums;
- compresión;
- rendimiento;
- ACL/xattrs/SELinux;
- sparse files;
- backups;
- `--link-dest`;
- consistencia;
- filesystems;
- seguridad;
- diagnóstico.

Distinguir sincronización, mirror, backup y snapshot.

No presentar rsync como mecanismo que garantice por sí mismo snapshots consistentes de aplicaciones activas.

## Internals

Los bloques de internals deben conectar el comportamiento visible con la implementación upstream.

GNU Coreutils:

- estructura del código;
- gnulib;
- portability layer;
- `src/`;
- `lib/`;
- tests;
- Autoconf/Automake;
- option parsing;
- syscalls;
- errno;
- diagnostics;
- locale e i18n.

GNU Findutils:

- arquitectura;
- parser de expresiones;
- representación conceptual de la expresión;
- predicates;
- actions;
- traversal;
- optimizer;
- costes y probabilidades;
- side effects;
- xargs;
- tests y build system.

No exigir programación como prerrequisito para las lecciones conceptuales. El código upstream puede utilizarse para explicar implementación cuando aporte valor.

## Automatización

La automatización debe favorecer herramientas reutilizables y funciones modulares.

Cuando corresponda:

- Bash para ejemplos portables;
- funciones Zsh para herramientas del entorno del curso;
- configuración separada del código;
- validación;
- dry-run;
- logging;
- manejo de señales;
- cleanup;
- tests;
- ShellCheck;
- shfmt.

No convertir el PATH en un curso completo de programación shell.

## Proyecto final

El proyecto `coreutils-toolkit` debe integrar progresivamente:

- archivos y rutas;
- permisos y ownership;
- almacenamiento;
- hashes;
- texto;
- fechas;
- cálculo con bc;
- selección con find;
- ejecución batch con xargs;
- sincronización con rsync;
- NUL safety;
- dry-run;
- explain mode;
- seguridad;
- logging;
- métricas;
- tests;
- documentación;
- empaquetado RPM;
- integración opcional con systemd.

El proyecto debe poder trabajar sobre datos y árboles reales, pero las pruebas destructivas deben realizarse primero sobre fixtures reproducibles.

## Estructura pedagógica

Cada lección debe:

1. comenzar con `🎯 OBJETIVO`;
2. incluir `📚 LECTURA`;
3. desarrollar el tema de forma autocontenida y específica;
4. utilizar `🧪 Laboratorio/ejemplos` cuando aporte valor;
5. utilizar `⚠️ Errores frecuentes` cuando aporte valor;
6. utilizar `💡 Idea importante` cuando aporte valor;
7. terminar con `🧠 QUÉ DEBES RECORDAR`, con entre 3 y 7 ideas.

Evitar scaffolding genérico y ejemplos intercambiables entre lecciones.

## Límites

Este PATH no pretende sustituir cursos específicos de:

- Bash o Zsh;
- regex;
- sed;
- awk;
- SELinux;
- systemd;
- OpenSSH;
- administración avanzada de filesystems;
- programación C.

Cuando estos dominios aparezcan, explicar únicamente lo necesario para comprender Coreutils y las herramientas integradas, remitiendo conceptualmente al PATH especializado cuando corresponda.
