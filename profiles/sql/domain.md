# DOMAIN — SQL DE 0 A EXPERTO
## SQL estándar + PostgreSQL como implementación principal

## 1. Propósito

Este perfil genera un curso técnico de SQL desde nivel cero hasta nivel experto.

El curso no debe reducir SQL a una colección de recetas ni identificar SQL con un único
producto. La progresión debe enseñar primero los conceptos del lenguaje SQL y del modelo
relacional, y después utilizar PostgreSQL como implementación principal para estudiar con
profundidad ejecución, concurrencia, optimización, almacenamiento, observabilidad e internals.

La idea central es:

SQL estándar → modelo relacional → PostgreSQL → ejecución física → internals → diagnóstico.

El estudiante debe terminar siendo capaz no sólo de escribir consultas correctas, sino de
razonar sobre su semántica, demostrar su comportamiento, analizar su plan de ejecución,
entender sus efectos transaccionales y diagnosticar problemas reales.

## 2. Alcance

El PATH cubre, de forma progresiva:

- entorno PostgreSQL y psql;
- SELECT, expresiones, filtros, ORDER BY, DISTINCT;
- NULL y lógica ternaria;
- claves y relaciones;
- funciones escalares y agregadas;
- fechas, horas e intervalos;
- GROUP BY y HAVING;
- CASE y lógica condicional;
- joins;
- subqueries;
- CTE y recursive CTE;
- operaciones de conjuntos;
- window functions;
- GROUPING SETS, ROLLUP y CUBE;
- views y materialized views;
- temporary y unlogged tables;
- modelo relacional;
- álgebra relacional;
- dependencias funcionales;
- normalización y desnormalización;
- modelado conceptual, lógico y físico;
- DDL, tipos, constraints, sequences, identity y generated columns;
- DML, RETURNING, UPSERT, MERGE y COPY;
- transacciones, savepoints e isolation levels;
- MVCC;
- locks y deadlocks;
- índices B-tree, Hash, GiST, SP-GiST, GIN y BRIN;
- índices parciales, de expresión y covering;
- planner y cost model;
- EXPLAIN y EXPLAIN ANALYZE;
- scan nodes, join algorithms, sort y aggregate nodes;
- estadísticas y extended statistics;
- memoria de consultas, paralelismo y JIT;
- metodología de optimización;
- funciones SQL, PL/pgSQL, procedures y triggers;
- JSON/JSONB y SQL/JSON;
- full-text search;
- particionamiento y partition pruning;
- roles, privileges, RLS y SECURITY DEFINER;
- SQL injection y prepared statements;
- system catalogs e information_schema;
- pg_stat_* y observabilidad;
- VACUUM, autovacuum, freeze, visibility map, FSM, HOT y bloat;
- arquitectura de almacenamiento;
- heap pages, tuples y TOAST;
- B-tree internals;
- buffer manager;
- WAL, checkpoints y crash recovery;
- procesos PostgreSQL;
- query lifecycle;
- parser, analyzer, rewrite system, planner y executor;
- patrones SQL avanzados;
- modelado temporal, jerárquico, graph-like y multi-tenant;
- diseño para concurrencia y rendimiento;
- OLTP y analytics;
- SQL Standard vs extensiones PostgreSQL;
- portabilidad a MySQL/MariaDB/SQLite cuando sea útil;
- testing, benchmarking y pgbench;
- pg_stat_statements y logging;
- extensiones PostgreSQL relevantes;
- troubleshooting sistemático;
- orientación al código fuente de PostgreSQL;
- proyecto diagnóstico sql-postgresql-debugger;
- proyecto integrador final.

## 3. SQL estándar frente a PostgreSQL

SQL y PostgreSQL no son sinónimos.

Cada lección debe distinguir, cuando sea relevante, entre:

1. concepto relacional;
2. construcción definida por SQL estándar;
3. sintaxis o comportamiento PostgreSQL;
4. detalle de implementación PostgreSQL;
5. diferencias de portabilidad con otros motores.

Una característica específica de PostgreSQL debe identificarse explícitamente como tal.

Ejemplos típicos de características PostgreSQL-specific:

- `DISTINCT ON`;
- `ILIKE`;
- `RETURNING` cuando se estudie como extensión histórica/implementación concreta;
- arrays;
- `JSONB`;
- range y multirange types;
- exclusion constraints;
- partial indexes;
- expression indexes;
- `ON CONFLICT`;
- operadores PostgreSQL;
- system catalogs `pg_catalog`;
- `ctid`, `xmin`, `xmax`;
- `VACUUM`;
- MVCC específico de PostgreSQL;
- tipos y access methods propios.

