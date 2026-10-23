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

Antes de generar el curso completo, seleccionar una versión estable de
NumPy 2.x compatible con la versión elegida de Python y fijar ambas como
objetivo de toda la generación. Registrar versiones exactas, dependencias
y configuración BLAS. Consultar documentación correspondiente a ese
objetivo; las URLs /stable/ pueden cambiar y no fijan una versión.

Actualizar el objetivo debe ser una decisión explícita acompañada de
validación de ejemplos, pruebas y compatibilidad de extensiones.

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


## Criterios adicionales de profundidad experta

En cada lección pertinente se exige distinguir precondiciones, postcondiciones y efectos secundarios; demostrar con ejemplos verificables cuándo una operación devuelve una vista, una copia o un resultado que puede compartir memoria; y razonar sobre shape, dtype, ejes, casting, aliasing y mutabilidad.

La explicación del coste debe distinguir complejidad temporal asintótica, memoria auxiliar, tráfico de memoria y comportamiento medido. Nunca equiparar vectorización con mejora garantizada. Incluir benchmarks repetidos, control del entorno, calentamiento cuando proceda y análisis de variabilidad.

En cálculo numérico separar precisión de representación, condicionamiento del problema, estabilidad del algoritmo y error observado. Introducir ULP, epsilon de máquina, acumulación, tolerancias escaladas y error residual cuando corresponda.

Para funciones reutilizables documentar contratos de entrada y salida, gestión de excepciones, compatibilidad entre versiones, pruebas de casos límite, invariantes, propiedades y pruebas diferenciales. Los laboratorios deben incluir predicción, ejecución, inspección, diagnóstico y prueba automatizada.

En extensiones compiladas explicar ownership, referencias, ABI, manejo de errores, compilación, empaquetado y validación de compatibilidad con NumPy 2.x. No presentar detalles internos como garantías públicas sin respaldo de documentación oficial.

## Compatibilidad y verificación de versiones

Comprobar disponibilidad y firma de cada API en la versión objetivo antes de generar código. En particular, tratar NEP 50, StringDType, funciones recientes de numpy.linalg, Array API, C-API y cambios de compatibilidad binaria como contenidos sujetos a versión. No asumir que una API de SciPy forma parte de NumPy.

## Requisitos del proyecto final ampliado

El proyecto de sensores debe establecer objetivos medibles de precisión, memoria y rendimiento, ofrecer CLI reproducible, pruebas automatizadas, validación de datos, política de persistencia segura, trazabilidad de dependencias, benchmarks y documentación de limitaciones.

## Progresión y delimitación de contenidos

Mantener 31 bloques y 405 lecciones. En cada bloque de contenido situar
los laboratorios integradores después de sus prerrequisitos. El bloque
13 contiene dos laboratorios complementarios al cierre. El bloque 30
desarrolla un proyecto por etapas: los presupuestos de precisión, memoria
y rendimiento se acuerdan al principio y se auditan antes de entregar.

Introducir strides y contigüidad de manera elemental en el bloque 6,
antes de explicar copias en reshape. Reservar el cálculo de direcciones,
los flags y el análisis profundo del layout para el bloque 26.

Distinguir introducción y aplicación avanzada en las lecciones sobre
reduceat, SeedSequence, normalización FFT, StringDType y tipado de formas.
No repetir una misma explicación como si fuera un contenido nuevo.

## Casos técnicos obligatorios

En ufuncs con where, explicar que, si out no se proporciona, las
posiciones con condición falsa pueden quedar sin inicializar. Contrastar
con un out inicializado y con np.where, que selecciona entre expresiones
ya evaluadas y no evita por sí mismo evaluar una operación inválida.

En concurrencia distinguir liberación del GIL y ejecución con Python
free-threaded. Verificar soporte en las versiones objetivo. Explicar
carreras de datos, sincronización, tiempo de vida y riesgos de object;
la ausencia del GIL no garantiza seguridad al compartir arrays.

En protocolos utilizar los nombres exactos __array__,
__array_interface__, __array_ufunc__, __array_function__ y
__array_namespace__. Explicar el contrato vigente de dtype y copy de
__array__ y verificar qué objetos implementan cada protocolo.

## Integración con el generador

El YAML expresa la intención pedagógica de este PATH. La sintaxis válida
no garantiza que el cargador interprete todas las claves. Antes de
generar, contrastar el esquema y la resolución de files.pedagogy con
la implementación instalada de course-generator. Las instrucciones
esenciales también se expresan en este documento para evitar que
dependan exclusivamente de claves opcionales del perfil.
