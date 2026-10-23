# Bibliografía --- LaTeX 0 → Experto

## Bibliografía principal

### George Grätzer --- *Text and Math Into LaTeX*

Referencia principal para composición de texto y, especialmente,
matemáticas. Se utiliza desde los fundamentos documentales hasta los
bloques de matemáticas avanzadas, teoremas, referencias y preparación de
material científico.

**Uso prioritario:** bloques 1--3, 6--7, 10 y 22.

### Stefan Kottwitz --- *LaTeX Beginner's Guide*

Texto principal de entrada al ecosistema LaTeX. Proporciona una
progresión práctica adecuada para documentos iniciales, estructura,
texto, listas, tablas, imágenes, referencias y otros elementos
esenciales.

**Uso prioritario:** bloques 0--13 y como apoyo práctico posterior.

### Stefan Kottwitz --- *LaTeX Cookbook*

Fuente práctica transversal basada en soluciones y recetas. Complementa
el aprendizaje conceptual con técnicas aplicables a documentos reales.

**Uso prioritario:** bloques intermedios y avanzados, especialmente
diseño, tablas, gráficos, automatización y resolución de problemas.

### Stefan Kottwitz --- *LaTeX Graphics with TikZ*

Referencia especializada para el itinerario gráfico. Debe acompañar la
progresión desde los fundamentos de TikZ hasta diagramas y gráficos
complejos.

**Uso prioritario:** bloques 14--17.

### Frank Mittelbach et al. --- *The LaTeX Companion, Third Edition, Part I*

Referencia avanzada del ecosistema LaTeX moderno. Se utiliza para
profundizar en composición, estructura, paquetes, tipografía,
matemáticas y mecanismos avanzados.

**Uso prioritario:** nivel intermedio → experto.

### Frank Mittelbach et al. --- *The LaTeX Companion, Third Edition, Part II*

Continuación de la referencia avanzada. Junto con Part I constituye la
principal obra de consulta para los bloques expertos y para comprender
soluciones robustas dentro del ecosistema LaTeX contemporáneo.

**Uso prioritario:** nivel avanzado → experto.

## Documentación normativa y oficial

### LaTeX Project

La documentación oficial de LaTeX es la referencia de autoridad para
interfaces, evolución del formato, programación moderna, hooks, expl3 y
herramientas del proyecto.

### CTAN --- Comprehensive TeX Archive Network

Fuente principal para documentación actual de paquetes y clases. Antes
de afirmar opciones o comportamiento específico de un paquete, debe
preferirse su documentación actual en CTAN.

### TeX Live Documentation

Referencia para distribución, herramientas, instalación, configuración y
utilidades del ecosistema TeX Live.

### PGF/TikZ Manual

Referencia normativa para TikZ y PGF. Debe utilizarse para verificar
sintaxis, libraries, keys, paths, nodes, transformations, decorations,
layers y mecanismos avanzados.

### PGFPlots Manual

Referencia principal para comportamiento y sintaxis de PGFPlots.

### biblatex / Biber Documentation

Referencia principal para bibliografía moderna, modelos de datos,
estilos, filtros, sorting y procesamiento con Biber.

### expl3 / LaTeX3 Documentation

Referencia principal para programación LaTeX moderna: funciones,
variables, tipos de datos, convenciones, mensajes, expansión e
interfaces.

### l3build Documentation

Referencia principal para testing, regression tests, documentación y
automatización del desarrollo de paquetes LaTeX.

## Mapa bibliográfico por nivel

**Inicial:** *LaTeX Beginner's Guide* + documentación oficial.

**Fundamentos matemáticos:** *Text and Math Into LaTeX*.

**Intermedio:** *LaTeX Cookbook* + *Text and Math Into LaTeX* +
documentación de paquetes.

**Gráficos:** *LaTeX Graphics with TikZ* + manuales PGF/TikZ y PGFPlots.

**Avanzado:** *The LaTeX Companion, Third Edition --- Part I & Part II*.

**Experto/programación:** *The LaTeX Companion* + documentación oficial
LaTeX/expl3/l3build + documentación específica de cada paquete.

## Política de referencias en las lecciones

Cada lección comienza con `🎯 OBJETIVO` y contiene `📚 LECTURA`. Las
lecturas pueden clasificarse como principal, normativa, motor,
profundización o consulta.

No se inventarán capítulos, secciones ni páginas. Las referencias
exactas solo se proporcionarán cuando estén verificadas. Para
comportamiento que pueda haber cambiado desde la publicación de un
libro, la documentación oficial actual tiene prioridad.


## Documentación complementaria por especialidad

