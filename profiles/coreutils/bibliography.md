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

### Linux ACL — acl(5), getfacl(1), setfacl(1)

Fuentes principales para ACL POSIX en Linux y las utilidades del paquete
`acl`, que no forman parte de GNU Coreutils.

Usar para:

- modelo de entradas ACL y algoritmo de permisos efectivos;
- ACL de acceso y predeterminadas, máscara y herencia;
- `getfacl` y `setfacl`: lectura, modificación y eliminación;
- copias de seguridad y restauración de ACL;
- diferencias entre permisos tradicionales, ACL y SELinux;
- soporte del filesystem y límites de portabilidad.

Verificar la implementación y versión instalada en Fedora/RHEL con
`rpm -q acl`, `rpm -qf /usr/bin/getfacl` y `man acl`.

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

### The Linux Command Line — William Shotts

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
- `bc(1)`;
- `acl(5)`, `getfacl(1)` y `setfacl(1)`.

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

### ACL (herramientas relacionadas)

Principal:
`acl(5)`, `getfacl(1)` y `setfacl(1)` de la versión instalada.

Consulta:
`getfacl --help`, `setfacl --help`, `rpm -q acl` y manuales locales.

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

1. documentación de esa misma versión como contrato esperado;
2. comportamiento observado en pruebas reproducibles de esa versión;
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


## Acceso a fuentes y control de versiones

Estos enlaces son puntos de entrada oficiales. La documentación web puede
corresponder a una versión distinta de la instalada. Registrar versión, fecha
de consulta y edición; preferir manual local cuando exista una discrepancia.
No fijar una versión upstream como requisito universal de Fedora o RHEL.

| Fuente | Acceso | Uso |
| --- | --- | --- |
| GNU Coreutils | https://www.gnu.org/software/coreutils/manual/coreutils.html | Semántica, inventario y opciones |
| Coreutils upstream | https://github.com/coreutils/coreutils | Código y tests; fijar tag o commit |
| GNU Findutils | https://www.gnu.org/software/findutils/manual/ | find, xargs, seguridad y recorrido |
| GNU bc | https://www.gnu.org/software/bc/manual/bc.html | Lenguaje; comprobar implementación local |
| rsync | https://rsync.samba.org/documentation.html | Manuales y algoritmo |
| rsync(1) | https://download.samba.org/pub/rsync/rsync.1 | Transferencias, filtros, opciones y errores |
| rsyncd.conf(5) | https://download.samba.org/pub/rsync/rsyncd.conf.5 | Configuración del daemon |
| POSIX | https://pubs.opengroup.org/onlinepubs/9799919799/ | POSIX.1-2024; indicar edición al comparar |
| Linux man-pages | https://www.kernel.org/doc/man-pages/ | Contratos de interfaces del kernel y libc |
| Fedora Packaging Guidelines | https://docs.fedoraproject.org/en-US/packaging-guidelines/ | Proyecto RPM |
| Fedora Packages | https://packages.fedoraproject.org/ | Proveedores y versiones por distribución |
| systemd | https://www.freedesktop.org/software/systemd/man/latest/ | Units, timers y dependencia de montajes |
| The Linux Command Line | https://linuxcommand.org/tlcl.php | Referencia didáctica; comprobar edición |

### Evidencia y discrepancias

Una prueba observada no se convierte automáticamente en garantía de interfaz:
puede depender del entorno, de la configuración o de un defecto. Registrar
comando, versión, filesystem, locale, privilegios y resultado antes de concluir.
Separar comportamiento documentado, comportamiento observado y conformidad
POSIX. Si difieren, explicar la discrepancia sin redefinir la especificación.

Las ediciones de los libros se identificarán desde la copia realmente utilizada.
No deducir número de edición o capítulo del título bibliográfico. Para TLPI y
APUE, la lectura de C es profundización opcional, no prerrequisito del recorrido.
Los snippets de buscadores sirven para localizar fuentes, no sustituyen la
verificación de una opción contra el manual de la versión que usa el laboratorio.


## Fuentes principales para los bloques 91–98

### fzf

- Repositorio y documentación upstream: https://github.com/junegunn/fzf
- Manual local `man fzf`, `fzf --help` y versión instalada.
- Verificar soporte real de `--read0`, `--print0`, `--preview`,
  `--bind`, `--filter` y variables de entorno en la versión utilizada.

### GNU tar y formatos de archivado

- GNU tar Manual: https://www.gnu.org/software/tar/manual/
- `tar(1)` local; POSIX para ustar/pax cuando corresponda.
- Comprobar opciones GNU de ACL, xattrs, SELinux y archivos incrementales.

