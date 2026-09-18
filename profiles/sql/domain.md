# Domain — SQL

## Propósito

Este curso desarrolla dominio de **SQL como lenguaje**, desde consultas
elementales hasta query engineering avanzado, utilizando PostgreSQL como
implementación práctica de referencia.

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
- Vistas, vistas materializadas y tablas temporales.
- DML: `INSERT`, `UPDATE`, `DELETE`, `RETURNING`, UPSERT y `MERGE`.
- Transacciones y locking expresados desde SQL.
- Arrays, JSON/JSONB y capacidades de consulta propias de PostgreSQL.
- Patrones SQL analíticos.
- Semántica SQL, NULL, duplicados, granularidad y corrección.
- `EXPLAIN`, `EXPLAIN ANALYZE` y lectura de planes para query tuning.
- Seguridad y mantenibilidad de consultas.

## Plataforma

La implementación de referencia es **PostgreSQL**. Se prioriza SQL
estándar cuando resulta razonable y se identifica explícitamente la
funcionalidad específica de PostgreSQL.

Las prácticas deben poder ejecutarse con `psql` y archivos `.sql`.

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

1.  el resultado de una consulta;
2.  cardinalidad y duplicados;
3.  JOINs;
4.  errores de integridad producidos por DML;
5.  planes de ejecución;
6.  rendimiento de una consulta.

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

## Objetivo final

El alumno debe ser capaz de recibir un esquema ya diseñado y utilizar
SQL para consultar, combinar, transformar, analizar y modificar sus
datos; construir consultas complejas correctas; detectar errores
semánticos; y diagnosticar problemas de rendimiento desde el punto de
vista de la consulta.
