# GO — DOMAIN

## Propósito

Este PATH forma desde cero hasta un nivel experto en Go, con énfasis en comprensión del lenguaje, programación idiomática, concurrencia, networking, servicios, testing, tooling, runtime, profiling, rendimiento e internals.

El objetivo no es memorizar APIs: cada lección debe explicar el modelo mental, las garantías del lenguaje, los costes, los trade-offs y la forma idiomática de resolver problemas en Go.

## Plataforma

- Plataforma principal: Fedora/Linux.
- Base mínima de esta revisión: Go 1.26.0. Fijar una versión estable exacta del toolchain en cada laboratorio y CI; verificar sus notas de versión y actualizaciones de seguridad. No interpretar esta base como afirmación de cuál es la última versión disponible.
- El contenido debe ser version-aware: cuando una característica dependa de una versión concreta, indicarlo.
- La especificación y documentación oficial de Go prevalecen ante diferencias con libros más antiguos.
- No asumir GOPATH como modelo moderno de gestión de proyectos: enseñar módulos y workspaces como enfoque actual, explicando GOPATH por contexto histórico y por su papel residual en el entorno.

## Profundidad pedagógica

Cada lección debe comenzar exactamente con:

🎯 OBJETIVO

Después debe desarrollar el tema de forma progresiva, profunda y didáctica. No producir resúmenes superficiales.

Cuando aporten valor, incorporar:

🧪 Laboratorio/ejemplos
⚠️ Errores frecuentes
💡 Idea importante
📚 LECTURA

Cada lección debe terminar exactamente con:

🧠 QUÉ DEBES RECORDAR

Este cierre contendrá entre 3 y 7 ideas esenciales y no será una repetición del objetivo.

## Código

- Todo concepto de lenguaje debe incluir código mínimo y ejecutable cuando sea razonable.
- Explicar primero el código y después incrementar su complejidad.
- Mostrar salida esperada cuando ayude a comprender el comportamiento.
- Diferenciar claramente código válido, inválido, no idiomático y deliberadamente peligroso.
- Preferir la biblioteca estándar antes de introducir dependencias externas.
- Usar `gofmt`.
- Los ejemplos deben compilar con la versión objetivo salvo que se identifiquen expresamente como históricos o dependientes de versión.
- Explicar tipos, zero values, ownership lógico, aliasing, lifetime, allocations y efectos de concurrencia cuando sean relevantes.

## Go idiomático

El PATH debe reforzar:

- simplicidad y claridad;
- composición en lugar de jerarquías de herencia;
- interfaces pequeñas;
- errores como valores;
- dependencia mínima;
- APIs explícitas;
- context para cancelación/deadlines, no como contenedor genérico de parámetros;
- concurrencia con ownership y lifecycle claros;
- evitar goroutines sin estrategia de terminación;
- medir antes de optimizar.

No trasladar mecánicamente patrones de Java/C++ a Go.

## Concurrencia

La concurrencia es un eje principal, no un apéndice.

Debe cubrir goroutines, channels, select, sync, atomics, race detector, deadlocks, leaks, cancellation, pipelines, worker pools, backpressure y Go Memory Model.

Distinguir siempre:

- concurrencia frente a paralelismo;
- coordinación mediante comunicación frente a memoria compartida;
- race condition frente a data race;
- corrección frente a rendimiento;
- goroutine creada frente a goroutine correctamente gestionada.

## Runtime y rendimiento

A nivel avanzado se debe explicar:

- scheduler G-M-P;
- stacks;
- heap y allocator;
- garbage collector;
- escape analysis;
- inlining y optimizaciones del compilador;
- pprof;
- execution tracing;
- runtime metrics;
- contention;
- allocation pressure;
- PGO.

Las optimizaciones deben justificarse con mediciones reproducibles.

## Testing y calidad

Cubrir unit tests, table-driven tests, subtests, integration tests, examples, benchmarks, fuzzing, coverage y race detector.

Enseñar `go test`, `go vet`, `govulncheck` y herramientas de diagnóstico como parte del flujo normal de ingeniería.

## Servicios y producción

Los bloques de producción deben conectar Go con:

HTTP, TCP/UDP, TLS, database/sql, logging estructurado, métricas, tracing, graceful shutdown, signals, health checks, containers, Kubernetes y CI/CD.

