# PYTHON 3.15 EN PROFUNDIDAD — Dominio y contrato pedagógico

## Finalidad y alcance

Ruta de cero a experto en Python, con Fedora como entorno principal y CPython como implementación de referencia. Incluye lenguaje, modelo de objetos, biblioteca estándar, ingeniería de software, concurrencia, asincronía, rendimiento e internals. La profundidad debe ser comparable al PATH de C++ del usuario. Un índice extenso no demuestra dominio: cada hito exige código, pruebas y explicación de decisiones.

Los archivos suministran el índice y las instrucciones para generar lecciones; no son las 684 lecciones desarrolladas. Mantener los 32 bloques y su numeración, sin eliminar los temas solicitados.

NumPy, pandas, Polars, Matplotlib y Seaborn tienen PATH propios. Introducir sus conexiones al final, sin convertirlos en dependencias de los laboratorios básicos. Frameworks web, ciencia de datos y aprendizaje automático son especializaciones posteriores.

## Versión y fuentes

Objetivo: Python 3.15. Fecha de preparación: 2026-09-16. La documentación consultada identifica 3.15.0rc2; no presentar la versión final como publicada en esta fecha. Antes de desarrollar o ejecutar material, registrar versión exacta, implementación, sistema y tipo de build. Revisar la documentación 3.15 vigente y las dependencias compatibles. No sustituir el Python que utiliza Fedora para administrar el sistema; utilizar un intérprete y entorno aislados.

La referencia oficial determina firmas, métodos, excepciones y comportamiento. Los libros aportan pedagogía, ejemplos y diseño; no constituyen una referencia normativa de 3.15. Etiquetar la versión de introducción cuando proceda: una característica utilizada en 3.15 no necesariamente apareció en 3.15.

Distinguir garantías de Python de detalles de CPython; marcar bytecode, layouts, GIL, JIT, free-threading, C API y cambios experimentales como dependientes de implementación, versión o build. Verificar las novedades específicas antes de enseñarlas; el bloque 30 organiza esa revisión.

## Progresión y prerrequisitos

0–6: fundamentos y colecciones. 7–10: funciones, iteración, recursos y módulos. 11–15: objetos, protocolos, decoradores, tipos y modelado. 16–21: persistencia e ingeniería profesional. 22–24: concurrencia, asincronía y redes. 25–30: rendimiento, metaprogramación, internals, interoperabilidad, seguridad y evolución. 31: integración y evaluación.

Los ejemplos deben utilizar conceptos ya explicados. Si resulta imprescindible uno posterior, dar una introducción mínima y remitir a su bloque. Introducir pruebas sencillas desde los primeros laboratorios y reservar la estrategia completa para el bloque 19. La interoperabilidad nativa requiere fundamentos de C o C++; proporcionar preparación y no exigirlos en bloques iniciales.

## Estructura obligatoria de cada lección

1. Abrir con «🎯 OBJETIVO»: capacidades concretas y verificables.
2. Indicar prerrequisitos y contexto de uso.
3. Incluir «📚 LECTURA»: Principal, Complementaria/Profundización, Consulta oficial y Python moderno cuando corresponda. No rellenar categorías sin una lectura relevante.
4. Desarrollar el concepto con profundidad, usando encabezados específicos del tema.
5. Mostrar sintaxis general o firma antes de los ejemplos.
6. Explicar cada componente de la sintaxis con texto o tabla.
7. Presentar un ejemplo mínimo ejecutable, la salida esperada y el razonamiento paso a paso.
8. Desarrollar variantes, casos límite y un ejemplo aplicado.
9. Incluir «⚠️ ERRORES FRECUENTES» con código incorrecto identificado, causa y corrección.
10. Incluir «🧪 LABORATORIO / EJERCICIOS» con objetivos, entradas y criterios de aceptación. Añadir solución razonada separada para autoevaluación.
11. Añadir «💡 IDEA IMPORTANTE» cuando aporte una distinción útil.
12. Incluir referencias bibliográficas específicas verificadas antes del cierre.
13. Cerrar con «🧠 QUÉ DEBES RECORDAR»: entre 3 y 7 ideas concretas, sin repetir el objetivo.

No usar una plantilla superficial con texto intercambiable. Explicar por qué el resultado se produce, no solo mostrar código. No imponer un límite artificial que suprima variantes necesarias.

## Contrato de sintaxis, gramática y ejemplos

Para una construcción como if, mostrar primero una forma general:

```python
if condicion:
    instrucciones
```

Aclarar que los nombres anteriores son marcadores. Cuando ayude, incluir la gramática formal de la referencia y explicar terminales, alternativas, repeticiones y elementos opcionales; no presentar gramática como código ejecutable. Una condición se evalúa por su valor de verdad, no por identidad con True.

