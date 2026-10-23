# Bibliografía — Java 0 → Experto en profundidad

## Libro troncal

### Cay S. Horstmann — *Core Java, Volumes I & II*, 14th Edition

Es la referencia principal del PATH. Debe utilizarse como columna vertebral para el lenguaje,
biblioteca estándar, orientación a objetos, Collections, concurrencia, I/O, networking,
internacionalización, seguridad y características modernas de Java cubiertas por la edición.

**Uso:** transversal a prácticamente todo el curso.

---

## Fundamentos y aprendizaje inicial

### Kathy Sierra, Bert Bates, Trisha Gee — *Head First Java*, 3rd Edition

Complemento pedagógico para los primeros bloques, especialmente objetos, referencias,
polimorfismo, excepciones, colecciones, lambdas y fundamentos de concurrencia.

**Bloques:** 0–7, 11–14 y fundamentos de 22.

### Chris Mayfield, Allen B. Downey — *Think Java*, 2nd Edition

Útil para razonamiento computacional, fundamentos, métodos, arrays, objetos, algoritmos y
resolución progresiva de problemas.

**Bloques:** 1–6 y laboratorios iniciales.

### Marc Loy, Patrick Niemeyer, Daniel Leuck — *Learning Java: An Introduction to Real-World Programming with Java*

Referencia práctica amplia para lenguaje, APIs y construcción de aplicaciones reales.

**Bloques:** fundamentos, I/O, networking, concurrencia y aplicaciones.

### *Java in a Nutshell*, 8th Edition

Referencia compacta del lenguaje, plataforma y APIs. Especialmente útil una vez superados
los fundamentos.

**Uso:** consulta transversal y consolidación.

---

## Recetas y práctica

### Ian F. Darwin — *Java Cookbook*, 5th Edition

Colección de soluciones y técnicas prácticas. No sustituye al libro troncal: se utiliza para
ampliar laboratorios y mostrar soluciones idiomáticas a problemas concretos.

**Bloques:** transversal; especialmente Strings, uso de regex desde Java, números, fechas,
I/O, networking, Collections, concurrencia y aplicaciones. En regex se utiliza únicamente
para la integración con las APIs Java (`Pattern`, `Matcher`, `String`, Streams, etc.); la
teoría y sintaxis de expresiones regulares pertenecen al PATH Regex.

---

## Expresiones regulares — integración con Java

Las expresiones regulares tienen un PATH especializado independiente. Este curso de Java
**no duplica la enseñanza de Regex**.

En Java se estudia cómo aplicar patrones previamente aprendidos mediante:

- `java.util.regex.Pattern`;
- `java.util.regex.Matcher`;
- operaciones regex de `String`;
- grupos y grupos nombrados desde la API;
- búsqueda, extracción, sustitución y tokenización;
- `Matcher.results()` y Streams;
- escaping entre literales Java y patrones;
- Unicode;
- `PatternSyntaxException`;
- reutilización de `Pattern`, rendimiento y thread-safety;
- integración con I/O y procesamiento de texto.

**Bloque principal:** 16.

Para sintaxis, construcción de patrones, metacaracteres, cuantificadores, alternancia,
lookarounds, backreferences, teoría de motores y regex avanzado, utilizar el PATH Regex.

---

## Generics y Collections

### Maurice Naftalin, Philip Wadler — *Java Generics and Collections*, 2nd Edition: Fundamentals and Recommended Practices

Referencia especializada para estudiar el sistema de tipos genérico y Collections más allá
del uso superficial.

**Bloques principales:** 10 y 11.

Temas prioritarios:
- bounded type parameters;
- wildcards;
- PECS;
- variance/invariance;
- type erasure;
- bridge methods;
- heap pollution;
- diseño de APIs genéricas;
- elección y uso correcto de colecciones.

---

## Big-O — aplicación dentro de Java

Big-O dispone de un PATH especializado independiente. Este curso de Java **no duplica la teoría general de complejidad algorítmica**.

En Java se estudia cómo aplicar ese conocimiento a código y APIs concretas: arrays, Collections, hashing, árboles, queues/deques, Strings, Streams, recursividad, I/O, JDBC, concurrencia y decisiones de rendimiento. También se distingue explícitamente el análisis asintótico de la medición empírica con JMH y de factores propios de la JVM como JIT, GC, allocations y locality.

