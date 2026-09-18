# BIBLIOGRAFÍA — OPENSSH + WATCHDOG EN PROFUNDIDAD — FEDORA

## Bibliografía principal

### Barrett, Daniel J.; Silverman, Richard E.; Byrnes, Robert G.
**SSH, The Secure Shell: The Definitive Guide, 2nd Edition. O'Reilly Media.**

Libro principal del PATH para construir una comprensión profunda de SSH y OpenSSH.

Utilizar especialmente para:

- fundamentos de SSH;
- arquitectura cliente-servidor;
- autenticación;
- claves;
- agentes;
- forwarding;
- port forwarding;
- configuración del cliente;
- configuración del servidor;
- seguridad;
- automatización;
- administración y troubleshooting conceptual.

### Regla de uso

El libro es una fuente conceptual e histórica de gran valor, pero su segunda edición es
anterior a numerosas características y decisiones actuales de OpenSSH.

Por ello:

> El libro principal nunca debe prevalecer sobre la documentación actual de OpenSSH,
> Fedora, systemd o el kernel Linux cuando exista una diferencia de comportamiento,
> sintaxis, algoritmos, defaults o recomendaciones de seguridad.

No trasladar automáticamente configuraciones legacy a una Fedora moderna.

---

## Documentación principal actual — OpenSSH

### OpenSSH manual pages

Fuentes normativas operativas:

```text
ssh(1)
sshd(8)
ssh_config(5)
sshd_config(5)
ssh-keygen(1)
ssh-agent(1)
ssh-add(1)
ssh-copy-id(1), cuando esté disponible como documentación instalada
ssh-keyscan(1)
sftp(1)
scp(1)
```

Consultar localmente mediante:

```bash
man ssh
man sshd
man ssh_config
man sshd_config
man ssh-keygen
man ssh-agent
man ssh-add
man ssh-keyscan
man sftp
man scp
```

Las páginas man correspondientes a la versión instalada tienen prioridad para sintaxis,
opciones y comportamiento efectivo.

### OpenSSH upstream

Documentación, release notes y código fuente de OpenSSH Portable.

Utilizar para:

- cambios entre versiones;
- algoritmos;
- opciones nuevas/deprecadas;
- defaults;
- compatibilidad;
- comportamiento interno;
- evolución de SCP/SFTP;
- seguridad.

---

## Fedora

### Fedora Documentation

Fuente de referencia para la integración con la distribución.

Utilizar para:

- administración del sistema;
- paquetes;
- systemd;
- SELinux;
- firewalld;
- políticas criptográficas;
- networking;
- troubleshooting.

### Paquetes RPM

La propia instalación constituye una fuente primaria de descubrimiento:

```bash
rpm -qi openssh
rpm -qi openssh-clients
rpm -qi openssh-server

rpm -ql openssh
rpm -ql openssh-clients
rpm -ql openssh-server
```

Usar también:

```bash
rpm -qf /ruta/al/archivo
```

para relacionar archivos reales con sus paquetes.

---

## Fedora Crypto Policies

Consultar la documentación actual de Fedora y las páginas man instaladas relacionadas con
system-wide cryptographic policies.

Fundamental para comprender por qué la disponibilidad o aceptación de algoritmos SSH puede
estar condicionada por políticas externas a `ssh_config` y `sshd_config`.

Herramientas relevantes:

```bash
update-crypto-policies --show
ssh -Q
```

---

## systemd

### systemd manual pages

Referencias principales:

```text
systemd(1)
systemctl(1)
journalctl(1)
systemd-system.conf(5)
systemd.service(5)
systemd.exec(5)
systemd.kill(5)
systemd.unit(5)
sd_notify(3)
```

Especialmente importantes para Watchdog:

```text
RuntimeWatchdogSec=
RebootWatchdogSec=
WatchdogSec=
NotifyAccess=
```

Consultar siempre las páginas man correspondientes a la versión instalada.

---

