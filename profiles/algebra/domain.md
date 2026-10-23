# Domain — Álgebra Booleana 0 → Experto

## Propósito

Este dominio define un curso completo y progresivo de Álgebra Booleana,
desde cero hasta nivel experto. El objetivo no es memorizar operadores y
tablas, sino dominar el razonamiento algebraico, la representación de
funciones, la demostración de equivalencias, la minimización y las
técnicas simbólicas y algorítmicas usadas en informática y lógica
digital.

## Alcance principal

El curso debe cubrir en profundidad:

- valores y variables booleanas;
- NOT, AND, OR y operadores derivados;
- tablas de verdad y evaluación de expresiones;
- precedencia y notación;
- todas las leyes fundamentales y derivadas;
- De Morgan, absorción, consenso y dualidad;
- equivalencia y demostración;
- funciones booleanas;
- literales, términos y cláusulas;
- minterms y maxterms;
- SOP, POS, DNF y CNF;
- simplificación algebraica;
- mapas de Karnaugh;
- implicantes primos y esenciales;
- don’t-care conditions;
- Quine–McCluskey y método de Petrick;
- definición axiomática de álgebra booleana;
- orden parcial y retículos;
- relación con teoría de conjuntos;
- homomorfismos e isomorfismos a nivel introductorio;
- completitud funcional;
- NAND-only y NOR-only;
- expansión y descomposición de Shannon;
- cofactors y diferencia booleana introductoria;
- árboles de decisión, BDD, OBDD y ROBDD;
- satisfacibilidad, CNF-SAT, 2-SAT y 3-SAT;
- fundamentos de DPLL y CDCL;
- Espresso y minimización heurística;
- comparación entre minimización exacta y heurística;
- aplicación a puertas y circuitos lógicos;
- aplicación a programación, bitwise, máscaras y flags;
- lógica ternaria de SQL;
- selección del método adecuado según tamaño y objetivo.

## Frontera del dominio

La lógica digital se usa como aplicación del Álgebra Booleana. Se deben
explicar puertas, conversión expresión↔circuito, circuitos
combinacionales y los fundamentos de circuitos secuenciales.

No convertir el curso en un curso completo de Digital Logic / Digital
Design. Temas como FSM en profundidad, clock domains, timing analysis,
setup/hold, metastabilidad, hazards avanzados, HDL, FPGA y síntesis
física pertenecen a un dominio posterior.

## Progresión pedagógica

La progresión obligatoria es:

1.  intuición y valores de verdad;
2.  operadores y tablas;
3.  expresiones y precedencia;
4.  leyes;
5.  equivalencia y simplificación;
6.  funciones y formas canónicas;
7.  minimización manual;
8.  estructura matemática;
9.  representación y algoritmos avanzados;
10. aplicaciones;
11. integración experta.

No introducir una técnica avanzada antes de establecer sus
prerrequisitos.

## Profundidad requerida

Cada concepto importante debe responder, cuando aplique, a:

- ¿Qué es?
- ¿Por qué existe?
- ¿Cómo se representa?
- ¿Cómo se calcula?
- ¿Cómo se demuestra?
- ¿Qué propiedades cumple?
- ¿Con qué conceptos se relaciona?
- ¿Cuándo se utiliza?
- ¿Cuándo no conviene utilizarlo?
- ¿Cuáles son los errores frecuentes?
- ¿Cómo se verifica el resultado?

Las simplificaciones y demostraciones deben mostrar pasos intermedios y
nombrar la ley aplicada.

Ejemplo:

    A ∨ (A ∧ B)
    = (A ∧ 1) ∨ (A ∧ B)    [identidad]
    = A ∧ (1 ∨ B)          [distributiva]
    = A ∧ 1                [dominación]
    = A                    [identidad]

Esta derivación prueba la absorción utilizando otras leyes ya establecidas.
Declarar los axiomas elegidos y evitar usar como paso la identidad que se
pretende demostrar.

## Cálculo y práctica

El estudiante debe aprender a calcular, no solo reconocer:

