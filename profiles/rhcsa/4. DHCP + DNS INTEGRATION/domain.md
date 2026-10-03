# Domain — DHCP + DNS Integration

## 1. Dominio del curso

Este curso cubre en profundidad la integración entre **DHCP y DNS** en sistemas
Fedora/RHEL utilizando principalmente:

- ISC Kea DHCPv4
- ISC Kea DHCPv6
- Kea DHCP-DDNS (D2)
- BIND 9
- DNS Dynamic Update (RFC 2136)
- TSIG
- DHCID
- registros A, AAAA y PTR

El objetivo no es estudiar DHCP y DNS como tecnologías aisladas, sino dominar
el sistema completo que mantiene sincronizado el ciclo de vida de un lease DHCP
con los registros DNS forward y reverse.

## 2. Modelo conceptual principal

La cadena técnica central del curso es:

```text
DHCP Client
    │
    │ DHCPv4 / DHCPv6
    ▼
Kea DHCP Server
    │
    │ Name Change Request (NCR)
    ▼
Kea DHCP-DDNS / D2
    │
    │ RFC 2136 DNS UPDATE
    │ TSIG authentication
    ▼
BIND authoritative DNS
    │
    ├── A
    ├── AAAA
    ├── PTR
    └── DHCID
```

El curso estudia tanto la creación como la modificación y eliminación de estos
registros durante el ciclo de vida del lease.

## 3. Áreas de conocimiento

### 3.1 DHCP-DDNS

Incluye:

- relación DHCP ↔ DNS;
- hostname y FQDN;
- DHCP Client FQDN;
- decisión de actualización por cliente/servidor;
- generación de Name Change Requests;
- ADD y REMOVE NCR;
- sincronización lease ↔ DNS.

### 3.2 Kea DHCP

Se cubren los componentes necesarios para DDNS:

- `kea-dhcp4`;
- `kea-dhcp6`;
- configuración DHCP-DDNS;
- generación de nombres;
- qualifying suffix;
- renovación;
- release;
- expiración;
- lease reclamation;
- interacción con D2.

### 3.3 Kea DHCP-DDNS / D2

D2 constituye el intermediario entre DHCP y DNS.

El dominio incluye:

- recepción de NCR;
- forward updates;
- reverse updates;
- selección de dominio;
- selección de servidor DNS;
- TSIG;
- comunicación RFC 2136;
- errores y reintentos;
- logging;
- troubleshooting.

### 3.4 BIND Dynamic Update

Incluye:

- servidor DNS autoritativo;
- zonas forward;
- reverse IPv4;
- reverse IPv6;
- RFC 2136;
- `allow-update`;
- `update-policy`;
- journals de zona;
- administración con `rndc`;
- comprobación mediante `dig`;
- pruebas mediante `nsupdate`.

### 3.5 TSIG

Incluye:

- autenticación de DNS UPDATE;
- secretos compartidos;
- algoritmos HMAC;
- generación y almacenamiento de claves;
- integración BIND ↔ D2;
- mínimo privilegio;
- rotación;
- BADKEY;
- BADSIG;
- BADTIME;
- dependencia de una hora correctamente sincronizada.

### 3.6 Forward DNS

Se estudian:

```text
hostname/FQDN
      │
      ├── IPv4 → A
      └── IPv6 → AAAA
```

Incluyendo creación, actualización, sustitución, TTL, eliminación y conflictos.

### 3.7 Reverse DNS

Se estudian:

```text
IPv4 → in-addr.arpa → PTR
IPv6 → ip6.arpa     → PTR
```

Incluyendo cálculo de nombres reverse, zonas reverse, consistencia
forward/reverse y detección de PTR huérfanos.

### 3.8 DHCID

Incluye:

- ownership de nombres;
- detección de conflictos;
- relación cliente ↔ lease ↔ nombre;
- protección contra sobrescrituras incorrectas;
- resolución de conflictos de FQDN.

## 4. Lease ↔ DNS lifecycle

Este es uno de los dominios fundamentales del curso.

```text
cliente solicita configuración
          ↓
Kea asigna lease
          ↓
obtención/generación hostname
          ↓
construcción FQDN
          ↓
NCR
          ↓
D2
          ↓
TSIG + RFC 2136
          ↓
A / AAAA + PTR + DHCID
```

Posteriormente:

```text
renew
  ↓
mantener o actualizar DNS

cambio de dirección/nombre
  ↓
eliminar registros anteriores
  ↓
crear registros nuevos

release / expiration / reclamation
  ↓
REMOVE NCR
  ↓
eliminar A / AAAA / PTR
```

El alumno debe comprender no solamente el estado final, sino cada transición.

## 5. IPv4 e IPv6

El curso debe cubrir ambos protocolos.

### IPv4

- DHCPv4;
- registros A;
- `in-addr.arpa`;
- PTR;
- lease lifecycle.

### IPv6

- DHCPv6;
- registros AAAA;
- `ip6.arpa`;
- formato nibble;
- PTR;
- lease lifecycle.

También debe estudiarse una infraestructura dual stack.

## 6. Instalación y plataforma

Plataforma principal:

```text
Fedora
RHEL
```

El contenido práctico debe incluir:

- paquetes;
- repositorios cuando sean necesarios;
- archivos de configuración;
- usuarios/grupos de servicio;
- directorios de runtime;
- systemd;
- firewalld;
- SELinux;
- permisos;
- validación de configuración.

No deben asumirse rutas o nombres de unidades idénticos entre todas las
versiones. Las lecciones deben enseñar a descubrirlos y verificarlos.

## 7. Logging

