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
- API directa y sockets de control; Control Agent para versiones anteriores;
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
├── API directa y sockets de control (Control Agent histórico)
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
- IA_TA únicamente como mecanismo histórico obsoleto (RFC 9915);
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
- protección de sockets de control y listeners de administración;
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

- API directa por daemon y compatibilidad histórica con Control Agent;
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

## Revisión técnica y política de versiones — 2026-10-23

Se conservan los bloques 0–24 y sus identificadores de lección. Se amplían sus
objetivos y se añade el bloque 25 de clasificación. Para integrar esta materia
antes de los escenarios avanzados, el orden de estudio es 0–10, 25, 11–24.
El número del bloque identifica contenido, no impone el orden de ejecución.

Antes del laboratorio se registra distribución, repositorio, versión de Kea,
paquetes de hooks, bibliotecas, unidades systemd y versión del ARM. Usar el
manual de la versión instalada; los enlaces stable pueden cambiar. No asumir
nombres de unidades, rutas de hooks ni disponibilidad de paquetes en RHEL.
Los comandos systemctl de este documento son ejemplos sujetos al inventario.

Kea 3.0 incorpora acceso directo a la API y depreca Control Agent. Kea 3.2 lo
retira. Enseñar sockets Unix y HTTP/HTTPS directos según versión; mantener el
agente como itinerario de compatibilidad para instalaciones anteriores.
Usar control-sockets en versiones modernas y verificar compatibilidad antes de
migrar una configuración. Las pruebas -t y -T tienen alcance diferente; una
validación correcta no demuestra que la red o todos los recursos funcionen.
Kea admite comentarios en configuración: jq solo valida JSON estricto y no
sustituye al parser de Kea.

## Relaciones con IAM, TIME y DNS

DHCP asigna configuración de red sin requerir LDAP, Kerberos, SSSD o FreeIPA.
MAC, client-id, DUID, reservas, clases y Option 82 son datos para seleccionar
políticas; no prueban la identidad de un usuario. No crear directorios de
usuarios dentro de este PATH. El acceso administrativo al host puede consumir
IAM de forma opcional sin cambiar el protocolo de asignación DHCP.

DNS y TIME pueden anunciarse a clientes mediante opciones compatibles con cada
protocolo. Anunciar un servidor no configura ese servidor ni garantiza que el
cliente acepte la opción. DHCP básico puede operar sin resolver nombres y sin
IAM; las integraciones que usan nombres, TLS, HA o registros distribuidos
añaden requisitos que se deben comprobar por separado.

La integración DDNS se limita al puente del bloque 24. En el PATH siguiente,
TSIG autentica al actualizador autorizado ante DNS; no autentica a clientes
DHCP ni a usuarios. Si la zona está gestionada por FreeIPA, respetar su
administración y políticas; no modificar a ciegas su configuración BIND.

## Correcciones y profundidad de IPv6

RFC 9915 sustituye a RFC 8415 como base normativa; IA_TA queda como historia.
Incluir CONFIRM, Rapid Commit, códigos de estado, temporizadores por IA y
troubleshooting de movilidad entre enlaces. DHCPv6 no entrega la ruta por
defecto: se aprende mediante RA. Distinguir M/O, SLAAC, RDNSS/DNSSL y las
capacidades efectivas del cliente. Una dirección o un prefijo concedido no
prueba conectividad: validar RA, rutas y tráfico de ida y vuelta.

## Clasificación, persistencia y operación avanzada

El bloque 25 desarrolla clases, expresiones, evaluación, reservas, shared
networks y selección de pools/opciones. Cada regla se justifica con paquetes
reales y se prueba con clientes que coinciden y que no coinciden.

Las reservas usan parámetros actuales como reservations-global,
reservations-in-subnet y reservations-out-of-pool según el ARM correspondiente.
reservation-mode se trata como sintaxis heredada a migrar, no como receta base.

Memfile incluye persistencia y Lease File Cleanup. Enseñar recuperación sin
editar ficheros activos. Para SQL se exige un backend PostgreSQL funcional,
con alternativa MySQL/MariaDB, esquema compatible, permisos, credenciales,
reintentos y recuperación. Diferenciar leases, hosts y configuración: no son
backends intercambiables. Practicar backup y restauración; no presentar rollback
de esquema como una operación automáticamente reversible.

HA requiere verificar hooks, conectividad de peers y acceso desde relays.
Distinguir replicación de leases de distribución de configuración y de backup.
Ensayar caída del proceso, caída del host y partición del enlace entre peers.
Comparar estado y decisiones de asignación tras recuperación.

La capacidad se mide con perfdhcp en una red aislada, usando parámetros del
manual instalado. Registrar tasa ofrecida y respondida, pérdida, tiempos,
recursos, versión y ajustes. Comparar multithreading, colas y backends con
ensayos controlados; no trasladar un resultado aislado como garantía general.

## Contrato de laboratorio y evaluación

Topologías progresivas: (1) kea1 y cliente en un segmento; (2) router/relay y
dos segmentos cliente; (3) kea2 para HA; (4) backend SQL y cliente router IA_PD.
Usar redes virtuales aisladas y documentar cualquier DHCP preexistente de
libvirt. Configuración estática para servidores y relays; direccionamiento
dinámico en clientes. No se requiere acceso público ni IAM.

Cada lección práctica debe especificar prerrequisitos, topología, archivos,
comandos, resultado esperado, verificación positiva y negativa, evidencias y
limpieza/rollback. Las lecciones generadas deben incluir configuración completa
cuando sea necesaria, y explicar diferencias de versión. Estos cuatro archivos
son la especificación del curso: no constituyen un despliegue ejecutable.

Aceptación mínima:

| Escenario | Evidencia requerida |
|---|---|
| DHCPv4 | DORA, opciones aplicadas, lease persistente y renovación |
| DHCPv6 | Intercambio, IA/lifetimes, RA y ruta por defecto diferenciados |
| Reserva/clase | Cliente coincidente y no coincidente; decisión explicada |
| Relay | Captura en ambos lados y selección correcta de subnet |
| HA | Servicio durante fallo, resincronización y configuración coherente |
| SQL/LFC | Persistencia, mantenimiento y recuperación probados |
| Seguridad | Diagnóstico por logs/AVC sin desactivar SELinux como solución |
| Recuperación | Restauración aislada y medición frente a RPO/RTO definidos |
| Rendimiento | Informe de carga reproducible y limitaciones del ensayo |

El proyecto integrador utiliza estos criterios aunque el bloque de
clasificación tenga número 25. Entregar configuración, inventario, capturas,
logs relevantes, métricas y runbooks; proteger datos identificativos y secretos.
