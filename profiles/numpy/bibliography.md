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

### Python for Data Analysis --- Wes McKinney

Uso principal:

-   modelo práctico de arrays;
-   indexación;
-   vectorización;
-   broadcasting;
-   procesamiento de datos;
-   relación NumPy/pandas.

Debe contrastarse con NumPy 2.x cuando el libro utilice versiones
anteriores.

### Python Data Science Handbook --- Jake VanderPlas

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

### Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib --- Robert Johansson

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

### High Performance Python --- Micha Gorelick e Ian Ozsvald

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

  -----------------------------------------------------------------------
  Bloques                             Fuentes prioritarias
  ----------------------------------- -----------------------------------
  0--4                                NumPy docs, Python Data Science
                                      Handbook, Python for Data Analysis

  5--12                               NumPy docs, Python Data Science
                                      Handbook

  13--16                              NumPy docs, Numerical Python,
                                      textos de análisis numérico

  17--18                              NumPy docs, Strang, Trefethen & Bau

  19                                  NumPy docs, Numerical Python

  20--22                              NumPy docs y documentación Python

  23--24                              NumPy docs, High Performance Python

  25                                  documentación oficial de cada
                                      biblioteca interoperable

  26--27                              NumPy internals, interoperability,
                                      Array API y DLPack

  28                                  NumPy C-API, Numba, Cython, F2PY,
                                      Python/C API

  29                                  NumPy release notes y migration
                                      guides

  30                                  conjunto completo de fuentes según
                                      cada componente
  -----------------------------------------------------------------------

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
