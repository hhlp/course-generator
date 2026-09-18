# Dominio: diseño de bases de datos relacionales

## Objetivo
Aprender a transformar reglas de negocio en un esquema justificable, demostrar sus propiedades, implementarlo en PostgreSQL y comparar alternativas de almacenamiento y mantenimiento con evidencia. C. J. Date es la referencia principal para teoría y normalización. La ruta comprende 37 bloques (0–36) y 285 lecciones.

## Alcance y separación respecto al curso SQL
Este curso es responsable de requisitos, modelado conceptual y lógico, claves, dependencias, normalización, restricciones, diseño temporal, diseño físico, capacidad, costes y consistencia de datos derivados.
El curso SQL es responsable de la escritura de consultas: SELECT, filtros, funciones, CASE, joins, subconsultas, CTE, funciones de ventana y técnicas de consulta analítica. Aquí pueden aparecer consultas breves como instrumentos para comprobar un diseño o medirlo, pero no se convertirán en lecciones de sintaxis SQL.
El álgebra relacional se utiliza para razonar sobre hechos y reconstrucción de relaciones. Los algoritmos de joins se estudian como operadores físicos y modelos de coste. EXPLAIN se utiliza para evaluar decisiones de diseño; la reescritura sistemática de consultas pertenece al curso SQL.
DDL, restricciones, transacciones y triggers se explican con la profundidad necesaria para implementar y conservar invariantes. No se desarrolla un curso de administración de PostgreSQL, alta disponibilidad o copias de seguridad.

## Entorno y prerrequisitos
Inicio desde cero en diseño. Introducir conjuntos y lógica sin presuponer formación matemática avanzada. Para los laboratorios de implementación se requiere SQL básico, adquirido en la ruta complementaria.
Usar PostgreSQL 18 como base reproducible, en un entorno local Fedora/RHEL o un contenedor. Indicar la versión exacta y las extensiones empleadas en cada laboratorio; contrastar diferencias de versión con documentación oficial. Python es opcional para comprobar cierres y generar datos.
El archivo profile.yaml referencia ../../config/pedagogy.md, que debe existir en el proyecto course-generator. Los cuatro archivos se colocan juntos, por ejemplo en paths/database-design/. La bibliografía se llama deliberadamente bibliografy.md y la referencia del perfil debe coincidir.

## Progresión y evaluación
- Bloques 0–8: fundamentos, requisitos, modelo conceptual y restricciones. Entrega: glosario, diagrama y catálogo de invariantes.
- Bloques 9–19: anomalías, dependencias y normalización. Entrega: claves, cierres y demostraciones de descomposición.
- Bloques 20–27: implementación, patrones, tiempo, antipatrones y evolución. Entrega: DDL, pruebas de rechazo y migración.
- Bloques 28–33: capacidad, estadísticas, modelos de coste y medición. Entrega: cálculos con unidades y un benchmark reproducible.
- Bloques 34–35: derivados y consistencia concurrente. Entrega: estrategias comparadas y reconciliación.
- Bloque 36: proyecto integrador y defensa del diseño.
Avanzar cuando se puedan explicar las decisiones y construir contraejemplos, no solo ejecutar SQL correctamente.

## Formato obligatorio de cada lección
Comenzar con 🎯 OBJETIVO. Explicar conceptos y notación antes de utilizarlos. Incluir un ejemplo resuelto paso a paso, 🧪 LABORATORIO con datos y resultado esperado, ⚠️ ERRORES FRECUENTES y 📚 LECTURA con referencias verificables. Usar 💡 IDEA IMPORTANTE cuando aporte una distinción esencial. Terminar con 🧠 QUÉ DEBES RECORDAR.
En ejercicios formales, presentar solución razonada después del enunciado. En decisiones abiertas, comparar alternativas sin fingir una única respuesta correcta. No inventar páginas, capítulos, citas textuales ni resultados de ejecución. Mantener los encabezados de initial.txt sin indentación ni texto antes del bloque 0.

## Rigor relacional
Distinguir valor de relación, relvar y tabla SQL. Especificar todas las dependencias relevantes y todas las claves candidatas. Una muestra puede refutar una dependencia, pero no demostrar una regla universal del negocio. Añadir una clave sustituta no elimina dependencias ni normaliza el esquema.
1FN no equivale a prohibir cualquier tipo estructurado: explicar dominios y hechos independientes. Para 2FN considerar atributos no primos y todas las claves candidatas. Para 3FN usar la condición formal: en toda dependencia no trivial X → A, X es superclave o A es primo. Para BCNF exigir superclave en el determinante de toda dependencia funcional no trivial.
Distinguir ausencia de pérdida y preservación de dependencias. No descomponer relaciones ternarias sin una dependencia de reunión que lo justifique. Introducir 4FN, 5FN, 6FN y DKNF con sus definiciones y supuestos; ETNF, RFNF y SKNF requieren lectura guiada de la fuente y no deben presentarse como una escalera numérica universal.

