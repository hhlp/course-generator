# DOMAIN — SYSTEMD EN PROFUNDIDAD — FEDORA

## Identidad del dominio

Este dominio define un curso de nivel progresivo desde fundamentos hasta administración experta e internals de **systemd en Fedora Linux**.

El propósito no es enseñar únicamente `systemctl`. El curso debe construir una comprensión completa de systemd como:

- PID 1;
- service manager;
- unit manager;
- dependency manager;
- process supervisor;
- event-driven activation framework;
- cgroup manager;
- logging infrastructure;
- boot orchestration system;
- user service manager;
- resource-control framework;
- security boundary helper;
- D-Bus service;
- conjunto integrado de herramientas del sistema Linux.

---

## Plataforma objetivo

Distribución principal:

**Fedora Linux**

Las lecciones deben asumir un sistema Fedora moderno con systemd como PID 1.

Cuando sea útil se pueden mencionar RHEL y otros sistemas Linux, pero Fedora debe seguir siendo la referencia operativa.

No convertir el curso en material genérico independiente de distribución cuando Fedora tenga comportamiento, rutas, presets, integración RPM, SELinux o políticas específicas relevantes.

---

## Objetivo pedagógico

El alumno debe progresar desde:

- entender qué es systemd;

hasta poder:

- leer y escribir unidades;
- interpretar dependencias;
- diagnosticar fallos de arranque;
- analizar transacciones;
- estudiar el journal;
- controlar recursos mediante cgroups;
- aplicar hardening;
- utilizar timers, sockets, paths y mounts;
- trabajar con servicios de usuario;
- comprender generators;
- integrar paquetes RPM;
- inspeccionar D-Bus;
- comprender partes relevantes de los internals;
- construir herramientas propias de diagnóstico;
- desarrollar el proyecto final `mini-systemd-debugger`.

---

## Estilo obligatorio de las lecciones

Todas las lecciones deben comenzar exactamente con:

# 🎯 OBJETIVO

El objetivo debe explicar qué será capaz de comprender o realizar el alumno al terminar la lección.

El contenido debe ser:

- profundo;
- didáctico;
- progresivo;
- técnicamente preciso;
- orientado a administración real;
- basado en Fedora;
- acompañado por ejemplos concretos;
- conectado con temas anteriores y posteriores cuando corresponda.

Cuando aporten valor, utilizar:

# 🧪 LABORATORIO / EJEMPLOS

# ⚠️ ERRORES FRECUENTES

# 💡 IDEA IMPORTANTE

Todas las lecciones deben terminar exactamente con:

# 🧠 QUÉ DEBES RECORDAR

Esta sección final debe contener entre **3 y 7 ideas clave**.

No debe repetir literalmente el objetivo.

---

## Profundidad esperada

No generar resúmenes superficiales.

Cada concepto importante debe cubrir, cuando corresponda:

1. definición;
2. motivación;
3. funcionamiento interno conceptual;
4. sintaxis;
5. archivos implicados;
6. rutas Fedora;
7. comandos de inspección;
8. ejemplos;
9. diagnóstico;
10. errores frecuentes;
11. relaciones con otros componentes de systemd;
12. seguridad;
13. persistencia;
14. implicaciones operativas.

---

## Filosofía de enseñanza

Evitar enseñar comandos aislados.

Ejemplo incorrecto:

> `systemctl start foo.service` inicia un servicio.

Ejemplo esperado:

Explicar:

- qué representa la unidad;
- cómo systemd la carga;
- qué dependencias pueden añadirse;
- qué job se crea;
- cómo entra en una transaction;
- qué significa el estado resultante;
- cómo comprobarlo;
- dónde aparecen los logs;
- cómo analizar un fallo.

---

## Fedora-first

Siempre que sea pertinente explicar:

