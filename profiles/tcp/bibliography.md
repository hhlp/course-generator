# Bibliography — TCP/IP 0 → experto

## Política bibliográfica

Las referencias se agrupan por **scope** (ámbito de aplicación), no por dificultad ni por orden de lectura. Una misma obra puede cubrir varios scopes. Las RFC vigentes y la documentación upstream tienen prioridad para detalles normativos y comportamiento actual; los libros clásicos se emplean para fundamentos y contexto. El diseño y planificación de redes IPv4/IPv6 (VLSM exhaustivo, planes de direccionamiento y topologías de diseño) pertenecen a un learning path independiente.

## Catálogo de libros (identificadores únicos)

- **B01** — W. Richard Stevens; Kevin R. Fall. *TCP/IP Illustrated, Volume 1: The Protocols*, 2nd ed.
- **B02** — James F. Kurose; Keith W. Ross. *Computer Networking: A Top-Down Approach*, 8th ed.
- **B03** — Andrew S. Tanenbaum; David J. Wetherall. *Computer Networks*, 6th ed.
- **B04** — Michael W. Lucas. *Networking for Systems Administrators*, 2nd ed.
- **B05** — Chris Sanders. *Practical Packet Analysis*, 3rd ed.
- **B06** — Laura Chappell. *Wireshark Network Analysis*, 2nd ed.
- **B07** — Gordon Lyon. *Nmap Network Scanning*.
- **B08** — Charles M. Kozierok. *The TCP/IP Guide: A Comprehensive, Illustrated Internet Protocols Reference*.
- **B09** — Joe Casad. *Sams Teach Yourself TCP/IP in 24 Hours* (consultar edición utilizada).
- **B10** — James Pyles; Jeffrey L. Carrell; Ed Tittel. *Guide to TCP/IP: IPv6 and IPv4* (consultar edición utilizada).

## Scopes y referencias

### S01 — Fundamentos, modelos OSI/TCP-IP y encapsulación
**Libros:** B09, B02, B03, B08, B01. **Bloques:** 0–1.

### S02 — Arquitectura y protocolos TCP/IP
**Libros:** B08, B01, B02, B03. **Bloques:** 0–12, 31–32.

### S03 — IPv4/IPv6 operativos, ARP/NDP, ICMP y routing
**Libros:** B10, B08, B01, B04. **Bloques:** 2–6, 31, 37–39. **Límite:** no sustituye el path independiente de diseño IPv4/IPv6.

### S04 — Linux networking, sockets y kernel
**Libros:** B04, B01. **Referencias:** documentación de iproute2 (`ip`, `ss`), Linux man-pages (`socket(2)`, `tcp(7)`, `udp(7)`, `ip(7)`, `ipv6(7)`, `packet(7)`), Linux kernel networking docs, documentación Fedora y RHEL. **Bloques:** 6–7, 13–18, 33–36.

### S05 — TCP, UDP, control de congestión y rendimiento
**Libros:** B01, B08. **Referencias:** RFC 9293, RFC 768 y documentación Linux actual. **Bloques:** 8–12, 31, 34–36.

### S06 — Captura, BPF, Wireshark/tshark y PCAP
**Libros:** B05, B06. **Referencias:** manuales tcpdump/libpcap, Wireshark User's Guide, Wireshark Display Filter Reference y manual tshark. **Bloques:** 19–26, 37–39.

### S07 — Nmap, descubrimiento y análisis de puertos
**Libros:** B07. **Referencias:** Nmap Reference Guide y documentación NSE. **Bloques:** 27–30, 37–39.

### S08 — RFC, estándares y especificaciones
**Referencias iniciales:** RFC 8200 (IPv6), RFC 9293 (TCP), RFC 768 (UDP), RFC 792 (ICMPv4), RFC 4443 (ICMPv6), RFC 826 (ARP), RFC 4861 (NDP), RFC 1918 (privadas), RFC 4632 (CIDR), RFC 1191 (PMTUD IPv4), RFC 8201 (PMTUD IPv6), RFC 6724 (selección de direcciones). Verificar actualizaciones, obsolescencia y erratas antes de enseñar detalles normativos. **Bloques:** transversales.

### S09 — Troubleshooting, observabilidad y laboratorios
**Libros:** B04, B05, B06, B01. **Referencias:** documentación kernel, Fedora/RHEL, tcpdump, tshark y Nmap. **Bloques:** 33–39.

## Matriz rápida: libro → scope → bloques

| Libro | Scopes | Bloques principales |
|---|---|---|
| B01 Stevens/Fall | S01 S02 S03 S04 S05 S09 | 0–12, 31–39 |
| B02 Kurose/Ross | S01 S02 | 0–12 |
| B03 Tanenbaum/Wetherall | S01 S02 | 0–6 |
| B04 Lucas | S03 S04 S09 | 2–7, 13–18, 33–39 |
| B05 Sanders | S06 S09 | 19–26, 37–39 |
| B06 Chappell | S06 S09 | 23–26, 37–39 |
| B07 Lyon | S07 | 27–30 |
| B08 Kozierok | S01 S02 S03 S05 | 0–12, 31–32 |
| B09 Casad | S01 | 0–9 |
| B10 Pyles/Carrell/Tittel | S03 | 2–6, 31, 37–39 |

## Criterio de selección por lección

Seleccionar primero el scope correspondiente al bloque; dentro de él, priorizar una referencia conceptual y una fuente técnica/normativa, cuando proceda. No atribuir contenido a un libro sin comprobar que su edición lo cubre. En CLI usar la documentación de la versión instalada y verificar ejemplos en laboratorio.
