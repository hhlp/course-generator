# OpenTelemetry con Go — dominio y contrato de generación

## Propósito y relación con los demás PATH

Especialización independiente de 0 a experto en instrumentación de aplicaciones
Go. «Cero» significa sin conocimientos previos de OpenTelemetry con Go; se
requieren módulos, interfaces, errores, HTTP, goroutines y fundamentos de Go.
El bloque 0 comprueba estos requisitos sin convertirse en un curso de Go.

El PATH común OpenTelemetry en profundidad aporta especificaciones, señales,
OTLP, Collector, OTTL, seguridad y operación de la plataforma. Se puede estudiar
en paralelo por necesidad: no es obligatorio completar sus 184 bloques antes
de empezar esta especialización. Aquí se explican los fundamentos mínimos y
se profundiza en las decisiones concretas del SDK y del código Go.

Esta ruta es hermana de OpenTelemetry con Python, C++, JavaScript y Java.
No exige estudiar esos lenguajes ni repetir sus laboratorios. No modifica el
PATH común ni convierte Go en su lenguaje obligatorio. El desarrollo de
componentes Collector utiliza Go, pero tiene una finalidad distinta a
instrumentar aplicaciones; su bloque 37 es una ampliación opcional.

## Secuencia y niveles

| Bloques | Etapa | Resultado |
| --- | --- | --- |
| 0–3 | Fundamentos y primer circuito | Servicio local identificable y bootstrap correcto |
| 4–12 | Trazas e integración | Contexto correcto en HTTP, RPC, workers, SQL y mensajes |
| 13–18 | Métricas y logs | Instrumentos adecuados y correlación entre señales |
| 19–21 | Exportación y ciclo de vida | Transporte, cierre y sampling razonados |
| 22–23 | Pruebas | Contratos verificables sin depender de un backend externo |
| 24–28 | Operación y coste | Collector, SLOs, privacidad, overhead y diagnóstico |
| 29–33 | Modalidades y despliegue | Frameworks, zero-code, batch, Linux y Kubernetes |
| 34–38 | Experto y mantenimiento | Runbooks, bibliotecas, extensiones y migraciones |
| 39 | Proyecto experto | Sistema reproducible con evidencias de aceptación |

Seguir 0–39 como orden principal. Los bloques 9, 11 y 12 proporcionan casos
especializados; el proyecto requiere HTTP, un RPC, un worker y persistencia.
Se elige un framework y un broker, sin repetir obligatoriamente todos los
productos. Kubernetes requiere fundamentos previos de Kubernetes; su alternativa
local permite completar el núcleo con procesos o contenedores. La extensión de
Collector del bloque 37 no es requisito para instrumentar correctamente Go.

## Estándar pedagógico obligatorio

Cada lección empieza con `🎯 OBJETIVO` y termina con
`🧠 QUÉ DEBES RECORDAR` con 3–7 ideas esenciales. Incorporar
`🧪 Laboratorio/ejemplos`, `⚠️ Errores frecuentes` y `💡 Idea importante`
cuando aporten valor. Desarrollar explicaciones completas, progresivas y
profundas. No sustituir los mecanismos específicos por párrafos intercambiables.

En cada tema explicar entradas, estado, ciclo de vida, salidas, invariantes,
concurrencia, límites, errores, evidencia y alternativas pertinentes. No inventar
configuración para conceptos abstractos. Mostrar código completo compilable
cuando el ejercicio lo requiera, imports y archivos relacionados incluidos.
Distinguir comportamiento normativo de la especificación, implementación del
SDK Go y decisiones elegidas para el laboratorio.

## Contrato de cada laboratorio generado

1. Objetivo observable, requisitos y relación con la lección.
2. Versiones exactas de toolchain, módulos, Collector, imagen y backend usados;
   fijar tags o digests y conservar go.mod/go.sum. No usar latest como resultado
   final ni forzar versiones iguales a módulos con ciclos distintos.
3. Árbol de archivos, código completo y configuración. Distinguir aplicación,
   Collector y backend; incluir un mecanismo de arranque y parada documentado.
4. Comandos desde un directorio conocido, variables descritas y secretos señuelo.
5. Comprobaciones previas y comandos de ejecución; carga y duración controladas.
6. Resultado esperado y procedimiento de observación. Separar expectativa de
   evidencia medida; no inventar trace IDs, capturas, tasas o benchmarks reales.
