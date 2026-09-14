# DOMAIN — PostgreSQL Server Administration

## 1. Identidad del PATH

Este PATH enseña **administración profesional de servidores PostgreSQL desde cero hasta nivel experto**, con énfasis en PostgreSQL moderno sobre Linux y, cuando sea relevante para la integración con el sistema operativo, con ejemplos orientados a Fedora/RHEL.

El objetivo no es formar únicamente a un usuario de SQL ni a un desarrollador de aplicaciones. El objetivo es formar a un **DBA / PostgreSQL Server Administrator** capaz de instalar, configurar, asegurar, observar, diagnosticar, mantener, recuperar, replicar, actualizar, optimizar y operar PostgreSQL en entornos reales de producción.

El PATH debe avanzar desde los fundamentos hasta un nivel en el que el alumno pueda comprender tanto el comportamiento operativo del servidor como sus mecanismos internos.

Debe cubrir, entre otros:

- arquitectura cliente-servidor;
- cluster PostgreSQL;
- databases, schemas y objetos globales;
- instalación e inicialización;
- `PGDATA`;
- configuración;
- `postgresql.conf`;
- `postgresql.auto.conf`;
- `pg_hba.conf`;
- `pg_ident.conf`;
- administración mediante `psql`;
- SQL administrativo;
- catálogos del sistema;
- vistas de estadísticas;
- funciones administrativas;
- roles y privilegios;
- autenticación;
- TLS;
- seguridad;
- almacenamiento físico;
- páginas y tuples;
- MVCC;
- VACUUM;
- autovacuum;
- ANALYZE;
- estadísticas del planner;
- locking y concurrencia;
- WAL;
- checkpoints;
- memoria;
- I/O;
- tablespaces;
- índices;
- planner y executor;
- `EXPLAIN`;
- rendimiento;
- logging;
- monitorización;
- backups;
- archivado WAL;
- PITR;
- disaster recovery;
- replicación física;
- replicación síncrona;
- replication slots;
- failover;
- switchover;
- alta disponibilidad;
- replicación lógica;
- logical decoding;
- particionamiento;
- mantenimiento;
- extensiones;
- FDW;
- paralelismo;
- JIT;
- integración con Linux;
- capacity planning;
- benchmarking;
- troubleshooting;
- corrupción e integridad;
- upgrades;
- migraciones;
- automatización;
- observabilidad;
- performance tuning;
- internals;
- diagnóstico experto;
- arquitectura de producción;
- operaciones;
- gestión de incidentes;
- diseño de estrategia DBA;
- proyecto final de plataforma PostgreSQL de producción.

---

## 2. Filosofía del curso

El curso debe enseñar PostgreSQL como un sistema completo.

No se debe reducir PostgreSQL a:

- una colección de comandos;
- un conjunto de recetas;
- una lista de parámetros;
- consultas SQL aisladas;
- una guía de instalación;
- una preparación superficial para certificación;
- una simple colección de comandos `pg_*`.

Cada tema debe explicar:

1. qué problema resuelve;
2. qué componente de PostgreSQL interviene;
3. cómo funciona;
4. cómo se observa;
5. cómo se configura;
6. qué impacto tiene;
7. cómo falla;
8. cómo se diagnostica;
9. cómo se recupera;
10. cómo interactúa con otros componentes;
11. qué compromisos de diseño implica;
12. cuándo no debe utilizarse.

La administración debe relacionarse continuamente con la arquitectura interna del servidor.

Ejemplo:

No basta con enseñar:

```sql
VACUUM;
```

Se debe explicar progresivamente:

- por qué PostgreSQL necesita VACUUM;
- cómo MVCC crea versiones de tuples;
- qué son dead tuples;
- qué papel tiene `xmin`;
- qué papel tiene `xmax`;
- qué es la visibility map;
- qué es freezing;
- qué es XID wraparound;
- qué ocurre con autovacuum;
- cómo se observa el proceso;
- qué estadísticas existen;
- cómo se diagnostica un autovacuum insuficiente;
- cómo afecta a índices, almacenamiento, I/O y rendimiento.

---

## 3. SQL administrativo como competencia central del DBA

El PATH debe considerar **SQL administrativo** una competencia esencial de PostgreSQL Server Administration.

No debe tratarlo como una repetición del PATH general de SQL.

Un DBA PostgreSQL necesita utilizar SQL para interrogar y administrar el propio servidor.

Debe quedar clara la diferencia entre:

### SQL de aplicación

Ejemplos:

- modelar datos;
- desarrollar consultas funcionales;
- implementar lógica de negocio;
- construir informes;
- consultas de aplicación.

### SQL administrativo

Ejemplos:

- descubrir actividad del servidor;
- revisar configuración;
- analizar bloqueos;
- inspeccionar catálogos;
- comprobar replicación;
- observar WAL;
- investigar autovacuum;
- analizar estadísticas;
- medir tamaños;
- detectar objetos problemáticos;
- obtener información sobre sesiones;
- terminar backends cuando corresponda;
- diagnosticar rendimiento;
- investigar dependencias;
- comprobar privilegios;
- consultar metadatos;
- administrar objetos.

El alumno debe aprender a utilizar PostgreSQL como su propia interfaz de observabilidad.

---

## 4. Base `postgres` y databases administrativas

