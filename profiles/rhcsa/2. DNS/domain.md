# Domain — DNS + BIND 9

## Dominio del curso

Este curso cubre DNS desde sus fundamentos hasta un nivel experto, con BIND 9 como implementación principal y Fedora/RHEL como plataforma de administración.

El objetivo no es aprender únicamente a editar `named.conf`, sino comprender DNS como protocolo distribuido, jerárquico y crítico para la infraestructura, y ser capaz de diseñar, desplegar, operar, asegurar, automatizar, monitorizar y diagnosticar servicios DNS reales.

## Alcance técnico

### Fundamentos de DNS
- Namespace jerárquico.
- Root, TLD, dominios y subdominios.
- FQDN y nombres relativos.
- Stub resolver, recursive resolver y authoritative server.
- Consultas recursivas e iterativas.
- Delegación.
- Caché positiva y negativa.
- TTL.
- UDP y TCP.
- EDNS(0).
- Formato de mensajes DNS.
- Flags y RCODE.
- Integración con NSS, glibc, `/etc/resolv.conf`, NetworkManager y mecanismos de resolución del sistema.

### Herramientas
- `dig`
- `host`
- `nslookup`
- `delv`
- `getent`
- `resolvectl`
- `nmcli`
- `rndc`
- `named-checkconf`
- `named-checkzone`
- `tcpdump`
- Wireshark
- `ss`
- `journalctl`
- `strace` como herramienta avanzada de último recurso.

### BIND 9
- Instalación mediante DNF.
- Paquetes y archivos RPM.
- `named`.
- `named.service`.
- `/etc/named.conf`.
- `/etc/named/`.
- `/var/named/`.
- Permisos y ownership.
- Estructura modular de configuración.
- `options`, `zone`, `acl`, `key`, `server`, `logging`, `controls` y `view`.
- Validación de configuración y zonas.
- Administración mediante `rndc`.

### DNS authoritative
- Primary y secondary.
- Delegación.
- Zone cuts.
- Glue.
- In-bailiwick y out-of-bailiwick.
- Hidden primary.
- Arquitecturas multi-secondary.
- AXFR.
- IXFR.
- NOTIFY.
- Alta disponibilidad.

### Recursive y caching DNS
- Resolución iterativa.
- Root hints.
- Root priming.
- Cache lifetime.
- Positive y negative caching.
- NXDOMAIN y NODATA.
- Prefetch.
- Serve stale.
- QNAME minimization.
- DNSSEC validation.
- Prevención de open resolvers.
- Performance y seguridad del resolver.

### Zonas y Resource Records
- Master file format.
- `$ORIGIN`.
- `$TTL`.
- SOA.
- Serial, refresh, retry, expire y negative TTL.
- A.
- AAAA.
- NS.
- CNAME.
- MX.
- PTR.
- TXT.
- SRV.
- CAA.
- NAPTR.
- SSHFP.
- TLSA.
- SVCB.
- HTTPS.
- Wildcards.
- Forward zones.
- Reverse zones IPv4.
- `in-addr.arpa`.
- RFC 2317.
- Reverse IPv6.
- `ip6.arpa`.

### Forwarding
- Forwarders.
- `forward first`.
- `forward only`.
- Global forwarding.
- Per-zone forwarding.
- Conditional forwarding.
- Arquitecturas empresariales de forwarding.

### ACL y TSIG
- ACL de BIND.
- `allow-query`.
- `allow-query-cache`.
- `allow-recursion`.
- `allow-transfer`.
- `allow-update`.
- TSIG.
- HMAC.
- Autenticación de transferencias.
- Autenticación de actualizaciones dinámicas.
- Gestión y rotación de secretos.

### DDNS
- RFC 2136.
- DNS UPDATE.
- `nsupdate`.
- `allow-update`.
- `update-policy`.
- TSIG + DDNS.
- Journals `.jnl`.
- `rndc freeze`, `thaw` y `sync`.
- Forward y reverse updates.
- Integración DHCP/DNS.
- BIND + Kea.
- Kea DHCP-DDNS/D2.
- Lifecycle lease ↔ DNS.

