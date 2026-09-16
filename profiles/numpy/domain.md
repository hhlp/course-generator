# NumPy --- Domain

## Identidad del PATH

**Nombre:** NumPy --- Learning Path 0 → Experto\
**Dominio:** cálculo numérico, computación científica y programación de
arrays con Python.\
**Plataforma principal:** Python moderno + NumPy 2.x.\
**Nivel:** fundamentos → avanzado → internals → extensibilidad → nivel
experto.

## Propósito

Este PATH enseña NumPy como sistema de computación numérica, no como una
simple colección de funciones. El estudiante debe comprender el modelo
de arrays multidimensionales, tipos de datos, ejes, broadcasting,
vectorización, memoria, estabilidad numérica, álgebra lineal, generación
aleatoria, persistencia, rendimiento, interoperabilidad, protocolos e
internals.

El objetivo final es poder diseñar, implementar, verificar, optimizar y
mantener software numérico basado en NumPy, justificando las decisiones
sobre formas, tipos, memoria, precisión y rendimiento.

## Alcance

El PATH cubre:

-   fundamentos de Python necesarios para trabajar con NumPy;
-   creación, inspección, indexación y transformación de `ndarray`;
-   `dtype`, casting, promoción de tipos y precisión;
-   vistas, copias, ownership, strides y layout de memoria;
-   broadcasting, vectorización y universal functions;
-   reducciones, acumulaciones, composición, búsqueda y conjuntos;
-   estadística descriptiva, NaN y arrays enmascarados;
-   `numpy.random`, reproducibilidad, simulación y Monte Carlo;
-   álgebra lineal, tensores, `einsum`, FFT y métodos numéricos;
-   fechas, texto, tipos estructurados y operaciones de bits;
-   `.npy`, `.npz`, texto, binarios y memory mapping;
-   diseño de APIs numéricas, `numpy.typing` y `numpy.testing`;
-   profiling conceptual, rendimiento, memoria y procesamiento por
    bloques;
-   BLAS/LAPACK, hilos, GIL y multiprocesamiento;
-   interoperabilidad con pandas, Matplotlib, SciPy, scikit-learn,
    xarray, Dask, CuPy, JAX y PyTorch;
-   internals de `ndarray`;
-   protocolos `__array__`, `__array_ufunc__`, `__array_function__`,
    Array API y DLPack;
-   Numba, Cython, C/C++, C-API de NumPy, generalized ufuncs y F2PY;
-   NumPy 2.x, migración, compatibilidad y mantenimiento;
-   proyecto final integrador de nivel experto.

## Límites del PATH

NumPy es el núcleo del PATH. Las bibliotecas externas se estudian
únicamente hasta el nivel necesario para comprender interoperabilidad,
límites y transferencia de datos. No se convierte el PATH en un curso
completo de pandas, SciPy, Matplotlib, scikit-learn, Dask, CuPy, JAX,
PyTorch, Cython o Numba.

Los fundamentos matemáticos se explican cuando son necesarios para
comprender correctamente una operación NumPy, pero el PATH no sustituye
cursos completos de análisis numérico, estadística, probabilidad,
álgebra lineal o procesamiento digital de señales.

## Plataforma y versiones

La referencia principal debe ser la documentación oficial de la versión
estable de NumPy 2.x disponible durante la generación de cada lección.

Cuando una API o comportamiento dependa de la versión:

1.  indicar la versión relevante;
2.  distinguir comportamiento actual de comportamiento histórico;
3.  evitar enseñar APIs obsoletas como práctica recomendada;
4.  explicar migraciones cuando aporten valor;
5.  contrastar libros antiguos con la documentación oficial actual.

## Convenciones de código

Usar normalmente:

``` python
import numpy as np
```

Los ejemplos deben favorecer:

-   código ejecutable y autocontenido;
-   nombres de variables descriptivos;
-   shapes suficientemente pequeños para inspección manual;
-   impresión explícita de `shape`, `dtype`, `strides` o resultados
    cuando ayude;
-   `np.random.default_rng()` frente a la API aleatoria global heredada;
-   `@` o `np.matmul` cuando se quiera expresar producto matricial;
-   `np.linalg.solve` frente a calcular una inversa para resolver
    sistemas;
-   tolerancias justificadas en comparaciones de coma flotante;
-   mediciones antes de afirmar que una optimización mejora el
    rendimiento.