El curso debe explicar cuidadosamente que PostgreSQL no dispone de una única "base de administración" que contenga toda la configuración del cluster.

Debe explicar:

- `postgres`;
- `template0`;
- `template1`;
- databases de usuario;
- objetos globales;
- objetos locales a una database;
- catálogos replicados por database;
- información global del cluster;
- limitaciones de visibilidad entre databases.

Debe explicarse que `postgres` suele utilizarse como database convencional para tareas administrativas, pero no es una "DB de sistema" equivalente a modelos de otros productos.

El alumno debe comprender qué información pertenece:

- al cluster;
- a una database;
- a un schema;
- a un objeto;
- a una sesión;
- a un proceso.

---

## 5. Bloque obligatorio: Administración mediante SQL y catálogos

El PATH debe incluir explícitamente un bloque profundo dedicado a **Administración mediante SQL y catálogos PostgreSQL**.

Debe cubrir al menos:

### 5.1 Interfaz administrativa

- PostgreSQL como interfaz administrativa;
- SQL administrativo frente a SQL de aplicación;
- `psql` como consola DBA;
- database `postgres` como punto administrativo convencional;
- conexión a distintas databases;
- diferencias de visibilidad;
- objetos globales frente a objetos por database.

### 5.2 Catálogos y schemas del sistema

- `pg_catalog`;
- `information_schema`;
- system catalogs;
- system views;
- statistics views;
- funciones de información;
- funciones administrativas;
- OID;
- tipos `reg*`;
- dependencias entre objetos.

Debe cubrir al menos:

- `pg_database`;
- `pg_class`;
- `pg_attribute`;
- `pg_type`;
- `pg_namespace`;
- `pg_roles`;
- `pg_authid`;
- `pg_proc`;
- `pg_index`;
- `pg_constraint`;
- `pg_tablespace`;
- `pg_depend`;
- `pg_extension`;
- `pg_statistic`;
- `pg_statistic_ext`;
- `pg_settings`;
- `pg_file_settings`;
- `pg_hba_file_rules`;
- `pg_ident_file_mappings`.

### 5.3 Vistas administrativas

Debe cubrir de forma práctica y profunda:

- `pg_stat_activity`;
- `pg_locks`;
- `pg_stat_database`;
- `pg_stat_database_conflicts`;
- `pg_stat_all_tables`;
- `pg_stat_user_tables`;
- `pg_stat_sys_tables`;
- `pg_stat_all_indexes`;
- `pg_stat_user_indexes`;
- `pg_statio_*`;
- `pg_stat_wal`;
- `pg_stat_io`;
- `pg_stat_bgwriter` cuando corresponda por versión;
- `pg_stat_checkpointer`;
- `pg_stat_archiver`;
- `pg_stat_replication`;
- `pg_stat_wal_receiver`;
- `pg_replication_slots`;
- `pg_stat_subscription`;
- `pg_stat_subscription_stats` cuando corresponda;
- `pg_stat_ssl`;
- `pg_stat_gssapi` cuando corresponda;
- `pg_stat_progress_*`;
- `pg_backend_memory_contexts` cuando corresponda;
- otras vistas administrativas relevantes de la versión estudiada.

No se deben memorizar nombres sin explicar:

- qué mide cada vista;
- de dónde procede la información;
- cuándo se actualiza;
- si es acumulativa;
- cuándo se resetea;
- qué permisos requiere;
- qué problemas puede diagnosticar;
- qué limitaciones presenta.

### 5.4 Funciones administrativas

Debe incluir funciones para:

#### Tamaños

- `pg_database_size()`;
- `pg_table_size()`;
- `pg_indexes_size()`;
- `pg_total_relation_size()`;
- `pg_relation_size()`;
- `pg_size_pretty()`.

#### WAL

- `pg_current_wal_lsn()`;
- `pg_current_wal_insert_lsn()` cuando corresponda;
- `pg_wal_lsn_diff()`;
- `pg_walfile_name()`;
- funciones equivalentes vigentes en la versión estudiada.

#### Recovery y replicación

- `pg_is_in_recovery()`;
- `pg_last_wal_receive_lsn()`;
- `pg_last_wal_replay_lsn()`;
- `pg_last_xact_replay_timestamp()`;
- `pg_promote()`.

#### Procesos

- `pg_cancel_backend()`;
- `pg_terminate_backend()`;
- señalización segura;
- permisos;
- consecuencias operativas.

#### Configuración

- `current_setting()`;
- `set_config()`;
- `pg_reload_conf()`;
- funciones de configuración relevantes.

#### Objetos físicos

- `pg_relation_filepath()`;
- `pg_filenode_relation()`;
- funciones relacionadas con almacenamiento cuando proceda.

### 5.5 Descubrimiento del sistema

El alumno debe aprender a descubrir información sin depender exclusivamente de consultas memorizadas.

Debe saber utilizar:

- documentación oficial;
- `\?`;
- `\h`;
- `\d`;
- `\d+`;
- `\df`;
- `\dv`;
- `\du`;
- `\dn`;
- `\dx`;
- `\db`;
- `\conninfo`;
- `pg_catalog`;
- `information_schema`;
- funciones de descripción;
- comentarios del catálogo;
- introspección mediante SQL.

El objetivo es que el alumno pueda entrar en un PostgreSQL desconocido y construir consultas de diagnóstico por sí mismo.

