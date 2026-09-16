# MATPLOTLIB + SEABORN + POLARS — Dominio del PATH

## Objetivo y alcance

Desarrollar desde cero la capacidad de preparar datos con Polars, crear visualizaciones con Matplotlib y realizar exploración estadística con Seaborn. Culminar en pipelines reproducibles, verificables y eficientes. El programa canónico es initial.txt: 29 bloques (0–28) y 236 lecciones. No omitir ni fusionar lecciones al generar contenidos. El temario es un índice de lecciones que se desarrollarán, no un curso ya redactado.

Polars es la biblioteca de datos; no confundirla con gráficos polares, que se estudian en 15.4. Matplotlib aporta el control de figuras; Seaborn, visualización estadística. NumPy, pandas, Arrow y estadística son conocimientos auxiliares. No convertir esta ruta en un curso completo de pandas, desarrollo web, aprendizaje automático o administración de bases de datos.

## Plataforma y reproducibilidad

Usar Fedora, Python y uv. Elegir una versión estable de Python compatible con todas las dependencias necesarias; no exigir una versión preliminar. Registrar versiones efectivas, dependencias, semilla y procedencia del conjunto de datos. Mantener pyproject.toml y uv.lock en los proyectos prácticos. Diferenciar instalación de paquetes Python y dependencias del sistema, como fuentes y codificadores de vídeo. No fijar como universal una versión de API sin consultar su documentación.

Los ejemplos deben funcionar en scripts y explicar las diferencias relevantes con JupyterLab. Proporcionar datos pequeños construidos en código o archivos reproducibles; evitar que un laboratorio dependa exclusivamente de una descarga remota. Los datos sintéticos deben identificarse como tales. Separar código, datos originales, datos preparados y salidas.

## Estándar obligatorio de cada lección

1. Abrir con 🎯 OBJETIVO: resultados concretos y comprobables.
2. Explicar desde los requisitos previos hasta el mecanismo y las decisiones prácticas. Mantener profundidad; no entregar únicamente una lista de funciones.
3. Incluir ejemplos completos con importaciones, datos y resultado esperado. Explicar las unidades, formas, tipos y significado estadístico.
4. Incluir 🧪 Laboratorio/ejemplos con pasos, comprobaciones y criterios de éxito cuando corresponda; las lecciones tituladas laboratorio siempre deben tener práctica completa.
5. Añadir ⚠️ Errores frecuentes y 💡 Idea importante cuando aporten valor.
6. Incluir lectura y referencias específicas verificables antes del cierre. No inventar capítulos, páginas ni resultados de ejecución.
7. Terminar siempre con 🧠 QUÉ DEBES RECORDAR: entre 3 y 7 ideas clave, sin repetir simplemente el objetivo.

Usar español claro y nombres originales de las APIs. En initial.txt conservar un bloque o una lección por línea, sin sangría, viñetas, tablas, títulos previos ni etiquetas de etapa. Mantener numeración continua dentro de cada bloque.

## Reglas técnicas: Polars

Explicar Series, DataFrame, LazyFrame, esquemas y contextos de expresiones antes de optimizaciones. Priorizar expresiones nativas y evitar bucles por fila. Diferenciar null y NaN, casts estrictos y tolerantes, fechas con y sin zona horaria, y List/Array/Struct. No trasladar automáticamente conceptos de índices de pandas.

En joins declarar claves, cardinalidad esperada y tratamiento de ausencias; comprobar duplicación de filas. En ventanas temporales documentar orden, límites, frecuencia y zona horaria. Comparar planes mediante explain y materializar solamente lo necesario. Streaming y zero-copy deben justificarse para la operación, tipos y versiones concretas, no prometerse siempre.

## Reglas técnicas: Matplotlib

Priorizar la interfaz explícita Figure/Axes. Diferenciar Figure, Axes y Axis. Las funciones reutilizables deben recibir un Axes o devolver los objetos creados; documentar quién guarda y cierra la figura. Explicar transforms, Artists, backends, layouts y Collections de forma progresiva.

Los gráficos deben incluir etiquetas, unidades, leyendas y escalas justificadas. Para exportación controlar dimensiones físicas, DPI, tipografía, rasterización y formato. Para automatización explicar renderizado sin pantalla y cierre de figuras. Distinguir interactividad del backend, widgets y animación; indicar dependencias externas al exportar vídeo.

## Reglas técnicas: Seaborn e interoperabilidad

Diferenciar funciones de nivel Axes y Figure; no asumir que las segundas aceptan un Axes existente. Explicar datos largos y anchos, hue/size/style, facetas, orden y paletas consistentes. Cubrir tanto funciones clásicas como seaborn.objects.

Verificar compatibilidad de DataFrames de Polars con la función y versión utilizadas. Cuando sea necesario, convertir únicamente la tabla final a pandas o NumPy, declarando dependencias, tipos, copias y pérdida potencial de información. No afirmar que toda integración es nativa o sin copias.

Explicitar cuándo Seaborn agrega datos, qué estimador utiliza y qué significa el intervalo mostrado. Evitar doble agregación después de Polars. Distinguir recuentos, proporciones, densidades, desviación estándar, error estándar e intervalos de confianza. Justificar KDE, bootstrap, unidad de muestreo y observaciones dependientes. Una tendencia visual o regresión exploratoria no demuestra causalidad.

## Calidad, diseño y rendimiento

Comenzar cada gráfico con una pregunta analítica. Tratar escalas truncadas, ejes dobles, sobreposición, accesibilidad cromática y límites del 3D. Comparar alternativas según claridad y corrección, no sólo estética.

Medir separadamente carga, consulta, conversión y renderizado. Declarar hardware, tamaño y metodología al comparar rendimiento. Muestreo y reducción temporal deben exponer sesgos y pérdida de extremos. Probar transformaciones con polars.testing y contratos de datos; usar regresión visual sólo cuando aporte valor, controlando fuentes, backend y tolerancias.

## Hitos y evaluación

| Bloques | Resultado demostrable |
| --- | --- |
| 0–6 | Preparar el entorno, interpretar gráficos, cargar y limpiar datos. |
| 7–13 | Agregar y combinar datos, trabajar con tiempo y crear figuras compuestas. |
| 14–23 | Elaborar visualizaciones científicas y estadísticas avanzadas. |
| 24–27 | Automatizar, verificar, optimizar y diagnosticar pipelines. |
| 28 | Defender proyectos completos y justificar decisiones. |

Cada proyecto debe entregar pregunta, datos y licencia/procedencia, contrato de esquema, código reproducible, verificaciones, figuras exportadas, interpretación y limitaciones. El proyecto integral incluirá lectura lazy, limpieza, joins o ventanas, validación, visualización y exportación mediante un comando. El nivel experto requiere práctica y resolución de problemas nuevos; completar el índice no lo garantiza.

## Uso del paquete en course-generator

Ubicar los cuatro archivos en paths/python-graficos/. El perfil referencia el archivo compartido ../../config/pedagogy.md, que no forma parte de este paquete. Mantener el nombre solicitado bibliografy.md y la clave files.bibliography apuntando a él. La sintaxis YAML y la numeración pueden verificarse independientemente; la compatibilidad completa del perfil debe comprobarse con el cargador de la instalación real de course-generator, no disponible en esta entrega.
