# Domain — Identity & Access Management (IAM)

## Dominio

Administración de identidades y accesos en sistemas Linux empresariales, con énfasis en Fedora, RHEL y tecnologías del ecosistema Red Hat.

El alcance principal es IAM de infraestructura Linux empresarial. Las capas se
relacionan según la integración; no forman una única cadena obligatoria.

| Función | Flujo representativo | Resultado |
|---|---|---|
| Resolución de identidad | Aplicación → NSS → files o SSSD → directorio | UID/GID y grupos |
| Autenticación PAM | Aplicación → PAM → pam_sss → SSSD → proveedor | Validación del método configurado |
| Autenticación LDAP | Aplicación → LDAP bind sobre TLS → directorio | Identidad autenticada |
| SSO Kerberos | Cliente → KDC → ticket → servicio mediante GSSAPI | Principal autenticado |
| Autorización | Punto de control → reglas aplicables | Permitir o denegar el recurso |

La autorización puede consultar HBAC mediante PAM/SSSD, reglas sudo, ACL del
directorio o políticas de la aplicación y del sistema de archivos. Kerberos
no sustituye esos controles. DNS en NSS resuelve nombres de hosts, no cuentas.

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

Al finalizar, el estudiante podrá distinguir los flujos de la tabla inicial,
identificar el punto que aplica autorización y probar cada capa por separado.
La lista de diagnóstico es una guía de comprobaciones, no una secuencia de
dependencias que deba ejecutar toda autenticación.

También deberá ser capaz de desplegar una infraestructura FreeIPA/IdM redundante, integrar clientes Linux y servicios consumidores, aplicar políticas de acceso y privilegios, validar una misma identidad central en varios servicios, administrar credenciales y resolver fallos complejos de DNS, tiempo, TLS, LDAP, Kerberos, SSSD, PAM y autorización.


## Laboratorios y progresión operativa

Se conservan los bloques 0–24 y sus lecciones; las ampliaciones se añaden al
final de cada bloque para preservar sus identificadores. Las lecciones de
ampliación se pueden usar como talleres de consolidación antes del siguiente
bloque. Una referencia anticipada a una tecnología se explica conceptualmente
y se implementa después de completar sus requisitos.

| Entorno | Objetivo | Aislamiento |
|---|---|---|
| OpenLDAP | DIT, schemas POSIX, ACL, TLS y syncrepl | Directorio independiente |
| MIT Kerberos | Realm, KDC, intercambios, keytabs y recuperación | Realm independiente |
| FreeIPA/IdM | Proveedor integrado, clientes, políticas y réplica | Dominio final independiente |

El laboratorio final usa dos servidores IdM, un cliente Linux y hosts de
servicios consumidores en una red privada. Se documentan recursos necesarios,
FQDN, IP, DNS, sincronización temporal, paquetes, unidades, puertos, SELinux y
versiones reales. No requiere exposición pública. Los laboratorios previos
pueden ejecutarse en máquinas separadas o reconstruirse de forma reproducible.
Los snapshots facilitan rollback de prácticas; no sustituyen backups probados.

No se despliega OpenLDAP sobre el directorio 389 DS de FreeIPA ni un KDC
independiente para reemplazar su KDC integrado. En FreeIPA se utilizan las
interfaces administrativas documentadas; las modificaciones directas de sus
componentes internos requieren un procedimiento oficial específico.

## Contratos de integración y aceptación

Cada consumidor documenta la fuente de identidad, el método de autenticación,
el punto de autorización, la política offline y los tiempos de propagación.
SSSD no es un backend genérico intercambiable con LDAP para toda aplicación:
hay que indicar la interfaz real usada, como NSS, PAM o una consulta LDAP.
HBAC no se aplica automáticamente a NFS, SMTP, HTTP o todo servicio GSSAPI.
Se prueba el acceso efectivo al recurso además de la autenticación.

Una baja central se evalúa distinguiendo nuevas autenticaciones, TGT, tickets
de servicio emitidos, sesiones abiertas, cachés de identidad, credenciales
offline, claves SSH y certificados. Deshabilitar la cuenta no garantiza cierre
inmediato de sesiones ni invalidación de tickets previamente emitidos.
El runbook define mecanismos por consumidor y mide la ventana residual.
MFA también se comprueba por flujo: no se presume que todos los protocolos
heredan el requisito de otro método de login.

Se valida la coherencia de UID/GID, grupos y propietarios antes y después de
migraciones. Una rotación de keytab comprueba KVNO, claves y tickets nuevos;
se distingue de copiar el fichero. Los certificados públicos no son secretos;
sí lo son las claves privadas y los bundles que las incluyan.

## Disponibilidad, recuperación y operación

La réplica no equivale a backup. Se distinguen topología y convergencia del
directorio de los roles de CA, KRA y DNS, cuando se despliegan. El proyecto
prueba failover desde el cliente, pérdida de servidor y recuperación aislada.
Se registran RPO/RTO objetivo y observado, dependencias, claves necesarias,
integridad del backup y verificación funcional de identidad, SSO y políticas.

Para cada componente se identifica el destino real de logs: journald, archivos
en /var/log o destinos configurados. No se presupone que todas las versiones
escriben en las mismas rutas. La depuración es temporal y evita exponer secretos.

## Relación con los otros PATH

| PATH | Papel |
|---|---|
| TIME | Dependencia de Kerberos y correlación de eventos |
| DNS | Resolución y descubrimiento; componente opcional integrado de FreeIPA |
| DHCP y DHCP + DNS | Servicios de red; Kea D2 y TSIG no son IAM de usuarios |
| IAM | Administración central de identidades, credenciales y políticas |
| SSH, NFS/Samba, Proxy, Mail, Web y OpenVPN | Consumidores según integración explícita |
| WireGuard | Identidad criptográfica de peers; gestión humana requiere otra capa |

El orden de revisión de documentos no altera las dependencias del despliegue.
DNS y TIME deben funcionar antes de desplegar FreeIPA. El PATH DHCP + DNS
desarrolla Kea D2/BIND; aquí se explica el descubrimiento de IdM y GSS-TSIG
cuando corresponda. No se presupone que ambos mecanismos DDNS sean idénticos.

## Límites y extensiones

OIDC autentica sobre OAuth 2.0; OAuth 2.0 se ocupa de autorización delegada.
SAML cubre federación y SCIM aprovisionamiento. Se explica su relación con
LDAP/Kerberos y con proveedores de identidad para aplicaciones; su despliegue
profundo queda para un PATH de federación. FreeIPA no se presenta como un
proveedor universal de esos protocolos. Los productos PAM comerciales y cloud
IAM mantienen su exclusión; JIT, JEA y vaulting no se atribuyen automáticamente
a FreeIPA por aparecer en el temario.

Las recetas especifican distribución, versión y soporte. La disponibilidad de
OpenLDAP servidor se comprueba por plataforma, diferenciando clientes LDAP.
Samba, passkeys, smart cards y trusts requieren una matriz de capacidades y
limitaciones según versiones. El material conserva alternativas didácticas
sin confundirlas con configuraciones soportadas para producción.
