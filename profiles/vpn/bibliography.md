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

### Identity & Access Management
- FreeIPA official documentation.
- SSSD official documentation and manual pages.
- Linux-PAM documentation and manual pages.
- MIT Kerberos documentation.
- OpenLDAP documentation.
- Fedora/RHEL documentation for identity management, SSSD, PAM and Kerberos integration.

Estas fuentes se utilizarán específicamente para la integración de OpenVPN como consumidor de identidad central. Para WireGuard se usarán para estudiar el plano de control/provisioning externo, dejando claro que WireGuard no consume directamente PAM, LDAP, Kerberos o FreeIPA para autenticar peers.

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
