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


## Referencias concretas para la revisión

Seleccionar el manual de OpenVPN que corresponda al binario instalado, no asumir
que un manual de otra versión describe todos sus valores predeterminados.

- [OpenVPN Community Docs y manuales por versión](https://openvpn.net/community-docs/).
- [OpenVPN 2.6: manual de referencia de esa rama](https://openvpn.net/community-docs/community-articles/openvpn-2-6-manual/).
  Revisar plugin, auth-user-pass, auth-gen-token, reneg-sec, management,
  crl-verify, compresión y DCO en el manual aplicable.
- [Código OpenVPN y plugin auth-pam](https://github.com/OpenVPN/openvpn/tree/master/src/plugins/auth-pam).
  Consultar también el código de la etiqueta correspondiente a la instalación.
- [Easy-RSA](https://easy-rsa.readthedocs.io/en/latest/).
- [WireGuard: modelo conceptual](https://www.wireguard.com/).
- [WireGuard: Quick Start](https://www.wireguard.com/quickstart/).
- [WireGuard: protocolo](https://www.wireguard.com/protocol/).
- [WireGuard: namespaces y routing](https://www.wireguard.com/netns/).
- [WireGuard: limitaciones conocidas](https://www.wireguard.com/known-limitations/).
- [wg(8), fuente del manual](https://git.zx2c4.com/wireguard-tools/tree/src/man/wg.8).
- [wg-quick(8), fuente del manual](https://git.zx2c4.com/wireguard-tools/tree/src/man/wg-quick.8).
- [NetworkManager: WireGuard](https://networkmanager.dev/docs/api/latest/settings-wireguard.html).
- [SSSD: documentación](https://sssd.io/docs/).
- [FreeIPA: documentación](https://www.freeipa.org/page/Documentation).
- [Linux-PAM: documentación](https://www.linux-pam.org/Linux-PAM-html/).
- [MIT Kerberos: administración](https://web.mit.edu/kerberos/krb5-latest/doc/admin/).
- [firewalld: documentación](https://firewalld.org/documentation/).
- [nftables: documentación del proyecto](https://wiki.nftables.org/).
- [FRRouting: documentación](https://docs.frrouting.org/en/latest/).
- [Kernel Linux: networking](https://docs.kernel.org/networking/).
- [systemd: journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html).
- [Ansible: documentación](https://docs.ansible.com/).

## Correspondencia temática

| Bloques | Referencias principales |
| --- | --- |
| 2–11, 32 | Manual OpenVPN de la versión instalada, Easy-RSA y auth-pam |
| 9A | OpenVPN auth/tokens, Linux-PAM, SSSD, FreeIPA y MIT Kerberos |
| 12–21, 33 | WireGuard, wg(8), wg-quick(8) y NetworkManager |
| 9B | Modelo WireGuard y documentación del controlador externo elegido |
| 7, 18, 24–25 | firewalld, nftables y documentación SELinux de la distribución |
| 22–23, 29 | NetworkManager, kernel, iproute2 y FRRouting |
| 26–30, 34–35 | systemd, Ansible y referencias del componente validado |

Para cada referencia de lección registrar sección y versión cuando proceda.
Los libros existentes se conservan como apoyo conceptual; las opciones actuales
se contrastan con documentación primaria y manuales instalados.
