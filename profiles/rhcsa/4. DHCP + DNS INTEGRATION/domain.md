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

release o expiración seguida de reclamación, según el caso
  ↓
si corresponde y el procesamiento tiene éxito: REMOVE NCR
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


## 17. Dependencias y relación con IAM

Orden base de práctica: RHCSA → TIME → DNS y DHCP → DHCP + DNS Integration.
IAM no es prerrequisito del despliegue Kea + D2 + BIND con HMAC-TSIG.
Esta ruta no administra ni autentica usuarios humanos mediante LDAP/SSSD/PAM.
La identidad DHCP (client-id/DUID), el ownership DHCID y la identidad que firma
un UPDATE son conceptos distintos.

En una infraestructura con FreeIPA deben acordarse las zonas, subdominios y
nombres que administra cada actor. Documentar quién escribe A/AAAA/PTR y qué
sucede si el cliente también actualiza DNS. Evitar que D2 gestione libremente
nombres de servidores, registros de infraestructura o nombres administrados
por otro actor. El laboratorio base usará una zona dinámica dedicada.

GSS-TSIG/Kerberos es una ampliación opcional posterior al PATH IAM. Requiere
verificar la versión y disponibilidad del hook de D2, configurar principals y
keytabs de servicio y autorizar únicamente las actualizaciones necesarias.
No se presupone que disponer de FreeIPA habilite automáticamente D2 para sus
zonas. En FreeIPA los cambios de política deben realizarse mediante mecanismos
soportados por la plataforma, sin trasladar ciegamente un named.conf independiente.
La ruta principal conserva TSIG compartido y puede completarse sin IAM.

## 18. Semántica que toda lección debe respetar

- TTL controla la duración en caché; no borra registros del servidor autoritativo.
- Expiración del lease, reclamación, generación de REMOVE y eliminación DNS
  confirmada son momentos diferentes. Registrar timestamps y configuración.
- Un lease válido no demuestra que DNS se haya actualizado correctamente.
- Forward y reverse no forman una transacción atómica conjunta. Una operación
  RFC 2136 se limita a una zona; deben diagnosticarse resultados parciales.
- TSIG aporta autenticación e integridad de mensajes, no cifrado del tráfico.
- DHCID protege ownership según las reglas aplicadas; no autentica personas.
- La cola de solicitudes de D2 es volátil: su contenido pendiente puede perderse
  al detener el servicio. No prometer replay duradero ni reconciliación automática.
- HA de DHCP no garantiza HA completa de DDNS. Probar cada componente y el
  destino real de UPDATE en la topología DNS elegida.

## 19. Identidad y conflictos en dual stack

Estudiar qué datos se usan para construir DHCID en cada protocolo. No asumir
que compartir hostname, MAC o equipo físico produce automáticamente el mismo
DHCID entre DHCPv4 y DHCPv6. Introducir client-id, DUID, IAID y RFC 4361 según
corresponda, contrastando el resultado con la implementación y clientes reales.

Comparar los modos admitidos de `ddns-conflict-resolution-mode`, la comprobación
de DHCID y las protecciones que se pierden al cambiar de modo. La práctica debe
incluir nombres estáticos existentes, dos clientes con el mismo FQDN y un host
dual stack. No resolver un fallo deshabilitando indiscriminadamente salvaguardas.

Para IPv6, distinguir direcciones asignadas mediante DHCPv6 de SLAAC y sus
extensiones de privacidad. D2 no inventaría automáticamente las direcciones
SLAAC. Un prefijo delegado tampoco equivale a una dirección AAAA de un host.

## 20. Configuración dependiente de versión

Registrar versiones de Kea y BIND antes de generar configuraciones. Consultar
la documentación de esa versión para opciones, valores, ámbitos y hooks.
Incluir `ddns-update-on-renew`, `ddns-conflict-resolution-mode`, controles TTL,
precedencia global/subred/reserva y flags de Client FQDN. No garantizar que
una renovación repare todas las divergencias; comprobar requisitos y resultados.

Descubrir también los mecanismos de control disponibles: Control Agent e
interfaces del daemon según versión. No presentar una arquitectura histórica
como requisito universal de instalación.

## 21. Laboratorios ampliados y criterios de aceptación

El laboratorio base será local, aislado y sin exposición pública, con clientes
compatibles y sin otro DHCP que interfiera. Debe entregar configuraciones
completas y comandos reproducibles al desarrollar las lecciones; estos cuatro
archivos definen el currículo y no son un despliegue ejecutable del laboratorio.

| Caso | Evidencia mínima de aceptación |
|---|---|
| ADD IPv4/IPv6 | Lease, FQDN, NCR y A/AAAA/PTR consultados al autoritativo |
| Renovación | Comparación antes/después y explicación de la política efectiva |
| Release/reclamación | Tiempos de transición, REMOVE y resultado DNS verificado |
| Conflicto de nombre | Rechazo o acción esperada y conservación de registros ajenos |
| Dual stack | Identidades/DHCID explicados y A/AAAA/PTR coherentes |
| Fallo TSIG | Respuesta/log de fallo y recuperación sin ampliar privilegios |
| Caída D2/DNS | Divergencia identificada, inventario afectado y reparación probada |
| Caché | Contraste entre autoritativo, caché positiva y caché negativa |
| Recuperación | Leases y zonas restaurados, ownership verificado y consultas finales |
| GSS-TSIG opcional | Identidad de servicio y permisos probados tras completar IAM |

La reconciliación comienza con inventario de leases y registros, propuesta de
cambios y verificación de ownership. Usar comandos de reenvío DDNS únicamente
si la versión y hooks los soportan. Una reparación manual debe conservar otras
direcciones y RRsets válidos; nunca eliminar en bloque una zona para ocultar
inconsistencias. Documentar RPO/RTO y guardar evidencias antes y después.

## 22. Referencias técnicas de esta revisión

- Kea ARM, DHCP-DDNS: https://kea.readthedocs.io/en/stable/arm/ddns.html
- Kea ARM, hooks: https://kea.readthedocs.io/en/stable/arm/hooks.html
- Kea ARM, DHCPv4: https://kea.readthedocs.io/en/stable/arm/dhcp4-srv.html
- TSIG vigente: https://www.rfc-editor.org/info/rfc8945/

Los enlaces stable sirven para localizar documentación; el laboratorio debe
usar la edición que corresponda a las versiones instaladas.