**Bloque principal:** 12.

Referencias Java de apoyo: *Core Java, Volumes I & II*, *Java Generics and Collections*, *Think Java* y *Java Performance*. Para la teoría matemática y algorítmica completa se utiliza el PATH Big-O.

---

## Programación funcional

### Ben Weidig — *A Functional Approach to Java*

Referencia principal para el salto desde lambdas/Streams hacia pensamiento funcional en Java.

**Bloques principales:** 13–15.

Temas:
- funciones y composición;
- inmutabilidad;
- higher-order functions;
- Optional;
- Streams;
- lazy evaluation;
- diseño declarativo y funcional.

---

## Concurrencia, multihilo y async

### A N M Bazlur Rahman — *Modern Concurrency in Java*

Referencia especializada para concurrencia moderna.

**Bloques principales:** 23–29.

El PATH debe usarla para conectar:
`Thread → sincronización → JMM → java.util.concurrent → Executors → Future →
CompletableFuture → virtual threads → concurrencia estructurada`.

Las APIs modernas que cambien de estado entre releases deben contrastarse con la
documentación del JDK utilizado.

---

## Performance y JVM

### Scott Oaks — *Java Performance: In-Depth Advice for Tuning and Programming Java 8, 11, and Beyond*

Referencia principal de performance.

**Bloques principales:** 39–45, 50 y 53.

Temas:
- JVM;
- memoria;
- garbage collection;
- JIT;
- threads;
- profiling;
- medición;
- rendimiento de aplicaciones.

Debe complementarse con documentación actual del JDK porque algunos collectors, defaults,
flags y herramientas evolucionan entre versiones.

---

## Desarrollo de software real

### Raoul-Gabriel Urma, Richard Warburton — *Real-World Software Development*

Referencia para conectar conocimiento del lenguaje con diseño mantenible, testing,
refactoring y organización de aplicaciones.

**Bloques principales:** 35, 46–48, 52 y proyectos.

---


## Áreas de Core Java Vol. I & II, 14th Edition presentes en el PATH

El PATH incluye explícitamente las siguientes áreas. Esta lista acredita cobertura
temática; no certifica equivalencia exhaustiva capítulo por capítulo con el libro:

- assertions dentro del bloque de excepciones;
- XML (DOM, SAX, StAX, XPath, XSLT y seguridad);
- internationalization (Locale, ResourceBundle, formatos, Collator y Unicode);
- Compiler API y scripting;
- AWT, Swing y Graphics2D, aunque JavaFX siga siendo la GUI principal del curso;
- Foreign Function & Memory API (FFM) e interoperabilidad nativa.

**Bloques principales añadidos:** 55–60, además de la ampliación del bloque 7.

---

# Referencias oficiales imprescindibles

Además de los libros, el curso debe consultar las fuentes oficiales correspondientes al JDK
objetivo:

- Java Language Specification (JLS).
- Java Virtual Machine Specification (JVMS).
- Java SE API Documentation.
- OpenJDK JEP Index.
- Documentación de herramientas del JDK.
- JavaFX/OpenJFX documentation para los bloques GUI.
- Java SE AWT/Swing/2D API documentation.
- Java XML processing APIs (JAXP) documentation.
- Foreign Function & Memory API documentation del JDK objetivo.
- Java Compiler API (`javax.tools`) y JShell API documentation.
- JDBC specification/API documentation para persistencia relacional.

Estas fuentes tienen prioridad para comprobar sintaxis, semántica, estado de APIs,
características Preview/Incubator y comportamiento específico de una versión.

---

# Mapa resumido libro → área

| Área | Referencia principal |
|---|---|
| Curso completo | Core Java Vol. I & II, 14th |
| Introducción | Head First Java 3rd |
| Pensamiento/programación básica | Think Java 2nd |
| Java práctico | Learning Java |
| Consulta | Java in a Nutshell 8th |
| Recetas | Java Cookbook 5th |
| Generics/Collections | Java Generics and Collections 2nd |
| Funcional | A Functional Approach to Java |
| Concurrencia | Modern Concurrency in Java |
| JVM/Performance | Java Performance |
| Ingeniería de software | Real-World Software Development |

