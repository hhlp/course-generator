# SED EN PROFUNDIDAD — Bibliografía

## Política bibliográfica

Las referencias se organizan por función dentro del PATH.

Las lecciones deben citar secciones o capítulos exactos solamente cuando hayan sido verificados. No se deben inventar números de página, capítulos o apartados.

Cuando una característica dependa de una versión concreta de GNU sed, debe verificarse contra la documentación correspondiente a esa versión.

## Principal

### Daniel A. Goldman — *Definitive Guide to sed: Tutorial and Reference*

EHDP Press, 2013.

Referencia pedagógica principal del PATH.

Uso principal:

- introducción progresiva a sed;
- comando `s`;
- flags de sustitución;
- regex utilizadas por GNU sed;
- direcciones;
- comandos `d` y `D`;
- `a`, `i`, `c`;
- `p`, `P`, `l`;
- `r`, `R`, `w`, `W`;
- `n`, `N`;
- `h`, `H`, `g`, `G`, `x`;
- labels, branching y quit;
- comandos adicionales;
- consejos de utilización;
- ejemplos desde tareas breves hasta transformaciones complejas;
- referencia de comandos, flags, direcciones y regex.

El libro cubre GNU sed 4.2.1. Por ello es una excelente fuente pedagógica, pero las características modernas o cuyo comportamiento pueda haber cambiado deben contrastarse con la documentación GNU actual.

## Normativa

### The Open Group / IEEE — POSIX, `sed`

Referencia normativa para sed portable.

Uso principal:

- sintaxis POSIX;
- opciones requeridas;
- editing commands;
- direcciones;
- BRE/ERE cuando correspondan a sed;
- pattern space y hold space;
- comportamiento de entrada/salida;
- requisitos de portabilidad;
- environment variables y locale;
- exit status;
- límites mínimos exigidos por el estándar;
- rationale y diferencias históricas cuando aporten valor.

Debe utilizarse la edición vigente de POSIX cuando se comprueben requisitos normativos.

### The Open Group / IEEE — POSIX Base Definitions, Regular Expressions

Referencia normativa complementaria para BRE/ERE utilizadas por sed.

El PATH independiente de Regex conserva la responsabilidad de enseñar regex en profundidad. Esta referencia se usa aquí para resolver comportamiento normativo que afecte directamente a sed.

## Motor / implementación principal

### GNU Project — *GNU sed, a stream editor*

Manual oficial de GNU sed.

Referencia principal para el comportamiento real de GNU sed utilizado en Fedora.

Uso principal:

- invocación;
- opciones de línea de comandos;
- exit status;
- scripts;
- comandos;
- sustitución;
- direcciones;
- regex;
- ciclos y buffers;
- pattern space;
- hold space;
- procesamiento multilínea;
- extensiones GNU;
- `-i`;
- `-z`;
- `-s`;
- `-u`;
- `--debug`;
- `--sandbox`;
- `--follow-symlinks`;
- `--posix`;
- comandos específicos de GNU;
- ejemplos;
- limitaciones;
- diferencias GNU/POSIX.

Para comportamiento dependiente de versión, esta fuente tiene prioridad sobre descripciones antiguas del libro principal.

### GNU sed — `sed(1)` / documentación instalada en Fedora

Fuentes locales:

```text
man sed
info sed
sed --help
sed --version
```

Uso principal:

- verificar la versión instalada;
- comprobar opciones disponibles;
- contrastar ejemplos con el entorno Fedora real;
- detectar cambios respecto a documentación o libros anteriores.

## Profundización

### GNU sed — código fuente

Código fuente oficial de GNU sed.

Uso principal en los bloques de internals:

- parser;
- representación de comandos;
- direcciones;
- ciclo de ejecución;
- buffers;
- pattern space;
- hold space;
- sustitución;
- integración con regex;
- branching;
- entrada/salida;
- edición in-place;
- procesamiento NUL;
- debugging;
- manejo de errores;
- tests de regresión.

El código fuente debe utilizarse como profundización y verificación, no como sustituto de la explicación pedagógica.

### Dale Dougherty & Arnold Robbins — *sed & awk*, 2nd Edition

O'Reilly Media.

Referencia complementaria para:

- filosofía Unix de procesamiento de texto;
- sed dentro del ecosistema de herramientas;
- interacción conceptual entre sed y awk;
- problemas clásicos de transformación;
- criterios para decidir cuándo awk resulta más apropiado.

No debe utilizarse para reemplazar documentación moderna de GNU sed en características específicas de implementación.

## Consulta

### `man sed`

Consulta rápida de sintaxis y opciones de GNU sed instalado.

### `info sed`

Consulta navegable de la documentación GNU disponible localmente.

### POSIX `sed`

Consulta de comportamiento portable y resolución de dudas normativas.

### GNU sed manual

Consulta de comportamiento GNU, extensiones, ejemplos y detalles de implementación visibles para el usuario.

## Fuentes auxiliares

### sed FAQ / sed community resources

Pueden utilizarse para algoritmos históricos, ejemplos clásicos y contexto, siempre que las afirmaciones técnicas importantes se contrasten con POSIX o GNU sed cuando corresponda.

### Documentación de Fedora

Debe utilizarse cuando una lección dependa específicamente de:

- empaquetado de sed en Fedora;
- versión disponible;
- integración con RPM;
- convenciones o comportamiento específico del sistema Fedora.

## Jerarquía de fuentes

Cuando las fuentes parezcan discrepar, utilizar esta jerarquía según el tipo de afirmación:

1. POSIX vigente para afirmar qué es portable o normativamente requerido.
2. Manual/documentación de la versión actual de GNU sed para comportamiento GNU.
3. Código fuente y tests de GNU sed para internals o verificación de implementación.
4. *Definitive Guide to sed* para explicación pedagógica y organización conceptual.
5. *sed & awk* y otras referencias para profundización, comparación y contexto histórico.

No debe interpretarse esta jerarquía como que POSIX describe todo el comportamiento GNU: responden a preguntas diferentes.

## Correspondencia con 📚 LECTURA

Cada lección utilizará, cuando corresponda:

**Principal:**
Daniel A. Goldman — *Definitive Guide to sed: Tutorial and Reference*.

**Normativa:**
POSIX `sed` y las secciones normativas relacionadas.

**Motor:**
GNU sed manual y documentación de la versión instalada.

**Profundización:**
Código fuente GNU sed, *sed & awk* u otra referencia técnica apropiada.

**Consulta:**
`man sed`, `info sed`, manual GNU y documentación Fedora.

No es obligatorio forzar una referencia de todas las categorías cuando una categoría no aporte nada a la lección. Las referencias exactas deben estar verificadas antes de incluir capítulos, secciones o páginas concretas.