- 2^n filas de una tabla;
- 2^(2^n) funciones booleanas de n variables;
- tablas de verdad completas;
- minterms y maxterms;
- índices binarios y decimales;
- SOP/POS;
- CNF/DNF;
- agrupaciones de Karnaugh;
- prime implicants;
- coberturas;
- Quine–McCluskey;
- Petrick;
- cofactors;
- expansión de Shannon;
- BDD/ROBDD;
- asignaciones SAT;
- máscaras de bits.

## Demostraciones

El curso debe enseñar y practicar:

- demostración mediante tabla de verdad;
- demostración algebraica;
- equivalencias sucesivas;
- dualidad;
- contraejemplos;
- comprobación computacional cuando resulte útil.

Nunca presentar una identidad no trivial sin explicar cómo puede
comprobarse o derivarse.

## Notación

Usar preferentemente:

- ¬A para NOT;
- A ∧ B para AND;
- A ∨ B para OR;
- A ⊕ B para XOR;
- A → B para implicación;
- A ↔ B para bicondicional/equivalencia.

Cuando sea útil, mostrar también las notaciones usadas en lógica digital
y programación, explicando que no siempre son intercambiables.

## Programación

Las aplicaciones en lenguajes deben reforzar el concepto matemático, no
sustituirlo.

Distinguir rigurosamente:

- lógica booleana;
- truthiness/falsy cuando el lenguaje lo permita;
- short-circuit;
- operadores bitwise;
- representación binaria;
- máscaras y flags.

Los lenguajes de aplicación son Python, C/C++, Rust, Go, Java y
JavaScript/TypeScript.

## SQL

SQL debe tratarse separadamente porque NULL introduce UNKNOWN. Explicar
lógica ternaria y por qué no puede trasladarse mecánicamente la lógica
booleana clásica a expresiones que contienen NULL.

## Laboratorios

Los laboratorios deben progresar desde papel y lápiz hasta
automatización:

- construir tablas;
- comprobar leyes;
- simplificar expresiones;
- generar minterms/maxterms;
- resolver Karnaugh;
- implementar Quine–McCluskey en pequeño;
- construir BDD sencillos;
- codificar un evaluador booleano;
- comparar expresiones exhaustivamente;
- implementar máscaras;
- modelar un problema como SAT;
- transformar una función en circuito.

## Errores que el curso debe atacar explícitamente

- confundir OR inclusivo con XOR;
- confundir equivalencia con igualdad textual;
- aplicar reglas del álgebra aritmética sin justificación;
- olvidar precedencia;
- aplicar incorrectamente De Morgan;
- confundir minterm con maxterm;
- inventar diferencias entre SOP/DNF o POS/CNF bajo iguales definiciones;
- confundir formas generales con formas canónicas;
- agrupar incorrectamente mapas de Karnaugh;
- ignorar wrap-around;
- seleccionar implicantes no mínimos;
- asumir que una simplificación es necesariamente mínima;
- confundir boolean AND con bitwise AND;
- confundir NOT lógico con complemento bitwise;
- ignorar UNKNOWN en SQL;
- asumir que un BDD pequeño existe para cualquier orden de variables.

## Resultado esperado

Al terminar, el estudiante debe poder tomar un requisito lógico y
recorrer de forma justificada:

    requisito
       ↓
    variables
       ↓
    expresión / tabla
       ↓
    forma canónica
       ↓
    simplificación
       ↓
    minimización
       ↓
    representación avanzada
       ↓
    verificación
       ↓
    circuito o implementación software

El nivel experto exige además saber elegir entre álgebra manual, tablas,
Karnaugh, Quine–McCluskey, Espresso, BDD y SAT según el problema.


## Contrato de estructura y conservación

Conservar los 15 bloques y los 92 temas principales numerados de 0 a 91.
Cada identificador x.y representa una sublección en una línea independiente.
No eliminar objetivos originales ni renumerar sus identificadores. Las nuevas
sublecciones amplían cada tema con numeración consecutiva.

Los epígrafes iniciales breves necesitan desarrollo: definición, ejemplo
resuelto, ejercicio y comprobación cuando corresponda. Enlazar sublecciones
relacionadas sin repetir literalmente su explicación.