# Estrategia de lectura

No es necesario leer todos los libros secuencialmente. `Core Java` actúa como texto
principal. Los demás entran cuando el PATH alcanza su especialidad. La documentación oficial
se usa continuamente para verificar el comportamiento de la versión moderna del JDK.


## Fuentes oficiales concretas para la base JDK 25

Consultadas para la revisión del 19 de octubre de 2026. El estado indicado se
refiere al JDK 25 elegido, no al último JDK que pudiera existir.

- [JLS 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html):
  sintaxis, tipos, inicialización, sobrecarga, excepciones y modelo de memoria.
- [JVMS 25](https://docs.oracle.com/javase/specs/jvms/se25/html/index.html):
  class files, bytecode, carga, linking e inicialización.
- [API Java SE 25](https://docs.oracle.com/en/java/javase/25/docs/api/index.html):
  contratos exactos de las clases y métodos usados en cada lección.
- [Preview APIs de JDK 25](https://docs.oracle.com/en/java/javase/25/docs/api/preview-list.html):
  Structured Concurrency es quinta preview; no presentarla como API final.
- [Cambios del lenguaje por versión](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-release.html):
  archivos compactos, main de instancia, imports de módulos y constructores flexibles.
- [Sequenced Collections](https://docs.oracle.com/en/java/javase/21/core/creating-sequenced-collections-sets-and-maps.html):
  interfaces incorporadas en JDK 21; contratos actuales en la API 25.
- [Cambios JDK 24](https://docs.oracle.com/en/java/javase/25/migrate/significant-changes-jdk-24.html):
  Gatherers, Class-File API, virtual threads y restricciones de interoperabilidad.
- [Cambios JDK 25](https://docs.oracle.com/en/java/javase/25/migrate/significant-changes-jdk-25.html):
  ScopedValue, AOT caches y evolución de la plataforma.
- [ScopedValue](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ScopedValue.html):
  contexto léxico final desde Java 25.
- [Structured Concurrency](https://docs.oracle.com/en/java/javase/25/core/structured-concurrency.html):
  laboratorio separado y fijado a JDK 25 con preview habilitada.
- [FFM](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/foreign/package-summary.html):
  API estable desde JDK 22; lifetime, layouts y native access del JDK elegido.
- [Página del autor de Core Java](https://horstmann.com/corejava/):
  edición 14, código de ejemplos y erratas.
- [Ficha editorial de Java Generics and Collections, 2nd Edition](https://www.oreilly.com/library/view/java-generics-and/9781098136710/):
  autoría acreditada: Maurice Naftalin y Philip Wadler.

## Lectura y trazabilidad de la revisión

| Área | Bloques | Evidencia requerida al generar las lecciones |
|---|---|---|
| Lenguaje y objetos | 0–10, 17, 51 | Sección de JLS/API y pruebas de contratos |
| Collections y complejidad aplicada | 11–12 | API concreta y supuestos de coste |
| Funcional y texto | 13–16 | Contratos de Streams y regex de Java |
| I/O y red | 18–20 | API, ownership y cierre de recursos |
| Reflection y compilación | 21–22, 57 | API y límites de encapsulación |
| Concurrencia | 23–29 | JMM, contratos, estado final/preview y pruebas |
| Persistencia | 30–32 | JDBC, documentación pgJDBC y proveedor ORM |
| Desktop | 33–34, 58–59 | OpenJFX y API Java desktop |
| Ingeniería | 35–38, 46–50, 52–54 | Documentación de herramientas fijadas |
| JVM y medición | 39–45 | JVMS, documentación JDK y JMH |
| i18n y XML | 55–56 | API y configuración segura |
| Interoperabilidad | 60 | API FFM, ABI y biblioteca del laboratorio |

La lectura especializada de performance se retoma después de aprender las APIs
que se miden. La comprobación con JMH del bloque 12 se realiza tras 45.
Para afirmar cobertura exhaustiva de Core Java se requiere todavía una matriz
capítulo/sección del índice de ambos volúmenes frente a IDs del PATH; no se
inventa esa equivalencia a partir de títulos generales.
