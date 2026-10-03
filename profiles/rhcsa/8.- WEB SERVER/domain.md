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