No presentar estas características simplemente como “SQL” sin calificación.

## 4. PostgreSQL de referencia

La implementación práctica principal es PostgreSQL 18.

Las lecciones deben preferir el comportamiento documentado de PostgreSQL 18 y señalar diferencias
de versión cuando sean importantes.

No convertir el PATH en un curso de administración general de PostgreSQL. Los temas de servidor,
almacenamiento, WAL, VACUUM, procesos, buffers o checkpoints se incluyen en la medida en que son
necesarios para comprender SQL, rendimiento, concurrencia, diagnóstico e internals.

## 5. Entorno

Entorno principal:

- Fedora Linux;
- PostgreSQL;
- `psql`;
- shell;
- utilidades estándar del sistema cuando sean necesarias.

Para laboratorios introductorios debe bastar una instalación local de PostgreSQL.

Cuando una práctica requiera dos sesiones concurrentes, indicar claramente:

- sesión A;
- sesión B;
- orden exacto de ejecución;
- estado esperado;
- consultas de observación.

## 6. Progresión pedagógica

El curso avanza de:

1. sintaxis observable;
2. semántica SQL;
3. modelo relacional;
4. diseño;
5. transacciones;
6. ejecución;
7. optimización;
8. internals;
9. diagnóstico.

Una lección inicial no debe recibir prematuramente detalles de internals que pertenecen a bloques
posteriores.

Una lección avanzada puede reutilizar conocimientos previos sin reenseñarlos por completo.

## 7. Semántica antes que receta

Toda explicación importante debe responder, según corresponda:

- qué expresa la construcción;
- qué filas produce;
- qué ocurre con NULL;
- qué ocurre con duplicados;
- qué cardinalidad puede producir;
- qué garantías transaccionales existen;
- qué aspectos son lógicos y cuáles físicos;
- qué depende del motor.

Debe evitarse enseñar SQL únicamente como “escribe esta consulta”.

## 8. NULL y lógica ternaria

NULL debe tratarse con especial rigor.

Nunca equiparar NULL con:

- cero;
- cadena vacía;
- `false`;
- valor desconocido en todos los contextos sin matices.

Explicar TRUE, FALSE y UNKNOWN cuando sea necesario.

Recordar las consecuencias sobre:

- comparaciones;
- `WHERE`;
- `CHECK`;
- joins;
- `IN` / `NOT IN`;
- aggregates;
- unique constraints;
- ordering.

## 9. Duplicados y bag semantics

SQL normalmente trabaja con multiconjuntos, no con relaciones matemáticas puras.

Las lecciones deben distinguir:

- set semantics;
- bag/multiset semantics;
- `DISTINCT`;
- `UNION` frente a `UNION ALL`;
- multiplicación de filas por joins;
- duplicados reales frente a duplicados aparentes.

No recomendar `DISTINCT` como corrección automática de joins mal diseñados.

## 10. Joins y cardinalidad

Los joins deben enseñarse como operaciones con cardinalidad, no sólo como sintaxis.

Para consultas no triviales, razonar sobre:

- cardinalidad de cada entrada;
- unicidad;
- claves;
- fan-out;
- one-to-one;
- one-to-many;
- many-to-many;
- filtros en `ON` frente a `WHERE`;
- efecto de NULL;
- posibilidad de join explosion.

## 11. Modelo relacional

El curso debe distinguir el modelo relacional de SQL.

Los temas de teoría incluyen:

- relación;
- tupla;
- atributo;
- dominio;
- claves;
- integridad;
- álgebra relacional;
- dependencias funcionales;
- normalización;
- lossless decomposition;
- dependency preservation.

La teoría debe conectarse con decisiones prácticas de esquema PostgreSQL.

## 12. Diseño de esquemas

No existe una regla universal “normalizar siempre” ni “desnormalizar por rendimiento”.

Toda decisión de diseño debe justificar:

- requisitos;
- invariantes;
- cardinalidades;
- patrones de acceso;
- coste de escritura;
- coste de lectura;
- concurrencia;
- integridad;
- mantenibilidad.

Las constraints deben preferirse para invariantes que la base de datos pueda garantizar
declarativamente.

## 13. Transacciones y concurrencia

Distinguir:

- atomicidad;
- aislamiento;
- locking;
- MVCC;
- snapshot;
- anomalías;
- garantías del isolation level.

Los laboratorios deben permitir reproducir de forma controlada:

