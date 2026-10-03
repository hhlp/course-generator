# Bibliografía — IP Addressing, Subnetting, VLSM e IPv6

## Referencias fundamentales
- RFC 791 — Internet Protocol.
- RFC 950 — Internet Standard Subnetting Procedure.
- RFC 1519 — Classless Inter-Domain Routing (CIDR): an Address Assignment and Aggregation Strategy (histórico).
- RFC 1918 — Address Allocation for Private Internets.
- RFC 3021 — Using 31-Bit Prefixes on IPv4 Point-to-Point Links.
- RFC 4291 — IP Version 6 Addressing Architecture.
- RFC 4632 — Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan.
- RFC 6164 — Using 127-Bit IPv6 Prefixes on Inter-Router Links.
- RFC 6890 — Special-Purpose IP Address Registries.
- RFC 8200 — Internet Protocol, Version 6 (IPv6) Specification.

## Libros
- Douglas E. Comer — *Internetworking with TCP/IP, Volume 1*.
- Kevin R. Fall, W. Richard Stevens — *TCP/IP Illustrated, Volume 1: The Protocols*.
- Silvia Hagen — *IPv6 Essentials*.
- Cricket Liu — *DNS and BIND* (como referencia complementaria para A/AAAA y reverse DNS).

## Documentación práctica
- Linux `ip-address(8)`, `ip-route(8)`, `ip-neighbour(8)` e `ip(8)`.
- NetworkManager / `nmcli` documentation.
- Python Standard Library — `ipaddress`.
- IANA IPv4 Special-Purpose Address Registry.
- IANA IPv6 Special-Purpose Address Registry.

## Criterio de uso
Las RFC y registros IANA son la referencia normativa para rangos, semántica y casos especiales. Los libros sirven para explicación conceptual y progresión pedagógica; la documentación Linux/Python se utiliza en laboratorios y automatización.
