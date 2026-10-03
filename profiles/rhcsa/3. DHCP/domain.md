# Domain — DHCP 0 → Experto en profundidad

## Dominio principal

Administración, diseño, operación y troubleshooting de servicios **DHCP en sistemas Fedora/RHEL**, utilizando **ISC Kea** como implementación principal y estudiando DHCPv4 y DHCPv6 desde el protocolo hasta escenarios de producción.

## Alcance

La ruta cubre DHCP como servicio de infraestructura completo, no únicamente la sintaxis de configuración de un servidor.

El dominio incluye:

- fundamentos y arquitectura DHCP;
- DHCPv4;
- DHCPv6;
- SLAAC y Router Advertisement en su relación con DHCPv6;
- ISC Kea;
- instalación y operación en Fedora/RHEL;
- subnets y address pools;
- leases;
- host reservations;
- DHCP options;
- DHCP relay;
- Option 82;
- Kea High Availability;
- backends;
- hooks;
- Control Agent y API;
- systemd;
- journald;
- firewalld;
- SELinux;
- logging;
- observabilidad;
- seguridad;
- packet capture;
- troubleshooting;
- diseño de producción;
- recuperación ante fallos.

## Implementación de referencia

La implementación principal es:

```text
ISC Kea
├── kea-dhcp4
├── kea-dhcp6
├── Control Agent
├── hooks
├── lease backends
├── host reservations
└── High Availability
```

ISC DHCP puede aparecer como contexto histórico o comparativo, pero no constituye el servidor principal del PATH.

## Plataforma

Plataformas principales:

```text
Fedora
RHEL
```

La enseñanza debe integrar DHCP con las herramientas normales de administración del sistema:

```text
DNF / RPM
systemd
journald
NetworkManager
firewalld
SELinux
iproute2
tcpdump
Wireshark/tshark
```

## DHCPv4

Debe estudiarse el protocolo suficientemente profundo como para interpretar tráfico real.

Incluye:

```text
DHCPDISCOVER
DHCPOFFER
DHCPREQUEST
DHCPACK
DHCPNAK
DHCPDECLINE
DHCPRELEASE
DHCPINFORM
```

El estudiante debe comprender:

- DORA;
- transaction ID;
- direcciones ciaddr, yiaddr, siaddr y giaddr;
- client identifiers;
- lease lifetime;
- T1;
- T2;
- renewal;
- rebinding;
- expiración;
- selección de servidor;
- estados del cliente.

## DHCPv6

DHCPv6 se trata como protocolo propio y no como simple traducción de DHCPv4.

Debe incluir:

- SOLICIT;
- ADVERTISE;
- REQUEST;
- REPLY;
- RENEW;
- REBIND;
- RELEASE;
- DECLINE;
- INFORMATION-REQUEST;
- DUID;
- IAID;
- IA_NA;
- IA_TA;
- IA_PD;
- Prefix Delegation;
- preferred lifetime;
- valid lifetime.

También debe explicarse claramente la relación:

```text
IPv6
├── Neighbor Discovery
├── Router Advertisement
├── SLAAC
└── DHCPv6
    ├── Stateless
    └── Stateful
```

## Configuración y asignación

El estudiante debe dominar:

- subnet4;
- subnet6;
- pools;
- múltiples pools;
- múltiples subnets;
- shared networks;
- selección de subnet;
- lease allocation;
- expiración y reclamación de leases;
- agotamiento de pools.

## Reservations

Debe cubrir reservas basadas en identificadores apropiados para IPv4 e IPv6:

- MAC;
- client-id;
- DUID;
- flex-id cuando corresponda;
- direcciones reservadas;
- hostname;
- opciones específicas por host;
- reservas por subnet;
- reservas globales.

El troubleshooting debe distinguir especialmente entre MAC, client-id y DUID.

## DHCP Options

Debe enseñarse tanto el uso de opciones estándar como la creación de opciones personalizadas.

Ejemplos:

- router/default gateway;
- DNS servers;
- domain-name;
- domain-search;
- NTP;
- PXE/TFTP;
- boot server;
- boot file;
- vendor options;
- custom options;
- DHCPv6 options.

Debe estudiarse la precedencia de opciones entre niveles global, subnet, pool y host.

## DHCP Relay

El dominio incluye redes donde cliente y servidor no comparten segmento.

Debe cubrir:

```text
Client
   ↓
VLAN/Subnet
   ↓
DHCP Relay
   ↓
Router
   ↓
Kea Server
```

Conceptos principales:

- giaddr;
- selección de subnet;
- Option 82;
- Circuit ID;
- Remote ID;
- DHCPv6 Relay;
- RELAY-FORW;
- RELAY-REPL;
- routing;
- firewall;
- diagnóstico mediante capturas en múltiples puntos.

