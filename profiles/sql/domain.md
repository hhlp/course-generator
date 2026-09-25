# Domain — SQL

## Propósito

Este curso desarrolla dominio de **SQL como lenguaje**, desde consultas
elementales hasta query engineering avanzado y programación de base de datos
con PostgreSQL, utilizando PostgreSQL como implementación práctica de referencia.

El aprendizaje se centra primero en el concepto y la semántica SQL y,
cuando corresponda, identifica de forma explícita el comportamiento,
sintaxis o extensión específica de PostgreSQL.

## Alcance principal

El dominio incluye:

- `SELECT`, expresiones, alias, ordenación y paginación.
- Filtrado y lógica de tres valores.
- Funciones escalares, fechas y agregaciones.
- `GROUP BY`, `HAVING` y agregación avanzada.
- JOINs y composición multitabla.
- `CASE` y expresiones condicionales.
- CTEs normales y recursivas.
- Operaciones `UNION`, `INTERSECT` y `EXCEPT`.
- Subconsultas y consultas correlacionadas.
- Self joins.
- Funciones de ventana y window frames.
- Vistas, vistas materializadas y tablas temporales, incluyendo vistas actualizables, `WITH CHECK OPTION`, `security_invoker`, `security_barrier` e `INSTEAD OF` triggers.
- DML: `INSERT`, `UPDATE`, `DELETE`, `RETURNING`, UPSERT y `MERGE`.
- Transacciones y locking expresados desde SQL.
- Arrays, ranges/multiranges, JSON/JSONB, SQL/JSON, full-text search y tipos/expresiones avanzadas de PostgreSQL.
- Funciones y operadores incorporados de PostgreSQL.
- `CREATE FUNCTION`, funciones `LANGUAGE SQL` y set-returning functions.
- PL/pgSQL: variables, control de flujo, SQL dinámico, excepciones y cursores.
- Stored functions y stored procedures con `CREATE PROCEDURE` / `CALL`.
- Trigger functions, row/statement triggers, `BEFORE`, `AFTER`, `INSTEAD OF`, transition relations y event triggers desde la perspectiva de programación SQL.
- Patrones SQL analíticos.
- Semántica SQL, NULL, duplicados, granularidad y corrección.
- `EXPLAIN`, `EXPLAIN ANALYZE` y lectura de planes para query tuning.
- Seguridad y mantenibilidad de consultas y rutinas, incluyendo `SECURITY DEFINER`, `search_path` y SQL dinámico seguro.

## Plataforma y dialecto

La implementación de referencia es **PostgreSQL**. Se prioriza SQL
estándar cuando resulta razonable y se identifica explícitamente la
funcionalidad específica de PostgreSQL.

Las prácticas deben poder ejecutarse con `psql` y archivos `.sql`.

Cuando una fuente utilice MySQL, MariaDB u otro dialecto, debe conservarse
el concepto SQL que se pretende enseñar y adaptar el ejemplo a PostgreSQL.
Las diferencias de sintaxis o comportamiento relevantes deben explicarse,
no ocultarse.

En particular, los ejemplos de *Learning SQL, 3rd Edition* basados en
MySQL/Sakila pueden utilizarse como referencia conceptual, pero los
laboratorios del curso deben preferir PostgreSQL y el dataset canónico
definido a continuación.

## Dataset canónico de laboratorio

La base de datos de ejemplo principal del PATH es **PostgreSQL Sample
Database** publicada por Neon:

https://neon.com/postgresql/getting-started/sample-database

Este dataset actúa como base de datos canónica para ejemplos, ejercicios y
laboratorios siempre que su esquema permita demostrar adecuadamente el
concepto de la lección.

Debe utilizarse progresivamente para practicar, entre otros:

- consultas básicas y filtrado;
- ordenación y paginación;
- agregaciones;
- JOINs y self joins;
- subconsultas;
- `CASE`;
- CTEs;
- operaciones de conjuntos;
- funciones de ventana;
- vistas y vistas materializadas;
- funciones SQL y PL/pgSQL;
- procedimientos;
- triggers cuando el dataset o un dataset mínimo reproducible lo permita;
- DML cuando el laboratorio pueda realizarse de forma reproducible;
- `EXPLAIN` y `EXPLAIN ANALYZE`;
- comparación y optimización de consultas.

