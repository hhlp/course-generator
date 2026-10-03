# Domain — Proxy / Load Balancing

## Dominio
Administración avanzada de proxies, reverse proxies y balanceadores de carga en Linux empresarial, con énfasis en Fedora/RHEL y en Squid, Nginx, HAProxy y Keepalived.

## Objetivo
Construir conocimiento desde los fundamentos de TCP/IP, HTTP y TLS hasta el diseño y operación de arquitecturas proxy/load-balancing seguras, observables, altamente disponibles y diagnosticables.

## Alcance principal
- Fundamentos de proxy, forward proxy y reverse proxy.
- Explicit proxy y transparent/intercept proxy.
- HTTP/HTTPS proxying y CONNECT.
- ACL, autenticación, filtering y caching.
- Funcionamiento de Proxy/LB sin IAM y criterios para decidir cuándo integrar identidad centralizada.
- Squid como consumidor de IAM mediante LDAP/Kerberos/SPNEGO/FreeIPA, sin duplicar la administración propia del proveedor IAM.
- Distinción entre identidad humana, identidad de servicio/máquina y controles puramente de red.
- Squid como forward proxy.
- Nginx como reverse proxy y balanceador HTTP/TCP según capacidades disponibles.
- HAProxy como proxy/balanceador L4 y L7.
- Algoritmos de load balancing y persistencia.
- Active/passive health checking según producto/capacidad.
- TLS termination, passthrough, re-encryption y mTLS.
- Alta disponibilidad con HAProxy + Keepalived/VRRP.
- Logging, métricas y observabilidad.
- Integración conceptual y práctica con Prometheus/Grafana.
- Rendimiento, capacidad y benchmarking.
- Seguridad y hardening.
- Troubleshooting por capas.
- Diseño de arquitecturas de producción.

## Plataforma
Prioridad práctica:
- Fedora actual.
- Red Hat Enterprise Linux y derivados compatibles cuando proceda.
- systemd.
- firewalld.
- SELinux en enforcing.
- DNF/RPM.

Las diferencias de versión o de edición de Squid, Nginx y HAProxy deben indicarse explícitamente cuando una función no esté disponible de forma equivalente en todos los paquetes/distribuciones.

## Enfoque didáctico
Cada tecnología debe estudiarse mediante la secuencia:

concepto → arquitectura → instalación → configuración → validación → operación → logs → seguridad → observabilidad → fallo inducido → troubleshooting → laboratorio.

No limitar el aprendizaje a copiar archivos de configuración. Explicar por qué funciona cada directiva y qué ocurre en la red.

## Laboratorios
Los laboratorios deben emplear múltiples hosts/VMs/contenedores cuando sea útil para representar:
- clientes;
- proxies;
- load balancers;
- backends;
- DNS;
- observabilidad.

Cada laboratorio debe incluir comprobaciones desde cliente, proxy/load balancer y backend.

## Troubleshooting
El diagnóstico debe seguir una metodología por capas:

cliente → DNS → routing → firewall → SELinux → socket TCP/UDP → proxy/load balancer → TLS → HTTP → backend → aplicación.

Herramientas prioritarias:
- systemctl
- journalctl
- ss
- lsof
- curl
- openssl
- dig
- tcpdump
- tshark
- ausearch

Los logs específicos de Squid, Nginx y HAProxy deben estudiarse tanto en condiciones normales como ante fallos inducidos.

## Seguridad
Todo ejemplo debe evitar por defecto configuraciones inseguras de producción. Deben estudiarse explícitamente:
- open proxies;
- confianza de Forwarded/X-Forwarded-*;
- TLS y PKI;
- mTLS;
- ACL;
- autenticación;
- integración segura con IAM cuando exista una necesidad de identidad humana;
- protección de principals, keytabs y credenciales de servicio;
- rate/connection limiting;
- segmentación;
- SELinux;
- firewalld;
- secretos y claves privadas;
- hardening de servicios;
- fundamentos defensivos de ataques HTTP relevantes para proxies.

## Observabilidad
Distinguir:
- logs;
- métricas;
- health checks;
- estado runtime;
- latencia;
- throughput;
- errores;
- saturación;
- disponibilidad.

Relacionar estos datos con los PATH independientes de Logging, Prometheus y Grafana sin duplicarlos completamente.

## Límites
No convertir el curso en un curso completo de:
- TCP/IP;
- DNS;
- PKI/TLS;
- SELinux;
- firewalld;
- Prometheus/Grafana;
- servidores web;
- IAM/LDAP/Kerberos/FreeIPA como disciplina completa.

Esos conocimientos se reutilizan y se profundizan únicamente donde afectan directamente a proxy/load balancing. En IAM, el curso debe enseñar el lado consumidor: integración, flujo de autenticación/autorización, dependencias, logs y troubleshooting; la creación y gobierno central de identidades pertenece al PATH IAM.

## Resultado esperado
Al finalizar, el estudiante debe poder instalar, configurar, asegurar, observar y diagnosticar Squid, Nginx y HAProxy; implementar alta disponibilidad; analizar tráfico y logs; seleccionar arquitecturas adecuadas según requisitos técnicos; decidir justificadamente cuándo Proxy/LB debe operar sin IAM o consumir un IAM central; integrar Squid con identidad centralizada cuando corresponda; y operar una plataforma proxy/load-balancing con criterios de producción.
