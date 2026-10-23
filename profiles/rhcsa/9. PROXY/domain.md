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

## Ampliación de la revisión: integración y operación verificable

Se conservan los 28 bloques originales y sus 540 lecciones. Las ampliaciones
se añaden al final de cada bloque para conservar referencias existentes.

### Itinerarios y dependencias
- Base común: RHCSA, TCP/IP, HTTP y TLS en el nivel requerido por la práctica.
- Itinerario sin IAM: ACL de red, reverse proxy, balanceo y HA independientes.
- Itinerario con IAM: proveedor central preparado en su PATH; DNS y tiempo
  operativos antes de Kerberos; confianza TLS antes de LDAP protegido.
- Squid consume usuarios/grupos centrales. El navegador obtiene tickets del KDC
  y Squid valida el ticket de servicio con su keytab; no describir cada petición
  como una consulta obligatoria de Squid al KDC. La autorización de grupos puede
  requerir otro helper/directorio y tiene sus propias reglas de caché.
- Nginx puede delegar mediante auth_request a un servicio autenticador externo.
  El módulo decide a partir de una subrequest; no implementa por sí solo un
  proveedor LDAP/Kerberos/OIDC. Verificar módulo, protocolo y servicio elegido.
- HAProxy y Keepalived no requieren identidad humana para el flujo de balanceo
  habitual. La gestión del host puede consumir IAM por un circuito independiente.

### Autenticación y límites de confianza
La autenticación de proxy Squid requiere proxy explícito y no se habilita en
puertos intercept/tproxy. Diferenciar 407 y Proxy-Authorization de 401 y
Authorization. Basic es codificación, no cifrado: proteger por separado el
tramo cliente–proxy y el tramo proxy–LDAP. CONNECT hacia HTTPS no transforma
automáticamente el primer tramo en TLS. El laboratorio LDAP debe usar TLS
verificado y un transporte cliente–proxy protegido compatible con el cliente;
si no existe, estudiar el flujo sin enviar credenciales reales.

En Kerberos, validar FQDN, SPN, tickets, keytab y permisos, además de DNS/tiempo.
Los secretos de servicio son entregados por el proveedor IAM con privilegio
mínimo. No crear usuarios centrales en este PATH ni guardar secretos en logs.

En Nginx, incluir ruta pública y ruta protegida, servicio autenticador externo,
respuestas permitidas/denegadas, fallo del autenticador y cabeceras de identidad
establecidas solo tras validación. El backend no debe admitir acceso directo
que evite el control. Fallar de forma cerrada en los recursos protegidos.

### Caché, reintentos y protocolos
Desarrollar proxy_cache en Nginx: claves, Vary, bypass, exclusión de escritura,
cookies, Authorization, revalidación, lock y uso controlado de contenido obsoleto.
Probar con dos identidades que no se comparten respuestas privadas. Distinguir
funciones nativas de opciones comerciales o módulos adicionales.

Enseñar reintentos con presupuesto de tiempo y pruebas de idempotencia: una
petición fallida puede haber modificado ya el backend. No activar repetición
de escrituras de forma indiscriminada. Cubrir PROXY protocol e IP real con
emisores explícitamente confiables; añadir SSE y conexiones prolongadas.

### HA y estado
Estudiar peers y stick tables de HAProxy, incluyendo transferencia entre procesos
durante reload y límites ante restart/fallo. Diferenciar configuración persistente,
cambios runtime, certificados, contadores y estado de aplicación. No prometer que
VRRP conserva conexiones TCP existentes: medir reconexión desde el cliente.
Documentar protocolo IP 112, unicast/multicast, restricciones del entorno, binds
de la VIP, preemption/failback, particiones y recuperación de doble MASTER.

### Contrato de laboratorio y entregables del curso
Cada práctica generada incluirá topología, inventario, versiones/build, archivos
comentados, comandos explicados, resultado esperado, pruebas positivas/negativas,
capturas o logs saneados, fallo inducido, recuperación, limpieza y rollback.
Comprobar cliente, intermediario y backend. Medir disponibilidad/recuperación y
demostrar autorización correcta, ausencia de bypass y aislamiento de caché.
Estos cuatro archivos describen el currículo para course-generator; no equivalen
a un despliegue ejecutado ni a un paquete de scripts de infraestructura.

La integración con WEB SERVER reutiliza backends y aplicaciones de aquel PATH;
este desarrolla intermediación, políticas, balanceo, disponibilidad y diagnóstico.
La documentación oficial correspondiente a la versión instalada prevalece.
