# Bibliografía — DNS + BIND 9

## Bibliografía principal

### DNS and BIND
Cricket Liu y Paul Albitz. *DNS and BIND*, 5.ª edición. O'Reilly Media, 2006.

[Ficha editorial](https://www.oreilly.com/library/view/dns-and-bind/0596100574/).

Referencia clásica para comprender DNS, resolución, zonas, delegación, servidores authoritative/recursive y administración de BIND. Debe utilizarse junto con documentación moderna de BIND porque algunas ediciones describen prácticas o versiones históricas.

### Pro DNS and BIND
Ron Aitchison. *Pro DNS and BIND*, 1.ª edición. Apress, 2005.

[Ficha editorial](https://link.springer.com/book/10.1007/978-1-4302-0050-5).
No confundir con *Pro DNS and BIND 10* (2011); las opciones históricas
deben contrastarse con el ARM de BIND 9 instalado.

Útil para profundizar en diseño, operación, seguridad y configuración de BIND.

## Documentación técnica principal

### BIND 9 Administrator Reference Manual
Internet Systems Consortium (ISC).

Fuente principal para sintaxis y comportamiento actual de BIND 9: `named.conf`, DNSSEC, `dnssec-policy`, logging, ACL, views, RPZ, DDNS, estadísticas, herramientas y operación.

### Red Hat Enterprise Linux Documentation
Documentación de Red Hat relacionada con networking, DNS/BIND, SELinux, firewalld, systemd y NetworkManager.

### Fedora Documentation
Documentación de Fedora para administración de red, paquetes, systemd, SELinux y firewalld.

## RFC fundamentales

### DNS básico
- RFC 1034 — Domain Names: Concepts and Facilities
- RFC 1035 — Domain Names: Implementation and Specification

### Transferencias, actualización y operación
- RFC 1996 — A Mechanism for Prompt Notification of Zone Changes (DNS NOTIFY)
- RFC 2136 — Dynamic Updates in the Domain Name System (DNS UPDATE)
- RFC 2181 — Clarifications to the DNS Specification
- RFC 2308 — Negative Caching of DNS Queries
- RFC 2317 — Classless IN-ADDR.ARPA Delegation
- RFC 8945 — Secret Key Transaction Authentication for DNS (TSIG), referencia actual.
- RFC 2845 — TSIG, referencia histórica sustituida por RFC 8945.
- RFC 5936 — DNS Zone Transfer Protocol (AXFR)
- RFC 6891 — Extension Mechanisms for DNS (EDNS(0))

### DNSSEC
- RFC 4033 — DNS Security Introduction and Requirements
- RFC 4034 — Resource Records for the DNS Security Extensions
- RFC 4035 — Protocol Modifications for the DNS Security Extensions
- RFC 5155 — DNS Security (DNSSEC) Hashed Authenticated Denial of Existence
- RFC 6781 — DNSSEC Operational Practices
- RFC 7344 — Automating DNSSEC Delegation Trust Maintenance
- RFC 8078 — Managing DS Records from the Parent via CDS/CDNSKEY

### Privacidad y transporte moderno
- RFC 7858 — Specification for DNS over Transport Layer Security (TLS)
- RFC 8484 — DNS Queries over HTTPS (DoH)
- RFC 9250 — DNS over Dedicated QUIC Connections

### Seguridad y robustez
- RFC 5452 — Measures for Making DNS More Resilient against Forged Answers
- RFC 7873 — Domain Name System (DNS) Cookies
- RFC 8198 — Aggressive Use of DNSSEC-Validated Cache
- RFC 9156 — DNS Query Name Minimisation to Improve Privacy

## Herramientas y documentación que deben consultarse durante el curso

- `man named`
- `man named.conf`
- `man rndc`
- `man rndc.conf`
- `man dig`
- `man delv`
- `man nsupdate`
- `man named-checkconf`
- `man named-checkzone`
- `man resolv.conf`
- `man nsswitch.conf`
- `man NetworkManager.conf`
- `man firewalld`
- documentación y páginas de manual instaladas por los paquetes de la distribución

## Fuentes para bloques integrados

### SELinux
Documentación de Red Hat/Fedora sobre SELinux, tipos de BIND/named, `semanage`, `restorecon`, auditoría AVC y políticas aplicables.

### firewalld
Documentación oficial de firewalld y documentación Fedora/RHEL.

### systemd / journald
Páginas de manual y documentación de systemd para unidades, servicio `named` y journal.

### Kea
ISC Kea Administrator Reference Manual, especialmente DHCP-DDNS (D2), actualización forward/reverse y autenticación de actualizaciones.

### FreeIPA / IdM y relación DNS-IAM
Documentación de FreeIPA/IdM para DNS integrado y DNS externo, registros SRV, descubrimiento de servicios Kerberos/LDAP, zonas forward/reverse y actualizaciones dinámicas.

Debe utilizarse para distinguir dos arquitecturas: DNS independiente de IAM y DNS como infraestructura/dependencia de IAM. BIND no debe tratarse por ello como consumidor normal de identidades humanas.

### Kerberos y GSS-TSIG
Documentación técnica de Kerberos/FreeIPA/BIND aplicable al descubrimiento mediante DNS y a la autenticación de actualizaciones DNS mediante mecanismos GSS cuando corresponda. Debe diferenciarse de TSIG y de la autenticación interactiva de usuarios.

### Observabilidad
Documentación de BIND 9 sobre statistics channels y métricas; documentación de Prometheus/Grafana y del exporter seleccionado en el laboratorio.

## Criterio de uso

Los libros aportan explicación conceptual y progresión pedagógica. Para opciones concretas, defaults, sintaxis, algoritmos disponibles, características DNSSEC y comportamiento dependiente de versión, prevalece la documentación oficial correspondiente a la versión de BIND instalada.

Los RFC se incorporan progresivamente: primero como referencia y, en los bloques de internals y nivel experto, como material de lectura técnica directa.


## Fuentes verificables para la ampliación

Documentación oficial consultada para esta revisión: 23 de octubre de 2026.
Elegir en el ARM la rama que corresponda al paquete instalado y registrar la versión;
los enlaces estables pueden cambiar de contenido con nuevas versiones.

| Fuente | Uso en el curso |
|---|---|
| [BIND 9 ARM](https://bind9.readthedocs.io/en/stable/) | Configuración, DNSSEC, TSIG, dnstap, EDE y operación según versión |
| [Referencia BIND](https://bind9.readthedocs.io/en/stable/reference.html) | Directivas, soporte DoT/DoH, logging y estadísticas |
| [RFC 8945](https://www.rfc-editor.org/info/rfc8945/) | TSIG; sustituye RFC 2845 y 4635 |
| [RFC 3645](https://www.rfc-editor.org/info/rfc3645/) | GSS-TSIG |
| [RFC 1982](https://www.rfc-editor.org/info/rfc1982/) | Aritmética del serial |
| [RFC 8914](https://www.rfc-editor.org/info/rfc8914/) | Extended DNS Errors |
| [Chrony](https://chrony-project.org/documentation.html) | Diagnóstico temporal y configuración según versión |
| [Instalación IdM en RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-server-installation) | Requisitos de hostname, DNS y tiempo; consultar la versión RHEL usada |
| [FreeIPA](https://www.freeipa.org/page/Documentation) | DNS integrado/externo, registros y administración |
| [Kea ARM](https://kea.readthedocs.io/en/stable/arm/) | D2, TSIG, actualizaciones y conflictos |
| [Fedora Docs](https://docs.fedoraproject.org/) | Paquetes, red y administración |
| [RHEL Docs](https://docs.redhat.com/) | BIND, IdM, SELinux y firewalld de la versión elegida |

### Lectura por etapa

- Bloques 0–11: libros para conceptos; RFC 1034/1035 y ARM para contrastar protocolo/configuración.
- Bloques 12–18: ARM, RFC 1982, 2136, 8945 y RFC DNSSEC de la lista principal.
- Bloques 19–30: ARM para dnstap, EDE, logging, observabilidad y operaciones.
- Bloques 31–34: FreeIPA/IdM, Chrony, Kea y RFC 3645 para integración.
- Bloques 35–37: lectura directa de RFC, release notes y diseños con evidencias.
