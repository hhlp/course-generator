# OpenTelemetry con C++ — dominio y contrato de profundidad

## Propósito y relación con otros paths

Especialización independiente para instrumentar, probar, distribuir y operar
aplicaciones y bibliotecas C++. El nivel inicial es cero en **OpenTelemetry
para C++**; se presupone programación C++ básica. El bloque 1 cubre el puente
necesario de ownership y concurrencia, sin reemplazar el path general de C++.

El curso general de OpenTelemetry aporta el modelo común: señales, contexto,
OTLP, Collector, backends, sampling y convenciones. Este path aplica ese modelo
al SDK de C++ y desarrolla sus dificultades propias: compilación, enlace, ABI,
vida útil, RAII, threads, callbacks y cierre. No exige completar Python, Go,
JavaScript ni Java. Un servicio externo ya preparado puede usarse para probar
interoperabilidad sin estudiar otro lenguaje.

El paquete contiene **34 bloques, 0–33, con 340 lecciones**: diez por bloque.
Cada bloque termina en dos laboratorios específicos; hay 68 laboratorios
curriculares. El bloque 29, Kubernetes, es opcional. La ruta principal tiene
33 bloques y 330 lecciones. El proyecto experto es el bloque 33.

## Qué contiene este paquete

- `initial.txt`: secuencia numerada del currículo.
- `domain.md`: alcance, decisiones, laboratorios y reglas de profundidad.
- `profile.yaml`: perfil pedagógico y catálogo estructurado de lecciones.
- `bibliography.md`: fuentes y función de cada referencia.

Estos archivos sirven para desarrollar las lecciones. **No contienen todavía
los fuentes C++, CMakeLists, Compose ni scripts ejecutables del laboratorio.**
Cada lección práctica deberá entregarlos completos al generarse. Los ejemplos
de resultados serán etiquetados como esperados si no se han ejecutado.

## Orden y prerrequisitos

| Etapa | Bloques | Resultado exigido |
| --- | --- | --- |
| Preparación | 0–4 | Compilación reproducible y separación API/SDK |
| Trazas y contexto | 5–13 | Causalidad correcta en red, workers y ejecución asíncrona |
| Métricas y logs | 14–17 | Tres señales con unidades, dimensiones y correlación |
| Transporte y contratos | 18–21 | OTLP, Collector, esquema y biblioteca reutilizable |
| Calidad y distribución | 22–25 | Pruebas, fallos, overhead y compatibilidad binaria |
| Operación | 26–28 | Cierre, protección de datos y operación Linux |
| Kubernetes opcional | 29 | Aplicar la instrumentación a un despliegue de clúster |
| Consolidación | 30–33 | Diagnóstico, CI, interoperabilidad y proyecto final |

Las coroutines del bloque 9 son una ampliación avanzada: requieren dominar
callbacks y contexto primero. Si la herramienta no permite ejecutarlas, se
completa el caso equivalente con callbacks y se documenta esa limitación; no
se declara haber validado una coroutine que no se ha ejecutado.

Antes de empezar conviene dominar los fundamentos de observabilidad del curso
general. No es necesario terminar su administración experta de Kubernetes ni
sus integraciones con todos los backends.

## Política de versiones y capacidades

Fecha de revisión documental: 22 de octubre de 2026. No se fija una supuesta
«última versión» sin validar sus artefactos. Antes del primer laboratorio
compilable se elige una release oficial de `opentelemetry-cpp`, se fija tag y
commit y se consultan sus instrucciones. El branch `main` es una referencia de
navegación, no una versión reproducible. El mismo criterio se aplica al Collector,
backends, imágenes, dependencias y convenciones semánticas.

Registrar en un manifiesto del laboratorio:

1. SDK: release, commit, URL de origen y opciones de CMake.
2. Compilador, biblioteca estándar, arquitectura, estándar C++ y versión CMake.
3. Dependencias gRPC/protobuf, TLS y HTTP realmente empleadas.
4. Collector y backends: versión e imagen con digest cuando proceda.
5. Convenciones semánticas y schema URL cuando corresponda.
6. Comandos de configuración, construcción, instalación y ejecución.

CMake es la ruta principal; Bazel se estudia como alternativa oficial. C++17
es la elección pedagógica inicial si es compatible con la release escogida;
C++20 se usa en los ejercicios de coroutines. No confundir esta elección con
el mínimo oficial de una versión concreta del SDK.