---

## 6. DBA Toolbox SQL

El curso debe desarrollar progresivamente una **DBA Toolbox** de consultas reutilizables.

No debe presentarse como una colección de recetas sin explicación.

Cada consulta debe explicar:

- qué devuelve;
- por qué funciona;
- qué catálogos cruza;
- qué columnas son importantes;
- qué permisos necesita;
- qué problemas puede revelar;
- qué falsos positivos puede producir;
- cómo adaptar la consulta.

La toolbox debe incluir consultas para:

- sesiones;
- consultas activas;
- consultas idle;
- idle in transaction;
- sesiones largas;
- transacciones largas;
- bloqueos;
- blocker/blockee;
- deadlocks observables;
- tamaños;
- crecimiento;
- índices no utilizados;
- índices duplicados;
- tablas con muchas dead tuples;
- autovacuum;
- estadísticas;
- cache hit;
- temporary files;
- conexiones;
- WAL;
- replication lag;
- slots;
- checkpoints;
- archive failures;
- progress views;
- settings;
- parámetros modificados;
- parámetros pendientes de restart;
- objetos grandes;
- bloat aproximado cuando corresponda;
- extensiones;
- privilegios;
- ownership;
- dependencias;
- locks de mantenimiento;
- activity por usuario;
- activity por database;
- activity por aplicación;
- wait events.

El laboratorio final del bloque debe construir una **DBA toolbox exclusivamente mediante SQL y psql**.

---

## 7. Versiones de PostgreSQL

El PATH debe utilizar PostgreSQL moderno.

La documentación oficial vigente debe ser la referencia principal para comportamiento dependiente de versión.

Los libros:

- `Learn PostgreSQL, Second Edition`;
- `Mastering PostgreSQL 17`;
- `PostgreSQL 16 Administration Cookbook`;

son fuentes de aprendizaje, no una restricción de versión.

Cuando una funcionalidad haya cambiado entre PostgreSQL 16, 17, 18 o versiones posteriores utilizadas durante la generación, la lección debe:

1. enseñar el comportamiento actual;
2. indicar brevemente la diferencia relevante;
3. evitar procedimientos obsoletos;
4. utilizar la documentación oficial para confirmar sintaxis y semántica.

No debe enseñar opciones eliminadas como si siguieran vigentes.

---

## 8. Linux como plataforma operativa

PostgreSQL debe estudiarse principalmente sobre Linux.

Cuando se necesite contexto específico del sistema operativo, debe preferirse Fedora/RHEL.

Debe relacionarse PostgreSQL con:

- systemd;
- journald;
- firewalld;
- SELinux;
- filesystem;
- permisos;
- sockets;
- TCP/IP;
- procesos;
- señales;
- `/proc`;
- file descriptors;
- memoria virtual;
- page cache;
- I/O;
- storage;
- kernel;
- cgroups;
- resource limits;
- networking.

Sin embargo, el PATH no debe transformarse en un curso de Fedora.

Cuando un concepto sea propio de PostgreSQL, debe explicarse primero desde PostgreSQL.

Luego debe mostrarse la integración Linux/Fedora cuando aporte valor.

---

## 9. Instalación y layout

Las lecciones de instalación deben enseñar a descubrir el layout real del sistema y no asumir rutas universales.

Deben distinguir:

- paquetes Fedora/RHEL;
- repositorios PostgreSQL PGDG;
- instalaciones compiladas;
- diferencias de layout;
- ubicación de binaries;
- service units;
- `PGDATA`;
- archivos de configuración;
- ownership;
- permisos.

El alumno debe aprender a descubrir las rutas mediante herramientas como:

```bash
rpm -ql
rpm -qi
systemctl cat
systemctl show
pg_config
ps
```

cuando corresponda.

---

## 10. Arquitectura PostgreSQL

El PATH debe explicar progresivamente:

- proceso principal `postgres`;
- proceso por conexión;
- background processes;
- shared memory;
- local memory;
- checkpointer;
- WAL writer;
- background writer;
- autovacuum launcher;
- autovacuum workers;
- archiver;
- WAL sender;
- WAL receiver;
- logical replication workers;
- parallel workers;
- shared buffers;
- locks;
- LWLocks;
- latches;
- IPC.

El alumno debe ser capaz de correlacionar:

```text
cliente
→ conexión
→ backend PostgreSQL
→ PID
→ consulta
→ wait event
→ lock
→ I/O
→ proceso Linux
```

---

## 11. Configuración

La configuración debe enseñarse como sistema, no como catálogo de parámetros.

Debe incluir:

- `postgresql.conf`;
- `postgresql.auto.conf`;
- `ALTER SYSTEM`;
- `ALTER DATABASE ... SET`;
- `ALTER ROLE ... SET`;
- `SET`;
- `SHOW`;
- `RESET`;
- precedencia;
- contexts;
- reload;
- restart;
- `pending_restart`;
- includes;
- configuración modular.

Debe utilizarse `pg_settings` para comprender cada parámetro.

Cuando sea útil se deben estudiar:

- `name`;
- `setting`;
- `unit`;
- `category`;
- `short_desc`;
- `context`;
- `vartype`;
- `source`;
- `sourcefile`;
- `sourceline`;
- `pending_restart`.

No se deben recomendar valores "mágicos".

Toda recomendación de tuning debe depender del workload y ser medible.

