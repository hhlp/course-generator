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
-   Programación LaTeX moderna con expl3, xparse y l3keys.
-   Fundamentos internos de TeX: tokens, category codes, expansión,
    ejecución, registros, glue, boxes y modos.
-   Desarrollo de paquetes `.sty` y clases `.cls`.
-   doc, docstrip, `.dtx`, `.ins` y l3build.
-   LuaLaTeX y extensibilidad con Lua.
-   Rendimiento, testing, compatibilidad y mantenimiento.

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
experto.

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
