# Bibliografía — PostgreSQL Server Administration

## Referencia principal y autoritativa

### PostgreSQL Official Documentation

Uso: referencia transversal y fuente principal para cualquier comportamiento dependiente de versión.

Prioridad: máxima.

Debe consultarse especialmente para:

- instalación e inicialización
- server configuration
- client authentication
- roles y privilegios
- runtime configuration
- WAL
- checkpoints
- backup y restore
- continuous archiving
- PITR
- streaming replication
- replication slots
- logical replication
- system catalogs
- statistics collector / cumulative statistics
- monitoring
- VACUUM y autovacuum
- concurrency control
- transaction isolation
- locking
- query planning
- EXPLAIN
- extensions
- FDW
- pg_upgrade
- server administration
- internals documentados

URL base:

https://www.postgresql.org/docs/current/

Regla de uso:

Para opciones, parámetros, vistas, defaults y comportamiento que pueda cambiar entre versiones, comprobar siempre la documentación de la versión objetivo antes de afirmarlo como vigente.


## Libro 1 — Introducción y fundamentos

### Learn PostgreSQL, Second Edition

Rol: introducción estructurada y formación de base.

Uso principal aproximado:

- fundamentos PostgreSQL
- arquitectura conceptual
- instalación
- databases
- schemas
- users y roles
- seguridad básica
- objetos PostgreSQL
- administración inicial
- consultas necesarias para comprender el servidor
- introducción a transacciones
- introducción a índices
- backup y tareas comunes

Bloques donde tendrá mayor peso:

0–16 aproximadamente, reutilizándose posteriormente cuando aporte claridad didáctica.

No debe utilizarse como única referencia para funcionalidades que hayan evolucionado en versiones modernas de PostgreSQL.


## Libro 2 — Administración e internals avanzados

### Mastering PostgreSQL 17

Rol: fuente principal de profundización técnica y administración avanzada.

Uso especialmente importante para:

- arquitectura PostgreSQL
- MVCC
- transacciones
- locks
- concurrencia
- VACUUM
- autovacuum
- planner
- optimizer
- EXPLAIN
- índices
- performance
- memory management
- WAL
- replication
- internals
- troubleshooting
- extensibilidad
- comportamiento avanzado del servidor

Bloques donde tendrá mayor peso:

16–30
39–53
58–73

Debe cruzarse con la documentación oficial, especialmente en parámetros y funcionalidades dependientes de PostgreSQL 17 o posteriores.


## Libro 3 — Operación y recetas administrativas

### PostgreSQL 16 Administration Cookbook

Rol: fuente práctica para operación cotidiana, escenarios de administración y procedimientos reproducibles.

Uso especialmente importante para:

- instalación
- configuración
- administración de roles
- seguridad
- logging
- backup
- restore
- monitoring
- maintenance
- replication
- HA
- troubleshooting
- upgrades
- automatización
- tareas operativas de DBA

Bloques donde tendrá peso destacado:

1–15
18–19
31–48
54–66
74–81

Las recetas deben explicarse, no copiarse como comandos sin contexto.

Cada procedimiento debe responder, cuando proceda:

- por qué se hace
- qué modifica
- qué riesgo tiene
- cómo verificarlo
- cómo revertirlo
- cómo cambia entre versiones


## Bibliografía complementaria recomendada

### PostgreSQL Wiki

Uso:

- prácticas operativas
- troubleshooting
- tooling
- información histórica útil

Debe considerarse complementaria y verificarse frente a la documentación oficial cuando el contenido sea antiguo.


### PostgreSQL Source Code

Repositorio oficial del proyecto PostgreSQL.

Uso:

- internals
- comportamiento no suficientemente claro en documentación
- almacenamiento
- WAL
- locks
- planner
- executor
- procesos backend
- herramientas pg_*

Especialmente relevante para los bloques 67–73.

El objetivo no es convertir todas las lecciones en lectura de código, sino utilizar el código fuente como autoridad técnica cuando sea necesario.


### PostgreSQL CommitFest / mailing lists / release notes

Uso selectivo para:

- comprender cambios entre releases
- novedades de arquitectura
- deprecations
- comportamiento recientemente introducido

No deben sustituir a la documentación oficial para formación básica.


## Documentación Linux/Fedora/RHEL

### Fedora Documentation

Uso:

- paquetes
- systemd
- SELinux
- firewalld
- integración con Fedora


