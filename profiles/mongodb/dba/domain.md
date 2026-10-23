# MongoDB administrador — dominio y alcance

Fecha de revisión documental: 21 de octubre de 2026.

Este itinerario forma administradores de MongoDB desde cero hasta la operación experta.
El foco es implementación y gestión; CRUD, agregación e índices se estudian en lo necesario
para verificar datos, generar cargas y diagnosticar rendimiento. La programación de búsquedas,
pipelines avanzados, relevancia y búsqueda vectorial pertenece al itinerario de desarrollo.
La infraestructura de Search/Vector Search se revisa como extensión de capacidad y observabilidad
cuando esté disponible en la edición y versión seleccionadas; no se promete paridad entre entornos.

Base práctica: MongoDB Community autogestionado en red privada, Linux compatible, tres miembros
con datos y configuración estática explícita por nodo. Fedora puede ser el host de VMs o
contenedores; no asumir soporte oficial de paquetes del servidor sobre Fedora.
Se añade Atlas para aprender las decisiones que conserva el cliente en un servicio gestionado.
Enterprise, Kerberos, Ops Manager, backups gestionados, PITR y funciones por plan se identifican
por requisitos. Nunca se presenta una práctica Community como equivalente completo de Enterprise.

Elegir una versión soportada antes del laboratorio y fijar servidor, sistema operativo, drivers,
mongosh, Database Tools, Atlas CLI y providers. Revisar documentación de esa versión, release notes,
matriz de compatibilidad y ciclo de vida. No usar latest ni trasladar parámetros entre versiones
sin comprobarlos. La versión elegida se registra en el manifiesto de cada práctica.

## Resultados de salida

El alumno podrá desplegar y operar MongoDB; proteger identidades y comunicaciones;
explicar las garantías de consistencia; sostener un replica set y un clúster sharded;
diagnosticar incidencias con evidencias; recuperar datos; automatizar cambios y defender
decisiones de arquitectura y coste. «Experto» requiere práctica sostenida con cargas y
fallos reales además de completar el currículo.

## Laboratorios y crecimiento de recursos

| Etapa | Topología | Qué demuestra |
|---|---|---|
| Inicial | Una instancia aislada | Instalación, configuración y primera copia/restore |
| Replica set | Tres mongod con datos | Elecciones, mayoría, replicación y mantenimiento |
| Fallos de host | Tres VMs o hosts separados | Dominios de fallo y pérdida de un host |
| Sharding | Dos shards de tres miembros, CSRS de tres y dos mongos | Distribución, balanceo y operación distribuida |
| Atlas | Proyecto y despliegue compatible con la práctica | Gobierno y responsabilidad compartida |
| Enterprise | Infraestructura y licencia/evaluación habilitadas | Kerberos y controles específicos |

Un replica set de tres procesos en un portátil enseña protocolo y recuperación de procesos;
no demuestra tolerancia a la pérdida del portátil. El clúster sharded completo requiere
nueve procesos mongod y dos mongos: puede ejecutarse por fases o en VMs según recursos.
No se fija un mínimo de RAM universal: se miden memoria, disco y carga y se adapta el dataset.
La simulación local de regiones reproduce latencia y cortes, no garantiza resiliencia cloud.

Red privada por defecto. La fase inicial de una instancia usa loopback. Antes de aceptar
acceso por red se aplican autenticación, reglas de acceso y TLS. Sin puertos de base de datos
abiertos a Internet ni credenciales reales en el repositorio. Los datos son sintéticos o
sample datasets; para datos sensibles se necesita un diseño adicional de protección.

## Organización de evidencias

- `config/`: configuración estática identificada por nodo, sin secretos.
- `inventory/`: nombres, IP privadas, roles, puertos y versiones.
- `runbooks/`: inicio, parada, failover, sustitución, backup, restore y upgrade.
- `evidence/`: comandos saneados, logs relevantes, métricas y verificaciones.
- `reports/`: arquitectura, capacidad, revisión de acceso y postmortems.
- `secrets/`: sólo ruta de ejecución local protegida, excluida de Git; rotación documentada.
- `backups/`: catálogo y referencias de almacenamiento; copias fuera del host cuando aplique.

Estas carpetas describen los entregables que generará el alumno; no vienen implementadas
como infraestructura ejecutable en este paquete.

## Versiones, plataformas y disponibilidad

