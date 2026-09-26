# Domain — Algorithmic Complexity & Big O

## Propósito

Este dominio define un curso independiente del lenguaje para aprender a
analizar la eficiencia de algoritmos y estructuras de datos desde nivel
inicial hasta avanzado. El objetivo no es memorizar tablas de
complejidad, sino aprender a construir modelos de coste, derivar
funciones T(n), simplificarlas asintóticamente y justificar las
conclusiones.

## Alcance principal

El curso cubre:

- análisis temporal y espacial;
- funciones de crecimiento;
- notaciones O, Ω, Θ, o y ω;
- best, average, worst y expected case;
- análisis amortizado;
- sumatorios, logaritmos y matemáticas necesarias;
- recurrencias, árboles de recursión y Master Theorem;
- búsqueda y ordenación;
- complejidad de estructuras de datos;
- árboles, hashing, heaps y Union-Find;
- grafos y complejidad en términos de V y E;
- técnicas de optimización algorítmica;
- análisis empírico y benchmarking;
- lower bounds;
- algoritmos aleatorizados;
- complejidad de memoria, caché, I/O y paralelismo como introducción
  avanzada;
- introducción rigurosa a P, NP, NP-hard y NP-complete;
- separación entre garantías algorítmicas e implementación concreta.

## Fuera de alcance

Este PATH no pretende documentar exhaustivamente la complejidad de las
APIs de un lenguaje concreto. Esas aplicaciones se separarán
posteriormente en PATH especializados:

- Python;
- C++;
- Rust;
- Go;
- JavaScript;
- TypeScript.

Los PATH específicos reutilizarán esta teoría y se concentrarán en
estructuras estándar, garantías documentadas, runtimes, implementaciones
y particularidades del lenguaje.

## Principios conceptuales

### Big O no es un cronómetro

O(g(n)) describe una cota asintótica. No expresa segundos, ciclos de CPU
ni una velocidad absoluta.

### Big O no es sinónimo de worst case

Best, average y worst describen conjuntos o distribuciones de entradas.
O, Ω y Θ describen relaciones asintóticas. El curso debe mantener
separadas ambas dimensiones.

### El modelo de coste debe declararse

Todo análisis depende de qué operaciones se consideran elementales y de
cómo se representa la entrada.

### La entrada puede tener más de una dimensión

No reducir artificialmente O(n + m), O(nm), O(V + E) u otras expresiones
multivariables a una sola n cuando las dimensiones son independientes.

### Average, expected y amortized no son equivalentes

El curso debe explicar y ejercitar sus diferencias explícitamente.

### Teoría y medición se complementan

Los benchmarks sirven para observar comportamiento real, constantes,
efectos de caché y puntos de cruce. No sustituyen una demostración
asintótica.

## Progresión

La progresión pedagógica es:

intuición → conteo de operaciones → funciones T(n) → simplificación
asintótica → definiciones formales → análisis de algoritmos clásicos →
recurrencias → análisis amortizado → estructuras de datos → grafos →
optimización → lower bounds → modelos avanzados → complejidad
computacional.

## Matemáticas requeridas

Se introducen dentro del propio curso los conocimientos necesarios:

- álgebra elemental;
- exponentes;
- logaritmos;
- sumatorios;
- series aritméticas y geométricas;
- factorial;
- combinatoria elemental;
- límites como intuición asintótica.

No se presupone cálculo avanzado.

## Laboratorios

Los laboratorios deben favorecer:

1.  contar operaciones;
2.  obtener T(n);
3.  simplificar T(n);
4.  justificar O/Ω/Θ;
5.  comparar algoritmos;
6.  construir recurrencias;
7.  resolver recurrencias;
8.  medir experimentalmente;
9.  explicar discrepancias entre teoría y medición;
10. documentar supuestos.

Se puede usar pseudocódigo como herramienta principal. Cuando sea útil
ejecutar experimentos, el lenguaje empleado es auxiliar y no debe
convertir la lección en una lección específica de ese lenguaje.

## Convenciones

- Usar `n`, `m`, `k` para tamaños genéricos independientes.
- Usar `V` y `E` para grafos.
- Diferenciar claramente upper bound, lower bound y tight bound.
- Especificar cuando una complejidad es worst-case, average-case,
  expected o amortized.
- Evitar afirmar garantías de implementaciones concretas sin
  documentación verificable.
- Explicar primero el razonamiento y después la notación final.
- Incluir contraejemplos cuando una simplificación habitual sea
  incorrecta.

## Resultado esperado

Al terminar, el estudiante debe poder recibir un algoritmo nuevo,
identificar sus parámetros de entrada, establecer un modelo de coste,
derivar y simplificar su complejidad temporal y espacial, distinguir
tipos de cotas y casos, analizar recurrencias comunes y razonar sobre la
elección de estructuras y algoritmos sin depender de un lenguaje
concreto.