La documentación oficial consultada clasifica trazas, métricas y logs como
estables. Esa clasificación no demuestra que toda función de una especificación,
convención o integración esté implementada en una release concreta. Antes de
usarlas, verificar en documentación, headers y tests de esa release:

- Variables `OTEL_*`, precedencia y objetos que las interpretan.
- Factories, opciones OTLP, TLS, compresión y comportamiento de retry.
- Views, límites de cardinalidad, histogramas exponenciales y exemplars.
- Registro y retirada de callbacks observables.
- Bridges de logging y detectores de Resource.
- Instrumentación de frameworks, drivers y brokers concretos.
- Opciones ABI y compatibilidad de bibliotecas compartidas.

Si falta una capacidad, señalarlo y aplicar una alternativa soportada. Una
prueba de compilación puede demostrar presencia de una API; su comportamiento
requiere además una prueba funcional. Las capacidades experimentales se
presentan como tales y quedan fuera del camino obligatorio si carecen de una
alternativa reproducible.

## Semántica de C++ que debe explicarse

### Ownership y RAII

Explicar quién posee cada provider, processor, exporter, instrumento, callback
y estado capturado, y cuándo puede destruirse. No equiparar un guard de ámbito
con finalizar un span: activar/restaurar el contexto y ejecutar `End` son
responsabilidades distintas salvo que el wrapper concreto implemente ambas.
La semántica debe comprobarse en su implementación.

Revisar copias, moves, vistas de strings, buffers temporales, dobles cierres y
referencias a stacks ya destruidos. Los ejemplos de fallo de memoria se aíslan
en binarios de prueba y se contrastan con la solución corregida. El curso no
promueve depender de comportamiento indefinido como técnica de producción.

### Concurrencia y contexto

El contexto activo del hilo no representa automáticamente el contexto de una
tarea, coroutine o callback. Capturarlo antes del salto asíncrono, conservarlo
por valor con una vida útil adecuada y activarlo/restaurarlo en el ejecutor.
No mantener un Scope asociado a un hilo mientras una coroutine puede migrar
a otro sin un mecanismo compatible explícito.

Probar aislamiento entre solicitudes, restauración del contexto anterior,
fan-out, fan-in, cancelación, deadlines y reuso de workers. Un `shared_ptr`
resuelve ciertos problemas de duración; no vuelve thread-safe al objeto
compartido ni elimina data races sobre su estado.

### Cierre y procesos

Secuencia de referencia: dejar de aceptar trabajo, drenar o cancelar tareas,
retirar callbacks, efectuar flush y shutdown con plazos y destruir recursos.
Adaptarla a las interfaces de cada señal y al orden de ownership real. No
llamar al SDK desde un signal handler asíncrono; comunicar la petición de
parada a un contexto normal mediante un mecanismo seguro para señales.

No prometer persistencia ante crash o SIGKILL. La aceptación en una cola local
no equivale a recepción remota ni a indexación. El Collector también puede
perder datos según sus componentes y configuración. Evaluar fork después de
crear threads y preferir un diseño compatible documentado, como inicializar
tras fork o emplear fork-exec cuando corresponda.

### ABI y entrega del binario

Separar compatibilidad fuente y binaria. Revisar combinaciones de compilador,
stdlib, flags, dependencias y namespaces ABI antes de actualizar o cargar
plugins. Verificar duplicaciones de instancias globales al integrar copias
estáticas en múltiples módulos. No cruzar interfaces binarias sin contrato.
Conservar símbolos y herramientas de diagnóstico para resolver problemas de
carga y enlace en el entorno de ejecución.

## Señales y fronteras de responsabilidad

Trazas: spans finalizados, padres y links correctos, nombres acotados,
SpanKind, eventos y errores explícitos. La instrumentación debe representar
operaciones lógicas y evitar duplicar el trabajo de una integración existente.

Métricas: elección de instrumento, unidad, atributos, agregación, reader y
exportación. No usar trazas muestreadas para contar todos los errores. Un
histograma solo es útil si sus límites y consulta permiten responder a la
pregunta operativa. Reinicios, temporalidad y transformaciones del destino
forman parte de su validación.

Logs: cuerpo estructurado, severidad, timestamps, atributos y correlación con
contexto válido. Un fichero, stdout y OTLP son rutas de emisión diferentes;
combinarlas puede duplicar registros. Una integración de spdlog u otra
biblioteca se construye o selecciona por evidencia, no por analogía con Java.

