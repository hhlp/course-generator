# Bibliografía — OpenVPN + WireGuard

## Fuentes primarias

### OpenVPN
- OpenVPN Community Documentation.
- OpenVPN 2.x Manual Page.
- OpenVPN Community Resources.
- Easy-RSA Documentation.
- OpenVPN source code and project documentation.

### WireGuard
- WireGuard official documentation.
- WireGuard Quick Start.
- WireGuard protocol and cryptography documentation.
- WireGuard whitepaper: *WireGuard: Next Generation Kernel Network Tunnel* — Jason A. Donenfeld.
- WireGuard Linux kernel and wireguard-tools source code.

### Linux networking
- Linux kernel networking documentation.
- `iproute2` documentation and manual pages.
- `ip(8)`, `ip-route(8)`, `ip-rule(8)` and related manual pages.
- nftables documentation and Netfilter project documentation.
- firewalld documentation.
- NetworkManager documentation.
- systemd documentation and manual pages.
- SELinux documentation for Fedora/RHEL.

## Libros recomendados

### Networking
- *TCP/IP Illustrated, Volume 1: The Protocols, Second Edition* — Kevin R. Fall, W. Richard Stevens.
- *UNIX Network Programming, Volume 1: The Sockets Networking API, Third Edition* — W. Richard Stevens, Bill Fenner, Andrew M. Rudoff.
- *Linux Networking Cookbook* — Carla Schroder.
- *Understanding Linux Network Internals* — Christian Benvenuti.

### Seguridad y criptografía
- *Serious Cryptography, 2nd Edition* — Jean-Philippe Aumasson.
- *Cryptography Engineering* — Niels Ferguson, Bruce Schneier, Tadayoshi Kohno.
- *Real-World Cryptography* — David Wong.

### Linux
- *The Linux Programming Interface* — Michael Kerrisk.
- *How Linux Works* — Brian Ward.

### Automatización
- Documentación oficial de Ansible.
- Documentación oficial de Terraform/OpenTofu cuando el laboratorio utilice aprovisionamiento de infraestructura.

## RFC y especificaciones relevantes

Consultar las RFC originales cuando una lección profundice en IP, UDP, TCP, IPv6, Path MTU Discovery, CIDR, NAT, DNS, TLS u otros protocolos estandarizados.

No es necesario convertir el curso en una lectura secuencial de RFC. Deben utilizarse como referencia normativa para explicar comportamiento de protocolo y verificar detalles técnicos.

## Jerarquía de fuentes

Para contenido que pueda cambiar entre versiones, utilizar este orden:

1. Documentación oficial actual del proyecto.
2. Manuales instalados en Fedora/RHEL.
3. Documentación del kernel o distribución.
4. Especificaciones y RFC.
5. Código fuente cuando sea necesario estudiar internals.
6. Libros técnicos para explicación conceptual y contexto.

## Uso dentro de las lecciones

Cada lección debe terminar con referencias concretas relacionadas con el tema tratado. Las referencias no deben añadirse únicamente al final del curso.

Para comandos y opciones susceptibles de cambiar, contrastar con la versión vigente de la documentación antes de presentar la sintaxis como actual.

## Referencias adicionales organizadas por scope

### OpenVPN: versiones, TLS y DCO
- Manual oficial OpenVPN 2.x: opciones TLS, cifrados, autenticación, logging y compatibilidad.
- Documentación técnica oficial OpenVPN sobre Data Channel Offload (DCO), requisitos y limitaciones.
- Repositorio de código OpenVPN y componentes DCO para Linux.

### WireGuard: protocolo, identidad e internals
- Whitepaper de Jason A. Donenfeld, secciones sobre NoiseIK, mensajes, cookies y temporizadores.
- Documentación y código fuente de WireGuard en el kernel Linux.
- Manuales `wg(8)` y `wg-quick(8)` para distinguir configuración nativa y extensiones de integración.

### IAM y autenticación externa
- Documentación oficial de SSSD y FreeIPA (PAM, proveedores de identidad, caché y troubleshooting).
- Documentación de Linux-PAM y módulos de autenticación compatibles con OpenVPN.
- RFC 2865 (RADIUS) y documentación del servidor RADIUS elegido para laboratorios.
- Documentación de Easy-RSA y OpenSSL para revocación y ciclo de vida X.509.

### Networking, alta disponibilidad y routing
- Documentación oficial FRRouting para OSPF, BGP y pruebas de convergencia.
- Documentación de Keepalived/VRRP y limitaciones de failover de sesiones.
- Linux kernel docs: policy routing, netfilter/conntrack, rp_filter y network namespaces.
- RFC 1191, RFC 8201 y RFC 8899: Path MTU Discovery y datagram PLPMTUD.

### Observabilidad, automatización y operación
- Documentación de Prometheus: métricas, reglas de alertas y buenas prácticas.
- Documentación de Ansible y Molecule para validación de roles e idempotencia.
- Documentación systemd/journald, auditd, SELinux y herramientas de tracing del kernel.

## Aplicación de referencias por lección
Cada lección debe citar su referencia primaria concreta, la versión del software comprobada cuando corresponda y, en laboratorios, los manuales de comandos utilizados. Los libros existentes son referencias conceptuales, no sustitutos de la documentación técnica vigente.
