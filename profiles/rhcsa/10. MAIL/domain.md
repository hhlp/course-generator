# Domain — MAIL

## Dominio
Administración avanzada de infraestructura de correo electrónico en Linux, con orientación principal a Fedora/RHEL.

## Alcance
El curso cubre el ciclo completo del correo electrónico desde la resolución DNS y la conversación SMTP hasta la entrega, almacenamiento y acceso IMAP. El stack principal está formado por Postfix y Dovecot, complementado con SASL, TLS, SPF, DKIM, DMARC y mecanismos modernos de seguridad y autenticación del dominio. Además, diferencia explícitamente el funcionamiento autónomo con identidades locales/virtuales del funcionamiento como consumidor de un IAM centralizado basado en LDAP, Kerberos y FreeIPA.

## Objetivo técnico
Al finalizar, el estudiante debe poder diseñar, instalar, configurar, securizar, operar, monitorizar y diagnosticar una infraestructura de correo basada en Linux, entendiendo no sólo qué parámetros configurar sino cómo fluye internamente cada mensaje y cómo localizar fallos de extremo a extremo.

## Plataforma principal
- Fedora Linux
- Red Hat Enterprise Linux y sistemas compatibles cuando corresponda
- systemd
- journald
- firewalld
- SELinux
- RPM/DNF

## Tecnologías principales
- SMTP / ESMTP
- Message Submission
- IMAP
- MIME
- DNS aplicado al correo
- Postfix
- Dovecot
- SASL
- TLS / X.509
- SPF
- DKIM
- DMARC
- ARC
- SRS
- MTA-STS
- TLS-RPT
- DANE/TLSA
- OpenDKIM
- SpamAssassin / Rspamd como tecnologías antispam de estudio
- Prometheus / Grafana para observabilidad
- HAProxy en escenarios de alta disponibilidad
- LDAP / Kerberos / FreeIPA como IAM central consumido por el stack mail cuando corresponda
- SSSD / PAM como capas de integración cuando el diseño las requiera

## Competencias
El estudiante aprenderá a:

1. Explicar MUA, MSA, MTA y MDA y reconstruir el recorrido completo de un mensaje.
2. Analizar manualmente sesiones SMTP e IMAP.
3. Diseñar los registros DNS necesarios para un dominio de correo.
4. Instalar y administrar Postfix en Fedora/RHEL.
5. Comprender la arquitectura interna y las queues de Postfix.
6. Configurar routing, aliases, virtual domains, restrictions y authenticated relay.
7. Instalar y administrar Dovecot.
8. Implementar Maildir, IMAP, LMTP y autenticación SASL.
9. Implementar TLS correctamente para SMTP, Submission e IMAP.
10. Diseñar y diagnosticar SPF, DKIM y DMARC.
11. Comprender forwarding, SRS, ARC, MTA-STS, TLS-RPT y DANE.
12. Aplicar controles antispam y hardening defensivo.
13. Integrar correctamente firewalld y SELinux.
14. Encontrar y analizar logs mediante journald/rsyslog y correlacionar Queue ID y Message-ID.
15. Diagnosticar fallos mediante dig, openssl, swaks, nc, ss, tcpdump y tshark.
16. Diseñar monitorización, backups, recuperación y alta disponibilidad.
17. Operar el servicio siguiendo prácticas de deliverability y runbooks.
18. Diseñar Mail tanto sin IAM centralizado como integrado como consumidor de identidad central.
19. Integrar LDAP/Kerberos/FreeIPA y SSSD/PAM cuando corresponda, sin convertir Mail en proveedor de identidades.
20. Diagnosticar dependencias y fallos entre Postfix/Dovecot/SASL y el IAM central.
21. Construir y documentar un servidor mail completo como proyecto final.

## Filosofía didáctica
Cada tecnología se estudia en cinco capas:

Fundamentos → arquitectura interna → configuración → operación → troubleshooting.

Las lecciones prácticas deben priorizar inspección real del sistema, comandos reproducibles, lectura de logs y experimentos controlados. Las configuraciones no deben presentarse como recetas opacas: cada parámetro importante debe relacionarse con el protocolo, flujo o componente que modifica.

## Laboratorios
Los laboratorios deben incluir escenarios funcionales y escenarios deliberadamente rotos. El estudiante debe aprender tanto a construir el servicio como a diagnosticarlo.

Cuando sea posible, cada laboratorio debe incluir:
- objetivo;
- topología;
- requisitos;
- comandos;
- configuración;
- validación;
- logs relevantes;
- errores frecuentes;
- troubleshooting;
- criterios de éxito.

## Logging
Debe explicarse la diferencia entre journald y archivos de log tradicionales. No se debe asumir que todos los sistemas generan automáticamente `/var/log/maillog`; debe enseñarse a descubrir la configuración efectiva y, cuando corresponda, a enrutar eventos mediante rsyslog.

## Seguridad
El curso aborda seguridad desde una perspectiva defensiva y operacional: evitar open relay, proteger credenciales, TLS, autenticación, permisos, SELinux, firewalld, rate limiting, reputación, spoofing y mecanismos de autenticación del dominio.

## Resultado final
El estudiante debe ser capaz de recibir una incidencia como «el correo no llega», «el mensaje queda deferred», «SASL falla», «DKIM no valida» o «el destinatario rechaza por DMARC» y recorrer sistemáticamente DNS, red, TLS, SMTP, autenticación, queue, entrega, mailbox, políticas del dominio y logs hasta identificar la causa raíz.
