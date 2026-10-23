# OpenTelemetry con JavaScript: dominio y contrato del curso

## Propósito y relación con el path general

Especialización independiente de 36 bloques y 360 lecciones. Enseña a implementar,
comprobar y operar instrumentación en aplicaciones JavaScript, desde el primer
span hasta el diagnóstico de sistemas distribuidos. «Desde cero» significa cero
experiencia en OpenTelemetry con JavaScript; presupone JavaScript básico.

El path general de OpenTelemetry aporta arquitectura, semántica de las señales,
OTLP, Collector, almacenamiento, muestreo distribuido y operación transversal.
Este path aplica esos conceptos a módulos, asincronía, bibliotecas, runtimes y
ciclo de vida JavaScript. Puede estudiarse después del general o en paralelo,
consultando los fundamentos necesarios antes de cada laboratorio.

OpenTelemetry con Python, C++, Go y Java son especializaciones independientes.
No se exige realizar prácticas en esos lenguajes. El proyecto puede comunicarse
con otros servicios por estándares abiertos sin convertirlo en un curso multilenguaje.

## Prerrequisitos y decisiones de alcance

- JavaScript: funciones, objetos, excepciones, módulos, promesas y async/await.
- Node.js: instalación, npm, scripts, HTTP, variables de entorno y señales.
- Linux: archivos, procesos, permisos, puertos y logs básicos.
- OpenTelemetry general: API/SDK, spans, recursos, métricas, logs y OTLP.

Node.js es el recorrido principal. Los ejemplos obligatorios se ejecutan como
JavaScript. TypeScript complementa tipado y herramientas cuando resulte útil;
si se emplea, la lección conserva una variante JavaScript ejecutable. No se
convierte este currículo en un curso general de JavaScript, TypeScript o frontend.

Los bloques 28–31 desarrollan navegador y frontend como extensión completa.
Requieren fundamentos de HTML, navegación, fetch y políticas del navegador.
Quien estudie solo backend puede completar el proyecto sin frontend y documentar
que su frontera de observabilidad comienza en el servidor HTTP.

Kubernetes y serverless son ampliaciones de despliegue. El laboratorio principal
no requiere nube, cuenta comercial ni clúster Kubernetes. Bun, Deno y runtimes
edge se evalúan según evidencia de compatibilidad, sin asumir equivalencia con Node.js.

## Estado de soporte y reproducibilidad

Consulta de referencia: 22 de octubre de 2026. La página oficial de JavaScript
clasifica trazas y métricas como estables, logs en desarrollo e instrumentación
de navegador experimental. Las lecciones deben comprobar de nuevo el estado
antes de fijar sus ejemplos. Esa clasificación no garantiza la compatibilidad
individual de un plugin ni todas las funciones de un backend.

