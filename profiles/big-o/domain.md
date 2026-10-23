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
- TypeScript;
- Java.

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

La progresión combina una primera aproximación intuitiva con revisiones
formales posteriores:

- Bloques 0–2: modelos elementales, crecimiento y conteo de operaciones.
- Bloques 3–6: notaciones formales, casos, espacio y matemáticas de apoyo.
- Bloques 7–8: búsqueda y ordenación, primero con razonamiento intuitivo.
- Bloques 9–10: recurrencias y formalización de los algoritmos anteriores.
- Bloques 11–13: amortización, estructuras, árboles y grafos.
- Bloques 14–16: optimización, medición y auditoría de errores.
- Bloques 17–18: modelos avanzados y complejidad computacional.
- Bloques 19–20: síntesis independiente del lenguaje y proyecto final.

Las lecciones nuevas se añaden al final de cada bloque para conservar los
identificadores originales. Un laboratorio original puede actuar como
checkpoint intermedio; el laboratorio añadido integra la ampliación.
Las herramientas matemáticas se presentan intuitivamente cuando aparecen
por primera vez y se formalizan en el bloque 6. Los ejemplos iniciales de
espacio recursivo se trazan manualmente antes del estudio de recurrencias.

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

## Precisión del modelo y de las garantías

Cada análisis declara tamaños, representación, operaciones elementales,
caso o distribución, fuente de aleatoriedad y recursos medidos. Separar
el número de elementos de la longitud en bits. En Word-RAM se explicitan
el tamaño de palabra y las operaciones consideradas constantes; las
operaciones sobre enteros arbitrarios o claves largas requieren otro
coste cuando exceden esas hipótesis.

El espacio se mide como máximo simultáneamente necesario. Diferenciar
entrada, espacio auxiliar, salida y volumen acumulado de asignaciones.
Una salida materializada impone su propio coste; un recorrido incremental
puede cambiar el espacio auxiliar sin eliminar el coste de producirla.

Para hashing, separar el coste de calcular y comparar claves, el efecto
de colisiones y la amortización del redimensionamiento. Para grafos,
declarar representación, región recorrida, pesos y estructura de prioridad.
Para Union-Find, asociar las cotas a las heurísticas realmente utilizadas.
Para ordenación, declarar el modelo de comparación o los parámetros de
rango, base y longitud de las claves.

## Demostración, probabilidad y corrección

Introducir precondiciones, postcondiciones, invariantes, terminación e
inducción. La optimización debe preservar la especificación del problema.
Los algoritmos greedy y las ventanas deslizantes necesitan condiciones de
corrección; no son transformaciones universales.

El análisis promedio declara una distribución de entradas. El análisis
esperado de un algoritmo aleatorizado declara la aleatoriedad interna y
puede hacerse para una entrada fija. Explicar también cotas esperadas
amortizadas y distinguir esperanza de garantías con alta probabilidad.
No exigir independencia para utilizar linealidad de la esperanza.

## Profundidad y evaluación

El núcleo requiere derivaciones completas, contraejemplos y problemas
nuevos. Caché, memoria externa, paralelismo y complejidad parametrizada
son introducciones avanzadas con ejercicios guiados, no especializaciones
exhaustivas. La etiqueta experto describe el objetivo de análisis del
núcleo; no implica dominar toda la teoría de complejidad computacional.

Los laboratorios expresamente nombrados en el temario son obligatorios.
Cada uno entrega supuestos, razonamiento, resultado y límites. Los
benchmarks añaden entradas, entorno, repeticiones y dispersión.

## Contrato del proyecto final

Algorithm Complexity Analyzer será un analizador educativo de un
subconjunto explícito de pseudocódigo, acompañado de análisis manuales.
No se plantea resolver automáticamente la complejidad de programas
arbitrarios. Debe admitir secuencias, bucles con límites reconocibles,
condicionales y llamadas con costes declarados; las recurrencias se
resuelven solo cuando encajan en plantillas justificadas.

El resultado distingue cota demostrada bajo supuestos, estimación y
no determinado. No inventar cotas para construcciones desconocidas.
Documentar gramática, anotaciones, casos admitidos, rechazo de entradas,
limitaciones y pruebas representativas. Evaluar por separado corrección
del analizador, calidad del razonamiento y reproducibilidad experimental.

## Fuentes académicas de apoyo

- MIT 6.006, recursos de modelos y análisis:
  https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Cornell, análisis amortizado de tablas hash:
  https://courses.cs.cornell.edu/cs3110/2021sp/textbook/eff/amortized_hash.html
- Jeffrey Erickson, Algorithms y materiales complementarios:
  https://jeffe.cs.illinois.edu/teaching/algorithms/
