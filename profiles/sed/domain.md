# LATEX --- DOMAIN

## Propósito

Este dominio define un curso progresivo de LaTeX desde cero hasta nivel
experto. El objetivo no es limitarse a aprender comandos para producir
PDF, sino comprender la composición tipográfica, el ecosistema
TeX/LaTeX, matemáticas, bibliografía, gráficos, automatización,
programación moderna con expl3 y los fundamentos internos de TeX
necesarios para diseñar paquetes y clases mantenibles.

## Alcance

El curso cubre:

-   TeX, LaTeX y LaTeX2e.
-   pdfTeX, XeTeX y LuaTeX.
-   TeX Live y un entorno de trabajo orientado a Fedora/Linux.
-   Sintaxis, comandos, entornos, grupos, longitudes, contadores, cajas
    y glue.
-   Estructuración de artículos, informes, libros, tesis y proyectos
    grandes.
-   Tipografía y composición profesional.
-   Matemáticas desde modo matemático básico hasta composición avanzada
    con AMS.
-   Tablas, floats, imágenes y referencias cruzadas.
-   BibTeX, Biber y biblatex.
-   Índices, glosarios, acrónimos y nomenclatura.
-   TikZ/PGF y PGFPlots.
-   Unicode, OpenType, fontspec y unicode-math.
-   Internacionalización.
-   KOMA-Script, memoir y clases especializadas.
-   Beamer.
-   Documentos científicos y técnicos.
-   latexmk, Make, arara, Git y CI/CD.
-   Diagnóstico sistemático de errores.
-   Macros y entornos personalizados.
-   Programación moderna con expl3, l3keys e interfaces del kernel;
    xparse como contexto histórico y de compatibilidad.
-   Fundamentos internos de TeX: tokens, category codes, expansión,
    ejecución, registros, glue, boxes y modos.
-   Desarrollo de paquetes `.sty` y clases `.cls`.
-   doc, docstrip, `.dtx`, `.ins` y l3build.
-   LuaLaTeX y extensibilidad con Lua.
-   Rendimiento, testing, compatibilidad y mantenimiento.
-   Accesibilidad, PDF etiquetado, validación y proyecto final experto.

## Fuera de alcance principal

No se convierte el curso en un curso general de diseño gráfico, edición
editorial comercial, Lua generalista, Git, Docker/Podman o CI/CD. Estas
tecnologías aparecen únicamente en la profundidad necesaria para un
flujo de trabajo LaTeX profesional.

## Entorno de referencia

El entorno principal es Fedora/Linux con TeX Live. Los ejemplos deben
ser portables siempre que sea razonable y deben distinguir entre
características de LaTeX y particularidades de una distribución, motor o
herramienta externa.

## Progresión

La progresión conceptual es:

LaTeX básico → composición de texto → matemáticas →
tablas/figuras/referencias → bibliografía → TikZ/PGFPlots → documentos
científicos y grandes proyectos → automatización → macros → expl3 →
internos de TeX → paquetes y clases → LuaLaTeX → testing y mantenimiento
→ accesibilidad y PDF avanzado → proyecto final experto.

## Filosofía del curso

El alumno debe aprender primero la interfaz documental de LaTeX y
después descender progresivamente hacia sus mecanismos internos. Los
detalles de expansión, category codes o registros no deben adelantarse
innecesariamente, pero deben explicarse con profundidad cuando pasan a
ser necesarios para comprender programación avanzada y debugging.

## Práctica

Las lecciones deben favorecer ejemplos compilables y laboratorios
reproducibles. Cuando se enseñe sintaxis, se debe mostrar código LaTeX
real y explicar qué produce y por qué. En debugging se deben usar
Minimal Working Examples. En los bloques avanzados deben aparecer
pequeños paquetes, clases y tests reales.

## Matemáticas

La composición matemática constituye un eje principal del curso. Debe
explicarse la diferencia entre significado matemático y representación
tipográfica, el uso correcto de operadores, delimitadores, espaciado,
alineación, numeración y estructuras AMS.

## TikZ y gráficos

TikZ debe progresar desde coordenadas, paths y nodes hasta estilos
reutilizables, libraries, layers, clipping, pics y externalization.
PGFPlots se trata como la capa principal para visualización científica
reproducible basada en datos.

## Programación

