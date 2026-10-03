# DHCP + DNS Integration — Learning Path 0 → Experto en profundidad

Ruta práctica para dominar la integración entre **Kea DHCP** y **BIND DNS**
mediante **Kea DHCP-DDNS (D2)**, **RFC 2136 Dynamic Update** y **TSIG**.

## Objetivo

No se limita a “hacer que DHCP registre nombres en DNS”. El objetivo es poder
explicar, construir y diagnosticar todo el recorrido:

```text
Cliente
  │
  │ DHCPv4 / DHCPv6
  ▼
Kea DHCP
  │
  │ Name Change Request (NCR)
  ▼
Kea DHCP-DDNS / D2
  │
  │ RFC 2136 + TSIG
  ▼
BIND authoritative DNS
  ├── A
  ├── AAAA
  └── PTR
```

También se estudia el recorrido de eliminación:

```text
lease release / expiration
          │
          ▼
        Kea
          │ REMOVE NCR
          ▼
         D2
          │ authenticated DNS UPDATE
          ▼
        BIND
          ├── elimina A / AAAA
          └── elimina PTR
```

## Plataforma

El laboratorio está orientado a **Fedora/RHEL** y contempla:

- paquetes y archivos de configuración;
- systemd;
- journald y logs explícitos;
- firewalld;
- SELinux;
- Kea DHCPv4/DHCPv6;
- Kea D2;
- BIND;
- `dig`, `nsupdate`, `rndc`, `tcpdump` y análisis con Wireshark.

## Filosofía

Los bloques anteriores de la infraestructura estudian DNS y DHCP de forma
independiente. Este PATH se concentra en la **integración**, por lo que repasa
solo los elementos necesarios antes de profundizar en el flujo DHCP-DDNS.

La ruta presta especial atención a:

1. instalación real;
2. configuración reproducible;
3. seguridad con TSIG;
4. A, AAAA y PTR;
5. DHCID y conflictos;
6. ciclo de vida lease ↔ DNS;
7. IPv4 e IPv6;
8. logging;
9. troubleshooting por capas;
10. operación y recuperación.

## Logging

No se asume que todos los componentes escriban necesariamente en un único
archivo bajo `/var/log`. Se aprende a distinguir entre:

```text
systemd service
      │
      ▼
journald
      │
      └── journalctl -u <unidad>

Kea / BIND
      │
      └── logging explícitamente configurado
              │
              └── archivo/destino definido por el administrador
```

El alumno aprenderá a localizar el destino real de los mensajes en su sistema,
seguirlos en tiempo real y correlacionar eventos entre DHCP, D2 y BIND.

## Troubleshooting

La metodología principal sigue el flujo real:

```text
Cliente
 ↓
¿obtuvo lease?
 ↓
¿hostname/FQDN correcto?
 ↓
¿Kea decidió hacer DDNS?
 ↓
¿se creó NCR?
 ↓
¿D2 recibió NCR?
 ↓
¿D2 encontró la zona?
 ↓
¿BIND es alcanzable?
 ↓
¿TSIG es válido?
 ↓
¿RFC 2136 fue aceptado?
 ↓
¿A/AAAA existe?
 ↓
¿PTR existe?
 ↓
¿DHCID/ownership es coherente?
```

Se practican errores como `REFUSED`, `NOTAUTH`, `NOTZONE`, `BADKEY`, `BADSIG`,
`BADTIME`, timeouts, zonas reverse incorrectas, PTR huérfanos, registros stale,
problemas de firewalld, permisos y SELinux.

## Laboratorio final

El proyecto final construye y rompe deliberadamente una infraestructura:

```text
                    DHCPv4 / DHCPv6
Cliente  ─────────────────────────────────► Kea
                                             │
                                             │ NCR
                                             ▼
                                           D2
                                             │
                                      RFC 2136 + TSIG
                                             │
                                             ▼
                                           BIND
                                        ┌────┴────┐
                                        │         │
                                      A/AAAA     PTR
```

Al terminar, el alumno debe poder demostrar una asignación de lease, creación
de registros forward/reverse, renovación, expiración/liberación, eliminación
de registros y diagnóstico basado en logs y capturas de tráfico.
