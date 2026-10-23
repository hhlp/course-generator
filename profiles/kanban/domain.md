# Domain — Kanban 0 → Experto

## Modelo integrador

> **F4P = propósito/cliente; Upstream = demanda antes del compromiso; Kanban = flujo y delivery; KMM = cómo evoluciona todo el sistema organizacional hacia mayores capacidades.**

Este PATH trata los dominios como partes de un único sistema end-to-end.

- **Fit for Purpose (F4P):** descubre qué resultados, experiencia y criterios hacen que un servicio sea adecuado para un cliente en un contexto determinado.
- **Upstream Kanban:** gestiona demanda, opciones, discovery, selección, riesgo y commitment antes de introducir trabajo en delivery.
- **Kanban:** gestiona el flujo desde commitment hasta delivery mediante visualización, pull, WIP, políticas, métricas, cadencias y mejora evolutiva.
- **Kanban Maturity Model (KMM):** proporciona un mapa para evolucionar las capacidades organizacionales, seleccionar prácticas apropiadas al contexto y desarrollar agilidad, resiliencia y capacidad de reinvención.
- **Discovering Kanban:** aporta la visión sistémica y evolutiva que conecta servicios, organización, cambio, madurez y Enterprise Kanban.

## Flujo conceptual

Customer need → F4P / Fitness Criteria → Demand → Options → Discovery → Selection →
Commitment → Delivery Kanban → Outcome → Customer Feedback → aprendizaje.

KMM envuelve ese ciclo:

Capability actual → nivel/contexto → prácticas apropiadas → experimento evolutivo →
capability mejorada → nuevo contexto → siguiente evolución.

## KMM dentro del PATH

KMM no se enseña como una nota o ranking de organizaciones. Los Kanban Maturity
Levels se estudian como un mapa de capacidades y patrones que ayuda a decidir qué
cambios son razonables en cada contexto.

El bloque KMM estudia explícitamente ML0–ML6, sus características, capability,
prácticas, riesgos, transiciones, plateaus, posibles retrocesos y conexiones con
STATIK, F4P, Upstream, Portfolio y Enterprise Kanban.

## Alcance obligatorio

Pensamiento sistémico; servicios; principios Kanban; visualización; WIP; pull;
políticas; clases de servicio; métricas; CFD; aging; Little's Law; SLE;
forecasting probabilístico; Monte Carlo; cadencias; STATIK; service delivery;
F4P; Upstream; demand management; optionality; discovery; commitment;
replenishment; portfolio; riesgo; cost of delay; KMM; ML0–ML6; capability;
prácticas y transiciones de madurez; resiliencia; reinvención; redes de servicios;
Enterprise Kanban; analítica y troubleshooting.

## Contrato pedagógico

Cada lección comienza con `🎯 OBJETIVO` y termina con `🧠 QUÉ DEBES RECORDAR`
con 3–7 ideas esenciales. Se añaden `🧪 Laboratorio/ejemplos`,
`⚠️ Errores frecuentes` y `💡 Idea importante` cuando aportan valor.

La profundidad debe progresar desde modelo mental y mecanismo hasta aplicación,
diagnóstico y toma de decisiones. El PATH no debe reducir Kanban a un tablero,
KMM a una certificación de superioridad, F4P a satisfacción genérica ni Upstream
a un backlog previo al backlog.

## Proyecto final

Diseño de un Enterprise Kanban System completo: F4P, demanda, upstream, discovery,
commitment, delivery, métricas, SLE, forecasting, riesgo, portfolio, cadencias,
diagnóstico KMM, capability gaps y roadmap evolutivo.

## Requisitos de profundidad experta

Cada tema técnico debe cubrir, cuando corresponda: definiciones operativas, supuestos, mecanismos causales, unidades, fórmulas explicadas, límites de aplicación, interpretación, errores, ejemplos resueltos, ejercicios y decisiones justificadas. No introducir matemáticas artificiales en lecciones puramente organizacionales.

### Métricas, datos y forecasting

