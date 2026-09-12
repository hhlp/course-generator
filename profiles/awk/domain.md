# AWK EN PROFUNDIDAD --- domain.md

## Identidad del PATH

Este PATH enseña AWK desde fundamentos hasta un nivel experto, usando
Fedora Linux como entorno práctico principal y GNU awk (`gawk`) como
implementación de referencia para las capacidades avanzadas.

AWK debe presentarse primero como lenguaje de procesamiento de texto y
datos orientado a registros, no como una colección de one-liners. El
alumno debe comprender el modelo de ejecución, el sistema de registros y
campos, las expresiones, los patterns, las actions, los arrays
asociativos, las funciones y la entrada/salida antes de abordar
extensiones avanzadas.

## Alcance

El PATH cubre:

-   fundamentos Unix necesarios para comprender AWK;
-   modelo `pattern { action }`;
-   registros, campos, `RS`, `ORS`, `FS`, `OFS`, `FPAT` y `FIELDWIDTHS`;
-   variables, tipos, coerciones y expresiones;
-   ERE utilizadas por AWK;
-   control de flujo;
-   strings y funciones matemáticas;
-   arrays asociativos y multidimensionalidad;
-   funciones definidas por el usuario;
-   variables predefinidas;
-   procesamiento multiarchivo;
-   `getline`;
-   interacción con shell y sistema;
-   agregación, análisis, joins y algoritmos clásicos;
-   GNU awk en profundidad;
-   ordenación;
-   tiempo, fechas, bitwise y capacidades numéricas;
-   locales, Unicode e internacionalización;
-   programas AWK grandes;
-   debugging, profiling, portabilidad, rendimiento y seguridad;
-   AWK como parser y generador de informes;
-   integración con Fedora;
-   internals de AWK/gawk;
-   extensiones dinámicas de GNU awk y comunicación con C;
-   ingeniería, testing, distribución y mantenimiento;
-   CLI y modos de ejecución de gawk;
-   procesamiento de CSV/TSV y formatos difíciles;
-   coprocesses y comunicación avanzada;
-   proyecto final `awk-toolkit`.

## Modelo conceptual obligatorio

Las lecciones deben mantener como eje conceptual:

entrada → registros → campos → patterns → actions → estado → salida

El alumno debe poder explicar qué sucede para cada registro y cómo
`BEGIN`, las reglas normales, `END`, `BEGINFILE` y `ENDFILE` alteran el
ciclo.

No enseñar AWK únicamente mediante recetas. Cada construcción debe
relacionarse con su semántica dentro del modelo de ejecución.

## POSIX AWK frente a GNU awk

Distinguir explícitamente tres categorías cuando sea relevante:

1.  comportamiento y características de AWK especificadas por POSIX;
2.  comportamiento ampliamente disponible pero dependiente de
    implementación;
3.  extensiones específicas de GNU awk/gawk.

No presentar una extensión GNU como si perteneciera al lenguaje AWK
portable.

Cuando una solución pueda escribirse razonablemente en POSIX AWK,
mostrar primero la solución portable. Después puede mostrarse una
variante gawk si aporta claridad, seguridad, rendimiento o
funcionalidad.

Las lecciones específicamente dedicadas a GNU awk pueden usar
directamente sus extensiones, pero deben identificarlas como tales.

## Implementaciones

El alumno debe conocer al menos conceptualmente:

-   BWK/original awk;
-   nawk y su importancia histórica;
-   GNU awk (`gawk`);
-   mawk.

Fedora y `gawk` constituyen el entorno práctico preferido, pero el PATH
debe enseñar a reconocer dependencias específicas de implementación.

## Política sobre expresiones regulares

Este PATH no sustituye al PATH independiente de Regex.

Aquí se enseña únicamente lo necesario para comprender las expresiones
regulares dentro de AWK:

-   ERE;
-   `/regex/`;
-   `~` y `!~`;
-   regex constantes;
-   regex dinámicas;
-   regex almacenadas en variables;
-   interacción con `FS`, `RS`, `FPAT`, `match()`, `sub()`, `gsub()`,
    `gensub()` y funciones relacionadas;
-   efectos de locale;
-   diferencias relevantes POSIX/gawk.

No convertir las lecciones de AWK en un segundo curso general de regex.

## Fedora Linux

Los laboratorios deben utilizar Fedora cuando el sistema operativo sea
relevante.

Priorizar mecanismos reales de descubrimiento:

-   `rpm -qi gawk`;
-   `rpm -ql gawk`;
-   `awk --version` cuando corresponda;
-   `gawk --version`;
-   `man`;
-   `info gawk`;
-   `/etc/passwd`;
-   `/etc/group`;
-   `rpm`;
-   `dnf`;
-   `journalctl`;
-   `systemctl`;
-   `ss`;
-   `ip`;
-   `/proc`;
-   `/sys`.

No asumir que una herramienta o extensión opcional está instalada.
Enseñar a comprobarlo.

## Relación con el shell

AWK debe integrarse correctamente con pipelines Unix y con Bash/Zsh sin
confundir los dos lenguajes.

Explicar especialmente:

-   qué interpreta el shell;
-   qué interpreta AWK;
-   quoting;
-   expansión de `$`;
-   `-v`;
-   `ENVIRON`;
-   asignaciones `variable=valor`;
-   stdin/stdout/stderr;
-   pipes;
-   process substitution cuando sea pertinente;
-   exit status.

Evitar interpolaciones inseguras de datos del shell dentro del código
AWK.

## Datos reales

Los ejemplos deben evolucionar desde datasets pequeños y controlados
hacia datos reales.

El alumno debe aprender cuándo AWK es adecuado y cuándo debe utilizar
otra herramienta.

