# Bibliografía — Matplotlib + Seaborn + Polars

## Criterio de uso

La documentación oficial es la referencia principal de APIs y compatibilidad. No se presupone que el usuario posea libros adicionales. Los libros son apoyo conceptual opcional y nunca limitan la profundidad del PATH. Consultar documentación correspondiente a las versiones instaladas; no inventar números de capítulos o páginas. Las URLs stable pueden cambiar con el tiempo.

## Principal: documentación oficial

| Fuente | Uso en la ruta | Enlace |
| --- | --- | --- |
| Polars User Guide | Modelo de datos, expresiones, limpieza, IO, joins, tiempo, lazy y rendimiento; bloques 3–9 y 24–28 | https://docs.pola.rs/user-guide/ |
| Polars Python API | Firmas, tipos, restricciones y pruebas | https://docs.pola.rs/api/python/stable/reference/ |
| Polars: Visualization | Integración con herramientas gráficas; revisar conversiones y tipos | https://docs.pola.rs/user-guide/misc/visualization/ |
| Matplotlib Quick start | Interfaz explícita y estructura de figuras; bloque 10 | https://matplotlib.org/stable/users/explain/quick_start.html |
| Matplotlib User guide | Ejes, color, layouts, Artists, backends y publicación; bloques 10–17 | https://matplotlib.org/stable/users/index.html |
| Matplotlib API | Referencia de objetos y funciones | https://matplotlib.org/stable/api/index.html |
| Matplotlib Gallery | Ejemplos para adaptar y explicar, sin copiarlos sin contexto | https://matplotlib.org/stable/gallery/index.html |
| Seaborn | Documentación y acceso a tutoriales, ejemplos y API; bloques 18–23 | https://seaborn.pydata.org/ |
| Seaborn Tutorial | Semántica, distribuciones, categorías, facetas y estadística | https://seaborn.pydata.org/tutorial.html |
| Seaborn API | Funciones clásicas y objetos declarativos | https://seaborn.pydata.org/api.html |

## Complementaria: fundamentos e interoperabilidad

1. Python, documentación oficial: https://docs.python.org/3/ — fundamentos del bloque 0 y organización de proyectos.
2. NumPy, documentación oficial: https://numpy.org/doc/ — arrays, dtypes, dimensiones y vectorización.
3. pandas, documentación oficial: https://pandas.pydata.org/docs/ — conversiones e interoperabilidad; no sustituye Polars como núcleo del PATH.
4. Apache Arrow, documentación oficial de Python: https://arrow.apache.org/docs/python/ — tipos columnares e intercambio de datos.
5. uv, documentación oficial: https://docs.astral.sh/uv/ — entornos y dependencias reproducibles.
6. JupyterLab, documentación oficial: https://jupyterlab.readthedocs.io/en/stable/ — entorno interactivo.
7. SciPy, documentación oficial: https://docs.scipy.org/doc/scipy/ — herramientas estadísticas y clustering cuando la práctica lo requiera.

## Profundización conceptual opcional

1. Claus O. Wilke, Fundamentals of Data Visualization. Lectura sobre selección de gráficos, color, escalas, incertidumbre y composición. Edición en línea del autor: https://clauswilke.com/dataviz/ . Útil para bloques 1–2, 11–16 y proyectos.
2. Nicolas P. Rougier, Scientific Visualization: Python + Matplotlib. Apoyo para diseño científico y personalización avanzada. Repositorio del autor: https://github.com/rougier/scientific-visualization-book . Útil para bloques 10–17; contrastar ejemplos con la API instalada.
3. Jake VanderPlas, Python Data Science Handbook. Apoyo para NumPy y visualización; los apartados basados en pandas complementan la interoperabilidad, no reemplazan el recorrido de Polars. Edición en línea del autor: https://jakevdp.github.io/PythonDataScienceHandbook/ . Revisar antigüedad de APIs antes de reutilizar ejemplos.

## Asignación de lecturas por etapa

| Bloques | Principal | Complementaria |
| --- | --- | --- |
| 0–2 | Python, NumPy y documentación de entorno | Wilke: fundamentos y representación |
| 3–9 | Polars User Guide y API | Arrow y pandas para interoperabilidad |
| 10–17 | Matplotlib User guide, API y Gallery | Rougier y Wilke |
| 18–23 | Seaborn Tutorial y API | Matplotlib y fundamentos estadísticos |
| 24–27 | Referencias oficiales de las tres bibliotecas | uv y herramientas de pruebas |
| 28 | Fuentes específicas de las técnicas utilizadas | Diseño e interpretación de resultados |

## Referencias en cada lección

Incluir una lectura principal y, cuando aporten valor, lecturas complementarias o de profundización. Citar título y URL específica del tema; para libros usar capítulos sólo cuando hayan sido comprobados en la edición consultada. Señalar APIs obsoletas, alternativas actuales y límites de compatibilidad. Distinguir documentación consultada de lectura propuesta.

Las páginas de integración de Polars, la guía inicial de Matplotlib y la portada de Seaborn se consultaron al preparar este paquete. Las demás referencias se ofrecen como rutas de consulta; no implican que todos sus ejemplos se hayan ejecutado.
