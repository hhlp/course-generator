# Domain — Scrum 0 → Experto

## Propósito

Este PATH forma a un Scrum Master desde cero hasta un nivel avanzado de práctica profesional.
La progresión está separada por tres hitos: PSM I, PSM II y PSM III. El objetivo no es
memorizar preguntas de examen, sino comprender Scrum desde sus primeros principios y ser
capaz de aplicarlo, explicarlo, enseñarlo, facilitarlo y defender decisiones en contextos reales.

## Regla de autoridad

La fuente normativa para Scrum es **The Scrum Guide** vigente. Las lecciones deben distinguir
siempre entre:

1. **Elementos de Scrum**: teoría, valores, Scrum Team y accountabilities, events, artifacts,
   commitments y Definition of Done.
2. **Prácticas complementarias compatibles con Scrum**: User Stories, Acceptance Criteria,
   Definition of Ready, Story Points, Planning Poker, velocity, Burndown, Burnup, Scrum Board,
   CFD, Kanban, Monte Carlo, Liberating Structures, etc.
3. **Anti-patrones o usos peligrosos**: convertir velocity en objetivo, comparar equipos por
   Story Points, tratar Daily Scrum como status meeting, hardening Sprints, QA Sprints, etc.

Nunca presentar una práctica opcional como requisito del Scrum Guide.

## Hito PSM I

Debe producir dominio sólido de Scrum: empirismo, Scrum Values, accountabilities, events,
artifacts, commitments, Done, self-management y aplicación fundamental. El alumno debe
poder reconocer mitos y distinguir Scrum de prácticas añadidas.

## Hito PSM II

Debe pasar del conocimiento a la aplicación avanzada: liderazgo, coaching, mentoring,
teaching, facilitación, conflictos, equipos self-managing, Product Ownership, stakeholders,
impedimentos organizacionales, métricas y comportamiento sistémico.

## Hito PSM III

Debe desarrollar razonamiento profesional distinguido: explicar decisiones desde principios,
trabajar con ambigüedad, coaching sistémico y organizacional, cambio, valor, liderazgo,
facilitación avanzada y argumentación escrita precisa en inglés.

## Estimación y producto

Cubrir sizing, estimación relativa, Story Points, Planning Poker, Affinity Estimation,
T-Shirt Sizing, Bucket System, Three-Point Estimation, PERT, Wideband Delphi, Reference
Stories, triangulación y No Estimates. Enseñar que Scrum no prescribe Story Points ni
Planning Poker.

Cubrir Product Goal, Product Backlog, refinement, User Stories, 3 Cs, INVEST, Acceptance
Criteria, Given/When/Then, slicing vertical, spikes y Definition of Ready como práctica
opcional.

## Definition of Done

DoD debe estudiarse en profundidad por ser parte formal de Scrum. Cubrir calidad, Increment,
estándares organizacionales, múltiples equipos, testing, integración, seguridad, documentación,
CI/CD, DevOps, deuda técnica y evolución de la DoD. Diferenciar DoD, Acceptance Criteria y DoR.

## Charts, métricas y forecasting

Cubrir Sprint Burndown, Product/Release Burndown, Burnup, Velocity Chart, Cumulative Flow
Diagram, Control Chart, Cycle Time Scatterplot, histogramas de Cycle Time, Aging Work in
Progress Chart, Throughput Run Chart, WIP Chart y dashboards.

Antes de construir los charts, enseñar explícitamente la procedencia y el modelo de los datos.
Distinguir Product Backlog, Sprint Backlog y registros del workflow como posibles fuentes.
El alumno debe comprender cómo un PBI o Work Item genera observaciones como estado, fecha
de inicio, fecha de finalización, timestamps de transición, trabajo restante, trabajo completado,
scope y, cuando el equipo haya elegido esa práctica, Story Points.

Story Points no son prescritos por Scrum y no deben presentarse como requisito para generar
métricas o charts. Explicar qué visualizaciones pueden construirse usando Story Points y cuáles
pueden trabajar con conteo de items, fechas, estados o tiempos. En particular, mostrar Sprint
Burndown con y sin Story Points; Velocity Chart cuando se utiliza sizing mediante Story Points;
y flow metrics basadas principalmente en items y tiempo.

La progresión pedagógica para cada visualización debe ser:

fuente de datos → dataset → métrica/cálculo → construcción del chart → actualización →
interpretación → patrones/anomalías → limitaciones → decisiones posibles.

