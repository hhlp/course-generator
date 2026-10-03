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

El dominio se estudia con dos modelos explícitos: servicios File/Storage autónomos y servicios que consumen identidad centralizada. NFS se estudia primero con UID/GID y `sec=sys`, y después como consumer de Kerberos/FreeIPA. Samba se estudia primero con usuarios/grupos locales y `smbpasswd`/`pdbedit`, y después integrado con identidad central, Kerberos y servicios de directorio. iSCSI conserva normalmente un modelo independiente del IAM de usuarios basado en IQN, ACL y CHAP.

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