7. Prueba negativa vinculada al mecanismo del bloque y diagnóstico por capas.
8. Remedio y repetición de la comprobación que demuestre la corrección.
9. Limpieza y explicación de datos persistentes o procesos retenidos.
10. Limitaciones, privacidad y coste del experimento.

La base es local, sin exposición pública: aplicación en localhost y receptores
publicados solo en loopback. En red interna de contenedores se permite la escucha
que necesite la conectividad, distinguiéndola del puerto publicado del host.
No desactivar SELinux ni firewalld para ocultar un fallo de configuración.

Los archivos de este paquete son entradas curriculares. No incluyen todavía
fuentes Go de los laboratorios, imágenes, manifests desplegados o mediciones
reales. El generador deberá producirlos al desarrollar las lecciones y verificar
su ejecución por separado.

## Arquitectura práctica progresiva

Comenzar por stdout para aislar el SDK; pasar enseguida a Go → OTLP → Collector
→ backend. Añadir un segundo servicio HTTP, un RPC, persistencia y worker según
la etapa. PostgreSQL y un broker local son dependencias del laboratorio, no
cursos de administración. Usar Jaeger o Tempo para trazas, Prometheus para
métricas y un backend de logs compatible cuando corresponda. Grafana consulta
los datasources configurados; no se presupone un endpoint OTLP universal de
Grafana OSS. Los backends adicionales se eligen por necesidad y compatibilidad.

El proyecto puede ejecutarse sin un clúster público. En Fedora/RHEL distinguir
configuración nativa systemd de contenedores Podman/Docker. Para Kubernetes,
incluir recursos, permisos, secretos y políticas necesarios para ese escenario.

## Reglas técnicas que el generador debe respetar

- Una goroutine no hereda context.Context por sí sola. Pasar explícitamente el
  contexto adecuado y justificar el desacoplamiento; no usar Background para
  reparar un flujo roto. El contexto de shutdown debe tener plazo propio cuando
  el de señal o petición ya está cancelado.
- RecordError y SetStatus son acciones distintas. Tratar el error de negocio y
  el error del exporter en rutas separadas. Evitar bucles al instrumentar las
  conexiones del propio exporter o al registrar sus errores con el mismo bridge.
- Las bibliotecas dependen de API y reciben proveedores; la aplicación posee
  SDK y ciclo de vida. No instalar un SDK global desde una biblioteca reutilizable.
- No crear un proveedor por petición. Reutilizar clientes e instrumentos y
  cerrar bodies, streams, filas y callbacks según su contrato.
- Normalizar rutas, nombres de span y dimensiones. TraceID, user ID y valores
  de consultas no son etiquetas de métricas por defecto. Baggage no se convierte
  automáticamente en atributos y cruza fronteras de confianza.
- Distinguir un span no grabado, uno no muestreado y uno no exportado. Tail
  sampling no reconstruye spans descartados en el origen. Las tasas de negocio
  se calculan con métricas adecuadas y no con una muestra sesgada de trazas.
- Distinguir Counter, UpDownCounter, Gauge e Histogram y sus variantes
  disponibles; explicar Views, agregación, temporality, histogramas y exemplars.
  Asegurar unicidad del escritor y evitar doble ingestión al mezclar OTLP y scrape.
- Usar slog como API de logging de la aplicación y otelslog como bridge cuando
  proceda. Comparar forwarding de stdout y SDK de logs directo; evitar duplicados.
  La correlación depende del contexto aportado y del backend configurado.
- En HTTP, revisar semántica del body cliente, streaming y capacidades del
  ResponseWriter. En gRPC, utilizar la API vigente del paquete seleccionado;
  no copiar interceptores retirados sin verificar compatibilidad.
- Las variables OTEL, configuración declarativa y precedencia no son uniformes
  por definición entre lenguajes. Documentar soporte concreto de Go y la opción
  de código correspondiente en cada versión usada.
- Separar pprof/runtime trace de trazas distribuidas y de OTLP Profiles.
  Tratar integración de perfiles como dependiente de soporte real, sin afirmar
  madurez general del SDK Go por analogía con traces o metrics.
- OBI, otelc, instrumentación manual y wrappers son mecanismos diferentes.
  Verificar señales, dependencias, arquitectura, kernel, toolchain y permisos.
  Auto SDK requiere una integración compatible; no combinar proveedores de
  manera improvisada ni trasladar instrucciones de agentes de Java o Python.
- Resiliencia significa colas acotadas, retries y pérdidas/duplicados posibles.
  ForceFlush o Shutdown exitoso no prueba almacenamiento definitivo del backend.

