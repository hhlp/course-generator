# domain.md — FILE / STORAGE SERVICES

## Dominio

Administración Linux de servicios de archivos y almacenamiento en red sobre Fedora/RHEL.

## Tecnologías principales

### NFS
NFSv3, NFSv4.x, nfs-utils, exports, RPC, clientes, Kerberos, ACL, rendimiento y diagnóstico.

### autofs
Master maps, direct/indirect maps, wildcards, multimounts, NFS/CIFS automount, debugging y systemd.

### Samba / SMB
SMB2/SMB3, Samba server/client, shares, ACL, SELinux, signing/encryption, integración con Kerberos/Active Directory y troubleshooting.

### iSCSI
LIO, targetcli, iscsiadm, targets, initiators, LUN, IQN, CHAP, LVM, multipath, rendimiento y recuperación.

## Relación con IAM

El dominio se estudia con dos modelos explícitos: servicios File/Storage autónomos y servicios que consumen identidad centralizada. NFS se estudia primero con UID/GID y `sec=sys`, y después como consumer de Kerberos/FreeIPA. Samba se estudia primero con usuarios/grupos locales y `smbpasswd`/`pdbedit`, y después integrado con identidad central mediante recorridos separados para AD y FreeIPA/IdM, con requisitos y soporte propios. iSCSI conserva normalmente un modelo independiente del IAM de usuarios basado en IQN, ACL y CHAP.

La ruta no convierte File/Storage en proveedor de identidades: el proveedor central pertenece al PATH IAM. File/Storage aprende a consumirlo cuando corresponde.

## Dominios transversales

- TCP/IP y resolución DNS
- POSIX permissions y ACL
- SELinux
- firewalld
- systemd y boot ordering
- Kerberos e identidad
- journald / rsyslog / logs
- observabilidad
- capacity planning
- rendimiento
- hardening
- troubleshooting por capas
- runbooks y documentación

## Límites

El PATH se centra en administración de storage Linux empresarial. Los filesystems distribuidos/clusterizados como CephFS, GlusterFS o GFS2 pueden constituir rutas independientes y no sustituyen el estudio detallado de NFS, SMB e iSCSI.

## Resultado esperado

El estudiante debe poder justificar técnicamente cuándo utilizar file storage o block storage, implementar los servicios desde cero, operarlos de forma segura y diagnosticar fallos desde la red hasta el filesystem.

## Contrato con las rutas previas

La base Linux, TCP/IP, DNS y TIME se validan antes del laboratorio. El escenario
centralizado requiere un proveedor IAM operativo y cuentas/grupos de prueba ya
creados allí. Storage enrola sus hosts, solicita principals y keytabs y configura
la autorización de recursos. No despliega otro proveedor ni duplica cuentas
humanas centrales en bases locales. El escenario autónomo sí enseña cuentas
locales como modelo independiente.

## Integración detallada

- NFS: diferenciar identidad NSS, idmapping, autenticación RPCSEC_GSS y permisos.
  Incluir gssproxy en servidor y rpc.gssd en cliente según versión, nfs/FQDN,
  tickets, keytabs, sec=krb5/krb5i/krb5p y pruebas de expiración/denegación.
- autofs: mapas locales y mapas IdM mediante SSSD; locations, keys,
  ipa-client-automount, caché y diagnóstico del mapa frente al recurso montado.
  Recuperar mapas no concede por sí mismo acceso al almacenamiento.
- Samba AD: utilizar winbindd para el servidor miembro en RHEL. SSSD puede
  intervenir en otros roles Linux, pero no se enseña como sustituto soportado
  de winbind para servir SMB en ese escenario. Separar unión Linux al dominio
  y configuración del servidor de archivos; realmd/adcli no son intercambiables
  con toda la configuración que necesita Samba.
- Samba FreeIPA/IdM: recorrido específico con ipa-client-samba y cifs/FQDN.
  La documentación RHEL 9 consultada lo clasifica como Technology Preview;
  explicar restricciones de clientes Windows y trusts. Revalidar soporte para
  la versión elegida, sin extrapolarlo a Fedora ni a otras versiones de RHEL.
- iSCSI: identidad del initiator, ACL de LUN y CHAP. CHAP no cifra el tráfico;
  DNS/TIME pueden ser dependencias operativas sin convertirlo en consumidor
  de identidades humanas. La administración del host sí puede usar IAM.

## Profundidad operativa y límites de disponibilidad

Añadir cuotas, recuperación de bloqueos NFSv4, persistencia de configuración,
rotación de secretos y migraciones conservando UID/GID, SID, ACL y atributos
extendidos. Las ACL NFSv4/POSIX se contrastan con las capacidades reales del
servidor y filesystem, sin asumir equivalencia.

Multipath recupera rutas hacia un LUN; la continuidad ante caída del target
requiere una arquitectura adicional. Se estudian HA, estado, quorum y fencing
como criterios de diseño; la implementación completa de clústeres corresponde
a una ruta HA. XFS/ext4 no se montan con escritura desde múltiples hosts sobre
el mismo LUN. GFS2 y otros filesystems de clúster siguen fuera del núcleo.

Backup incluye RPO/RTO, consistencia de aplicación, copias independientes y
restauración comprobada de datos y metadatos. Un snapshot aislado no satisface
por sí solo el diseño de backup. Se verifica el contexto SELinux en el destino.

## Laboratorio y evaluación

Usar máquinas virtuales Fedora/RHEL en una red privada con discos desechables.
Registrar versiones, roles, FQDN, direcciones, puertos, volúmenes y dependencias.
El laboratorio principal no requiere acceso público. AD e IdM son escenarios
alternativos explícitos; si falta un proveedor, documentar ese escenario como
pendiente, sin sustituirlo por usuarios locales y llamarlo integración central.

Cada práctica incluye objetivo, configuración completa apropiada a la versión,
comandos, evidencia esperada, caso denegado, logs efectivos y recuperación.
Las pruebas de fio usan datos desechables. Los fallos de IAM, DNS, TIME y
Storage se inyectan por separado y se registra el comportamiento observado.
El proyecto final comprueba reinicio, persistencia, permisos, cuotas, integridad,
restauración y caída de rutas. Esta entrega define el currículo; los scripts y
configuraciones ejecutables se elaboran durante las lecciones.
