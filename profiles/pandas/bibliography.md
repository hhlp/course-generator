# Bibliografía — Pandas 3 (22 bloques)

## A. Referencias principales

### A1. Daniel Y. Chen — *Pandas for Everyone, Second Edition*
**Rol:** base pedagógica de cero a intermedio-avanzado. **Ámbitos:** Series/DataFrame, limpieza, transformación, análisis, joins, agrupación y ejercicios. Priorizar bloques 0–14 y 21.

### A2. Matt Harrison — *Effective Pandas: Patterns for Data Manipulation*
**Rol:** patrones idiomáticos y decisiones de diseño. **Ámbitos:** indexación, tipos, vectorización, encadenamiento, legibilidad, memoria, GroupBy y rendimiento. Transversal, especialmente bloques 2–5, 8–10, 15–20.

### A3. Boris Paskhaver — *Pandas in Action*
**Rol:** práctica y problemas completos. **Ámbitos:** selección, transformación, joins, reshape, tiempo y análisis. Priorizar bloques 1–14, 16 y 21.

## B. Referencia normativa

### B1. Documentación oficial de pandas 3.x
https://pandas.pydata.org/docs/
**Autoridad normativa:** APIs, tipos, Copy-on-Write, deprecaciones y migración. Consultar la documentación de la versión menor objetivo.

### B2. Guías oficiales por scope
- **Fundamentos e indexación:** User Guide — Indexing and selecting data; Essential basic functionality.
- **Tipos y nulos:** User Guide — Missing data; Text data; Categorical data; Extension types.
- **Memoria:** User Guide — Copy-on-Write; Scaling to large datasets.
- **I/O y Arrow:** User Guide — IO tools; PyArrow Functionality; documentación Apache Arrow y Parquet.
- **GroupBy, reshape y joins:** User Guide — Group by; Merge, join, concatenate and compare; Reshaping and pivot tables.
- **Tiempo:** User Guide — Time series / date functionality; Windowing operations.
- **Rendimiento:** User Guide — Enhancing performance; Scaling to large datasets.
- **Migración:** What's new / release notes y guías oficiales de migración aplicables a pandas 3.x.
- **Testing:** pandas.testing API; documentación de pytest e Hypothesis para pruebas de transformaciones.

## C. Mapa por bloques

| Bloques | Fuente pedagógica | Patrones/práctica | Referencia normativa prioritaria |
|---|---|---|---|
| 0–3 | Chen | Harrison, Paskhaver | Objetos, indexación y alineación |
| 4–5 | Chen | Harrison | Tipos, nulos y Copy-on-Write |
| 6–8 | Chen | Harrison, Paskhaver | I/O y transformación |
| 9–11 | Chen | Harrison, Paskhaver | GroupBy, joins y reshape |
| 12–13 | Chen | Paskhaver, Harrison | Texto, categorías y tiempo |
| 14–16 | Chen | Harrison, Paskhaver | EDA, rendimiento y testing |
| 17 | Complementaria | Harrison | Arquitectura y APIs públicas |
| 18 | Complementaria | Harrison | Arrow, dtypes y Parquet |
| 19 | Complementaria | Harrison | Performance y escalabilidad |
| 20 | Complementaria | Harrison, Paskhaver | Testing API, pytest e Hypothesis |
| 21 | Chen | Harrison, Paskhaver | Release notes y migración |

## D. Política de uso
1. No exigir todos los libros en cada lección: elegir por pertinencia.
2. La documentación oficial prevalece frente a ejemplos obsoletos de libros.
3. No inventar capítulos, páginas, citas o benchmarks; comprobar antes de referenciarlos.
4. Indicar diferencias de comportamiento entre versiones cuando afecten a la corrección.
5. Las referencias a NumPy, SQL y Polars son contextuales, no sustituyen sus learning paths.
