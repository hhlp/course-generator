# MongoDB: consultas y búsquedas de cero a experto

## Objetivo y alcance

Aprender a consultar, transformar, buscar y evaluar información en MongoDB Atlas,
desde los primeros documentos hasta búsqueda vectorial e híbrida. El currículo
incluye 27 bloques, 270 lecciones y 27 laboratorios integradores. Es un temario
profundo con especificaciones de prácticas, no 270 lecciones ya redactadas.
Estimación orientativa: 300–450 horas, dependiendo de conocimientos y práctica.

Todo el trabajo con bases de datos se realiza en Atlas. mongosh, Compass y los
scripts PyMongo se ejecutan como clientes en el equipo del alumno: no se instala
un servidor MongoDB local. No se requieren conocimientos de administración de
nodos. Python básico se necesita al llegar al bloque 17.

El nivel experto se refiere a consultas y recuperación de información. La
administración de replica sets, elecciones, alta disponibilidad, sharding,
backup operativo y automatización de infraestructura queda fuera de esta ruta.
Las transacciones distribuidas y Change Streams tampoco son bloques obligatorios.
RAG se presenta como aplicación opcional de un recuperador ya evaluado.

## Progresión y criterios de dominio

| Bloques | Área | Evidencia |
|---|---|---|
| 0–2 | Fundamentos, Atlas y BSON | Conectar e interpretar documentos y tipos |
| 3–6 | CRUD y arrays | Consultas correctas, paginación estable y escrituras acotadas |
| 7–9 | Modelado, validación y patrones | Elegir estructuras que sirvan a las consultas |
| 10–14 | Aggregation Pipeline | Construir y comprobar transformaciones y analítica |
| 15–16 | Índices y explain | Justificar índices mediante planes y mediciones |
| 17 | PyMongo | Ejecutar consultas y búsquedas desde Python |
| 18–19 | MongoDB Search | Crear búsqueda textual con relevancia, facetas y autocompletado |
| 20–22 | Embeddings y Vector Search | Contrato vectorial correcto y evaluación ANN/ENN |
| 23 | Híbrida y reranking | Comparar recuperación y fusión; RAG opcional |
| 24 | Geoespacial | Resolver proximidad, áreas y distancias |
| 25 | Optimización integral | Medir corrección, relevancia, latencia y coste |
| 26 | Proyecto experto | Defender un buscador completo de películas |

## Datos oficiales y herramientas

| Dataset o colección | Uso |
|---|---|
| sample_mflix.movies | Filtros, arrays, agregaciones, índices y Search |
| sample_mflix.comments | Relaciones y $lookup |
| sample_mflix.embedded_movies | Búsqueda vectorial e híbrida |
| sample_mflix.theaters | Búsqueda geoespacial |
| sample_supplies.sales | Arrays, importes y agregaciones de ventas |
| sample_airbnb.listingsAndReviews | Documentos anidados y modelado |
| sample_analytics | Consultas entre entidades relacionadas |
| sample_geospatial.shipwrecks | Ejercicios espaciales complementarios |
| sample_training y sample_guides | Ejercicios iniciales y adicionales |

Cargar primero sample_mflix y añadir otros datasets cuando sean necesarios.
Inspeccionar nombres, tipos y campos reales; los datos y la interfaz pueden cambiar.
Crear colecciones derivadas para escrituras, migraciones y fixtures de ejercicios.
El contenido original queda como referencia de lectura.

## Preparación mínima de Atlas

Configurar el acceso a Atlas, un usuario de base de datos con permisos acotados,
acceso de red restringido y TLS. Mantener secretos fuera de los archivos del curso.
Registrar versión, driver, plan y funciones disponibles antes de cada laboratorio.
Comprobar que el plan elegido permite los índices y operadores utilizados.
No se presupone que todas las funciones estén disponibles en el plan gratuito.
Si un operador avanzado no está disponible, explicar su alternativa dentro de
Atlas o desde el cliente; por ejemplo, fusionar rankings en Python.
No aprovisionar recursos de pago automáticamente como parte del material.

## Primer laboratorio guiado: Atlas y mflix

1. Crear un proyecto y un despliegue compatible con el trabajo inicial.
2. Crear un usuario de base de datos con permisos apropiados; distinguirlo de la
   cuenta que inicia sesión en Atlas. Restringir el acceso de red y usar TLS.
3. En las acciones del clúster, localizar la opción de cargar datos de ejemplo,
   elegir sample_mflix si la interfaz permite selección y esperar su finalización.
   Añadir los otros datasets solo cuando se necesiten. Si ya existe el namespace,
   consultar el procedimiento de carga antes de intentar repetir la operación.
4. Conectar con mongosh o Compass usando la URI generada por Atlas. Proporcionar
   credenciales de forma externa; no pegar una URI con contraseña en scripts.
5. Ejecutar en mongosh las consultas de inspección siguientes.