- **LaTeX PDF management y latex-lab** — Interfaces y evolución del soporte PDF, etiquetado y metadatos. Prioridad: bloque 34 y proyecto final.
- **tagpdf** — Manual del paquete y compatibilidad con el etiquetado PDF. Prioridad: bloque 34.
- **LuaTeX / LuaHBTeX manuals** — APIs Lua, nodos, callbacks y motores. Prioridad: bloques 18 y 31.
- **KOMA-Script Guide** — Opciones, clases y tipografía documental. Prioridad: bloque 20.
- **TeX Directory Structure (TDS)** — Organización de árboles TEXMF y distribución. Prioridad: bloques 1 y 29.
- **LaTeX2e source documentation y interfaces del kernel** — Hooks, programación y diagnóstico. Prioridad: bloques 26–30.
- **PDF Association y especificaciones PDF/UA** — Referencia normativa de accesibilidad; verificar la versión aplicable y los derechos de acceso al documento. Prioridad: bloque 34.

## Uso por bloques ampliados

- **1:** CTAN, texdoc, kpathsea, TeX Live y TDS; Fedora RPM frente a tlmgr.
- **27–30:** documentación expl3, interfaces de comandos, kernel, docstrip y l3build.
- **31:** manuales LuaTeX y LuaHBTeX, documentación de luatexbase.
- **33–34:** l3build, latex-lab, tagpdf y documentación de validación PDF.
- **35:** bibliografía transversal y documentación oficial específica de cada dependencia.


## Enlaces oficiales y localización de manuales

Enlaces consultados el 16 de octubre de 2026. En CTAN, usar la sección de
documentación del paquete. Registrar la versión del manual utilizado y
contrastar con la instalación local. No presuponer que el manual web y el
manual instalado describen la misma versión.

| Referencia | Enlace oficial | Consulta local orientativa |
| --- | --- | --- |
| Documentación del kernel y guías de autores | [LaTeX Project](https://www.latex-project.org/help/documentation/) | `texdoc usrguide` |
| Guía para autores de clases y paquetes | [clsguide](https://ctan.org/pkg/clsguide) | `texdoc clsguide` |
| PGF/TikZ | [pgf](https://ctan.org/pkg/pgf) | `texdoc pgfmanual` |
| PGFPlots | [pgfplots](https://ctan.org/pkg/pgfplots) | `texdoc pgfplots` |
| biblatex | [biblatex](https://ctan.org/pkg/biblatex) | `texdoc biblatex` |
| Programación expl3 | [l3kernel](https://ctan.org/pkg/l3kernel) | `texdoc interface3` |
| Pruebas de regresión | [l3build](https://ctan.org/pkg/l3build) | `texdoc l3build` |
| Matemáticas complementarias | [mathtools](https://ctan.org/pkg/mathtools) | `texdoc mathtools` |
| Presentaciones y contenido literal | [beamer](https://ctan.org/pkg/beamer) | `texdoc beameruserguide` |
| Código resaltado y herramientas externas | [minted](https://ctan.org/pkg/minted?lang=en) | `texdoc minted` |
| Estado histórico de xparse | [xparse](https://ctan.org/pkg/xparse?lang=en) | `texdoc xparse` |
| PDF accesible: instrucciones por versión | [LaTeX Tagging Project](https://tagging-project.latex-project.org/documentation/usage-instructions) | Contrastar con la documentación instalada |

Si texdoc no encuentra un documento, usar `texdoc -l`, comprobar los paquetes
de documentación instalados y buscar desde la página oficial correspondiente.

## Lecturas para los ajustes de progresión

- **0 y 18–19:** documentación del motor y de idiomas para un documento mínimo
  en español; avanzar después hacia fuentes e internacionalización completa.
- **6–7:** documentación AMS y mathtools para texto, referencias, alineaciones
  y elección de entornos; ampliar las referencias en el bloque 10.
- **21–24:** manuales Beamer y minted, incluidos frames fragile, latexminted y
  requisitos de ejecución de la versión utilizada.
- **26–30:** guías de autores, clsguide e interface3. Priorizar interfaces del
  kernel; tratar xparse como antecedente y compatibilidad histórica.
- **34–35:** instrucciones actuales del proyecto de etiquetado, compatibilidad
  de clases y paquetes, validación automática y revisión manual.

## Identificación de ediciones y versiones

Se conserva la tercera edición ya indicada de The LaTeX Companion, Part I y
Part II. Para los demás libros, el alumno o el generador debe identificar la
edición del ejemplar utilizado antes de asignar capítulos o páginas. No se
añaden números de edición, ISBN ni localizaciones que no se hayan verificado.
Las páginas CTAN y los manuales son referencias técnicas mantenidas por sus
autores; no constituyen por sí mismos normas formales de conformidad PDF/UA.
