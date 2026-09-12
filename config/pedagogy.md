# PEDAGOGY — CURSOS TÉCNICOS EN PROFUNDIDAD

## Propósito

Este archivo define las reglas pedagógicas comunes para todos los perfiles del generador.
El objetivo es producir lecciones técnicas profundas, progresivas, auditables y útiles para
estudio real, evitando resúmenes superficiales y plantillas genéricas.

## Principios generales

1. Cada lección debe enseñar exactamente el tema indicado por el PATH.
2. La profundidad debe venir del contenido técnico, no de repetir definiciones ni de añadir
   secciones artificiales.
3. La lección debe ser autocontenida respecto a su objetivo, pero respetar la progresión del PATH.
4. No adelantar contenidos pertenecientes claramente a lecciones posteriores salvo una mención
   mínima necesaria para situar el concepto.
5. No repetir en detalle contenidos ya enseñados en lecciones anteriores; reutilizarlos como
   conocimientos previos cuando corresponda.
6. Explicar no sólo qué es algo, sino por qué existe, cómo funciona, qué problema resuelve,
   cuáles son sus límites y cómo se reconoce en la práctica.
7. Distinguir conceptos próximos que puedan confundirse.
8. Los ejemplos deben ser específicos del tema y verificables.
9. Cuando un experimento o laboratorio aporte valor, debe permitir observar una propiedad concreta,
   no ser una secuencia de comandos sin interpretación.
10. Los errores frecuentes deben ser reales y pedagógicamente relevantes.
11. Nunca inventar resultados de comandos, referencias bibliográficas exactas, comportamiento de
    herramientas o detalles de implementación.
12. Si una característica depende de un dialecto, versión, motor, plataforma o implementación,
    indicarlo explícitamente.

## Estructura común de las lecciones

### 🎯 OBJETIVO

Debe ser siempre el primer apartado.

Debe indicar con precisión qué será capaz de comprender, distinguir, analizar o ejecutar el
estudiante al terminar la lección.

No debe ser una lista genérica ni una reformulación del título.

### 📚 LECTURA

Debe aparecer cuando el perfil lo requiera.

La lectura debe estar vinculada al tema concreto de la lección. Se pueden indicar fuentes,
capítulos, secciones o temas solamente cuando exista suficiente seguridad sobre la referencia.

Nunca inventar páginas, capítulos o secciones exactas.

### Desarrollo

La estructura interna debe adaptarse al tema.

No imponer siempre los mismos encabezados. Deben usarse títulos específicos que reflejen los
conceptos reales de la lección.

Cuando sea útil, explicar:

- modelo mental;
- terminología;
- sintaxis;
- semántica;
- funcionamiento interno;
- casos límite;
- diferencias entre alternativas;
- portabilidad;
- rendimiento;
- seguridad;
- diagnóstico;
- relación con conceptos anteriores y posteriores.

### 🧪 Laboratorio / ejemplos

Incluir cuando ayude a demostrar una propiedad o comportamiento.

Cada experimento debe dejar claro:

- qué se prueba;
- qué entrada se utiliza;
- qué se espera observar;
- qué conclusión debe obtener el estudiante.

### ⚠️ Errores frecuentes

Incluir cuando existan confusiones relevantes.

No fabricar errores sólo para llenar una sección.

### 💡 Idea importante

Incluir únicamente cuando exista una idea conceptual que merezca destacarse.

### 🧠 QUÉ DEBES RECORDAR

Debe ser siempre el último apartado cuando el perfil lo requiera.

Debe contener entre 3 y 7 ideas fundamentales de la lección.

No debe repetir literalmente el objetivo. Debe condensar los conocimientos que el estudiante
debería conservar después de estudiar el tema.

## Profundidad

Una lección profunda debe priorizar:

- precisión conceptual;
- causalidad;
- mecanismos;
- distinciones;
- evidencia;
- ejemplos;
- límites;
- consecuencias prácticas.

No usar longitud, número de apartados o cantidad de código como sustituto de profundidad.

## Progresión

El PATH es la autoridad sobre el orden pedagógico.

NEIGHBORS sirve para:

- evitar adelantar excesivamente contenidos posteriores;
- conectar la lección con lo inmediatamente anterior;
- preparar de forma controlada lo inmediatamente siguiente.

PROJECT_CONTEXT sirve para reutilizar artefactos reales cuando exista una dependencia física,
pero nunca debe convertir una dependencia de conocimiento en dependencia de archivos.

## Artefactos y proyectos

No toda lección necesita archivos o proyecto.

Elegir artefactos sólo cuando aporten valor pedagógico real.

Distinguir siempre:

- knowledge_dependencies: conocimientos necesarios;
- artifact_dependencies: archivos o proyectos que realmente deben reutilizarse.

Un proyecto diagnóstico debe ayudar a observar y correlacionar evidencia, no limitarse a ejecutar
comandos de forma mecánica.

## Auditoría

Una lección debe considerarse correcta sólo si:

- cumple el objetivo;
- cubre los conceptos obligatorios;
- respeta el alcance;
- no contradice DOMAIN;
- utiliza BIBLIOGRAPHY responsablemente;
- mantiene coherencia con el PATH;
- no inventa referencias;
- no usa una plantilla genérica en lugar de enseñar el tema;
- conserva la estructura obligatoria definida por PROFILE.
