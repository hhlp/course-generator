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

## Referencias enlazadas para las ampliaciones

Consulta de la revisión: 23 de octubre de 2026. Las páginas sin versión fija
pueden evolucionar; registrar en cada laboratorio versión RPM, build/módulos,
edición y enlace del manual específico utilizado. Esta lista no declara que
todas las funciones estén disponibles en todos los paquetes Fedora/RHEL.

### Squid: autenticación y ACL
- [auth_param: referencia oficial y restricciones intercept/tproxy](https://www.squid-cache.org/Doc/config/auth_param/).
- [acl: referencia oficial](https://www.squid-cache.org/Doc/config/acl/).
- [Proxy Authentication: helpers, Basic y modos de interceptación](https://wiki.squid-cache.org/Features/Authentication).
- [Manuales de Squid y helpers](https://www.squid-cache.org/Doc/man/).
  Seleccionar helpers de autenticación y autorización por grupos realmente
  instalados; no deducir rutas de ejecutables a partir de ejemplos antiguos.

### Nginx: autenticación delegada, caché y reintentos
- [ngx_http_auth_request_module](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html):
  disponibilidad del módulo y semántica 2xx/401/403 de las subrequests.
- [Autenticación mediante servicio externo](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-subrequest-authentication/):
  integración con autenticador externo y verificación del build.
- [ngx_http_proxy_module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html):
  proxy_cache, bypass/no_cache, revalidación, stale y proxy_next_upstream.
- [ngx_http_upstream_module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html):
  algoritmos, fallos y capacidades por edición/versión.
- [ngx_http_realip_module](https://nginx.org/en/docs/http/ngx_http_realip_module.html):
  confianza en proxies e IP del cliente.
- [ngx_stream_core_module](https://nginx.org/en/docs/stream/ngx_stream_core_module.html):
  contexto stream, TCP/UDP y soporte de PROXY protocol.

### HAProxy: operación y estado
- [Manuales oficiales por rama](https://www.haproxy.org/#docs):
  seleccionar la rama del binario instalado para configuración y gestión.
- [Stick tables y peers](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/proxying-essentials/custom-rules/stick-tables/).
- [Runtime API: show peers](https://www.haproxy.com/documentation/haproxy-runtime-api/reference/show-peers/).
- [Preservar stick tables durante reload](https://www.haproxy.com/blog/preserve-stick-table-data-when-reloading-haproxy):
  artículo técnico del fabricante; no extrapolar la recarga a un restart completo.

### Keepalived, IAM y protocolos
- [Keepalived: documentación oficial](https://www.keepalived.org/documentation/)
  y keepalived.conf(5) de la versión instalada.
- [FreeIPA: documentación oficial](https://www.freeipa.org/page/Documentation).
- [MIT Kerberos: documentación oficial](https://web.mit.edu/kerberos/krb5-latest/doc/).
- [OpenLDAP: documentación oficial](https://www.openldap.org/doc/).
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110):
  CONNECT, autenticación, métodos e idempotencia.
- [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111):
  cachés compartidas, validación y contenido autenticado.
- [RFC 7239: Forwarded](https://www.rfc-editor.org/rfc/rfc7239):
  transmisión de información del cliente y límites de confianza.
- [RFC 9568: VRRP Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568):
  referencia normativa; comprobar compatibilidad de la implementación usada.

## Uso por bloque
| Bloques | Fuente prioritaria |
|---|---|
| 0–3 | HTTP Semantics, HTTP Caching, manuales de los productos |
| 4–9 | Squid, helpers instalados, MIT Kerberos y FreeIPA |
| 10–14 | Módulos oficiales Nginx y guía de autenticación externa |
| 15–21 | Manual HAProxy de la rama instalada y Runtime API |
| 22 | Keepalived, man local y VRRP |
| 23–27 | Fuentes anteriores y documentación Fedora/RHEL aplicable |

Los libros de apoyo originales se conservan como ampliación conceptual.
Las recetas de versiones antiguas deben contrastarse con los manuales actuales.
