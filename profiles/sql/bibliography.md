# BIBLIOGRAPHY — SQL DE 0 A EXPERTO
## SQL estándar + PostgreSQL como implementación principal

## Política bibliográfica

La documentación oficial de PostgreSQL es la fuente operativa principal.

Las obras de teoría relacional y SQL estándar se utilizan para evitar confundir el lenguaje SQL
con un dialecto concreto.

Los libros específicos de PostgreSQL complementan, pero no sustituyen, a la documentación oficial.

Las referencias exactas de capítulo/sección sólo deben incluirse cuando estén verificadas. Si no
se ha comprobado una localización exacta, citar la obra sin inventar capítulo o página.

## 1. Principal — PostgreSQL

### PostgreSQL Global Development Group
**PostgreSQL 18 Documentation**

Uso principal durante todo el PATH.

Áreas especialmente importantes:

- Tutorial;
- The SQL Language;
- Data Definition;
- Data Manipulation;
- Queries;
- Data Types;
- Functions and Operators;
- Type Conversion;
- Indexes;
- Full Text Search;
- Concurrency Control;
- Performance Tips;
- Parallel Query;
- Client Authentication;
- Database Roles;
- Managing Databases;
- Monitoring Database Activity;
- Routine Database Maintenance Tasks;
- Backup/restore cuando el PATH lo necesite como contexto;
- Server Programming;
- Internals;
- SQL Commands;
- `psql`.

Regla: ante dudas sobre sintaxis o comportamiento PostgreSQL, esta documentación tiene prioridad.

## 2. Normativa — SQL estándar

### ISO/IEC 9075 — Database languages — SQL

Referencia normativa para distinguir SQL estándar de extensiones PostgreSQL.

Utilizar especialmente para:

- terminología;
- sintaxis estándar;
- joins;
- set operations;
- window functions;
- recursive queries;
- MERGE;
- SQL/JSON;
- portabilidad.

No reproducir texto protegido de la norma. Usarla como referencia conceptual/normativa.

### C. J. Date; Hugh Darwen
**A Guide to the SQL Standard, 4th Edition**

Obra clásica para comprender SQL desde la perspectiva del estándar.

Uso:

- diferencias entre modelo relacional y SQL;
- semántica;
- NULL;
- constraints;
- lenguaje estándar;
- portabilidad.

## 3. Teoría relacional y diseño

### C. J. Date
**An Introduction to Database Systems, 8th Edition**

Profundización en:

- modelo relacional;
- álgebra relacional;
- integridad;
- dependencias;
- normalización;
- teoría de bases de datos.

### Ramez Elmasri; Shamkant B. Navathe
**Fundamentals of Database Systems**

Complementaria para:

- modelado conceptual;
- ER;
- modelo relacional;
- diseño lógico;
- normalización;
- transacciones;
- arquitectura de DBMS.

### Abraham Silberschatz; Henry F. Korth; S. Sudarshan
**Database System Concepts**

Complementaria para:

- teoría de bases de datos;
- almacenamiento;
- índices;
- transacciones;
- concurrencia;
- recuperación;
- query processing;
- query optimization.

## 4. SQL práctico y avanzado

### Joe Celko
**Joe Celko's SQL for Smarties: Advanced SQL Programming**

Profundización para patrones SQL avanzados, razonamiento declarativo y transformaciones.

Usar con criterio: contrastar siempre cualquier comportamiento dependiente del dialecto con
PostgreSQL actual.

### Joe Celko
**SQL Programming Style**

Consulta para claridad, estilo y diseño de SQL mantenible.

### Bill Karwin
**SQL Antipatterns**

Útil para:

- modelado;
- consultas;
- NULL;
- claves;
- relaciones;
- EAV;
- diseño de aplicaciones alrededor de SQL;
- anti-patterns.

Las recomendaciones deben contrastarse con PostgreSQL actual y el contexto concreto.

## 5. PostgreSQL — profundización general

### Hans-Jürgen Schönig
**Mastering PostgreSQL 17**

Complementaria importante para PostgreSQL avanzado:

- SQL avanzado;
- índices;
- optimización;
- concurrencia;
- administración relacionada con rendimiento;
- características específicas de PostgreSQL.

Usarla como complemento de la documentación PostgreSQL 18; cuando exista discrepancia, prevalece
la documentación de la versión objetivo.

