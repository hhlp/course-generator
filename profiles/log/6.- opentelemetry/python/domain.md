# OpenTelemetry + Python — dominio y contrato de generación

## Identidad y relación con otros PATH

Especialización independiente de 0 a experto en instrumentación de aplicaciones
Python. «Cero» significa cero experiencia con OpenTelemetry Python: se requieren
funciones, clases, excepciones, módulos y dependencias de Python, además de Linux
básico. asyncio y concurrencia se introducen en su contexto antes de instrumentarlas.
No sustituye al PATH de Python ni exige completar previamente todo OpenTelemetry.

El PATH general es referencia para fundamentos comunes, especificación, Collector,
OTTL, seguridad y operación de la plataforma. Aquí se incluye el repaso necesario
para recorrer una aplicación de extremo a extremo sin obligar a cursar sus 184
bloques. Remitir por tema, sin inventar identificadores de otro itinerario.

OpenTelemetry + C++, Go, Java y JavaScript serán especializaciones separadas.
Este itinerario solo exige código Python; no incluye implementación del Collector
en Go. Su configuración YAML es infraestructura auxiliar del laboratorio.

## Alcance y progresión

Desarrollar íntegramente las lecciones de initial.txt, sin fusionar temas ni
sustituirlos por resúmenes. Primero entorno y circuito local; después trazas,
propagación e instrumentación web; métricas y logs; concurrencia y tareas;
pruebas, operación, extensiones y proyecto experto. No introducir Flask, Django
y FastAPI como dependencias simultáneas: son variantes de laboratorio.

Distinguir API, SDK, instrumentor, exporter, protocolo OTLP, Collector y backend.
La aplicación configura el SDK; una biblioteca reutilizable depende de la API y
no fuerza un backend ni reconfigura providers globales de su consumidor.

## Estructura de las lecciones

Cada lección abre con 🎯 OBJETIVO y termina con 🧠 QUÉ DEBES RECORDAR, con 3–7
ideas. Desarrollar explicación, mecanismos, ejemplos Python completos y criterios
de verificación. Usar 🧪 Laboratorio/ejemplos, ⚠️ Errores frecuentes y 💡 Idea
importante cuando aporten valor. Explicar entradas, estado, salidas y límites
propios de cada tema. No repetir párrafos genéricos ni exigir un despliegue para
una lección de análisis. Incluir prerequisitos y referencias puntuales.

## Versiones y precisión técnica

Consulta de referencia: 2026-10-22. No se fija una versión universal ficticia.
Antes de generar un laboratorio ejecutable, registrar en su README: Python,
API/SDK/exporters, contrib, frameworks, Collector y backend; consultar metadatos
Requires-Python, restricciones de dependencias y changelogs. Fijar las versiones
compatibles reales y producir un lockfile o requirements con resolución comprobada.
No utilizar latest en imágenes ni tomar salidas antiguas como versión recomendada.

Verificar por componente y versión la estabilidad de trazas, métricas y logs.
Las APIs de logs, configuración declarativa, histogramas exponenciales, exemplars,
instrumentaciones y convenciones pueden cambiar de forma independiente. No
prometer compatibilidad por aparecer un paquete en el catálogo. Explicar el uso
de imports con guion bajo solo si el upstream los documenta para la versión,
identificando el riesgo de evolución. No extrapolar el soporte de otro lenguaje.

Distinguir propagación de contexto de transporte de baggage y de identidad de
recurso. Baggage no se convierte automáticamente en atributo de span. Una excepción
registrada y el estado ERROR son conceptos distintos. Verificar defaults y
opciones del context manager antes de afirmar comportamiento automático.

En métricas, explicar temporality, agregación, identidad de escritores, resets y
cardinalidad. No agregar histogramas ni contadores de workers sin analizar sus
recursos y semántica. La correlación mediante exemplars depende del soporte real.

En logs, separar: inyección de campos de contexto, formato de logging y envío OTLP.
La presencia de trace_id en stdout no demuestra exportación. Revisar handlers,
propagate y rutas de ingestión para impedir duplicados. No suponer que la CLI
habilita cada señal de igual manera en todas las versiones.

En concurrencia, mostrar contexto capturado al crear tareas y verificar límites de
hilos y procesos. No asumir propagación automática por ThreadPoolExecutor o IPC.
En prefork, configurar componentes del SDK después de fork según guía upstream
y hooks del servidor; no compartir ciegamente threads, locks o readers heredados.
Probar SIGTERM, cancelación y cierre acotado. Flush no implica durabilidad del
backend ni entrega exactamente una vez.

## Laboratorio progresivo y variantes

Base local sin exposición pública: aplicación Python, Collector y backend de
trazas Jaeger. Introducir Prometheus para métricas y Loki para logs cuando se
necesiten; Grafana consulta los backends. Al inicio, consola/debug permite aislar
cada señal. Tempo sustituye a Jaeger en una variante. No desplegar todos los
backends a la vez. Comprobar consultas y APIs del backend seleccionado.

Aplicación de referencia: API de pedidos sintéticos en FastAPI, cliente HTTP,
PostgreSQL, Redis y worker de tareas. Flask y Django tienen prácticas separadas.
Elegir una biblioteca de mensajería y versión con instrumentación compatible;
si no existe soporte, desarrollar propagación e instrumentación manual sin
presentarlas como una integración automática upstream.

Sistema principal Fedora/RHEL. Contenedores con Podman; ofrecer equivalentes
Docker donde sean necesarios. Kubernetes es una variante avanzada que requiere
conocimientos básicos del orquestador. No convertir este PATH en un curso general
de Kubernetes, bases de datos o administración del Collector.

Cada laboratorio desarrollado debe entregar código, estructura de directorios,
configuración, dependencias fijadas, comandos completos, datos de prueba,
resultados esperados, comprobaciones automáticas apropiadas y limpieza. Usar
unidades systemd, Containerfile o manifiestos cuando corresponda. Incluir TLS y
credenciales sintéticas en el bloque de seguridad, sin publicar secretos.

## Pruebas y aceptación

- Spans: nombres, parentesco, links, SpanKind, errores y contexto remoto.
- Métricas: unidades, dimensiones, agregaciones, resets y límites de series.
- Logs: contexto dentro y fuera de un span, severidad y ausencia de duplicados.
- Concurrencia: usuarios simultáneos sin mezcla de contexto; workers identificables.
- Exportación: caída del Collector, timeouts, colas llenas y reinicio del destino.
- Cierre: proceso corto, cancelación y SIGTERM con comprobación de pérdida posible.
- Seguridad: ausencia de tokens, parámetros sensibles y PII en las tres señales.
- Rendimiento: baseline, carga comparable, CPU, memoria y latencia con incertidumbre.

Los tests de instrumentación deben usar fixtures y exporters/lectores de prueba
compatibles; evitar reutilizar providers globales entre pruebas. Verificar tiempos
con polling acotado, no con sleeps arbitrarios. No afirmar resultados medidos si
solo se ha escrito la prueba. En CI separar tests locales de integración que
requieren contenedores. Mostrar diferencias entre resultados esperados y reales.

El proyecto final entrega repositorio reproducible, diagrama, decisiones,
lockfiles, pruebas, consultas, dashboard/alertas cuando procedan, runbooks,
mediciones, limitaciones y procedimiento de actualización/rollback.

## Naturaleza de esta entrega

Estos cuatro archivos son el currículo y las instrucciones para generar el curso.
No son un laboratorio desplegado ni incluyen las implementaciones futuras de las
lecciones. La validación adjunta comprueba estructura y coherencia estática, no la
compatibilidad en ejecución de paquetes que todavía no se han seleccionado.
