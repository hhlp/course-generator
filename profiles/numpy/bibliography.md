# Bibliografía --- NumPy 0 → Experto

## Criterio de uso

La documentación oficial de NumPy es la autoridad para APIs, semántica
actual y cambios entre versiones. Los libros aportan explicación,
práctica, contexto científico y modelos mentales, pero cualquier
diferencia con NumPy 2.x debe resolverse a favor de la documentación
oficial vigente.

## Principal

### Documentación oficial de NumPy

Referencia primaria para todo el PATH:

-   NumPy User Guide.
-   NumPy API Reference.
-   NumPy Tutorials.
-   NumPy 2.x release notes.
-   NumPy 2.0 migration guide.
-   NumPy C-API documentation.
-   NumPy typing documentation.
-   NumPy CPU/SIMD optimization documentation.
-   NumPy interoperability documentation.

Uso: bloques 1--30, especialmente APIs actuales, `dtype`, broadcasting,
random, linalg, FFT, I/O, typing, testing, internals, protocolos, C-API
y migración.

## Complementaria

### Python for Data Analysis — Wes McKinney, 3.ª edición

[Texto oficial del autor](https://wesmckinney.com/book/).

Uso principal:

-   modelo práctico de arrays;
-   indexación;
-   vectorización;
-   broadcasting;
-   procesamiento de datos;
-   relación NumPy/pandas.

Debe contrastarse con NumPy 2.x cuando el libro utilice versiones
anteriores.

### Python Data Science Handbook — Jake VanderPlas

[Texto web del autor](https://jakevdp.github.io/PythonDataScienceHandbook/)
y [repositorio oficial](https://github.com/jakevdp/PythonDataScienceHandbook).
Distinguir la edición del texto web de la edición de los notebooks usados.

Uso principal:

-   arrays;
-   broadcasting;
-   ufuncs;
-   agregaciones;
-   máscaras;
-   fancy indexing;
-   ordenación;
-   contexto del ecosistema científico.

Adecuado para reforzar los bloques fundamentales e intermedios.

## Profundización numérica

### Numerical Python — Robert Johansson, 3.ª edición

[Ficha editorial](https://link.springer.com/book/10.1007/979-8-8688-0413-7).

Uso principal:

-   computación científica;
-   álgebra lineal;
-   métodos numéricos;
-   señales;
-   simulación;
-   interacción con SciPy y Matplotlib.

Los ejemplos dependientes de versiones antiguas deben modernizarse.

### Elegant SciPy --- Juan Nunez-Iglesias, Stéfan van der Walt, Harriet Dashnow

Uso principal:

-   pensamiento vectorizado;
-   diseño de soluciones científicas;
-   transición desde NumPy hacia algoritmos especializados de SciPy.

No sustituye la documentación NumPy para semántica de APIs.

## Fundamentos matemáticos

### Introduction to Linear Algebra --- Gilbert Strang

Uso principal:

-   vectores y matrices;
-   sistemas lineales;
-   rango;
-   mínimos cuadrados;
-   autovalores;
-   factorizaciones;
-   interpretación matemática de operaciones de `numpy.linalg`.

### Numerical Linear Algebra --- Lloyd N. Trefethen y David Bau III

Uso principal:

-   estabilidad;
-   condicionamiento;
-   QR;
-   SVD;
-   algoritmos y razonamiento numérico.

Especialmente relevante para los bloques 13, 17 y el proyecto final.

## Rendimiento e internals

### High Performance Python — Micha Gorelick e Ian Ozsvald, 3.ª edición

[Ficha editorial](https://www.oreilly.com/library/view/high-performance-python/9781098165956/).

Uso principal:

-   medición;
-   coste de bucles Python;
-   memoria;
-   vectorización;
-   profiling;
-   paralelismo;
-   Numba y Cython.

Las recomendaciones concretas deben verificarse contra Python y NumPy
actuales.

### Guide to NumPy --- Travis E. Oliphant

Referencia histórica y conceptual para comprender el diseño de NumPy y
`ndarray`.

Uso recomendado:

-   internals;
-   arrays;
-   tipos;
-   ufuncs;
-   C-API.

No debe utilizarse como autoridad de API moderna sin contrastar con
NumPy 2.x.

## Extensiones

### Cython documentation

Uso:

-   typed memoryviews;
-   integración Python/C;
-   optimización de bucles numéricos.

### Numba documentation

Uso:

-   compilación JIT;
-   bucles numéricos especializados;
-   límites de compatibilidad con NumPy.

### Python/C API documentation

Uso:

-   ownership;
-   referencias;
-   buffers;
-   integración de extensiones.

### F2PY documentation de NumPy

Uso:

-   interoperabilidad con Fortran;
-   wrapping;
-   compilación y distribución.

## Interoperabilidad

Consultar documentación oficial actual de:

-   pandas;
-   Matplotlib;
-   SciPy;
-   scikit-learn;
-   xarray;
-   Dask;
-   CuPy;
-   JAX;
-   PyTorch;
-   Python Array API Standard;
-   DLPack.

Estas fuentes se utilizan en el bloque 25 y en los protocolos del bloque
27. El objetivo es comprender fronteras, conversiones, semántica y
costes de transferencia, no desarrollar cursos completos de esas
bibliotecas.

## Mapa bibliográfico por bloques

| Bloques | Fuentes prioritarias |
| --- | --- |
| 0–4 | NumPy, Python Data Science Handbook, Python for Data Analysis |
| 5–12 | NumPy, Python Data Science Handbook |
| 13–16 | NumPy, Numerical Python, textos de análisis numérico |
| 17–18 | NumPy, Strang, Trefethen y Bau |
| 19 | NumPy, Numerical Python |
| 20–22 | NumPy y Python |
| 23–24 | NumPy, High Performance Python |
| 25 | Documentación oficial de cada biblioteca |
| 26–27 | Internals, interoperabilidad, Array API y DLPack |
| 28 | C-API, Numba, Cython, F2PY, Python/C API |
| 29 | Notas de publicación y guías de migración |
| 30 | Fuentes de cada componente del proyecto |

## Política para material antiguo

Una fuente antigua sigue siendo útil para fundamentos, pero no se
copiarán mecánicamente:

-   APIs retiradas;
-   aliases de tipos eliminados;
-   patrones de `numpy.random` heredados como recomendación principal;
-   comportamientos de promoción anteriores a NumPy 2;
-   instrucciones de compilación obsoletas.

Cuando un libro y la documentación actual difieran, la lección debe
explicar la diferencia y enseñar primero la práctica moderna.


## Referencias especializadas adicionales por scope

### Scope: promoción, tipos y NumPy 2.x (bloques 4, 20, 26 y 29)

- NumPy Enhancement Proposal 50 (NEP 50): promoción de tipos y precisión de escalares.
- NEP 52: limpieza de la API de Python para NumPy 2.0.
- Documentación oficial de NumPy: DTypes, StringDType y migration guide.

### Scope: Array API e interoperabilidad (bloques 25 y 27)

- NEP 47: adopción del estándar Array API en NumPy (contexto histórico y de diseño).
- Python Array API Standard: especificación vigente y compatibilidad.
- Documentación de DLPack y protocolos de interoperabilidad NumPy.

### Scope: testing y contratos numéricos (bloques 13 y 22)

- pytest: documentación oficial para fixtures, parametrización y pruebas.
- Hypothesis: documentación oficial para property-based testing.
- numpy.testing: referencia oficial de comparaciones y tolerancias.

### Scope: rendimiento y concurrencia (bloques 23 y 24)

- NumPy CPU/SIMD optimizations: documentación oficial.
- threadpoolctl: documentación para inspección y control de pools de hilos.
- NumPy Global State y Thread Safety: documentación oficial.

### Scope: internals, extensiones y empaquetado (bloques 26–29)

- NumPy C-API, ufunc API, DType API y guía de migración a NumPy 2.
- Python/C API: referencias, buffers, manejo de errores y ownership.
- Python Packaging User Guide: compilación y distribución de extensiones.
- Cython, Numba y F2PY: documentación oficial de versiones compatibles.

## Política de consulta por lección

Priorizar documentación oficial de la versión objetivo; usar libros para modelos conceptuales y ejemplos. Verificar deprecaciones, disponibilidad de APIs y compatibilidad antes de generar ejercicios. Las fuentes externas de interoperabilidad no amplían el alcance a cursos completos de otras bibliotecas.

## Enlaces oficiales de consulta

Elegir la versión documentada al inicio de la generación. Los enlaces
/stable/ sirven como entrada; registrar la versión concreta consultada.
Para libros sin edición identificada, registrar la edición del ejemplar
utilizado antes de citar capítulos o páginas. No inferirla por el título.

| Área | Fuente |
| --- | --- |
| NumPy: guía y API | [Documentación](https://numpy.org/doc/) |
| Ufuncs, out y where | [Referencia](https://numpy.org/doc/stable/reference/ufuncs.html) |
| Migración a NumPy 2 | [Guía](https://numpy.org/doc/stable/numpy_2_0_migration_guide.html) |
| Memoria y copias | [Guía](https://numpy.org/doc/stable/user/basics.copies.html) |
| Concurrencia y free-threaded | [Thread safety](https://numpy.org/doc/stable/reference/thread_safety.html) |
| Array API | [Compatibilidad NumPy](https://numpy.org/doc/stable/reference/array_api.html) |
| Protocolos | [Interoperabilidad](https://numpy.org/doc/stable/user/basics.interoperability.html) |
| NEP 50 | [Propuesta](https://numpy.org/neps/nep-0050-scalar-promotion.html) |
| NEP 52 | [Propuesta](https://numpy.org/neps/nep-0052-python-api-cleanup.html) |
| NEP 47 | [Propuesta histórica](https://numpy.org/neps/nep-0047-array-api-standard.html) |
| Estándar Array API | [Especificación](https://data-apis.org/array-api/latest/) |
| DLPack | [Documentación](https://dmlc.github.io/dlpack/latest/) |
| Tipado | [numpy.typing](https://numpy.org/doc/stable/reference/typing.html) |
| Pruebas | [numpy.testing](https://numpy.org/doc/stable/reference/routines.testing.html) |
| pytest | [Documentación](https://docs.pytest.org/) |
| Hypothesis | [Documentación](https://hypothesis.readthedocs.io/) |
| Pools de hilos | [threadpoolctl](https://github.com/joblib/threadpoolctl) |
| C-API | [Referencia](https://numpy.org/doc/stable/reference/c-api/) |
| Python/C API | [Referencia](https://docs.python.org/3/c-api/) |
| Cython | [Documentación](https://docs.cython.org/) |
| Numba | [Documentación](https://numba.readthedocs.io/) |
| F2PY | [Documentación](https://numpy.org/doc/stable/f2py/) |
| Empaquetado | [Guía oficial](https://packaging.python.org/) |
