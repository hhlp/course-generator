# Bibliography — Proxy / Load Balancing

## Documentación principal

### Squid
- Squid Project — Official Documentation.
- Squid Wiki — Configuration, ACL, authentication, caching and troubleshooting documentation.
- `squid.conf` reference/documentation correspondiente a la versión instalada.
- Páginas man incluidas por la distribución.

### Nginx
- NGINX — Official Documentation.
- NGINX — HTTP Proxy Module documentation.
- NGINX — HTTP Upstream Module documentation.
- NGINX — Stream Module documentation.
- NGINX — SSL Module documentation.
- Documentación y notas de los paquetes Fedora/RHEL utilizados en los laboratorios.

### HAProxy
- HAProxy Technologies — HAProxy Configuration Manual correspondiente a la rama estudiada.
- HAProxy Documentation — Management Guide.
- HAProxy Documentation — Runtime API.
- HAProxy Documentation — Configuration tutorials y referencias oficiales.

### Keepalived
- Keepalived — Official Documentation.
- `keepalived.conf(5)` y páginas man relacionadas.
- Documentación de VRRP relevante para comprender el protocolo y sus restricciones.

## IAM e identidad centralizada
- FreeIPA — documentación oficial de administración, clientes, Kerberos, principals y keytabs.
- MIT Kerberos — documentación oficial, especialmente principals, tickets, keytabs y troubleshooting.
- OpenLDAP — documentación oficial para conceptos LDAP, bind, search, TLS y control de acceso.
- SSSD — documentación oficial para comprender su papel cuando participe en la integración del host.
- RFC y estándares IETF aplicables a Kerberos, LDAP y mecanismos HTTP Negotiate/SPNEGO.
- La documentación del PATH IAM es la referencia para creación, ciclo de vida y gobierno central de identidades; este PATH estudia principalmente el lado consumidor.

## Linux / Fedora / RHEL
- Fedora Documentation.
- Red Hat Enterprise Linux Documentation.
- systemd manual pages y documentación oficial.
- firewalld documentation.
- SELinux documentation y man pages de políticas aplicables.

## Protocolos y estándares
Usar RFC y estándares IETF como referencia normativa cuando corresponda, especialmente para:
- HTTP semantics.
- HTTP caching.
- HTTP CONNECT.
- Forwarded header.
- HTTP/2.
- HTTP/3 y QUIC a nivel conceptual.
- TLS.
- ALPN.
- VRRP para IPv4/IPv6.

## Libros de apoyo
- Michael W. Lucas — *Networking for Systems Administrators*.
- Michael W. Lucas — *TLS Mastery*.
- Ivan Ristić — *Bulletproof TLS and PKI*.
- Brendan Gregg — *Systems Performance: Enterprise and the Cloud*, 2nd Edition.
- Brendan Gregg — *BPF Performance Tools* como ampliación para diagnóstico avanzado Linux.

## Observabilidad
- Prometheus — Official Documentation.
- Grafana — Official Documentation.
- Documentación de exporters/integraciones utilizadas para HAProxy/Nginx cuando corresponda.

## Herramientas de diagnóstico
Consultar documentación oficial y páginas man de:
- curl
- OpenSSL
- iproute2 / ss
- lsof
- tcpdump
- Wireshark / tshark
- dig
- journalctl
- ausearch

## Criterio bibliográfico
La documentación oficial de cada producto y versión tiene prioridad sobre libros, blogs y ejemplos antiguos. El comportamiento de proxies y balanceadores cambia entre versiones y algunas características dependen de edición, build, módulos compilados o empaquetado de la distribución.
