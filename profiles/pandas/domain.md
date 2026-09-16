# Dominio — Pandas 3 en profundidad

## Propósito

Este PATH enseña pandas 3 desde cero hasta un nivel experto y profesional. No está diseñado como una colección de recetas aisladas: desarrolla el modelo mental necesario para comprender Series, DataFrame, Index, dtypes, alineación, missing data, transformación, agregación, reshaping, series temporales, I/O, rendimiento, Copy-on-Write, PyArrow, testing e internals.

## Plataforma

- Python moderno compatible con pandas 3.x.
- pandas 3.x como versión objetivo.
- NumPy y PyArrow como tecnologías fundamentales de interoperabilidad.
- Jupyter/IPython para exploración, sin convertir los notebooks en sustituto de código mantenible.
- SQLAlchemy/PostgreSQL cuando se estudie integración SQL.
- Matplotlib/Seaborn solo como integración; su aprendizaje profundo pertenece a sus PATH específicos.
- Polars se trata únicamente como interoperabilidad y contraste conceptual; su aprendizaje profundo pertenece a su PATH específico.

## Alcance pedagógico

El alumno comienza sin asumir conocimientos previos de pandas. Al terminar debe poder diseñar, implementar, depurar, probar, optimizar y mantener pipelines de datos profesionales basados en pandas 3.

Cada lección debe comenzar con:

🎯 OBJETIVO

El desarrollo debe ser completo, progresivo, técnico y didáctico. No debe limitarse a resumir la API.

Cuando aporte valor debe incluir:

🧪 Laboratorio/ejemplos
⚠️ Errores frecuentes
💡 Idea importante

Cada lección debe terminar con:

🧠 QUÉ DEBES RECORDAR

Este cierre debe contener entre 3 y 7 ideas esenciales y no limitarse a repetir el objetivo.

## Principios técnicos

1. Explicar primero el modelo mental y después la sintaxis.
2. Diferenciar selección por etiqueta y por posición.
3. Tratar la alineación automática como una característica central de pandas.
4. Enseñar dtypes de forma explícita, incluyendo nullable dtypes y Arrow-backed data.
5. Explicar missing data según el dtype y no como un único caso genérico.
6. Favorecer operaciones vectorizadas y APIs nativas frente a loops y apply innecesarios.
7. Enseñar merges con cardinalidad y validación.
8. Enseñar GroupBy como split-apply-combine.
9. Introducir method chaining y pipe para construir pipelines legibles.
10. Tratar Copy-on-Write como parte del modelo moderno de pandas 3.
11. Separar optimización de CPU, memoria e I/O.
12. Incluir testing, debugging, profiling y diseño profesional.
13. Llegar a internals y extensibilidad sin depender de detalles privados inestables como API pública.
14. Señalar deprecaciones y diferencias relevantes entre pandas 2.x y 3.x.
15. Priorizar la documentación oficial cuando exista discrepancia con libros anteriores a pandas 3.

## Ejemplos

Los ejemplos deben ser ejecutables y crecer progresivamente. Deben incluir datasets pequeños para explicar semántica y datasets más realistas para laboratorios.

Cuando se enseñe una API importante se debe mostrar, según proceda:

- firma o forma conceptual de uso;
- tipos de entrada;
- resultado esperado;
- efecto del índice y los dtypes;
- comportamiento con missing values;
- errores frecuentes;
- implicaciones de rendimiento;
- alternativa recomendada cuando exista un antipatrón común.

## Profundidad

El PATH debe cubrir tanto uso cotidiano como conocimiento avanzado:

Series → DataFrame → Index → dtypes → missing data → strings → MultiIndex → combinación → reshaping → GroupBy → windows → time series → I/O → limpieza → estadística → visualización → pipelines → rendimiento → pandas 3 → PyArrow → SQL → testing → troubleshooting → internals → extensibilidad → arquitectura → interoperabilidad → patrones → antipatrones → proyecto experto.

## Límites

Este PATH no sustituye:

- un PATH completo de Python;
- un PATH completo de NumPy;
- un PATH completo de SQL/PostgreSQL;
- un PATH completo de Matplotlib/Seaborn;
- un PATH completo de Polars.

Se explicará lo necesario para comprender pandas y su interoperabilidad, remitiendo conceptualmente a esos dominios cuando corresponda.