---

## 12. Seguridad

La seguridad debe ser transversal.

Debe cubrir:

- usuario Linux `postgres`;
- permisos filesystem;
- ownership;
- roles;
- atributos de roles;
- membership;
- predefined roles;
- autenticación;
- `pg_hba.conf`;
- SCRAM;
- TLS;
- certificados;
- privilegios;
- ownership;
- schemas;
- `search_path`;
- `SECURITY DEFINER`;
- `SECURITY INVOKER`;
- Row Level Security;
- extensions;
- secretos;
- logging;
- auditoría;
- SELinux;
- firewalld;
- mínimo privilegio.

Debe explicar los límites de SUPERUSER y por qué no debe utilizarse innecesariamente.

---

## 13. MVCC

MVCC debe ser uno de los pilares conceptuales del PATH.

Debe enseñarse progresivamente desde nivel introductorio hasta internals.

Debe conectar:

- transactions;
- XID;
- snapshots;
- tuple versions;
- `xmin`;
- `xmax`;
- visibility;
- dead tuples;
- HOT;
- pruning;
- hint bits;
- VACUUM;
- freezing;
- wraparound;
- MultiXact;
- isolation;
- concurrency.

El alumno debe poder explicar por qué un `UPDATE` genera nuevas versiones y qué ocurre físicamente y lógicamente.

---

## 14. VACUUM y autovacuum

VACUUM no debe explicarse como una tarea periódica genérica.

Debe relacionarse con MVCC.

Debe cubrir:

- plain VACUUM;
- VACUUM FULL;
- ANALYZE;
- dead tuples;
- reclaiming reusable space;
- visibility map;
- freezing;
- XID wraparound;
- MultiXact;
- aggressive vacuum;
- failsafe;
- cost-based vacuum;
- thresholds;
- scale factors;
- configuración por tabla;
- workers;
- monitoring;
- bloat;
- I/O;
- workloads grandes.

Debe explicarse que desactivar autovacuum generalmente es peligroso.

---

## 15. WAL y checkpoints

WAL debe enseñarse desde concepto hasta internals.

Debe conectar:

```text
modificación
→ WAL record
→ WAL buffer
→ WAL flush
→ data page
→ checkpoint
→ crash recovery
→ replication
→ archiving
→ PITR
```

Debe cubrir:

- WAL records;
- LSN;
- segments;
- full-page writes;
- wal_level;
- buffers;
- compression;
- recycling;
- retention;
- checkpoints;
- crash recovery;
- archive;
- streaming replication;
- logical decoding.

Se debe utilizar `pg_waldump` cuando aporte valor.

---

## 16. Memoria

La memoria debe enseñarse evitando fórmulas simplistas.

Debe distinguir:

- memoria compartida;
- memoria por backend;
- memoria por operación;
- shared buffers;
- OS page cache;
- `work_mem`;
- `maintenance_work_mem`;
- `autovacuum_work_mem`;
- `temp_buffers`;
- `wal_buffers`;
- huge pages;
- dynamic shared memory;
- effective cache size.

Debe dejar claro que `work_mem` puede multiplicarse por:

- operaciones;
- nodos del plan;
- workers;
- sesiones.

El alumno debe aprender a modelar consumo de memoria y riesgo de OOM.

---

## 17. Almacenamiento e I/O

Debe relacionarse PostgreSQL con almacenamiento real.

Debe cubrir:

- pages;
- relation files;
- forks;
- FSM;
- VM;
- TOAST;
- WAL;
- fsync;
- page cache;
- SSD;
- NVMe;
- HDD;
- RAID;
- network storage;
- latency;
- IOPS;
- throughput;
- queueing;
- `pg_stat_io`.

No se deben hacer recomendaciones de filesystem o storage sin explicar el motivo.

---

## 18. Planner, executor y estadísticas

Aunque el PATH no sea un curso general de SQL, un DBA debe comprender el procesamiento de consultas.

Debe cubrir:

```text
SQL
→ parser
→ analyzer
→ rewriter
→ planner/optimizer
→ plan
→ executor
```

Debe enseñar:

- estadísticas;
- cardinality;
- histogramas;
- MCV;
- `n_distinct`;
- correlation;
- extended statistics;
- scan types;
- join algorithms;
- cost model;
- parallel plans;
- JIT;
- `EXPLAIN`;
- `EXPLAIN ANALYZE`.

El objetivo es diagnosticar problemas del servidor, no enseñar a desarrollar aplicaciones SQL.

---

## 19. Locks y concurrencia

Debe cubrir:

- table locks;
- row locks;
- advisory locks;
- predicate locks;
- heavyweight locks;
- LWLocks conceptualmente;
- wait events;
- compatibility;
- blocking;
- blockers;
- deadlocks;
- lock timeouts;
- statement timeouts;
- idle transaction timeout.

Debe enseñar a diagnosticar bloqueos mediante SQL.

Debe relacionarse:

```text
pg_stat_activity
+
pg_locks
+
PIDs
+
wait_event
```

---

## 20. Backups

Debe diferenciar claramente:

### Backup lógico

- `pg_dump`;
- `pg_dumpall`;
- `pg_restore`;
- formatos;
- parallel dump;
- parallel restore;
- globals;
- roles;
- ownership;
- privileges.

### Backup físico

