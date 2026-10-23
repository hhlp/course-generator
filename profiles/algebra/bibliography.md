# Bibliografía — Álgebra Booleana 0 → Experto

## Base matemática y lógica

1.  George Boole. *An Investigation of the Laws of Thought*.
    Obra histórica fundacional. Útil como referencia conceptual e
    histórica, no como texto introductorio principal.

2.  Kenneth H. Rosen. *Discrete Mathematics and Its Applications*.
    McGraw-Hill.
    Referencia general para lógica proposicional, equivalencias, métodos
    de demostración, conjuntos, relaciones y estructuras discretas.

3.  Susanna S. Epp. *Discrete Mathematics with Applications*. Cengage.
    Especialmente útil para razonamiento lógico, equivalencias y
    construcción gradual de demostraciones.

4.  Ralph P. Grimaldi. *Discrete and Combinatorial Mathematics: An
    Applied Introduction*. Pearson.
    Complemento para lógica, estructuras discretas y formalización
    matemática.

## Álgebra Booleana y lógica digital

5.  M. Morris Mano; Michael D. Ciletti. *Digital Design*. Pearson.
    Referencia principal para álgebra booleana aplicada, simplificación,
    mapas de Karnaugh, puertas y circuitos combinacionales/secuenciales.

6.  Thomas L. Floyd. *Digital Fundamentals*. Pearson.
    Texto pedagógico para operadores, tablas de verdad, simplificación,
    Karnaugh y fundamentos de lógica digital.

7.  Ronald J. Tocci; Neal S. Widmer; Gregory L. Moss. *Digital Systems:
    Principles and Applications*. Pearson.
    Complemento práctico para puertas, circuitos y aplicaciones
    digitales.

8.  Stephen Brown; Zvonko Vranesic. *Fundamentals of Digital Logic with
    VHDL Design*. McGraw-Hill.
    Útil para profundizar en funciones booleanas, minimización y
    conexión con diseño lógico. El contenido HDL queda fuera del núcleo
    de este PATH.

## Minimización y síntesis lógica

9.  Edward J. McCluskey Jr. “Minimization of Boolean Functions.” *Bell
    System Technical Journal* (1956).
    DOI: <https://doi.org/10.1002/j.1538-7305.1956.tb03835.x>.
    Referencia clásica asociada al método tabular de minimización.

10. Willard V. Quine. “The Problem of Simplifying Truth Functions.”
    *The American Mathematical Monthly*, 59(8) (1952).
    DOI: <https://doi.org/10.1080/00029890.1952.11988183>.
    Base histórica y teórica del método Quine–McCluskey.

11. Robert K. Brayton et al. *Logic Minimization Algorithms for VLSI
    Synthesis*. Springer/Kluwer.
    Referencia avanzada para minimización lógica y fundamentos
    relacionados con Espresso.

12. Giovanni De Micheli. *Synthesis and Optimization of Digital
    Circuits*. McGraw-Hill.
    Referencia avanzada sobre representación, optimización y síntesis de
    funciones lógicas.

## BDD y representación simbólica

13. Randal E. Bryant. “Graph-Based Algorithms for Boolean Function
    Manipulation.” *IEEE Transactions on Computers*, 35(8), 677–691
    (1986). DOI: <https://doi.org/10.1109/TC.1986.1676819>.
    [Texto del autor](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).
    Referencia fundamental para Reduced Ordered Binary Decision Diagrams
    (ROBDD).

14. Henrik Reif Andersen. *An Introduction to Binary Decision
    Diagrams*.
    Introducción técnica a BDD, orden de variables, reducción y
    operaciones.

## SAT

15. Armin Biere; Marijn Heule; Hans van Maaren; Toby Walsh (eds.).
    *Handbook of Satisfiability*. IOS Press.
    Referencia experta sobre SAT, algoritmos, representaciones y
    aplicaciones.

16. Martin Davis; George Logemann; Donald Loveland. “A Machine Program
    for Theorem-Proving.” *Communications of the ACM*, 5(7), 394–397
    (1962). DOI: <https://doi.org/10.1145/368273.368557>.
    Referencia clásica del algoritmo DPLL.

