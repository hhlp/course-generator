# Bibliografía — DHCP + DNS Integration

## Documentación principal

### ISC Kea

La documentación oficial de **ISC Kea** debe ser la referencia principal para:

- Kea DHCPv4 y DHCPv6;
- DHCP-DDNS;
- Kea D2;
- Name Change Requests;
- parámetros DDNS;
- DHCID y conflict resolution;
- logging;
- HA;
- Control Agent y operación.

Referencia: *Kea Administrator Reference Manual*, Internet Systems Consortium.

### BIND 9

La documentación oficial de **BIND 9** será la referencia principal para:

- configuración de zonas autoritativas;
- Dynamic Update;
- `update-policy`;
- TSIG;
- logging;
- `rndc`;
- administración de zonas dinámicas;
- troubleshooting.

Referencia: *BIND 9 Administrator Reference Manual*, Internet Systems Consortium.

## RFC fundamentales

- RFC 2136 — Dynamic Updates in the Domain Name System (DNS UPDATE).
- RFC 2845 — Secret Key Transaction Authentication for DNS (TSIG).
- RFC 4701 — A DNS Resource Record (RR) for Encoding Dynamic Host Configuration Protocol (DHCP) Information (DHCID RR).
- RFC 4702 — The DHCP Client FQDN Option.
- RFC 4703 — Resolution of FQDN Conflicts among DHCP Clients.
- RFC 4704 — The DHCPv6 Client FQDN Option.
- RFC 3007 — Secure Domain Name System (DNS) Dynamic Update.
- RFC 1034 — Domain Names — Concepts and Facilities.
- RFC 1035 — Domain Names — Implementation and Specification.

## Documentación de plataforma

### Red Hat / Fedora

Consultar la documentación vigente de Fedora y Red Hat Enterprise Linux para:

- instalación y gestión de BIND;
- systemd;
- journald;
- firewalld;
- SELinux;
- administración de red;
- Chrony y sincronización temporal.

Las rutas de archivos, nombres exactos de paquetes, unidades systemd y
políticas SELinux pueden variar entre versiones; deben verificarse en la
plataforma usada durante el laboratorio.

## Herramientas de referencia

Documentación/man pages de:

- `dig`
- `nsupdate`
- `rndc`
- `named-checkconf`
- `named-checkzone`
- `journalctl`
- `systemctl`
- `tcpdump`
- `ss`
- `firewall-cmd`
- herramientas de Kea disponibles en la versión instalada

## Lectura complementaria

- Cricket Liu & Paul Albitz — *DNS and BIND*.
- Ron Aitchison — *Pro DNS and BIND*.
- documentación de Wireshark sobre DNS/DHCP para análisis de protocolos.

## Criterio de uso

La bibliografía no sustituye la observación del sistema real. Cada lección
práctica debe contrastar documentación con:

```text
configuración
   +
estado systemd
   +
journald/logs
   +
estado DHCP
   +
dig/nsupdate/rndc
   +
captura de red cuando sea necesaria
```

Para opciones de Kea/BIND que puedan cambiar entre versiones, prevalece la
documentación oficial correspondiente a la versión instalada.
