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
- parsing conceptual del patrón y representación mediante AST;
- compilación conceptual de regex;
- simplificación y optimización conceptual del patrón;
- autómatas finitos y relación con lenguajes regulares;
- construcción de Thompson a nivel pedagógico;
- NFA/DFA a nivel pedagógico;
- subset construction y minimización de DFA a nivel conceptual;
- Pike VM, lazy DFA y motores híbridos como modelos de implementación;
- backtracking;
- complejidad;
- catastrophic backtracking;
- ReDoS;
- optimización;
- portabilidad;
- testing y depuración;
- diseño de patrones mantenibles;
- análisis léxico y relación regex → token → lexer → parser;
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
- elección de motores con garantías distintas de complejidad;
- distinguir comportamiento lineal, polinómico y exponencial cuando sea relevante;
- distinguir entrada controlada por la aplicación de entrada controlada por un atacante.

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


## Progresión y alcance de las ampliaciones

Se conservan los bloques 0 a 48 y todos los identificadores originales.
Las nuevas lecciones se añaden al final del bloque correspondiente. Cuando
una ampliación introductoria sea un prerrequisito, las lecciones anteriores
incluyen una explicación mínima y remiten a ella; no se exige al estudiante
conocimiento de bloques posteriores para entender el concepto inicial.

Antes de 4.12, introducir agrupación mínima siguiendo 0.26. Antes del bloque 5,
explicar decisiones y retroceso según 4.19. La agrupación detallada permanece
en el bloque 9 y el backtracking sistemático en el 25.
La lección 7.10 es un avance guiado; su desarrollo pertenece a 13 a 15.
Las lecciones 15.27 y 15.28 presentan una comparación conceptual y se retoman
tras el bloque 18. La primera explicación no presupone dominar atomicidad.
El bloque 43 es un proyecto integrador intermedio; el cierre experto es el 48.

## Contrato observable de búsqueda

Distinguir búsqueda, coincidencia desde una posición, validación completa,
extracción, iteración, división y sustitución. Cada laboratorio declara la
operación, el patrón, el dialecto, el motor y versión cuando haya ejecución,
los flags, el locale relevante, la entrada y los resultados esperados.
La primera aparición de una operación incluye la explicación mínima de su
contrato; el recorrido sistemático se desarrolla en el bloque 23.

Registrar coincidencias mediante intervalos [inicio, fin), con inicio inclusivo
y fin exclusivo, indicando si las posiciones se miden en bytes, code units o
code points. Esta es la convención del informe, no una convención universal
de las herramientas. Distinguir captura vacía, grupo no participante y ausencia
de coincidencia. Declarar la política de solapamiento y de avance después de
una coincidencia vacía, incluido el fin de entrada.

## Precisión sobre dialectos y motores

En clases POSIX enseñar [[:alpha:]] como expresión completa; [:alpha:] es la
clase interior. Explicar efectos de locale y colación antes de generalizar
rangos como [a-z]. Separar BRE/ERE normativos de extensiones locales.
La semántica POSIX incluye selección de subcoincidencias; no se reduce a elegir
la coincidencia completa más larga. Selección de resultados y estrategia de
ejecución son ejes distintos: no identificar POSIX con DFA ni leftmost-first
exclusivamente con backtracking.

En 31.10, longitud variable significa soporte acotado y condicionado por la
versión y la función usada. PCRE2 10.43 y posteriores incorporan determinadas
longitudes variables en pcre2_match; no inferir soporte de repeticiones sin
cota. Comparar sus restricciones con pcre2_dfa_match y registrar la versión.
Las aserciones tradicionales pueden retroceder internamente mientras se
evalúan y seguir siendo atómicas respecto a un fallo posterior. Las extensiones
no atómicas requieren identificación expresa del motor y su sintaxis.

En Unicode distinguir codificación UTF, propiedades, equivalencia canónica,
normalización, grafemas y segmentación de palabras. No asumir normalización
automática ni equivalencia entre las fronteras de \b y UAX #29. Una transformación
de la entrada requiere documentar cómo se relacionan sus posiciones con las
originales. Diferenciar Script de Script_Extensions y UTF de UCP en PCRE2.

## Rendimiento: objetivos diferentes por bloque

- Bloque 26: medir, comparar y mejorar patrones conservando sus resultados.
- Bloque 27: reconocer exposición a ReDoS y aplicar mitigaciones verificables.
- Bloque 46: razonar sobre parámetros, complejidad y límites de las garantías.

Separar compilación, búsqueda individual, iteración y producción de salida.
Declarar tamaño del patrón y de la entrada, corpus, unidades, flags y versión.
Una garantía lineal respecto a la entrada no elimina la dependencia del patrón.
No equiparar límites de pasos, profundidad o memoria con timeout de reloj.
La atomicidad y la posesividad no son refactorizaciones automáticamente
correctas: comprobar coincidencias y capturas, además del tiempo.

## Proyecto Analyzer compatible con el alcance agnóstico

La entrega obligatoria de 43 y 48 es un dossier reutilizable: especificación,
fichas de análisis, árboles dibujados o descritos manualmente, corpus con
resultados esperados y observados e informes de portabilidad y rendimiento.
Los verbos construir, recibir, ejecutar, mostrar y visualizar se concretan en
este flujo manual y en herramientas existentes. No exigen crear software.
La implementación ejecutable queda como ampliación opcional en otro PATH.

El analizador declara un subconjunto de sintaxis y rechaza o marca como no
soportado lo que no pueda analizar. No promete interpretar todos los dialectos.
Las alertas ReDoS son heurísticas justificadas; ausencia de alerta no demuestra
seguridad. Una propuesta de refactorización conserva la operación, los matches
y las capturas relevantes o documenta expresamente el cambio.

El corpus mínimo incluye éxito, fallo, vacío, coincidencia vacía, fin de entrada,
Unicode, saltos de línea y crecimiento controlado de entradas. Cada informe
identifica limitaciones y enlaza sus conclusiones con casos reproducibles.

## Validación del perfil y referencias de archivos

La validación sintáctica de YAML, la auditoría pedagógica, la ejecución de labs
y las comprobaciones de course-generator son verificaciones diferentes.
validation.enabled permanece desactivado porque no hay un comando universal
para todos los dialectos y operaciones; no implica desactivar la auditoría.
Las políticas adicionales orientan el contenido y no prueban que el generador
implemente automáticamente cada campo. Verificar su interpretación en el código.
Resolver files.pedagogy desde la ubicación real del perfil antes de generar;
se conserva la ruta recibida al no disponer aquí de la estructura del repositorio.
