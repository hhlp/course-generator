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