## Tratamiento pedagógico obligatorio

Cada lección debe comenzar con:

# 🎯 OBJETIVO

El desarrollo debe ser completo, progresivo, técnico y didáctico. No
debe limitarse a enumerar APIs.

Cuando aporten valor, incluir:

-   🧪 Laboratorio / ejemplos
-   ⚠️ Errores frecuentes
-   💡 Idea importante

Cada lección debe terminar con:

# 🧠 QUÉ DEBES RECORDAR

Este cierre debe contener entre 3 y 7 ideas esenciales y no limitarse a
repetir el objetivo.

## Profundidad esperada

Para cada concepto relevante explicar, cuando corresponda:

1.  qué problema resuelve;
2.  modelo mental;
3.  sintaxis y firma conceptual;
4.  parámetros importantes;
5.  forma y `dtype` de entrada;
6.  forma y `dtype` del resultado;
7.  significado de `axis`;
8.  broadcasting implicado;
9.  vistas frente a copias;
10. costes de memoria;
11. estabilidad y precisión numérica;
12. complejidad o rendimiento práctico;
13. casos límite;
14. errores frecuentes;
15. alternativas y criterios de elección;
16. cambios relevantes entre versiones.

## Arrays y formas

No describir una operación multidimensional únicamente con palabras.
Siempre que sea útil, mostrar las formas:

``` text
A.shape == (m, n)
x.shape == (n,)
A @ x -> (m,)
```

En broadcasting, mostrar la alineación conceptual de dimensiones.

Distinguir cuidadosamente:

``` text
(n,)
(n, 1)
(1, n)
```

## `axis`

`axis` debe enseñarse como eje que la operación consume o sobre el que
actúa, explicando qué dimensiones permanecen en el resultado.

No usar reglas memorísticas ambiguas como sustituto del razonamiento por
shapes.

## Vistas, copias y mutabilidad

Cuando una operación pueda compartir memoria o crear una copia,
explicarlo explícitamente.

Distinguir:

-   asignación de referencias;
-   vista;
-   copia;
-   copia superficial de elementos `object`;
-   ownership del buffer.

Usar cuando proceda:

``` python
a.base
np.shares_memory(a, b)
np.may_share_memory(a, b)
```

## Tipos y precisión

Explicar los `dtype` como representaciones de tamaño finito.

Incluir cuando corresponda:

-   rango;
-   precisión;
-   overflow y underflow;
-   casting;
-   promoción;
-   NaN e infinito;
-   error absoluto y relativo;
-   tolerancias;
-   cancelación;
-   acumulación.

No comparar floats mediante igualdad exacta cuando la naturaleza del
problema requiera tolerancia.

## Rendimiento

No presentar "vectorizar" como regla absoluta.

Comparar cuando proceda:

-   bucles Python;
-   ufuncs;
-   broadcasting;
-   temporales;
-   operaciones `out=`;
-   in-place;
-   procesamiento por bloques;
-   Numba/Cython/extensiones.

Separar tiempo de ejecución, consumo de memoria y claridad del código.

## Seguridad

Advertir explícitamente sobre:

-   `allow_pickle=True` con archivos no confiables;
-   `as_strided` y layouts inválidos o memoria solapada;
-   buffers externos y ownership;
-   mutación concurrente de arrays compartidos;
-   conversiones que pierden información;
-   overflow silencioso cuando corresponda.

## Laboratorios

Los laboratorios deben pedir al estudiante observar y justificar
resultados, no solo copiar código.

Cuando sea posible deben incluir:

1.  predicción;
2.  ejecución;
3.  inspección;
4.  explicación;
5.  modificación;
6.  comprobación mediante una prueba o invariante.

## Proyecto final

El proyecto final integra el PATH mediante una biblioteca y una CLI para
análisis de sensores. Debe demostrar:

-   diseño consciente de shapes y `dtype`;
-   reproducibilidad;
-   persistencia;
-   tratamiento de datos inválidos;
-   estadística;
-   procesamiento de señales;
-   álgebra lineal;
-   remuestreo;
-   procesamiento por bloques;
-   pruebas;
-   medición y optimización;
-   documentación de decisiones y límites numéricos.

El resultado debe parecer software numérico mantenible, no una colección
de celdas de notebook.