### DNSSEC
- Objetivos y límites de DNSSEC.
- Cadena de confianza.
- Trust anchors.
- DNSKEY.
- RRSIG.
- DS.
- NSEC.
- NSEC3.
- ZSK.
- KSK.
- CSK.
- Signing.
- Validation.
- `dnssec-policy`.
- Key lifecycle.
- Key rollover.
- CDS/CDNSKEY.
- Parent-child trust.
- Estados secure, insecure, bogus e indeterminate.
- Diagnóstico con `dig` y `delv`.
- Relación con sincronización temporal mediante Chrony/NTP.

### Views y Split DNS
- Views.
- Split-horizon DNS.
- `match-clients`.
- `match-destinations`.
- Vistas internas y externas.
- ACL y recursion por view.
- Consideraciones de DNSSEC.

### Instalación y operación Fedora/RHEL
El curso debe enseñar explícitamente:
- instalación;
- descubrimiento de paquetes y archivos;
- habilitación y administración del servicio;
- rutas de configuración;
- permisos;
- SELinux;
- firewalld;
- validación;
- actualización;
- backup;
- restore;
- disaster recovery.

No se debe asumir que una configuración funciona simplemente porque `named` inicia.

## Logging

Logging es una competencia central del curso.

### journald
- `systemctl status named`
- `journalctl -u named`
- filtrado temporal y por prioridad;
- seguimiento en tiempo real;
- correlación entre eventos del servicio y errores DNS.

### Logging propio de BIND
- `logging {}`
- channels.
- categories.
- severity.
- `general`.
- `queries`.
- `query-errors`.
- `security`.
- `resolver`.
- `lame-servers`.
- `notify`.
- `xfer-in`.
- `xfer-out`.
- `update`.
- `update-security`.
- `dnssec`.
- `rpz`.
- `rate-limit`.

Se puede enseñar el diseño de logs dedicados bajo `/var/log/named/`, pero nunca afirmar que todas las instalaciones escriben allí por defecto. Deben explicarse configuración, ownership, permisos, SELinux y rotación.

## Troubleshooting

Troubleshooting es un eje transversal, no únicamente un bloque final.

La metodología debe seguir la cadena:

```text
Aplicación
    ↓
NSS / glibc
    ↓
Configuración del resolver local
    ↓
Recursive resolver
    ↓
Root
    ↓
TLD
    ↓
Delegación
    ↓
Authoritative server
    ↓
Zona / Resource Record
    ↓
Respuesta al cliente
```

Debe cubrir como mínimo:
- NXDOMAIN.
- NODATA.
- SERVFAIL.
- REFUSED.
- Timeout.
- Lame delegation.
- Broken delegation.
- Missing/incorrect glue.
- Serial incorrecto.
- AXFR/IXFR failures.
- NOTIFY failures.
- Problemas de caché.
- DNSSEC bogus.
- RRSIG expirada.
- Missing/incorrect DS.
- Clock skew.
- Problemas UDP/TCP.
- EDNS.
- MTU y fragmentación.
- firewalld.
- SELinux AVC.
- DDNS.
- TSIG.
- Kea/D2.

El alumno debe aprender a demostrar dónde se encuentra el fallo, no limitarse a reiniciar servicios.

## Seguridad
- Cache poisoning.
- Spoofing.
- Reflection/amplification.
- Open resolvers.
- DNS tunneling.
- Zone transfer leakage.
- Reconnaissance.
- Random subdomain attacks.
- NXDOMAIN floods.
- RRL.
- ACL.
- TSIG.
- DNSSEC.
- Minimal responses.
- Least privilege.
- SELinux.
- firewalld.
- RPZ.
- Hardening.

## DNS moderno
- DNS over TLS.
- DNS over HTTPS.
- DNS over QUIC.
- Diferencias entre cifrado de transporte y DNSSEC.
- Privacidad.
- Políticas empresariales.
- Limitaciones operacionales.