17. João P. Marques-Silva; Karem A. Sakallah. “GRASP: A Search Algorithm
    for Propositional Satisfiability.” *IEEE Transactions on Computers*,
    48(5), 506–521 (1999).
    DOI: <https://doi.org/10.1109/12.769433>.
    [Texto](https://eprints.soton.ac.uk/262032/1/jpms-tcomp99.pdf).
    Referencias históricas importantes para la evolución hacia CDCL.

## Complementaria para informática

18. Thomas H. Cormen; Charles E. Leiserson; Ronald L. Rivest; Clifford
    Stein. *Introduction to Algorithms*. MIT Press.
    Complementaria para razonamiento algorítmico, complejidad y análisis
    de técnicas usadas en niveles avanzados.

19. Donald E. Knuth. *The Art of Computer Programming, Volume 4A:
    Combinatorial Algorithms, Part 1*. Addison-Wesley.
    Referencia avanzada para estructuras y algoritmos combinatorios
    relacionados.

## Uso recomendado

La bibliografía debe utilizarse por capas:

- **Inicio:** Epp/Rosen + Floyd.
- **Álgebra y diseño lógico:** Mano & Ciletti como referencia central.
- **Minimización:** Mano → Quine/McCluskey → Brayton/De Micheli.
- **BDD:** Bryant + Andersen.
- **SAT:** introducción didáctica del curso → DPLL → *Handbook of
  Satisfiability*.
- **Nivel experto:** consultar fuentes originales y textos avanzados
  para contrastar terminología, algoritmos y límites.

La bibliografía de lógica digital es de apoyo: el objetivo central sigue
siendo Álgebra Booleana. HDL, FPGA y diseño digital físico no forman
parte del alcance principal.


## Ampliación matemática y práctica de la revisión

20. Ryan O’Donnell. *Analysis of Boolean Functions*. Cambridge University
    Press (2014).
    [Texto del autor](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf).
    Seleccionar la representación polinómica sobre GF(2), grado y funciones
    afines como complemento de ANF. El análisis de Fourier avanzado no es
    requisito de este path; distinguir las bases sobre GF(2) y sobre R.

21. Vaughan Pratt. *Algebras for Logic*, material docente, Stanford.
    [Texto](https://boole.stanford.edu/cs353/handouts/book3.pdf).
    Apoyo para operaciones booleanas, composición y criterio de Post.
    Explicar explícitamente la convención sobre constantes y aridades.

22. Armin Biere. *Tutorial on SAT*. CP/ICLP/SAT, Melbourne (2017).
    [Diapositivas](https://fmv.jku.at/biere/talks/Biere-CP17ICLP17SAT17-tutorial.pdf).
    Fuente práctica para equivalencia, codificación Tseitin, restricciones
    y conexión entre circuitos y SAT. Derivar las cláusulas con notación
    propia legible y verificar las polaridades de cada puerta.

## Mapa de lectura por objetivos

| Temas | Objetivo | Fuentes prioritarias |
| --- | --- | --- |
| 0–22 | Razonamiento, conectivas y demostración | Epp, Rosen, Floyd |
| 23–32 | Funciones, índices y formas normales | Mano/Ciletti, Rosen |
| 33–40 | Minimización y coberturas exactas | Mano/Ciletti, Quine, McCluskey |
| 41–45 | Estructura matemática y ANF | Rosen, Grimaldi, O’Donnell |
| 46–48 | Completitud y bases | Pratt, Mano/Ciletti |
| 49–55 | Shannon y algoritmos ROBDD | Bryant, Andersen |
| 56–58 | SAT, codificación y algoritmos | Biere, Davis et al., GRASP, Handbook |
| 59–62 | Heurísticas y escalabilidad | Brayton et al., De Micheli |
| 63–70 | Aplicación a circuitos | Mano/Ciletti, Floyd, Tocci et al. |
| 71–81 | Semántica de lenguajes y SQL | Documentación oficial indicada abajo |
| 82–91 | Verificación e integración | Bryant, Biere, De Micheli, Handbook |

## Documentación primaria para aplicaciones

Consultar la documentación de la versión usada en cada laboratorio. Registrar
esa versión en el resultado; no fijar ejemplos a una supuesta versión más
reciente. Los enlaces siguientes son entradas de consulta, no una afirmación
de compatibilidad de herramientas instaladas.

- Python: [expresiones](https://docs.python.org/3/reference/expressions.html)
  y [tipos incorporados](https://docs.python.org/3/library/stdtypes.html).
- C/C++: especificar edición del estándar y compilador; comprobar promociones,
  tipos sin signo y desplazamientos en el texto normativo correspondiente.
  [WG14](https://www.open-std.org/jtc1/sc22/wg14/) y
  [WG21](https://www.open-std.org/jtc1/sc22/wg21/).
- Rust: [operadores](https://doc.rust-lang.org/reference/expressions/operator-expr.html).
- Go: [especificación](https://go.dev/ref/spec).
- Java: [especificaciones del lenguaje](https://docs.oracle.com/javase/specs/).
- JavaScript: [ECMAScript](https://tc39.es/ecma262/).
- TypeScript: [Handbook](https://www.typescriptlang.org/docs/handbook/intro.html).
  El tipado estático no sustituye la semántica de ejecución de JavaScript.
- PostgreSQL: [operadores lógicos](https://www.postgresql.org/docs/current/functions-logical.html),
  [comparaciones](https://www.postgresql.org/docs/current/functions-comparison.html)
  y [restricciones](https://www.postgresql.org/docs/current/ddl-constraints.html).
  Usar su tratamiento de NULL, predicados y CHECK como aplicación concreta.

## Criterios de uso de fuentes

- Los libros generales apoyan la exposición; los artículos justifican
  algoritmos y límites concretos. No exigir leer un artículo de investigación
  antes de disponer de sus prerrequisitos.
- La selección de edición debe quedar registrada al generar el curso. Las
  entradas que no indican edición no afirman cuál es la edición más reciente.
- Las referencias digitales sirven a los objetivos algebraicos del path.
  HDL y diseño físico siguen siendo contenidos de otro dominio.
