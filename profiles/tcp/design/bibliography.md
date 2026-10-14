# Bibliografía — IP Addressing, Subnetting, VLSM e IPv6

## Organización por scope
Cada referencia tiene un scope principal y puede apoyar otros scopes. Los scopes delimitan contenidos, no implican duplicar libros. Las RFC y los registros IANA prevalecen para la interpretación normativa; los libros guían el aprendizaje y la práctica.

### S01 — Fundamentos de direccionamiento IP (bloques 0–2)
- Douglas E. Comer — *Internetworking with TCP/IP, Volume 1*. Principal: S01. Secundarios: S02, S05, S07.
- Kevin R. Fall; W. Richard Stevens — *TCP/IP Illustrated, Volume 1: The Protocols*. Principal: S01. Secundario: S08. Referencia contextual, sin duplicar el PATH TCP/IP.
- RFC 791 — Internet Protocol; RFC 950 — Internet Standard Subnetting Procedure (histórica).

### S02 — IPv4, máscaras y direcciones especiales (bloques 1–3)
- RFC 1918 — Address Allocation for Private Internets.
- RFC 3021 — Using 31-Bit Prefixes on IPv4 Point-to-Point Links.
- RFC 6890 — Special-Purpose IP Address Registries; IANA IPv4 Special-Purpose Address Registry.

### S03 — Subnetting y cálculo IPv4 (bloques 3–6)
- Rene Molenaar — *How to Master Subnetting*. Principal: S03. Secundario: S04.
- Paul Browning — *IP Subnetting: From Zero to Guru*. Principal: S03. Secundario: S04.
- Todd Lammle — *Subnetting* (título facilitado; edición por verificar). Principal: S03. Secundario: S04.

### S04 — CIDR, FLSM y VLSM (bloques 7–11)
- Paul Browning — *IP Subnetting: From Zero to Guru* (referencia cruzada a S03).
- Todd Lammle — *Subnetting* (referencia cruzada a S03).
- Rene Molenaar — *How to Master Subnetting* (referencia cruzada a S03).
- RFC 4632 — Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan.

### S05 — Supernetting y sumarización (bloques 7, 12, 20–21)
- RFC 4632 — CIDR (referencia cruzada a S04).
- RFC 1519 — Classless Inter-Domain Routing (CIDR): An Address Assignment and Aggregation Strategy (histórica).
- Douglas E. Comer — *Internetworking with TCP/IP, Volume 1* (referencia cruzada a S01).

### S06 — IPv6 y subnetting IPv6 (bloques 13–15)
- Silvia Hagen — *IPv6 Essentials*, 3rd edition. Principal: S06. Secundario: S07.
- RFC 4291 — IP Version 6 Addressing Architecture.
- RFC 5952 — A Recommendation for IPv6 Address Text Representation.
- RFC 6164 — Using 127-Bit IPv6 Prefixes on Inter-Router Links.
- RFC 8200 — Internet Protocol, Version 6 (IPv6) Specification.
- IANA IPv6 Special-Purpose Address Registry.

### S07 — Diseño profesional y dual-stack (bloques 11, 16, 20–21)
- Silvia Hagen — *IPv6 Essentials* (referencia cruzada a S06).
- RFC 6177 — IPv6 Address Assignment to End Sites.
- RFC 4632 — CIDR (referencia cruzada a S04).
- Referencias de S01 y S06 para fundamentos y jerarquías.

### S08 — Linux, verificación y troubleshooting (bloques 17, 19, 21)
- Linux manual pages: `ip(8)`, `ip-address(8)`, `ip-route(8)`, `ip-neighbour(8)`.
- NetworkManager y `nmcli`: documentación oficial.
- Kevin R. Fall; W. Richard Stevens — *TCP/IP Illustrated, Volume 1* (consulta contextual).

### S09 — Automatización e IPAM (bloques 18, 20–21)
- Python Standard Library — `ipaddress` (documentación oficial).
- Documentación oficial de las herramientas IPAM utilizadas en laboratorio (según implementación elegida).

### S10 — Normativa y registros (transversal)
- RFC 791, 950, 1519, 1918, 3021, 4291, 4632, 5952, 6164, 6177, 6890, 8200.
- IANA IPv4/IPv6 Special-Purpose Address Registries.

### Referencias complementarias fuera del scope central
- Cricket Liu — *DNS and BIND*: consulta puntual sobre registros A/AAAA y DNS inverso, sin impartir un curso DNS.
- Cricket Liu — *DNS and BIND on IPv6*: consulta puntual sobre DNS IPv6, sin impartir un curso DNS.

## Criterio pedagógico
1. Mostrar derivación matemática antes de técnicas rápidas.
2. Resolver ejemplos con cálculo manual y validación independiente.
3. Aplicar Molenaar, Browning y Lammle prioritariamente a subnetting IPv4; no presentarlos como bibliografía principal de diseño IPv6.
4. Emplear RFC e IANA para casos especiales y vigencia de asignaciones.
5. Separar claramente diseño de direccionamiento de la enseñanza integral de TCP, UDP, DNS, DHCP o routing.
