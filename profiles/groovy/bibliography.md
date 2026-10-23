# Bibliografía — Groovy 0 → Experto

## Principal

### Groovy in Action
Referencia extensa para lenguaje, estilo idiomático, closures, builders, metaprogramación y ecosistema. Debe complementarse con la documentación oficial de la versión de Groovy estudiada.

## Oficial

### Apache Groovy Documentation
Fuente normativa principal para sintaxis, semántica, closures, POO, GDK, metaprogramación, AST transformations, type checking, static compilation e integración.

Áreas principales:
- Language Documentation
- Groovy Development Kit
- Closures
- Object orientation
- Semantics
- Metaprogramming
- Program structure
- Operators
- AST transformations
- Type checking extensions
- Integrating Groovy

Cuando exista diferencia entre un libro y la versión actual, prevalece la documentación oficial correspondiente.

## JVM y Java

### Java Language Specification
Referencia para comparar semántica Java/Groovy cuando sea relevante.

### Java Virtual Machine Specification
Referencia avanzada para bytecode, ejecución JVM, invokedynamic e internals.

### Java Platform API Documentation
Referencia para APIs Java usadas desde Groovy, especialmente `java.util`, `java.io`, `java.nio` y `java.util.concurrent`.

## Testing

### Spock Framework Documentation
Referencia principal para specifications, fixtures, data-driven testing, interactions, mocks, stubs y spies.

### JUnit Documentation
Referencia complementaria para interoperabilidad con testing Java/JVM.

## Build

### Gradle User Manual
Referencia para proyectos Groovy, Groovy plugin, source sets, dependencias, tasks, testing y publicación. El curso distingue lenguaje Groovy, Groovy DSL de Gradle y APIs de Gradle.

## Jenkins

### Jenkins User Documentation
Referencia para Jenkinsfile, Pipeline, Declarative Pipeline, Scripted Pipeline y conceptos CI/CD.

### Jenkins Pipeline Documentation
Referencia para Pipeline syntax, steps, stages, environment, parameters, post, parallel y matrix.

### Jenkins Shared Libraries Documentation
Referencia para `src/`, `vars/`, `resources/`, `@Library`, carga de bibliotecas y diseño de Shared Libraries.

### Jenkins Script Security Documentation
Referencia para Groovy Sandbox, Script Approval y seguridad de Groovy dentro de Jenkins.

### Jenkins Developer Documentation / Javadocs
Referencia avanzada para Jenkins internals y acceso programático al object model.

## Profundización

### Making Java Groovy
Útil para interoperabilidad Java/Groovy y adopción de Groovy en aplicaciones JVM.

### Programming Groovy
Referencia complementaria para estilo idiomático, closures, builders y programación dinámica.

## Política bibliográfica
Prioridad:
1. Documentación oficial de Apache Groovy.
2. Especificaciones/documentación Java y JVM.
3. Documentación oficial de Spock, Gradle y Jenkins.
4. Libros especializados.

No se inventan capítulos, páginas, secciones ni números de edición. Las referencias exactas solo se incluyen cuando han sido verificadas.


## Referencias adicionales por scope

### Lenguaje, AST y herramientas (oficial)
- Apache Groovy — Language Specification, Semantics, Operators, Closures, Metaprogramming, AST Transformations y Type Checking Extensions. https://groovy-lang.org/documentation.html
- Apache Groovy — Groovy Development Kit y API documentation. https://groovy-lang.org/
- CodeNarc — documentación oficial de reglas, Gradle y análisis estático. https://codenarc.org/

### Integración y JVM
- Oracle/OpenJDK — java.net.http.HttpClient, java.nio.file, java.util.concurrent y Java Flight Recorder. https://docs.oracle.com/en/java/javase/
- OpenJDK — JMH (Java Microbenchmark Harness). https://github.com/openjdk/jmh
- GPars — documentación del proyecto, sujeta a verificación de compatibilidad. https://gpars.org/

### Testing y build
- Spock Framework — User Guide, interacción, fixtures y data-driven tests. https://spockframework.org/
- JaCoCo — documentación oficial. https://www.jacoco.org/jacoco/
- Gradle — Groovy plugin, toolchains, dependency locking, publishing y testing. https://docs.gradle.org/current/userguide/userguide.html

### Jenkins: CPS y Shared Libraries
- Jenkins — Pipeline CPS Method Mismatches. https://www.jenkins.io/doc/book/pipeline/cps-method-mismatches/
- Jenkins — Extending with Shared Libraries. https://www.jenkins.io/doc/book/pipeline/shared-libraries/
- Jenkins — Pipeline Best Practices. https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/
- Jenkins — Script Security. https://www.jenkins.io/doc/book/managing/script-approval/
- JenkinsPipelineUnit — proyecto y documentación para unit tests de pipelines; complementar con integración real. https://github.com/jenkinsci/JenkinsPipelineUnit

## Política de alcance bibliográfico
Clasificar cada lectura según el bloque y scope; no presentar herramientas o librerías opcionales como parte obligatoria del lenguaje. Verificar versiones compatibles de Groovy, JDK, Spock, Gradle y Jenkins antes de fijar comandos o dependencias.

## Lecturas dirigidas para los ajustes de profundidad
- Semántica numérica: Apache Groovy, Syntax y Operators; división,
  promoción numérica, BigDecimal e intdiv().
  https://groovy-lang.org/syntax.html
  https://groovy-lang.org/operators.html
- Closures: documentación oficial y API de groovy.lang.Closure; clone(),
  rehydrate(), dehydrate(), trampoline() y estrategias de resolución.
  https://groovy-lang.org/closures.html
  https://docs.groovy-lang.org/latest/html/api/groovy/lang/Closure.html
- BigDecimal, MathContext y RoundingMode: API oficial del JDK elegido.
  https://docs.oracle.com/en/java/javase/
- Jenkins: Pipeline Best Practices, ejecución en controller y delegación
  de operaciones al agente. Lectura de la especialización opcional.
  https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/
- Jenkins: Shared Libraries, confianza, repositorio SCM y permisos.
  https://www.jenkins.io/doc/book/pipeline/shared-libraries/

## Uso por itinerario
Las referencias Jenkins corresponden a la especialización opcional.
La bibliografía administrativa de Jenkins sirve solo de consulta contextual;
su desarrollo completo pertenece al PATH independiente de Jenkins.
Para cada laboratorio se registra la versión exacta de la documentación
utilizada, además de JDK, Groovy y herramientas. Los enlaces latest/current
son puntos de entrada, no una garantía de reproducibilidad.
