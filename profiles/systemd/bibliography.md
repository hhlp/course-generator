# Bibliography — SYSTEMD EN PROFUNDIDAD — FEDORA

## Alcance

Esta bibliografía acompaña el PATH **SYSTEMD EN PROFUNDIDAD — FEDORA** y debe utilizarse como soporte para generar lecciones profundas, prácticas y técnicamente rigurosas sobre systemd en Fedora.

El PATH no debe limitarse a resumir libros. Los libros proporcionan estructura pedagógica y contexto; la documentación oficial vigente de systemd y Fedora tiene prioridad cuando exista cualquier diferencia técnica, cambio de versión o comportamiento dependiente de la distribución.

---

## 1. Bibliografía principal

### Linux Service Management Made Easy with systemd

**Rol:** fuente principal de aprendizaje progresivo sobre administración de servicios con systemd.

Debe utilizarse especialmente para:

- fundamentos de systemd;
- transición desde init tradicionales;
- unidades y unit files;
- administración de servicios;
- dependencias;
- targets;
- systemctl;
- journal y journalctl;
- habilitación y arranque de servicios;
- timers;
- troubleshooting básico e intermedio;
- administración cotidiana de servicios Linux.

No debe considerarse una autoridad superior a la documentación oficial cuando existan diferencias de comportamiento entre versiones.

---

## 2. Bibliografía complementaria y de profundización

### David Both — *systemd for Linux SysAdmins: All You Need to Know About the systemd Suite for Linux Users*

**Rol:** profundización conceptual y práctica en el ecosistema systemd desde la perspectiva del administrador Linux.

Debe utilizarse especialmente para:

- arquitectura general del ecosistema systemd;
- boot y startup;
- servicios;
- targets;
- mounts;
- automounts;
- timers;
- systemd-journald;
- administración y diagnóstico;
- comprensión de dependencias;
- diseño operativo de unidades;
- herramientas auxiliares del ecosistema systemd;
- análisis del comportamiento del sistema.

Debe aprovecharse para relacionar los distintos componentes de la suite systemd y evitar estudiar `systemctl` como una herramienta aislada.

---

## 3. Documentación oficial — máxima autoridad técnica

### systemd

Fuentes prioritarias:

- manuales instalados en Fedora;
- páginas `man` correspondientes a cada componente;
- documentación oficial del proyecto systemd;
- documentación publicada en `systemd.io`;
- documentación de referencia del código fuente cuando sea necesario estudiar internals.

Páginas de manual especialmente relevantes:

- `systemd(1)`
- `systemctl(1)`
- `systemd.unit(5)`
- `systemd.service(5)`
- `systemd.exec(5)`
- `systemd.kill(5)`
- `systemd.resource-control(5)`
- `systemd.directives(7)`
- `systemd.syntax(7)`
- `systemd.special(7)`
- `systemd.target(5)`
- `systemd.timer(5)`
- `systemd.socket(5)`
- `systemd.path(5)`
- `systemd.mount(5)`
- `systemd.automount(5)`
- `systemd.swap(5)`
- `systemd.device(5)`
- `systemd.slice(5)`
- `systemd.scope(5)`
- `systemd.generator(7)`
- `systemd.generator(7)`
- `systemd-run(1)`
- `systemd-analyze(1)`
- `systemd-cgls(1)`
- `systemd-cgtop(1)`
- `systemd-journald.service(8)`
- `journald.conf(5)`
- `journalctl(1)`
- `systemd-tmpfiles(8)`
- `tmpfiles.d(5)`
- `systemd-sysusers(8)`
- `sysusers.d(5)`
- `systemd-creds(1)`
- `systemd.exec(5)`
- `systemd.security(7)`
- `systemd.preset(5)`
- `systemd.preset-all(1)`
- `systemd.environment-generator(7)`
- `systemd-system.conf(5)`
- `systemd-user.conf(5)`
- `systemd-logind.service(8)`
- `loginctl(1)`
- `systemd-user-sessions.service(8)`
- `systemd-oomd.service(8)`
- `oomd.conf(5)`
- `systemd-networkd.service(8)` cuando corresponda;
- `systemd-resolved.service(8)` cuando corresponda;
- `bootup(7)`.

Para cada lección se deben consultar las páginas de manual específicas del tema cuando resulte útil.

---

## 4. Fedora como plataforma de referencia

La distribución objetivo del PATH es **Fedora Linux**.

Deben utilizarse como referencias:

- Fedora Documentation;
- Fedora Packages;
- Fedora Changes cuando afecten a systemd;
- documentación de empaquetado RPM de Fedora;
- Fedora Packaging Guidelines;
- políticas de seguridad de Fedora;
- SELinux;
- firewalld;
- systemd presets;
- integración con RPM;
- configuración distribuida en `/usr/lib/systemd/`;
- overrides locales en `/etc/systemd/`;
- unidades de usuario;
- paquetes systemd instalados por Fedora.

Las lecciones deben explicar claramente cuándo un comportamiento pertenece a systemd upstream y cuándo deriva de decisiones o empaquetado de Fedora.

---

## 5. Código fuente e internals

Para temas avanzados e internals puede emplearse el código fuente upstream de systemd.

Debe utilizarse especialmente para:

- PID 1;
- manager;
- transaction engine;
- job engine;
- dependency graph;
- unit loading;
- generators;
- activation;
- cgroups;
- sd-bus;
- D-Bus API;
- journal internals;
- serialization;
- reexec;
- watchdog;
- socket activation;
- process supervision.

El código fuente no debe introducirse prematuramente. Primero debe explicarse el modelo conceptual y después relacionarlo con la implementación.

---

## 6. Jerarquía de confianza

Cuando varias fuentes entren en conflicto, utilizar este orden:

1. comportamiento comprobado en Fedora actual;
2. documentación oficial de systemd correspondiente a la versión instalada;
3. documentación oficial de Fedora;
4. código fuente upstream;
5. libros principales;
6. artículos, blogs y material externo.

Los libros nunca deben utilizarse para justificar sintaxis o comportamiento obsoleto frente a documentación oficial más reciente.

---

## 7. Uso pedagógico por nivel

### Fundamentos

Priorizar:

- Linux Service Management Made Easy with systemd;
- David Both;
- páginas `man` introductorias.

### Administración intermedia

Combinar:

- ambos libros;
- documentación oficial;
- laboratorios Fedora.

### Administración avanzada

Priorizar:

- documentación oficial;
- páginas `man`;
- Fedora;
- código fuente cuando sea necesario.

### Internals

Priorizar:

- documentación upstream;
- D-Bus;
- código fuente;
- herramientas de diagnóstico;
- pruebas reproducibles.

---

## 8. Principio de generación

Toda lección debe responder a tres preguntas:

1. ¿Qué modelo conceptual necesita comprender el alumno?
2. ¿Cómo se observa y administra realmente en Fedora?
3. ¿Cómo se diagnostica cuando falla?

El objetivo final no es memorizar comandos, sino comprender systemd como gestor de servicios, unidades, dependencias, procesos, recursos, eventos y estado del sistema.
