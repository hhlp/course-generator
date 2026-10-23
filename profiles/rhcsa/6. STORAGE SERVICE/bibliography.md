# Bibliografía — FILE / STORAGE SERVICES

## Criterio de uso

La documentación oficial de la versión instalada manda sobre ejemplos de libros
históricos. Registrar distribución, versión, kernel y paquetes en cada práctica.
La revisión de integración se contrastó con documentación RHEL 9; comprobar la
matriz de soporte de la versión elegida antes de aplicar el escenario a otra.

## Documentación oficial principal

1. [Red Hat Enterprise Linux 9 — Configuring and using network file services](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_using_network_file_services/index).
   Referencia operativa para Samba, NFS y sus clientes. Revisar especialmente
   winbind, idmap, ACL, Kerberos y los servicios del servidor NFS.
2. [RHEL 9 — Using Samba as a server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_using_network_file_services/assembly_using-samba-as-a-server_configuring-and-using-network-file-services).
   Recorridos autónomo, miembro AD y miembro IdM. Para el servidor Samba miembro
   en RHEL, winbindd es el backend soportado; SSSD no es un sustituto equivalente.
3. [RHEL 9 — Setting up Samba on an IdM domain member](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_external_red_hat_utilities_with_identity_management/setting-up-samba-on-an-idm-domain-member_using-external-red-hat-utilities-with-idm).
   Preparación del dominio, ipa-client-samba, principal CIFS y limitaciones.
   La edición consultada lo clasifica como Technology Preview; revisar el estado
   y los tipos de clientes admitidos para la versión concreta del laboratorio.
4. [RHEL 9 — Managing file systems](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_file_systems/index).
   Filesystems, cuotas, montajes y autofs. Incluir mapas IdM consultados por
   SSSD, caché y configuración NSS, diferenciándolos del acceso al recurso.
5. [RHEL 9 — Using external Red Hat utilities with Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_external_red_hat_utilities_with_identity_management/using_external_red_hat_utilities_with_identity_management).
   Complemento de integración NFS, automount y Samba con IdM.
6. [Catálogo de documentación RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9).
   Consultar *Managing storage devices*, *Configuring device mapper multipath*,
   *Configuring and managing logical volumes* y guías de seguridad aplicables.
   Referencias para LIO, initiators, LUN, LVM, ALUA, multipath y recuperación.
7. [Fedora Documentation](https://docs.fedoraproject.org/).
   Contrastar paquetes, unidades y configuración con la edición instalada.
8. [Samba Project Documentation](https://www.samba.org/samba/docs/).
   Manuales de smb.conf, winbind, clientes y módulos VFS; consultar la versión
   que corresponda al paquete utilizado.
9. [Linux Kernel Documentation — NFS](https://docs.kernel.org/filesystems/nfs/index.html).
   Arquitectura y detalles de cliente/servidor. Complementar con documentación
   SCSI y device mapper de la misma colección cuando el laboratorio lo requiera.
10. [systemd manual pages](https://www.freedesktop.org/software/systemd/man/latest/).
    systemd.mount, systemd.automount, systemd.special y systemd.unit. Contrastar
    siempre con las páginas instaladas, ya que latest puede describir funciones
    posteriores a las de la distribución.
11. [fio documentation](https://fio.readthedocs.io/en/latest/).
    Diseño de cargas, latencias, percentiles y verificación; utilizar discos o
    archivos de laboratorio desechables.
12. [Prometheus node_exporter](https://github.com/prometheus/node_exporter).
    Verificar collectors y métricas disponibles. Completar con sondas de servicio
    y fuentes específicas cuando el collector no cubra la señal requerida.

## Manuales instalados obligatorios

- NFS: exports(5), nfs(5), nfs.conf(5), mount.nfs(8), exportfs(8),
  nfsstat(8), nfsiostat(8), rpc.gssd(8), gssproxy(8), idmapd.conf(5).
- autofs: autofs(5), auto.master(5), autofs.conf(5), automount(8),
  sssd.conf(5), sssd-ldap(5), ipa-client-automount(1).
- SMB: smb.conf(5), smbclient(1), smbstatus(1), mount.cifs(8),
  cifs.upcall(8), winbindd(8), wbinfo(1), net(8), vfs_acl_xattr(8),
  vfs_full_audit(8), ipa-client-samba(1).
- iSCSI y multipath: targetcli(8), iscsiadm(8), iscsid(8), multipath(8),
  multipath.conf(5), multipathd(8), lvmdevices(8), lvm.conf(5).
- Metadatos y diagnóstico: acl(5), getfacl(1), setfacl(1), getfattr(1),
  setfattr(1), xfs_quota(8), rsync(1), tar(1), journalctl(1),
  semanage-fcontext(8), restorecon(8), tcpdump(8), fio(1).

Si una página no está instalada, identificar el paquete que la proporciona.
No asumir que todas las herramientas o funciones existen en cualquier versión.

## Libros de apoyo

- Brent Callaghan. *NFS Illustrated*. Addison-Wesley, 2000.
  Fundamentos y contexto histórico; no usar como guía de despliegue NFSv4
  moderno ni de seguridad actual.
- Gerald Carter, Jay Ts y Robert Eckstein. *Using Samba*, 3.ª edición.
  O'Reilly, 2007. Arquitectura y conceptos históricos; contrastar SMB, AD,
  parámetros y seguridad con documentación Samba actual.
- Ulf Troppens, Rainer Erkens, Wolfgang Müller-Friedt, Rainer Wolafka y
  Nils Haustein. *Storage Networks Explained*, 2.ª edición. Wiley, 2009.
  Fundamentos NAS/SAN, disponibilidad y diseño; no sustituye las guías de LIO.
- Brian Ward. *How Linux Works*, 3.ª edición. No Starch Press, 2021.
  Apoyo de almacenamiento, dispositivos, arranque y funcionamiento de Linux.

Se retira la referencia ambigua «Linux Storage»: no identifica una obra
verificable mediante título completo, autor y edición. Los libros anteriores
son material complementario; el núcleo operativo procede de las guías oficiales.

## Mapa de consulta por bloques

| Bloques | Fuentes principales |
|---|---|
| 0 | Filesystems RHEL, Fedora, systemd y fundamentos de Linux |
| 1–5 | Guía de servicios de archivos, kernel NFS, manuales NFS e IdM |
| 6–8 | Filesystems RHEL, utilidades IdM, autofs y SSSD |
| 9–14 | Guía Samba RHEL, Samba Project, manuales VFS y recorrido IdM |
| 15–22 | Storage devices, LVM, multipath, manuales LIO/iSCSI y fio |
| 23–24 | systemd, manuales de diagnóstico y node_exporter |
| 25–27 | Conjunto de guías; diseño, restauración y evidencias del laboratorio |