Los charts no deben enseñarse únicamente como conceptos. Para cada visualización relevante,
el alumno debe aprender qué pregunta responde, qué datos necesita, cómo obtener y preparar
esos datos, qué cálculos son necesarios, cómo construir el chart paso a paso, cómo actualizarlo,
cómo interpretarlo y cuáles son sus limitaciones, patrones engañosos y anti-patrones de uso.

Los laboratorios deben partir de datasets concretos y exigir construir manualmente las
visualizaciones principales antes de interpretar sus resultados. Incluir un laboratorio que
derive un dataset desde Product Backlog/Sprint Backlog y otro que compare el mismo Sprint
representado mediante Story Points y mediante conteo de items.

Los laboratorios deben incluir al menos Burndown, Burnup, Velocity Chart, CFD, Cycle Time
Scatterplot, histograma de Cycle Time, Aging WIP, Throughput Run Chart y WIP Chart. También
debe practicarse la comparación de varios charts construidos a partir del mismo dataset y la
selección de la visualización adecuada según la pregunta que se intenta responder.

Cubrir WIP, throughput, lead time, cycle time, work item age, SLE y flow efficiency,
incluyendo su cálculo e interpretación, y conectarlos posteriormente con forecasting
probabilístico mediante Monte Carlo. Las métricas deben apoyar transparencia, empirismo,
inspección, adaptación y decisiones; no convertirse en objetivos de productividad individual.

## Retrospectivas

Profundizar en diseño, facilitación, seguridad, generación de insights, acciones y seguimiento.
Incluir Retrospectives Antipatterns como fuente práctica para diagnosticar retrospectivas
disfuncionales.

## Zombie Scrum

Utilizar Zombie Scrum Survival Guide para detectar Scrum mecánico: eventos sin propósito,
falta de Increment usable, ausencia de stakeholders, poca autonomía, Product Ownership débil
y mejora continua inexistente. El objetivo es aprender recuperación, no crear una variante
del framework.

## Professional Scrum Team

Estudiar el Scrum Team como unidad: cross-functionality, self-management, colaboración,
calidad, ownership, Product Goal, Sprint Goal, Done y profesionalismo. Evitar dividir el
aprendizaje en silos artificiales de roles.

## Nexus

Nexus se estudia después de dominar Scrum. Debe enseñarse como extensión mínima de Scrum
para múltiples Scrum Teams trabajando sobre un único producto, no como sustituto de Scrum.
Cubrir Nexus Integration Team, Cross-Team Refinement, Nexus events, Nexus Sprint Backlog,
Nexus Sprint Goal, Integrated Increment, dependencias e integración.

## Estilo de las lecciones

Cada lección comienza con **🎯 OBJETIVO** y termina con **🧠 QUÉ DEBES RECORDAR** con 3–7
ideas esenciales. Cuando aporten valor, incluir **🧪 Laboratorio/ejemplos**, **⚠️ Errores
frecuentes** y **💡 Idea importante**.

Las explicaciones deben ser profundas, didácticas y orientadas a escenarios. Para PSM II y
PSM III se prioriza el razonamiento sobre la memorización. En PSM III se practicarán respuestas
escritas en inglés.

## Resultado esperado

Al terminar, el alumno debe poder explicar Scrum con precisión, aplicar sus principios,
facilitar equipos y eventos, trabajar con Product Owners y stakeholders, utilizar métricas
sin abusar de ellas, ayudar a eliminar impedimentos, trabajar sobre cambio organizacional,
escalar un producto mediante Nexus y razonar al nivel exigible en PSM I, PSM II y PSM III.


## Profundidad transversal obligatoria — práctica profesional

Para cada tema de liderazgo, coaching, facilitación, conflictos, cambio organizacional, escalado y PSM III, seguir la secuencia: **concepto → fundamentos → contexto → aplicación → ejemplo → escenario complejo → intervención → consecuencias → anti-patrones → laboratorio → evaluación**. Explicar tanto cuándo intervenir como cuándo no intervenir. Distinguir claramente reglas del Scrum Guide, guías complementarias y propuestas de autores.

### Coaching, equipos y facilitación

Enseñar diagnóstico de contexto, escucha, preguntas abiertas, acuerdos, límites éticos, conflictos, decisiones inclusivas, diseño de sesiones y evaluación de sus efectos. Los laboratorios deben incluir guiones, transcripciones o registros de decisiones y una revisión crítica posterior. No confundir coaching profesional con terapia ni con evaluación jerárquica.

### Sistemas y cambio organizacional

