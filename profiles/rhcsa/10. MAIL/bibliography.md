# Bibliography — MAIL

## Documentación principal

### Postfix
- Postfix Documentation — documentación oficial del proyecto Postfix.
- Postfix Standard Configuration Examples.
- Postfix Address Rewriting.
- Postfix SMTP Access Policy Delegation.
- Postfix SASL Howto.
- Postfix TLS Support.
- Postfix Virtual Domain Hosting Howto.

### Dovecot
- Dovecot Documentation — documentación oficial.
- Dovecot Authentication.
- Dovecot LMTP.
- Dovecot Mail Location.
- Dovecot SSL/TLS.
- Dovecot Administration / doveadm documentation.

### Fedora / Red Hat
- Fedora Documentation.
- Red Hat Enterprise Linux documentation relativa a networking, systemd, SELinux, firewalld, TLS y servicios de infraestructura.
- man pages instaladas por Postfix, Dovecot, OpenSSL, systemd, firewalld y herramientas de red.

## IAM e integración de identidad
- Documentación oficial de FreeIPA — arquitectura, usuarios, grupos, Kerberos, LDAP, service principals y keytabs.
- MIT Kerberos Documentation — principals, tickets, keytabs, GSSAPI y operación del KDC.
- OpenLDAP Documentation / Administrator's Guide — directorio, bind, search, ACL y TLS.
- SSSD Documentation — integración de identidad/autenticación y resolución de usuarios cuando corresponda.
- Linux-PAM documentation y man pages — integración PAM cuando el diseño de autenticación la utilice.
- Dovecot Documentation — Authentication, LDAP, PAM, passdb/userdb y mecanismos SASL.
- Postfix Documentation — LDAP tables/maps y SASL, cuando se utilicen como consumidores de datos o autenticación centralizada.

## Libros

### Postfix y correo Linux
- Kyle D. Dent — Postfix: The Definitive Guide. O'Reilly Media.
- Ralf Hildebrandt, Patrick Koetter — The Book of Postfix: State-of-the-Art Message Transport. No Starch Press.
- Peer Heinlein, Peer Hartleben — The Book of IMAP: Building a Mail Server with Courier and Cyrus. No Starch Press. Utilizar principalmente como referencia conceptual e histórica de IMAP.

### Protocolos y arquitectura de Internet
- Douglas E. Comer — Internetworking with TCP/IP. Referencia complementaria para TCP/IP y arquitectura de red.
- Michael W. Lucas — DNSSEC Mastery. Referencia complementaria para DNSSEC.

## RFC y estándares esenciales

### SMTP y formato de mensajes
- RFC 5321 — Simple Mail Transfer Protocol.
- RFC 5322 — Internet Message Format.
- RFC 6409 — Message Submission for Mail.
- RFC 6531 — SMTP Extension for Internationalized Email.
- RFC 3461 — SMTP Service Extension for Delivery Status Notifications.

### MIME
- RFC 2045 — MIME Part One: Format of Internet Message Bodies.
- RFC 2046 — MIME Part Two: Media Types.
- RFC 2047 — MIME Part Three: Message Header Extensions.

### IMAP
- RFC 9051 — Internet Message Access Protocol (IMAP) Version 4rev2.
- RFC 3501 — IMAP4rev1, como referencia histórica y de compatibilidad.

### TLS y transporte
- RFC 3207 — SMTP Service Extension for Secure SMTP over TLS.
- RFC 8314 — Cleartext Considered Obsolete: TLS for Email Submission and Access.
- RFC 8461 — SMTP MTA Strict Transport Security (MTA-STS).
- RFC 8460 — SMTP TLS Reporting.
- RFC 7672 — SMTP Security via Opportunistic DNS-Based Authentication of Named Entities (DANE) TLSA.

### SASL
- RFC 4422 — Simple Authentication and Security Layer (SASL).
- RFC 4954 — SMTP Service Extension for Authentication.

### SPF
- RFC 7208 — Sender Policy Framework (SPF).

### DKIM
- RFC 6376 — DomainKeys Identified Mail (DKIM) Signatures.
- RFC 8301 — Cryptographic Algorithm and Key Usage Update to DKIM.

