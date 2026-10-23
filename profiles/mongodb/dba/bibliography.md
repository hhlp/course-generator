# Bibliografía — MongoDB administrador

Revisión: 21 de octubre de 2026. Fuentes primarias oficiales.

Las rutas `manual` y `current` evolucionan. Antes de cada laboratorio, seleccionar la documentación correspondiente a las versiones registradas en el inventario. La referencia 8.0 es un ejemplo versionado, no una versión impuesta al curso.

- [Despliegue y elección de entorno](https://www.mongodb.com/es/docs/deployment/) — Bloques 0, 3, 23; ediciones y responsabilidades.
- [Gestión de MongoDB](https://www.mongodb.com/es/docs/management/) — Mapa de operaciones, seguridad, backup, escalado e IaC.
- [Instalación Community y Enterprise](https://www.mongodb.com/docs/manual/installation/) — Bloques 1–4; plataforma y paquetes compatibles.
- [Production Notes](https://www.mongodb.com/docs/manual/administration/production-notes/) — Bloques 1, 6, 17; requisitos del sistema dependientes de versión.
- [Operations Checklist](https://www.mongodb.com/docs/manual/administration/production-checklist-operations/) — Revisiones de despliegue y readiness.
- [Security Checklist](https://www.mongodb.com/docs/manual/administration/security-checklist/) — Bloques 8–10; autenticación, roles, TLS y protección de datos.
- [Kerberos en despliegues autogestionados](https://www.mongodb.com/docs/manual/core/kerberos/) — Bloque 10; Enterprise, principals, keytabs y usuarios externos.
- [Replication](https://www.mongodb.com/docs/manual/replication/) — Bloques 11–14; replica sets y replicación.
- [Replica Set Deployment Architectures, ejemplo versionado 8.0](https://www.mongodb.com/docs/v8.0/core/replica-set-architectures/) — Lectura de arquitectura; contrastar con la versión finalmente elegida.
- [Monitoring](https://www.mongodb.com/docs/manual/administration/monitoring/) — Bloques 15–17 y 28; estadísticas, herramientas y diagnóstico.
- [Backup Methods](https://www.mongodb.com/docs/manual/core/backups/) — Bloques 18–19; métodos y requisitos por topología.
- [Sharding](https://www.mongodb.com/docs/manual/sharding/) — Bloques 20–21; arquitectura, claves y distribución.
- [Actualizaciones de parche](https://www.mongodb.com/docs/manual/tutorial/upgrade-revision/) — Bloque 22; completar con guía origen/destino de versión.
- [Atlas](https://www.mongodb.com/docs/atlas/) — Bloques 23–25; administración del servicio.
- [Atlas Architecture Center](https://www.mongodb.com/docs/atlas/architecture/current/) — Arquitectura, gobierno y responsabilidad compartida.
- [Alta disponibilidad Atlas](https://www.mongodb.com/docs/atlas/architecture/current/high-availability/) — Bloques 12, 24 y 29; diseño de resiliencia gestionada.
- [Atlas Free Cluster Limits](https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/) — Matriz de restricciones de prácticas; comprobar antes de usar.
- [Atlas Cloud Backup](https://www.mongodb.com/docs/atlas/backup/cloud-backup/overview/) — Bloques 18, 19 y 24; disponibilidad de backup según despliegue.
- [Alertas Atlas](https://www.mongodb.com/docs/atlas/reference/alert-conditions/) — Bloques 15 y 24; métricas y condiciones disponibles.
- [Atlas CLI](https://www.mongodb.com/docs/atlas/cli/current/) — Bloques 23 y 26; automatización y operaciones desde terminal.
- [MongoDB Controllers for Kubernetes](https://www.mongodb.com/docs/kubernetes/current/) — Bloques 29–30; verificar operator, edición y documentación actuales.

## Cómo usar las fuentes

Las páginas de despliegue y gestión son el mapa de entrada. Cada lección debe enlazar además
el procedimiento y la referencia exactos de la versión utilizada: parámetros, comandos,
roles, garantías y restricciones. Las instrucciones del curso se contrastan con el manual;
no se copian valores por defecto o comandos de una versión distinta.

Para Ansible, Terraform, SELinux, firewalld, Prometheus/Grafana y Kubernetes se añaden las
documentaciones oficiales de sus versiones durante el desarrollo de las lecciones. En
particular, se verifica el provider de Atlas y el exporter concreto antes de automatizar.
No se impone ningún libro comercial; se puede incorporar bibliografía secundaria después
sin sustituir las referencias oficiales ni sus advertencias de compatibilidad.

## Fuentes para las vías ampliadas

- [MongoDB Community en Docker](https://www.mongodb.com/docs/manual/administration/install-community-docker/): imagen oficial, montaje de configuración y selección de versión; bloques 27–28.
- [Docker Compose Specification](https://docs.docker.com/reference/compose-file/): servicios, redes, volúmenes, health checks y configuración declarativa.
- [Secrets en Compose](https://docs.docker.com/compose/how-tos/use-secrets/): acceso por servicio y archivos montados; verificar permisos efectivos.
- [Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html): integración con systemd, redes y volúmenes.
- [Podman compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html): proveedor externo y diferencias de ejecución.
- [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/): identidad y almacenamiento estables.
- [Kubernetes Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/): PVC, PV, StorageClass y políticas de recuperación.
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/): límites de protección y buenas prácticas.
- [Kubernetes Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/): PDB y disrupciones voluntarias e involuntarias.
- [Kubernetes Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/): API/CSI; completar con garantías del método de backup MongoDB.
- [MongoDB Controllers for Kubernetes](https://www.mongodb.com/docs/kubernetes/current/): selección de operator, edición y documentación de la CRD; bloques 29–30.

Las fuentes `latest` y `current` son puntos de entrada: fijar versiones para reproducir
las prácticas. Los ejemplos de instalación rápida no sustituyen el diseño de seguridad,
la persistencia ni las verificaciones de recuperación exigidas por este currículo.