- Distinguir métricas por servicio, clase de trabajo y puntos de inicio/fin; registrar definiciones y calidad de datos.
- Explicar las condiciones de estabilidad y conservación de flujo para Little's Law y las limitaciones de la aproximación de Kingman.
- Usar percentiles, distribuciones empíricas, Monte Carlo, bootstrap, análisis de sensibilidad y backtesting con advertencias sobre no estacionariedad y sesgo.
- Expresar SLE y pronósticos en términos probabilísticos, nunca como garantía automática.

### F4P, upstream y economía

- Diseñar criterios de fitness observables, segmentación contextual y mecanismos de feedback con análisis de sesgos.
- Mantener diferenciados idea, opción, discovery, selección, compromiso y delivery.
- Enseñar Cost of Delay, perfiles temporales, CD3, valor de información y decisiones de abandono con hipótesis y límites explícitos.

### KMM y Enterprise Kanban

- Presentar ML0–ML6 como mapa evolutivo contextual; no convertir niveles en puntuaciones ni atribuirlos sin evidencias.
- Diagnosticar capacidades con indicadores observables, distinguir servicios heterogéneos y seleccionar prácticas apropiadas.
- Evaluar dependencias, capacidad compartida, riesgo sistémico, cultura, liderazgo, resiliencia y transiciones.

### Laboratorios y evaluación

- Cada bloque debe incluir al menos un caso aplicado con datos o evidencias adecuados a su naturaleza.
- Para laboratorios cuantitativos: especificar dataset, unidades, supuestos, cálculos reproducibles, interpretación y decisiones.
- Para laboratorios organizacionales: describir contexto, stakeholders, artefactos, criterios de decisión y evidencias de resultado.
- Incluir checkpoints de diagnóstico y evaluación progresiva, con rúbricas para el proyecto final.
- Proyecto final: diseño integrado, forecast validado, medición F4P, diagnóstico KMM basado en evidencias y roadmap 30/60/90 días.

### Progresión de la lección

🎯 OBJETIVO → conceptos y contexto → mecanismo/ejemplo trabajado → 🧪 Laboratorio → ⚠️ Errores frecuentes → 💡 Idea importante → evaluación o preguntas de decisión → 🧠 QUÉ DEBES RECORDAR (3–7 puntos). Mantener la profundidad sin rellenar apartados inaplicables.

## Precisiones cuantitativas obligatorias

Antes de las lecciones 0.21–0.23, introducir dentro de esas lecciones las unidades,
el intervalo de observación, las tasas por unidad de tiempo, el promedio temporal
de WIP, la media aritmética de tiempos y la variabilidad. La primera simulación
será guiada y podrá hacerse en una hoja de cálculo, sin exigir programación.

Little relaciona el WIP medio, el throughput medio y el tiempo medio dentro de
los mismos límites de sistema, bajo las condiciones pertinentes. No identifica
el WIP medio con un límite WIP. Un percentil usado para expresar un SLE no debe
sustituirse por el tiempo medio en esa relación. La elección inicial de límites
es una hipótesis de política que se calibra experimentalmente, considerando
bloqueos, capacidad, variabilidad y resultados; no una garantía de cumplimiento.

Kingman se presenta como aproximación para una cola G/G/1 en régimen estable,
con un servidor, utilización menor que uno, disciplina y supuestos especificados.
Explicar los coeficientes de variación y los límites de aplicar ese modelo a
trabajo de conocimiento, servicios en red o capacidad variable. No presentar la
aproximación como una ley exacta o causalidad demostrada por datos observacionales.

## Service Request Review y decisiones upstream

Enseñar explícitamente Service Request Review (SRR): propósito, participantes,
opciones revisadas, evidencias, decisiones, políticas y seguimiento. Diferenciar
la evaluación y evolución de opciones del compromiso de entrega en replenishment.
Conectar SRR con Risk Review y documentar cuándo un contexto permite combinar
cadencias sin perder sus propósitos. Las decisiones y acciones deben conservar
responsable, fecha, evidencia y revisión posterior.

## Progresión sin repetición

- Little: intuición y unidades en 0.21; aplicación al WIP en 3.20; condiciones,
  medición y contraejemplos en 5.20–5.21 y 5.30; calibración en 22.41.