- base backups;
- `pg_basebackup`;
- WAL;
- backup manifests;
- `pg_verifybackup`;
- tablespaces;
- standby backups;
- consistency.

Debe enseñarse que un backup no está validado hasta haber probado su restauración.

---

## 21. PITR y disaster recovery

PITR debe comprenderse a partir de:

```text
base backup
+
WAL archive
+
recovery configuration
=
Point-in-Time Recovery
```

Debe cubrir:

- recovery targets;
- time;
- XID;
- LSN;
- named restore points;
- timelines;
- promotion;
- recovery actions;
- restore validation.

DR debe incluir:

- RPO;
- RTO;
- runbooks;
- offsite backup;
- inmutabilidad cuando proceda;
- cifrado;
- restore testing;
- simulacros.

---

## 22. Replicación física

Debe explicarse profundamente:

- primary;
- standby;
- WAL sender;
- WAL receiver;
- streaming;
- async;
- sync;
- hot standby;
- replication lag;
- LSN;
- slots;
- cascading;
- timelines;
- promotion.

El alumno debe comprender qué datos se transmiten y por qué la replicación física es diferente de la lógica.

---

## 23. Replicación síncrona

Debe enseñar los trade-offs:

```text
latencia
vs
durabilidad
vs
disponibilidad
```

Debe cubrir cuando corresponda:

- `synchronous_commit`;
- `synchronous_standby_names`;
- FIRST;
- ANY;
- quorum;
- `remote_write`;
- `on`;
- `remote_apply`.

No debe presentarse como una opción simplemente "mejor".

---

## 24. Replication slots

Debe cubrir:

- physical slots;
- logical slots;
- `restart_lsn`;
- `confirmed_flush_lsn`;
- WAL retention;
- inactive slots;
- límites;
- failover slots cuando estén disponibles;
- riesgo de llenar disco.

Debe haber laboratorios donde se provoque de forma segura retención excesiva de WAL.

---

## 25. Failover, switchover y HA

Debe diferenciar claramente:

- failover;
- switchover;
- promotion;
- rejoin;
- rewind;
- fencing;
- split brain.

Debe enseñar primero failover manual antes de automatizarlo.

Herramientas externas como:

- Patroni;
- etcd;
- Consul;
- HAProxy;
- PgBouncer;

deben introducirse después de comprender la mecánica PostgreSQL subyacente.

---

## 26. Replicación lógica

Debe cubrir:

- logical decoding;
- publication;
- subscription;
- replication identity;
- initial synchronization;
- workers;
- slots;
- conflicts;
- DDL limitations;
- sequences;
- row filters;
- column lists;
- monitoring.

Debe compararse con replicación física.

---

## 27. Monitoring y observabilidad

El alumno debe aprender a construir observabilidad a partir de PostgreSQL antes de depender de productos externos.

Debe dominar:

- `pg_stat_activity`;
- `pg_stat_database`;
- `pg_stat_user_tables`;
- `pg_stat_user_indexes`;
- `pg_stat_io`;
- `pg_stat_wal`;
- `pg_stat_replication`;
- `pg_stat_archiver`;
- `pg_stat_progress_*`;
- `pg_locks`;
- `pg_stat_statements`.

Después pueden integrarse:

- Prometheus;
- postgres_exporter;
- Grafana.

Debe relacionarse métricas PostgreSQL con métricas Linux.

---

## 28. Logging

Debe enseñar:

- qué registrar;
- qué no registrar;
- volumen;
- impacto;
- privacidad;
- seguridad;
- rotación;
- correlación.

Debe cubrir cuando proceda:

- stderr;
- csvlog;
- jsonlog;
- syslog;
- `log_line_prefix`;
- connection logs;
- disconnection logs;
- slow statements;
- checkpoints;
- autovacuum;
- temp files;
- lock waits.

Debe poder correlacionarse:

```text
timestamp
PID
database
user
application
session
statement
```

---

## 29. Performance tuning

No debe enseñarse tuning como una lista de valores recomendados.

Debe seguir:

```text
medir
→ identificar cuello de botella
→ formular hipótesis
→ cambiar una variable controlada
→ volver a medir
→ validar
```

Debe separar:

- CPU-bound;
- memory-bound;
- I/O-bound;
- lock-bound;
- connection-bound;
- WAL-bound;
- checkpoint-bound.

Debe cubrir:

- server configuration;
- SQL diagnosis;
- indexes;
- statistics;
- autovacuum;
- WAL;
- checkpoints;
- memory;
- connection pooling;
- OS.

---

## 30. Benchmarking

`pgbench` debe utilizarse para enseñar metodología, no únicamente comandos.

Debe cubrir:

- scale factor;
- clients;
- threads;
- duration;
- TPS;
- latency;
- custom scripts;
- read workloads;
- write workloads;
- reproducibility;
- warm cache;
- cold cache;
- saturation.

Debe distinguir benchmarks sintéticos de workloads reales.

---

## 31. Troubleshooting

El troubleshooting debe enseñarse sistemáticamente.

Modelo:

```text
síntoma
→ alcance
→ cambios recientes
→ métricas
→ PostgreSQL
→ SQL
→ OS
→ storage
→ red
→ hipótesis
→ evidencia
→ corrección
→ validación
```

Debe cubrir incidentes como:

