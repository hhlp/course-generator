# Domain — Identity & Access Management (IAM)

## Dominio

Administración de identidades y accesos en sistemas Linux empresariales, con énfasis en Fedora, RHEL y tecnologías del ecosistema Red Hat.

El dominio cubre la cadena completa:

```text
Identity
  ↓
NSS
  ↓
PAM
  ↓
LDAP / Kerberos
  ↓
SSSD / realmd
  ↓
FreeIPA / Red Hat IdM
  ↓
IAM Provider → Service Consumers
  ↓
Authentication + Authorization
  ↓
Privileged Access + Secrets
  ↓
Auditing + Hardening + Troubleshooting
```

## Objetivo general

Pasar desde la administración local de usuarios Linux hasta ser capaz de diseñar, desplegar, asegurar, operar y diagnosticar una infraestructura IAM centralizada.

El estudiante debe comprender no sólo comandos y configuración, sino también los protocolos, flujos, dependencias y componentes internos.

## Plataformas

- Fedora Linux.
- Red Hat Enterprise Linux.
- FreeIPA.
- Red Hat Identity Management cuando corresponda.
- OpenLDAP para aprendizaje profundo del protocolo y servidor LDAP.
- MIT Kerberos.
- SSSD.
- realmd.
- 389 Directory Server como componente de FreeIPA/IdM.

## Áreas de conocimiento

### Linux Identity

Usuarios, grupos, UID/GID, `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/gshadow`, `login.defs`, lifecycle local y resolución de identidades.

### NSS

Name Service Switch, `nsswitch.conf`, glibc, fuentes de identidad y resolución mediante `files`, DNS y SSSD.

### PAM

Arquitectura de Pluggable Authentication Modules, stacks, módulos, control flags, `authselect` e integración con login, SSH, sudo y SSSD.

### LDAP

Protocolo LDAP, DIT, DN/RDN, entries, attributes, schemas, bind, search, filters, ACL/ACI, LDIF, TLS y operación de OpenLDAP.

### Kerberos

Realms, principals, KDC, AS/TGS, TGT, service tickets, keytabs, service principals, SSO, ticket caches y MIT Kerberos.

### SSSD

Resolución de identidad, autenticación, autorización, caching, operación offline y providers LDAP, Kerberos, IPA y AD.

### realmd

Descubrimiento y unión a realms, integración con SSSD/Kerberos y fundamentos de integración con Active Directory.

### FreeIPA / Red Hat IdM

LDAP, Kerberos, DNS, CA/PKI, SSSD, users, groups, hosts, service principals, HBAC, sudo, RBAC, certificados, MFA, replicas, backup y troubleshooting.

### IAM Provider → Service Consumers

El IAM actúa como origen central de identidades, credenciales y políticas. OpenSSH, NFS/Samba, Squid, Mail, Web y OpenVPN se estudian aquí como consumidores de identidad sólo hasta el nivel necesario para comprender el patrón de integración; la administración profunda de cada servicio permanece en su PATH específico.

El modelo evita duplicar usuarios por aplicación: una identidad central puede resolverse mediante SSSD/NSS, autenticarse mediante PAM o Kerberos/GSSAPI y recibir autorización mediante HBAC, sudo u otras políticas del servicio. También se distingue explícitamente entre identidades humanas, service principals, host principals, machine identities, keytabs y certificados.

DNS y Chrony/NTP se consideran dependencias fundamentales de FreeIPA/Kerberos, no proveedores de identidad de usuarios. WireGuard se trata como un caso distinto: sus claves de peers identifican peers criptográficos, pero no constituyen por sí mismas un sistema IAM de usuarios.

### Authentication

Passwords, SSH keys, SSH certificates, X.509, Kerberos, OTP, MFA, smart cards y FIDO2.

### Authorization

DAC, POSIX ACL, RBAC, conceptos ABAC, sudo, HBAC y relación con SELinux.

### Privileged Access

Privileged Access Management, PASM, vaulting, credential rotation, JIT, JEA, approvals, session recording, command auditing y break-glass.

### Machine identities y secrets

Service accounts, machine identities, principals, keytabs, certificados, secretos y lifecycle de credenciales no humanas.

### Observabilidad IAM

journald, auditd y logs de PAM, sudo, SSSD, LDAP, Kerberos, SSH y FreeIPA.

### Seguridad

Least privilege, MFA, hardening, credential protection, TLS, Kerberos security, privileged identities y detección de abuso.

### Troubleshooting

Diagnóstico sistemático desde las dependencias fundamentales:

```text
TIME
 ↓
DNS
 ↓
NETWORK
 ↓
TLS
 ↓
IDENTITY
 ↓
LDAP
 ↓
KERBEROS
 ↓
SSSD
 ↓
NSS/PAM
 ↓
AUTHORIZATION
 ↓
APPLICATION
```

## Dependencias previas recomendadas

El estudiante debería conocer previamente:

- Administración Linux/RHCSA.
- systemd.
- journald.
- OpenSSH.
- SELinux.
- firewalld.
- TCP/IP.
- DNS/BIND.
- Chrony/NTP.
- PKI/TLS.

DNS y sincronización temporal son especialmente importantes antes de Kerberos y FreeIPA.

## Enfoque práctico

Cada tecnología debe estudiarse siguiendo, cuando corresponda:

1. Fundamentos.
2. Arquitectura.
3. Protocolos.
4. Instalación explícita en Fedora/RHEL: paquetes, dependencias, repositorios si fueran necesarios, servicios systemd, firewall/puertos y verificación inicial.
5. Configuración.
6. Administración CLI.
7. Integración.
8. Seguridad.
9. Logs.
10. Troubleshooting.
11. Laboratorio.
12. Fallos intencionados y recuperación.

## Resultado esperado

Al finalizar, el estudiante podrá explicar y diagnosticar un flujo como:

```text
user
 ↓
application
 ↓
PAM
 ↓
SSSD
 ├── NSS identity lookup
 ├── LDAP/IPA identity
 └── Kerberos authentication
        ↓
authorization policy
        ↓
HBAC / sudo / local policy
        ↓
service access
        ↓
audit trail
```

También deberá ser capaz de desplegar una infraestructura FreeIPA/IdM redundante, integrar clientes Linux y servicios consumidores, aplicar políticas de acceso y privilegios, validar una misma identidad central en varios servicios, administrar credenciales y resolver fallos complejos de DNS, tiempo, TLS, LDAP, Kerberos, SSSD, PAM y autorización.
