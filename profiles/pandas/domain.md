# PANDAS 3 — DOMAIN

## Propósito
Curso 0 → experto de 18 bloques y 216 lecciones para dominar Pandas 3 en manipulación, limpieza, transformación, análisis y pipelines reproducibles.

## Fuentes y función
- **Daniel Y. Chen — Pandas for Everyone, Second Edition:** referencia pedagógica principal.
- **Matt Harrison — Effective Pandas: Patterns for Data Manipulation:** patrones idiomáticos, vectorización, tipos, method chaining, rendimiento, legibilidad y antipatterns.
- **Boris Paskhaver — Pandas in Action:** práctica, transformación, análisis y workflows completos.
- **Documentación oficial de pandas 3.x:** referencia normativa para API y comportamiento vigente.

## Regla de versión
Los libros aportan conceptos, pedagogía, patrones y práctica. Cuando reflejen una versión anterior, el código se adapta a Pandas 3.x. La documentación oficial prevalece para API, Copy-on-Write, tipos, deprecaciones y migración.

## Progresión
**Bloques 0–5:** fundamentos, Series/DataFrame, selección, índices, tipos, nulos y Copy-on-Write.
**Bloques 6–13:** I/O, limpieza, transformación, GroupBy, joins, reshape, texto, categorías y tiempo.
**Bloques 14–16:** EDA, rendimiento, Pandas idiomático, pipelines, calidad y testing.
**Bloque 17:** migración a Pandas 3 y proyecto integral.

## Principios
- Copy-on-Write forma parte del modelo mental central.
- Se prioriza vectorización cuando es apropiada.
- Se enseña alineación por etiquetas explícitamente.
- Los dtypes se tratan como decisiones de corrección, memoria y rendimiento.
- Se evita chained assignment y se enseña asignación segura.
- Effective Pandas se integra transversalmente, no solo en optimización.
- Se usan `assign`, `pipe` y method chaining para construir pipelines legibles.
- El rendimiento se demuestra mediante medición.
- Las referencias exactas de capítulos/páginas solo se incluyen cuando estén verificadas.

## Fuera de alcance
NumPy, SQL, visualización, estadística, Polars y diseño de bases de datos aparecen solo cuando son necesarios para comprender Pandas; sus contenidos completos pertenecen a sus respectivos learning paths.