### Compresión

- gzip: https://www.gnu.org/software/gzip/manual/
- bzip2: https://sourceware.org/bzip2/
- XZ Utils: https://tukaani.org/xz/
- Zstandard: https://facebook.github.io/zstd/
- Documentación local: `gzip(1)`, `bzip2(1)`, `xz(1)`, `zstd(1)`.

### ZIP y compresión paralela

- `zip(1)`, `unzip(1)`, `zipinfo(1)` y documentación de las
  implementaciones instaladas.
- `pigz(1)`, `pixz(1)` y opciones multithread de `zstd(1)`;
  verificar proveedores, disponibilidad y versiones con RPM/DNF.

### Criterios de lectura y verificación

Aplicar la jerarquía de fuentes ya definida: manual de la versión
instalada, pruebas reproducibles, documentación upstream y normas
aplicables. No confundir CRC/checksum de formato con autenticación,
ni una extracción exitosa con una restauración verificada.


## Fuentes para la extensión awesome-cli (99–110)

Catálogo de descubrimiento: https://github.com/jmparis/awesome-cli
README consultado el 25 de octubre de 2026; blob
`5b302f64391ce43ca22faacde1ed434c2799dbfc`.
No reproducir sus calificativos de velocidad o compatibilidad como garantías.
Para cada lección consultar README, manual y documentación de la versión
instalada del proyecto correspondiente. Registrar release/tag/commit cuando
se cite implementación; comprobar proveedores locales con RPM/DNF.

| Herramienta | Proyecto de referencia | Aplicación |
| --- | --- | --- |
| bat | https://github.com/sharkdp/bat | Bloque 100 |
| exa | https://github.com/ogham/exa | Bloque 101 |
| lsd | https://github.com/Peltoche/lsd | Bloque 101 |
| delta | https://github.com/dandavison/delta | Bloque 100 |
| dust | https://github.com/bootandy/dust | Bloque 103 |
| duf | https://github.com/muesli/duf | Bloque 103 |
| broot | https://github.com/Canop/broot | Bloque 102 |
| fd | https://github.com/sharkdp/fd | Bloque 102 |
| ripgrep | https://github.com/BurntSushi/ripgrep | Bloque 106 |
| ag | https://github.com/ggreer/the_silver_searcher | Bloque 106 |
| fzf | https://github.com/junegunn/fzf | Bloque 91–93 |
| mcfly | https://github.com/cantino/mcfly | Bloque 107 |
| choose | https://github.com/theryangeary/choose | Bloque 104 |
| jq | https://github.com/stedolan/jq | Bloque 104 |
| sd | https://github.com/chmln/sd | Bloque 106 |
| cheat | https://github.com/cheat/cheat | Bloque 105 |
| tldr | https://github.com/tldr-pages/tldr | Bloque 105 |
| bottom | https://github.com/ClementTsang/bottom | Bloque 107 |
| glances | https://github.com/nicolargo/glances | Bloque 107 |
| gtop | https://github.com/aksakalli/gtop | Bloque 107 |
| hyperfine | https://github.com/sharkdp/hyperfine | Bloque 105 |
| gping | https://github.com/orf/gping | Bloque 108 |
| procs | https://github.com/dalance/procs | Bloque 107 |
| httpie | https://github.com/httpie/httpie | Bloque 108 |
| curlie | https://github.com/rs/curlie | Bloque 108 |
| xh | https://github.com/ducaale/xh | Bloque 108 |
| zoxide | https://github.com/ajeetdsouza/zoxide | Bloque 102 |
| dog | https://github.com/ogham/dog | Bloque 108 |

Referencias actualizadas adicionales:

- eza: https://github.com/eza-community/eza y manuales del proyecto.
- exa: https://github.com/ogham/exa; la advertencia de su README justifica
  tratarlo como antecedente y remitir a eza.
- jq: https://github.com/jqlang/jq y https://jqlang.org/manual/.
- lsd: https://github.com/lsd-rs/lsd; comprobar redirección del enlace histórico.
- Bash: https://www.gnu.org/software/bash/manual/.
- Zsh: https://www.zsh.org/Doc/.

cheat y tldr son ayudas comunitarias, no fuentes normativas. Distinguir
la colección tldr-pages del cliente instalado. Medir con hyperfine no
demuestra equivalencia semántica; verificar primero los resultados.
No trasladar a sd, choose, fd o rg las opciones y dialectos de otras herramientas.
En HTTP, DNS y monitorización prevalece el manual de la implementación y
se remite al PATH especializado para desarrollar el dominio completo.