La selección de versión es una actividad del bloque 0. Las opciones de filesystem,
THP, swap, límites, caché y NUMA se deciden con las Production Notes de la versión;
no se enseñan recetas históricas como universales. Se usan rutas del paquete instalado:
mongod.conf, dbPath y logpath se comprueban; no se asume que coincidan entre RPM,
DEB, contenedores y Atlas. La observabilidad cubre journald y los archivos reales de logs.

| Capacidad | Base accesible | Extensión condicionada |
|---|---|---|
| Replica sets y sharding | Community local | Atlas según tipo de despliegue |
| SCRAM y X.509 | Community | Integraciones según entorno |
| Kerberos | Diseño con IAM existente | Ejecución con MongoDB Enterprise y MIT Kerberos |
| Cifrado | TLS y cifrado de volumen del sistema | Cifrado nativo y gestión de claves según edición |
| Auditoría | Revisión de acceso y evidencias operativas | Auditoría formal según edición o plan |
| Backups | Dump/restore y snapshots consistentes compatibles | Ops Manager o backup Atlas según requisitos |
| PITR | Estudio de garantías y escenarios | Herramienta y retención compatibles verificadas |
| Docker/Podman | Standalone y replica set persistentes con TLS y keyfile | Sharding local y Quadlet |
| Kubernetes | Bloques propios 29–30 con prerrequisitos | Operator, CSI y edición compatibles |

La base gratuita no permite probar todas las operaciones gestionadas. Cada laboratorio
Atlas declara plan, disponibilidad, posible coste y alternativa. Una alternativa local
enseña el objetivo técnico común y no certifica el funcionamiento de la función gestionada.
No se contrata ni aprovisiona ningún recurso de pago como parte de este documento.

## Backups, HA y recuperación: garantías distintas

Replicación reduce interrupciones por fallos de miembros. También replica borrados y errores
lógicos. Sharding distribuye datos/carga; cada shard mantiene su propia disponibilidad mediante
replicación. Backup permite recuperar una historia conservada. Ninguno reemplaza a los otros.
Un dump de un clúster sharded con escrituras concurrentes no se supone globalmente consistente.
Se enseña el método coordinado documentado para la topología y herramienta concretas.
Las instantáneas de VM se usan para comodidad del laboratorio y no se equiparan a una política
de backup consistente de producción. El restore se valida en destino aislado y se miden RPO/RTO.

## Progresión y evaluación

Cada lección debe desarrollar:
- 🎯 OBJETIVO: resultado observable y prerrequisitos.
- 💡 IDEA: fundamentos, arquitectura, decisiones y compromisos.
- Procedimiento: comandos explicados, rutas reales y configuración completa cuando aplique.
- 🧪 LAB: preparación, ejecución, verificación de datos, fallo controlado y recuperación.
- Logs y diagnóstico: dónde mirar, qué significan las evidencias y siguiente comprobación.
- ⚠️ ERRORES: síntomas comunes, causas, mitigación y cómo evitar recurrencias.
- 🧠 RECORDAR: criterios de decisión y comprobaciones esenciales.
- Evaluación práctica, limpieza de recursos y bibliografía oficial versionada.

No basta con que un comando termine con código cero. Las prácticas verifican servicio,
topología, permisos, datos y comportamiento del cliente según corresponda. Los fallos se
introducen únicamente en entornos desechables. Antes de una mutación se identifican impacto,
criterio de parada y recuperación. Los procedimientos de producción necesitan su propia
revisión y adaptación; este paquete contiene el currículo, no scripts de despliegue terminados.

Se estima una dedicación orientativa de 580–880 horas, ajustable por conocimientos previos y
profundidad de las prácticas. No es una garantía de dominio ni una certificación oficial.
Los hitos de initial.txt exigen evidencias, no sólo lectura. IAM avanzado exige fundamentos
de Kerberos; IaC exige Ansible/Terraform; Los bloques 29–30 de Kubernetes tienen su propio prerrequisito.

Rúbrica del proyecto: despliegue y reproducibilidad 20 %, seguridad 20 %, disponibilidad y
consistencia 15 %, recuperación verificada 20 %, observabilidad y rendimiento 15 %,
operación y defensa de decisiones 10 %. Objetivo recomendado: 80/100 y ninguna carencia
crítica en acceso restringido, persistencia, recuperación o protección de secretos.
No se considera superado un proyecto que no haya restaurado sus datos de forma verificable.

