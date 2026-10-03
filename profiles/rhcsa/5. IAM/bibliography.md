# Bibliography — Identity & Access Management (IAM)

## Documentación principal

### Red Hat

- Red Hat Enterprise Linux — Configuring authentication and authorization.
- Red Hat Enterprise Linux — Managing systems using the RHEL identity management domain.
- Red Hat Enterprise Linux — Installing Identity Management.
- Red Hat Enterprise Linux — Configuring and managing Identity Management.
- Red Hat Enterprise Linux — Planning Identity Management.
- Red Hat Enterprise Linux — Integrating RHEL systems directly with Windows Active Directory.
- Red Hat Enterprise Linux — Security hardening.
- Red Hat Enterprise Linux — Using SELinux.
- Red Hat Enterprise Linux — Security auditing.

### FreeIPA

- FreeIPA Documentation.
- FreeIPA Design Documentation.
- FreeIPA Workshop material.
- FreeIPA troubleshooting documentation.

### SSSD

- SSSD official documentation.
- `sssd.conf(5)`.
- `sssctl(8)`.
- SSSD design pages and troubleshooting documentation.

### MIT Kerberos

- MIT Kerberos Documentation.
- Kerberos V5 System Administrator's Guide.
- Kerberos V5 Application Developer documentation.
- `krb5.conf(5)`.
- `kinit(1)`, `klist(1)`, `kvno(1)`, `kadmin(1)`.

### OpenLDAP

- OpenLDAP Administrator's Guide.
- OpenLDAP Software documentation.
- LDAP command manual pages: `ldapsearch`, `ldapadd`, `ldapmodify`, `ldapdelete`, `ldapwhoami`.

### Linux PAM

- Linux-PAM System Administrators' Guide.
- Linux-PAM Module Writers' Guide.
- `pam(8)`.
- `pam.d(5)`.
- Documentation for `pam_unix`, `pam_sss`, `pam_faillock`, `pam_pwquality`, `pam_limits` and `pam_access`.

### NSS / glibc

- GNU C Library documentation — Name Service Switch.
- `nsswitch.conf(5)`.
- `getent(1)`.

### sudo

- sudo official documentation.
- `sudo(8)`.
- `sudoers(5)`.
- `visudo(8)`.
- sudo logging and I/O logging documentation.

### 389 Directory Server

- 389 Directory Server Documentation.
- Administration and troubleshooting documentation.
- Replication and security documentation.

### Dogtag / PKI

- Dogtag Certificate System documentation.
- Red Hat Certificate System documentation where relevant.

## Integración de servicios consumidores

Para el bloque Provider → Consumer se utilizará documentación oficial específica de cada integración, sin convertir este PATH en sustituto de los cursos de cada servicio:

- Red Hat documentation — SSSD, PAM, Kerberos/GSSAPI and IdM client integration.
- OpenSSH documentation — PAM and GSSAPI authentication.
- NFS documentation — NFSv4 with RPCSEC_GSS/Kerberos (`krb5`, `krb5i`, `krb5p`).
- Samba documentation — centralized identity and Kerberos integration.
- Squid documentation — LDAP and Negotiate/Kerberos authentication helpers.
- Dovecot documentation — LDAP, PAM and authentication backends.
- Postfix/SASL documentation — directory and SASL integration where applicable.
- Apache HTTP Server documentation — LDAP and GSSAPI authentication modules.
- Nginx documentation — authentication integration patterns and architectural limitations.
- OpenVPN documentation — PAM/plugin, certificate and external identity integration.
- WireGuard documentation — peer public-key identity model, explicitly distinguished from user IAM.

## Libros recomendados

### LDAP

- Gerald Carter — *LDAP System Administration*, O'Reilly Media.
- Brian Arkills — *LDAP Directories Explained: An Introduction and Analysis*, Addison-Wesley.

### Kerberos

- Jason Garman — *Kerberos: The Definitive Guide*, O'Reilly Media.
- Brian Tung — *Kerberos: A Network Authentication System*, Addison-Wesley.

### Linux Security / Authentication

- Michael D. Bauer — *Building Secure Servers with Linux*, O'Reilly Media.
- Steve Suehring — *Linux Firewalls* and general Linux security references as complementary material.

## RFC y estándares

Para profundizar en protocolos:

- RFC 4510 — Lightweight Directory Access Protocol (LDAP): Technical Specification Road Map.
- RFC 4511 — LDAP: The Protocol.
- RFC 4512 — LDAP: Directory Information Models.
- RFC 4513 — LDAP: Authentication Methods and Security Mechanisms.
- RFC 4514 — LDAP: String Representation of Distinguished Names.
- RFC 4515 — LDAP: String Representation of Search Filters.
- RFC 4519 — LDAP: Schema for User Applications.
- RFC 4120 — The Kerberos Network Authentication Service (V5).
- RFC 4121 — Kerberos Version 5 GSS-API Mechanism.
- RFC 4556 — Public Key Cryptography for Initial Authentication in Kerberos (PKINIT).
- RFC 6238 — TOTP.
- RFC 4226 — HOTP.

## Manual pages esenciales

```text
passwd(5)
shadow(5)
group(5)
login.defs(5)
useradd(8)
usermod(8)
chage(1)
getent(1)
nsswitch.conf(5)
pam(8)
pam.d(5)
authselect(8)
sudo(8)
sudoers(5)
sssd.conf(5)
sssctl(8)
realm(8)
krb5.conf(5)
kinit(1)
klist(1)
kvno(1)
kadmin(1)
ldapsearch(1)
ldapmodify(1)
ldapadd(1)
ldapdelete(1)
ldapwhoami(1)
ipa(1)
journalctl(1)
auditctl(8)
ausearch(8)
aureport(8)
```

## Criterio de uso de fuentes

La documentación oficial de Fedora, Red Hat, FreeIPA, SSSD, MIT Kerberos, OpenLDAP, sudo y Linux-PAM debe tener prioridad para instalación, sintaxis y comportamiento actual.

Los libros se utilizarán principalmente para fundamentos, arquitectura, protocolos y explicación conceptual.

Los RFC se utilizarán en los bloques avanzados para comprender LDAP y Kerberos a nivel de protocolo.
