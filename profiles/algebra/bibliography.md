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

9.  Edward J. McCluskey. *Minimization of Boolean Functions*. Bell
    System Technical Journal.
    Referencia clásica asociada al método tabular de minimización.

10. Willard V. Quine. Trabajos clásicos sobre simplificación de
    funciones de verdad.
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
    Manipulation.” *IEEE Transactions on Computers*.
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
    for Theorem-Proving.”
    Referencia clásica del algoritmo DPLL.

17. João Marques-Silva; Karem A. Sakallah. Trabajos sobre GRASP y
    aprendizaje basado en conflictos.
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