## Estado de versiones y fuentes

Consulta documental de diseño: 2026-10-22. La página general de Go presenta
traces y metrics como estables y logs como release candidate. Algunas páginas
de instrumentación y comienzo aún etiquetan partes de logging como experimental.
Esta diferencia debe quedar visible: la etiqueta de una página general no prueba
la estabilidad de cada módulo, bridge o API. Antes de generar código, revisar
releases, go.mod y documentación de los tags elegidos, especialmente sdk/log,
exporters de logs, otelslog, Auto SDK y herramientas zero-code.

No se fija aquí una combinación de versiones supuestamente probada: este es un
currículo. En cada laboratorio generado se debe resolver y registrar una matriz
exacta que realmente compile. El módulo semconv versionado también se alinea con
la instrumentación y consultas elegidas. bibliography.md reúne fuentes de
consulta y referencias adicionales, diferenciando su papel.

## Pruebas, validación y evidencias

Las pruebas de aplicación incluyen context propagation, relaciones parent-child,
links, nombres, status, atributos, métricas conocidas y LogRecords. Preferir
proveedores por prueba, tracetest, ManualReader y receptores locales a sleeps
arbitrarios o aserciones sobre tiempos e IDs exactos. Probar el comportamiento
no-op y conservar semántica de negocio. Race detector y benchmarks apoyan el
análisis; no prueban por sí solos ausencia de todos los defectos de concurrencia.

Los checks de este paquete solo verifican estructura curricular, numeración,
YAML, enlaces internos y archivo ZIP. No equivalen a ejecutar los laboratorios,
validar el esquema privado de course-generator ni certificar compatibilidad de
código que todavía no se ha generado.

## Matriz de prácticas y evidencias mínimas

Las lecciones .9 y .10 de cada bloque son la práctica y el fallo deliberado.
La siguiente evidencia se desarrolla con comandos y aserciones en las lecciones.

