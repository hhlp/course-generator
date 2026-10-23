# Bibliography — Web Servers

Revisión: 2026-10-23. La sintaxis y las funciones se contrastarán con la versión instalada y la documentación correspondiente. Registrar versiones, repositorios y módulos antes de cada laboratorio.

## Documentación principal

- [Apache HTTP Server 2.4](https://httpd.apache.org/docs/2.4/): arquitectura, MPM, VirtualHost, módulos, TLS, proxy, logs y rendimiento. Referencia normativa de Apache para este PATH.
- [NGINX Documentation](https://nginx.org/en/docs/): configuración de server/location, FastCGI, proxy, TLS, upstreams y módulos. Comprobar versión y opciones mediante `nginx -V`; distinguir Nginx Open Source de funciones comerciales.
- [HAProxy Documentation](https://www.haproxy.org/#docs): Configuration Manual, Management Guide y Runtime API de la rama instalada; contrastar con `haproxy -vv`.
- [Red Hat Enterprise Linux Documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux): seleccionar versión de RHEL; servicios web, SELinux, firewalld, systemd y políticas criptográficas.
- [Fedora Documentation](https://docs.fedoraproject.org/): administración y empaquetado; no asumir que los módulos o valores del paquete coinciden con RHEL.
- [PHP Manual: FPM](https://www.php.net/manual/en/install.fpm.php): instalación, pools, configuración, slowlog y operación FastCGI de la versión instalada.
- [OpenSSL Documentation](https://docs.openssl.org/): herramientas, certificados y diagnóstico; elegir versión coincidente con el sistema.
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/): ACME, challenges y operación de certificados públicos.
- [Certbot Documentation](https://eff-certbot.readthedocs.io/en/stable/): emisión, renovación, pruebas y hooks; contrastar plugins y versión.

## Apache e IAM

- [Authentication and Authorization](https://httpd.apache.org/docs/2.4/howto/auth.html): tipos de autenticación, proveedores y autorización; distinguir usuario autenticado de usuario autorizado.
- [mod_authnz_ldap](https://httpd.apache.org/docs/2.4/mod/mod_authnz_ldap.html): búsqueda/bind, TLS y autorización por grupos.
- [mod_ldap](https://httpd.apache.org/docs/2.4/mod/mod_ldap.html): conexiones y cachés; estudiar demoras de propagación de cambios en grupos y credenciales.
- [mod_auth_gssapi, proyecto upstream](https://github.com/gssapi/mod_auth_gssapi): configuración de GSSAPI/SPNEGO y keytabs; seleccionar documentación compatible con el paquete instalado.
- [FreeIPA: autenticación y autorización web, taller](https://freeipa.readthedocs.io/en/latest/workshop/5-web-app-authnz.html): práctica Apache con mod_auth_gssapi. Reutilizar el proveedor IAM ya preparado.
- [FreeIPA: Web App Authentication](https://www.freeipa.org/page/Web_App_Authentication): patrones de integración y separación entre autenticación y atributos de identidad; contrastar los ejemplos históricos con versiones actuales.
- [MIT Kerberos Documentation](https://web.mit.edu/kerberos/krb5-latest/doc/): principals, tickets, keytabs, kvno y diagnóstico del cliente.
- [OpenLDAP Documentation](https://www.openldap.org/doc/): LDAP, TLS y herramientas de diagnóstico, como integración consumidora; la administración del directorio pertenece al PATH IAM.

## Nginx, proxy y límites de confianza

- [ngx_http_auth_request_module](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html): autorización delegada por subpetición; 2xx permite, 401/403 deniega y otros estados generan error. El módulo no se compila por defecto en upstream: comprobar el paquete instalado.
- [ngx_http_proxy_module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html): procesamiento de URI, cabeceras, buffering y TLS upstream. Estudiar expresamente `proxy_ssl_verify`, CA, hostname y SNI.
- [ngx_http_realip_module](https://nginx.org/en/docs/http/ngx_http_realip_module.html): IP cliente y proxies confiables; comprobar disponibilidad del módulo.
- [Apache mod_remoteip](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html): IP cliente original y límites de confianza.
- [Apache mod_proxy](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html): reverse proxy, conexiones y prevención de forward proxy abierto.
- [Apache mod_ssl](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html): TLS de entrada y verificación TLS hacia backends.

## Estándares y referencias HTTP/TLS

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110).
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111).
- [RFC 9112 — HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112).
- [RFC 9113 — HTTP/2](https://www.rfc-editor.org/rfc/rfc9113).
- [RFC 9114 — HTTP/3](https://www.rfc-editor.org/rfc/rfc9114).
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446).
- [RFC 7239 — Forwarded HTTP Extension](https://www.rfc-editor.org/rfc/rfc7239).
- [RFC 4559 — SPNEGO-based Kerberos and NTLM HTTP Authentication](https://www.rfc-editor.org/rfc/rfc4559): referencia informativa de HTTP Negotiate; este PATH practica Kerberos.
- [RFC 7617 — HTTP Basic Authentication](https://www.rfc-editor.org/rfc/rfc7617): estudiar junto con HTTPS.
- [RFC 8555 — ACME](https://www.rfc-editor.org/rfc/rfc8555).

## Revocación y vigencia operativa

- [Let's Encrypt: OCSP Service Has Reached End of Life](https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life/), 6 de agosto de 2025: cierre del responder OCSP y publicación de revocación mediante CRL. No presentar OCSP stapling como requisito universal ni exigirlo a certificados que no lo soportan.

## Libros complementarios

- Ben Laurie y Peter Laurie. [Apache: The Definitive Guide, 3.ª edición](https://www.oreilly.com/library/view/apache-the-definitive/0596002033/). O'Reilly Media, 2002. Referencia histórica y conceptual: cubre Apache 1.3/2.0; no usar sus directivas como configuración vigente de Apache 2.4.
- Derek DeJonghe. [NGINX Cookbook, 2.ª edición](https://www.oreilly.com/library/view/nginx-cookbook-2nd/9781098126230/). O'Reilly Media, 2022. Edición de referencia identificada, no afirmación de última edición; recetas de operación y proxy. Separar funciones de Open Source y NGINX Plus y contrastar la sintaxis actual.
- Ilya Grigorik. [High Performance Browser Networking](https://hpbn.co/). O'Reilly Media, 2013. Fundamentos de transporte y rendimiento; contrastar HTTP/2, HTTP/3 y TLS con sus RFC y documentación vigente.

## Mapa de lectura

| Bloques | Lecturas principales |
|---|---|
| 0 y 25–26 | RFC HTTP/TLS, OpenSSL y High Performance Browser Networking |
| 1–8 | Apache 2.4, mod_proxy, mod_ssl y documentación Fedora/RHEL |
| 9–16 | Nginx, PHP-FPM, módulos proxy y Cookbook como complemento |
| 17–22 | Manual de HAProxy instalado, proxy TLS y módulos Real IP |
| 23–26 | Manuales comparados, Fedora/RHEL y metodología de diagnóstico |
| 27 | FreeIPA, MIT Kerberos, mod_auth_gssapi, LDAP y auth_request |
| 28–33 | Referencias anteriores aplicadas a seguridad, fallos y proyecto |

## Criterio de uso

La documentación oficial y los RFC tienen prioridad para sintaxis y comportamiento vigente. Los libros se utilizan para explicación, arquitectura, ejercicios y contexto. Cada laboratorio debe citar la referencia aplicable a su versión, incluir comandos y configuración verificables y registrar sus limitaciones. Los servicios de identidad se preparan en el PATH IAM; Web Servers estudia su consumo sin duplicar usuarios centrales.