### Ryan Booz; Grant Fritchey
**Introduction to PostgreSQL for the Data Professional**

Complementaria para conectar fundamentos SQL con PostgreSQL moderno.

### Jimmy Angelakos
**PostgreSQL Mistakes and How to Avoid Them**

Complementaria para revisión, anti-patterns y diagnóstico.

## 6. PostgreSQL — administración relacionada con este PATH

### Gianni Ciolli; Boriss Mejías; Jimmy Angelakos; Vibhor Kumar; Simon Riggs
**PostgreSQL 16 Administration Cookbook**

Uso complementario para:

- mantenimiento;
- monitorización;
- VACUUM;
- configuración;
- seguridad;
- troubleshooting.

Este PATH no es un curso completo de administración; utilizar sólo los capítulos relevantes para
SQL, rendimiento, concurrencia, observabilidad e internals.

### PostgreSQL Global Development Group
**PostgreSQL 18 Server Administration documentation**

Fuente preferente cuando una lección entra en:

- server configuration;
- runtime statistics;
- VACUUM;
- WAL;
- checkpoints;
- roles;
- authentication;
- monitoring.

## 7. Rendimiento e índices

### Markus Winand
**SQL Performance Explained**

Referencia de profundización para:

- B-tree;
- acceso mediante índices;
- índices multicolumna;
- joins;
- sorting;
- execution plans;
- SQL performance.

Importante: es una obra multi-DBMS. Separar los conceptos generales del comportamiento concreto de
PostgreSQL.

### Markus Winand
**Use The Index, Luke!**

Consulta práctica para fundamentos de indexación y SQL performance.

### PostgreSQL Global Development Group
**PostgreSQL 18 — Performance Tips**

Fuente principal para:

- EXPLAIN;
- estadísticas;
- planner;
- join strategies;
- plan interpretation.

### PostgreSQL Global Development Group
**PostgreSQL 18 — Indexes**

Fuente principal para:

- B-tree;
- Hash;
- GiST;
- SP-GiST;
- GIN;
- BRIN;
- multicolumn indexes;
- unique indexes;
- expression indexes;
- partial indexes;
- index-only scans;
- operator classes.

## 8. Planner, query processing e internals

### PostgreSQL Global Development Group
**PostgreSQL 18 — Internals**

Principal para:

- query processing;
- parser;
- rewrite system;
- planner;
- executor;
- storage;
- catalogs;
- WAL;
- index access methods;
- extensibility.

### Jesús Espino
**Deep Dive Into a SQL Query: A Journey Through PostgreSQL's Query Processing**

Profundización especialmente adecuada para los bloques de query lifecycle, planner y executor.

### PostgreSQL source code

Fuente primaria para los últimos bloques de internals.

Usar conjuntamente:

- source tree;
- comments;
- README internos;
- regression tests;
- documentación oficial.

No depender del código fuente para enseñar comportamiento SQL que ya esté especificado
documentalmente; usarlo para comprender implementación.

## 9. Transacciones, MVCC y concurrencia

### PostgreSQL Global Development Group
**PostgreSQL 18 — Concurrency Control**

Fuente principal para:

- transaction isolation;
- explicit locking;
- row-level locks;
- deadlocks;
- advisory locks;
- serializable transactions.

### PostgreSQL Global Development Group
**PostgreSQL 18 — Routine Vacuuming / MVCC-related documentation**

Fuente principal para conectar:

- MVCC;
- dead tuples;
- VACUUM;
- freezing;
- transaction ID wraparound.

### Database System Concepts

Complementaria para teoría general de:

- serializability;
- locking;
- concurrency;
- recovery.

## 10. Observabilidad y mantenimiento

### PostgreSQL Global Development Group
**PostgreSQL 18 — Monitoring Database Activity**

Principal para:

- `pg_stat_activity`;
- `pg_stat_*`;
- wait events;
- cumulative statistics;
- progress reporting.

### PostgreSQL Global Development Group
**PostgreSQL 18 — System Catalogs**

Principal para introspección y diagnóstico basado en metadata.

### PostgreSQL Global Development Group
**PostgreSQL 18 — Routine Database Maintenance Tasks**

Principal para:

- VACUUM;
- ANALYZE;
- autovacuum;
- planner statistics;
- reindexing cuando corresponda.