Las dependencias externas como gRPC u OpenTelemetry se introducen después de comprender los mecanismos equivalentes o fundamentales de la biblioteca estándar.

## Internals

Los bloques de internals deben usar código fuente real del proyecto Go cuando sea apropiado, pero sin convertir el PATH en un curso de desarrollo del compilador.

Objetivo: poder razonar sobre el comportamiento y coste del programa observando runtime, compiler, assembly y perfiles.

## Laboratorios

Los laboratorios deben ser acumulativos. Evitar ejercicios de juguete cuando el nivel permita problemas reales.

El proyecto final debe integrar:

CLI, configuración, HTTP, persistencia, concurrencia, context, errores, logging, métricas, tracing, testing, fuzzing, race detection, benchmarks, profiling, optimización, PGO, seguridad, containerización y graceful shutdown.


## Big O aplicado a Go

El bloque específico de complejidad aplica conceptos del PATH independiente de Big O; no repite su fundamentación matemática. En cada estructura o algoritmo indicar operación, tamaño de entrada, caso de análisis, complejidad temporal y espacial, supuestos y límites de la garantía. Distinguir complejidad esperada/amortizada de garantías en peor caso. Contrastar con `testing.B`, `-benchmem`, `benchstat` y `pprof`, sin presentar tiempos medidos como prueba de una cota asintótica. Analizar costes de `append`, slices, maps, strings, ordenación, estructuras genéricas y concurrencia.

## Regex aplicado a Go

Enseñar el paquete `regexp` y su sintaxis RE2 en profundidad aplicada, remitiendo al PATH independiente de regex para teoría general. Incluir familias de métodos, capturas, sustituciones, UTF-8 e índices en bytes, seguridad, pruebas y benchmarks. No atribuir a RE2 lookarounds ni backreferences; distinguir complejidad lineal en la entrada para patrón fijo de costes dependientes del patrón. Comparar con `strings`, `bytes` y parsers específicos.

## Desarrollo CLI en Go

Enseñar aplicaciones CLI de producción con biblioteca estándar primero: `flag`, `os`, `io`, `context`, `os/signal`, `filepath`, formatos de salida, códigos de salida, configuración, subcomandos, testing, empaquetado y distribución. Mantener ejemplos Fedora/Linux y diferenciar extensiones de terceros de funcionalidades estándar.

## Integración transversal

Relacionar Big O con slices, maps, generics, concurrencia, benchmarks y performance; relacionar regex con logs, seguridad, CLI y streaming. El proyecto final incluirá análisis de complejidad documentado y un subcomando de extracción de logs basado en `regexp`, con tests, fuzzing y benchmarks. Mantener la numeración correlativa del `initial.txt` como referencia canónica de bloques.

## Autoridad de fuentes

Orden de prioridad ante discrepancias:

1. Go Language Specification.
2. Documentación oficial de Go y documentación de paquetes.
3. Go Memory Model y documentación oficial del runtime/toolchain.
4. Learning Go.
5. Efficient Go.
6. Learn Concurrent Programming with Go.
7. Go in Action, Second Edition.
8. Go Cookbook.

Los libros son referencias pedagógicas; no deben congelar el curso en una versión antigua del lenguaje.


## Progresión y prerrequisitos obligatorios

Conservar los 45 bloques (0–44) y todos los títulos de lecciones originales.
Las ampliaciones se integran con numeración correlativa dentro de cada bloque.
El número de lecciones de esta revisión queda registrado en el resumen de validación.

- Bloque 0: crear un módulo mínimo antes del primer programa; el bloque 14 desarrolla módulos en profundidad.
- Bloque 3: type switch es un anticipo ilustrativo con una explicación mínima de interfaces; su dominio se exige después del bloque 10.
- Bloque 7: explicar punteros a structs antes de utilizarlos. Los tags se presentan como metadatos; reflection avanzada se reserva para el bloque 31.
- Bloque 8: explicar escape analysis, stack y heap conceptualmente; las herramientas de medición se desarrollan después.
- Bloque 14: enseñar pruebas mínimas, tablas de casos, benchmarks con B.Loop y un fuzz target antes del bloque 16. Incluir comandos y lectura de resultados.
- Bloque 16: utilizar ese anticipo para probar regexp. El profiling se introduce mediante una captura guiada mínima; el análisis avanzado pertenece al bloque 36.
- Bloque 18: desarrollar primero costes secuenciales. Las lecciones de complejidad de goroutines, channels, worker pools y span se realizan en una segunda pasada tras los bloques 19–23; se integran con evidencia en el bloque 40.
- Bloque 19: presentar WaitGroup de forma mínima antes de laboratorios de coordinación; profundizar en el bloque 21.
- Bloques 25–26: proporcionar las herramientas de prueba mínimas requeridas por HTTP y SQL sin esperar al desarrollo completo del bloque 27.

