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

**Bloques:** transversal; especialmente Strings, regex, números, fechas, I/O, networking,
Collections, concurrencia y aplicaciones.

---

## Generics y Collections

### Maurice Naftalin, Philip Wadler, Stuart Marks — *Java Generics and Collections*, 2nd Edition: Fundamentals and Recommended Practices

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

## Programación funcional

### Ben Weidig — *A Functional Approach to Java*

Referencia principal para el salto desde lambdas/Streams hacia pensamiento funcional en Java.

**Bloques principales:** 12–14.

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

**Bloques principales:** 22–28.

El PATH debe usarla para conectar:
`Thread → sincronización → JMM → java.util.concurrent → Executors → Future →
CompletableFuture → virtual threads → concurrencia estructurada`.

Las APIs modernas que cambien de estado entre releases deben contrastarse con la
documentación del JDK utilizado.

---

## Performance y JVM

### Scott Oaks — *Java Performance: In-Depth Advice for Tuning and Programming Java 8, 11, and Beyond*

Referencia principal de performance.

**Bloques principales:** 38–44, 49 y 52.

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

**Bloques principales:** 34, 45–47, 51 y proyectos.

---


## Cobertura explícita de Core Java Vol. I & II, 14th Edition

Para asegurar que el PATH no omita capítulos del libro troncal, se estudian explícitamente:

- assertions dentro del bloque de excepciones;
- XML (DOM, SAX, StAX, XPath, XSLT y seguridad);
- internationalization (Locale, ResourceBundle, formatos, Collator y Unicode);
- Compiler API y scripting;
- AWT, Swing y Graphics2D, aunque JavaFX siga siendo la GUI principal del curso;
- Foreign Function & Memory API (FFM) e interoperabilidad nativa.

**Bloques principales añadidos:** 54–59, además de la ampliación del bloque 7.

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