Logging forma parte del dominio principal y no debe relegarse a una nota.

Debe enseñarse a trabajar con:

- journald;
- `journalctl`;
- logging configurable de Kea;
- logging de D2;
- logging de BIND;
- categorías de logging;
- severidades;
- debug;
- timestamps;
- rotación;
- persistencia.

Especialmente importante:

```text
DHCP event
    ↓
Kea log
    ↓
NCR
    ↓
D2 log
    ↓
DNS UPDATE
    ↓
BIND update/security log
```

El alumno debe aprender a correlacionar estos eventos temporalmente.

### /var/log

El curso no debe afirmar que Kea o BIND siempre escriben en un archivo fijo de
`/var/log`.

Debe explicar la diferencia entre:

- mensajes capturados por journald;
- logging configurado explícitamente hacia archivos;
- syslog cuando corresponda;
- rutas dependientes de distribución/configuración.

## 8. Troubleshooting

Troubleshooting es una competencia principal.

La metodología debe seguir el flujo real:

```text
1. Cliente
2. Lease
3. Hostname/FQDN
4. decisión DDNS de Kea
5. NCR
6. D2
7. conectividad
8. selección de zona
9. TSIG
10. RFC 2136
11. BIND
12. A/AAAA
13. PTR
14. DHCID
```

Problemas que deben estudiarse:

- lease correcto sin registro DNS;
- A/AAAA sin PTR;
- PTR sin A/AAAA;
- registros stale;
- FQDN incorrecto;
- qualifying suffix incorrecto;
- conflictos de nombres;
- DHCID conflict;
- zona forward incorrecta;
- zona reverse incorrecta;
- D2 apuntando al DNS incorrecto;
- `REFUSED`;
- `NOTAUTH`;
- `NOTZONE`;
- `SERVFAIL`;
- `BADKEY`;
- `BADSIG`;
- `BADTIME`;
- timeout;
- firewall;
- SELinux;
- permisos;
- errores de configuración.

## 9. Herramientas de diagnóstico

El alumno debe adquirir soltura con:

```text
systemctl
journalctl
dig
nsupdate
rndc
named-checkconf
named-checkzone
tcpdump
ss
firewall-cmd
```

Cuando resulte útil, Wireshark se empleará para inspección de protocolos.

## 10. Seguridad

El dominio de seguridad incluye:

- nunca exponer Dynamic Update indiscriminadamente;
- TSIG;
- `update-policy`;
- mínimo privilegio;
- separación de claves;
- protección de secretos;
- rotación;
- permisos;
- SELinux;
- firewalld;
- segmentación;
- auditoría;
- backups seguros.

## 11. Alta disponibilidad

A nivel avanzado deben estudiarse:

- Kea HA;
- interacción HA ↔ DDNS;
- prevención de updates duplicados;
- fallo de D2;
- fallo del DNS autoritativo;
- primario/secundario BIND;
- transferencias de zona;
- NOTIFY;
- recuperación;
- consistencia después de fallos.

## 12. Operación

El curso debe desarrollar competencias para:

- comprobar salud de servicios;
- validar forward/reverse DNS;
- detectar registros stale;
- auditar lease ↔ DNS;
- realizar backups;
- restaurar configuraciones;
- tratar correctamente zonas dinámicas;
- respaldar claves TSIG;
- actualizar Kea/BIND;
- validar después de upgrades;
- crear runbooks.

## 13. Laboratorios

Las lecciones deben favorecer laboratorios reproducibles.

Cada laboratorio relevante debe incluir:

1. objetivo;
2. topología;
3. configuración;
4. comandos;
5. resultado esperado;
6. validación;
7. logs relevantes;
8. errores frecuentes;
9. troubleshooting;
10. limpieza/restauración cuando corresponda.

## 14. Laboratorio final

La práctica final debe implementar:

```text
               ┌───────────────┐
               │ DHCP Client   │
               └───────┬───────┘
                       │
                 DHCPv4/DHCPv6
                       │
               ┌───────▼───────┐
               │   Kea DHCP    │
               └───────┬───────┘
                       │ NCR
               ┌───────▼───────┐
               │    Kea D2     │
               └───────┬───────┘
                       │
                RFC 2136 + TSIG
                       │
               ┌───────▼───────┐
               │     BIND      │
               └───────┬───────┘
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              A / AAAA      PTR
```

Debe comprobarse:

- asignación DHCPv4;
- asignación DHCPv6;
- A;
- AAAA;
- PTR IPv4;
- PTR IPv6;
- DHCID;
- renovación;
- cambio;
- release;
- expiración;
- eliminación DNS;
- logs;
- capturas de tráfico;
- TSIG;
- recuperación ante fallos.

## 15. Fuera de alcance principal

DNS y DHCP básicos se repasan solamente cuando sean necesarios para comprender
la integración. Sus cursos independientes deben cubrirlos con mayor amplitud.

No es objetivo convertir este PATH en un curso general de:

- DNS desde cero;
- BIND completo;
- DHCP desde cero;
- networking general;
- systemd;
- SELinux;
- firewalld.

Estos conocimientos se integran aquí desde la perspectiva DHCP-DDNS.

## 16. Resultado esperado

Al finalizar, el alumno debe ser capaz de:

> Diseñar, desplegar, asegurar, operar y diagnosticar una infraestructura
> DHCP-DDNS basada en Kea y BIND, comprendiendo cada transición desde la
> creación de un lease hasta la creación o eliminación autenticada de sus
> registros A/AAAA/PTR y pudiendo demostrar el comportamiento mediante
> configuración, logs, consultas DNS y capturas de red.