- `/usr/lib/systemd/system/`;
- `/etc/systemd/system/`;
- `/run/systemd/system/`;
- `/usr/lib/systemd/user/`;
- `/etc/systemd/user/`;
- `~/.config/systemd/user/`;
- vendor units;
- local overrides;
- drop-ins;
- RPM ownership;
- presets;
- SELinux;
- cgroups;
- journald;
- D-Bus;
- integración con paquetes Fedora.

No recomendar editar directamente archivos vendor en `/usr/lib/systemd/system/`.

Enseñar preferentemente:

```bash
systemctl edit unidad.service
```

y explicar drop-ins y precedencia.

---

## Versiones y cambios de systemd

systemd evoluciona rápidamente.

Nunca asumir que una directiva existe en todas las versiones.

Cuando una característica sea dependiente de versión:

- indicarlo;
- comprobar documentación oficial;
- enseñar cómo consultar la versión:

```bash
systemd --version
```

y cómo buscar soporte:

```bash
man systemd.directives
man systemd.service
```

---

## Uso de documentación

Debe enseñarse al alumno a trabajar con documentación local.

Ejemplos:

```bash
man systemd
man systemctl
man systemd.unit
man systemd.service
man systemd.exec
man systemd.directives
man bootup
```

También utilizar:

```bash
systemd-analyze man
```

cuando resulte pertinente.

La documentación oficial prevalece sobre ejemplos encontrados en Internet.

---

## systemctl

No limitar `systemctl` a start/stop/status.

Cubrir profundamente:

- start;
- stop;
- restart;
- reload;
- try-restart;
- reload-or-restart;
- enable;
- disable;
- reenable;
- preset;
- preset-all;
- mask;
- unmask;
- isolate;
- daemon-reload;
- daemon-reexec;
- edit;
- cat;
- show;
- status;
- list-units;
- list-unit-files;
- list-dependencies;
- list-jobs;
- show-environment;
- set-environment;
- import-environment;
- reset-failed;
- kill;
- clean;
- freeze/thaw cuando esté soportado;
- bind cuando corresponda.

Diferenciar siempre:

- estado de runtime;
- estado de habilitación;
- estado de carga;
- estado activo;
- estado fallido.

---

## Modelo de unidades

Explicar los tipos de unidad relevantes:

- `.service`;
- `.socket`;
- `.target`;
- `.device`;
- `.mount`;
- `.automount`;
- `.swap`;
- `.timer`;
- `.path`;
- `.slice`;
- `.scope`.

Explicar que cada tipo representa objetos y eventos distintos dentro del manager.

---

## Dependencias

Cubrir profundamente:

- `Requires=`;
- `Wants=`;
- `Requisite=`;
- `BindsTo=`;
- `PartOf=`;
- `Upholds=` cuando aplique;
- `Conflicts=`;
- `Before=`;
- `After=`;
- `OnFailure=`;
- dependencias implícitas;
- dependencias por defecto;
- dependencies generadas;
- ordering frente a requirement dependencies.

Debe quedar absolutamente clara la diferencia entre:

- necesidad;
- orden;
- propagación;
- conflicto.

---

## Services

Cubrir los distintos modelos:

- `Type=simple`;
- `exec`;
- `forking`;
- `oneshot`;
- `dbus`;
- `notify`;
- `notify-reload`;
- `idle`.

Estudiar:

- `ExecStart=`;
- múltiples comandos;
- prefijos especiales;
- `ExecStartPre=`;
- `ExecStartPost=`;
- `ExecReload=`;
- `ExecStop=`;
- `ExecStopPost=`;
- `Restart=`;
- `RestartSec=`;
- start limits;
- timeouts;
- watchdog;
- notifications;
- exit status;
- process tracking;
- `KillMode=`;
- signals;
- environment;
- working directories;
- credentials.

---

## Journald

Tratar journald como subsistema, no únicamente como fuente de `journalctl`.

Cubrir:

