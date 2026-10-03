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