## 11. JSON, SQL/JSON y datos semiestructurados

### PostgreSQL Global Development Group
**PostgreSQL 18 — JSON Types / JSON Functions and Operators / SQL/JSON**

Fuente principal.

Cubrir desde ella:

- `json`;
- `jsonb`;
- operators;
- SQL/JSON;
- jsonpath;
- indexing;
- construction;
- querying.

## 12. Full-text search

### PostgreSQL Global Development Group
**PostgreSQL 18 — Full Text Search**

Fuente principal para:

- `tsvector`;
- `tsquery`;
- dictionaries;
- configurations;
- ranking;
- GIN/GiST.

## 13. Particionamiento

### PostgreSQL Global Development Group
**PostgreSQL 18 — Table Partitioning**

Fuente principal para:

- RANGE;
- LIST;
- HASH;
- partition pruning;
- maintenance;
- indexes;
- constraints.

Las afirmaciones de rendimiento deben validarse mediante planes y mediciones.

## 14. Seguridad

### PostgreSQL Global Development Group
**PostgreSQL 18 — Database Roles and Privileges**

Fuente principal para roles y GRANT/REVOKE.

### PostgreSQL Global Development Group
**PostgreSQL 18 — Row Security Policies**

Principal para RLS.

### PostgreSQL Global Development Group
**PostgreSQL 18 — CREATE FUNCTION / Function Security**

Principal para:

- `SECURITY DEFINER`;
- `SECURITY INVOKER`;
- privileges;
- `search_path`.

### OWASP
**SQL Injection Prevention Cheat Sheet**

Complementaria para el concepto de parameterized queries y prevención de inyección desde
aplicaciones.

No sustituye la documentación del driver concreto cuando se estudie binding de parámetros.

## 15. Testing y benchmarking

### PostgreSQL Global Development Group
**pgbench documentation**

Principal para benchmarking reproducible.

### pgTAP documentation

Complementaria cuando el PATH introduzca testing de objetos y comportamiento SQL.

## 16. Extensiones

Para extensiones como:

- `pg_stat_statements`;
- `pg_trgm`;
- `citext`;
- `hstore`;
- `pgcrypto`;
- `tablefunc`;
- `btree_gist`;
- `btree_gin`;

usar primero la documentación oficial correspondiente a la versión PostgreSQL objetivo.

## 17. Bibliografía que ya posee el estudiante

### LEARN_POSTGRESQL_SECOND_EDITION

Usar como apoyo introductorio y práctico cuando el contenido coincida con el PATH.

No utilizar como autoridad sobre detalles de PostgreSQL 18 sin verificación.

### MASTERING_POSTGRESQL_17

Categoría recomendada:

- PostgreSQL;
- profundización;
- rendimiento.

### POSTGRESQL_16_ADMINISTRATION_COOKBOOK

Categoría recomendada:

- PostgreSQL;
- consulta;
- mantenimiento;
- observabilidad.

Su foco administrativo debe utilizarse sólo donde el PATH SQL entra en áreas necesarias para
comprender rendimiento e internals.

## 18. Prioridad de fuentes

Ante conflicto o duda, usar este orden:

1. SQL estándar, para determinar qué es normativo en SQL.
2. PostgreSQL 18 Documentation, para comportamiento PostgreSQL.
3. PostgreSQL source code, para detalles de implementación.
4. Libros especializados modernos.
5. Libros generales y obras clásicas.
6. Artículos, blogs o material secundario sólo como complemento.

## 19. Regla para las lecciones

La sección `📚 LECTURA` no debe ser una bibliografía repetitiva.

Debe seleccionar únicamente las fuentes pertinentes al tema de la lección.

Ejemplo conceptual:

Principal:
PostgreSQL 18 Documentation — sección pertinente.

Normativa:
ISO/IEC 9075 — sólo cuando exista una cuestión de estándar.

PostgreSQL:
Mastering PostgreSQL 17 — cuando aporte profundidad práctica.

Profundización:
Date / Elmasri / Silberschatz — cuando el tema sea teórico o de arquitectura.

Rendimiento:
SQL Performance Explained + documentación PostgreSQL — para índices/planner.

Internals:
PostgreSQL Internals + source code — en los bloques expertos.

Consulta:
Administration Cookbook u otras referencias auxiliares.

No inventar páginas, capítulos o epígrafes concretos.