Exigir mapas de actores, dependencias y causalidad; diferenciar síntomas de hipótesis de causa; estudiar incentivos, consecuencias no intencionadas y experimentos reversibles. Incluir evidencia previa, criterio de éxito, fecha de revisión y aprendizaje posterior.

### Forecasting y Evidence-Based Management

Utilizar datasets documentados, comprobar consistencia de timestamps y estados, explicitar supuestos, realizar análisis de sensibilidad y comunicar incertidumbre. Los experimentos de valor deben distinguir outputs de outcomes y no convertir métricas en objetivos individuales.

### Nexus y escalado

Trabajar con escenarios de integración fallida, dependencias cruzadas y responsabilidad del Nexus Integration Team. Contrastar cada regla formal con la versión vigente de The Nexus Guide; no presentar las técnicas de arquitectura como elementos obligatorios del framework.

### Evaluación de PSM III y proyecto final

Practicar respuestas escritas en inglés con rúbricas: precisión respecto a Scrum, reconocimiento de contexto y supuestos, alternativas, razonamiento empírico, Scrum Values, efectos secundarios y claridad. No prometer equivalencia con exámenes oficiales. El proyecto final debe aportar registros de decisiones, datasets reproducibles, charts, evidencias de facilitación, mapa sistémico, experimentos y defensa crítica.

### Reglas de preservación y evaluación

Mantener la progresión PSM I → PSM II → PSM III, sin eliminar temas originales. Cada laboratorio debe definir situación inicial, objetivo, datos/recursos, pasos, entregables, criterios de evaluación, errores frecuentes y reflexión. No sustituir práctica profesional real por aprobar simulacros.


## Sprint Backlog — gestión operativa y cambios durante el Sprint

Enseñar de manera explícita cómo los Developers construyen y mantienen el Sprint Backlog: Sprint Goal, PBIs seleccionados y plan accionable. Cubrir Sprint Planning, capacidad, desglose opcional en tareas, actualización diaria, trabajo descubierto, seguimiento del Sprint Goal, transparencia y Definition of Done. Los Developers son responsables del Sprint Backlog; el Scrum Master facilita la comprensión de Scrum y la autogestión, sin asignar tareas ni convertirse en administrador del artefacto.

Diferenciar las decisiones del Product Owner (ordenación y valor del Product Backlog) de las decisiones de los Developers (plan y adaptación del Sprint Backlog). Explicar cómo se negocia con el Product Owner el alcance cuando se aprende más, sin realizar cambios que pongan en peligro el Sprint Goal y sin reducir la calidad. Scrum no prescribe un workflow, una herramienta de tickets ni una política específica de hotfixes.

### Bugs, hotfixes, incidentes y PBIs nuevos

Comparar defectos descubiertos en el trabajo del Sprint, bugs existentes en producción, incidentes urgentes, hotfixes y solicitudes de funcionalidad. No afirmar que todo trabajo inesperado deba convertirse necesariamente en un PBI antes de actuar; explicar cuándo registrar un PBI, cuándo actualizar directamente el plan de los Developers y cómo mantener la trazabilidad. Para un nuevo PBI que se considere durante el Sprint, enseñar evaluación de valor y urgencia con el Product Owner, capacidad e impacto por los Developers, adaptación del Sprint Backlog y comunicación transparente.

Incluir criterios de severidad, riesgo, impacto de cliente, regresión, pruebas, Definition of Done, política de incidentes y alternativas ante compromisos de capacidad. Distinguir trabajo no Done al finalizar el Sprint de un Increment terminado y evitar atribuir al Scrum Master autoridad para imponer o aprobar cambios de alcance.

### Laboratorios obligatorios

1. Construir un Sprint Backlog desde un Product Backlog y un Sprint Goal, con plan y capacidad explícitos.
2. Simular actualizaciones diarias, nuevos hallazgos, dependencias y trabajo bloqueado.
3. Incorporar un bug durante el Sprint justificando su tratamiento y documentando cambios.
4. Simular un hotfix de producción crítico en el día 5 de un Sprint de dos semanas, con evaluación de urgencia, decisiones del Product Owner y Developers, alternativas, pruebas y protección del Sprint Goal.
5. Renegociar alcance y evaluar el trabajo no Done al finalizar el Sprint.

Cada laboratorio debe aportar Sprint Backlog antes/después, decisiones y responsables, efecto sobre el Sprint Goal, evidencia de calidad, cambios de scope y reflexión crítica. Conectar con los bloques 7, 8 y 19 para capacity, charts y WIP sin repetir sus explicaciones completas.
