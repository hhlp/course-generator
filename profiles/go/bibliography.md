# GO — BIBLIOGRAFÍA

## Principal

### Learning Go — Jon Bodner

Referencia principal para aprender el lenguaje de manera idiomática: tipos, funciones, slices, maps, structs, methods, interfaces, errores, modules, generics, context, concurrencia, testing y diseño de APIs.

Uso principal: bloques 0–15, 19–23, 25–29 y 38; apoyo transversal al bloque 44.

## Rendimiento y profundidad

### Efficient Go — Bartłomiej Płotka

Referencia principal para ingeniería de rendimiento. Debe utilizarse para enseñar medición, eficiencia, complejidad práctica, CPU, memoria, allocations, GC, profiling, observabilidad y optimización basada en evidencia.

Uso principal: bloques 18 y 34–37; apoyo a los bloques 40, 42 y 44.

## Concurrencia

### Learn Concurrent Programming with Go — James Cutajar

Referencia especializada para los fundamentos y patrones de concurrencia: threads y goroutines, memoria compartida, synchronization, channels, pipelines y problemas clásicos de coordinación.

Uso principal: bloques 19–23 y 40; apoyo al proyecto final (44).

## Aplicación profesional

### Go in Action, Second Edition — Joel Holmes, Andrew Walker, William Kennedy

Usar como referencia práctica para llevar las características del lenguaje a aplicaciones y sistemas reales, reforzando diseño idiomático, concurrencia, paquetes, servicios y prácticas profesionales.

Uso principal: bloques 13–15, 17, 19–30 y 38–42; apoyo al proyecto final (44).

## Recetario y laboratorios

### Go Cookbook: Expert Solutions for Commonly Needed Go Tasks — Sau Sheong Chang

No seguir necesariamente de forma lineal. Sus recetas deben utilizarse para enriquecer ejemplos, laboratorios y soluciones prácticas cuando correspondan al concepto estudiado.

Uso transversal: biblioteca estándar, archivos, encoding, networking, HTTP, datos, testing, concurrencia y tareas de sistema.

## Fuente normativa y de actualización

### Official Go Documentation

La documentación oficial es la autoridad técnica del PATH y debe consultarse durante todo el curso.

Referencias esenciales:

- The Go Programming Language Specification
- A Tour of Go
- Effective Go
- Go Code Review Comments
- Standard library package documentation
- Modules Reference
- Go workspaces documentation
- Go Memory Model
- Diagnostics
- Profile-guided optimization
- Garbage Collector Guide
- Fuzzing documentation
- Race Detector
- govulncheck / vulnerability management
- Release Notes de cada versión de Go
- Compiler and runtime documentation/source

Sitio oficial: https://go.dev/

Documentación de paquetes: https://pkg.go.dev/


## Referencias específicas — Big O y regexp en Go

- **Go standard library — regexp**: https://pkg.go.dev/regexp
- **Go regexp/syntax**: https://pkg.go.dev/regexp/syntax
- **RE2 Syntax**: https://github.com/google/re2/wiki/Syntax (referencia de sintaxis y restricciones; contrastar con `regexp/syntax`).
- **Go standard library — slices, maps, sort, container/heap, strings, bytes**: https://pkg.go.dev/std
- **Go testing y benchmarking**: https://pkg.go.dev/testing
- **Go diagnostics y pprof**: https://go.dev/doc/diagnostics
- **Go command y módulos**: https://pkg.go.dev/cmd/go
- **Go flag, os, os/signal**: https://pkg.go.dev/flag y https://pkg.go.dev/os/signal

Los PATH independientes de Big O y Regex aportan la teoría general; estas fuentes se utilizan para su aplicación específica a Go. *Efficient Go* sigue siendo el libro principal para medir y razonar sobre rendimiento; *Go Cookbook* apoya los laboratorios de regexp y CLI.

## Estrategia de lectura

### Nivel inicial

Principal:
- Learning Go
- A Tour of Go
- documentación oficial de cada package usado

Objetivo:
- sintaxis;
- sistema de tipos;
- funciones;
- arrays/slices/maps;
- structs;
- methods;
- interfaces;
- errores;
- packages/modules.

### Nivel intermedio

Principal:
- Learning Go
- Go in Action, Second Edition
- Go Cookbook
- documentación oficial

Objetivo:
- diseño idiomático;
- I/O;
- stdlib;
- HTTP;
- databases;
- testing;
- tooling;
- aplicaciones reales.

### Concurrencia

Principal:
- Learn Concurrent Programming with Go
- Learning Go

Normativa:
- Go Memory Model
- documentación de `sync`, `sync/atomic`, `context` y race detector

Objetivo:
- razonar sobre sincronización y lifecycle, no limitarse a conocer la sintaxis de goroutines/channels.

### Nivel avanzado

Principal:
- Efficient Go
- documentación oficial de diagnostics, GC, compiler, runtime y PGO

Objetivo:
- profiling;
- allocations;
- GC;
- scheduler;
- tracing;
- compiler;
- performance engineering.

### Nivel experto

Principal:
- código fuente y documentación oficial del proyecto Go
- Efficient Go como apoyo metodológico