- servidor no inicia;
- connection refused;
- authentication failure;
- too many connections;
- slow queries;
- CPU elevada;
- OOM;
- I/O elevada;
- disk full;
- pg_wal growing;
- replication lag;
- autovacuum failure;
- wraparound;
- locks;
- deadlocks;
- temp file explosion;
- checkpoint storms;
- crashes;
- corruption.

---

## 32. Corrupción e integridad

Debe enseñarse con extremo cuidado.

Debe cubrir:

- checksums;
- `pg_checksums`;
- `amcheck`;
- `pg_amcheck`;
- `pageinspect`;
- index corruption;
- heap corruption;
- hardware errors;
- storage errors;
- memory errors;
- backups.

`pg_resetwal` debe enseñarse claramente como una herramienta de último recurso y potencialmente destructiva.

Nunca debe presentarse como reparación rutinaria.

---

## 33. Upgrades

Debe diferenciar:

- minor upgrades;
- major upgrades.

Debe cubrir:

- backup previo;
- compatibility;
- extensions;
- `pg_upgrade`;
- `pg_upgrade --check`;
- dump/restore;
- logical replication;
- downtime;
- rollback;
- testing;
- validation.

Debe explicar que un upgrade no termina cuando PostgreSQL arranca: deben validarse datos, extensiones, estadísticas y rendimiento.

---

## 34. Automatización

La automatización debe introducirse después de comprender manualmente las operaciones.

Debe cubrir:

- shell;
- `psql`;
- exit codes;
- idempotencia;
- systemd timers;
- cron;
- Ansible;
- secrets;
- logging;
- validation.

Nunca debe automatizarse una operación que el alumno todavía no comprende.

---

## 35. Internals

El nivel experto debe incluir internals relevantes para DBA.

No se pretende convertir al alumno en desarrollador core de PostgreSQL, pero sí darle capacidad de razonar sobre el comportamiento interno.

Debe incluir:

- storage manager;
- heap;
- tuple layout;
- page layout;
- FSM;
- VM;
- TOAST;
- buffer manager;
- XID;
- snapshots;
- `pg_xact`;
- subtransactions;
- MultiXact;
- WAL internals;
- REDO;
- crash recovery;
- locks;
- ProcArray;
- query processing;
- memory contexts;
- resource owners.

Debe utilizar código fuente cuando ayude a explicar un comportamiento real.

---

## 36. Código fuente

En el nivel avanzado el alumno debe aprender a navegar:

- `src/backend`;
- `src/include`;
- `src/bin`;
- `contrib`.

Debe poder:

- compilar PostgreSQL;
- activar assertions cuando proceda;
- generar símbolos;
- utilizar gdb conceptualmente;
- obtener stack traces;
- relacionar una función interna con un comportamiento observado.

No se requiere desarrollar PostgreSQL Core para completar el PATH.

---

## 37. Herramientas del sistema para diagnóstico

Cuando aporte valor, el curso puede utilizar:

- `ps`;
- `top`;
- `htop`;
- `pidstat`;
- `vmstat`;
- `iostat`;
- `ss`;
- `lsof`;
- `strace`;
- `perf`;
- `/proc`;
- journalctl;
- systemctl.

Estas herramientas deben utilizarse para correlacionar PostgreSQL con Linux.

No deben sustituir las herramientas de observabilidad propias de PostgreSQL.

---

## 38. pg_stat_statements

`pg_stat_statements` debe tratarse como herramienta DBA fundamental.

Debe cubrir:

- instalación;
- `shared_preload_libraries`;
- extensión;
- queryid;
- calls;
- execution time;
- planning time cuando corresponda;
- blocks;
- WAL;
- temporary blocks;
- reset;
- normalización;
- top queries;
- limitaciones.

Debe evitarse interpretar una única métrica de forma aislada.

---

## 39. PgBouncer

Connection pooling debe enseñarse después de comprender el modelo proceso-por-conexión de PostgreSQL.

Debe cubrir:

- coste de conexiones;
- session pooling;
- transaction pooling;
- statement pooling;
- compatibilidad;
- prepared statements;
- pool sizing;
- HA;
- monitoring.

Debe explicarse qué semánticas pueden romperse en transaction pooling.

---

## 40. Particionamiento

Debe abordarse desde perspectiva administrativa.

Debe cubrir:

- range;
- list;
- hash;
- pruning;
- attach;
- detach;
- maintenance;
- indexes;
- constraints;
- statistics;
- autovacuum;
- backup;
- lifecycle.

Debe evitarse presentar particionamiento como solución universal de rendimiento.

---

## 41. Extensiones

Debe cubrir:

- extension lifecycle;
- `CREATE EXTENSION`;
- upgrades;
- dependencies;
- packages;
- preload requirements;
- security;
- compatibility with major upgrades.

Extensiones DBA importantes pueden incluir:

- `pg_stat_statements`;
- `pgstattuple`;
- `pageinspect`;
- `amcheck`;
- `postgres_fdw`;
- `pg_trgm`;

cuando sean relevantes.

---

## 42. Capacity planning

Debe cubrir capacidad desde datos medibles.

El alumno debe aprender a estimar:

- CPU;
- RAM;
- storage;
- IOPS;
- throughput;
- WAL rate;
- growth rate;
- number of connections;
- TPS;
- backup window;
- restore window;
- replication bandwidth;
- autovacuum capacity;
- headroom.

