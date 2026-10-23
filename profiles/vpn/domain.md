# Dominio — OpenVPN + WireGuard

## Propósito

Este itinerario desarrolla dominio progresivo de redes privadas virtuales sobre Linux, con especialización práctica y profunda en OpenVPN y WireGuard. El objetivo no es limitarse a desplegar un túnel funcional, sino comprender el comportamiento de la red, criptografía, routing, firewall, DNS, MTU, seguridad, observabilidad, automatización e internals necesarios para diseñar y operar soluciones VPN mantenibles.

## Plataforma principal

- Fedora y RHEL como plataformas Linux de referencia.
- systemd para gestión de servicios.
- NetworkManager y `nmcli` cuando corresponda.
- firewalld y nftables para filtrado, forwarding y NAT.
- SELinux en modo enforcing.
- `iproute2` para direccionamiento, routing y policy routing.
- OpenSSL y Easy-RSA para los componentes PKI de OpenVPN.
- `wg` y `wg-quick` para WireGuard.
- Ansible como mecanismo principal de automatización.
- Terraform como complemento de infraestructura cuando exista infraestructura externa que aprovisionar.

## Alcance técnico

### Fundamentos compartidos
IPv4, IPv6, CIDR, routing, forwarding, NAT, UDP/TCP, TUN/TAP, MTU/MSS, DNS, namespaces y modelos full-tunnel/split-tunnel.

### Criptografía
Criptografía simétrica y asimétrica, AEAD, hashes, HMAC, intercambio de claves, forward secrecy, PKI, X.509 y ciclo de vida de claves.

### OpenVPN
Arquitectura cliente-servidor, canales de control y datos, TLS, PKI, Easy-RSA, perfiles `.ovpn`, routing, CCD/`iroute`, autenticación, operación mediante systemd, management interface, hardening y troubleshooting.

### WireGuard
Peers, claves, handshake, Noise, cryptokey routing, `AllowedIPs`, endpoints, roaming, `PersistentKeepalive`, `wg`, `wg-quick`, NetworkManager, policy routing e internals de la implementación Linux.

### Integración Linux
firewalld, nftables, SELinux, systemd, NetworkManager, journald, iproute2, namespaces, Podman y componentes de observabilidad.

### Nivel avanzado
Policy-Based Routing, múltiples tablas, `fwmark`, multi-WAN, routing dinámico con FRRouting, OSPF/BGP sobre túneles, alta disponibilidad, multi-site, HA, automatización y análisis de código/internals.

## Filosofía del curso

El curso debe explicar primero el mecanismo y después la configuración. Cada directiva o comando importante debe relacionarse con el efecto que produce en interfaces, tablas de routing, firewall, resolución DNS o flujo de paquetes.

Las lecciones prácticas deben favorecer la inspección del estado real del sistema mediante herramientas como:

```bash
ip addr
ip route
ip rule
ss
wg show
firewall-cmd
nft
journalctl
tcpdump
tracepath
iperf3
openssl
```

## Progresión

1. Fundamentos de networking y criptografía.
2. OpenVPN desde instalación hasta administración avanzada.
3. WireGuard desde configuración básica hasta cryptokey routing e internals.
4. Integración con el stack Fedora/RHEL.
5. Seguridad, observabilidad y rendimiento.
6. Automatización e Infrastructure as Code.
7. Arquitecturas multi-site, routing avanzado y HA.
8. Internals y debugging.
9. Laboratorios expertos.
10. Proyecto final de arquitectura y operación.

## Laboratorios

Los laboratorios deben ser reproducibles y, cuando sea viable, construirse mediante máquinas virtuales o network namespaces para evitar depender de infraestructura externa.

Deben cubrir como mínimo:

- OpenVPN remote-access.
- OpenVPN site-to-site.
- WireGuard remote-access.
- WireGuard site-to-site.
- Full tunnel.
- Split tunnel.
- IPv4/IPv6 dual stack.
- DNS y split DNS.
- NAT y forwarding.
- firewalld y nftables.
- Policy routing.
- Multi-site.
- HA.
- Observabilidad.
- Automatización con Ansible.
- Diagnóstico de fallos intencionados.

## Metodología de troubleshooting

El diagnóstico debe comenzar observando el sistema antes de modificar la configuración. La secuencia pedagógica preferida es:

```text
servicio / proceso
        ↓
estado + logs
        ↓
interfaz y direcciones
        ↓
routing / policy routing
        ↓
firewall / NAT
        ↓
DNS
        ↓
MTU / MSS
        ↓
captura de paquetes
```

En OpenVPN se debe enseñar a correlacionar los logs propios del servidor y cliente con journald, TLS/PKI, NetworkManager, firewalld/nftables y eventos SELinux. Deben explicarse los niveles `verb`, las directivas `log`, `log-append` y `status`, la interpretación de errores frecuentes y el riesgo de habilitar logging excesivamente detallado en producción.

En WireGuard se debe remarcar que el modelo de diagnóstico es diferente: `wg show` y el estado observable del túnel —handshake, RX/TX, endpoint, `AllowedIPs` y keepalive— son fundamentales y se complementan con journald, logs del kernel, NetworkManager, firewall, SELinux y captura de paquetes.

