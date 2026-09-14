# DOMAIN — OPENSSH + WATCHDOG EN PROFUNDIDAD — FEDORA

## 1. Identidad del PATH

Este PATH enseña OpenSSH y Watchdog desde fundamentos hasta administración, seguridad,
diagnóstico e internals, usando Fedora como plataforma principal.

No debe tratar OpenSSH como una simple colección de comandos. Debe explicar la relación entre:

- protocolo SSH y OpenSSH;
- cliente `ssh` y servidor `sshd`;
- configuración global, por usuario y modular mediante `Include`;
- claves de usuario, host keys, `known_hosts`, `authorized_keys` y agentes;
- algoritmos criptográficos y crypto-policies de Fedora;
- forwarding, ProxyJump, bastiones, SCP y SFTP;
- systemd, firewalld y SELinux;
- hardening, auditoría y troubleshooting;
- watchdog del kernel, lockups y watchdogs hardware/software;
- sysctl, `/proc`, `/sys`, módulos del kernel y parámetros de arranque;
- watchdog de userspace y watchdog integrado con systemd.

El alumno debe terminar siendo capaz de descubrir, configurar, verificar, endurecer y
diagnosticar estos subsistemas sin depender de recetas memorizadas.

## 2. Plataforma

Plataforma primaria: Fedora Linux actual.

Las explicaciones deben partir del comportamiento real de Fedora y distinguir claramente:

1. comportamiento definido por upstream OpenSSH;
2. integración y empaquetado de Fedora;
3. configuración administrada por systemd;
4. restricciones de SELinux;
5. configuración de firewalld;
6. crypto-policies de Fedora;
7. comportamiento del kernel Linux;
8. diferencias históricas que puedan aparecer en bibliografía antigua.

No asumir que configuraciones antiguas siguen siendo válidas.

## 3. Alcance de OpenSSH

Cubrir en profundidad:

- SSH como protocolo;
- arquitectura cliente-servidor;
- `ssh`;
- `sshd`;
- `ssh-keygen`;
- `ssh-agent`;
- `ssh-add`;
- `ssh-copy-id`;
- `ssh-keyscan`;
- `sftp`;
- `scp`;
- paquetes `openssh`, `openssh-clients` y `openssh-server`;
- descubrimiento mediante RPM;
- páginas man;
- `ssh -V`;
- `ssh -G`;
- `sshd -t`;
- `sshd -T`;
- `/etc/ssh/`;
- `/etc/ssh/ssh_config`;
- `/etc/ssh/ssh_config.d/`;
- `/etc/ssh/sshd_config`;
- `/etc/ssh/sshd_config.d/`;
- `~/.ssh/config`;
- configuración modular de usuario mediante `Include`;
- configuración equivalente para root cuando corresponda;
- precedencia y semántica first-value-wins donde aplique;
- bloques `Host`;
- bloques `Match`;
- autenticación mediante claves;
- restricciones en `authorized_keys`;
- host keys;
- `known_hosts`;
- fingerprinting;
- forwarding local, remoto y dinámico;
- bastiones y `ProxyJump`;
- multiplexación;
- keepalives;
- transferencia de archivos;
- integración con systemd;
- logging mediante journal;
- firewalld;
- SELinux;
- hardening;
- troubleshooting;
- inspección efectiva de configuración.

## 4. Configuración modular

La configuración modular es una parte fundamental del PATH.

Explicar explícitamente:

```text
~/.ssh/config
~/.ssh/config.d/*.conf
```

cuando el usuario decide implementar esta organización mediante `Include`, y distinguirla
de los mecanismos y archivos proporcionados por el sistema.

También explicar:

```text
/etc/ssh/ssh_config
/etc/ssh/ssh_config.d/
```

y:

```text
/etc/ssh/sshd_config
/etc/ssh/sshd_config.d/
```

No presentar un directorio creado por el usuario como si necesariamente fuese un estándar
upstream o un directorio suministrado por Fedora.

Enseñar siempre a verificar el resultado efectivo con herramientas como:

```bash
ssh -G host
sudo sshd -T
sudo sshd -t
```

## 5. Precedencia

La precedencia debe explicarse conceptualmente y comprobarse experimentalmente.

Evitar reglas simplificadas del tipo “el último valor siempre gana”.

Para el cliente OpenSSH debe explicarse la selección de valores, el procesamiento de bloques
`Host`, los archivos implicados y por qué el orden puede modificar el resultado.

Usar `ssh -G` para demostrar la configuración resultante.

Para `sshd`, enseñar la interacción entre configuración principal, `Include`, defaults y
bloques `Match`, utilizando `sshd -T` y, cuando proceda, sus opciones de contexto.

## 6. Criptografía

Cubrir:

- claves de usuario;
- host keys;
- Ed25519;
- ECDSA;
- RSA;
- algoritmos legacy únicamente cuando sean necesarios para comprender compatibilidad;
- KEX;
- ciphers;
- MACs;
- firmas;
- fingerprints;
- `ssh -Q`;
- negociación;
- compatibilidad;
- crypto-policies de Fedora.

No recomendar algoritmos obsoletos solo porque aparezcan en el libro principal.

Distinguir siempre entre:

- explicación histórica;
- compatibilidad legacy;
- recomendación moderna.

## 7. Seguridad

El alumno debe comprender el efecto y las implicaciones de:

- `PermitRootLogin`;
- `PasswordAuthentication`;
- `PubkeyAuthentication`;
- `AuthenticationMethods` cuando corresponda;
- `AllowUsers`;
- `AllowGroups`;
- `DenyUsers`;
- `DenyGroups`;
- restricciones de `authorized_keys`;
- forwarding;
- agentes;
- permisos de archivos;
- host-key verification;
- `StrictHostKeyChecking`;
- bastiones;
- exposición de puertos;
- firewalld;
- SELinux;
- crypto-policies;
- privilegios y separación de responsabilidades.