```javascript
const mflix = db.getSiblingDB('sample_mflix');
mflix.getCollectionNames();
mflix.movies.findOne({}, {title: 1, year: 1, genres: 1, imdb: 1});
mflix.movies.countDocuments({});
mflix.movies.getIndexes();
mflix.movies.find(
  {year: {$gte: 2000}, genres: 'Drama', 'imdb.rating': {$gte: 8}},
  {_id: 0, title: 1, year: 1, 'imdb.rating': 1}
).sort({'imdb.rating': -1, title: 1}).limit(10);
```

Resultado verificable: conexión correcta, colecciones presentes y documentos
proyectados que satisfacen los filtros. No se exige un número exacto de películas.

## Primer pipeline progresivo

```javascript
const mflix = db.getSiblingDB('sample_mflix');
mflix.movies.aggregate([
  {$match: {year: {$gte: 2000}, 'imdb.rating': {$type: 'number'}}},
  {$unwind: '$genres'},
  {$group: {
    _id: '$genres',
    peliculas: {$sum: 1},
    media: {$avg: '$imdb.rating'}
  }},
  {$match: {peliculas: {$gte: 20}}},
  {$sort: {media: -1, _id: 1}},
  {$limit: 10}
]);
```

Explicar por qué una película puede contribuir a varios géneros y por qué la suma
de grupos no equivale al número de películas únicas. Ejecutar prefijos del pipeline
para inspeccionar tipos y cardinalidad. Comparar valores con un subconjunto manual.

## Progresión específica de búsqueda

1. Consultas exactas y regex: entender sus costes y su semántica.
2. Search: crear un índice de búsqueda, probar $search, relevancia y facetas.
3. Embeddings: explicar el espacio vectorial antes de ejecutar consultas.
4. Vector Search: seleccionar un campo real de embedded_movies e indexarlo.
5. Evaluación ANN/ENN y filtros: medir antes de elegir parámetros.
6. Híbrida: combinar texto y vectores y evaluar RRF/reranking.
7. RAG: añadir generación después de validar la recuperación y sus fuentes.

### Contrato vectorial obligatorio

Inspeccionar primero un documento sin imprimir todos sus embeddings. Registrar:
namespace, campo, proveedor/modelo, dimensión, formato BSON/subtipo y métrica.
La documentación consultada muestra campos de distintas generaciones de embeddings
en embedded_movies, incluyendo representaciones BinData; el curso no presupone
que el campo sea un array ni que todas las cargas tengan idéntico esquema.

Para cada consulta, el embedding debe proceder del mismo modelo y configuración
que los documentos. Compartir dimensión no garantiza compatibilidad semántica.
Si el modelo original no está accesible, generar una colección derivada con un
modelo elegido para documentos y consultas y crear su índice correspondiente.
No rellenar vectores con números inventados para aparentar una búsqueda válida.
Usar la documentación del driver para serializar y consultar el formato real.
La métrica elegida debe ser compatible con el modelo y el índice.

El laboratorio diferencia generación de embeddings, persistencia, indexación,
recuperación y generación de respuestas. Un embedding no es un LLM generador.

### Benchmark mínimo

- Al menos veinte consultas de intención diversa con identificadores estables.
- Referencia ENN para medir aproximación ANN, cuando esté soportada; evaluación
  humana separada para la relevancia semántica, que ENN no certifica.
- Recall@k, MRR o nDCG con juicios; p50/p95 de latencia y número de candidatos.
- Comparar texto, vectores e híbrida sobre el mismo corpus y filtros.
- Distinguir calentamiento de mediciones repetidas y registrar hardware/plan.
- Incluir consultas sin respuesta, ambigüedad, errores tipográficos y filtros
  restrictivos. No confundir score vectorial con probabilidad de verdad.
- Fusión en la aplicación si los operadores nativos no están soportados.

## Seguridad de los ejercicios de escritura

Crear colecciones derivadas en lab_mongodb con subconjuntos acotados. Registrar
el filtro de copia y conservar _id o una referencia al documento de origen.
Los ejercicios de usuarios, stock, carritos y outbox usan fixtures sintéticos
marcados como tales; no se afirma que esos datos existan en mflix.
Cada operación masiva comienza con una lectura equivalente y conteo de alcance.
La limpieza afecta solo a recursos del laboratorio identificados expresamente.

## Laboratorios integradores

### Bloque 0 — Fundamentos de bases de datos documentales

Dibujar la arquitectura de una aplicación de catálogo y justificar el modelo documental.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 1 — Atlas y preparación del entorno

Conectar mongosh y Compass, inventariar sample_mflix y registrar permisos y capacidades sin exponer secretos.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 2 — BSON y semántica del documento

Auditar tipos de movies y sales, detectar campos ausentes y diseñar conversiones sin pérdida.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 3 — CRUD I: lectura desde cero

Resolver veinte preguntas del catálogo con filtros y proyecciones; explicar null frente a missing.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 4 — CRUD II: arrays y consultas avanzadas

Comparar filtros con y sin $elemMatch en listingsAndReviews y construir paginación sin duplicados.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 5 — CRUD III: inserción y actualización