El estudiante debe aprender a correlacionar timestamps y evidencias procedentes de distintas capas, y a distinguir entre:

- logs de aplicación o servicio;
- estado operativo;
- métricas;
- eventos del kernel;
- eventos del firewall;
- denegaciones SELinux/AVC;
- capturas de paquetes.

No se debe cambiar múltiples parámetros simultáneamente para intentar resolver un fallo. Cada hipótesis debe comprobarse con evidencia y cada cambio debe poder relacionarse con el resultado observado.


## Seguridad

No se debe enseñar a solucionar problemas desactivando permanentemente SELinux o el firewall. Los fallos deben diagnosticarse y corregirse conservando las protecciones del sistema.

Las claves privadas, PSK, certificados y credenciales utilizadas en ejemplos deben ser ficticios o generados específicamente para los laboratorios.

## Relación con otros itinerarios

Este PATH puede apoyarse en itinerarios independientes de systemd, SELinux, firewalld, Ansible y observabilidad. Aquí esos componentes se estudian específicamente desde la perspectiva de OpenVPN y WireGuard, evitando repetir innecesariamente cursos completos de cada tecnología.

## Resultado esperado

Al finalizar, el estudiante debe ser capaz de diseñar, desplegar, asegurar, automatizar, observar, diagnosticar y mantener arquitecturas OpenVPN y WireGuard desde escenarios de acceso remoto sencillos hasta redes site-to-site, multi-site y de alta disponibilidad.

## Alcance experto consolidado

### IAM para OpenVPN
Estudiar autenticación y autorización diferenciadas: PAM, SSSD, FreeIPA, RADIUS y MFA mediante componentes compatibles. Explicar el papel de LDAP/Kerberos como servicios de identidad subyacentes, no como autenticación integrada automática de OpenVPN. Correlacionar logs de OpenVPN, PAM, SSSD, proveedores IAM y SELinux.

### Identidad y gestión de peers WireGuard
WireGuard autentica peers mediante claves criptográficas; no incorpora PAM, LDAP, Kerberos ni MFA de usuario de manera nativa. La asociación con personas, la autorización por grupos y el onboarding/offboarding requieren sistemas externos, inventario y políticas de red.

### Ingeniería e internals
Profundizar en TLS 1.3, DCO y compatibilidad OpenVPN, además de mensajes WireGuard, NoiseIK, cookies, protección antirreplay, temporizadores, netlink, código fuente y trazas. Distinguir siempre configuración del protocolo y comportamiento de herramientas auxiliares como wg-quick.

### Operación y resiliencia
Diseñar indicadores de servicio, monitorización sintética, alertas, control de cambios, backup/restore probado, actualizaciones y rollback. Diferenciar con pruebas medibles el failover de gateways de la continuidad de sesiones. Medir RTO/RPO y registrar evidencias.

### Criterios de profundidad por lección
Cada lección debe incluir objetivo, explicación conceptual, flujo de paquetes o secuencia de eventos cuando aplique, comandos explicados opción por opción, archivos/rutas afectados, integración Fedora/RHEL, observación de estado, logs pertinentes, errores habituales, seguridad, laboratorio reproducible, verificación, limpieza y referencias concretas. Evitar repetir contenidos de otros itinerarios salvo su aplicación directa a VPN.

### Criterios de aceptación de laboratorios
Los laboratorios deben tener topología explícita, prerrequisitos, comandos de preparación, configuración, pruebas positivas y negativas, evidencia de routing/firewall/DNS, captura o logs cuando proceda, rollback y criterios de éxito. Probar dual-stack, caída de túnel, rutas de retorno, revocación de acceso, recuperación y fugas DNS/IPv6.

### Estructura revisada
Se conservan los bloques 0–33 y se profundizan; se añaden 34 OpenVPN + IAM, 35 Gestión de identidad y peers WireGuard, 36 Ingeniería de protocolos VPN y 37 Operación VPN en producción y resiliencia. Los laboratorios expertos pasan a 38 y el proyecto final a 39.

## Contrato de progresión y eliminación de repeticiones

Se mantienen 40 bloques. Los temas recurrentes deben evolucionar mediante prerrequisitos, referencias a lecciones anteriores y nuevas evidencias; no repetir explicaciones completas.

| Bloques | Responsabilidad pedagógica |
| --- | --- |
| 0–1 | Preparar VMs, acceso de rescate, snapshots, topología y baseline; adquirir fundamentos. |
| 2–4 | En 2.19 se observa una demostración TLS con PKI desechable preparada por el instructor. El estudiante construye su propia PKI en 3 y reconstruye el despliegue en 4. No usar modo static-key como atajo. |
| 9 → 34 | En 9: mecanismos locales y visión general de integración. En 34: desplegar y diagnosticar IAM externo, autorización, MFA y baja efectiva. |
| 26 → 30 → 37 | En 26: instrumentación y alertas. En 30: redundancia y medición de failover. En 37: operar esos componentes conjuntamente con cambios, incidentes y restauración. |
| 32–33 → 36 | En 32/33: arquitectura y código de cada tecnología. En 36: investigación comparativa, trazas y regresiones sobre evidencias previas. |
| 38 → 39 | En 38: escenarios integradores con fallos. En 39: decisiones independientes, implementación y defensa mediante evidencias. |

