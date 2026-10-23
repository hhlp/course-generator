# Dominio — Git 0 → Experto en profundidad

## Objetivo
Dominar Git como sistema distribuido de control de versiones, desde la CLI y colaboración hasta el almacenamiento interno, seguridad, operación y contribución al proyecto.

## Alcance
- 66 bloques numerados 0–65; lecciones X.Y y sublecciones X.Y.Z.
- Laboratorios reproducibles en Fedora/Linux, inicialmente offline.
- Comandos porcelain y plumbing, parámetros, precondiciones, efectos y recuperación.
- El directorio `.git/` se estudia explícitamente en el bloque 3 y se retoma en internals y forense.
- Matriz por artefacto: comando creador, modificador, lector, eliminador, condiciones, formato y riesgos.
- Diferencias entre repositorio no bare, bare, worktree vinculado y formatos de refs files/reftable.
- Distinguir artefactos siempre presentes, opcionales, transitorios y dependientes de configuración o versión.
- Integraciones GitHub/GitLab, hooks, firmas GPG/SSH, CI/CD y GitOps desde el punto de vista de Git.

## Fuera de alcance
- Curso completo de administración de GitHub/GitLab, CI/CD o GitOps independiente.
- Manipulación manual de metadatos en repositorios de producción sin copia verificada.

## Navegación por el historial y el DAG
- Enseñar explícitamente `HEAD^`, `HEAD~N`, `HEAD^N`, composición de ancestros, operadores de revisión y rangos.
- Separar la navegación lineal por primer padre del recorrido del DAG completo y explicar merges y selección de padres.
- Incluir laboratorios con `git log --graph --all --decorate`, `git rev-list`, `git rev-parse` y `git merge-base`.
- Comparar `--first-parent`, `--topo-order`, `--ancestry-path` y orden por fecha.

## Criterios pedagógicos
Cada lección: objetivo, prerrequisitos, teoría profunda, sintaxis y opciones, ejemplos, laboratorio, errores, troubleshooting, evaluación y referencias. Progresión de ejercicios de observación → operación → diagnóstico → recuperación.

## Requisitos del laboratorio
Fedora/Linux; Git actualizado, Bash, OpenSSH, GPG y herramientas Unix. Los laboratorios destructivos usan repositorios efímeros, backups y verificaciones.

## Competencias de egreso
Diseñar flujos, recuperar historial, inspeccionar `.git/`, razonar sobre DAG y objetos, operar repositorios seguros, automatizar validaciones, diagnosticar corrupción y optimizar repositorios grandes.

## Hitos
Fundamentos (tras bloque 11), colaboración (tras 21), avanzado (tras 33), internals (tras 45), seguridad (tras 55) y proyecto experto (tras 65).

## Progresión del bloque 3
La primera pasada identifica HEAD, config, objects, refs y el index cuando
exista, mediante init, add, commit e inspección de solo lectura. Las entradas
sobre merge, rebase, fetch, worktrees y packs funcionan como mapa de consulta.
Sus prácticas se ejecutan después de estudiar las operaciones correspondientes.
Los ejercicios de corrupción y restauración se completan tras los bloques 44 y
60. Conservar todos los temas y sublecciones sin exigir internals avanzados a
quien todavía está aprendiendo el ciclo básico.

## Requisitos precisos de navegación
- No confundir el DAG con un árbol: un commit puede tener varios padres.
- Predecir el commit seleccionado antes de ejecutar cada expresión.
- Verificar HEAD~2 frente a HEAD^2, y explicar cada paso de HEAD~2^2.
- Inspeccionar padres reales; su orden no depende del dibujo ni de las fechas.
- Distinguir posición en el grafo, selección de conjuntos y orden de salida.
- Comparar log A..B y log A...B con diff A B y diff A...B.
- Diferenciar HEAD@{1}, HEAD~1 y @{-1} mediante un laboratorio de movimientos.
- Incluir rama unborn, revisión inexistente, objeto por ruta y stages del index.
- Cubrir simplificación del historial al filtrar rutas y límites de --follow.

## Contrato de cada laboratorio
Registrar versión y capacidades, prerrequisitos, comandos exactos, estado
inicial, predicción, salida relevante y comprobaciones finales. Los hashes y
fechas pueden variar: validar relaciones y contenido, evitando valores fijos.
Usar dos clones y un remoto bare para colaboración local. Restaurar desde una
copia independiente y comprobar integridad, referencias y contenido.
No borrar locks sin comprobar procesos activos ni editar metadatos como método
habitual de operación. Revocar secretos expuestos antes de reescribir historia.

## Automatización y operación
En scripts usar salidas estables, delimitación NUL cuando proceda, rutas
citadas, códigos de salida documentados y separación de opciones y rutas.
El backup debe declarar si incluye cambios sin commit, configuración, hooks,
objetos LFS, repositorios de submódulos y dependencias externas como alternates.
Distinguir verificación criptográfica de una firma y confianza en la identidad.

## Integración con course-generator
Estos archivos definen un temario, no garantizan por sí solos la interpretación
de campos de profile.yaml por una versión concreta del generador. La ruta
files.pedagogy se conserva del original y debe verificarse en el repositorio de
destino. La validación local comprueba YAML y estructura del temario; la prueba
real con --dry-run y --check-lessons requiere el proyecto y su configuración.
Las sublecciones X.Y.Z requieren comprobar el parser y --split-blocks; no asumir
que se convierten automáticamente en unidades independientes.