Crear lab_mongodb con copias pequeñas; ejecutar upserts idempotentes y comprobar resultados de escritura.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 6 — CRUD IV: arrays y escrituras masivas

Actualizar carritos y reseñas en una colección derivada, provocar un error parcial y recuperar el lote.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 7 — Modelado documental I

Diseñar catálogo, usuarios y reseñas derivados de mflix y justificar cada embedding o referencia.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 8 — Validación y evolución del esquema

Añadir validación a una colección de laboratorio, migrar dos versiones y documentar rollback.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 9 — Patrones de modelado avanzados

Comparar tres modelos del mismo catálogo mediante tamaño, consultas, escrituras y complejidad.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 10 — Aggregation Pipeline I

Obtener rankings por década y género, contrastando conteos antes y después de $unwind.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 11 — Aggregation Pipeline II: expresiones

Normalizar ratings y fechas heterogéneas sin abortar; conservar registros rechazados con su causa.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 12 — Aggregation Pipeline III: relaciones y composición

Unir movies y comments, producir facetas y comprobar que las películas sin comentarios siguen presentes.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 13 — Aggregation Pipeline IV: analítica avanzada

Construir un análisis temporal con ventas o datos meteorológicos y justificar ventanas y tratamiento de huecos.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 14 — Aggregation Pipeline V: producción

Materializar métricas, repetir el proceso sin duplicados y medir un cuello de botella con explain.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 15 — Índices I: fundamentos y diseño

Diseñar y medir índices para cinco consultas de movies; justificar cada índice con un plan.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 16 — Índices II: especialización y planes

Comparar planes antes/después, eliminar un índice redundante y demostrar los efectos en lectura y escritura.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 17 — Consultas y búsquedas desde PyMongo

Implementar un cliente de búsqueda Mflix con filtros, paginación, pipeline y tratamiento de errores; validar resultados con consultas equivalentes en mongosh.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 18 — MongoDB Search I: búsqueda textual

Crear un buscador textual de películas con filtros de género y año; explicar el índice y el ranking.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 19 — MongoDB Search II: relevancia y experiencia

Añadir autocompletado, facetas y resaltado; evaluar diez consultas y documentar fallos del ranking.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 20 — Vectores y embeddings: fundamentos

Inventariar campos vectoriales reales, seleccionar uno y documentar modelo, dimensión, formato y métrica compatibles.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 21 — MongoDB Vector Search I: indexación y consultas

Ejecutar búsquedas ANN y ENN sobre embedded_movies y explicar sus diferencias sin mezclar modelos de embeddings.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 22 — MongoDB Vector Search II: evaluación y rendimiento

Crear un benchmark reproducible de al menos veinte consultas y comparar recall, latencia y filtros.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 23 — Búsqueda híbrida, reranking y RAG

Construir un buscador híbrido y medir calidad frente a búsqueda textual y vectorial. Como ampliación opcional, crear un RAG con citas y abstención ante falta de evidencia.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 24 — Búsquedas geoespaciales en Atlas

Buscar cines por proximidad y dentro de una zona; contrastar coordenadas, distancias y planes de consulta.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 25 — Optimización y evaluación integral de consultas

Construir un informe reproducible con al menos cinco consultas estructuradas y veinte consultas de búsqueda; presentar planes, latencias, relevancia y decisiones de mejora.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

### Bloque 26 — Proyecto experto: buscador de películas en Atlas

Entregar un buscador Mflix reproducible en Atlas con CRUD acotado, filtros, pipelines, Search, Vector Search, búsqueda híbrida y benchmark; RAG como ampliación opcional.

Entregar consultas o scripts, resultados comprobables, explicación de decisiones y limpieza de datos derivados cuando corresponda.

## Proyecto final y evaluación

Buscador de películas sobre sample_mflix con filtros estructurados, paginación,
pipelines, facetas, búsqueda textual, vectorial e híbrida. Cliente Python con
configuración externa. Colecciones derivadas para escrituras y pruebas.
Comparar al menos veinte consultas de búsqueda con juicios humanos y medir
calidad y latencia; contrastar ANN con ENN cuando esté disponible.
RAG es una extensión opcional: debe citar documentos recuperados y abstenerse
cuando no haya evidencia. No sustituye a la evaluación del buscador.

Rúbrica propuesta: corrección de consultas 25%, agregaciones y modelado 20%,
búsqueda y relevancia 30%, rendimiento e índices 15%, reproducibilidad 10%.
Superación: 80/100 y sin errores críticos en filtros de autorización, semántica
de arrays, cardinalidad de métricas o compatibilidad de embeddings.

## Estado del material

Verificados: numeración, correspondencia de bloques, sintaxis YAML y estructura
del ZIP. Los ejemplos no se han ejecutado contra una cuenta Atlas del alumno.
La compatibilidad de cada comando se valida al desarrollar y ejecutar la lección.
El profile.yaml es una especificación pedagógica independiente; adaptar claves
si el generador de cursos exige un esquema distinto.