## Precisiones matemáticas obligatorias

- Para n entradas hay 2^n asignaciones y 2^(2^n) funciones totales distintas.
  Justificar el conteo; para n=0 hay una asignación vacía y dos funciones.
- Presentar {0,1} como álgebra booleana de dos elementos; no identificarla con
  toda álgebra booleana. Usar conjuntos potencia para modelos con más elementos.
- Separar el bicondicional como conectiva de la equivalencia como relación
  semántica. Distinguir implicación material de consecuencia semántica.
- Declarar precedencia, orden de variables y convención de índices. No imponer
  la precedencia matemática como si fuera universal en todos los lenguajes.
- SOP corresponde a DNF y POS a CNF cuando se utilizan las mismas definiciones.
  Distinguir forma general de completa/canónica y definir la palabra estándar.
- La disyunción vacía vale 0 y la conjunción vacía vale 1. En CNF, una cláusula
  vacía produce insatisfacibilidad; una conjunción sin cláusulas vale 1.
- Distinguir grupo maximal, cubierta irredundante, mínimo por inclusión y
  óptimo global respecto a un coste fijado. No inferir optimalidad de una
  mera simplificación, de grupos grandes aislados ni del resultado heurístico.
- En minimización parcial, ON, OFF y DC son disjuntos y cubren el dominio.
  Cubrir ON sin intersectar OFF; DC puede cubrirse o no. Comparar sobre ON/OFF.
- Un cofactor negativo sustituye x=0; no complementa el cofactor positivo.
- La canonicidad de ROBDD exige orden fijo; comparar identificadores de raíz
  solo dentro de un mismo gestor con tabla única coherente.
- Tseitin introduce auxiliares: distinguir equivalencia en las variables
  originales, proyección existencial y equisatisfacibilidad. Afirmar la raíz.
- En un miter, SAT ofrece un contraejemplo; UNSAT establece equivalencia
  dentro de las restricciones codificadas. Un timeout no establece UNSAT.

## Desarrollo matemático y algorítmico avanzado

Integrar, con ejemplos calculados y ejercicios corregidos:

1. Soporte y variables esenciales; funciones constantes y parcialmente
   especificadas; conjuntos ON/OFF/DC.
2. Orden inducido, átomos y representación de álgebras finitas mediante
   conjuntos de átomos. Presentar ideales y núcleo solo tras homomorfismos.
3. Anillos booleanos con suma XOR y producto AND. Introducir GF(2), monomios
   multilineales, ANF, unicidad, grado y funciones afines. Calcular una ANF
   desde tabla con transformada de Möbius y verificarla exhaustivamente.
4. Completitud funcional constructiva y criterio de Post. Definir preservación
   de 0/1, monotonía, autodualidad y afinidad; explicar cierre por composición
   y las convenciones relativas a constantes. No exigir teoría de clones.
5. Abstracción existencial/universal desde cofactors; diferencia booleana y
   soporte. Estos cuantificadores actúan sobre entradas booleanas; no abrir
   un curso general de lógica de primer orden ni de QBF.
6. ROBDD operativo: Mk, tabla única, Apply, memoización, restricción,
   cuantificación y conteo de modelos con variables omitidas. Comparar órdenes
   usando exactamente la misma función y medir el tamaño obtenido.
7. SAT práctico: restricciones de cardinalidad pequeñas, Tseitin, DIMACS,
   grafo de implicaciones de 2-SAT, DPLL trazado y CDCL guiado con resolución,
   First UIP y backjumping. Distinguir verificación de modelos y certificados
   de insatisfacibilidad. Herramientas externas requieren nombre y versión.
8. Minimización exacta y heurística: declarar coste y care set; medir calidad,
   tiempo y memoria; no afirmar garantías de óptimo para Espresso.
9. Introducción a AIG y compartición de subexpresiones como puente a síntesis
   multinivel, sin ampliar el alcance a diseño físico.

El curso mantiene su especialización en álgebra booleana y métodos de funciones
booleanas; no pretende agotar teoría de modelos, análisis de Fourier,
criptografía ni diseño de solvers industriales.