## Observabilidad y rendimiento
- Availability.
- Latency.
- QPS.
- RCODE.
- NXDOMAIN/SERVFAIL rate.
- Cache hit ratio.
- Recursive clients.
- Transfer failures.
- DNSSEC failures.
- Expiración de firmas.
- `rndc stats`.
- Statistics channels.
- Prometheus.
- Grafana.
- Synthetic queries.
- Alerting.
- Capacity planning.
- Benchmarking.
- Escalabilidad horizontal.
- Anycast.

## Automatización
- Git.
- CI.
- `named-checkconf`.
- `named-checkzone`.
- Ansible.
- Templates.
- Static zone files.
- Handlers.
- Validación antes del reload.
- `nsupdate`.
- Terraform cuando corresponda.
- GitOps.
- Gestión segura de secretos.
- Rollback.

## Integraciones
- Kea DHCP.
- Kea DHCP-DDNS/D2.
- FreeIPA.
- Kerberos.
- LDAP.
- Active Directory a nivel de interoperabilidad DNS.
- VPN.
- Containers.
- Kubernetes DNS como introducción.
- Cloud DNS.
- Hybrid DNS.

## Papel de DNS respecto a IAM

El curso debe enseñar DNS en dos arquitecturas explícitas:

### DNS sin IAM
- BIND puede operar de forma completamente independiente de LDAP, Kerberos y FreeIPA.
- Authoritative DNS, recursive/caching DNS, forwarding, DNSSEC y DDNS no requieren por sí mismos un directorio central de usuarios.
- DNS no debe presentarse como un consumidor obligatorio de identidades humanas.

### DNS con IAM
- DNS actúa como infraestructura y dependencia fundamental para descubrimiento y resolución de servicios de identidad.
- Debe cubrir registros SRV para Kerberos y LDAP, descubrimiento de KDC y directory servers, FQDN, forward/reverse DNS y DDNS.
- FreeIPA puede integrar DNS como parte de la plataforma, o utilizar una arquitectura con DNS externo según el diseño.
- Debe distinguirse claramente el consumo de identidades humanas de la autenticación/autorización técnica de operaciones DNS.
- Deben introducirse conceptualmente TSIG y GSS-TSIG donde corresponda, sin confundirlos con autenticación interactiva de usuarios.
- Troubleshooting debe poder seguir la cadena DNS -> SRV -> Kerberos/LDAP -> FreeIPA.

## Internals y nivel experto
- RFC 1034/1035.
- Wire format.
- Labels.
- Name compression.
- OPT pseudo-RR.
- Extended RCODE.
- DNS Cookies.
- Resolver algorithms.
- Cache internals.
- Bailiwick.
- DNSSEC validation algorithm.
- Lectura de capturas a nivel de paquete.
- Arquitecturas multi-site y multi-datacenter.
- Migraciones sin downtime.
- Incident response.
- Disaster recovery.

## Plataforma objetivo

Prioridad:
1. Fedora.
2. Red Hat Enterprise Linux.
3. Conceptos DNS independientes de distribución.

Los ejemplos de administración del sistema deben favorecer DNF, RPM, systemd, journald, NetworkManager, SELinux y firewalld.

## Límites pedagógicos

- No confundir DNS estándar con comportamiento específico de BIND.
- No enseñar configuraciones inseguras como modelo de producción.
- No usar `setenforce 0` como solución.
- No crear open resolvers salvo como escenario controlado para demostrar el riesgo.
- No depender exclusivamente de copiar configuraciones.
- No ocultar la razón protocolaria de una directiva.
- No asumir defaults cuando puedan cambiar entre versiones.
- Verificar opciones dependientes de versión contra la documentación de BIND instalada/oficial.

## Resultado esperado

Al finalizar, el estudiante debe ser capaz de:

1. Explicar una resolución DNS completa a nivel de protocolo.
2. Instalar y administrar BIND 9 en Fedora/RHEL.
3. Construir y delegar zonas forward y reverse.
4. Operar authoritative y recursive DNS.
5. Diseñar primary/secondary y transferencias seguras.
6. Implementar TSIG, DDNS y DNSSEC.
7. Integrar BIND con Kea.
8. Aplicar SELinux y firewalld correctamente.
9. Diseñar logging y observabilidad.
10. Diagnosticar fallos mediante evidencias.
11. Automatizar configuración y validación.
12. Diseñar una infraestructura DNS empresarial resiliente.
13. Analizar tráfico DNS y comprender internals del protocolo.
14. Ejecutar backup, restore, incident response y disaster recovery.


