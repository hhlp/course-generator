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

    A ∧ (A ∨ B)
    = (A ∧ A) ∨ (A ∧ B)    [distributiva]
    = A ∨ (A ∧ B)            [idempotencia]
    = A                      [absorción]

## Cálculo y práctica

El estudiante debe aprender a calcular, no solo reconocer:

- 2^n filas de una tabla;
- 2<sup>(2</sup>n) funciones booleanas de n variables;
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
- confundir SOP/POS con CNF/DNF sin matices;
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