No deben recomendarse tamaños de hardware arbitrarios.

---

## 43. Alta disponibilidad

HA debe enseñarse después de replicación y recovery.

Debe quedar claro que replicación no equivale automáticamente a HA.

Debe cubrir:

- SPOF;
- quorum;
- consensus;
- leader election;
- fencing;
- split brain;
- client routing;
- topology;
- failover;
- reintegration.

Debe analizar consecuencias de fallos parciales de red.

---

## 44. Operación de producción

El nivel experto debe incluir disciplina operativa:

- runbooks;
- change management;
- maintenance windows;
- patching;
- upgrade planning;
- backup testing;
- DR drills;
- failover drills;
- incident response;
- postmortems;
- capacity reviews;
- security reviews;
- performance reviews.

---

## 45. Laboratorios

Los laboratorios son obligatorios cuando el tema permita experimentación práctica.

Deben preferirse laboratorios reproducibles.

Cada laboratorio debe indicar:

- objetivo;
- entorno;
- comandos;
- SQL;
- resultados esperados;
- observaciones;
- cómo verificar;
- cómo revertir cuando proceda.

Los laboratorios de riesgo deben utilizar entornos desechables.

Nunca se debe sugerir provocar corrupción, pérdida de datos o failover destructivo en producción.

---

## 46. Errores frecuentes

Cuando exista valor pedagógico, debe incluirse:

### ⚠️ Errores frecuentes

Debe explicar errores reales como:

- confundir reload con restart;
- editar el archivo equivocado;
- utilizar trust innecesariamente;
- utilizar SUPERUSER para aplicaciones;
- ignorar `search_path`;
- desactivar autovacuum;
- aumentar `max_connections` sin analizar memoria;
- sobredimensionar `work_mem`;
- ignorar replication slots;
- no validar backups;
- usar VACUUM FULL rutinariamente;
- interpretar cache hit ratio de forma aislada;
- hacer tuning sin baseline;
- borrar manualmente archivos de `pg_wal`;
- ejecutar `pg_resetwal` como solución rápida;
- promover un standby sin entender timelines;
- automatizar failover sin fencing.

---

## 47. Descubrimiento antes que memorización

Un objetivo transversal es enseñar al alumno a descubrir.

Debe aprender a responder:

- ¿qué proceso está haciendo esto?;
- ¿qué parámetro controla este comportamiento?;
- ¿de dónde procede este valor?;
- ¿qué archivo está utilizando PostgreSQL?;
- ¿qué vista puede mostrarlo?;
- ¿qué función administrativa existe?;
- ¿qué permisos necesito?;
- ¿qué documentación corresponde a mi versión?;
- ¿qué cambió entre versiones?;
- ¿qué objeto físico corresponde a esta tabla?;
- ¿qué backend corresponde a este PID?;
- ¿qué sesión está bloqueando a otra?;
- ¿qué generó este WAL?;
- ¿qué produjo este I/O?.

Este principio debe evitar cursos basados en memorizar recetas.

---

## 48. Documentación oficial

La documentación oficial de PostgreSQL debe tener autoridad máxima para:

- sintaxis;
- semántica;
- defaults;
- parámetros;
- compatibilidad;
- comportamiento dependiente de versión;
- funciones;
- vistas;
- catálogos;
- utilities;
- recovery;
- replication;
- internals documentados.

Si un libro entra en conflicto con la documentación vigente, debe prevalecer la documentación de PostgreSQL correspondiente a la versión estudiada.

---

## 49. Uso de los libros

### Learn PostgreSQL, Second Edition

Debe utilizarse principalmente para:

- introducción;
- fundamentos;
- arquitectura inicial;
- SQL necesario para administración;
- objetos;
- administración básica;
- conceptos PostgreSQL.

### Mastering PostgreSQL 17

Debe adquirir mayor peso en:

- MVCC;
- concurrencia;
- locks;
- performance;
- planner;
- estadísticas;
- indexing;
- WAL;
- replication;
- internals;
- arquitectura avanzada.

### PostgreSQL 16 Administration Cookbook

Debe utilizarse como fuente práctica para:

- administración;
- configuración;
- seguridad;
- backups;
- recovery;
- replication;
- maintenance;
- monitoring;
- troubleshooting;
- operaciones.

No se debe copiar la estructura de los libros.

Los libros son referencias para construir un itinerario pedagógico coherente.

---

## 50. Formato pedagógico obligatorio

Cada lección debe comenzar con:

# 🎯 OBJETIVO

Debe describir concretamente qué comprenderá o podrá hacer el alumno.

Después debe desarrollarse el tema con profundidad.

Cuando aporte valor pueden utilizarse:

- 🧪 Laboratorio / ejemplos;
- ⚠️ Errores frecuentes;
- 💡 Idea importante.

Cada lección debe terminar siempre con:

# 🧠 QUÉ DEBES RECORDAR

Debe contener entre 3 y 7 ideas fundamentales.

No debe ser una repetición textual del objetivo.

Debe sintetizar los conceptos que el alumno necesita retener.

---

## 51. Profundidad

No generar resúmenes superficiales.

Una lección debe explicar lo suficiente para comprender el mecanismo estudiado y poder utilizarlo operativamente.

Cuando un tema sea complejo, debe avanzar en capas:

```text
concepto
→ arquitectura
→ observación
→ configuración
→ laboratorio
→ troubleshooting
→ internals cuando corresponda
```

No debe introducir todos los detalles internos prematuramente.

La dificultad debe crecer con el PATH.

---

## 52. Comandos y SQL

Todo comando debe ser realista.

Ejemplo shell:

```bash
sudo -u postgres psql
```

Ejemplo SQL:

```sql
SELECT
    pid,
    usename,
    datname,
    application_name,
    client_addr,
    state,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity;
```

Cuando un comando pueda ser peligroso debe explicarse antes de utilizarlo.

No se deben inventar opciones.

---

## 53. Privilegios en ejemplos

Los ejemplos deben utilizar el menor privilegio posible.

Debe distinguirse claramente cuándo se requiere:

- usuario Linux `postgres`;
- owner de database;
- owner de objeto;
- role administrativa;
- `pg_monitor`;
- `pg_signal_backend`;
- superuser.

No asumir SUPERUSER de manera automática.

---

## 54. Compatibilidad con Fedora/RHEL

Cuando se enseñe integración con Fedora/RHEL debe considerarse:

- systemd;
- RPM;
- SELinux;
- firewalld;
- journald;
- crypto policies cuando proceda.

Debe evitarse enseñar desactivar SELinux o firewalld como solución genérica.

La solución correcta debe integrarse con los mecanismos de seguridad del sistema.

---

## 55. Evitar dependencias innecesarias

El PATH debe enseñar primero las herramientas nativas de PostgreSQL.

Ejemplos:

Antes de Prometheus:

- `pg_stat_*`.

Antes de Patroni:

- streaming replication;
- promotion;
- failover;
- timelines;
- fencing.

Antes de pgBackRest/Barman si se introducen posteriormente:

- `pg_basebackup`;
- WAL archive;
- PITR;
- backup validation.

Antes de ORMs o frameworks:

- no son necesarios para la administración.

---

## 56. Herramientas externas

Las herramientas externas pueden introducirse si aportan valor operativo, pero deben quedar claramente diferenciadas de PostgreSQL Core.

Ejemplos:

- PgBouncer;
- Patroni;
- etcd;
- HAProxy;
- Prometheus;
- Grafana;
- postgres_exporter;
- pgBackRest;
- Barman;
- pg_repack;
- pgaudit.

Debe explicarse:

- qué problema resuelven;
- por qué PostgreSQL Core no cubre exactamente ese problema;
- arquitectura;
- riesgos;
- dependencia operacional.

---

## 57. SQL suficiente, no duplicado

No repetir innecesariamente el PATH general de SQL.

El alumno puede necesitar SQL como:

- SELECT;
- joins;
- aggregation;
- CTE;
- subqueries;
- functions;
- filtering;

para construir consultas administrativas.

Cuando sea necesario, estas construcciones pueden recordarse brevemente dentro de una lección.

No deben convertirse en capítulos generales de enseñanza de SQL salvo que sean imprescindibles para la administración.

---

## 58. Proyecto final

El proyecto final debe representar una plataforma PostgreSQL de producción completa.

Debe integrar:

```text
Linux
+
PostgreSQL
+
seguridad
+
configuración
+
monitorización
+
backups
+
PITR
+
replicación
+
HA
+
performance
+
automatización
+
runbooks
+
DR
```

Debe incluir fallos simulados.

Debe obligar al alumno a diagnosticar problemas utilizando:

- SQL administrativo;
- system catalogs;
- `pg_stat_*`;
- logs;
- tools PostgreSQL;
- herramientas Linux.

El proyecto debe validar que el alumno puede operar PostgreSQL y no simplemente instalarlo.

---

## 59. Resultado esperado del PATH

Al finalizar, el alumno debe ser capaz de:

- instalar PostgreSQL;
- inicializar y organizar clusters;
- comprender `PGDATA`;
- administrar múltiples databases;
- administrar roles;
- diseñar autenticación;
- configurar TLS;
- aplicar mínimo privilegio;
- entender MVCC;
- administrar VACUUM/autovacuum;
- interpretar estadísticas;
- diagnosticar locks;
- entender WAL;
- ajustar checkpoints;
- dimensionar memoria;
- diagnosticar I/O;
- gestionar tablespaces;
- mantener índices;
- utilizar `EXPLAIN`;
- utilizar `pg_stat_statements`;
- analizar sesiones;
- construir SQL administrativo;
- navegar catálogos;
- descubrir funciones administrativas;
- realizar backups;
- verificar backups;
- ejecutar PITR;
- administrar replicación;
- medir lag;
- manejar replication slots;
- ejecutar failover;
- ejecutar switchover;
- utilizar `pg_rewind`;
- comprender HA;
- administrar replicación lógica;
- monitorizar;
- hacer capacity planning;
- benchmarkear;
- diagnosticar incidentes;
- detectar corrupción;
- ejecutar upgrades;
- planificar migraciones;
- automatizar operaciones;
- correlacionar PostgreSQL con Linux;
- entender internals relevantes;
- navegar el código fuente cuando sea necesario;
- diseñar y operar una plataforma PostgreSQL de producción.

El objetivo final no es memorizar PostgreSQL.

El objetivo es **comprenderlo suficientemente bien como para investigar, administrar y diagnosticar sistemas PostgreSQL reales con criterio técnico**.