## Revisión de dependencias, progresión y operación

### Orden de aprendizaje y orden de despliegue

Mantener todos los bloques 0–37. El orden de revisión de los paths no establece
el orden de arranque ni obliga a completar el curso entero antes de instalar IAM.
La progresión práctica es base RHCSA → TIME y DNS básico → DNS operativo → IAM
→ integraciones DNS/IAM. Los bloques avanzados se completan progresivamente.
DNS autoritativo/recursivo independiente funciona sin directorio de usuarios.
DNSSEC necesita una hora suficientemente correcta para validar firmas; TSIG
comprueba marcas temporales; Kerberos agrega sus propias condiciones de tiempo.
No equiparar estos requisitos a una dependencia obligatoria de DNS respecto a IAM.

### Evitar el ciclo TIME/DNS

Chrony puede necesitar DNS para resolver nombres de fuentes NTP. Un reloj muy
incorrecto puede impedir validar DNSSEC, resolver esas fuentes y recuperar la hora.
El laboratorio debe documentar una ruta de arranque: reloj inicial razonable y una
fuente temporal interna accesible sin depender del resolver que se está reparando,
por ejemplo una dirección estable administrada y validada para ese laboratorio.
No fijar direcciones arbitrarias de pools públicos ni desactivar permanentemente
la validación. Un bootstrap por IP no sustituye la autenticación ni los requisitos
de certificados de NTS. Verificar resolución y sincronización después de reiniciar.
`After=` de systemd solo establece orden; no demuestra que el reloj esté sincronizado.
Consultar la salida de `chronyc tracking`, `chronyc sources -v` y `timedatectl`;
no usar el estado activo de un servicio como única evidencia.

### Delimitación de IAM

El bloque 33 compara arquitecturas, dependencias y responsabilidades. El bloque 34
implementa y diagnostica la integración. Conservar sus lecciones existentes como
puntos de enlace, sin repetir explicaciones completas. IAM es el origen central de
usuarios, hosts y credenciales. No crear directorios de usuarios paralelos en BIND.
En FreeIPA integrado, utilizar sus herramientas y políticas para administrar DNS;
no sobrescribir su configuración generada con un rol BIND independiente.
En DNS externo, comprobar y publicar los registros que indique la versión de IdM.
No asumir que toda aplicación LDAP busca SRV ni que PTR es un requisito universal
de Kerberos: distinguir requisitos de instalación IdM, descubrimiento y canonicalización.
Para GSS-TSIG, explicar el principal de servicio DNS y el keytab gestionado por la
plataforma, las credenciales del actualizador, `kinit`, `klist`, `nsupdate -g` y la
política de autorización. No copiar keytabs entre equipos como práctica genérica.

### Operación avanzada verificable

- Serial: aplicar RFC 1982 a un contador de 32 bits; no tratarlo como fecha obligatoria.
- TSIG: usar RFC 8945 como referencia actual; distinguir BADTIME, BADKEY y BADSIG.
  TSIG autentica transacciones y no cifra por sí mismo los datos.
- DNSSEC: distinguir TTL de inception/expiration de RRSIG. Planificar rollover según
  TTL, propagación, estado de claves y publicación del DS, sin cronogramas universales.
- Para una zona privada, construir una cadena de confianza local o un trust anchor
  explícito en el resolver del laboratorio. No intentar publicar DS en un padre público
  de un dominio que no se controla. En producción, el DS requiere coordinación con el padre.
- EDE: interpretar RFC 8914 y las capacidades de servidor/cliente. Complementa RCODE;
  no garantiza presencia, autenticidad ni una causa definitiva del fallo.
- dnstap: comprobar compilación, dependencias y herramientas del paquete instalado.
  Definir retención y acceso; no capturar tráfico de otros entornos para las prácticas.