En particular, distinguir:

-   texto delimitado simple;
-   TSV;
-   CSV real;
-   JSON;
-   XML;
-   YAML;
-   datos binarios;
-   protocolos y formatos que requieren parsers específicos.

No enseñar `FS=","` como parser CSV universal.

## getline

`getline` debe enseñarse con especial precisión.

Siempre aclarar qué variante se utiliza y qué variables puede modificar
(`$0`, `NF`, `NR`, `FNR`), así como su valor de retorno, EOF, errores y
necesidad potencial de `close()`.

No utilizar `getline` cuando el ciclo normal de entrada de AWK resuelva
el problema de forma más clara.

## Arrays

Explicar que los arrays AWK son asociativos.

Distinguir:

-   acceso `array[key]`;
-   pertenencia `key in array`;
-   creación implícita;
-   `delete`;
-   recorrido;
-   ausencia de orden portable;
-   `SUBSEP` e índices compuestos;
-   arrays de arrays de gawk.

No asumir orden de iteración salvo que una característica específica de
gawk lo establezca.

## Entrada/salida y recursos

Cuando se abran archivos, pipes o coprocesses dinámicamente, explicar la
gestión de recursos.

Cubrir `close()` y `fflush()` cuando correspondan.

Evitar ejemplos que generen cantidades ilimitadas de archivos o pipes
abiertos.

## Seguridad

Toda lección que combine entrada no confiable con `system()`, pipes,
nombres de archivos o comandos externos debe tratar la posibilidad de
command injection.

No construir comandos shell concatenando datos no confiables sin
discutir validación y quoting.

Considerar también:

-   consumo de memoria mediante arrays;
-   regex costosas;
-   entradas gigantes;
-   nombres de archivo hostiles;
-   límites de recursos;
-   ejecución con privilegios mínimos.

## Rendimiento

AWK es principalmente una herramienta de streaming, pero los arrays
pueden convertir un programa en consumidor de memoria proporcional al
dataset.

Distinguir algoritmos streaming de algoritmos que almacenan el conjunto
completo.

Las optimizaciones deben basarse en medidas cuando sea posible, usando
las herramientas de profiling de gawk en las lecciones correspondientes.

## Programas grandes

A partir del nivel avanzado, promover:

-   archivos `.awk`;
-   funciones;
-   separación de responsabilidades;
-   bibliotecas;
-   `@include` cuando se use gawk;
-   `AWKPATH`;
-   namespaces cuando aporten valor;
-   contratos de entrada/salida;
-   códigos de salida;
-   documentación;
-   tests;
-   fixtures;
-   golden files;
-   profiling.

AWK debe tratarse como software cuando el problema supera un one-liner.

## Internals

Los bloques de internals deben explicar suficientemente:

-   lexer;
-   parser;
-   AST conceptual;
-   evaluación;
-   ciclo de lectura;
-   field splitting y lazy field splitting;
-   reconstrucción de registros;
-   representación string/número;
-   arrays asociativos;
-   regex engine;
-   archivos abiertos;
-   funciones;
-   arquitectura de extensiones.

Diferenciar siempre entre comportamiento especificado/documentado e
implementación interna concreta de una versión.

## Extensiones GNU awk

Al tratar extensiones dinámicas:

-   explicar `@load`;
-   `AWKLIBPATH`;
-   API de extensiones;
-   intercambio de valores y arrays con C;
-   compilación en Fedora;
-   compatibilidad de versiones;
-   riesgos de portabilidad.

No convertir el curso en un curso de C: C aparece únicamente para
comprender y construir extensiones de gawk.

## Testing

Los programas avanzados deben poder verificarse mediante:

-   fixtures;
-   stdout esperado;
-   stderr esperado;
-   exit status;
-   golden files;
-   casos límite;
-   pruebas negativas;
-   diferentes locales;
-   diferentes implementaciones cuando sea posible;
-   `gawk --lint`;
-   modos POSIX/traditional cuando correspondan.

## Proyecto final

`awk-toolkit` debe ser una aplicación real y mantenible, no una
colección desconectada de one-liners.

Debe integrar, según el PATH:

-   stdin y múltiples archivos;
-   selección de registros/campos;
-   filtros regex y numéricos;
-   transformaciones;
-   agregaciones;
-   joins;
-   ordenación y top-N;
-   informes;
-   streaming;
-   funciones reutilizables;
-   manejo de errores;
-   exit codes;
-   debugging/profiling;
-   tests;
-   seguridad;
-   portabilidad documentada;
-   integración Fedora/Zsh;
-   distribución.

Las extensiones GNU deben utilizarse deliberadamente y documentarse.

## Criterio de profundidad

Cada lección debe ser autocontenida y específica del tema.

Evitar:

-   introducciones genéricas repetidas;
-   listas de definiciones sin explicar semántica;
-   ejemplos triviales que no demuestran el concepto;
-   afirmar comportamiento no verificado de una implementación;
-   confundir AWK portable con gawk.

Preferir:

concepto → modelo mental → sintaxis → semántica → ejemplo → observación
del resultado → límites → aplicación práctica.

## Resultado esperado

Al terminar el PATH, el alumno debe poder:

-   leer y explicar programas AWK complejos;
-   escribir soluciones POSIX portables;
-   aprovechar conscientemente GNU awk;
-   diagnosticar errores semánticos, de entrada, regex, tipos y
    recursos;
-   procesar datasets reales;
-   decidir cuándo AWK no es la herramienta apropiada;
-   diseñar, probar, perfilar, asegurar y mantener aplicaciones AWK;
-   comprender suficientemente los internals de gawk para relacionarlos
    con su comportamiento observable.
