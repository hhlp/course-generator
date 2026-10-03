# Bibliografía — DNS + BIND 9

## Bibliografía principal

### DNS and BIND
Cricket Liu y Paul Albitz. *DNS and BIND*. O'Reilly Media.

Referencia clásica para comprender DNS, resolución, zonas, delegación, servidores authoritative/recursive y administración de BIND. Debe utilizarse junto con documentación moderna de BIND porque algunas ediciones describen prácticas o versiones históricas.

### Pro DNS and BIND
Ron Aitchison. *Pro DNS and BIND*. Apress.

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
- RFC 2845 — Secret Key Transaction Authentication for DNS (TSIG)
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
