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

## Relación con Identity & Access Management (IAM)

El itinerario debe enseñar explícitamente dos modos de operación: VPN autónoma sin IAM centralizado y VPN integrada con una plataforma central de identidad. La integración es opcional y no debe convertirse en requisito para aprender o desplegar OpenVPN o WireGuard.

### OpenVPN
OpenVPN puede funcionar de forma independiente mediante su PKI, certificados y mecanismos propios, y también puede actuar como consumidor de IAM cuando la autenticación se integra con PAM/SSSD y servicios centrales como LDAP, Kerberos o FreeIPA. El curso debe distinguir autenticación, autorización, certificados y pertenencia a grupos, así como estudiar dependencias, fallos y logs de cada capa.

### WireGuard
WireGuard no debe presentarse como consumidor directo de PAM, LDAP, Kerberos o FreeIPA. Su identidad nativa se basa en claves públicas de peers y cryptokey routing. IAM puede participar en un plano de control externo que autorice, aprovisione, retire o audite peers, pero no sustituye el mecanismo criptográfico nativo del túnel.

### Principio pedagógico
Cada tecnología se estudiará primero sin IAM para comprender su modelo nativo. Después se añadirá la integración centralizada cuando corresponda. Los laboratorios deben permitir comparar dependencia, disponibilidad, lifecycle, revocación, auditoría y troubleshooting en ambos modelos.

## Resultado esperado

Al finalizar, el estudiante debe ser capaz de diseñar, desplegar, asegurar, automatizar, observar, diagnosticar y mantener arquitecturas OpenVPN y WireGuard desde escenarios de acceso remoto sencillos hasta redes site-to-site, multi-site y de alta disponibilidad.