La personalización documental básica precede a expl3. En el nivel
avanzado se priorizan interfaces mantenibles, separación entre API
pública e implementación, mensajes de error adecuados, key-value
interfaces, documentación y tests.

## Fuentes de autoridad

La documentación oficial de LaTeX, TeX Live, CTAN y la documentación
oficial de los paquetes tratados tienen prioridad para comportamiento
actual y sintaxis exacta. Los libros de la bibliografía proporcionan
explicación, progresión, ejemplos y profundidad conceptual.

## Reglas bibliográficas

Las referencias de lectura deben ser exactas solamente cuando capítulo,
sección o página hayan sido verificados. Si no se ha verificado una
localización concreta, se cita el libro o documentación relevante sin
inventar números de página o secciones.

## Resultado esperado

Al finalizar, el alumno debe poder diseñar, implementar, automatizar,
diagnosticar, probar y mantener proyectos LaTeX complejos; crear
documentos científicos de alta calidad; construir gráficos con
TikZ/PGFPlots; desarrollar paquetes y clases; y comprender
suficientemente el modelo de ejecución de TeX para razonar sobre
problemas avanzados.

## CTAN y aprendizaje autónomo de paquetes

El curso debe enseñar CTAN como parte operativa del flujo de trabajo, no únicamente como un repositorio que se menciona. El alumno debe aprender a pasar de una necesidad concreta a localizar un paquete, evaluar su propósito, encontrar y leer su documentación, comprobar si está instalado, cargarlo correctamente y validar su uso mediante un ejemplo mínimo compilable.

El flujo de referencia es:

Necesidad → buscar en CTAN → identificar el paquete → consultar documentación → `texdoc` → comprobar instalación con `kpsewhich` → revisar dependencias y opciones → cargar con `\usepackage` → construir un ejemplo mínimo → compilar → diagnosticar errores y warnings.

Cuando se introduzca un paquete nuevo, la lección debe explicar, según corresponda:

- qué problema resuelve y cuándo usarlo;
- nombre del paquete y relación entre nombre CTAN, paquete TeX Live y archivo `.sty`/`.cls`;
- dónde localizar su página y documentación;
- cómo consultar su manual con `texdoc`;
- cómo comprobar archivos instalados con `kpsewhich`;
- cómo cargarlo mediante `\usepackage{...}` o el mecanismo apropiado;
- opciones importantes y orden de carga cuando sea relevante;
- dependencias, incompatibilidades o requisitos importantes;
- un Minimal Working Example compilable;
- errores habituales, especialmente archivos no encontrados y conflictos de paquetes.

La instalación manual en árboles TEXMF debe enseñarse después de la gestión normal mediante TeX Live/distribución y debe explicarse cuándo es apropiada y cuándo conviene evitarla. En Fedora se distinguirán los paquetes del sistema, TeX Live y el árbol TEXMF del usuario.

Esta metodología se aplica transversalmente a paquetes como `amsmath`, `booktabs`, `hyperref`, `cleveref`, `biblatex`, `tikz`, `pgfplots`, `fontspec`, `unicode-math`, `tcolorbox` y los demás paquetes introducidos durante el curso.


## Profundidad experta y evaluación

Cada lección debe diferenciar conceptos, mecanismos internos, sintaxis, compatibilidad y casos reales. Incluir ejemplos compilables cuando corresponda, comandos de compilación, resultado esperado, interpretación, errores frecuentes y ejercicios de diagnóstico. No inventar salidas de herramientas ni garantizar compatibilidad sin verificar motor y versión.

Los laboratorios integradores de matemáticas, gráficos, automatización y programación deben producir artefactos verificables y reutilizables. Los proyectos avanzados incorporan tests de regresión, documentación y control de versiones.

## Seguridad de compilación

Explicar riesgos de ejecutar documentos de origen desconocido, shell escape, herramientas externas, lectura/escritura de archivos y entornos de compilación. Usar el mínimo privilegio y aislar builds cuando sea pertinente.

## Accesibilidad y PDF avanzado

El bloque 34 aborda PDF etiquetado, PDF/UA, DocumentMetadata, tagpdf, semántica, idioma, alternativas textuales, orden de lectura, tablas, enlaces y validación. Distinguir objetivos normativos de la compatibilidad real y cambiante del kernel, motor, clase y paquetes; combinar validación automática con revisión manual. El proyecto final experto se desplaza al bloque 35 y debe integrar estas competencias cuando sea viable.