Objetivo:
- interpretar internals;
- diagnosticar comportamiento de producción;
- analizar perfiles y assembly;
- comprender trade-offs del runtime;
- optimizar solamente a partir de evidencia.

## Regla de actualización

La bibliografía impresa puede describir versiones anteriores de Go. Nunca reproducir una limitación histórica como si siguiera vigente.

Para características que evolucionan —generics, toolchain, standard library, runtime, GC, HTTP, modules, testing o profiling— verificar primero la documentación y release notes oficiales de la versión objetivo.

## Referencias bibliográficas específicas

Bodner, Jon. *Learning Go*.

Płotka, Bartłomiej. *Efficient Go*.

Chang, Sau Sheong. *Go Cookbook: Expert Solutions for Commonly Needed Go Tasks*.

Holmes, Joel; Walker, Andrew; Kennedy, William. *Go in Action, Second Edition*.

Cutajar, James. *Learn Concurrent Programming with Go*.

The Go Authors. *The Go Programming Language Specification* y documentación oficial del proyecto Go.


## Correspondencia actual de fuentes y bloques

La numeración de initial.txt es canónica. Los rangos siguientes indican apoyo
pedagógico; no afirman que un libro cubra todas las APIs actuales del bloque.

| Bloques | Fuente principal o normativa |
| --- | --- |
| 0–10 | Learning Go; Tour; especificación y paquetes estándar |
| 11 | Especificación; iter; notas de Go 1.23–1.26; Learning Go |
| 12 | errors y fmt; Learning Go |
| 13–14 | Modules Reference, Go Toolchains y cmd/go |
| 15–17 | Documentación estándar; Go Cookbook |
| 18 | Efficient Go; contratos de paquetes; PATH general de Big O |
| 19–23 | Learn Concurrent Programming with Go; Memory Model; sync y context |
| 24–26 | net, net/http, crypto/tls y database/sql; Go Cookbook |
| 27–29 | testing, testing/synctest, cmd/go, flag y os/exec |
| 30 | Go Security; govulncheck; documentación de crypto y net/http |
| 31–33 | reflect, unsafe, cmd/cgo y runtime/cgo |
| 34–37 | GC Guide; diagnostics; runtime; PGO; Efficient Go |
| 38–40 | Learning Go; Go in Action; errgroup; fuentes oficiales de observabilidad |
| 41 | go/ast, go/types; golang.org/x/tools/go/analysis y go/packages |
| 42 | Documentación Go; documentación oficial de systemd, Podman y Kubernetes |
| 43 | Código fuente de la versión exacta de Go inspeccionada |
| 44 | Integración de fuentes anteriores con evidencia de aceptación |

## Fuentes oficiales específicas añadidas

- Notas Go 1.23: https://go.dev/doc/go1.23
- Notas Go 1.24: https://go.dev/doc/go1.24
- Notas Go 1.25: https://go.dev/doc/go1.25
- Notas Go 1.26: https://go.dev/doc/go1.26
- Selección del toolchain: https://go.dev/doc/toolchain
- Especificación: https://go.dev/ref/spec
- Iteradores: https://pkg.go.dev/iter
- Errores: https://pkg.go.dev/errors
- Pruebas: https://pkg.go.dev/testing
- Pruebas de concurrencia: https://pkg.go.dev/testing/synctest
- I/O: https://pkg.go.dev/io y https://pkg.go.dev/bufio
- Filesystem y Root: https://pkg.go.dev/os
- Procesos: https://pkg.go.dev/os/exec
- Sincronización: https://pkg.go.dev/sync y https://pkg.go.dev/sync/atomic
- Cancelación: https://pkg.go.dev/context
- Concurrencia estructurada: https://pkg.go.dev/golang.org/x/sync/errgroup
- HTTP: https://pkg.go.dev/net/http
- SQL: https://pkg.go.dev/database/sql
- Delve: https://github.com/go-delve/delve/tree/master/Documentation
- gopls: https://go.dev/gopls/
- Analyzers: https://pkg.go.dev/golang.org/x/tools/go/analysis
- Carga de paquetes: https://pkg.go.dev/golang.org/x/tools/go/packages
- Guía de GC: https://go.dev/doc/gc-guide
- PGO: https://go.dev/doc/pgo
- Seguridad: https://go.dev/doc/security/
- systemd: https://www.freedesktop.org/software/systemd/man/latest/
- Podman: https://docs.podman.io/
- Kubernetes: https://kubernetes.io/docs/

Consultar las páginas correspondientes a la versión fijada, en especial cuando
pkg.go.dev muestre una API posterior. Delve, gopls, errgroup, go/analysis y
OpenTelemetry son herramientas o módulos externos; no presentarlos como parte
de la biblioteca estándar. Fijar sus versiones en los laboratorios que los usen.

## Alcance de las referencias independientes

Big O y Regex generales aportan teoría. Los bloques 16 y 18 aplican sus conceptos
a Go, sin reconstruir esos cursos. Mantener un repaso mínimo cuando sea necesario
para interpretar una API, una prueba o un resultado de rendimiento.
