# Dominio — Groovy 0 → Experto

## Propósito
Enseñar Groovy como lenguaje completo sobre la JVM, desde fundamentos hasta metaprogramación, DSL, AST y ejecución embebida. Una especialización opcional aplica estos conocimientos a Jenkins Pipeline y Shared Libraries.

## Alcance
Incluye sintaxis y tipos; Groovy Truth; String/GString; regex; colecciones; métodos; closures; POO; traits y generics; AST; excepciones; I/O; JSON/XML; scripting Linux; interoperabilidad Java/JVM; GDK; programación funcional; MOP; metaprogramación; DSL; concurrencia; Spock; Gradle; internals y rendimiento; seguridad; embedding; Jenkins Pipeline; Shared Libraries y límites del entorno de ejecución Jenkins.

## Objetivo de dominio
Al finalizar, el estudiante podrá leer, escribir, probar, depurar y diseñar software Groovy idiomático; comprender su ejecución sobre la JVM; construir DSL internos; utilizar metaprogramación de forma controlada; y comprender la relación entre closures, delegation, DSL y Jenkins Pipeline.

## Principios
1. Groovy se estudia primero como lenguaje, no como simple sintaxis para Jenkins.
2. Java y la JVM forman parte del modelo mental.
3. Closures reciben tratamiento profundo.
4. `this`, `owner`, `delegate` y `resolveStrategy` se estudian mediante experimentos.
5. Metaprogramación se enseña junto con mantenimiento, seguridad y rendimiento.
6. Los DSL se explican desde sus mecanismos internos.
7. Jenkins se introduce después de dominar los mecanismos de Groovy que explican Pipeline.
8. Se distingue siempre Groovy estándar de APIs y DSL proporcionados por Jenkins.
9. Se priorizan ejemplos ejecutables y laboratorios reproducibles.
10. Referencias exactas de versiones y APIs deben verificarse contra documentación oficial.

## Entorno recomendado
- Linux/Fedora.
- JDK compatible con la versión de Groovy utilizada.
- Groovy estable actual.
- Gradle.
- Spock.
- Jenkins para la especialización final.

## Fuera de alcance principal
No sustituye un curso completo de Java, Gradle o administración de Jenkins. Estos dominios se cubren hasta la profundidad necesaria para comprender y aplicar Groovy profesionalmente.

## Proyecto final
Aplicación Groovy estructurada con POO, colecciones, closures, JSON/XML, DSL propio, metaprogramación, Spock y Gradle, con una ampliación opcional que produce una Jenkins Shared Library y un Jenkinsfile consumidor.

## Ampliación de competencias expertas
- Semántica avanzada: igualdad/identidad, coerción, GString, alcance, tipos y anotaciones de delegación.
- Arquitectura JVM: classloaders, bytecode, profiling, Java Memory Model y límites de rendimiento.
- Ingeniería de lenguaje: MOP, AST personalizadas, type checking extensions, DSL verificables y seguridad.
- Integración profesional: NIO.2, CLI robusta, HTTP/REST, JSON, XML, CSV y YAML mediante bibliotecas.
- Calidad: Spock, CodeNarc, JaCoCo, JFR, JMH, debugging y Gradle reproducible.
- Jenkins avanzado: CPS, @NonCPS, serialización, checkpoints, controller/agents, Script Security y Shared Libraries probadas.

## Profundidad obligatoria por lección xx.yy
Cada lección desarrollará el mecanismo, sintaxis, ejemplos ejecutables, casos límite, errores frecuentes, seguridad y laboratorio reproducible. Incluirá diagnóstico y criterios de verificación cuando corresponda. Las características dependientes de versión deben identificarse y contrastarse con la documentación de la versión elegida.

## Delimitación con otros learning paths
Regex se aplica mediante APIs de Groovy, sin duplicar la teoría completa del path de Regex. Java, Gradle y Jenkins se explican en lo necesario para dominar su integración con Groovy; el curso no sustituye sus paths independientes. GroovyShell y GroovyClassLoader no se consideran fronteras de seguridad para código no confiable.

## Evaluación
Checkpoints por bloque, laboratorios progresivos, pruebas automatizadas y diagnóstico de fallos. El proyecto final (bloque 34) debe demostrar una aplicación Groovy mantenible y probada. La ampliación opcional Jenkins se evalúa por separado e incluye una Shared Library, CPS, serialización y reanudación.

## Itinerarios y separación de Jenkins
El núcleo obligatorio comprende los bloques 0–25, 29–31 y el proyecto 34.
Los bloques 26–28 y 32–33 constituyen la especialización opcional Jenkins.
El estudiante puede completar y aprobar el núcleo sin instalar Jenkins.
La instalación, administración, jobs, nodes, plugins, credenciales globales,
JCasC y operación de Jenkins pertenecen a su PATH independiente. Aquí solo
se estudia el contexto necesario para escribir y diagnosticar código Groovy.
El bloque 27 introduce bibliotecas; el 33 exige refactorización, contratos,
gobierno y pruebas de regresión sobre una biblioteca ya construida.
El bloque 26 introduce Pipeline; el 32 profundiza en CPS y recuperación.
La versión de Groovy del proyecto local y la integrada en Jenkins deben
verificarse por separado; no se presupone que compartan sintaxis ni APIs.

## Checkpoints y criterios de aceptación
Cada bloque 0–33 termina con una lección numerada de checkpoint. Se exige
un ejemplo ejecutable, una prueba o comprobación observable, un fallo
introducido y diagnosticado, y una explicación de límites y decisiones.
En bloques conceptuales se usa un experimento mínimo reproducible.
El núcleo se aprueba con corrección funcional, pruebas significativas,
dependencias fijadas, manejo de errores, seguridad y documentación.
La extensión Jenkins añade pruebas reales de workspace/controller, CPS,
serialización y reinicio, además de la distinción trusted/untrusted.
Los mocks de JenkinsPipelineUnit no sustituyen estas pruebas reales.