- lost update;
- non-repeatable read;
- write skew;
- lock waits;
- deadlocks;
- serializable failures.

Nunca afirmar que “MVCC significa que no hay locks”.

## 14. MVCC PostgreSQL

Al profundizar en PostgreSQL, relacionar:

- versiones de tuples;
- `xmin`;
- `xmax`;
- snapshots;
- visibilidad;
- dead tuples;
- HOT;
- VACUUM;
- freezing;
- visibility map.

Distinguir columnas del sistema visibles al usuario de detalles internos que no forman parte de un
contrato SQL portable.

## 15. Índices

Un índice no debe presentarse como “acelerador universal”.

Para cada índice considerar:

- tipo de predicado;
- selectividad;
- distribución;
- orden;
- cardinalidad;
- tamaño;
- coste de escritura;
- mantenimiento;
- posibilidad de index-only scan;
- workload.

Cuando corresponda, comparar:

- B-tree;
- Hash;
- GiST;
- SP-GiST;
- GIN;
- BRIN.

Las recomendaciones deben basarse en evidencia.

## 16. Query planner y optimización

Separar siempre:

- SQL lógico;
- plan físico;
- estimaciones;
- ejecución observada.

Para diagnóstico real preferir:

- `EXPLAIN`;
- `EXPLAIN ANALYZE`;
- `BUFFERS`;
- `WAL` cuando aporte valor;
- estimated rows vs actual rows;
- loops;
- filtros;
- sorts;
- temp I/O;
- heap fetches.

No afirmar que un plan es malo sólo porque contenga `Seq Scan`.
No afirmar que un índice es mejor sólo porque exista.

## 17. EXPLAIN ANALYZE y seguridad

`EXPLAIN ANALYZE` ejecuta la consulta.

En operaciones con efectos laterales:

- utilizar una base de laboratorio;
- envolver en transacción y `ROLLBACK` cuando sea apropiado;
- advertir claramente del efecto;
- no ejecutar automáticamente DML destructivo.

## 18. Estadísticas

Cuando exista cardinality misestimation, considerar antes de modificar costes:

- `ANALYZE`;
- estadísticas obsoletas;
- `default_statistics_target`;
- estadísticas por columna;
- skew;
- MCV;
- histogramas;
- correlación;
- extended statistics;
- dependencias entre columnas.

## 19. Optimización

Metodología preferida:

1. reproducir;
2. medir baseline;
3. obtener plan;
4. identificar cuello de botella;
5. formular hipótesis;
6. aplicar un cambio;
7. medir de nuevo;
8. comprobar equivalencia semántica;
9. documentar trade-offs.

Evitar reglas simplistas como:

- “subquery siempre es lenta”;
- “CTE siempre materializa”;
- “indexar todas las foreign keys siempre resuelve rendimiento”;
- “más `work_mem` siempre es mejor”.

## 20. Funciones, procedures y triggers

Distinguir correctamente:

- SQL-language function;
- PL/pgSQL function;
- procedure;
- trigger function;
- row trigger;
- statement trigger;
- event trigger.

No utilizar triggers cuando una constraint declarativa resuelva mejor el problema.

Para `SECURITY DEFINER`, explicar `search_path`, ownership y privileges.

## 21. JSONB

JSONB es una herramienta, no un sustituto automático del modelo relacional.

Antes de recomendar JSONB valorar:

- estructura;
- invariantes;
- joins;
- constraints;
- evolución;
- patrones de consulta;
- indexación.

En modelos híbridos explicar por qué una parte es relacional y otra documental.

## 22. Particionamiento

No presentar particionamiento como optimización general.

Analizar:

- tamaño;
- patrón temporal o de clave;
- pruning;
- mantenimiento;
- retención;
- operaciones administrativas;
- número de particiones;
- índices;
- constraints.

Demostrar partition pruning mediante `EXPLAIN`.

## 23. Seguridad

Principios obligatorios:

- least privilege;
- roles separados;
- parameterized queries;
- evitar concatenación insegura;
- controlar `search_path`;
- no abusar de superuser;
- probar RLS con distintos roles;
- revisar ownership.

## 24. Catálogos e introspección

Para conocimiento portable usar `information_schema` cuando sea apropiado.

Para conocimiento PostgreSQL profundo usar:

- `pg_catalog`;
- `pg_class`;
- `pg_attribute`;
- `pg_type`;
- `pg_namespace`;
- `pg_constraint`;
- `pg_index`;
- `pg_proc`;
- `pg_depend`;
- demás catalogs relevantes.

