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
- RFC 8945 — Secret Key Transaction Authentication for DNS (TSIG).
  Referencia vigente que sustituye RFC 2845 y RFC 4635.
- RFC 2845 — TSIG: lectura histórica, sustituida por RFC 8945.
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


## Referencias adicionales para las ampliaciones

- RFC 3645 — Generic Security Service Algorithm for Secret Key Transaction
  Authentication for DNS (GSS-TSIG): https://www.rfc-editor.org/info/rfc3645/
- RFC 4361 — Node-specific Client Identifiers for DHCPv4:
  https://www.rfc-editor.org/info/rfc4361/
- RFC 2308 — Negative Caching of DNS Queries (DNS NCACHE):
  https://www.rfc-editor.org/info/rfc2308/
- RFC 8945 — TSIG vigente: https://www.rfc-editor.org/info/rfc8945/

### Documentación oficial con enlaces

- Kea ARM, D2 y limitaciones de colas:
  https://kea.readthedocs.io/en/stable/arm/ddns.html
- Kea ARM, parámetros DDNS y conflictos DHCPv4:
  https://kea.readthedocs.io/en/stable/arm/dhcp4-srv.html
- Kea ARM, DHCPv6:
  https://kea.readthedocs.io/en/stable/arm/dhcp6-srv.html
- Kea ARM, hooks y GSS-TSIG:
  https://kea.readthedocs.io/en/stable/arm/hooks.html
- BIND 9 ARM:
  https://bind9.readthedocs.io/en/stable/
- Documentación de FreeIPA, para la ampliación opcional:
  https://www.freeipa.org/page/Documentation

Seleccionar secciones sobre permisos de actualización DNS y Kerberos cuando se
practique GSS-TSIG. La presencia de un hook en la documentación no garantiza
su empaquetado en la distribución instalada: verificarlo antes de diseñar el lab.

### Mapa de lectura

| Bloques | Referencia prioritaria |
|---|---|
| 0–4 | Kea D2, BIND ARM y RFC 2136 |
| 5 | RFC 8945, BIND ARM y diagnóstico TSIG |
| 6–8 | Kea ARM de D2, DHCPv4 y DHCPv6 de la versión usada |
| 9–12 | RFC 4701–4704, RFC 4361 y parámetros DDNS de Kea |
| 13–14 | Logging Kea/BIND y herramientas de captura |
| 15 | BIND update-policy; RFC 3645 y hooks para la ampliación IAM |
| 16–18 | Limitaciones D2, Kea HA y operación de zonas dinámicas BIND |

Los libros complementarios conservan valor conceptual, pero no deben usarse
para deducir opciones actuales de Kea, algoritmos TSIG o disponibilidad de hooks.
