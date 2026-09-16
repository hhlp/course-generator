# Bibliografía — Python 3.15 en profundidad

## Política bibliográfica

Fecha de preparación: 2026-09-16. Esta selección es una propuesta de apoyo, no un inventario de libros que el usuario haya confirmado poseer. La documentación oficial de la versión objetivo prevalece sobre ejemplos antiguos. No es necesario comprar todos los libros para seguir la ruta.

No inventar capítulos, números de apartado ni páginas. Asignar lecturas por tema y, si se dispone del índice de la edición concreta, agregar referencias exactas verificadas. La edición de un libro no determina la versión de Python con la que deben ejecutarse sus ejemplos.

## Principal: fundamentos

Eric Matthes, **Python Crash Course, 3rd Edition**, No Starch Press. Base pedagógica para primeros programas, funciones, colecciones, clases y proyectos. Seleccionar las partes del lenguaje; los proyectos de frameworks o visualización no sustituyen los PATH específicos.

Recursos del autor: https://ehmatthes.github.io/pcc_3e/

## Profundización: modelo del lenguaje

Luciano Ramalho, **Fluent Python, 2nd Edition**, O'Reilly. Referencia de apoyo para modelo de datos, secuencias, funciones, decoradores, protocolos, tipado, generadores y concurrencia. Estudiarlo después de los fundamentos y contrastar cambios posteriores con la documentación oficial.

Sitio del libro: https://www.fluentpython.com/

## Complementaria: diseño y buenas prácticas

Brett Slatkin, **Effective Python: 125 Specific Ways to Write Better Python, 3rd Edition**, Addison-Wesley. Apoyo para APIs, robustez, diseño y rendimiento. El autor indica cobertura hasta Python 3.13: actualizar ejemplos y recomendaciones dependientes de versión para 3.15.

Sitio del autor: https://effectivepython.com/

## Consulta normativa — Python 3.15

- Documentación principal: https://docs.python.org/3.15/
- Tutorial: https://docs.python.org/3.15/tutorial/
- Referencia del lenguaje: https://docs.python.org/3.15/reference/
- Biblioteca estándar: https://docs.python.org/3.15/library/
- Tipos incorporados y contratos: https://docs.python.org/3.15/library/stdtypes.html
- Funciones incorporadas: https://docs.python.org/3.15/library/functions.html
- Modelo de datos: https://docs.python.org/3.15/reference/datamodel.html
- Expresiones: https://docs.python.org/3.15/reference/expressions.html
- Sentencias compuestas y gramática: https://docs.python.org/3.15/reference/compound_stmts.html
- itertools y recetas: https://docs.python.org/3.15/library/itertools.html
- functools: https://docs.python.org/3.15/library/functools.html
- collections: https://docs.python.org/3.15/library/collections.html
- typing: https://docs.python.org/3.15/library/typing.html
- asyncio: https://docs.python.org/3.15/library/asyncio.html
- threading: https://docs.python.org/3.15/library/threading.html
- multiprocessing: https://docs.python.org/3.15/library/multiprocessing.html
- concurrent.futures: https://docs.python.org/3.15/library/concurrent.futures.html
- C API: https://docs.python.org/3.15/c-api/
- Extensiones y embedding: https://docs.python.org/3.15/extending/

## Python moderno y evolución

- Novedades 3.15: https://docs.python.org/3.15/whatsnew/3.15.html
- Novedades 3.14: https://docs.python.org/3.14/whatsnew/3.14.html
- Calendario de Python 3.15, PEP 790: https://peps.python.org/pep-0790/
- Índice oficial de PEPs: https://peps.python.org/
- Guía de desarrollo de CPython: https://devguide.python.org/
- Código fuente de CPython: https://github.com/python/cpython

Consultar novedades y páginas concretas para verificar disponibilidad, estabilidad, deprecaciones y cambios de comportamiento. No enseñar una propuesta PEP como implementada solo por tener número.

## Herramientas — documentación de sus proyectos

- uv: https://docs.astral.sh/uv/
- Python Packaging User Guide: https://packaging.python.org/
- pytest: https://docs.pytest.org/
- Hypothesis: https://hypothesis.readthedocs.io/
- mypy: https://mypy.readthedocs.io/
- Ruff: https://docs.astral.sh/ruff/
- CFFI: https://cffi.readthedocs.io/
- Cython: https://docs.cython.org/
- pybind11: https://pybind11.readthedocs.io/

Elegir versiones compatibles con el intérprete del laboratorio y fijarlas en el proyecto. Estas referencias no implican haber probado todas las combinaciones con la RC de 3.15.

## Distribución de lecturas por bloques

| Bloques | Principal | Apoyo y consulta |
| --- | --- | --- |
| 0–3 | Python Crash Course | Tutorial, tipos, expresiones y uv |
| 4–6 | Python Crash Course | Fluent Python; referencia exhaustiva de métodos |
| 7–10 | Fluent Python | Tutorial, itertools, contextlib e importlib |
| 11–15 | Fluent Python | Effective Python, modelo de datos y typing |
| 16–18 | Documentación estándar | Effective Python; pathlib, sqlite3, subprocess y logging |
| 19–20 | Documentación de pruebas y packaging | Effective Python; pytest, Hypothesis y uv |
| 21 | Effective Python | Fluent Python y contratos del proyecto |
| 22–24 | Documentación de concurrencia y redes | Fluent Python y Effective Python, revisados por versión |
| 25–28 | Documentación de CPython y C API | Effective Python; documentación de bindings |
| 29–30 | Documentación oficial y What’s New | Effective Python y PEPs pertinentes |
| 31 | Fuentes de cada subsistema | Revisiones de diseño, pruebas y documentación del proyecto |

## Regla de referencias por lección

Dar título y autor del libro, edición, tema o capítulo confirmado, y enlaces oficiales pertinentes. Situar las referencias específicas antes de «🧠 QUÉ DEBES RECORDAR», para preservar el cierre pedagógico. Si no se puede verificar una página, omitir el número y referenciar el tema.