- Kingman: modelo mental en 0.22; cálculo y crítica del modelo en 5.31.
- Cost of Delay y CD3: introducción en 4 y 13; selección aplicada en 15;
  sensibilidad, hipótesis frágiles y fallos de la heurística en 19.
- Toda lección que retome un concepto debe remitir al prerrequisito y añadir
  una decisión, mecanismo, cálculo o diagnóstico que no se haya resuelto antes.

## Checkpoints: entregables verificables por bloque

Cada checkpoint exige un artefacto, interpretación de evidencias y decisiones
justificadas. Para aprobar, el entregable debe ser coherente con las políticas y
los límites del servicio definidos y explicar al menos una limitación.

| Bloque | Entregable mínimo y criterio observable |
|---|---|
| 0 | Modelo de servicio y simulación guiada con unidades y supuestos coherentes. |
| 1 | Ficha del servicio que identifique cliente, compromiso, entrega y principios. |
| 2 | Tablero con esperas, actividad, bloqueos y políticas de transición explícitas. |
| 3 | Experimento WIP que distinga límite y promedio y compare resultados. |
| 4 | Políticas versionadas con clases de servicio y excepciones justificadas. |
| 5 | Diccionario de métricas y análisis CFD, aging y distribuciones consistentes. |
| 6 | Forecast reproducible, backtesting temporal y explicación de incertidumbre. |
| 7 | Fichas de cadencias, acta SRR y seguimiento de decisiones entre revisiones. |
| 8 | Diseño STATIK trazable a demanda, insatisfacciones y capacidad observada. |
| 9 | Catálogo y acuerdos entre servicios respaldados por una revisión de servicio. |
| 10 | Segmentos por propósito y criterios de fitness con umbrales verificables. |
| 11 | Fitness box score, análisis de sesgos y decisión sobre evolución del servicio. |
| 12 | Mapa upstream con opciones, descarte y puntos de decisión y compromiso. |
| 13 | Análisis de demanda y política de admisión para un escenario de sobrecarga. |
| 14 | Registro de experimentos con evidencia y decisión de continuar, pivotar o cerrar. |
| 15 | Simulación de replenishment con capacidad restringida y selección argumentada. |
| 16 | Portfolio con WIP, dependencias, capacidad compartida y escenarios explícitos. |
| 17 | Matriz de evidencias KMM, incertidumbres y selección contextual de prácticas. |
| 18 | Red de servicios y escenario de interrupción con recuperación evaluable. |
| 19 | Comparación económica con unidades, hipótesis y sensibilidad de la decisión. |
| 20 | Informe de mejora que examine confusores y límites de inferencia causal. |
| 21 | Diagnóstico con hipótesis alternativas y experimento de recuperación del flujo. |
| 22 | Dossier integrado, defensa de decisiones y plan de medición a 30/60/90 días. |

### Rúbrica del proyecto final

Evaluar seis dimensiones: diseño del servicio, gestión upstream, flujo y políticas,
calidad del análisis cuantitativo, medición F4P y evolución KMM. Cada dimensión
recibe 0 (ausente), 1 (incompleta), 2 (coherente y sustentada) o 3 (contrastada con
alternativas y sensibilidad). Aprobar requiere al menos 2 en cada dimensión,
datos y supuestos trazables, y ausencia de errores críticos de interpretación.
La rúbrica es un instrumento pedagógico propio, no una evaluación oficial KMM.

## Integración con course-generator

Los requisitos descritos son editoriales. La sintaxis YAML no acredita que el
cargador interprete todas las claves del perfil. Verificar en el repositorio
qué campos consume, cuáles incorpora al prompt y cuáles ignora antes de asumir
automatismos de validación o evaluación.

La ruta `../../config/pedagogy.md` se conserva del perfil recibido. Debe resolverse
desde el directorio del perfil definitivo y comprobarse en el repositorio junto
con `domain.md` y `bibliography.md`. No se ha verificado aquí ese archivo externo
ni se incluye una copia inventada de su contenido.