## Cálculos y evidencia
Cada cálculo debe especificar variables, unidades, supuestos, derivación y límites. Separar complejidad asintótica, páginas procesadas, unidades del planificador, trabajo acumulado, latencia y coste económico.
Modelo didáctico de capacidad: filas_por_página = floor(espacio_útil / tamaño_fila); páginas = ceil(filas / filas_por_página). Explicar que omite detalles de almacenamiento y contrastarlo con mediciones.
Modelo básico de selectividad: cardinalidad = filas × selectividad. No asumir independencia de predicados correlacionados sin justificación.
Para algoritmos físicos, definir tamaño de entradas y memoria disponible, incluir materialización y derrames cuando correspondan, y no presentar fórmulas simplificadas como costes exactos de PostgreSQL.

## Caso transversal: total calculado frente a total almacenado
Usar pedidos y líneas con cantidades, precio pactado, descuentos y reglas de redondeo explícitas. Definir primero qué significa el total y qué sucede cuando no hay líneas. Diferenciar un derivado reconstruible de un importe histórico que representa un hecho del negocio.
Comparar: cálculo al consultar; columna total mantenida; tabla resumen; vista materializada refrescada; caché con invalidación o caducidad. Una columna generada no resuelve por sí sola un agregado entre filas. Una vista ordinaria no persiste el resultado.
Definir Q = lecturas/s, W = cambios/s, Cs = coste de sumar, Cr = coste de leer el agregado, Cw = coste base de escritura y Cm = mantenimiento adicional:

    C_calcular = Q × Cs + W × Cw
    C_almacenar = Q × Cr + W × (Cw + Cm)
    beneficio básico si Q × (Cs − Cr) > W × Cm

Si Cs > Cr, Q_equilibrio = W × Cm / (Cs − Cr). Incorporar además refresco, reconciliación, espacio y contención usando unidades compatibles. No sumar milisegundos y bytes como si fueran la misma magnitud. Los tiempos acumulados por segundo no son la latencia percibida ni permiten predecir por sí solos la capacidad.
Mantenimiento por diferencias: insertar suma el nuevo importe; borrar resta el antiguo; modificar resta el antiguo y suma el nuevo. Trasladar una línea afecta a dos pedidos. AVG exige conservar suma y contador; borrar el mínimo o máximo puede requerir buscar de nuevo. No generalizar el mantenimiento sencillo de SUM a todos los agregados.
Si se promete consistencia inmediata, detalle y agregado deben cambiar en la misma transacción con un protocolo seguro para todas las rutas de escritura. Estudiar incrementos atómicos, orden de bloqueos, interbloqueos, aislamiento y reintentos; una transacción por sí sola no corrige cualquier algoritmo concurrente.
Si el mantenimiento es asíncrono, definir retraso tolerado, orden, idempotencia, deduplicación, recuperación y reconstrucción. Comprobar reconciliación bajo una instantánea coherente o tras detener las escrituras.

## Laboratorio de rendimiento obligatorio
Variar líneas por pedido, número de pedidos, proporción de lecturas/escrituras, clientes concurrentes y concentración de cambios sobre pedidos calientes. Mantener equivalencia semántica y datos comparables entre estrategias.
Registrar versión, hardware, parámetros relevantes, índices, semilla y tamaño del conjunto. Separar calentamiento de medición; repetir ensayos y comunicar dispersión. Medir latencia y throughput además del plan. Validar el total después de operaciones, rollback, borrados, traslados y concurrencia.
No declarar una estrategia ganadora universal. Entregar el intervalo de cargas en el que compensa y el precio en complejidad y consistencia.

## Referencias de implementación
Los costes de EXPLAIN son unidades del planificador, y el coste de un nodo incluye a sus hijos; no sumar todos los costes del árbol. EXPLAIN ANALYZE ejecuta la sentencia. Fuente: [Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html).
CHECK no sustituye a una restricción arbitraria entre filas y su interacción con NULL exige atención. Fuente: [Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html).
Las vistas materializadas persisten resultados y su actualización debe planificarse explícitamente; no asumir mantenimiento incremental automático. Fuente: [Materialized Views](https://www.postgresql.org/docs/18/rules-materializedviews.html).

## Proyecto final
Entregar requisitos, glosario, diagrama, dependencias, claves, demostraciones, diccionario de datos, DDL y pruebas. Añadir historial de precios, migración, estimación de capacidad y comparación de agregados. La defensa debe justificar integridad, rendimiento, tolerancia a retrasos y recuperación, documentando alternativas descartadas y limitaciones de la evidencia.
