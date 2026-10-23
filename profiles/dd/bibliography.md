# Bibliografía: diseño de bases de datos relacionales

## Principal: C. J. Date

1. **Database Design and Relational Theory: Normal Forms and All That Jazz, 2.ª edición — C. J. Date. Apress.** Eje de los bloques 5 y 9–19: dependencias, claves, normalización y evaluación formal de diseños. [Ficha editorial](https://link.springer.com/book/10.1007/978-1-4842-5540-7).
2. **An Introduction to Database Systems, 8.ª edición — C. J. Date.** Referencia general para fundamentos, integridad y arquitectura. Utilizar de forma selectiva; las características concretas de PostgreSQL se contrastan con su documentación.
3. **SQL and Relational Theory: How to Write Accurate SQL Code, 3.ª edición — C. J. Date. O’Reilly.** Apoyo para distinguir el modelo relacional de SQL, especialmente duplicados, NULL y restricciones. En esta ruta se seleccionan los aspectos que afectan al diseño; el desarrollo de consultas pertenece al curso SQL.
4. **Time and Relational Theory — C. J. Date, Hugh Darwen y Nikos A. Lorentzos.** Ampliación para diseño temporal e histórico y relación con 6FN.

La [bibliografía mantenida por Hugh Darwen](https://www.dcs.warwick.ac.uk/~hugh/TTM/documents_and_books.html) permite verificar y localizar las obras de teoría relacional citadas, incluidas la segunda edición de Database Design and Relational Theory y la tercera de SQL and Relational Theory.

## Complementos por función

- **Database Design for Mere Mortals: 25th Anniversary Edition, 4.ª edición — Michael J. Hernandez.** Apoyo accesible para requisitos, entidades, relaciones y revisión del diseño. Edición base: 4.ª; contrastar los capítulos si se utiliza otra edición.
- **Database System Concepts, 7.ª edición — Abraham Silberschatz, Henry F. Korth y S. Sudarshan.** Complemento de sistemas para almacenamiento, índices, procesamiento, optimización y transacciones. Es una referencia de apoyo, no un sustituto del eje de Date. [Sitio de los autores](https://www.db-book.com/).

No es necesario adquirir todos los libros para seguir la ruta. Priorizar el libro principal de diseño, documentación oficial y ejercicios; ampliar las referencias según la etapa.

## Documentación oficial PostgreSQL

Se fija la rama 18 para facilitar la reproducción. Consultar la documentación de la versión efectivamente instalada cuando difiera.

- [Restricciones](https://www.postgresql.org/docs/18/ddl-constraints.html): implementación y límites de las reglas declarativas.
- [Índices](https://www.postgresql.org/docs/18/indexes.html): alternativas físicas y compromisos de mantenimiento.
- [EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html): planes estimados y ejecución medida.
- [Estadísticas del planificador](https://www.postgresql.org/docs/18/planner-stats.html): selectividad y estimación de cardinalidad.
- [Vistas materializadas](https://www.postgresql.org/docs/18/rules-materializedviews.html): persistencia de resultados.
- [REFRESH MATERIALIZED VIEW](https://www.postgresql.org/docs/18/sql-refreshmaterializedview.html): actualización de resultados materializados.
- [Aislamiento de transacciones](https://www.postgresql.org/docs/18/transaction-iso.html): consistencia bajo concurrencia.
- [Bloqueos explícitos](https://www.postgresql.org/docs/18/explicit-locking.html): coordinación de operaciones y contención.
- [Triggers](https://www.postgresql.org/docs/18/triggers.html): mecanismos de mantenimiento de invariantes.
- [Almacenamiento físico](https://www.postgresql.org/docs/18/storage.html): contraste de estimaciones de espacio.

## Mapa de lectura

| Bloques | Referencias y propósito |
|---|---|
| 0–4 | An Introduction to Database Systems y Hernandez: fundamentos y requisitos. |
| 5–8 | Date: claves, modelo relacional, álgebra e integridad. |
| 9–19 | Database Design and Relational Theory: dependencias y normalización, de básica a avanzada. |
| 20–21 | SQL and Relational Theory y documentación PostgreSQL: diferencias semánticas e implementación. |
| 22–24 | Date y Hernandez; Time and Relational Theory para el bloque temporal. |
| 25–27 | Documentación PostgreSQL y Database System Concepts: diseño físico, transacciones y evolución. |
| 28–33 | Database System Concepts y PostgreSQL: capacidad, costes, estadísticas y mediciones. |
| 34–35 | PostgreSQL: agregados persistidos, refresco, triggers, aislamiento y bloqueo. |
| 36 | Síntesis de las fuentes utilizadas para defender el proyecto. |

## Cómo citar en las lecciones

Citar autor, título y edición realmente consultada. Asignar capítulos o páginas únicamente después de verificarlos en esa edición. Para ETNF, RFNF y SKNF consultar la formulación concreta de Date; no inventar equivalencias con otras formas normales.
Los modelos numéricos didácticos deben identificarse como simplificaciones. Los resultados de benchmarks deben proceder de ejecuciones registradas; nunca atribuir cifras hipotéticas a los libros o a PostgreSQL.
La lectura guía el razonamiento; la evaluación requiere ejemplos resueltos, contraejemplos y decisiones justificadas.

## Referencias complementarias por scope (ampliación)

Estas obras complementan, pero no sustituyen, a C. J. Date. Antes de citar capítulos, verificar la edición concreta utilizada.

| Scope | Obra | Uso principal |
|---|---|---|
| Modelado conceptual y lógico (0–8, 22) | Ramez Elmasri y Shamkant B. Navathe, *Fundamentals of Database Systems*, 7.ª edición | ER/EER, restricciones, transformación y revisión de esquemas |
| Diseño práctico (3–6, 22–24) | Michael J. Hernandez, *Database Design for Mere Mortals*, 4.ª edición | Requisitos, entrevistas, entidades y reglas de negocio |
| Internals y diseño físico (25, 28–33) | Alex Petrov, *Database Internals*, publicación de octubre de 2019 | Índices, almacenamiento y compromisos físicos; contrastar particularidades con PostgreSQL |
| Implementación PostgreSQL (20–25, 27, 33–35) | Dimitri Fontaine, *The Art of PostgreSQL*, 2.ª edición, actualización de 2026 | Casos de implementación y contraste de decisiones; no reemplaza la documentación oficial |
| Concurrencia y consistencia (27, 34–35) | Martin Kleppmann, *Designing Data-Intensive Applications*, edición de marzo de 2017 | Consistencia, mantenimiento de derivados, fallos y sistemas distribuidos; uso selectivo |
| Modelado analítico (26) | Ralph Kimball y Margy Ross, *The Data Warehouse Toolkit*, 3.ª edición | Granularidad, dimensiones, hechos y cambios históricos |

## Reglas de asignación de lecturas

- **Principal:** Date para definiciones, dependencias, normalización y pruebas formales.
- **Normativa:** documentación oficial PostgreSQL 18 para sintaxis, semántica y límites del motor.
- **Motor:** documentación de índices, almacenamiento, planificador, EXPLAIN y transacciones de PostgreSQL 18.
- **Profundización:** obras complementarias solo para el bloque y la cuestión técnica pertinentes.
- **Consulta:** glosarios y referencias de apoyo verificables, sin páginas o capítulos inventados.

## Lecturas orientadas a ejercicios cuantitativos

Para los bloques 28–35, combinar *Database System Concepts*, *Database Internals* y documentación PostgreSQL. Cada ejercicio debe distinguir modelo matemático simplificado, supuestos, estimación del planificador, medición real y coste operativo. Evitar atribuir fórmulas didácticas exactas al optimizador de PostgreSQL.

## Ediciones de trabajo y fuentes de verificación

Estas son ediciones base elegidas para la ruta; no constituyen una afirmación de que todas sean las más recientes. No mezclar capítulos o páginas entre ediciones.

- Hernandez, 4.ª edición: [Pearson](https://www.pearson.com/en-us/pearsonplus/p/9780137459667.html).
- Elmasri y Navathe, 7.ª edición: [Pearson](https://eu.pearson.com/fundamentals-of-database-systems-global-edition/9781292097626R365).
- Silberschatz, Korth y Sudarshan, 7.ª edición: [sitio de los autores](https://www.db-book.com/).
- Petrov, publicación de octubre de 2019: [O’Reilly](https://www.oreilly.com/library/view/database-internals/9781492040330/).
- Fontaine, 2.ª edición, actualización de 2026: [historial del autor](https://theartofpostgresql.com/book/updates/). Registrar la revisión del ejemplar consultado.
- Kleppmann, edición de marzo de 2017: [O’Reilly](https://www.oreilly.com/library/view/designing-data-intensive/9781491903063/).
- Kimball y Ross, 3.ª edición: [Wiley](https://www.wiley.com/en-gb/the-data-warehouse-toolkit-the-definitive-guide-to-dimensional-modeling-3rd-edition-p-9781118530801).
- Para *Time and Relational Theory*, identificar año, edición e ISBN del ejemplar antes de asignar una lectura exacta; no se presupone un ejemplar concreto.

### Apoyo específico para las lecciones añadidas

- **21.8–21.11:** [introducción a transacciones](https://www.postgresql.org/docs/18/tutorial-transactions.html), [aislamiento](https://www.postgresql.org/docs/18/transaction-iso.html) y [bloqueos](https://www.postgresql.org/docs/18/explicit-locking.html).
- **25.12–25.15:** [tipos de índices](https://www.postgresql.org/docs/18/indexes-types.html) y [clases de operadores](https://www.postgresql.org/docs/18/indexes-opclass.html). Contrastar la elección con la carga y las mediciones de los bloques 28–33.