## High Availability

Kea HA debe estudiarse operativamente.

Incluye:

- HA hook;
- peers;
- hot-standby;
- load-balancing;
- heartbeat;
- lease synchronization;
- estados HA;
- partner-down;
- communication interrupted;
- failover;
- recuperación;
- network partition;
- split brain;
- resincronización.

Los laboratorios deben provocar fallos reales y observar el comportamiento del sistema.

## Logging

Logging es una parte obligatoria del dominio.

Debe cubrir:

- loggers de Kea;
- output options;
- severity;
- debuglevel;
- stdout/stderr;
- archivos;
- systemd/journald;
- persistencia;
- rotación;
- permisos;
- correlación de eventos.

No debe asumirse una ruta fija como `/var/log/kea`.

El estudiante debe aprender primero a determinar la configuración efectiva:

```bash
systemctl status kea-dhcp4
journalctl -u kea-dhcp4
journalctl -u kea-dhcp4 -f
```

y después localizar o configurar archivos de log cuando la implementación lo requiera.

## Troubleshooting

Troubleshooting constituye un eje transversal de todo el PATH.

La metodología general es:

```text
Cliente
  ↓
NIC / enlace
  ↓
VLAN
  ↓
Relay
  ↓
Routing
  ↓
Firewall
  ↓
SELinux
  ↓
Kea
  ↓
Subnet
  ↓
Pool
  ↓
Lease
  ↓
Options
```

Para DHCPv4:

```text
DISCOVER
   ↓
OFFER
   ↓
REQUEST
   ↓
ACK
```

El estudiante debe localizar exactamente dónde deja de producirse el flujo esperado.

El diagnóstico debe combinar:

```text
estado del servicio
        +
logs
        +
configuración
        +
estado de red
        +
captura de paquetes
```

## Herramientas de troubleshooting

Herramientas principales:

```text
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

No se considera suficiente solucionar problemas reiniciando el servicio sin identificar la causa.

## Seguridad

Debe cubrirse:

- rogue DHCP;
- DHCP starvation;
- pool exhaustion;
- spoofing de identificadores;
- DHCP snooping como concepto de switching;
- Option 82;
- segmentación;
- mínimo privilegio;
- firewalld;
- SELinux;
- protección del Control Agent;
- seguridad de API;
- permisos;
- backends;
- auditoría.

## Observabilidad

El estudiante debe aprender a observar:

- leases activas;
- utilización de pools;
- agotamiento de direcciones;
- errores;
- estado HA;
- salud de backends;
- tendencias de consumo;
- estadísticas Kea.

Esto debe desembocar en capacity planning y alertas operativas.

## Automatización

Se introduce la automatización mediante:

- Kea Control Agent;
- API;
- JSON;
- curl;
- jq;
- validación previa;
- backup;
- rollback;
- health checks.

Ansible puede utilizarse posteriormente para automatización completa, pero el alumno debe comprender primero la administración manual subyacente.

## Laboratorios

Los laboratorios deben ser reproducibles y aislados.

Topología mínima recomendada:

```text
client1 ─┐
         ├── subnet/VLAN ── relay/router ── kea1
client2 ─┘                                │
                                         └── kea2
                                             HA
```

Los escenarios deben incluir:

- DHCPv4;
- DHCPv6;
- reservations;
- options;
- múltiples subnets;
- relay;
- VLAN;
- HA;
- logs;
- packet capture;
- pool exhaustion;
- configuración inválida;
- firewall;
- SELinux;
- fallos de relay;
- fallos HA;
- recuperación.

## Límites del dominio

La integración completa DHCP/DNS no se desarrolla aquí para evitar solapamiento.

Este PATH únicamente prepara los conceptos necesarios.

La continuación corresponde al PATH independiente:

```text
DHCP + DNS Integration
│
├── Kea DHCP-DDNS
├── D2
├── BIND Dynamic Update
├── TSIG
├── A / AAAA
├── PTR
└── lease ↔ DNS lifecycle
```

## Resultado final

Al completar el dominio, el estudiante debe poder:

1. explicar DHCPv4 y DHCPv6 a nivel de protocolo;
2. instalar y operar Kea en Fedora/RHEL;
3. diseñar pools, reservations y options;
4. desplegar relay y HA;
5. interpretar leases y estados internos;
6. utilizar logs de manera efectiva;
7. capturar e interpretar tráfico DHCP;
8. diagnosticar problemas de red, servicio, firewall y SELinux;
9. identificar causas raíz;
10. diseñar y mantener una infraestructura DHCP preparada para producción;
11. continuar hacia la integración DHCP + DNS sin mezclar ambos dominios prematuramente.
