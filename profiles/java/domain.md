# Domain — Java 0 → Experto en profundidad

## Dominio principal

Programación e ingeniería de software con Java moderno y la plataforma JVM.

## Alcance

El curso cubre cuatro capas conectadas:

1. **Lenguaje Java**: sintaxis, tipos, POO, excepciones, generics, Collections, lambdas,
   programación funcional, Streams, módulos, annotations, reflection, assertions e internacionalización.
2. **Biblioteca y aplicaciones**: I/O/NIO, XML, networking/HTTP, JDBC, persistencia, JavaFX,
   AWT/Swing/Graphics2D, Compiler API/scripting, testing, logging, Maven y Gradle.
3. **Concurrencia**: threads, Java Memory Model, sincronización, java.util.concurrent,
   Executors, Fork/Join, CompletableFuture, virtual threads y concurrencia estructurada,
   distinguiendo claramente concurrencia, paralelismo, multihilo y asincronía.
4. **JVM y producción**: class files, bytecode, class loading, memoria, GC, JIT, FFM/native interop,
   profiling, JFR/JMC, JMH, performance, seguridad, observabilidad y troubleshooting.

## Plataforma de referencia

- OpenJDK moderno.
- Linux como entorno principal de laboratorio.
- PostgreSQL como base de datos relacional principal para JDBC.
- JavaFX como GUI desktop principal; AWT/Swing se estudian para cobertura de Java SE/Core Java y legado.
- Maven y Gradle como herramientas de build.
- JUnit, Mockito y Testcontainers para testing.
- HikariCP para prácticas de connection pooling.

Las APIs que sean Preview, Incubator o cuyo estado cambie entre versiones del JDK deben
enseñarse indicando explícitamente su estado en el JDK objetivo, evitando presentar una API
experimental como estable.

## Principios pedagógicos

- De fundamentos a internals.
- Primero Java estándar; frameworks después de comprender la abstracción subyacente.
- JDBC antes de JPA/Hibernate.
- Thread/synchronization/JMM antes de abstracciones concurrentes superiores.
- Future antes de CompletableFuture.
- Platform threads antes de virtual threads.
- Medición antes de optimización.
- CLI del JDK además del IDE.
- Cada concepto importante debe acompañarse de código ejecutable.
- Los errores, límites y anti-patrones forman parte del aprendizaje.

## Herramientas CLI que deben aparecer durante el curso

`java`, `javac`, `jshell`, `javap`, `jar`, `javadoc`, `jdeps`, `jlink`, `jpackage`,
`jcmd`, `jps`, `jstack`, `jmap`, `jstat`, `jinfo` y las herramientas de JFR/JMC
cuando correspondan.

## Fuera del núcleo inicial

Spring/Spring Boot, Jakarta EE, Android y sistemas distribuidos empresariales completos
pueden constituir PATHs posteriores. Este curso prepara sus fundamentos sin convertir
frameworks externos en sustitutos del conocimiento de Java/JVM.
