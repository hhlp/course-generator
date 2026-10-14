# PANDAS 3 — DOMAIN

## Propósito
Curso 0 → experto de **22 bloques y 414 lecciones**, conservando íntegramente las 216 lecciones de origen y ampliándolas con 198 lecciones de profundización. El objetivo es dominar manipulación tabular, semántica de tipos, análisis, ingeniería de datos con pandas, rendimiento, testing y migración a pandas 3.x.

## Fuentes y precedencia
1. **Documentación oficial de pandas 3.x:** referencia normativa para API, semántica y compatibilidad.
2. **Daniel Y. Chen — Pandas for Everyone, Second Edition:** base pedagógica, ejemplos y progresión.
3. **Matt Harrison — Effective Pandas: Patterns for Data Manipulation:** patrones idiomáticos, rendimiento, tipos y encadenamiento.
4. **Boris Paskhaver — Pandas in Action:** ejercicios, workflows y resolución de problemas.

Los libros pueden tratar versiones anteriores; sus ejemplos deben adaptarse y contrastarse con la documentación oficial. No inventar referencias a páginas o capítulos. Verificar comportamientos sensibles a la versión menor de pandas 3.x.

## Progresión
- **Bloques 0–5:** entorno, Series, DataFrame, selección, índices, dtypes, nulos y Copy-on-Write.
- **Bloques 6–13:** I/O, limpieza, transformación, GroupBy, joins, reshape, texto, categorías y tiempo.
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