## Gestión avanzada de CTAN y TeX Live

Distinguir paquetes RPM de Fedora de instalaciones TeX Live administradas por tlmgr; evitar mezclar gestores en el mismo árbol. Enseñar TDS, TEXMFHOME, TEXMFLOCAL, mktexlsr/texhash, texdoc -l y diagnóstico de versiones.


## Prerrequisitos y progresión operativa

- En el bloque 0, producir un documento mínimo en español con Unicode,
  idioma, acentos y guionado. Explicar únicamente la configuración necesaria
  para el motor elegido; ampliar fuentes e idiomas en los bloques 18 y 19.
- Antes del laboratorio 7.27, estudiar 6.21 y 6.22: referencias mínimas,
  texto en fórmulas y elección del entorno. El bloque 10 profundiza en
  referencias, enlaces y automatización sin repetir toda la introducción.
- Completar 26.16–26.18 antes del bloque 27. Introducen tokens, expansión y
  ejecución con ejemplos pequeños; el bloque 28 desarrolla el modelo interno.
- Al introducir 27.24, comprobar que se distingue token, valor y nombre de
  variable. Las firmas de argumentos no se presentan como intercambiables.
- Mantener las lecciones existentes y sus identificadores. Las ampliaciones
  se añaden al final del bloque; las dependencias pedagógicas se explicitan
  al inicio de la lección que las necesita.

## Interfaces modernas y compatibilidad histórica

Priorizar las interfaces documentales incorporadas al kernel, entre ellas
`\NewDocumentCommand`. No cargar `xparse` por rutina en documentos modernos.
Las lecciones históricas sobre xparse explican su relación con las interfaces
actuales y las necesidades de compatibilidad de documentos antiguos.
En paquetes y clases, distinguir `\usepackage`, `\RequirePackage`,
`\LoadClass`, requisitos de formato y gestión de opciones. Consultar la guía
actual para autores de clases y paquetes antes de recomendar una interfaz.

La búsqueda de CTAN se adapta al recurso: las bibliotecas TikZ se cargan con
`\usetikzlibrary`, las clases con `\documentclass` y los paquetes con su
mecanismo apropiado. No identificar automáticamente el nombre CTAN con el
archivo que se carga ni con el nombre del paquete RPM.

## Herramientas externas y ejemplos por versión

En minted, distinguir la versión del paquete, el ejecutable latexminted y
Pygments. Verificar requisitos reales de instalación y ejecución; no afirmar
que siempre hace falta shell escape completo. Explicar la ejecución
restringida, su configuración efectiva y los casos que requieren otro flujo.
En Beamer, introducir frames `fragile` antes de integrar contenido verbatim.

Cada laboratorio sensible a versiones registra motor, versión del formato,
clase, paquetes y herramientas externas. La documentación local puede
corresponder a una versión distinta de la publicada en CTAN: contrastarlas.

## Evaluación del proyecto final

El bloque 35 produce fuentes modulares, clase y paquete documentados,
recursos, instrucciones de compilación, pruebas y resultados verificables.
La evaluación utiliza estos criterios:

1. Compilación reproducible con motor y dependencias declarados; explicar
   diferencias entre reproducir el proceso y obtener bytes PDF idénticos.
2. Corrección tipográfica y funcional: matemáticas, referencias, bibliografía,
   índices y gráficos; resolver o justificar los avisos relevantes.
3. Interfaces mantenibles y pruebas de regresión con resultados registrados.
4. Accesibilidad: idioma, estructura, alternativas, navegación y orden de
   lectura; combinar revisión automática y manual con herramientas declaradas.
5. Documentación suficiente para instalar, compilar, probar y mantener.

Antes de exigir conformidad PDF/UA, declarar la versión objetivo y comprobar
la compatibilidad de la combinación utilizada. Una compilación correcta o un
validador sin errores no demuestran por sí solos accesibilidad completa.
Documentar limitaciones y alternativas; no declarar conformidad no verificada.
En el bloque 34, colocar `\DocumentMetadata` antes de `\documentclass` y
seleccionar sus claves a partir de la documentación aplicable a la versión.
