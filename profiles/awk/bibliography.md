# AWK EN PROFUNDIDAD --- bibliography.md

## Política bibliográfica

Las referencias se organizan por función pedagógica.

No inventar números de capítulo, sección o página. Las referencias
exactas de una lección deben incluirse únicamente cuando hayan sido
verificadas contra la edición o documentación utilizada.

Distinguir siempre documentación normativa, documentación de
implementación y bibliografía didáctica.

## Principal

### Learning AWK Programming

Libro principal indicado para este PATH.

Uso:

-   progresión didáctica del lenguaje;
-   fundamentos de AWK;
-   pattern-action;
-   registros y campos;
-   variables;
-   expresiones;
-   patterns;
-   control de flujo;
-   salida;
-   strings;
-   arrays;
-   funciones;
-   procesamiento de datos;
-   construcción progresiva de programas AWK.

Debe utilizarse como guía principal cuando cubra directamente la materia
de la lección.

Si un tema avanzado del PATH no está cubierto suficientemente por esta
obra, complementar con las referencias de GNU awk, POSIX y
profundización.

## Normativa

### POSIX / The Open Group --- awk

Referencia normativa para determinar el comportamiento portable de AWK.

Uso prioritario para:

-   sintaxis estándar;
-   operands y options;
-   modelo de entrada;
-   registros y campos;
-   variables estándar;
-   expresiones;
-   ERE;
-   patterns/actions;
-   statements;
-   funciones estándar;
-   comportamiento requerido por POSIX;
-   portabilidad.

Utilizarla para decidir si una característica pertenece a AWK portable.

No atribuir a POSIX extensiones que sólo existan en GNU awk u otras
implementaciones.

## Motor

### GNU Awk User's Guide

Documentación de referencia principal para GNU awk (`gawk`).

Uso prioritario para:

-   comportamiento de gawk;
-   opciones de línea de comandos;
-   `BEGINFILE` / `ENDFILE`;
-   `ARGIND`;
-   `RT`;
-   `FPAT`;
-   `FIELDWIDTHS`;
-   `PROCINFO`;
-   `SYMTAB`;
-   `FUNCTAB`;
-   `IGNORECASE`;
-   arrays de arrays;
-   `asort()` / `asorti()`;
-   `patsplit()`;
-   `gensub()`;
-   `strtonum()`;
-   tiempo;
-   bitwise;
-   MPFR/GMP y `--bignum`;
-   namespaces;
-   `@include`;
-   `AWKPATH`;
-   debugger;
-   profiling;
-   internacionalización;
-   coprocesses;
-   networking específico de gawk;
-   extensiones dinámicas;
-   `@load`;
-   `AWKLIBPATH`;
-   API de extensiones;
-   modos POSIX/traditional;
-   lint;
-   sandbox y demás opciones cuando estén disponibles en la versión
    estudiada.

Para características dependientes de versión, verificar la documentación
de la versión de gawk instalada o de la versión objetivo.

## Profundización

### Effective awk Programming --- Arnold Robbins

Referencia de profundización para comprender AWK y GNU awk más allá de
la sintaxis elemental.

Uso:

-   modelo mental de AWK;
-   idioms;
-   programación robusta;
-   diferencias de implementación;
-   GNU awk;
-   diseño de programas;
-   casos avanzados;
-   portabilidad;
-   debugging;
-   rendimiento;
-   extensibilidad.

Cuando *Effective awk Programming* corresponda a la misma documentación
distribuida como manual de GNU awk en una edición determinada, evitar
tratar ambas como evidencia independiente.

## Consulta

### `man awk`

Consulta rápida de la interfaz disponible en el sistema.

### `man gawk`

Consulta local de GNU awk cuando esté disponible.

### `info gawk`

Manual GNU instalado localmente. Debe priorizarse para comprobar la
versión realmente disponible en Fedora cuando sea necesario.

### `gawk --help`

Referencia inmediata para opciones soportadas por el binario instalado.

### `gawk --version`

Utilizar para identificar versión y capacidades antes de depender de
características específicas.

### Paquete Fedora `gawk`

Usar herramientas RPM para descubrir la instalación real:

``` text
rpm -qi gawk
rpm -ql gawk
```

La información del paquete sirve para estudiar cómo Fedora distribuye
gawk, qué documentación instala y qué archivos proporciona.

## Implementaciones adicionales para portabilidad

### BWK awk

Referencia de comparación para el AWK mantenido en la tradición de Brian
Kernighan.

Uso:

-   historia;
-   comportamiento entre implementaciones;
-   pruebas de portabilidad;
-   diferencias frente a GNU awk.

### mawk

Implementación adicional para estudiar portabilidad y comportamiento.

Uso:

-   comparación de scripts;
-   detección de dependencias GNU;
-   rendimiento cuando sea relevante;
-   matrices de pruebas.

No asumir que estas implementaciones están instaladas en Fedora.
Comprobar disponibilidad antes de los laboratorios.

## Código fuente e internals

### Código fuente de GNU awk

Fuente primaria para las lecciones dedicadas explícitamente a internals
de gawk.

Uso:

-   arquitectura;
-   lexer/parser;
-   evaluación;
-   representación de valores;
-   field splitting;
-   arrays;
-   integración con regex;
-   entrada/salida;
-   funciones;
-   debugger/profiler cuando proceda;
-   arquitectura de extensiones.

Las conclusiones derivadas del código fuente deben vincularse a una
versión concreta cuando el detalle pueda cambiar.

