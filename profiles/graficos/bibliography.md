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

## Profundización por API y calidad (ampliación)

- **Polars Lazy API y optimización:** https://docs.pola.rs/user-guide/lazy/ — optimizador, planes y ejecución; contrastar las opciones de motor streaming con la versión instalada.
- **Polars expresiones:** https://docs.pola.rs/user-guide/expressions/ — contextos, namespaces y ventanas.
- **Polars testing:** https://docs.pola.rs/api/python/stable/reference/testing.html — pruebas de Series y DataFrame.
- **Matplotlib Artists:** https://matplotlib.org/stable/users/explain/artists/artist_intro.html — arquitectura y jerarquía.
- **Matplotlib transforms:** https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html — coordenadas y composición.
- **Matplotlib backends:** https://matplotlib.org/stable/users/explain/figure/backends.html — renderizado e interactividad.
- **Matplotlib events:** https://matplotlib.org/stable/users/explain/figure/event_handling.html — callbacks y eventos.
- **Seaborn objects:** https://seaborn.pydata.org/tutorial/objects_interface.html — API declarativa, marcas, estadísticas y composición.
- **Seaborn statistical estimation:** https://seaborn.pydata.org/tutorial/error_bars.html — intervalos, incertidumbre y estimadores.
- **pytest:** https://docs.pytest.org/ — fixtures, parametrización y pruebas reproducibles.

Las URLs son puntos de consulta, no certificación de disponibilidad futura. Comprobar clases, parámetros y comportamientos en las versiones efectivamente instaladas.


## Referencias específicas de la revisión de progresión

- Polars, uso de la API lazy: https://docs.pola.rs/user-guide/lazy/using/ — scan, lazy y separación entre definición y ejecución.
- Polars, when: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.when.html — evaluación de ramas y restricciones de las expresiones.
- Polars, fuentes y sinks: https://docs.pola.rs/user-guide/lazy/sources_sinks/ — escritura de consultas y límites de materialización.
- Matplotlib, imágenes con valores enmascarados: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html — máscara y colores de valores especiales.
- Matplotlib, orientación y coordenadas de imshow: https://matplotlib.org/stable/users/explain/artists/imshow_extent.html — origin, extent y relación con los ejes.

Estas cinco páginas se consultaron para esta revisión. Su consulta no implica haber ejecutado los ejemplos. Para denominadores, ponderaciones y paradoja de Simpson, desarrollar ejemplos numéricos pequeños verificables; usar Wilke como apoyo para agregación e interpretación visual, sin atribuirle capítulos no comprobados.