### Red Hat Enterprise Linux Documentation

Uso:

- systemd
- SELinux
- firewalld
- performance tuning
- storage
- administración de servicios


### systemd documentation

Uso:

- units
- service management
- limits
- hardening
- journald


### Linux kernel documentation

Uso avanzado:

- memory management
- huge pages
- VM
- I/O
- process limits
- filesystem behavior
- networking relevante


## Herramientas y documentación complementaria

### PgBouncer documentation

Uso:

- connection pooling
- session / transaction pooling
- límites operativos
- prepared statements
- HA


### Patroni documentation

Uso:

- alta disponibilidad
- leader election
- failover
- switchover
- DCS
- PostgreSQL HA automation

Debe enseñarse después de comprender replicación nativa, timelines, promotion, slots, fencing y pg_rewind.


### etcd documentation

Uso:

- distributed configuration store
- consensus conceptual
- quorum
- Patroni

Solo en el contexto necesario para operar HA PostgreSQL.


### HAProxy documentation

Uso:

- routing de conexiones
- health checks
- acceso a primary/standby
- integración HA


### Prometheus documentation

Uso:

- métricas
- scraping
- alerting


### postgres_exporter documentation

Uso:

- exposición de métricas PostgreSQL para Prometheus


### Grafana documentation

Uso:

- visualización
- dashboards
- observabilidad


### pgBackRest documentation

Bibliografía adicional recomendada para una futura ampliación del PATH.

Uso potencial:

- backup físico
- WAL archive
- restore
- retention
- parallel backup
- repositorios remotos
- cifrado

Debe distinguirse siempre qué funcionalidad pertenece al core PostgreSQL y cuál pertenece a pgBackRest.


### Barman documentation

Bibliografía adicional recomendada para estrategias de backup/DR externas.

Debe explicarse después de dominar pg_basebackup, WAL archiving y PITR nativos.


## Distribución orientativa de fuentes por nivel

### Nivel 0 — Fundamentos

Principal:

- Learn PostgreSQL, Second Edition

Apoyo:

- PostgreSQL Official Documentation


### Nivel principiante — Administración básica

Principal:

- Learn PostgreSQL, Second Edition
- PostgreSQL 16 Administration Cookbook

Referencia:

- PostgreSQL Official Documentation


### Nivel intermedio — Operación real

Principal:

- PostgreSQL 16 Administration Cookbook
- Mastering PostgreSQL 17

Referencia:

- PostgreSQL Official Documentation


### Nivel avanzado — Rendimiento, replicación y HA

Principal:

- Mastering PostgreSQL 17
- PostgreSQL Official Documentation

Práctica:

- PostgreSQL 16 Administration Cookbook

Complementaria:

- PgBouncer
- Patroni
- etcd
- HAProxy
- Prometheus/Grafana


### Nivel experto — Internals y diagnóstico

Principal:

- PostgreSQL Official Documentation
- Mastering PostgreSQL 17
- PostgreSQL source code

Complementaria:

- Linux kernel documentation
- Fedora/RHEL documentation
- release notes
- mailing lists cuando aporten contexto técnico


## Política de versiones

El material bibliográfico incluye libros centrados en PostgreSQL 16 y PostgreSQL 17.

Esto no significa que el PATH deba congelarse en esas versiones.

Regla:

1. usar los libros para explicar principios y procedimientos
2. verificar en documentación oficial el comportamiento actual
3. adaptar nombres, defaults y funcionalidades a la versión objetivo
4. explicar diferencias cuando sean pedagógicamente relevantes
5. evitar procedimientos obsoletos aunque aparezcan en una edición anterior


## Prioridad de resolución de discrepancias

Cuando dos fuentes contradigan un comportamiento técnico actual, utilizar este orden:

1. documentación oficial de la versión PostgreSQL objetivo
2. release notes oficiales
3. código fuente PostgreSQL cuando sea necesario
4. Mastering PostgreSQL 17
5. PostgreSQL 16 Administration Cookbook
6. Learn PostgreSQL, Second Edition
7. fuentes comunitarias


## Uso pedagógico de la bibliografía

La bibliografía no debe provocar lecciones que sean resúmenes de capítulos.

Las fuentes se utilizan para construir una explicación coherente alrededor de la lección concreta definida en el PATH.

Cada lección debe poder combinar varias fuentes cuando sea necesario.

La selección debe priorizar comprensión, precisión técnica, observabilidad y aplicación práctica.