OTLP: tratar endpoint, protocolo y ruta según la configuración específica del
exportador. Verificar qué variables de entorno consume esa implementación.
No trasladar una tabla genérica de opciones a C++ sin comprobarla.

Collector y backends: implementar lo necesario para validar el servicio C++.
La administración completa de todos los backends, la alta disponibilidad del
Collector y el Operator pertenecen al curso general y sus paths propios.

## Laboratorio local y contrato por práctica

Topología incremental: primero un ejecutable y exportación a consola; luego
servicio A → servicio B por HTTP o gRPC; después un worker y procesamiento
asíncrono. Incorporar Collector y elegir un destino verificable para cada
señal. Prometheus puede cubrir métricas; Jaeger o Tempo, trazas; un backend de
logs compatible cubre logs. No exigir instalar todos los productos.

Todo puede comenzar nativo en Linux. Compose con Podman o Docker constituye
la vía local reproducible de integración. Kubernetes es opcional. Los puertos
se restringen al host o red local del laboratorio; se emplean datos sintéticos.

Cada laboratorio desarrollado debe aportar:

1. Objetivo observable y prerrequisitos exactos.
2. Árbol de archivos y contenido completo de cada archivo necesario.
3. Configuración CMake y dependencias fijadas, sin comodines de versión.
4. Configuración completa de Collector, contenedores y backend utilizado.
5. Comandos de construir, ejecutar, generar tráfico, comprobar y limpiar.
6. Explicación de ownership y propagación en las fronteras relevantes.
7. Resultado esperado y comprobación positiva por señal y topología.
8. Fallo deliberado, síntoma, hipótesis, evidencia y recuperación.
9. Límites, costes y datos que no deben capturarse.
10. Evidencia observada cuando se ejecute; nunca inventar resultados.

Ningún laboratorio depende de credenciales externas obligatorias. La limpieza
actúa sobre recursos identificados del ejercicio, sin borrar volúmenes o
contenedores ajenos. No emplear comandos destructivos globales.

## Evaluación y profundidad didáctica

Cada lección comienza con 🎯 OBJETIVO y termina con 🧠 QUÉ DEBES RECORDAR,
con 3–7 puntos. Desarrollar mecanismo, decisiones y límites; añadir código
completo cuando ayude a verificar el objetivo. Incluir laboratorios, errores
frecuentes e ideas importantes donde sean útiles. Evitar capítulos genéricos
que repitan «arquitectura, configuración y buenas prácticas» sin mecanismos
específicos de C++.

Checkpoints después de los bloques 4, 8, 13, 18, 23, 28, 31 y 33. Se avanza
cuando las evidencias satisfacen los criterios, no por leer todos los títulos.

El proyecto final entrega fuentes, configuración, instrucciones, pruebas y
runbooks. Debe demostrar las tres señales, propagación por red y workers,
una frontera asíncrona, ausencia de datos sensibles, fallos remotos y cierre
ordenado. Fija antes de medir un presupuesto numérico de latencia, CPU y
memoria acorde a su carga; aporta baseline, repeticiones y resultados. No hay
un porcentaje universal de overhead aceptable.

Se evalúan reproducibilidad, semántica, diagnóstico y justificación. Una
solución que compila pero pierde padres entre threads o destruye estado antes
de sus callbacks no supera la evaluación. Las funciones opcionales se valoran
solo si su soporte y comportamiento se han demostrado.

## Uso con el generador y validación del paquete

Colocar los cuatro archivos juntos en el directorio del path. El perfil conserva
la referencia `../../config/pedagogy.md`, siguiendo la estructura del curso
general: ese archivo pertenece al proyecto del generador y no se incluye aquí.
Si la ubicación del path cambia, ajustar esa referencia antes de generar.

El catálogo `curriculum.blocks` permite contrastar las 340 lecciones con el
texto. Los campos de dominio y capacidad expresan requisitos de generación;
no sustituyen comprobar qué campos admite la versión concreta del generador.

Validación realizada: lectura YAML, bloques consecutivos 0–33, diez lecciones
por bloque, 340 identificadores únicos y coincidencia exacta de identificadores
y títulos entre `initial.txt` y el catálogo YAML. Se comprueban los cuatro
archivos UTF-8 y la integridad del ZIP. No se ha ejecutado course-generator ni
compilado laboratorios C++ en esta entrega curricular.