- journal binario;
- volatile y persistent storage;
- namespaces;
- fields;
- metadata;
- indexing;
- filtering;
- boot IDs;
- cursor;
- priorities;
- facilities;
- kernel messages;
- service stdout/stderr;
- rate limiting;
- forwarding;
- vacuum;
- disk usage;
- sealing cuando corresponda.

Comandos importantes:

```bash
journalctl
journalctl -u
journalctl -b
journalctl -k
journalctl -p
journalctl --since
journalctl --until
journalctl -o verbose
journalctl --disk-usage
journalctl --vacuum-time=
```

---

## Boot

Cubrir el proceso de arranque de forma conceptual:

firmware → bootloader → kernel → initramfs → systemd PID 1 → generators → units → targets.

Estudiar:

- default target;
- emergency target;
- rescue target;
- initrd;
- switch-root;
- generators;
- fstab generator;
- cryptsetup generator cuando corresponda;
- ordering;
- boot performance.

---

## systemd-analyze

Cubrir:

- `time`;
- `blame`;
- `critical-chain`;
- `plot`;
- `dot`;
- `verify`;
- `security`;
- `calendar`;
- `timespan`;
- `cat-config`;
- `dump`;
- `unit-paths`;
- otras funciones pertinentes según versión.

No presentar `blame` como prueba definitiva de culpabilidad por lentitud.

---

## Timers

Estudiar:

- monotonic timers;
- realtime/calendar timers;
- `OnBootSec=`;
- `OnStartupSec=`;
- `OnUnitActiveSec=`;
- `OnUnitInactiveSec=`;
- `OnCalendar=`;
- `Persistent=`;
- `RandomizedDelaySec=`;
- accuracy;
- wake system cuando aplique;
- timer/service relationship.

Comparar con cron sin presentar timers simplemente como “cron moderno”.

---

## Socket activation

Cubrir:

- listening sockets;
- activation;
- service association;
- Accept=yes/no;
- inet;
- Unix sockets;
- FIFO cuando corresponda;
- socket ownership;
- file descriptors;
- LISTEN_FDS;
- ventajas arquitectónicas;
- seguridad.

---

## Path activation

Explicar:

- PathExists;
- PathChanged;
- PathModified;
- DirectoryNotEmpty;
- activación;
- limitaciones;
- inotify;
- relación con services.

---

## Mounts

Relacionar:

- mount units;
- `/etc/fstab`;
- generators;
- naming rules;
- automount;
- dependencies;
- network mounts;
- remote-fs;
- local-fs;
- boot ordering.

---

## Cgroups

Explicar cgroup v2 como base del seguimiento de procesos y control de recursos.

Cubrir:

- slices;
- scopes;
- services;
- hierarchy;
- delegation;
- CPU;
- memory;
- IO;
- tasks;
- accounting;
- limits;
- systemd-cgls;
- systemd-cgtop.

Relacionar las directivas systemd con cgroup v2.

---

## Servicios de usuario

Cubrir:

- user manager;
- `systemctl --user`;
- login session;
- lingering;
- environment;
- user units;
- user timers;
- user sockets;
- dependencia respecto a logind.

Explicar claramente la diferencia entre:

- system manager;
- user manager.

---

## tmpfiles

Cubrir:

- creación;
- limpieza;
- permisos;
- ownership;
- directorios runtime;
- persistencia;
- aging;
- configuración vendor/local.

---

## sysusers

Cubrir:

- creación declarativa de usuarios/grupos;
- empaquetado;
- relación con RPM;
- diferencias frente a scripts manuales.

---

## Seguridad y hardening

Estudiar directivas como:

- `User=`;
- `Group=`;
- `DynamicUser=`;
- `NoNewPrivileges=`;
- `PrivateTmp=`;
- `PrivateDevices=`;
- `ProtectSystem=`;
- `ProtectHome=`;
- `ProtectKernelTunables=`;
- `ProtectKernelModules=`;
- `ProtectControlGroups=`;
- `CapabilityBoundingSet=`;
- `AmbientCapabilities=`;
- `RestrictAddressFamilies=`;
- `SystemCallFilter=`;
- `RestrictNamespaces=`;
- `LockPersonality=`;
- `MemoryDenyWriteExecute=`;
- filesystem namespace;
- credentials.

