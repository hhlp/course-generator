# Dominio: OpenTelemetry con Java

Especialización de cero a experto en instrumentación Java. Se estudia por
separado de OpenTelemetry {Python, C++, Go, JavaScript}. No exige cursar esos
lenguajes y no reproduce toda la administración del Collector y los backends.
El tronco común aporta OTLP, modelos de señales, arquitectura del Collector,
semántica, seguridad y operación de la plataforma. Aquí se aplican a la JVM.

## Entrada y progresión

Se requiere Java básico, excepciones, herramientas de compilación y HTTP.
El bloque 0 ofrece nivelación de OpenTelemetry; no enseña Java desde cero.
Antes de concurrencia se repasan executors y CompletableFuture. Spring,
Reactor, gRPC y Kafka se introducen con el contexto mínimo para cada práctica.

- 0–5: entorno, laboratorio, agente, configuración y SDK.
- 6–9: spans, propagación, concurrencia y HTTP.
- 10–16: Spring MVC, Starter, Reactor, gRPC, JDBC y mensajería.
- 17–23: métricas, JVM/JMX, logs, transporte, sampling y contratos.
- 24–28: pruebas, CI, rendimiento, Linux, contenedores y Kubernetes.
- 29–31: diagnóstico, extensiones y proyecto experto.

El recorrido completo contiene 32 bloques y 320 lecciones. Kubernetes requiere
sus propios fundamentos; puede posponerse mientras se termina el proyecto
local. Quarkus/native image y otros clientes de datos son variantes avanzadas,
no prerrequisitos para dominar Spring Boot y la instrumentación Java normal.

## Contrato de cada lección generada

Abrir con 🎯 OBJETIVO y cerrar con 🧠 QUÉ DEBES RECORDAR, con 3–7 ideas.
Desarrollar mecanismo, motivación, comportamiento, código comentado, ejecución,
resultado esperado, errores frecuentes y criterios de elección. Evitar una
lista de definiciones sin explicación. Los talleres .9 integran el bloque;
las evaluaciones .10 exigen diagnosticar un fallo sin repetir el taller.

En cada laboratorio generado deben entregarse todos los archivos necesarios,
su árbol de directorios, comandos de compilación/arranque, configuración,
comprobaciones, evidencia esperada, prueba negativa, recuperación y limpieza.
Usar datos sintéticos. Una captura visual no sustituye un assert semántico.
No prometer cero pérdidas, overhead nulo ni entrega exactamente una vez.

## Elección del modo de instrumentación

Comenzar con el agente para observar los bordes de una aplicación existente.
Añadir API manual para operaciones de negocio y aprender SDK propio en una
aplicación sin agente. Comparar el Starter en un escenario independiente.
Identificar siempre quién crea y cierra el SDK. Evitar instalar dos SDK por
combinar agente, Starter y configuración manual sin una razón verificada.
Las bibliotecas reutilizables dependen de API y aceptan la instancia del host.

La disponibilidad de trazas, métricas y logs del núcleo no implica que cada
appender, bridge, convención o integración tenga la misma estabilidad.
Para cada integración se consulta su matriz real de versiones y se distingue
instrumentación automática, biblioteca independiente e integración nativa.

## Reproducibilidad y compatibilidad

Fijar JDK, SDK BOM, instrumentation BOM, agente, framework, Collector e imágenes.
No deducir compatibilidad porque coincidan números de versión entre proyectos.
Registrar checksums y comandos de diagnóstico. Elegir el protocolo OTLP de
forma explícita; no asumir el mismo valor por defecto para todos los modos.
Verificar precedencia de configuración y madurez de configuración declarativa
contra las releases elegidas. Evitar copiar opciones obsoletas de libros.

## Arquitectura de laboratorio

Progresar de aplicación → Collector/debug a servicios HTTP, PostgreSQL/JDBC,
Kafka y backends visuales. Ruta principal Docker Compose, con alternativa
Podman Compose validada en el entorno. Publicar interfaces de usuario solo
en loopback; entre contenedores utilizar DNS interno. El backend de trazas
puede ser Jaeger o Tempo; Prometheus y Grafana cubren métricas. Para logs,
elegir un backend compatible y documentar el transporte y su consulta.
No exigir simultáneamente todos los productos del tronco común.

Diferenciar correlación MDC de exportación de logs; no crear dos rutas de
captura para el mismo evento sin deduplicación. El sampling de trazas no
elimina automáticamente métricas ni logs. Tail sampling no recupera spans
que el SDK ya descartó. Cerrar Scope y spans en el momento correcto, incluso
con tareas asíncronas, cancelación y procesamiento reactivo.

## Evaluación y proyecto

Demostrar árbol y causalidad de trazas, aislamiento del contexto concurrente,
atributos permitidos, unidades de métricas, series acotadas y logs asociados.
Medir CPU, memoria, GC, throughput y percentiles bajo carga comparable.
Verificar fallos de dependencias, OTLP, TLS y cierre de proceso.

El proyecto final integra pedidos, pagos e inventario, persistencia JDBC y
procesamiento Kafka. Debe aportar código reproducible, pruebas de regresión,
matriz de versiones, dashboards/consultas, runbooks, medidas de overhead y
plan de actualización/rollback. La entrega se considera válida cuando otra
persona puede reproducir los incidentes y justificar su diagnóstico.

## Alcance de este paquete

Contiene el currículo y las reglas para generar el curso: initial.txt,
domain.md, profile.yaml y bibliography.md. No contiene todavía el código de
las aplicaciones, Dockerfiles, manifests, dashboards ni scripts ejecutables
de los laboratorios. Esos son entregables exigidos a las lecciones generadas.
La configuración YAML es válida sintácticamente; su aceptación por una versión
concreta de course-generator requiere validar el esquema de esa versión.
