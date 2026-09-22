# BIBLIOGRAPHY — COREUTILS EN PROFUNDIDAD

## Criterio

La bibliografía se organiza por autoridad y función. Las referencias exactas de capítulo, sección o nodo `info` deben incluirse en una lección únicamente cuando hayan sido verificadas contra la edición o versión utilizada.

## Principal

### GNU Coreutils Manual

Fuente principal para GNU Coreutils.

Usar para:

- semántica de cada utilidad;
- sintaxis;
- opciones GNU;
- variables de entorno;
- exit status;
- comportamiento especial;
- invocation;
- file permissions;
- operaciones con directorios y archivos;
- transformación de texto;
- ordenación;
- fechas;
- almacenamiento;
- checksums;
- ejecución de procesos.

Preferir el manual correspondiente a la versión instalada o una versión upstream compatible con la lección.

### GNU Findutils Manual — Finding Files

Fuente principal para GNU Findutils.

Usar para:

- `find`;
- expresiones;
- tests;
- actions;
- operators;
- traversal;
- `-exec`;
- `-execdir`;
- `-delete`;
- `-printf`;
- optimización;
- seguridad;
- `xargs`;
- delimitación NUL.

### rsync manual / rsync(1)

Fuente principal para rsync.

Usar para:

- sintaxis;
- archive mode;
- filtros;
- preservación;
- `--delete`;
- `--files-from`;
- SSH;
- daemon;
- algoritmo de transferencia;
- checksums;
- compresión;
- backups;
- `--link-dest`;
- rendimiento;
- seguridad;
- diagnóstico y exit codes.

### GNU bc manual

Fuente principal para bc.

Usar para:

- lenguaje;
- precisión arbitraria;
- `scale`;
- `ibase`;
- `obase`;
- arrays;
- control de flujo;
- funciones;
- biblioteca matemática;
- comportamiento de la implementación utilizada.

## Normativa

### POSIX.1 / The Open Group Base Specifications

Usar para distinguir comportamiento portable de extensiones GNU.

Especialmente relevante para:

- utility syntax;
- environment;
- locale;
- pathname handling;
- `cp`;
- `mv`;
- `rm`;
- `ln`;
- `chmod`;
- `chown`;
- `cat`;
- `head`;
- `tail`;
- `sort`;
- `uniq`;
- `tr`;
- `wc`;
- `printf`;
- `date`;
- `find`;
- `xargs`;
- `test`.

No atribuir a POSIX opciones que sean exclusivamente GNU.

### Linux man-pages

Usar como referencia normativa/práctica del interfaz Linux cuando el comportamiento dependa del kernel o de syscalls.

Especialmente:

- `open(2)`;
- `read(2)`;
- `write(2)`;
- `close(2)`;
- `stat(2)` / familia stat;
- `rename(2)`;
- `unlink(2)`;
- `link(2)`;
- `symlink(2)`;
- `chmod(2)`;
- `chown(2)`;
- `fsync(2)`;
- `fdatasync(2)`;
- `lseek(2)`;
- `getxattr(2)` y xattrs cuando corresponda.

## Motor / implementación

### Repositorio upstream de GNU Coreutils

Usar en los bloques de internals para:

- `src/`;
- `lib/`;
- tests;
- build system;
- implementación de utilidades;
- option parsing;
- diagnósticos;
- interacción con gnulib;
- locale e i18n.

### GNU gnulib

Usar para comprender:

- portability layer;
- wrappers;
- módulos compartidos;
- diferencias entre plataformas;
- infraestructura reutilizada por proyectos GNU.

### Repositorio upstream de GNU Findutils

Usar para:

- parser de expresiones;
- predicates;
- actions;
- traversal;
- optimizer;
- debug;
- implementación de xargs;
- testsuite.

### Código fuente de rsync

Usar en profundización cuando sea necesario explicar:

- rolling checksum;
- strong checksum;
- matching de bloques;
- generación y reconstrucción del delta;
- protocol behavior;
- decisiones de rendimiento.

No utilizar internals para reemplazar la documentación de interfaz cuando la pregunta sea sobre uso normal.

## Fedora

### Fedora Packages / RPM metadata

Usar para determinar:

- paquetes que proporcionan las herramientas;
- versiones instaladas;
- división de archivos entre paquetes;
- dependencias;
- archivos instalados.

Complementar con comandos locales:

- `rpm -q`;
- `rpm -qi`;
- `rpm -ql`;
- `rpm -qf`;
- `dnf info`.

### Fedora Packaging Guidelines

Usar cuando el proyecto final se empaquete como RPM.

Especialmente:

- estructura del SPEC;
- BuildRequires/Requires;
- macros;
- instalación;
- `%files`;
- permisos;
- documentación;
- licencias;
- scriptlets solo cuando sean necesarios.

### Fedora SELinux documentation

Usar únicamente cuando Coreutils/rsync interactúen con:

