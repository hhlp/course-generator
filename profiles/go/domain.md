# GO — DOMAIN

## Propósito

Este PATH forma desde cero hasta un nivel experto en Go, con énfasis en comprensión del lenguaje, programación idiomática, concurrencia, networking, servicios, testing, tooling, runtime, profiling, rendimiento e internals.

El objetivo no es memorizar APIs: cada lección debe explicar el modelo mental, las garantías del lenguaje, los costes, los trade-offs y la forma idiomática de resolver problemas en Go.

## Plataforma

- Plataforma principal: Fedora/Linux.
- Usar una versión estable y moderna de Go instalada en el sistema.
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