## Linux Kernel

### Linux kernel documentation

Fuente principal para la parte Watchdog y lockups.

Áreas de estudio:

- watchdog API;
- watchdog device drivers;
- softlockup detector;
- hardlockup detector;
- NMI watchdog;
- kernel parameters;
- sysctl;
- watchdog framework;
- kernel configuration.

Utilizar la documentación correspondiente al kernel estudiado.

### Configuración local del kernel

Consultar:

```bash
uname -r
grep WATCHDOG /boot/config-$(uname -r)
```

y estudiar opciones como:

```text
CONFIG_WATCHDOG
CONFIG_WATCHDOG_CORE
CONFIG_SOFT_WATCHDOG
```

además de drivers específicos presentes en la configuración concreta.

---

## Manuales Linux relevantes

Según la lección:

```text
sysctl(8)
proc_sys_kernel(5)
proc(5)
modprobe(8)
modinfo(8)
lsmod(8)
systemd-system.conf(5)
systemd.service(5)
```

---

## SELinux

Fuentes:

- documentación Fedora SELinux;
- documentación del proyecto SELinux;
- páginas man de políticas instaladas;
- herramientas de análisis de AVC.

Comandos relevantes:

```bash
getenforce
ls -Z
restorecon
semanage
ausearch
```

No recomendar desactivar SELinux como solución ordinaria a un problema SSH.

---

## firewalld

Fuentes:

- documentación oficial de firewalld;
- documentación Fedora;
- páginas man instaladas.

Comandos relevantes:

```bash
firewall-cmd --state
firewall-cmd --get-active-zones
firewall-cmd --list-all
firewall-cmd --get-services
```

---

## Jerarquía de fuentes

Ante contradicciones utilizar este orden orientativo:

1. comportamiento comprobado de la versión instalada;
2. páginas man de la versión instalada;
3. documentación upstream correspondiente a esa versión;
4. documentación actual de Fedora;
5. documentación actual de systemd/kernel para sus respectivos subsistemas;
6. libro principal;
7. fuentes históricas o secundarias.

El libro sigue siendo la guía conceptual principal para SSH, pero no debe emplearse para
imponer defaults o prácticas obsoletas.

---

## Política bibliográfica del generador

Las lecciones deben combinar bibliografía y comprobación práctica.

No inventar:

- opciones;
- rutas;
- defaults;
- algoritmos;
- parámetros sysctl;
- opciones CONFIG_;
- directivas systemd.

Cuando algo dependa de versión, hardware, kernel o empaquetado, indicarlo expresamente y
enseñar al alumno cómo descubrirlo.

## Bibliografía específica por área

| Área | Fuente prioritaria |
|---|---|
| Fundamentos SSH | Barrett et al., *SSH, The Secure Shell*, 2e |
| Cliente OpenSSH | `ssh(1)`, `ssh_config(5)` |
| Servidor OpenSSH | `sshd(8)`, `sshd_config(5)` |
| Claves | `ssh-keygen(1)` |
| Agent | `ssh-agent(1)`, `ssh-add(1)` |
| SCP/SFTP | `scp(1)`, `sftp(1)` |
| Algoritmos | OpenSSH actual + `ssh -Q` |
| Fedora | Fedora Documentation + RPM instalado |
| Crypto policies | Fedora system-wide crypto policies |
| systemd | manuales oficiales systemd |
| SELinux | Fedora/SELinux + políticas instaladas |
| firewalld | firewalld + Fedora |
| Watchdog kernel | Linux kernel documentation |
| Watchdog systemd | `systemd-system.conf(5)`, `systemd.service(5)` |
| Lockups | Linux kernel documentation |
| Internals | código/documentación upstream correspondiente |

## Referencia principal del PATH

Barrett, Daniel J.; Silverman, Richard E.; Byrnes, Robert G.
*SSH, The Secure Shell: The Definitive Guide*. 2nd Edition. O'Reilly Media.