## Precisiones técnicas obligatorias

- Registrar versión de distribución, kernel, OpenVPN, OpenSSL, wireguard-tools y gestores de red. Consultar el manual de la versión instalada; la presencia de un manual más reciente no garantiza disponibilidad de paquetes ni de DCO.
- Distinguir `auth` del HMAC y `auth-user-pass` de usuarios; explicar el comportamiento de AEAD y el contexto de control de acuerdo con la versión. No presentar `auth` como verificación de contraseña.
- Tratar la compresión como superficie de riesgo y compatibilidad histórica. Usar configuraciones sin compresión y comprobar qué opciones acepta la versión del laboratorio.
- Bloquear una cuenta o publicar una CRL no demuestra por sí mismo que una sesión ya abierta terminó. Probar rechazo de nuevas conexiones, reautenticación y terminación explícita de sesiones; considerar tokens y caché SSSD.
- WireGuard mantiene estado criptográfico y temporizadores. Un handshake antiguo en un peer ocioso no basta para declarar una caída; correlacionar tráfico esperado y sondas activas.
- `AllowedIPs` selecciona peers de salida y valida orígenes de entrada; la FIB de Linux decide la ruta hacia la interfaz. `wg` no instala por sí solo las rutas que añade `wg-quick` u otro gestor.
- `wg show ... dump` puede incluir claves privadas y PSK. No adjuntar su salida cruda a métricas, CI, incidencias ni evidencias. Preferir consultas específicas y redacción comprobada.
- `SaveConfig = true` puede sobrescribir cambios de archivo al bajar la interfaz. Elegir fuente de verdad. `wg syncconf` no sustituye la gestión de direcciones, rutas, DNS ni hooks.
- Un hostname en `Endpoint` requiere distinguir resolución inicial de actualización posterior. El cambio de IP de un registro DNS debe probarse con el gestor o automatización elegidos.
- En HA, replicar configuración no replica automáticamente sesiones criptográficas. Medir reconexión; no prometer continuidad por disponer de VRRP o conntrack.
- Probar ICMP/ICMPv6 necesario para PMTUD y el efecto de forwarding sobre Router Advertisements. Ajustar `accept_ra` solo cuando lo justifique la topología.
- Separar el propietario de reglas firewalld de tablas nftables propias. No ejecutar limpiezas globales del ruleset en un host administrado por firewalld.

## Rutas y evidencias de logging

El material debe descubrir el destino efectivo mediante la configuración y `systemctl cat`, en vez de asumir nombres de unidad o rutas idénticos en todas las versiones.

| Evidencia | Ubicación o herramienta | Condición |
| --- | --- | --- |
| Journal persistente | `/var/log/journal/`; consultar con `journalctl` | Según `Storage=` y estado efectivo de journald. |
| Journal volátil | `/run/log/journal/`; consultar con `journalctl` | Cuando el journal se almacena en memoria; se pierde tras reiniciar. |
| OpenVPN | Journal de su unidad o ruta de `log`/`log-append` | No existe un `/var/log/openvpn.log` universal. |
| Estado OpenVPN | Ruta de `status` | Es una instantánea de estado, no un histórico completo de eventos. |
| NetworkManager | `journalctl -u NetworkManager` | Filtrar por interfaz, perfil y ventana temporal. |
| WireGuard | `wg show`, journal de su gestor y `journalctl -k` | El protocolo no genera un log de sesiones equivalente a OpenVPN; debug del kernel es opcional. |
| Auditoría SELinux | `ausearch`; `/var/log/audit/audit.log` | Si auditd está instalado y configurado para ese destino; comprobar configuración. |
| Firewall | Journal/kernel o destino de logging configurado | Requiere reglas de logging; aplicar límites de tasa. |

Incluir `journalctl --list-boots`, filtrado temporal y por unidad, conservación, permisos y pruebas de rotación. La correlación entre máquinas exige relojes sincronizados. Las pruebas de fugas deben observar IPv4/IPv6 y el comportamiento real del resolver y las aplicaciones, incluyendo DNS cifrado cuando esté en alcance.

## Integración con course-generator

El archivo `profile.yaml` conserva las claves originales. Su sintaxis YAML y la coherencia con el temario pueden verificarse aquí; la aceptación semántica depende del cargador de la versión de course-generator utilizada. Las reglas esenciales también se expresan en este dominio para no depender exclusivamente de claves declarativas adicionales.

`files.pedagogy: ../../config/pedagogy.md` se conserva como dependencia externa. Antes de generar, resolver esa ruta según el cargador del proyecto y comprobar que existe, junto con `domain.md` y `bibliography.md`. Este paquete no incluye el repositorio ni permite certificar esa resolución. Ejecutar el modo `--dry-run` del generador en el checkout antes de producir lecciones.
