# Domain — Web Servers

## Dominio
Administración de infraestructura web en Fedora/RHEL con Apache HTTP Server, Nginx, PHP-FPM y HAProxy.

## Alcance
El curso cubre fundamentos HTTP/HTTPS; instalación y operación; virtual hosting/server blocks; contenido estático y dinámico; PHP-FPM; reverse proxy; load balancing; TLS/PKI aplicada; caching; seguridad; SELinux; firewalld; systemd; journald; logs; rendimiento; observabilidad; automatización con Ansible; alta disponibilidad web introductoria; operación autónoma sin IAM; integración opcional como consumidor de LDAP, Kerberos y FreeIPA; y troubleshooting por capas.

## Plataforma objetivo
- Fedora y Red Hat Enterprise Linux.
- systemd + journald.
- firewalld.
- SELinux enforcing.
- Apache HTTP Server (`httpd`).
- Nginx.
- PHP-FPM.
- HAProxy.

## Principios didácticos
Cada tecnología se estudia en el orden: concepto → instalación → configuración → validación → servicio → logs → seguridad → laboratorio → fallo intencionado → troubleshooting. Se prioriza comprender por qué funciona una configuración y diagnosticarla antes que memorizar recetas.

## Profundidad esperada
El alumno termina capaz de diseñar, desplegar, asegurar, observar, optimizar y diagnosticar una infraestructura web multicapa, diferenciando claramente web server, application runtime, reverse proxy y load balancer. También distingue un servidor web autónomo de un consumidor de IAM y sabe integrar autenticación centralizada sin convertir el PATH Web Servers en proveedor o administrador de identidades.

## Fuera de alcance principal
Desarrollo de aplicaciones web, frameworks PHP, programación frontend, WAF empresarial en profundidad, CDN comercial, Kubernetes ingress/gateway y clustering HA avanzado. Estos temas solo se introducen cuando ayudan a comprender la infraestructura web. La creación y administración central de usuarios, grupos, realms, directorios y políticas IAM pertenece al PATH IAM; aquí solo se estudia su consumo e integración desde servicios web.


## Prerrequisitos y orden de dependencias
El escenario autónomo requiere la base RHCSA y conocimientos de DNS y TLS; puede usar resolución local y una CA interna para el laboratorio. El escenario consumidor requiere además un proveedor IAM previamente desplegado, DNS coherente, sincronización horaria operativa y confianza en su CA. El orden de dependencia es DNS/TIME → IAM → integración web consumidora. No es necesario esperar a IAM para aprender publicación web autónoma.

## Contrato entre Web Servers e IAM
IAM administra usuarios, grupos, credenciales, realms, directorios y políticas centrales. En este PATH se consumen identidades existentes. El registro del servicio HTTP y la obtención o rotación de su keytab se estudian como operaciones de integración autorizadas y coordinadas con IAM. No se recrean usuarios humanos en cada servidor web. Las cuentas técnicas locales de httpd, nginx y PHP-FPM y los archivos htpasswd del laboratorio autónomo cumplen una función distinta.

Kerberos/SPNEGO es la práctica principal de SSO. LDAP sigue incluido como integración alternativa y fuente de autorización por grupos, con transporte protegido, permisos mínimos y estudio de cachés. Autenticar un principal no resuelve por sí solo la autorización por grupos. SSSD/PAM del host no autentica automáticamente las peticiones HTTP.

## Laboratorios de integración
1. Apache y Nginx autónomos: recurso público y recurso protegido mediante credenciales locales de laboratorio, siempre con HTTPS para Basic.
2. Apache consumidor: mod_auth_gssapi, principal HTTP del nombre público, keytab dedicado, cliente con ticket y validación SPNEGO.
3. Apache LDAP: configuración del proveedor, CA, cuenta de consulta cuando se necesite, autorización por grupos y pruebas de revocación/caché.
4. Nginx consumidor por delegación: auth_request con un servicio Apache/SPNEGO integrado con IAM. Comprobar módulos y soporte cliente antes del despliegue. La ruta de autorización será interna y se probará el intercambio Negotiate a través del nombre público.
5. HAProxy frontal: encaminamiento y balanceo, conservación del contrato de identidad y aislamiento de backends, sin asumir administración de identidades humanas.

Cada laboratorio especificará topología, versiones, puertos, paquetes y módulos disponibles; archivos de configuración completos; comandos; logs; resultados esperados; pruebas positivas/negativas; fallos y recuperación. Son requisitos para las lecciones generadas: estos cuatro archivos definen el currículo y no constituyen por sí mismos scripts ejecutables del laboratorio.

## Seguridad y compatibilidad operativa
Verificar CA, nombre y SNI en conexiones HTTPS al backend. El cifrado sin autenticación del servidor no satisface el objetivo del laboratorio. Limitar proxies confiables, sanear cabeceras de identidad, impedir acceso directo al backend y evitar que cachés compartan respuestas privadas. No registrar Authorization, contraseñas, keytabs ni cookies de sesión.

No asumir uniformidad entre Fedora y RHEL: documentar versión, repositorios, módulos y opciones compiladas. Diferenciar Nginx Open Source de funciones comerciales. HTTP/3 queda condicionado a soporte real de servidor, biblioteca TLS, cliente y red UDP. OCSP stapling depende de la CA y del certificado: Let’s Encrypt cerró su responder OCSP el 6 de agosto de 2025; estudiar también CRL y no exigir stapling donde no aplica.

## Criterios de aceptación del proyecto final
Conservar toda la plataforma multicapa original y entregar dos variantes comparables: autónoma y consumidora de IAM. Incluir Apache/SPNEGO y Nginx/auth_request, autorización por grupos con fuente explícita, pruebas de usuario permitido/denegado, cambio de grupo, tickets/cachés, caída del autenticador y recuperación. Rechazar cabeceras falsificadas, acceso directo al backend y certificados backend inválidos. Entregar configuración reproducible, evidencias de pruebas, diagrama, versiones, matriz de dependencias y runbook sin secretos.

## Relación con otros PATH
El PATH Proxy/LB desarrolla proxying y balanceo transversal con mayor profundidad; aquí se aplican a publicación web. IAM administra el proveedor central. DNS y TIME proporcionan dependencias de infraestructura. Observabilidad desarrolla las plataformas de métricas y logs; aquí se practica su instrumentación operativa básica. HA avanzada mantiene su PATH propio sin eliminar el laboratorio de disponibilidad web.
