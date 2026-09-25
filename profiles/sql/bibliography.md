# Bibliography — SQL

## Bibliografía principal

### Alan Beaulieu — *Learning SQL, 3rd Edition*

Texto base para construir fundamentos sólidos de SQL: consultas,
filtros, joins, subqueries, conjuntos, agregaciones, lógica condicional,
transacciones y conceptos necesarios para progresar desde nivel inicial.

**Uso en el PATH:** bloques 0–14 y fundamentos de 19–20.

Los ejemplos del libro basados en MySQL/Sakila se utilizan como referencia
conceptual. Cuando se incorporen al curso, deben adaptarse a PostgreSQL y,
cuando resulte adecuado, a la PostgreSQL Sample Database utilizada como
dataset canónico del PATH. Las diferencias de dialecto relevantes deben
explicarse explícitamente.

### Anthony Molinaro & Robert de Graaf — *SQL Cookbook: Query Solutions and Techniques for All SQL Users*

Fuente principal para aprender SQL mediante problemas y patrones.
Especialmente útil para transformación de datos, strings, fechas,
agregaciones, joins, ventanas y soluciones alternativas a un mismo
problema.

**Uso en el PATH:** bloques 8–14, 17, 21–24.

### Kevin Kline, Regina O. Obe & Leo S. Hsu — *SQL in a Nutshell: A Desktop Quick Reference, 4th Edition*

Referencia transversal de sintaxis, funciones y diferencias entre
implementaciones SQL. Regina Obe y Leo Hsu aportan especial relevancia
para PostgreSQL.

**Uso en el PATH:** referencia durante todo el curso y contraste SQL
estándar/PostgreSQL.

### Clare Churcher — *Beginning SQL Queries: From Novice to Professional*

Apoyo pedagógico para desarrollar razonamiento de consultas desde los
fundamentos hasta consultas multitabla y problemas progresivamente más
complejos.

**Uso en el PATH:** bloques 0–13.

### Cathy Tanimura — *SQL for Data Analysis: Advanced Techniques for Transforming Data into Insights*

Referencia central para SQL analítico: análisis temporal, cohortes,
ventanas, series, patrones de comportamiento y transformación de datos
orientada a insights.

**Uso en el PATH:** bloques 14, 17, 21–22 y proyecto final.

### Jun Shan, Haibin Li et al. — *SQL for Data Analytics, Fourth Edition: Analyze data effectively, uncover insights and master advanced SQL for real-world applications*

Complemento orientado a análisis aplicado y resolución de problemas
mediante SQL.

**Uso en el PATH:** bloques analíticos, ejercicios y proyecto final.

## Documentación primaria y autoritativa

### PostgreSQL Documentation

La documentación oficial de PostgreSQL es la autoridad práctica para la
sintaxis, semántica y comportamiento específico utilizado en los
laboratorios.

Consultar especialmente:

- SQL Commands
- Queries
- Data Types
- Functions and Operators
- SQL functions (`CREATE FUNCTION`)
- PL/pgSQL
- Procedures (`CREATE PROCEDURE` / `CALL`)
- Triggers and trigger functions
- Event Triggers
- Views and rules
- Materialized Views
- Arrays, range/multirange types, JSON/JSONB and SQL/JSON
- Full Text Search
- Type Conversion
- Indexes, solo en relación con query performance
- Concurrency Control
- Performance Tips
- `EXPLAIN`
- `psql`

**Rol:** referencia normativa/autoritativa. Cuando exista una diferencia
entre otra fuente y la versión actual de PostgreSQL utilizada en el curso,
prevalece la documentación oficial vigente.

## Tutoriales y recursos didácticos

### Neon — PostgreSQL Tutorial

https://neon.com/postgresql/tutorial

Tutorial práctico de PostgreSQL utilizado como referencia didáctica
complementaria para explicaciones, ejemplos, ejercicios y preparación de
laboratorios.

**Uso en el PATH:** apoyo transversal desde fundamentos hasta PostgreSQL
avanzado, incluyendo Functions, PL/pgSQL, procedures, triggers y views cuando
exista una sección pertinente.

**Rol:** fuente secundaria. No sustituye a la documentación oficial de
PostgreSQL para determinar el comportamiento exacto del motor.

## Datasets y bases de datos de laboratorio

### Neon — PostgreSQL Sample Database

https://neon.com/postgresql/getting-started/sample-database

Base de datos PostgreSQL de ejemplo utilizada como **dataset canónico de
laboratorio** del curso.

Se debe preferir para ejemplos, ejercicios y laboratorios progresivos de
consultas, joins, agregaciones, subconsultas, CTEs, operaciones de
conjuntos, funciones de ventana, views/materialized views, DML reproducible,
funciones SQL/PL/pgSQL y triggers cuando el esquema lo permita, además del
análisis de consultas con `EXPLAIN` / `EXPLAIN ANALYZE`.

Puede complementarse con datasets mínimos creados específicamente para
casos límite o demostraciones semánticas que requieran controlar con
precisión las filas de entrada.

## Criterio de uso bibliográfico

Las fuentes cumplen funciones diferentes:

1. **PostgreSQL Documentation** — autoridad para sintaxis, semántica y
   comportamiento actual de PostgreSQL.
2. **Bibliografía principal** — explicación conceptual, progresión,
   patrones y profundización.
3. **Neon PostgreSQL Tutorial** — apoyo didáctico y práctico
   complementario.
4. **PostgreSQL Sample Database** — experimentación, ejercicios y
   laboratorios reproducibles.

Los libros son fuentes de apoyo, no el límite del temario. Cuando exista
diferencia entre una edición de un libro, un tutorial y la versión actual
de PostgreSQL utilizada en el curso, prevalece la documentación oficial
vigente de PostgreSQL.

Los ejemplos procedentes de fuentes basadas en MySQL, MariaDB u otros
dialectos pueden adaptarse a PostgreSQL siempre que se conserve el concepto
SQL y se indiquen las diferencias de dialecto relevantes.

## Contenido deliberadamente delegado a otro PATH

La bibliografía de este curso no debe utilizarse para introducir bloques
de:

- normalización;
- formas normales;
- dependencias funcionales;
- modelado ER;
- diseño lógico;
- teoría de diseño relacional;
- desnormalización;
- decisiones de almacenamiento de atributos derivados.

Estos contenidos pertenecen al PATH **Relational Database Design**, cuya
bibliografía puede apoyarse separadamente en C. J. Date y otras obras
especializadas en diseño y teoría relacional.
