# Bibliografía — Jenkins 0 → experto

## Principal

### Jenkins: The Definitive Guide — John Ferguson Smart
Referencia amplia para fundamentos, automatización, jobs, builds, testing e integración continua. Debe complementarse con documentación oficial actual porque Jenkins ha evolucionado significativamente desde su publicación.

### Jenkins 2: Up and Running — Brent Laster
Útil para Jenkins moderno, Pipeline as Code, Jenkinsfile, arquitectura de pipelines y prácticas de automatización. Complementar siempre con la documentación oficial para sintaxis y comportamiento actuales.

## Oficial — Jenkins

### Jenkins User Documentation
Fuente normativa principal del curso para instalación, administración, Pipeline, seguridad, agentes, plugins, credenciales y operación.

Referencia: https://www.jenkins.io/doc/

### Jenkins Pipeline Documentation
Referencia principal para Jenkinsfile, Declarative Pipeline, Scripted Pipeline y Pipeline Syntax.

Referencia: https://www.jenkins.io/doc/book/pipeline/

### Pipeline Syntax
Referencia para steps, directives y sintaxis soportada.

Referencia: https://www.jenkins.io/doc/book/pipeline/syntax/

### Jenkins Shared Libraries
Referencia principal para vars/, src/, resources/, @Library y reutilización de código Pipeline.

Referencia: https://www.jenkins.io/doc/book/pipeline/shared-libraries/

### Jenkins Pipeline CPS Method Mismatches
Lectura fundamental para comprender CPS, @NonCPS y diferencias entre Groovy convencional y Jenkins Pipeline.

Referencia: https://www.jenkins.io/doc/book/pipeline/cps-method-mismatches/

### Jenkins Security Documentation
Referencia para authentication, authorization, credentials, Script Security, hardening y prácticas operativas.

Referencia: https://www.jenkins.io/doc/book/security/

### Jenkins Configuration as Code
Referencia para configuración reproducible y automatización de Jenkins.

Referencia: https://www.jenkins.io/projects/jcasc/

## Groovy — principal

### Programming Groovy 2 — Venkat Subramaniam
Base conceptual para aprender Groovy como lenguaje: closures, colecciones, objetos, metaprogramación y estilo idiomático.

### Making Java Groovy — Ken Kousen
Útil para comprender Groovy sobre la JVM y su relación con Java.

## Groovy — oficial

### Apache Groovy Documentation
Fuente principal para validar sintaxis y comportamiento actual de Groovy.

Referencia: https://groovy-lang.org/documentation.html

### Groovy Language Specification
Referencia técnica para semántica del lenguaje.

Referencia: https://groovy-lang.org/semantics.html

### Groovy Closures
Lectura esencial para Jenkins, DSLs y Shared Libraries.

Referencia: https://groovy-lang.org/closures.html

### Groovy Metaprogramming
Referencia para MetaClass, ExpandoMetaClass, methodMissing, propertyMissing y metaprogramación.

Referencia: https://groovy-lang.org/metaprogramming.html

## CI/CD y diseño

### Continuous Delivery — Jez Humble, David Farley
Fundamentos de pipelines de entrega, automatización, despliegue, feedback y diseño de procesos de entrega.

### Accelerate — Nicole Forsgren, Jez Humble, Gene Kim
Contexto para rendimiento de entrega de software, métricas y prácticas DevOps.

### The DevOps Handbook — Gene Kim, Jez Humble, Patrick Debois, John Willis
Contexto organizativo y técnico para CI/CD, flujo, feedback y automatización.

## Seguridad y supply chain

### NIST Secure Software Development Framework (SSDF)
Referencia para prácticas de desarrollo y entrega segura.

### SLSA
Referencia para provenance y seguridad de la cadena de suministro de software.

### OWASP CI/CD Security Cheat Sheet
Referencia práctica para amenazas y controles aplicables a pipelines CI/CD.

## Estrategia de lectura

La documentación oficial de Jenkins es normativa para comportamiento actual de Jenkins y sus plugins.

La documentación oficial de Apache Groovy es normativa para el lenguaje.

Los libros se utilizan para explicación conceptual y progresión pedagógica; cuando exista una diferencia con una versión actual, prevalece la documentación oficial correspondiente.

Para Pipeline avanzado debe seguirse esta secuencia:

Groovy → closures → DSLs → Jenkins Pipeline DSL → CPS → serialización → @NonCPS → Shared Libraries → Jenkins internals.