No presentar hardening como una lista universal de valores. Explicar amenaza, contexto,
consecuencia y método de validación.

## 8. Fedora

Cuando sea útil, emplear:

```bash
rpm -qi
rpm -ql
rpm -qf
dnf
systemctl
journalctl
firewall-cmd
getenforce
ls -Z
semanage
restorecon
ausearch
setsebool
update-crypto-policies
```

El alumno debe aprender a descubrir qué paquete instala un archivo, qué servicio controla
un componente y dónde está documentada una configuración.

## 9. Watchdog

Watchdog constituye una segunda parte diferenciada del PATH.

No confundir watchdog con SSH ni con comunicación cliente-servidor.

Explicar:

- concepto de watchdog;
- watchdog hardware;
- watchdog software;
- lockups;
- soft lockup;
- hard lockup;
- NMI watchdog;
- watchdog del kernel;
- watchdog de userspace;
- drivers;
- módulos;
- `/dev/watchdog`;
- `/dev/watchdog0`;
- configuración del kernel;
- `/boot/config-$(uname -r)`;
- `CONFIG_WATCHDOG`;
- opciones `CONFIG_*WATCHDOG*`;
- sysctl;
- `/proc/sys/kernel/`;
- `/sys`;
- parámetros de módulos;
- kernel command line;
- `grubby`;
- systemd watchdog;
- `RuntimeWatchdogSec=`;
- `RebootWatchdogSec=`;
- `WatchdogSec=`;
- `sd_notify()` cuando corresponda;
- diagnóstico.

## 10. Parámetros del kernel

Explicar y verificar según disponibilidad/versiones:

```text
kernel.watchdog
kernel.soft_watchdog
kernel.nmi_watchdog
kernel.watchdog_thresh
kernel.watchdog_cpumask
```

No asumir que todos existen o se comportan igual en cualquier kernel.

Enseñar a descubrirlos con:

```bash
sysctl
sysctl -a
/proc/sys/kernel/
/boot/config-$(uname -r)
modinfo
lsmod
```

## 11. systemd y watchdog

Distinguir:

1. watchdog hardware administrado por PID 1;
2. watchdog del kernel;
3. watchdog de un servicio;
4. supervisión normal de procesos por systemd.

Explicar la relación entre:

```text
RuntimeWatchdogSec=
RebootWatchdogSec=
WatchdogSec=
NotifyAccess=
Type=notify
```

sin mezclarlos como si fueran el mismo mecanismo.

## 12. Método pedagógico

Cada lección debe comenzar obligatoriamente con:

# 🎯 OBJETIVO

Después desarrollar el tema de forma progresiva, profunda y práctica.

Cuando aporten valor incluir:

# 🧪 Laboratorio / ejemplos

# ⚠️ Errores frecuentes

# 💡 Idea importante

Cada lección debe finalizar obligatoriamente con:

# 🧠 QUÉ DEBES RECORDAR

Este último apartado debe contener entre 3 y 7 ideas esenciales y no limitarse a repetir
el objetivo.

## 13. Estilo

- Español técnico claro.
- Comandos y rutas exactos.
- Explicar antes de memorizar.
- No convertir las lecciones en resúmenes.
- Evitar saltos conceptuales.
- Relacionar teoría y comportamiento observable.
- Utilizar ejemplos reproducibles en Fedora.
- Diferenciar configuración persistente y temporal.
- Diferenciar upstream, Fedora y decisiones del administrador.
- Explicar cómo verificar cada cambio importante.
- Indicar riesgos antes de cambios que puedan bloquear acceso SSH.

## 14. Laboratorios

Los laboratorios deben fomentar descubrimiento y diagnóstico.

Ejemplos:

```bash
rpm -ql openssh-clients
rpm -ql openssh-server
man ssh_config
man sshd_config
ssh -G host
sudo sshd -t
sudo sshd -T
ssh -Q cipher
systemctl status sshd
journalctl -u sshd
firewall-cmd --list-all
getenforce
sysctl kernel.watchdog
grep WATCHDOG /boot/config-$(uname -r)
```

No limitarse a “copiar comando → observar salida”. Explicar qué hipótesis se está verificando.

## 15. Troubleshooting

Aplicar una metodología por capas:

1. cliente;
2. resolución de nombres y red;
3. puerto;
4. firewalld;
5. servidor;
6. configuración efectiva;
7. autenticación;
8. permisos;
9. SELinux;
10. criptografía;
11. logs;
12. sistema/kernel cuando corresponda.

Usar herramientas como:

```bash
ssh -v
ssh -vv
ssh -vvv
ss
journalctl
sshd -t
sshd -T
ssh -G
firewall-cmd
ausearch
```

## 16. Criterio de profundidad

Una lección no está completa por definir el término.

Debe responder, según proceda:

- qué es;
- para qué existe;
- dónde se implementa;
- quién lo controla;
- dónde se configura;
- cómo se inspecciona;
- cómo se modifica;
- cómo se verifica;
- cómo interactúa con otros componentes;
- qué puede fallar;
- cómo se diagnostica;
- qué implicaciones de seguridad tiene.

## 17. Resultado final esperado

Al completar el PATH, el alumno debe poder administrar OpenSSH en Fedora de forma
independiente, construir configuraciones modulares cliente/servidor, diagnosticar problemas
por capas, aplicar hardening razonado y comprender/configurar los mecanismos watchdog del
kernel, hardware, userspace y systemd.
