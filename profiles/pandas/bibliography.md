# Bibliografía — Pandas 3 en profundidad

## Fuente normativa principal

### pandas documentation

La documentación oficial de pandas 3.x es la referencia normativa del PATH. Debe utilizarse para verificar API, semántica actual, deprecaciones, cambios incompatibles, Copy-on-Write, tipos de datos, I/O, GroupBy, ventanas, series temporales e internals documentados.

Se debe priorizar siempre sobre ejemplos de libros escritos para versiones anteriores cuando exista una diferencia de comportamiento.

## Libro principal

### Pandas for Everyone, 2nd Edition — Daniel Y. Chen

Libro principal para la progresión pedagógica desde fundamentos hasta manipulación y análisis práctico de datos. Sus ejemplos deben adaptarse a pandas 3.x cuando la API o la semántica hayan cambiado.

Uso principal:

- Series y DataFrame
- selección y transformación
- tidy data
- missing data
- GroupBy
- combinación
- fechas
- análisis práctico
- workflows reproducibles

## Referencias complementarias

### Python for Data Analysis — Wes McKinney

Referencia conceptual y práctica especialmente valiosa para comprender el modelo de datos de pandas, indexación, limpieza, reshaping, GroupBy y series temporales. Verificar siempre los detalles de API frente a pandas 3.x.

### Effective Pandas — Matt Harrison

Referencia para patrones idiomáticos, legibilidad, dtypes, method chaining, rendimiento y eliminación de antipatrones.

### Modern Pandas — Tom Augspurger

Material complementario para estilo idiomático, method chaining, rendimiento y diseño de transformaciones. Debe reinterpretarse a la luz de pandas 3.x.

## Ecosistema

### NumPy documentation

Referencia para arrays, dtypes, broadcasting, vectorización y las fronteras de interoperabilidad pandas/NumPy.

### Apache Arrow / PyArrow documentation

Referencia para Arrow memory model, Arrow-backed data, interoperabilidad, Parquet y comportamiento de tipos relacionados con PyArrow.

### SQLAlchemy documentation

Referencia para conexiones y operaciones SQL utilizadas por las APIs de pandas.

### Matplotlib documentation

Referencia únicamente para la integración de `Series.plot` y `DataFrame.plot` y la personalización que dependa del backend Matplotlib.

## Código fuente e internals

Para bloques avanzados se puede consultar el repositorio y código fuente de pandas con un objetivo educativo:

- arquitectura;
- ExtensionArray;
- ExtensionDtype;
- indexación;
- algoritmos;
- GroupBy;
- joins;
- ventanas;
- Copy-on-Write;
- integración con Arrow.

Los detalles privados del código fuente no deben presentarse como contratos estables de API.

## Uso por bloques

- Bloques 0–5: Pandas for Everyone 2e + documentación oficial.
- Bloques 6–12: documentación oficial + Python for Data Analysis.
- Bloques 13–17: documentación oficial + Pandas for Everyone + Effective Pandas.
- Bloques 18–20: documentación oficial + Effective Pandas + NumPy/PyArrow.
- Bloques 21–23: documentación oficial + SQLAlchemy + prácticas de testing de Python.
- Bloques 24–25: documentación de desarrollo y código fuente de pandas.
- Bloques 26–29: Effective Pandas + documentación oficial + referencias del ecosistema.
- Bloque 30: todas las fuentes anteriores, priorizando documentación oficial de pandas 3.x.

## Política de versiones

Este curso tiene como objetivo pandas 3.x. Cualquier material bibliográfico basado en pandas 1.x o 2.x debe considerarse una fuente conceptual y pedagógica, no normativa.

Cuando un libro y pandas 3.x difieran:

1. explicar el comportamiento actual;
2. identificar, cuando sea didácticamente útil, el comportamiento histórico;
3. mostrar la migración;
4. evitar enseñar como recomendada una API deprecada;
5. verificar la alternativa moderna en la documentación oficial.

## Referencias bibliográficas específicas

- Chen, Daniel Y. *Pandas for Everyone*, 2nd Edition.
- McKinney, Wes. *Python for Data Analysis*.
- Harrison, Matt. *Effective Pandas*.
- pandas Development Team. *pandas Documentation*, versión 3.x.
- NumPy Developers. *NumPy Documentation*.
- Apache Arrow Project. *Apache Arrow / PyArrow Documentation*.
- SQLAlchemy Authors. *SQLAlchemy Documentation*.
- Matplotlib Development Team. *Matplotlib Documentation*.
