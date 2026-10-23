# Bibliografía y documentación — MongoDB

Fecha de revisión de las fuentes principales: 21 de octubre de 2026.

Fuentes oficiales como referencia normativa. Los enlaces auxiliares son puntos de entrada para desarrollar las lecciones; seleccionar la versión correcta y seguir las redirecciones vigentes. No se afirma haber verificado individualmente todas sus subpáginas.

- [Guía principal de desarrollo](https://www.mongodb.com/es/docs/development/). Mapa general de capacidades; estructura de referencia del curso.
- [Manual de MongoDB](https://www.mongodb.com/docs/manual/). Semántica del servidor; seleccionar la versión del laboratorio.
- [Datasets oficiales](https://www.mongodb.com/docs/manual/sample-data/). Namespaces y conjuntos disponibles.
- [Mflix y embeddings](https://www.mongodb.com/docs/manual/sample-data/sample-mflix/). Películas, comentarios, cines y contrato de los campos vectoriales.
- [Carga de datos de ejemplo en Atlas](https://www.mongodb.com/docs/atlas/sample-data/). Punto de entrada oficial; seguir el enlace vigente de importación.
- [CRUD](https://www.mongodb.com/docs/manual/crud/). Lectura, escritura y actualización.
- [Referencia de operadores](https://www.mongodb.com/docs/manual/reference/operator/). Consultar cada operador y sus restricciones.
- [Modelado](https://www.mongodb.com/docs/manual/data-modeling/). Relaciones, patrones y validación.
- [Agregación](https://www.mongodb.com/docs/manual/aggregation/). Etapas, expresiones, acumuladores y optimización.
- [Índices](https://www.mongodb.com/docs/manual/indexes/). Diseño, índices especializados y planes.
- [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/). Driver, BSON, sesiones y API asíncrona vigente.
- [mongosh](https://www.mongodb.com/docs/mongodb-shell/). Shell y conexión.
- [Compass](https://www.mongodb.com/docs/compass/). Inspección visual y construcción de pipelines.
- [MongoDB Search](https://www.mongodb.com/docs/atlas/atlas-search/). Índices de búsqueda, analizadores, operadores y relevancia.
- [Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/). Indexación y consultas vectoriales; seguir redirecciones vigentes.
- [Búsqueda híbrida](https://www.mongodb.com/docs/vector-search/hybrid-search/hybrid-search-overview/). RRF, fusión de scores y evaluación de compatibilidad.
- [Integración híbrida con LangChain](https://www.mongodb.com/docs/atlas/ai-integrations/langchain/hybrid-search/). Lectura opcional después de implementar recuperación sin framework.
- [Atlas](https://www.mongodb.com/docs/atlas/). Operación, administración, backups y métricas.
- [Límites de Atlas Free](https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/). Decidir qué prácticas necesitan otro entorno.
- [Límites de servicio](https://www.mongodb.com/docs/atlas/reference/atlas-limits/). Cuotas y restricciones del servicio.
- [Notas de versión del servidor](https://www.mongodb.com/docs/manual/release-notes/). Comprobar cambios, deprecaciones y compatibilidad.

## Orden de lectura

Desarrollo → datasets → mongosh/Compass → CRUD → modelado y validación →
agregaciones → índices → PyMongo → Search → embeddings → Vector Search →
híbrida y evaluación. Añadir geoespacial y optimización para el proyecto final.

Consultar la documentación de cada operador y la versión del despliegue durante
el desarrollo de las lecciones. La ruta no requiere documentación de operación
de servidores. La documentación general de Atlas se utiliza para conectar y
comprobar capacidades necesarias para las consultas y los índices de búsqueda.
