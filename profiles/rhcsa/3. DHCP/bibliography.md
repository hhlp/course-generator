# Bibliografía — DHCP 0 → Experto en profundidad

## Documentación principal

### ISC Kea Administrator Reference Manual
Fuente técnica principal para la implementación del curso.

Áreas:
- Kea DHCPv4 y DHCPv6
- configuración
- host reservations
- options
- lease storage
- hooks
- High Availability
- Control Agent
- logging
- estadísticas
- troubleshooting operativo

### RFC 2131 — Dynamic Host Configuration Protocol
Referencia fundamental para DHCPv4.

### RFC 2132 — DHCP Options and BOOTP Vendor Extensions
Referencia para opciones DHCPv4.

### RFC 8415 — Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
Referencia moderna principal para DHCPv6.

### RFC 3046 — DHCP Relay Agent Information Option
Base para Option 82.

### RFC 6221 — Lightweight DHCPv6 Relay Agent
Referencia complementaria para relay DHCPv6.

## IPv6 relacionado

Estudiar conjuntamente la documentación/RFC correspondiente a:
- IPv6 Neighbor Discovery
- Router Advertisement
- SLAAC
- DHCPv6
- Prefix Delegation

El objetivo es comprender claramente qué responsabilidad pertenece a RA/SLAAC y cuál pertenece a DHCPv6.

## Fedora / RHEL

Usar la documentación vigente de:
- Fedora
- Red Hat Enterprise Linux
- systemd
- journald
- firewalld
- SELinux
- NetworkManager

para instalación, servicios, networking, logging, seguridad y troubleshooting.

## Herramientas

Documentación oficial y páginas man de:
- systemctl
- journalctl
- ss
- ip
- nmcli
- firewall-cmd
- ausearch
- tcpdump
- tshark
- Wireshark
- jq
- curl
- dig

## Orden de consulta recomendado

1. RFC para comprender el protocolo.
2. Kea ARM para comprender la implementación.
3. Fedora/RHEL para integración con el sistema operativo.
4. systemd/journald/firewalld/SELinux para operación.
5. tcpdump/Wireshark para demostrar el comportamiento real en la red.

## Principio de estudio

La bibliografía sirve como soporte, pero la ruta está diseñada para ir más allá de una lectura lineal de manuales. Cada concepto importante debe verificarse mediante configuración, logs, estado del sistema y tráfico real.
