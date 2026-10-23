# Bibliography — TCP/IP 0 → experto

## Política bibliográfica

Las referencias se agrupan por **scope** (ámbito de aplicación), no por dificultad ni por orden de lectura. Una misma obra puede cubrir varios scopes. Las RFC vigentes y la documentación upstream tienen prioridad para detalles normativos y comportamiento actual; los libros clásicos se emplean para fundamentos y contexto. El diseño y planificación de redes IPv4/IPv6 (VLSM exhaustivo, planes de direccionamiento y topologías de diseño) pertenecen a un learning path independiente.

## Catálogo de libros (identificadores únicos)

- **B01** — W. Richard Stevens; Kevin R. Fall. *TCP/IP Illustrated, Volume 1: The Protocols*, 2nd ed.
- **B02** — James F. Kurose; Keith W. Ross. *Computer Networking: A Top-Down Approach*, 8th ed.
- **B03** — Andrew S. Tanenbaum; Nick Feamster; David J. Wetherall. *Computer Networks*, 6th ed.
- **B04** — Michael W. Lucas. *Networking for Systems Administrators*, 2nd ed.
- **B05** — Chris Sanders. *Practical Packet Analysis*, 3rd ed.
- **B06** — Laura Chappell. *Wireshark Network Analysis*, 2nd ed.
- **B07** — Gordon Lyon. *Nmap Network Scanning*.
- **B08** — Charles M. Kozierok. *The TCP/IP Guide: A Comprehensive, Illustrated Internet Protocols Reference*.
- **B09** — Joe Casad. *Sams Teach Yourself TCP/IP in 24 Hours* (consultar edición utilizada).
- **B10** — James Pyles; Jeffrey L. Carrell; Ed Tittel. *Guide to TCP/IP: IPv6 and IPv4* (consultar edición utilizada).

## Scopes y referencias

### S01 — Fundamentos, modelos OSI/TCP-IP y encapsulación
**Libros:** B09, B02, B03, B08, B01. **Bloques:** 0–1; B09 también como introducción a 2–9.

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
| B01 Stevens/Fall | S01 S02 S03 S04 S05 S09 | 0–12, 31–32; apoyo conceptual 34–39 |
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


## Fuentes operativas para las ampliaciones
Se mantienen los scopes S01–S09; las fuentes siguientes complementan los libros.
No se presume que un libro clásico cubra comandos o algoritmos actuales.

| Scope | Fuente primaria | Uso y bloques |
|---|---|---|
| S01/S04 | NetworkManager y manual nmcli | Preparación y persistencia; 0, 6 |
| S02/S09 | Linux man-pages: nsswitch.conf, hosts, resolv.conf, getent; BIND dig | Resolución operativa; 7, 37–38 |
| S04 | proc_pid_net(5), network_namespaces(7), ss(8) | Namespaces, procesos y sockets; 15, 18, 33 |
| S04/S09 | Netfilter nftables, conntrack-tools y firewalld | Recorrido, reglas y evidencias; 32, 37–39 |
| S05 | Linux IP Sysctl y documentación TCP | Parámetros, colas y algoritmos; 12, 34–35 |
| S06 | Wireshark: TCP Analysis, Checksums, tshark; libpcap pcap-filter | Calidad y límites de captura; 19–26 |
| S07 | Nmap Reference Guide | Estados, IPv6 y razones; 27–30 |
| S09 | curl y OpenSSL s_client | Separar conexión, TLS y aplicación; 37–39 |

### Enlaces de consulta
- NetworkManager: https://networkmanager.dev/docs/api/latest/nmcli.html
- Resolución Linux: https://man7.org/linux/man-pages/man5/nsswitch.conf.5.html
- dig: https://bind9.readthedocs.io/en/latest/manpages.html#dig-dns-lookup-utility
- Namespace de /proc/PID/net: https://man7.org/linux/man-pages/man5/proc_pid_net.5.html
- Namespaces: https://man7.org/linux/man-pages/man7/network_namespaces.7.html
- ss: https://man7.org/linux/man-pages/man8/ss.8.html
- Kernel IP Sysctl: https://docs.kernel.org/networking/ip-sysctl.html
- nftables: https://wiki.nftables.org/
- firewalld: https://firewalld.org/documentation/
- conntrack-tools: https://conntrack-tools.netfilter.org/manual.html
- libpcap: https://www.tcpdump.org/manpages/pcap-filter.7.html
- Wireshark TCP Analysis: https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html
- Wireshark Checksums: https://www.wireshark.org/docs/wsug_html_chunked/ChAdvChecksums.html
- Nmap estados: https://nmap.org/book/man-port-scanning-basics.html
- curl: https://curl.se/docs/manpage.html
- OpenSSL: https://docs.openssl.org/master/man1/openssl-s_client/

## Control editorial
B03 incluye a Nick Feamster, coautor de la sexta edición, según Pearson:
https://www.pearson.com/en-us/subject-catalog/p/computer-networks/P200000003188
Las ediciones de los demás títulos se conservan como declaradas en el material
original; esta revisión no certifica todas sus fichas editoriales. Antes de
atribuir una sección a una obra, comprobar la edición realmente disponible.

## Estándares complementarios por contenido
Añadir a S08 RFC 1034/1035 (DNS), 2308 (caché negativa), 7766 (DNS sobre TCP),
8305 (Happy Eyeballs), 8981 (direcciones temporales IPv6), 6298 (RTO),
2018 (SACK), 8985 (RACK-TLP), 3168 (ECN), 8899 (DPLPMTUD), 9000 (QUIC) y
8446 (TLS 1.3), como puntos de partida. Comprobar actualizaciones, erratas y
estado vigente en RFC Editor antes de generar una lección normativa:
https://www.rfc-editor.org/