No es obligatorio forzar este dataset cuando un concepto requiera un
ejemplo mínimo, un caso límite o datos diseñados específicamente para
demostrar determinada semántica. En esos casos pueden crearse datasets
pequeños reproducibles dentro del propio laboratorio.

## Fuentes técnicas de referencia

### PostgreSQL Documentation

La documentación oficial de PostgreSQL constituye la referencia
autoritativa para sintaxis, semántica, comportamiento del motor,
`EXPLAIN`, planificación y características específicas de PostgreSQL.

### Neon PostgreSQL Tutorial

https://neon.com/postgresql/tutorial

El tutorial de PostgreSQL de Neon se utiliza como **referencia didáctica
complementaria** para explicaciones, ejemplos, ejercicios y preparación de
laboratorios.

No sustituye a la documentación oficial de PostgreSQL. Si existe una
diferencia o ambigüedad sobre el comportamiento actual del motor, prevalece
la documentación oficial vigente.

## Frontera estricta con Relational Database Design

No desarrollar como contenido pedagógico de este PATH:

- 1FN, 2FN, 3FN, BCNF, 4FN, 5FN o 6FN.
- Dependencias funcionales, multivaluadas o de join.
- Normalización o desnormalización.
- Diseño conceptual.
- Modelado ER/EER.
- Transformación de modelos conceptuales a esquemas relacionales.
- Diseño de claves candidatas/primarias como disciplina de modelado.
- Descomposición lossless/dependency preserving.
- Anomalías de inserción, actualización y borrado como teoría de diseño.
- Diseño lógico o físico general de bases de datos.
- Decisiones de diseño sobre almacenar valores derivados frente a
  calcularlos.
- Teoría relacional profunda que pertenezca al PATH Database Design.

## Excepciones necesarias

Se pueden explicar PK, FK, `UNIQUE`, `NOT NULL`, `CHECK` e índices de
manera limitada cuando sean necesarios para comprender:

1. el resultado de una consulta;
2. cardinalidad y duplicados;
3. JOINs;
4. errores de integridad producidos por DML;
5. planes de ejecución;
6. rendimiento de una consulta.

La explicación debe centrarse en **su efecto sobre SQL**, no en cómo
diseñar el esquema.

## Filosofía pedagógica

Cada concepto debe avanzar desde sintaxis → semántica → ejemplo → caso
límite → error frecuente → laboratorio.

Se debe enseñar a razonar sobre:

- qué filas entran;
- qué filas salen;
- cuál es la granularidad;
- dónde aparecen NULLs;
- dónde se multiplican filas;
- cuándo se eliminan duplicados;
- cuándo existe o no un orden garantizado;
- qué trabajo debe realizar PostgreSQL;
- cómo demostrar el comportamiento con una consulta.

## Laboratorios

Los laboratorios deben utilizar datasets suficientemente ricos para
practicar consultas reales y deben favorecer:

- consultas reproducibles;
- comparación de soluciones;
- comprobación del resultado;
- uso progresivo de `EXPLAIN`;
- ejecución desde `psql`;
- almacenamiento de soluciones en archivos `.sql`.

Se debe preferir **PostgreSQL Sample Database** como dataset compartido del
curso. Los datasets mínimos creados ad hoc siguen siendo apropiados para
casos límite, demostraciones semánticas y experimentos controlados.

## Objetivo final

El alumno debe ser capaz de recibir un esquema ya diseñado y utilizar
SQL para consultar, combinar, transformar, analizar y modificar sus
datos; construir consultas complejas correctas; crear interfaces mediante
views; programar funciones, procedimientos y triggers cuando estén
justificados; detectar errores semánticos; y diagnosticar problemas de
rendimiento desde el punto de vista de consultas y rutinas SQL.