### DMARC
- RFC 7489 — Domain-based Message Authentication, Reporting, and Conformance (DMARC), como especificación ampliamente desplegada y referencia histórica.
- RFC 9989 — DMARC: protocolo vigente; sustituye RFC 7489 y RFC 9091.
- RFC 9990 — DMARC Aggregate Reporting.
- RFC 9991 — DMARC Failure Reporting.
- IANA DMARC Parameters — registro vigente de etiquetas; pct figura como histórico.

### ARC
- RFC 8617 — The Authenticated Received Chain (ARC) Protocol.

## Herramientas
- OpenSSL documentation and man pages.
- swaks documentation.
- tcpdump man pages.
- Wireshark/tshark documentation.
- BIND utilities documentation para dig/host.
- systemd/journalctl man pages.
- firewalld documentation.
- SELinux user and administrator documentation.

## Criterio de uso de fuentes
Las RFC y documentación oficial constituyen la fuente primaria para comportamiento de protocolos y configuración actual. Los libros se utilizan para desarrollar intuición, arquitectura y contexto, pero una configuración concreta debe contrastarse con la documentación correspondiente a la versión instalada en Fedora/RHEL.

## Fuentes operativas con enlaces
- [Postfix SASL Howto](https://www.postfix.org/SASL_README.html): Dovecot SASL, cliente SMTP, mapas de remitente y autorización del sobre.
- [Postfix Configuration Parameters](https://www.postfix.org/postconf.5.html): consultar cada parámetro contra la versión instalada.
- [Postfix SMTP relay and access control](https://www.postfix.org/SMTPD_ACCESS_README.html): relay y restricciones.
- [Dovecot CE: documentación publicada](https://doc.dovecot.org/latest/): autenticación, userdb/passdb, LMTP, quotas, ACL, namespaces y comandos doveadm.
- [Dovecot: migración 2.3 a 2.4](https://doc.dovecot.org/2.4.2/installation/upgrade/2.3-to-2.4.html): cambios de sintaxis, mail_location y retirada de replicator/Director.
- [Dovecot Kerberos/GSSAPI](https://doc.dovecot.org/2.4.5/core/config/auth/mechanisms/kerberos.html): tickets, keytabs y necesidad de userdb.
- [Dovecot PAM](https://doc.dovecot.org/2.4.0/core/config/auth/databases/pam.html): límites y mecanismos compatibles; PAM no es userdb.
- [Dovecot ManageSieve](https://doc.dovecot.org/2.4.5/core/config/sieve/managesieve.html): configuración del servicio; consultar también Sieve/Pigeonhole para ejecución durante entrega.
- [Rspamd Documentation](https://docs.rspamd.com/): instalación, integración milter, Redis por módulo, rspamc, scoring, Bayes y firma DKIM.
- [FreeIPA Documentation](https://www.freeipa.org/page/Documentation): principals, keytabs, políticas y modelo de identidad.
- [SSSD Documentation](https://sssd.io/docs/): PAM/NSS, caché y diagnóstico.
- [RFC 9989](https://www.rfc-editor.org/rfc/rfc9989.html): DMARC vigente.
- [RFC 9990](https://www.rfc-editor.org/rfc/rfc9990.html): informes agregados DMARC.
- [RFC 9991](https://www.rfc-editor.org/rfc/rfc9991.html): informes de fallos DMARC.
- [IANA DMARC Parameters](https://www.iana.org/assignments/dmarc-parameters): etiquetas activas e históricas.
- RFC 5228 — Sieve: An Email Filtering Language.
- RFC 5804 — A Protocol for Remotely Managing Sieve Scripts.
- RFC 5230 — Sieve Email Filtering: Vacation Extension.
- RFC 4314 — IMAP4 Access Control List (ACL) Extension.
- RFC 7628 — SASL OAuth mechanisms, como ampliación conceptual opcional.

## Selección de fuentes por laboratorio
Registrar fecha de consulta, versión instalada y URL de la rama correspondiente.
Los enlaces latest sirven para localizar documentación: no autorizan a copiar
sintaxis de una rama distinta a la del paquete. Los libros existentes se conservan
como apoyo conceptual; los ejemplos actuales se contrastan con fuentes primarias.
