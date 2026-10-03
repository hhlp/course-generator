# DHCP — Learning Path 0 → Experto en profundidad

Ruta de aprendizaje orientada a la administración real de **DHCP en Fedora/RHEL**, utilizando **ISC Kea** como implementación principal.

## Objetivo

Al finalizar, el estudiante debe poder diseñar, instalar, configurar, operar, asegurar, observar y diagnosticar una infraestructura DHCP moderna, tanto IPv4 como IPv6.

La ruta no se limita a aprender una configuración funcional. Se estudia el protocolo, el comportamiento del cliente y servidor, las concesiones, relay, alta disponibilidad, logs y diagnóstico mediante captura de paquetes.

## Ejes de aprendizaje

- DHCPv4 y DORA en profundidad.
- DHCPv6, SLAAC, RA, Stateful/Stateless y Prefix Delegation.
- Arquitectura y configuración de ISC Kea.
- Instalación y operación en Fedora/RHEL.
- Subnets, pools, leases y reservations.
- DHCP options y opciones personalizadas.
- DHCP Relay, VLAN y Option 82.
- Kea High Availability.
- Backends, hooks, Control Agent y API.
- firewalld y SELinux.
- Logging con Kea, systemd/journald y archivos.
- tcpdump/Wireshark como herramientas centrales.
- Troubleshooting sistemático.
- Observabilidad, capacidad y diseño de producción.
- Laboratorio final con fallos deliberados.

## Logging: enfoque de la ruta

No se asume que Kea siempre escriba en un archivo fijo bajo `/var/log`.

Se aprende a descubrir la salida configurada y a trabajar con:

```bash
systemctl status kea-dhcp4
journalctl -u kea-dhcp4
journalctl -u kea-dhcp4 -f
```

así como logging explícito a archivo cuando se configure. También se estudian persistencia de journald, rotación, permisos y niveles de debug.

## Troubleshooting

El diagnóstico sigue una cadena reproducible:

```text
Cliente
  ↓
Interfaz / enlace
  ↓
VLAN
  ↓
Relay
  ↓
Routing
  ↓
Firewall / SELinux
  ↓
Kea
  ↓
Selección de subnet/pool
  ↓
Lease
  ↓
Options
```

Para DHCPv4 se aprende a localizar dónde se rompe:

```text
DHCPDISCOVER
      ↓
DHCPOFFER
      ↓
DHCPREQUEST
      ↓
DHCPACK
```

El objetivo es demostrar la causa mediante **logs + estado del sistema + captura de paquetes**, no simplemente reiniciar el servicio.

## Herramientas principales

```bash
dnf
rpm
systemctl
journalctl
ss
ip
nmcli
firewall-cmd
ausearch
tcpdump
tshark
Wireshark
jq
curl
dig
```

## Laboratorio recomendado

Como mínimo:

```text
client1 ─┐
         ├── LAN/VLAN ── relay/router ── kea1
client2 ─┘                              │
                                       └── kea2 (HA)
```

Se recomienda disponer además de IPv6 para practicar RA, DHCPv6 y Prefix Delegation.

## Relación con la ruta de infraestructura

```text
TIME / Chrony
      ↓
DNS / BIND
      ↓
DHCP / Kea
      ↓
DHCP + DNS
      ↓
DDNS
```

El bloque final introduce únicamente los conceptos necesarios para enlazar con el siguiente PATH de **DHCP + DNS Integration**, donde se estudiarán Kea DHCP-DDNS, BIND, actualizaciones forward/reverse y TSIG en profundidad.

## Resultado esperado

El estudiante debe ser capaz de recibir un incidente como «los equipos de VLAN 30 no obtienen dirección», construir una hipótesis, inspeccionar servicio/logs/red/relay, capturar paquetes, localizar el punto de fallo, corregirlo y documentar la causa raíz.
