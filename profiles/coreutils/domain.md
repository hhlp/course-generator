# DOMAIN — COREUTILS EN PROFUNDIDAD

## Identidad del PATH

Nombre: COREUTILS EN PROFUNDIDAD
Plataforma principal: Fedora Linux
Nivel: desde fundamentos hasta nivel experto
Orientación: administración y uso avanzado de herramientas GNU/Unix, composición de comandos, automatización y análisis de internals.
Lenguajes de propósito general: no forman parte del alcance base. Se permiten scripts shell y el lenguaje bc para composición, automatización y cálculo; no se exige programación C para internals conceptuales.
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

- POSIX sh para ejemplos declarados portables;
- Bash para ejemplos que requieran sus extensiones, identificándolas;
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

## Granularidad de las lecciones

Cada entrada `XX.YY` del `initial.txt` representa una **lección real**, no un simple ítem de inventario. Una lección debe tener amplitud suficiente para desarrollar un objetivo específico, explicación técnica, ejemplos o práctica cuando proceda, errores/limitaciones relevantes y un cierre con ideas que recordar.

Reglas de diseño:

- agrupar opciones hermanas, formatos, modificadores o conceptos inseparables cuando por separado producirían lecciones triviales;
- conservar separados los conceptos que introducen un modelo mental, riesgo, mecanismo, decisión de diseño o práctica sustancialmente distinta;
- no crear una lección independiente para una sola flag, especificador de formato o palabra clave salvo que su semántica justifique por sí misma una unidad completa;
- mantener laboratorios integradores como lecciones propias cuando cierren un bloque;
- permitir repetición únicamente cuando exista progresión explícita: fundamentos -> uso -> composición -> seguridad/rendimiento -> internals -> integración/proyecto;
- preservar todos los conceptos del temario aunque varios se integren en una misma lección.

El objetivo no es minimizar el número de lecciones, sino evitar microlecciones artificiales sin perder profundidad.

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


## Cobertura, plataformas y progresión

Fedora Linux es el entorno de referencia. RHEL es una plataforma secundaria:
verificar versiones, paquetes y capacidades antes de reutilizar ejemplos.
No prometer equivalencia de opciones ni de empaquetado entre ambas.
Registrar la versión instalada de Coreutils, Findutils, bc y rsync en los labs.
La presencia del programa multicall coreutils es opcional; consultar también
la versión de una utilidad concreta. El inventario instalado se compara con
upstream sin asumir que toda utilidad esté habilitada o empaquetada igual.

Incluir explícitamente rmdir, pathchk, shuf, factor, pr, ptx, tsort, printenv,
true, false, stty, chcon, runcon, dir, vdir, arch, echo y link. Las herramientas
pequeñas pueden compartir lección si existe un objetivo común sustancial.
stty se estudia con restauración del estado del terminal y fixtures seguros.
chcon y runcon se limitan a su relación con las utilidades y la política activa;
la administración de política SELinux corresponde a su PATH especializado.

La repetición debe añadir una capacidad verificable:

- bloques 3 y 27: inspección inicial -> contratos y composición de rutas;
- bloques 21, 53 y 54: mecanismos básicos -> entorno -> diagnóstico combinado;
- bloques 63 y 74: preservación -> diagnóstico y migración de identidades;
- bloques 50, 84 y 89: composición -> orquestación -> interfaz reutilizable.

Cada laboratorio debe declarar objetivo, datos iniciales, resultado esperado,
criterios de verificación y limpieza. Los bloques de integración han de incorporar
casos de fallo distintos, no repetir los ejemplos introductorios.

## Dialectos, versiones y límites de seguridad

Distinguir regex de expr, csplit y find; identificar -regextype cuando corresponda.
Los globs del shell, -name/-path y filtros rsync no son el mismo lenguaje.
El PATH de Regex desarrolla la teoría general; aquí se enseña la aplicación.
Fijar la edición de POSIX utilizada al hablar de portabilidad: una opción puede
haber cambiado de condición entre ediciones. Detectar capacidades localmente.

No atribuir opciones comunes a todas las utilidades. No confundir encoding con
cifrado, un checksum con autenticación, ni NUL safety con protección TOCTOU.
NUL no puede conservarse en variables shell: usar pipes o listas en archivos.
Una simulación no garantiza que el árbol siga igual durante la ejecución.
La atomicidad de rename y la durabilidad tras un fallo son garantías diferentes.

Para rsync, comprobar efectos de --files-from sobre recursión, formatos y --from0;
distinguir autenticación del daemon y cifrado; comprobar compatibilidad de
--secluded-args; proteger snapshots por hard links frente a modificaciones.
Los ejercicios de recuperación deben verificar contenido y metadata y simular
la indisponibilidad del origen. Evitar llamar snapshot consistente a una copia
de datos activos que no haya sido coordinada con la aplicación.

## Perfil y validación del generador

scope.programming_languages=false excluye cursos de lenguajes de propósito
general; no prohíbe los scripts shell ni bc expresamente incluidos aquí.
Los campos de calidad describen requisitos pedagógicos. Su presencia en YAML
no demuestra que el generador los ejecute como controles automáticos.
validation.enabled=false conserva desactivada la ejecución automática de
comandos: las lecciones abarcan entornos incompatibles y requieren seleccionar
validaciones por artefacto. No activar comandos globales sin comprobar el contrato
del generador y la disponibilidad de sus dependencias. La revisión de estos cuatro
archivos comprueba estructura y coherencia; no ejecuta los futuros laboratorios.
