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

## Catálogo de referencias concretas por bloque

Usar el manual correspondiente a la versión instalada. Los enlaces a documentación continua pueden cambiar; registrar en cada lección la versión y fecha consultadas. Las entradas anteriores de libros sirven de apoyo conceptual: verificar la edición de la copia utilizada antes de asignar capítulos, sin inventar paginación.

| Bloques | Fuente primaria | Aplicación |
| --- | --- | --- |
| 2–11, 24, 32, 34, 36 | [OpenVPN Community Docs](https://openvpn.net/community-docs/) | Elegir manual y notas de versión. |
| 2–11, 32, 34 | [Manual OpenVPN 2.6](https://openvpn.net/community-docs/community-articles/openvpn-2-6-manual.html) | Opciones y compatibilidad si se utiliza 2.6. |
| 2–11, 32, 34 | [Manual OpenVPN 2.7](https://openvpn.net/community-docs/community-articles/openvpn-2-7-manual.html) | Contrastar diferencias si se utiliza 2.7; no asumir disponibilidad. |
| 3, 24 | [Easy-RSA](https://easy-rsa.readthedocs.io/en/latest/) | CA, emisión y revocación. |
| 1, 3, 5 | [OpenSSL Docs](https://docs.openssl.org/) | Seleccionar versión, x509, verify, ca y proveedores. |
| 12–21, 33, 35 | [WireGuard Quick Start](https://www.wireguard.com/quickstart/) | Puesta en marcha y keepalive. |
| 13, 33, 36 | [WireGuard Protocol & Cryptography](https://www.wireguard.com/protocol/) | Mensajes y temporizadores. |
| 13, 33, 36 | [Whitepaper WireGuard](https://www.wireguard.com/papers/wireguard.pdf) | Diseño y modelo de seguridad. |
| 14–21, 35 | [wg(8), fuente oficial](https://git.zx2c4.com/wireguard-tools/tree/src/man/wg.8) | Consultas, cambios de peers y salida con secretos. |
| 14–22 | [wg-quick(8), fuente oficial](https://git.zx2c4.com/wireguard-tools/tree/src/man/wg-quick.8) | SaveConfig, strip, rutas, DNS y hooks. |
| 20, 33 | [Network namespaces de WireGuard](https://www.wireguard.com/netns/) | Namespace de interfaz y socket UDP. |
| 0, 6–7, 16–18, 29 | [Linux IP sysctl](https://docs.kernel.org/networking/ip-sysctl.html) | Forwarding, rp_filter y accept_ra. |
| 7, 18 | [firewalld Docs](https://firewalld.org/documentation/) | Zonas, policies y persistencia. |
| 7, 18, 29 | [nftables Wiki](https://wiki.nftables.org/) | Chains, hooks, conntrack y marks. |
| 8, 19, 22 | [NetworkManager Reference](https://networkmanager.dev/docs/api/latest/) | Perfiles VPN/WireGuard, rutas y DNS. |
| 10–11, 21, 26 | [journald.conf](https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html) | Storage, límites y retención. |
| 10–11, 21, 26 | [journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) | Consultas por unidad, boot y tiempo. |
| 22 | [systemd-resolved](https://www.freedesktop.org/software/systemd/man/latest/systemd-resolved.service.html) | Resolver y routing DNS. |
| 9, 34 | [Linux-PAM](https://www.linux-pam.org/) | Pila de autenticación y módulos. |
| 9, 34 | [SSSD Docs](https://sssd.io/docs/) | PAM, proveedores y caché. |
| 34 | [FreeIPA Docs](https://www.freeipa.org/page/Documentation) | Identidad central y políticas. |
| 34 | [RFC 2865](https://www.rfc-editor.org/rfc/rfc2865) | Base RADIUS; complementar con documentación del servidor y transporte elegidos. |
| 23 | [RFC 1191](https://www.rfc-editor.org/rfc/rfc1191), [RFC 8201](https://www.rfc-editor.org/rfc/rfc8201), [RFC 8899](https://www.rfc-editor.org/rfc/rfc8899) | PMTUD IPv4/IPv6 y datagram PLPMTUD. |
| 26, 37 | [Prometheus Docs](https://prometheus.io/docs/introduction/overview/) | Métricas y alertas. |
| 27 | [Ansible Docs](https://docs.ansible.com/), [Molecule](https://ansible.readthedocs.io/projects/molecule/) | Automatización y validación. |
| 29 | [FRRouting Docs](https://docs.frrouting.org/en/latest/) | OSPF/BGP, filtrado y convergencia. |
| 30 | [Keepalived Docs](https://www.keepalived.org/documentation.html) | VRRP; no confundir con replicación de sesiones VPN. |

Para Fedora/RHEL, complementar con los manuales instalados y la documentación oficial de la versión concreta de la distribución, especialmente para paquetes, repositorios, políticas criptográficas, SELinux y unidades systemd. No asumir que Fedora y RHEL ofrecen las mismas versiones o componentes.
