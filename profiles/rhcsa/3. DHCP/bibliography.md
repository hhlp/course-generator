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

### RFC 9915 — Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
Referencia normativa principal; sustituye a RFC 8415. IA_TA es histórico.

### RFC 8415 — referencia histórica
Para interpretar documentación y sistemas anteriores; no es la referencia principal.

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

## Enlaces oficiales y uso por bloques — revisión 2026-10-23

Fijar en cada laboratorio el ARM de la versión instalada. Los enlaces stable
pueden apuntar a otra versión en el futuro. Las RFC describen el protocolo,
no garantizan que una implementación soporte cada función.

| Fuente | Aplicación |
|---|---|
| [Kea ARM](https://kea.readthedocs.io/en/stable/) | Índice y selección de versión para toda la ruta |
| [DHCPv4](https://kea.readthedocs.io/en/stable/arm/dhcp4-srv.html) | Bloques 3–9: configuración, reservas y selección |
| [DHCPv6](https://kea.readthedocs.io/en/stable/arm/dhcp6-srv.html) | Bloques 2 y 6: configuración y límites de implementación |
| [Administración de bases de datos](https://kea.readthedocs.io/en/stable/arm/admin.html) | Bloques 9 y 18: esquemas y herramientas de migración |
| [Clasificación](https://kea.readthedocs.io/en/stable/arm/classify.html) | Bloque 25: clases, expresiones y evaluación |
| [Hooks](https://kea.readthedocs.io/en/stable/arm/hooks.html) | HA, backends y dependencias de bibliotecas |
| [Migración de Control Agent](https://kb.isc.org/docs/kea-control-agent-migration) | Bloques 3 y 19: API directa y compatibilidad |
| [API y sockets](https://kb.isc.org/docs/kea-api-sockets) | Listeners, sockets y administración por daemon |
| [Cambios de Kea 3.2](https://kb.isc.org/docs/things-to-be-aware-of-when-upgrading-to-kea-3-2) | Retirada de Control Agent y migración |
| [Repositorio oficial de Kea](https://gitlab.isc.org/isc-projects/kea) | Código, pruebas, herramientas y documentación de la misma versión |

Para LFC, catálogo de mensajes, estadísticas, API y perfdhcp utilizar las
secciones correspondientes del índice ARM y las páginas man instaladas:
kea-lfc, kea-admin, kea-dhcp4, kea-dhcp6 y perfdhcp. Verificar opciones antes de
copiar comandos de otra versión.

## Referencias normativas concretas

- [RFC 2131](https://www.rfc-editor.org/rfc/rfc2131): DHCPv4 y estados.
- [RFC 2132](https://www.rfc-editor.org/rfc/rfc2132): opciones DHCPv4.
- [RFC 9915](https://www.rfc-editor.org/rfc/rfc9915): DHCPv6 vigente.
- [RFC 8415](https://www.rfc-editor.org/rfc/rfc8415): antecedente histórico.
- [RFC 3046](https://www.rfc-editor.org/rfc/rfc3046): Option 82.
- [RFC 6221](https://www.rfc-editor.org/rfc/rfc6221): relay ligero DHCPv6.
- [RFC 4861](https://www.rfc-editor.org/rfc/rfc4861): Neighbor Discovery y RA.
- [RFC 4862](https://www.rfc-editor.org/rfc/rfc4862): SLAAC.
- [RFC 8106](https://www.rfc-editor.org/rfc/rfc8106): DNS mediante RA.
- [RFC 4702](https://www.rfc-editor.org/rfc/rfc4702): Client FQDN DHCPv4; puente DDNS.
- [RFC 4704](https://www.rfc-editor.org/rfc/rfc4704): Client FQDN DHCPv6; puente DDNS.
- [RFC 8945](https://www.rfc-editor.org/rfc/rfc8945): TSIG; desarrollo en DHCP + DNS.

## Operación Linux y análisis de paquetes

- [Fedora Documentation](https://docs.fedoraproject.org/): plataforma y redes.
- [RHEL Documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux): elegir versión instalada.
- [NetworkManager](https://networkmanager.dev/docs/): cliente DHCP y configuración.
- [systemd manuals](https://www.freedesktop.org/software/systemd/man/latest/): unidades y journal; contrastar con man local.
- [firewalld](https://firewalld.org/documentation/): zonas, servicios y reglas.
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/): captura y análisis.
- [tcpdump manuals](https://www.tcpdump.org/manpages/): filtros y capturas.
- [PostgreSQL Documentation](https://www.postgresql.org/docs/): servicio SQL, backup y recuperación; escoger versión.

El bloque SQL enseña la operación necesaria para Kea; la administración profunda
del motor pertenece a su PATH. La integración completa D2/BIND/TSIG y el ciclo
lease–DNS pertenecen al PATH DHCP + DNS.