## Extensiones de especialización

Operar Search/Vector Search, nodos de búsqueda, índices de búsqueda, consumo de RAM/disco,
builds, estados de sincronización y capacidad como módulo posterior, según soporte verificado.
No se desarrolla aquí el temario de relevancia, embeddings, RAG ni pipelines de búsqueda.
LDAP no es la vía central de integración IAM de este path; se prioriza Kerberos en Enterprise
y SCRAM/X.509 en la base Community.

## Formato del paquete

initial.txt contiene el temario; profile.yaml es un perfil declarativo con bloques y lecciones;
domain.md define alcance, entornos y evaluación; bibliography.md conserva las fuentes.
El YAML se valida sintácticamente y se verifica su coherencia con initial.txt. No se ha probado
su compatibilidad con un esquema específico ni ejecutado course-generator en esta sesión.

## Ampliación: vías Docker/Podman y Kubernetes

El path actualizado comprende 34 bloques y 372 lecciones. El antiguo bloque conjunto 27
se sustituye por cuatro bloques de 18 lecciones. Troubleshooting, SRE y proyecto final
pasan a 31, 32 y 33. Ansible/Terraform permanece en el bloque 26 y conserva su laboratorio.

| Bloque | Vía | Prácticas detalladas |
|---|---|---|
| 27 | Docker/Podman: standalone | Persistencia, bootstrap, SCRAM/TLS, backup/restore, SELinux y rootless |
| 28 | Compose y operación de replica set | Tres miembros, keyfile/TLS, conversión, failover, rotación, restore, Quadlet y extensión sharded |
| 29 | Kubernetes: despliegue | Standalone didáctico, StatefulSet, operator compatible, PVC, red y colocación |
| 30 | Kubernetes: operación | Mantenimiento, fallos, rotación, upgrade, backup/restore e incidentes de almacenamiento |

### Material que deben desarrollar las lecciones

Cada práctica producirá manifiestos completos y procedimientos desde cero: archivos de
configuración por nodo, Compose, unidades Quadlet o manifiestos/valores y recursos del
operator correspondiente; guías de secretos y certificados; verificaciones y runbooks.
El YAML del perfil incluye la tarea y el criterio de verificación de cada práctica ampliada.
Este paquete sigue siendo el temario y perfil de generación: los laboratorios no se han
ejecutado y no se entregan aquí despliegues de infraestructura ya implementados.

### Condiciones específicas

- Verificar la imagen elegida, su usuario, entrypoint, rutas y mecanismo de bootstrap.
  No trasladar variables de inicialización entre imágenes suponiendo que son equivalentes.
- En standalone, SCRAM autentica al cliente y TLS cifra la conexión. El keyfile compartido
  se utiliza al configurar autenticación interna del replica set o clúster sharded.
- Compose y Kubernetes deben montar secretos con permisos que mongod acepte; comprobar
  el propietario y modo efectivos dentro del contenedor, no sólo la declaración YAML.
- El proveedor usado por `podman compose` se registra. Se ofrece Quadlet como vía de
  integración Podman/systemd; no se asume paridad completa con Docker Compose.
- DNS anunciado por MongoDB y SAN de certificados deben ser resolubles/válidos desde
  el cliente. Un puerto publicado no resuelve por sí solo el descubrimiento de topología.
- El operator se selecciona por versión, edición y funciones soportadas. Su CRD y su
  reconciliación gobiernan los cambios: no se aplican parches manuales permanentes a los
  recursos administrados para saltarse ese modelo.
- Un clúster local de un nodo no demuestra tolerancia al fallo físico del host. Para
  pruebas de nodo se necesita capacidad y almacenamiento adecuados y se explicita
  qué dominios de fallo se han validado. PDB no garantiza protección ante todo fallo.
- Un VolumeSnapshot se evalúa por consistencia de datos y topología; no basta su existencia
  para declararlo backup válido. El restore debe verificarse en PVC independientes.
- Los backups, ediciones Enterprise o servicios cloud condicionados siguen siendo
  extensiones identificadas; la alternativa local no se declara equivalente funcional.

La ampliación cambia el medio de despliegue y la operación sobre cada plataforma. Mantiene
los fundamentos de replicación, seguridad, consistencia y recuperación de los bloques
anteriores y remite a ellos para evitar repetirlos como teoría introductoria.
