# GO — BIBLIOGRAFÍA

## Principal

### Learning Go — Jon Bodner

Referencia principal para aprender el lenguaje de manera idiomática: tipos, funciones, slices, maps, structs, methods, interfaces, errores, modules, generics, context, concurrencia, testing y diseño de APIs.

Uso principal: bloques 0–16, 21, 25, 26 y 35.

## Rendimiento y profundidad

### Efficient Go — Bartłomiej Płotka

Referencia principal para ingeniería de rendimiento. Debe utilizarse para enseñar medición, eficiencia, complejidad práctica, CPU, memoria, allocations, GC, profiling, observabilidad y optimización basada en evidencia.

Uso principal: bloques 31–34 y proyecto final.

## Concurrencia

### Learn Concurrent Programming with Go — James Cutajar

Referencia especializada para los fundamentos y patrones de concurrencia: threads y goroutines, memoria compartida, synchronization, channels, pipelines y problemas clásicos de coordinación.

Uso principal: bloques 17–21 y 37.

## Aplicación profesional

### Go in Action, Second Edition — Joel Holmes, Andrew Walker, William Kennedy

Usar como referencia práctica para llevar las características del lenguaje a aplicaciones y sistemas reales, reforzando diseño idiomático, concurrencia, paquetes, servicios y prácticas profesionales.

Uso principal: bloques 13–26, 35–39 y proyecto final.

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