- Backup: definir un punto coherente de zonas dinámicas y journals; incluir claves,
  metadatos y estado de DNSSEC. Restaurar en aislamiento y probar consultas reales.
- DoT/DoH/DoQ: documentar por versión y rol el soporte entrante, saliente y de las
  herramientas. No deducir soporte DoQ del soporte de DoT/DoH. Si se usa otra
  implementación, identificarla y mantener BIND como núcleo del curso.

## Contrato común de los laboratorios

El contenido generado para cada práctica debe incluir archivos de configuración
completos del escenario, comandos, resultados esperados y restauración. Estos cuatro
archivos definen el currículo; no constituyen un despliegue ya ejecutado del laboratorio.
La automatización se incorpora progresivamente después del montaje y diagnóstico manual.

### Topología de referencia aislada

| Nodo | IPv4 | Función |
|---|---|---|
| ns1.lab.example.test | 192.168.56.10 | Primary authoritative |
| ns2.lab.example.test | 192.168.56.11 | Secondary authoritative |
| resolver.lab.example.test | 192.168.56.12 | Resolver separado |
| client.lab.example.test | 192.168.56.20 | Cliente de pruebas |
| time.lab.example.test | 192.168.56.30 | Fuente temporal del laboratorio |
| ipa.lab.example.test | 192.168.56.40 | IAM, solo escenario integrado |
| kea.lab.example.test | 192.168.56.50 | DHCP/D2, bloques integrados |

Usar una red privada sin puente a la LAN; adaptar el rango si existe conflicto.
Para IPv6, generar un prefijo ULA propio y documentar subred, direcciones y reversa.
`lab.example.test` es el dominio de referencia; conservar `example.internal` de 7.2
como comparación de diseño. Nunca usar `.local` para este laboratorio DNS unicast.
Las pruebas iterativas y DNSSEC usarán una jerarquía privada de padre/hijo para `.test`;
`dig +trace` contra la raíz pública no resolverá las zonas privadas del laboratorio.
La salida a Internet solo se necesita para paquetes y ejercicios públicos seleccionados.
DHCP se limitará a la red del laboratorio. No exponer recursión, RNDC ni estadísticas.
La fuente TIME debe ser una fuente válida según el path TIME; no declarar un servidor
sincronizado solo porque responde NTP ni usar `local` de Chrony como equivalente a UTC.

### Entregables y aceptación por práctica

1. Objetivo, prerrequisitos y versión de sistema/BIND/paquetes.
2. Diagrama o tabla de nodos, red, zonas, puertos y credenciales técnicas necesarias.
3. Configuración comentada, permisos, SELinux, firewalld y validación previa aplicable.
4. Consultas desde cliente y servidor, por UDP/TCP y por IPv4/IPv6 cuando corresponda.
5. Resultado esperado: AA/RA/AD según rol, RCODE, RRsets y ausencia de acceso no autorizado.
6. Fallo introducido, evidencia de causa y recuperación con las mismas comprobaciones.
7. Restauración del estado inicial y registro de cambios, sin secretos en el informe.

### Pruebas finales obligatorias

- Perfil A sin IAM: primary/secondary, resolver, TSIG, DNSSEC y Kea según bloque 36.
- Perfil B con IAM: extender A con DNS externo para IdM o usar un subdominio delegado
  para DNS integrado; no ejecutar dos servicios distintos sobre la misma IP/puerto.
- Modificar un RR y demostrar convergencia del secundario; después simular fallo del primary.
- Probar respuesta a clientes permitidos y rechazo de recursión/transferencia no autorizada.
- Completar rollover sin pérdida de validación y recuperar una firma/DS deliberadamente roto.
- Simular BADTIME y clock skew solo en VMs desechables con snapshot y fuera del host.
- Reiniciar el conjunto y demostrar recuperación de TIME, DNS y luego IAM.
- Restaurar backup en aislamiento, medir tiempo de recuperación y documentar RPO/RTO.
- Aportar consultas y logs antes/después, capturas relevantes y métricas; no basta con `active`.