Utilizar:

```bash
systemd-analyze security
```

pero explicar que la puntuación es una ayuda heurística, no una demostración absoluta de seguridad.

---

## Credenciales

Cubrir el sistema de credentials de systemd:

- `LoadCredential=`;
- encrypted credentials;
- `systemd-creds`;
- acceso por servicios;
- ventajas sobre environment variables;
- integración con unidades.

---

## Packaging RPM

El curso debe explicar cómo un paquete Fedora instala y administra unidades.

Cubrir:

- ubicación vendor;
- presets;
- macros RPM;
- daemon-reload;
- enablement policy;
- actualización;
- eliminación;
- sysusers;
- tmpfiles;
- scriptlets cuando corresponda;
- ownership de unidades.

No enseñar prácticas históricas obsoletas si Fedora ofrece macros o mecanismos declarativos modernos.

---

## D-Bus

Explicar que systemd expone una API D-Bus.

Cubrir:

- manager object;
- unit objects;
- properties;
- methods;
- signals;
- busctl;
- introspection;
- monitorización;
- relación con systemctl.

Ejemplos:

```bash
busctl introspect org.freedesktop.systemd1 /org/freedesktop/systemd1
busctl tree org.freedesktop.systemd1
```

---

## Internals

Los temas avanzados deben introducir:

- manager;
- units;
- jobs;
- transactions;
- dependency graph;
- load states;
- active states;
- job modes;
- event loop;
- sd-event;
- sd-bus;
- serialization;
- daemon-reexec;
- generators;
- cgroups;
- notification protocol;
- PID tracking;
- main PID;
- control PID.

No convertir internals en una lectura lineal del código fuente.

---

## Troubleshooting

Cada bloque importante debe enseñar diagnóstico.

Flujo recomendado:

1. observar estado;
2. inspeccionar unidad efectiva;
3. consultar propiedades;
4. examinar journal;
5. revisar dependencias;
6. comprobar procesos/cgroups;
7. validar sintaxis;
8. inspeccionar seguridad;
9. revisar configuración vendor/drop-ins;
10. reproducir el fallo.

Herramientas:

```bash
systemctl status
systemctl cat
systemctl show
systemctl list-dependencies
systemctl list-jobs
journalctl
systemd-analyze verify
systemd-analyze dump
systemd-cgls
systemd-cgtop
busctl
```

---

## Laboratorios

Los laboratorios deben ser reproducibles en Fedora y evitar daños permanentes.

Cuando se modifique configuración:

- conservar backups cuando corresponda;
- preferir unidades de laboratorio;
- utilizar `/etc/systemd/system/`;
- usar drop-ins;
- limpiar recursos al finalizar.

Los ejemplos destructivos deben estar claramente marcados y, cuando sea posible, sustituidos por entornos seguros.

---

## Proyecto final

El PATH culmina en un:

**mini-systemd-debugger**

Debe integrar progresivamente:

- inspección de unidades;
- estados;
- unit files;
- dependencias;
- jobs;
- journal;
- cgroups;
- properties;
- security analysis;
- dependency graphs;
- boot analysis;
- diagnóstico automatizado.

El proyecto debe reforzar comprensión, no ocultar systemd detrás de una abstracción.

---

## Bibliografía del dominio

Fuentes principales:

1. *Linux Service Management Made Easy with systemd*.
2. David Both — *systemd for Linux SysAdmins: All You Need to Know About the systemd Suite for Linux Users*.
3. documentación oficial de systemd.
4. manuales locales de Fedora.
5. documentación Fedora.
6. código fuente upstream de systemd para internals.

Ante conflicto, prevalece la documentación oficial correspondiente a la versión instalada.