No usar detalles internos como si fueran garantías de POSIX.

## Fedora

### Documentación Fedora

Referencia para aspectos específicos del entorno:

-   instalación;
-   paquetes;
-   integración con el sistema;
-   convenciones Fedora;
-   empaquetado cuando el PATH llegue a distribución.

### RPM

Para descubrir contenido y metadatos del paquete:

``` text
rpm -qi gawk
rpm -ql gawk
rpm -q --requires gawk
```

La salida real del sistema tiene prioridad sobre asumir qué archivos
contiene una versión de Fedora.

## Shell y utilidades Unix

Cuando una lección combine AWK con shell o herramientas externas,
consultar la documentación específica correspondiente:

-   Bash/Zsh cuando el quoting dependa del shell;
-   GNU Coreutils;
-   grep;
-   sed;
-   sort;
-   findutils;
-   util-linux;
-   systemd;
-   rpm/dnf;
-   iproute2.

AWK sigue siendo el objeto de estudio. Estas referencias deben
utilizarse sólo para explicar correctamente la interfaz entre
herramientas.

## Regex

El PATH independiente de Regex constituye la base conceptual general.

En AWK, utilizar POSIX y GNU awk para verificar específicamente:

-   ERE admitidas;
-   regex constants;
-   dynamic regex;
-   operadores `~` / `!~`;
-   interval expressions;
-   locale;
-   comportamiento específico de gawk.

No duplicar innecesariamente la teoría general del PATH Regex.

## Datos estructurados

Para CSV, JSON, XML o YAML, las fuentes de AWK deben utilizarse para
explicar las capacidades y límites de AWK.

Cuando se compare con herramientas especializadas, consultar la
documentación de esas herramientas únicamente para la comparación
necesaria.

No afirmar que AWK implementa correctamente un formato completo sólo
porque un ejemplo sencillo pueda procesarse con `FS` o regex.

## Seguridad

Para seguridad, priorizar:

1.  documentación GNU awk para semántica de `system()`, pipes,
    coprocesses, sandbox y E/S;
2.  documentación del shell para quoting y ejecución;
3.  principios generales de validación de entrada y mínimo privilegio.

Los ejemplos deben distinguir entre datos y código/comandos.

## Rendimiento

Para rendimiento:

1.  GNU Awk User's Guide para profiling y comportamiento documentado;
2.  mediciones reproducibles;
3.  código fuente sólo cuando se investigue un detalle interno.

No presentar intuiciones de rendimiento como resultados medidos.

## Mapeo por niveles

### Fundamentos

Principal: - Learning AWK Programming

Normativa: - POSIX awk

Motor: - GNU Awk User's Guide

### Intermedio

Principal: - Learning AWK Programming

Normativa: - POSIX awk

Motor: - GNU Awk User's Guide

Profundización: - Effective awk Programming

### Avanzado

Motor: - GNU Awk User's Guide

Profundización: - Effective awk Programming

Normativa: - POSIX awk para límites de portabilidad

Consulta: - documentación local Fedora/gawk

### Experto

Motor: - GNU Awk User's Guide

Normativa: - POSIX awk

Profundización: - Effective awk Programming

Consulta: - código fuente de GNU awk; - BWK awk; - mawk; - documentación
Fedora; - documentación de herramientas integradas.

## Regla para 📚 LECTURA

Cada lección puede utilizar estas categorías:

### Principal

Learning AWK Programming cuando cubra el tema.

### Normativa

POSIX awk cuando exista una cuestión de semántica estándar o
portabilidad.

### Motor

GNU Awk User's Guide cuando se estudie gawk o sea necesario contrastar
su comportamiento.

### Profundización

Effective awk Programming cuando aporte explicación o diseño adicional.

### Consulta

Manuales locales, código fuente, Fedora u otras herramientas cuando sean
pertinentes.

No rellenar categorías artificialmente. Si una categoría no aporta una
referencia relevante y verificable para una lección, indicarlo conforme
a la política del generador en vez de inventar una referencia.

## Regla de referencias exactas

Las referencias específicas de capítulo, sección o página deben
verificarse.

Formato recomendado:

``` text
📚 LECTURA

Principal:
  Learning AWK Programming
  └── capítulo/sección verificada

Normativa:
  POSIX — awk
  └── sección verificada

Motor:
  GNU Awk User's Guide
  └── sección verificada

Profundización:
  Effective awk Programming
  └── sección verificada

Consulta:
  man gawk / info gawk / documentación Fedora
  └── recurso concreto cuando corresponda
```

No generar una falsa precisión bibliográfica.

## Jerarquía ante discrepancias

Si las fuentes parecen discrepar:

1.  para portabilidad normativa, comprobar POSIX;
2.  para comportamiento de GNU awk, comprobar la documentación de la
    versión de gawk;
3.  para comportamiento observable, reproducirlo en la versión objetivo
    cuando sea apropiado;
4.  para internals, comprobar el código fuente de esa versión;
5.  utilizar los libros para pedagogía e interpretación, no para
    sustituir una especificación o documentación de versión más precisa.

Documentar explícitamente las diferencias relevantes.

## Objetivo bibliográfico

La bibliografía debe permitir que el curso enseñe simultáneamente:

-   AWK como lenguaje;
-   AWK portable;
-   GNU awk como implementación avanzada;
-   uso real sobre Fedora;
-   ingeniería de programas AWK;
-   internals y extensibilidad;

sin mezclar estas capas ni presentar características específicas de GNU
como parte universal del lenguaje.