Ejemplo mínimo completo:

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
print("Fin del programa")
```

Salida:

```text
Eres mayor de edad
Fin del programa
```

Explicar comparación, selección del bloque y continuación. Añadir un caso falso. Seguir el mismo criterio para elif, bucles, funciones, métodos, clases, decoradores y asincronía.

Los ejemplos deben contener imports, datos e instrucciones de ejecución necesarios. Separar código correcto de demostraciones de error. Identificar resultados aproximados, aleatorios o dependientes de plataforma. No prometer un orden de conjuntos o finalización concurrente. Emplear servicios locales simulados y fixtures para evitar credenciales, pagos y red obligatoria.

## Cobertura exhaustiva de métodos solicitados

Cubrir todos los métodos públicos documentados de str, list, dict, set, frozenset y tuple. El índice dedica una lección explícita a cada uno de los 96 métodos del inventario inicial; cotejarlo contra la referencia de la versión exacta al generar el curso y documentar incorporaciones sin omitirlas. Distinguir métodos públicos específicos, métodos heredados y métodos especiales; estos últimos se desarrollan en el modelo de datos.

Para cada método explicar: firma y valores por defecto; parámetros posicionales y por nombre; tipo y valor de retorno; mutación o creación de resultado; complejidad cuando esté justificada; ejemplos básico y aplicado; colección vacía, elemento ausente u otros límites relevantes; excepciones; comparación con alternativas; ejercicio y solución.

No confundir métodos con funciones incorporadas u operadores. Cubrir también len, sorted, reversed, enumerate, zip, all, any, min, max, sum; indexación, slicing, pertenencia, operadores y comprensiones. Contrastar sort/sorted, append/extend, remove/pop, get/corchetes/setdefault, strip/removeprefix, find/index, discard/remove, copy/deepcopy y tuple/frozenset.

En texto incluir Unicode y cada método de clasificación; no reducir isdecimal, isdigit e isnumeric a sinónimos. En listas explicar retornos None de métodos mutadores. En dict, vistas dinámicas y orden de inserción. En sets, no indexación y ausencia de orden garantizado. En tuplas, inmutabilidad de la estructura frente a elementos mutables.

Cubrir además métodos públicos documentados de los tipos numéricos y binarios en sus respectivas lecciones, con tabla de referencia.

## Funciones, objetos y herramientas avanzadas

Obligatorio: parámetros/argumentos; defaults y su evaluación; /, *, *args, **kwargs; desempaquetado al llamar; retornos; mutación frente a reasignación; LEGB, global, nonlocal; closures y captura tardía; lambda y recursión. No describir Python como paso por referencia equivalente a C++.

Incluir herencia simple y múltiple, MRO, super cooperativo, composición, polimorfismo, ABC, property, getter/setter/deleter, classmethod y staticmethod. Explicar por qué no se necesitan getters/setters mecánicos para todos los atributos.

Desarrollar decoradores simples, parametrizados, apilados, de métodos, clases y corutinas; preservar retorno, firma observable cuando proceda y metadatos. Cubrir functools, operator e itertools completo, además de generadores y protocolos.

## Concurrencia y asincronía

Distinguir concurrencia, paralelismo, I/O-bound y CPU-bound. Enseñar hilos, procesos, futures, sincronización, comunicación, carreras, deadlocks y cierre. Indicar método de arranque de procesos y necesidad de proteger el punto de entrada.

Para asyncio mostrar async def, await, asyncio.run, tareas, TaskGroup, gather, timeouts, cancelación, excepciones agrupadas, colas, backpressure, semáforos, contextvars, async for y async with. Contrastar awaits secuenciales con tareas concurrentes. No afirmar que async acelera cálculos por sí mismo. No bloquear el event loop con time.sleep ni llamadas síncronas largas. No silenciar cancelaciones de manera indiscriminada.

Comparar builds con GIL y sin GIL sin asumir que desaparecerán las carreras o que cualquier extensión será compatible. Medir rendimiento y no inventar tiempos exactos.

## Hitos y evaluación

| Hito | Evidencia mínima |
| --- | --- |
| Fundamentos | Gestor de inventario con validación, funciones, colecciones y casos límite |
| Lenguaje | Biblioteca con protocolos, iteradores/generadores y contratos explicados |
| Profesional | Paquete instalable con tipos, pruebas, documentación y CI |
| Avanzado | Cliente concurrente con límites, timeouts, cancelación y cierre comprobable |
| Experto | Generador de cursos modular, reanudable, medido y documentado |

Rúbrica: corrección 30 %, pruebas y fallos 20 %, diseño 20 %, explicación técnica 15 %, reproducibilidad y documentación 15 %. Exigir al menos 80 % y ausencia de fallos críticos en pérdida de datos, seguridad o cierre de recursos. Es un criterio pedagógico, no una certificación oficial.

## Integración con course-generator

Colocar estos archivos juntos en paths/python/. El initial.txt empieza directamente por el bloque 0, contiene una línea por bloque/lección y no incluye un título suelto anterior. Conservar nombres y saltos de línea UTF-8.

profile.yml sigue las claves del perfil existente consultado; files.bibliography apunta deliberadamente a bibliografy.md, tal como pidió el usuario. files.pedagogy referencia ../../config/pedagogy.md, archivo compartido ya perteneciente al proyecto: no se incluye ni se sobrescribe aquí.

La extensión solicitada es .yml. Si el cargador local solo busca profile.yaml, renombrar profile.yml a profile.yaml sin modificar su contenido. Verificar esa resolución con el cargador real. No se ha ejecutado course-generator desde este entorno ni se dispone de su código; validación.enabled: false no equivale a pruebas aprobadas. Las reglas pedagógicas específicas residen en este domain.md para que se incorporen como contexto del generador.

Comprobación local sugerida, una vez registrado el perfil python:

```bash
uv run course-generator paths/python/initial.txt --profile python --split-blocks --check-lessons --dry-run
```

La validación de entrega comprueba sintaxis YAML, numeración continua, referencias locales e inventario de métodos; la integración final corresponde al comando anterior en el proyecto del usuario.