Mantener títulos originales no obliga a repetir contenido: los anticipos y revisitas
señalan alcance, conocimientos previos y objetivo nuevo. No exigir una herramienta
que no se haya explicado o acompañado de una guía ejecutable.

## Versión y precisión técnica

Base mínima Go 1.26.0; registrar go version, GOOS, GOARCH y directivas go/toolchain.
Etiquetar APIs por su versión de incorporación y contrastar cualquier evolución
posterior con la documentación del toolchain fijado. Las características
experimentales deben separarse de las garantías estables y ser optativas.

Cubrir iteradores y range sobre funciones (Go 1.23), alias genéricos, os.Root,
B.Loop y tool en go.mod (Go 1.24), WaitGroup.Go y testing/synctest (Go 1.25),
y new con expresión, constraints autorreferentes y errors.AsType (Go 1.26).
Para métodos genéricos distinguir métodos de tipos genéricos de métodos con
parámetros de tipo propios; verificar su soporte exacto antes de mostrar código.
No deducir soporte de una propuesta o de una versión de desarrollo.

Distinguir garantías de la especificación de decisiones del compilador/runtime.
No fijar como contrato factores de crecimiento de slices, complejidad de maps,
representación de interfaces, elección stack/heap ni algoritmos internos del GC.
Presentar estos últimos como implementaciones de la versión inspeccionada.
Go pasa todos los argumentos por valor; explicar el aliasing de datos subyacentes.
Los strings pueden contener bytes que no formen UTF-8 válido; rune no equivale
a grafema. Aclarar estos límites en regex, índices y procesamiento de texto.

## Contratos de recursos y corrección

- I/O: procesar n > 0 antes del error; distinguir EOF de lectura incompleta; tratar escrituras y errores de cierre; limitar tokens, buffers y volumen de entrada.
- Concurrencia: asignar propietario, política de cancelación y espera de terminación a cada tarea. Cancelar no equivale a hacer join. No copiar sincronizadores tras utilizarlos.
- HTTP: cerrar cuerpos de respuestas, explicar cuándo se reutilizan conexiones, limitar solicitudes y aplicar timeouts con su alcance correcto.
- SQL: cerrar filas, comprobar Rows.Err, gestionar rollback/commit y medir saturación del pool. Usar un driver explícito y una base de pruebas aislada.
- Procesos: preferir os/exec con argumentos separados; documentar streams, ExitError, señales y límites de la cancelación del proceso y sus descendientes.
- Seguridad: contrastar math/rand y crypto/rand, restringir destinos de red y rutas, y proteger endpoints de profiling.

## Laboratorios y evaluación final

Cada laboratorio entrega código, comandos reproducibles, versión de herramientas,
resultados esperados y criterios de aceptación. Las pruebas deben demostrar
contratos observables y fallos relevantes. No sustituir pruebas de corrección
por benchmarks, ni interpretar cobertura o race detector como prueba exhaustiva.

El bloque 44 requiere además de los componentes originales:

1. Un subcomando que extraiga logs mediante regexp con procesamiento incremental y límites explícitos de memoria/entrada.
2. Tests de coincidencias, UTF-8 inválido, entradas vacías, límites y errores de I/O; fuzzing y benchmarks reproducibles.
3. Un documento con tiempo y espacio por operación, tamaño de entrada, tamaño de patrón, supuestos y contraste con mediciones.
4. Ensayos de cancelación, fallo de persistencia y apagado con productores bloqueados, verificando liberación de recursos.
5. SLO del laboratorio y presupuesto de recursos definidos por el alumno, junto con evidencia de aceptación y limitaciones.

Los contenidos de Big O y Regex generales son prerrequisitos de referencia.
Aquí se aplica esa teoría a Go; los repasos mínimos enlazan al PATH independiente.
