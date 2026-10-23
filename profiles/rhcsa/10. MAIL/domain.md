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

## Secuencia y variantes de identidad
Se mantiene toda la cobertura original y se reorganiza la secuencia: Postfix y
SASL, TLS, IMAP, Dovecot, almacenamiento e integración LMTP preceden a Sieve y
al bloque de IAM. Autenticación SMTP de usuarios y autenticación del cliente
Postfix hacia un smarthost se enseñan por separado.

En la variante autónoma se estudian usuarios locales y virtuales. En la variante
centralizada los usuarios humanos y sus credenciales se administran en IAM.
Mail consume las identidades y mantiene sus datos operativos: mensajes, índices,
reglas Sieve, ACL y metadatos del buzón. Una cuenta técnica vmail no representa
una nueva fuente de identidades humanas.

## Contrato entre IAM y Mail
Documentar origen, formato, propietario, consulta y actualización de: login,
dirección principal, aliases, grupos, habilitación de correo, UID/GID, home,
ruta y cuota. Un atributo puede resolverse desde IAM o una política Mail
explícita; no se supone que FreeIPA proporcione un esquema completo de buzones.
Las búsquedas LDAP se limitan con filtros, ACL y cuenta de servicio de sólo
lectura. No se presupone acceso a hashes de contraseñas del proveedor.

Distinguir tres diseños: autenticación con contraseña por PAM/SSSD; consultas o
binds LDAP protegidos; autenticación Kerberos/GSSAPI con tickets y clientes
compatibles. GSSAPI sigue necesitando userdb para resolver el buzón. Verificar
principals imap/smtp, keytabs, permisos, resolución DNS y sincronización horaria.
PAM no sustituye userdb. HBAC sólo se aplica donde el servicio PAM y la política
lo integren y se haya comprobado el resultado.

Autenticar no habilita automáticamente acceso a Mail ni autoriza cualquier
remitente. Enseñar habilitación por grupo/atributo, MAIL FROM frente a identidad
SASL y política separada del encabezado From. Las ACL de buzones compartidos no
equivalen al permiso para enviar como otra dirección.

En altas y bajas verificar primer acceso, aprovisionamiento del directorio del
buzón, revocación de nuevas sesiones, sesiones existentes, cachés y retención.
Ante caída de IAM probar por separado SMTP AUTH, IMAP, consulta de destinatarios
y entrega LMTP. No asumir que la caché SSSD cubre LDAP directo o GSSAPI; distinguir
error temporal de backend de credenciales inválidas o destinatario inexistente.

## Compatibilidad y actualización
Registrar versiones y características compiladas antes de aplicar ejemplos.
Dovecot 2.3 y 2.4 requieren ejemplos diferenciados: mail_location en 2.3 frente
a mail_driver/mail_path y otros ajustes en 2.4. Enseñar los parámetros de versión
de configuración y almacenamiento exigidos por 2.4. No mezclar plugins ni
configuraciones entre ramas sin una validación explícita.

En Dovecot CE 2.4 se retiraron replicator y Director. doveadm sync/backup sirve
para sincronización y migración; no constituye por sí solo HA automática.
Estudiar HA con almacenamiento y consistencia, fencing, pruebas de pérdida de
nodo y plan de reversión según arquitectura soportada. Múltiples MX no replican
la cola de un servidor que ya aceptó un mensaje.

DMARC usa RFC 9989, 9990 y 9991 como referencias actuales, manteniendo RFC 7489
para compatibilidad histórica. Tratar pct como histórico; estudiar descubrimiento
de política, np, psd y t, informes y diferencias de implementación.

## Funciones de buzón y filtrado
Incluir Pigeonhole/Sieve, ejecución durante LMTP/LDA, ManageSieve sobre TLS,
reglas globales/personales, vacaciones, pruebas y diagnóstico. Incluir namespaces,
buzones compartidos, ACL y validación de permisos con identidades distintas.
Rspamd requiere instalación, integración milter, configuración validada,
dependencias por módulo, scoring, aprendizaje y tratamiento de falsos positivos.
Elegir un responsable de firma DKIM entre OpenDKIM y Rspamd cuando se solapen.

## Laboratorio privado reproducible
Topología mínima: DNS interno, servidor Postfix/Dovecot, cliente y segundo MTA
para intercambio controlado. IAM se añade en una instancia separada para la
variante centralizada. Usar red privada, mail.test y peer.test, registros directos,
inversos, MX y TXT internos, CA de laboratorio y reloj sincronizado.

La ruta privada permite probar SMTP, Submission, IMAP, LMTP, SPF, DKIM, DMARC,
antispam, Sieve, ACL, fallos IAM y recuperación con receptores bajo control.
No demuestra reputación ni aceptación por proveedores públicos. La extensión
pública requiere dominio delegado, PTR gestionable, conectividad SMTP y
certificados adecuados; evaluar estas condiciones antes de esa variante.

Cada laboratorio debe proporcionar al generar las lecciones: inventario y
versiones, archivos de configuración completos con rutas, comandos por host,
validación previa a recarga, pruebas positivas/negativas, logs esperados,
criterios de éxito, limpieza y reversión. Estos cuatro archivos definen el curso;
no son por sí mismos scripts de despliegue ni configuraciones ejecutables.

## Evidencia mínima del proyecto
- Mensaje trazado de Submission a IMAP y entre dos MTA.
- Relay anónimo externo bloqueado y destinatario inexistente rechazado a tiempo.
- Usuario autenticado sin permiso Mail y remitente no autorizado denegados.
- Alta y baja centralizadas sin contraseñas humanas duplicadas en Mail.
- Cuota, regla Sieve y ACL de buzón compartido verificadas.
- Caída IAM y del filtro con comportamiento temporal y recuperación documentados.
- Backup restaurado con mensajes y metadatos comprobados.
- Prueba de fallo tras aceptación SMTP y localización del mensaje aceptado.
- Matriz de versiones, configuración efectiva, runbook y plan de reversión.