- security contexts;
- xattrs;
- etiquetado;
- preservación/restauración de contextos;
- denegaciones relevantes.

### systemd documentation

Usar para los bloques de automatización de rsync mediante:

- service units;
- `Type=oneshot`;
- timer units;
- `OnCalendar=`;
- `Persistent=`;
- hardening;
- journal.

## Profundización

### The Linux Programming Interface — Michael Kerrisk

Usar como profundización conceptual para:

- file descriptors;
- filesystems;
- inodes;
- links;
- metadata;
- procesos;
- señales;
- I/O;
- syscalls;
- timestamps;
- permisos;
- usuarios y grupos.

No utilizarlo como sustituto del manual específico de una utilidad GNU.

### Advanced Programming in the UNIX Environment — W. Richard Stevens, Stephen A. Rago

Usar como profundización para:

- Unix process model;
- files;
- directories;
- file I/O;
- process environment;
- signals;
- user/group IDs;
- portability.

### The Linux Command Line 3Ed - William Shotts

Referencia didáctica complementaria para fundamentos de:

- shell;
- comandos;
- redirecciones;
- pipelines;
- filesystem;
- permisos;
- herramientas GNU.

Su función es pedagógica; para semántica exacta prevalece la documentación oficial.

## Consulta

### `info coreutils`

Consulta local prioritaria para GNU Coreutils cuando esté disponible.

### páginas man

Especialmente:

- `coreutils(1)` cuando exista en la distribución;
- `cp(1)`;
- `mv(1)`;
- `rm(1)`;
- `ls(1)`;
- `stat(1)`;
- `sort(1)`;
- `date(1)`;
- `dd(1)`;
- `find(1)`;
- `xargs(1)`;
- `rsync(1)`;
- `bc(1)`.

Las páginas man deben contrastarse con `info` cuando el manual GNU contenga explicaciones más completas.

### `--help`

Utilizar para:

- descubrir opciones de la versión instalada;
- verificar sintaxis;
- detectar diferencias de versión.

No usar `--help` como única fuente para conceptos complejos.

### documentación instalada por RPM

Localizar mediante:

- `rpm -ql coreutils`;
- `rpm -ql coreutils-common`;
- `rpm -ql findutils`;
- `rpm -ql rsync`;
- `rpm -ql bc`.

## Referencias por área

### Coreutils

Principal:
GNU Coreutils Manual.

Normativa:
POSIX cuando la utilidad esté especificada.

Motor:
GNU Coreutils source + gnulib.

Profundización:
The Linux Programming Interface.

Consulta:
`info coreutils`, páginas man y `--help`.

### Findutils

Principal:
GNU Findutils Manual — Finding Files.

Normativa:
POSIX `find` y `xargs`.

Motor:
GNU Findutils source + gnulib.

Profundización:
Linux man-pages y literatura Unix/Linux cuando el tema sea traversal, metadata o procesos.

Consulta:
`find(1)`, `xargs(1)`, `find --help`, `xargs --help`.

### bc

Principal:
manual de GNU bc correspondiente a la implementación utilizada.

Normativa:
POSIX bc cuando se estudie portabilidad.

Profundización:
documentación de la implementación para extensiones no POSIX.

Consulta:
`bc(1)` y ayuda local.

### rsync

Principal:
`rsync(1)` y documentación oficial de rsync.

Motor:
código fuente upstream de rsync.

Profundización:
documentación técnica del algoritmo rsync cuando el bloque trate internals.

Consulta:
`rsync --help`, `rsync --version`.

### Fedora

Principal:
documentación oficial de Fedora correspondiente al subsistema estudiado.

Consulta local:
RPM/DNF y documentación instalada.

## Política de referencias de las lecciones

La sección `📚 LECTURA` debe utilizar las categorías definidas por el perfil:

Principal:
documentación oficial de la herramienta estudiada.

Normativa:
POSIX, Linux interfaces u otra especificación aplicable.

Motor:
código fuente o documentación de implementación cuando aporte valor.

Profundización:
bibliografía técnica que explique el modelo subyacente.

Consulta:
man, info, ayuda local y documentación de Fedora.

No es obligatorio rellenar artificialmente todas las categorías si una de ellas no aporta valor a la lección.

No inventar capítulos, secciones, nodos info, páginas o numeraciones.

Cuando no se haya verificado una referencia exacta, citar la obra o manual y el tema correspondiente sin inventar localización.

## Jerarquía ante discrepancias

Para comportamiento de una versión concreta instalada:

1. comportamiento observado de esa versión;
2. documentación de esa misma versión;
3. documentación upstream compatible;
4. especificación POSIX cuando sea aplicable;
5. bibliografía secundaria.

Para portabilidad:

1. POSIX;
2. documentación de cada implementación;
3. pruebas controladas en las plataformas comparadas.

Para internals:

1. código fuente de la versión estudiada;
2. tests upstream;
3. documentación del proyecto;
4. bibliografía explicativa.