Fuentes: [estado JavaScript](https://opentelemetry.io/docs/languages/js/),
[SDK y releases](https://github.com/open-telemetry/opentelemetry-js).

Cada laboratorio fijará una matriz con runtime, API, SDK, paquetes experimentales,
plugins contrib, bibliotecas instrumentadas, Collector y backend. Las versiones
de esas familias pueden diferir; no se asignará el mismo número a todos los
paquetes por conveniencia. Conservar package-lock.json y usar npm ci.

En CommonJS y ESM se comprobará el orden de carga. Precargar el SDK y parchear
módulos son problemas relacionados: no se dará por hecho que --import resuelve
por sí solo la auto-instrumentación ESM. Las opciones y hooks se verificarán con
la documentación de la combinación fijada. Los ejemplos no dependerán de una
API antigua copiada de un libro sin contrastarla con upstream.

Los backends también tendrán versiones fijadas. Para OTLP se explicarán protocolo,
ruta, TLS y cabeceras; un puerto abierto no demuestra recepción de una señal.
No se asumirán exemplars, histogramas exponenciales o funciones específicas de
consulta sin verificarlas en SDK, exportador, Collector y almacenamiento.

## Progresión y puntos de control

| Bloques | Resultado verificable |
| --- | --- |
| 0–3 | Entorno, modelo del SDK y arranque CommonJS/ESM reproducibles |
| 4–7 | Servicio con recursos y trazas automáticas y de negocio |
| 8–14 | Contexto y propagación por HTTP, base de datos, mensajes y workers |
| 15–18 | Métricas útiles, runtime y logs correlacionados |
| 19–22 | Muestreo, exportación fiable y stack local consultable |
| 23–25 | Pruebas, troubleshooting y cierre controlado de Node.js |
| 26–27 | Despliegue Kubernetes y serverless según compatibilidad |
| 28–31 | Extensión web: navegador, seguridad, SPA/SSR y RUM |
| 32–34 | Bibliotecas, gobernanza, internals y migraciones |
| 35 | Proyecto experto con incidente y evidencias |

Las extensiones de despliegue pueden posponerse hasta después del proyecto local.
El bloque de bibliotecas requiere dominar contexto, trazas y pruebas. La rama web
requiere conocer primero exportación y políticas de privacidad.

## Profundidad de las lecciones

Cada lección empieza con «🎯 OBJETIVO» y termina con «🧠 QUÉ DEBES RECORDAR»,
con 3–7 ideas concretas. Explica mecanismo, flujo y decisiones antes de presentar
comandos. Incluye ejemplos comentados, errores frecuentes y diagnóstico cuando
corresponda. Una lista de funciones o un resumen de documentación no sustituye
el desarrollo didáctico.

Los temas de contexto deben explicar relación entre span activo, propagación y
ciclo de vida. Registrar una excepción no sustituye decidir el estado del span.
Un span debe cerrarse incluso ante rechazo, timeout o cancelación. En concurrencia
se comprobará que no se mezclan peticiones; entre procesos se transmitirá un
carrier explícito cuando corresponda.

Las métricas deben justificar instrumento, unidad, dimensiones y agregación.
Distinguir contadores, valores instantáneos y distribuciones; evitar etiquetas
con IDs de petición o usuario. El muestreo de trazas no debe eliminar la medida
completa de tasa de solicitudes y errores que necesita un SLO.

Los logs deben distinguir emisión, correlación y transporte. Enriquecer stdout
con IDs no significa exportarlo por OTLP. La lección elegirá una ruta de envío
para cada objetivo y comprobará ausencia de duplicados. Se separa diag del SDK
de los logs de negocio.

La rama navegador no equivale a una plataforma RUM completa. La propagación a la
API y la exportación al receptor tienen políticas distintas. CORS y CSP se
configurarán por separado. No se incluirán credenciales del backend en un bundle
público y no se prometerá entrega garantizada al cerrar una pestaña.

## Contrato obligatorio de laboratorio

Cada práctica generada proporcionará:

1. Objetivo, prerrequisitos, versiones fijadas y árbol de archivos.
2. Código fuente completo, package.json, lockfile y configuración necesaria.
3. Instrucciones de instalación y ejecución desde un directorio limpio.
4. Variables documentadas, permisos y puertos; secretos fuera del repositorio.
5. Carga de prueba determinista y consulta para comprobar el resultado.
6. Evidencia esperada: atributos, relaciones, métrica o log según el objetivo.
7. Una prueba negativa con hipótesis, diagnóstico y recuperación.
8. Limpieza reversible, límites y diferencias de plataforma.

El entorno por defecto es local en Fedora/RHEL o Linux equivalente. Se publica
en loopback y se selecciona Docker Compose o Podman Compose con compatibilidad
comprobada. No se desactiva SELinux ni firewalld como solución genérica. Si un
laboratorio exige un permiso o ajuste, se explica su alcance y reversión.

El stack mínimo contiene aplicación, Collector y backend de trazas; se añaden
métricas y logs cuando lo requiere el objetivo. No se obliga a instalar todos
los backends posibles. Las alternativas no deben introducir configuraciones
incompletas o incompatibles con la versión fijada.

La validación sigue el recorrido emisión → transporte → recepción → almacenamiento
→ consulta. Si falta una señal se comprueba cada frontera. Guardar una captura
sin explicar consulta, carga y expectativas no basta como evidencia.

## Proyecto experto y evaluación

Construir dos APIs Node.js, una base de datos y un worker; añadir frontend si se
sigue la extensión web. El estudiante elige un transporte de mensajería y un
stack de almacenamiento mínimo. El proyecto incluye instrumentación automática,
spans de negocio, métricas de SLO, logs correlacionados y cierre controlado.

Inyectar al menos estos fallos: pérdida de contexto, saturación o timeout de una
dependencia y caída temporal del receptor. Para cada uno, aportar síntoma,
hipótesis, consulta, evidencia, solución y explicación de pérdidas de telemetría.

Entregar código, versiones, configuraciones, scripts de arranque y parada,
pruebas de contrato, paneles o consultas y runbook. Comparar rendimiento con
una referencia sin instrumentación bajo la misma carga y justificar límites
de cardinalidad, privacidad y muestreo.

Criterios: corrección causal, valor operativo de las señales, reproducibilidad,
diagnóstico, costes, privacidad y calidad de la documentación. No se considera
experto un proyecto que solo produce spans sin demostrar su utilidad.

## Archivos de este paquete

initial.txt define el temario numerado; domain.md especifica alcance y contrato;
profile.yaml configura la generación; bibliography.md reúne fuentes y su uso.
Este paquete contiene el diseño formativo. No incluye todavía implementaciones,
lockfiles, contenedores ni scripts ejecutables de los laboratorios descritos.
La referencia ../../config/pedagogy.md pertenece al repositorio course-generator:
si se usa otro árbol, debe adaptarse a su ubicación real.