| Bloque | Práctica | Evidencia de aceptación |
| --- | --- | --- |
| 0 | Preparar repositorio y ejecutar un servicio HTTP local sin instrumentación | Compilar el servicio y registrar códigos HTTP y latencias de referencia |
| 1 | Levantar el primer circuito Go a Collector con configuración completa | Observar service.name y el mismo trace ID emitido por la aplicación |
| 2 | Construir internal/telemetry con proveedores inyectables y limpieza | Comprobar emisión con proveedor real y ausencia controlada con no-op |
| 3 | Distinguir dos servicios Go y dos instancias en el mismo backend | Verificar agrupación por servicio y explicar los conflictos detectados |
| 4 | Construir una cadena handler a servicio a repositorio con spans hijos | Demostrar un trace ID común y relaciones parent-child correctas |
| 5 | Instrumentar una operación con errores envueltos y un panic recuperado | Verificar eventos de error, status esperado y spans finalizados |
| 6 | Conectar dos servicios y transportar un atributo Baggage permitido | Confirmar continuidad válida y creación segura de una nueva raíz |
| 7 | Instrumentar endpoints de éxito, error y streaming en net/http | Validar nombres estables y funcionamiento de streaming y cancelación |
| 8 | Conectar frontend y backend con cliente HTTP instrumentado | Observar spans cliente-servidor y explicar el recurso retenido |
| 9 | Construir un RPC unary y otro streaming entre servicios Go | Validar continuidad del RPC, códigos de estado y cierre de spans |
| 10 | Implementar fan-out y un pool cancelable con trazas causales | Comprobar relaciones, drenaje del pool y ausencia de carreras detectadas |
| 11 | Instrumentar PostgreSQL y una caché en una operación de negocio | Diferenciar espera de pool, consulta y caché mediante evidencias |
| 12 | Implementar productor y consumidor en un broker local elegido | Distinguir intentos y correlación sin prometer entrega exactamente una vez |
| 13 | Añadir peticiones, operaciones activas y latencia a un servicio | Verificar conteos conocidos, equilibrio de activos y unidad de duración |
| 14 | Correlacionar carga y presión de memoria con métricas del runtime | Mostrar variación del heap y tiempo de colección con límites explícitos |
| 15 | Comparar dos vistas sobre una distribución de latencia controlada | Reducir series con una View sin perder la pregunta operativa |
| 16 | Publicar métricas de Go y consultar sus series en Prometheus | Explicar conteos y resets con una única ruta activa por serie |
| 17 | Emitir logs de una petición mediante slog y el bridge seleccionado | Comparar logs con y sin trace ID y validar Resource y severidad |
| 18 | Reconstruir una petición lenta desde métrica a traza y log | Contar duplicados y explicar enlaces que carecen de traza retenida |
| 19 | Comparar envío HTTP y gRPC usando el mismo servicio Go | Diagnosticar cada fallo con logs internos y recepción en Collector |
| 20 | Apagar un servicio con tráfico y drenar los tres proveedores | Comparar spans y logs recibidos antes y después de corregir el cierre |
| 21 | Comparar head sampling con retención de errores por tail sampling | Justificar tasas observadas sin afirmar recuperación de spans descartados |
| 22 | Construir pruebas deterministas de una operación HTTP instrumentada | Detectar la regresión mediante relaciones y atributos significativos |
| 23 | Validar un flujo de negocio con trazas, métricas y logs | Conseguir pruebas que fallen por cambios semánticos y pasen al corregirlos |
| 24 | Integrar tres señales de Go con Collector y backend local | Cuantificar recibidos, descartados y duplicados posibles durante la recuperación |
| 25 | Crear un dashboard y un recorrido de diagnóstico de un incidente | Demostrar un SLI calculado desde contadores y una traza explicativa |
| 26 | Auditar una petición con datos señuelo y exportación autenticada | Verificar ausencia del secreto y rechazo o aislamiento del tenant |
| 27 | Comparar no-op, SDK local y OTLP bajo la misma carga | Presentar mediciones repetidas de latencia, memoria y pérdidas |
| 28 | Diagnosticar una degradación con spans, heap y perfil CPU | Identificar las funciones responsables y conservar perfiles como evidencias |
| 29 | Comparar net/http con un framework en el mismo contrato HTTP | Demostrar una sola capa de span servidor y continuidad del contexto |
| 30 | Comparar una aplicación manual con una modalidad zero-code compatible | Conservar matriz de soporte y evidencias de continuidad del trace ID |
| 31 | Instrumentar un comando y ejecutarlo mediante un timer systemd | Conservar código de salida, último log y resultado del span raíz |
| 32 | Desplegar la aplicación Go y Collector en un entorno local Fedora | Restablecer envío con permisos y certificados mínimos necesarios |
| 33 | Desplegar dos réplicas Go y ejecutar un rolling update con tráfico | Medir diferencias de cierre y continuidad de servicio durante el rollout |
| 34 | Resolver un incidente ciego con fallos de contexto, exportación y backend | Entregar una cronología con pruebas que descarten hipótesis alternativas |
| 35 | Publicar localmente un módulo Go con instrumentación opcional | Comprobar aislamiento, no-op funcional y contrato estable de spans |
| 36 | Implementar un SpanProcessor pequeño con pruebas de carrera | Demostrar corrección funcional y coste dentro del presupuesto definido |
| 37 | Construir y probar un processor local con OCB | Ejecutar pruebas de componente y documentar por qué OTTL no bastaba |
| 38 | Migrar una dependencia y comparar contratos antes y después | Detectar la regresión y diseñar transición y rollback verificables |
| 39 | Construir el sistema y ejecutar su plan de aceptación completo | Entregar repositorio reproducible, informe de pruebas y diagnóstico defendible |

## Proyecto experto: aceptación

El repositorio final debe contener fuentes Go, go.mod/go.sum, configuración
Collector y backends, un arranque local documentado, carga sintética, dashboards,
pruebas, runbooks y limpieza. Un escenario combina API HTTP, RPC, worker, SQL y
un error deliberado. Identificar dependencias opcionales y requisitos de host.

- Verificar continuidad HTTP/RPC y el contrato parent o link en mensajería.
- Ejecutar una carga conocida y contrastar contadores, histograma y operaciones
  activas. Definir tolerancias por ventanas de exportación, no números ficticios.
- Vincular al menos un log con su span; explicar referencias a trazas descartadas.
- Probar error de negocio, timeout, cancelación y SIGTERM con tráfico activo.
- Interrumpir Collector/backend, observar colas y justificar pérdidas y duplicados.
- Ensayar cardinalidad elevada y datos señuelo sensibles con medidas correctoras.
- Comparar baseline y aplicación instrumentada con carga repetible e incertidumbre.
- Ejecutar pruebas de contratos y de integración; documentar fallos pendientes.
- Presentar un incidente reconstruido y una migración/rollback de instrumentación.

El bloque opcional de componentes Collector añade código y pruebas propias, pero
no es necesario crear componentes personalizados para superar este proyecto.
