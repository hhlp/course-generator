# Domain — Java 0 → Experto en profundidad

## Dominio principal

Programación e ingeniería de software con Java moderno y la plataforma JVM.

## Alcance

El curso cubre cuatro capas conectadas:

1. **Lenguaje Java**: sintaxis, tipos, POO, excepciones, generics, Collections, lambdas,
   programación funcional, Streams, módulos, annotations, reflection, assertions, internacionalización,
   uso de expresiones regulares mediante las APIs de Java y aplicación de Big-O al código y APIs Java.
2. **Biblioteca y aplicaciones**: I/O/NIO, XML, networking/HTTP, JDBC, persistencia, JavaFX,
   AWT/Swing/Graphics2D, Compiler API/scripting, testing, logging, Maven y Gradle.
3. **Concurrencia**: threads, Java Memory Model, sincronización, java.util.concurrent,
   Executors, Fork/Join, CompletableFuture, virtual threads y concurrencia estructurada,
   distinguiendo claramente concurrencia, paralelismo, multihilo y asincronía.
4. **JVM y producción**: class files, bytecode, class loading, memoria, GC, JIT, FFM/native interop,
   profiling, JFR/JMC, JMH, performance, seguridad, observabilidad y troubleshooting.

## Relación con los PATHs especializados

Big-O y Regex se consideran competencias transversales con PATH propio. Java no reenseña sus fundamentos generales: estudia su aplicación concreta dentro del lenguaje, biblioteca y JVM.

### Relación con el PATH Big-O

El curso aplica análisis de complejidad a arrays, Collections, Strings, Streams, recursividad, I/O, JDBC y concurrencia; compara estructuras según sus operaciones dominantes y separa complejidad asintótica de benchmarking, JIT, GC, allocations y costes constantes. La teoría matemática general, notaciones asintóticas y técnicas generales de análisis pertenecen al PATH Big-O.

### Relación con el PATH Regex

Regex se considera una competencia transversal con PATH propio. Este dominio no reenseña la
sintaxis ni la teoría general de expresiones regulares. El curso Java cubre en profundidad
su **aplicación dentro de Java**: `Pattern`, `Matcher`, APIs de `String`, Streams, escaping,
Unicode, manejo de errores, rendimiento, reutilización, thread-safety e integración con I/O
y procesamiento de texto.

## Plataforma de referencia

- OpenJDK 25 como plataforma base; registrar distribución y actualización exacta.
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


## Contrato de versión y reproducibilidad

La referencia del curso es Java SE/OpenJDK 25. Esto es una elección de plataforma,
no una afirmación de que sea la última versión disponible. `javac --release 25`
y un runtime JDK 25 se utilizan en el recorrido base. Se registra distribución,
actualización exacta y salida de `java -version`/`javac -version` en cada entrega.

Las versiones exactas de Maven/Gradle Wrapper, plugins, JUnit, Mockito,
Testcontainers, JavaFX, PostgreSQL JDBC, HikariCP e Hibernate se fijan en el
proyecto del laboratorio después de comprobar compatibilidad con JDK 25.
No usar versiones dinámicas, rangos abiertos o `latest`. Este PATH no entrega
un proyecto ejecutable ni certifica todavía esa matriz de dependencias.
JavaFX se instala como dependencia externa y se comprueba el runtime OCI
requerido por Testcontainers; esos componentes no vienen incluidos en OpenJDK.

| Característica | Estado en la base JDK 25 | Ubicación |
|---|---|---|
| Sequenced Collections | Final desde 21 | 11 |
| FFM, java.lang.foreign | Final desde 22 | 60 |
| Stream Gatherers | Final desde 24 | 15 |
| Class-File API | Final desde 24 | 40 |
| ScopedValue | Final en 25 | 29 |
| Compact source files y main de instancia | Final en 25 | 0 y 51 |
| Module import declarations | Final en 25 | 9 y 51 |
| Flexible constructor bodies | Final en 25 | 4 y 51 |
| Structured Concurrency | Quinta preview en 25 | 29, módulo separado |

Los ejemplos preview requieren JDK 25 tanto al compilar como al ejecutar,
`javac --enable-preview --release 25` y `java --enable-preview`.
No copiar ejemplos de otras previews sin adaptar y verificar su API.
La documentación normativa de API/JLS tiene prioridad frente a resúmenes de cambios.

## Progresión y dependencias

Los 61 bloques (0–60) y los identificadores originales se conservan. Las
ampliaciones se añaden al final de las lecciones de su bloque. La ruta anotada
en `initial.txt` forma parte del contrato docente: los IDs no obligan a ejecutar
un laboratorio antes de comprender sus dependencias.

| Etapa | Dependencia y entrega |
|---|---|
| Inicio | Build mínimo y JUnit en 0; pruebas de métodos desde 2 |
| Tipos | Wrappers/boxing en 4 antes de 10–11; consolidación en 17 |
| Enums | 8.3 introduce; 11 desarrolla EnumSet/EnumMap |
| Big-O aplicado | 12 por etapas; Streams tras 15, I/O tras 19, JDBC tras 32 |
| Big-O concurrente | Tras 29; rendimiento/memoria y JMH tras 41–45 |
| Networking | 20 síncrono; threads tras 26 y HTTP async tras 27 |
| Dinamismo | Reflection en 21 y laboratorio combinado tras 22 |
| Testing | Transversal desde 0; profundización en 35 |
| Entrega final | Base en 54; defensa e integración después de 60 |

El PATH Regex aporta la construcción de patrones antes de 16; el PATH Big-O
aporta fundamentos de análisis antes de 12. No se exige completar ambos PATHs
enteros antes de comenzar Java. En Java se evalúa el uso de sus APIs y contratos.

## Evaluación y laboratorio

Cada lección declara objetivo observable, prerrequisitos concretos, código y
comandos completos, salida esperada, errores y límites. Cada práctica incluye
pruebas reproducibles y limpieza de threads, streams, conexiones y procesos.
No usar tiempos de sleep ni el resultado de una sola ejecución como prueba de
corrección concurrente. Las mediciones separan análisis asintótico y rendimiento.

Para superar un proyecto: compilar con la plataforma declarada; pasar pruebas
positivas, negativas y de frontera; justificar contratos; demostrar liberación
de recursos; documentar cómo reproducir y diagnosticar un fallo. Los proyectos
con BD tienen pruebas de rollback/aislamiento y los de GUI verifican el límite
entre UI y background. El cierre incluye un incidente reproducible y un informe
de medición con sus límites. Los bloques 55–60 se estudian completos; el proyecto
solo integra extensiones que respondan a requisitos concretos.

## Integración con course-generator

Distribución prevista en el repositorio: `paths/java/initial.txt` y
`profiles/java/{profile.yaml,domain.md,bibliography.md}`. Desde ese directorio
de perfil, `../../config/pedagogy.md` apunta a `config/pedagogy.md`.
La existencia de esa ruta y la interpretación de campos del perfil deben
comprobarse con el repositorio y su cargador. Esta revisión valida los archivos
estáticos; no ejecuta course-generator ni genera todas las lecciones.
Los campos adicionales de evaluación/versionado son instrucciones docentes;
no presuponen nuevas opciones de CLI ni funcionalidad del generador.
