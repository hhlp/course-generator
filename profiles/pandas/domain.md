# PANDAS 3 — DOMAIN

## Propósito
Curso 0 → experto de **22 bloques y 421 lecciones**, revisadas a partir de las 414 lecciones entregadas. Se conservan sus contenidos, se reubican seis lecciones para respetar prerrequisitos y se añaden siete lecciones. La conservación de las 216 lecciones históricas no se ha verificado contra su versión base. El objetivo es dominar manipulación tabular, semántica de tipos, análisis, ingeniería de datos con pandas, rendimiento, testing y migración a pandas 3.x.

## Fuentes y precedencia
1. **Documentación oficial de pandas 3.x:** referencia normativa para API, semántica y compatibilidad.
2. **Daniel Y. Chen — Pandas for Everyone, Second Edition:** base pedagógica, ejemplos y progresión.
3. **Matt Harrison — Effective Pandas: Patterns for Data Manipulation:** patrones idiomáticos, rendimiento, tipos y encadenamiento.
4. **Boris Paskhaver — Pandas in Action:** ejercicios, workflows y resolución de problemas.

Los libros pueden tratar versiones anteriores; sus ejemplos deben adaptarse y contrastarse con la documentación oficial. No inventar referencias a páginas o capítulos. Verificar comportamientos sensibles a la versión menor de pandas 3.x.

## Progresión
- **Bloques 0–5:** entorno, Series, DataFrame, selección, índices, dtypes, nulos y Copy-on-Write.
- **Bloques 6–13:** I/O, limpieza, transformación, GroupBy, joins, reshape, texto, categorías y tiempo. Las ventanas y Grouper temporal se desarrollan en el bloque 13, después de introducir fechas.
- **Bloques 14–16:** EDA, rendimiento inicial, patrones idiomáticos, calidad, testing y producción.
- **Bloque 17:** arquitectura interna, semántica de memoria y límites de APIs privadas.
- **Bloque 18:** Apache Arrow, tipos modernos, Parquet e interoperabilidad.
- **Bloque 19:** rendimiento experto, profiling y escalabilidad en memoria.
- **Bloque 20:** testing avanzado, contratos y arquitectura de pipelines.
- **Bloque 21:** migración desde pandas 2 y proyecto integral reproducible.

## Principios de profundidad
Cada lección comienza con un objetivo y desarrolla conceptos, mecánica paso a paso, ejemplos ejecutables, casos límite, errores frecuentes, laboratorio y recordatorio final. Cuando aplique, añadir costes de memoria, complejidad, comparación de alternativas y pruebas automatizadas. Los laboratorios deben usar datasets pequeños reproducibles antes de escalar a escenarios realistas.

## Reglas técnicas
- Copy-on-Write es parte del modelo mental central: explicar aislamiento, asignación y coste de copia.
- Priorizar semántica correcta, alineación por etiquetas y nulos antes de optimizar.
- Distinguir dtypes NumPy, nullable y Arrow-backed; no afirmar equivalencia universal.
- Preferir operaciones vectorizadas cuando se demuestre que son adecuadas; `apply` y la iteración también tienen casos legítimos.
- Comparar benchmarks en condiciones controladas; no afirmar mejoras sin medir.
- Separar APIs públicas estables de internals exploratorios.
- Validar claves y cardinalidad antes de combinar datasets; explicar comportamiento de nulos en joins.
- Considerar DST, zonas horarias, calendarios y frecuencias en series temporales.
- Construir pipelines testeables, idempotentes cuando proceda y reproducibles.
- Para migraciones, usar pruebas de regresión y matriz de cambios, sin suponer compatibilidad automática.

## Fuera de alcance
NumPy, SQL, Polars, estadística avanzada, visualización especializada y diseño de bases de datos se abordan solo en la medida necesaria para pandas; sus itinerarios completos son independientes.

## Evaluación
Checkpoints por etapa, ejercicios de depuración, comparaciones de implementaciones, profiling, tests automatizados y proyecto final con ingestión, validación, transformación, agregación, persistencia, informe y documentación de migración.

## Precisiones de la revisión
- Introducir MultiIndex antes de selección transversal con xs.
- Enseñar ordenación estable, selección de extremos, discretización, relleno,
  interpolación y operaciones acumulativas con sus casos límite.
- Distinguir object, str (NaN), string (pd.NA), almacenamiento Python/PyArrow
  y ArrowDtype; el backend físico no determina por sí solo la semántica de nulos.
- No asumir resolución temporal nanosegundo: comprobar dtype, unidad,
  precisión y rango antes de convertir o comparar resultados.
- Incluir anti joins left_anti y right_anti y su validación de claves.
- Bloque 15: aprender a medir y aplicar optimizaciones locales. Bloque 19:
  atribuir costes, medir variabilidad y resolver cargas con presupuesto de memoria.
- Bloque 16: construir y probar un pipeline pequeño. Bloque 20: evolucionar
  contratos, generar casos adversos y verificar compatibilidad de dependencias.
- Los laboratorios de código incluyen assertions o tests; los de instalación
  y entorno incluyen comandos de diagnóstico y criterios de éxito verificables.
- Fijar una versión concreta de pandas 3.x y dependencias en el lockfile de
  cada laboratorio; contrastar las APIs con su documentación correspondiente.