No depender del layout interno de catalogs sin indicar que es específico de PostgreSQL.

## 25. Observabilidad

Utilizar según el tema:

- `pg_stat_activity`;
- `pg_locks`;
- `pg_stat_database`;
- `pg_stat_user_tables`;
- `pg_stat_user_indexes`;
- `pg_stat_io`;
- `pg_stat_progress_*`;
- `pg_stat_statements`.

Las métricas deben interpretarse en contexto, no como umbrales universales.

## 26. VACUUM y mantenimiento

Relacionar VACUUM con MVCC.

Distinguir:

- VACUUM;
- VACUUM FULL;
- autovacuum;
- ANALYZE;
- freeze;
- anti-wraparound vacuum;
- bloat;
- visibility map;
- free space map.

No recomendar `VACUUM FULL` como mantenimiento rutinario.

## 27. Internals

La parte experta puede introducir:

- relation files;
- pages;
- heap tuples;
- TOAST;
- B-tree pages;
- shared buffers;
- WAL;
- checkpoints;
- parser;
- analyzer;
- rewrite;
- planner;
- executor;
- source tree.

Cada detalle interno debe conectarse con un comportamiento observable.

## 28. Código fuente PostgreSQL

En bloques de internals se puede orientar al estudiante por el árbol de fuentes de PostgreSQL.

El objetivo no es convertir el curso en desarrollo completo de PostgreSQL, sino permitir:

- localizar subsistemas;
- correlacionar conceptos con estructuras;
- entender mejor planner/executor/storage;
- verificar hipótesis.

No inventar nombres de funciones o archivos del código fuente. Si una referencia exacta no está
verificada, describir el subsistema sin atribuirle una ruta exacta.

## 29. Comparaciones con MySQL/MariaDB/SQLite

Las comparaciones son secundarias.

Se incluyen sólo cuando mejoran:

- comprensión del estándar;
- portabilidad;
- prevención de falsas generalizaciones.

PostgreSQL sigue siendo el motor práctico principal.

## 30. Laboratorios

Un laboratorio bueno debe ser:

- reproducible;
- específico de la lección;
- verificable;
- pequeño cuando enseña semántica;
- suficientemente grande cuando enseña rendimiento.

Cuando sea útil debe incluir:

- DDL;
- dataset;
- consulta;
- resultado esperado;
- consulta de verificación;
- limpieza.

No introducir dependencias externas innecesarias.

## 31. Datos de laboratorio

Los datasets deben contener deliberadamente casos que permitan razonar sobre:

- NULL;
- duplicados;
- claves;
- skew;
- valores extremos;
- fechas límite;
- relaciones 1:N y N:M.

Para rendimiento, usar datasets suficientemente grandes para que el planner tenga alternativas
reales.

## 32. Lecturas

La sección `📚 LECTURA` debe seleccionar sólo fuentes realmente útiles para la lección.

Categorías del perfil:

- Principal: documentación oficial PostgreSQL actual;
- Normativa: SQL estándar y obras centradas en SQL estándar;
- PostgreSQL: manuales y libros específicos;
- Profundización: teoría relacional, diseño y SQL avanzado;
- Rendimiento: planner, índices y tuning;
- Internals: arquitectura y código fuente;
- Consulta: referencias de apoyo.

No es obligatorio rellenar todas las categorías en cada lección.

No inventar capítulos, páginas o secciones bibliográficas exactas.

## 33. Proyectos

### sql-postgresql-debugger

Es un proyecto diagnóstico.

Debe aprender a recopilar evidencia y no convertirse en un “optimizador mágico”.

Debe diferenciar:

- hechos observados;
- señales;
- hipótesis;
- recomendaciones.

No debe ejecutar automáticamente cambios destructivos.

### Proyecto final

Debe integrar:

- modelado;
- DDL;
- DML;
- consultas;
- constraints;
- transacciones;
- concurrencia;
- seguridad;
- índices;
- planner;
- observabilidad;
- mantenimiento;
- internals;
- troubleshooting.

La calidad del proyecto se mide por la justificación de decisiones, no por el número de features.

## 34. Criterio de nivel experto

Al terminar el PATH el estudiante debe poder recibir:

- una consulta desconocida;
- un esquema desconocido;
- un plan de ejecución;
- un problema de locking;
- una tabla con bloat;
- una estimación errónea;
- un workload;

y construir una explicación basada en evidencia desde SQL lógico hasta comportamiento interno de
PostgreSQL.