## Progresión y comprobación proporcionada al tamaño

Introducir la clasificación elemental de fórmulas en 5.11 y retomarla en 56
con modelos y SAT. Anticipar la noción de implicante al estudiar Karnaugh y
formalizarla en 35. El tema de una sublección puede necesitar un anticipo
breve; enlazarlo y no asumir contenidos que todavía no se han explicado.

Las tablas completas son obligatorias en ejemplos pequeños donde aporten
evidencia. Para casos grandes usar SAT, BDD u otra justificación adecuada;
no construir tablas exponenciales por una regla mecánica.

Establecer checkpoints acumulativos al cerrar 22, 32, 40, 45, 55, 58 y 81.
Cada checkpoint incluye resolución manual, justificación y verificación;
se exige resolver un caso nuevo y explicar un error deliberado.

## Semántica de las aplicaciones

Las identidades algebraicas describen funciones puras. En programación,
comprobar además orden de evaluación, efectos, excepciones y tipo devuelto.
El cortocircuito no autoriza a conmutar expresiones con efectos secundarios.
Tratar cada lenguaje como aplicación breve y remitir a su path para sintaxis
y herramientas generales. Evitar siete implementaciones redundantes de todo
el curso; Python puede servir de lenguaje de referencia para los algoritmos.

Especificar ancho de palabra y signo para máscaras. Explicar precisión
arbitraria y complemento en Python, promociones en C/C++, operadores de Go,
evaluación completa de booleanos con &/| en Java y conversión bitwise de
Number a enteros de 32 bits en JavaScript. Separar Number y BigInt.

SQL requiere tablas con TRUE/FALSE/UNKNOWN. WHERE y HAVING seleccionan TRUE;
CHECK permite TRUE o UNKNOWN. Incluir NOT IN con NULL y NOT EXISTS. No afirmar
que dejan de cumplirse todas las leyes clásicas: mostrar con tablas cuáles
se conservan y cuáles fallan, como el tercero excluido con UNKNOWN.

Los circuitos secuenciales son una frontera introductoria. Separar función de
salida y próximo estado; no confundir equivalencia combinacional con ausencia
de hazards o equivalencia temporal.

## Proyecto final y criterios de aceptación

El proyecto tiene dos casos relacionados:

- Caso A: función pequeña, preferentemente 3–4 entradas. Obtener todas las
  representaciones originales exigidas, ANF, Karnaugh, Quine–McCluskey/Petrick,
  Shannon y ROBDD; verificar exhaustivamente y justificar cada coste.
- Caso B: instancia mayor parametrizable. Evitar tabla y formas canónicas
  completas cuando exploten. Usar SAT o BDD para verificar y explicar qué
  métodos dejan de ser razonables. Documentar restricciones y care set.

En el caso A, SOP/DNF y POS/CNF pueden compartir un mismo resultado con una
explicación de la correspondencia; no pedir artefactos duplicados sin propósito.
La obligación de validación exhaustiva corresponde al caso pequeño. Para el
caso grande entregar evidencia simbólica y no llamar prueba a un muestreo.

Entregar requisitos, entradas, expresiones/circuitos, código, resultados,
versiones de herramientas, orden de variables, criterio de coste y comandos
reproducibles. Una comparación experimental debe registrar límites y tamaños
de entrada; no deducir superioridad general de un único ejemplo.

Rúbrica: corrección matemática 40 %, justificación y elección del método 25 %,
reproducibilidad y verificación 25 %, claridad y explicación de límites 10 %.
Una equivalencia falsa, una codificación incorrecta o una validación ausente
debe corregirse aunque la puntuación agregada sea suficiente.

## Integración de los archivos

initial.txt es el inventario de temas y sublecciones; domain.md define las
reglas de contenido; bibliography.md relaciona fuentes y objetivos. Las claves
descriptivas de profile.yaml expresan requisitos y no garantizan que el
generador implemente validadores o herramientas para cada una.
La ruta files.pedagogy se conserva del perfil original; comprobar su resolución
en el repositorio real antes de generar. La validez sintáctica de YAML no
equivale a compatibilidad con el esquema o cargador de course-generator.
