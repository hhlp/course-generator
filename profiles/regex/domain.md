# DOMAIN — REGEX EN PROFUNDIDAD

## Identidad del dominio

Este perfil enseña expresiones regulares desde cero hasta nivel experto.

La base conceptual debe ser independiente de un lenguaje de programación concreto y de una
herramienta concreta. El objetivo es comprender el modelo de las expresiones regulares antes de
aplicarlo posteriormente en herramientas como grep/ripgrep, sed, awk, lenguajes de programación,
editores, motores PCRE u otros consumidores de regex.

## Alcance principal

El curso debe cubrir progresivamente:

- concepto de expresión regular;
- texto de entrada, patrón y coincidencia;
- caracteres literales;
- metacaracteres;
- escapes;
- clases y conjuntos de caracteres;
- rangos;
- negación;
- anclas;
- cuantificadores;
- agrupación;
- alternancia;
- captura y no captura;
- referencias posteriores cuando el dialecto las permita;
- búsqueda, matching y extracción;
- codicia, pereza y posesividad;
- lookahead y lookbehind;
- grupos atómicos cuando proceda;
- condiciones y construcciones avanzadas cuando existan en motores concretos;
- Unicode y propiedades de caracteres;
- límites de palabra y nociones de frontera;
- multiline y dotall;
- flags/modificadores;
- diferencias entre familias y dialectos;
- POSIX BRE;
- POSIX ERE;
- PCRE/PCRE2;
- motores tipo Perl;
- motores backtracking;
- motores basados en autómatas;
- compilación conceptual de regex;
- autómatas finitos y relación con lenguajes regulares;
- NFA/DFA a nivel pedagógico;
- backtracking;
- complejidad;
- catastrophic backtracking;
- ReDoS;
- optimización;
- portabilidad;
- testing y depuración;
- diseño de patrones mantenibles;
- límites teóricos y prácticos de regex.

## Regla fundamental: base agnóstica

Las primeras capas del curso deben enseñar conceptos sin asumir Python, JavaScript, Perl, sed,
awk, grep, ripgrep u otra herramienta.

Cuando una construcción no sea universal, debe marcarse explícitamente como dependiente del
dialecto o motor.

Ejemplo:

- `.` como concepto de comodín puede explicarse de forma general;
- el comportamiento exacto frente a salto de línea depende del motor y sus modos;
- lookbehind no pertenece a todos los dialectos;
- BRE, ERE y PCRE no deben presentarse como equivalentes.

## Sintaxis frente a semántica

Siempre distinguir:

- cómo se escribe una construcción;
- qué significa;
- qué texto puede reconocer;
- qué comportamiento depende del motor.

No asumir que dos sintaxis visualmente similares tienen idéntica semántica en todos los dialectos.

## Familias y dialectos

El curso debe enseñar que “regex” no es un único lenguaje universal.

Como mínimo debe contextualizar:

- expresiones regulares formales;
- POSIX BRE;
- POSIX ERE;
- PCRE/PCRE2;
- Perl-compatible syntax;
- variantes implementadas por herramientas y lenguajes.

Las diferencias deben aparecer cuando sean pedagógicamente relevantes, no como una tabla masiva
sin contexto.

## Lookaround

Lookahead y lookbehind forman parte del recorrido avanzado.

Deben explicarse después de que el estudiante domine:

- secuencias;
- grupos;
- alternancia;
- cuantificadores;
- captura;
- semántica de matching.

Debe explicarse la naturaleza de aserción de ancho cero y las restricciones que algunos motores
imponen, especialmente en lookbehind.

## Teoría

La teoría debe servir para comprender el comportamiento práctico.

Distinguir:

- expresión regular en sentido formal;
- extensiones de los motores modernos que exceden la clase clásica de lenguajes regulares;
- backreferences y otras extensiones;
- NFA/DFA como modelos;
- motores de backtracking.

No convertir el curso en una asignatura puramente matemática, pero tampoco ocultar las diferencias
teóricas cuando explican comportamiento, rendimiento o límites.

## Rendimiento y seguridad

El curso debe cubrir:

- coste de alternativas;
- cuantificadores ambiguos;
- anidamiento;
- backtracking;
- catastrophic backtracking;
- ReDoS;
- estrategias para reducir ambigüedad;
- grupos atómicos y cuantificadores posesivos cuando estén disponibles;
- elección de motores con garantías distintas de complejidad.

No afirmar que todas las regex tienen el mismo coste ni que todos los motores usan backtracking.

## Unicode

Unicode debe tratarse explícitamente.

Distinguir:

- bytes;
- caracteres;
- code points;
- grapheme clusters;
- categorías y propiedades Unicode;
- clases ASCII tradicionales;
- comportamiento dependiente del motor.

No asumir que `\w`, `\d`, `.` o límites de palabra significan exactamente lo mismo en todos los
motores.

## Ejemplos

Los ejemplos iniciales deben poder razonarse sin depender de una herramienta concreta.

Cuando haga falta ejecutar patrones, se puede usar una herramienta o motor concreto como banco de
pruebas, pero debe identificarse claramente la implementación utilizada y separar:

1. concepto general;
2. sintaxis del dialecto;
3. resultado observado en la herramienta concreta.

## Relación con cursos posteriores

Regex es la base conceptual para cursos posteriores de:

- sed;
- awk;
- grep/ripgrep.

No debe absorber el contenido especializado de esas herramientas.

Por ejemplo:

- Regex enseña BRE/ERE y el concepto de matching;
- grep/ripgrep enseñará selección, opciones, recursive search, engines y workflow propio;
- sed enseñará addressing, sustitución, pattern space/hold space y edición de streams;
- awk enseñará records, fields, patterns/actions, lenguaje y procesamiento estructurado.

## Plataforma

Fedora Linux es la plataforma práctica preferida cuando haya que ejecutar herramientas o consultar
implementaciones disponibles.

Sin embargo, el conocimiento base de regex debe seguir siendo portable y no convertirse en un
curso exclusivo de Fedora.

## Criterios de calidad específicos

Una lección de Regex debe:

- identificar el dialecto cuando una característica no sea universal;
- distinguir patrón, texto, match y resultado;
- mostrar contraejemplos cuando ayuden a fijar semántica;
- evitar patrones artificialmente complejos sin necesidad;
- explicar por qué un patrón coincide o no coincide;
- incorporar rendimiento y seguridad cuando el tema lo justifique;
- preservar la progresión definida por el PATH;
- no adelantar herramientas especializadas que tendrán su propio curso.
