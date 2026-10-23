# Bibliografía — Jenkins 0 → experto en profundidad

> **Criterio:** la documentación oficial de Jenkins y de cada plugin prevalece para versiones, APIs, compatibilidad y seguridad. Los libros sirven como contexto histórico y conceptual. El path de Groovy es independiente.

## Scope A — Fundamentos y CI/CD
- John Ferguson Smart — *Jenkins: The Definitive Guide* (fundamentos históricos).
- Brent Laster — *Jenkins 2: Up and Running* (Pipeline y arquitectura; contrastar con documentación actual).
- Jez Humble y David Farley — *Continuous Delivery*.
- Nicole Forsgren, Jez Humble y Gene Kim — *Accelerate*.
- Gene Kim et al. — *The DevOps Handbook*.

## Scope B — Jenkins Core, instalación y administración
- Jenkins User Documentation: https://www.jenkins.io/doc/
- Installing Jenkins: https://www.jenkins.io/doc/book/installing/
- Managing Jenkins: https://www.jenkins.io/doc/book/managing/
- Jenkins LTS: https://www.jenkins.io/download/lts/

## Scope C — Pipeline, Jenkinsfile y SCM
- Pipeline: https://www.jenkins.io/doc/book/pipeline/
- Pipeline Syntax: https://www.jenkins.io/doc/book/pipeline/syntax/
- Pipeline Steps Reference: https://www.jenkins.io/doc/pipeline/steps/
- Multibranch Pipeline: https://www.jenkins.io/doc/book/pipeline/multibranch/

## Scope D — Groovy aplicado, CPS y Shared Libraries
- Shared Libraries: https://www.jenkins.io/doc/book/pipeline/shared-libraries/
- CPS Method Mismatches: https://www.jenkins.io/doc/book/pipeline/cps-method-mismatches/
- Pipeline Best Practices: https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/
- Groovy documentation (solo consulta puntual): https://groovy-lang.org/documentation.html

## Scope E — Seguridad y software supply chain
- Jenkins Security: https://www.jenkins.io/doc/book/security/
- Jenkins Security Advisories: https://www.jenkins.io/security/advisories/
- OWASP CI/CD Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html
- NIST SSDF: https://csrc.nist.gov/Projects/ssdf
- SLSA: https://slsa.dev/

## Scope F — JCasC, Job DSL y automatización
- Jenkins Configuration as Code: https://www.jenkins.io/projects/jcasc/
- Jenkins REST API: https://www.jenkins.io/doc/book/using/remote-access-api/
- Jenkins CLI: https://www.jenkins.io/doc/book/managing/cli/
- Job DSL Plugin: https://plugins.jenkins.io/job-dsl/

## Scope G — Testing y desarrollo de plugins
- Jenkins Developer Documentation: https://www.jenkins.io/doc/developer/
- Plugin Tutorial: https://www.jenkins.io/doc/developer/tutorial/
- Jenkins Test Harness: https://www.jenkins.io/doc/developer/testing/
- JenkinsPipelineUnit: https://github.com/jenkinsci/JenkinsPipelineUnit

## Scope H — Agentes, contenedores y Kubernetes
- Distributed Builds: https://www.jenkins.io/doc/book/scaling/architecting-for-scale/
- Kubernetes Plugin: https://plugins.jenkins.io/kubernetes/
- Docker Pipeline Plugin: https://plugins.jenkins.io/docker-workflow/

## Scope I — Observabilidad, operaciones y recuperación
- Jenkins Monitoring: https://www.jenkins.io/doc/book/system-administration/monitoring/
- Jenkins Backup: https://www.jenkins.io/doc/book/system-administration/backing-up/
- Jenkins Upgrade Guide: https://www.jenkins.io/doc/upgrade-guide/

## Estrategia de lectura
Para cada lección seleccionar primero la documentación oficial específica, luego referencias complementarias verificadas. No asignar capítulos, números de página ni versiones no comprobados. Evitar duplicar la bibliografía general de Groovy.

## Referencias específicas de la revisión
- Pipeline: Nodes and Processes (sh, node, ws y dir):
  https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/
- Preparing for Plugin Development (puente Java/Maven y herramientas):
  https://www.jenkins.io/doc/developer/tutorial/prepare/
- Testing (harness y escenarios con reinicios):
  https://www.jenkins.io/doc/developer/testing/

## Aplicación a lecciones y criterios
- 3.6.1–3.6.3 y bloque 15: Pipeline Best Practices y CPS Method Mismatches.
- Shell, contexto de nodo y workspace: Nodes and Processes y Steps Reference.
- Bloque 17: Developer Documentation y Pipeline Best Practices; distinguir
  administración de uso de APIs de core desde Pipeline.
- 21.2.1–21.2.4: Preparing for Plugin Development; consultar un path Java
  independiente si faltan bases del lenguaje, sin duplicarlo aquí.
- Bloques 21 y 23: documentación de testing y JenkinsPipelineUnit; separar
  pruebas simuladas de pruebas de integración con Jenkins y reinicios.
- Bloques 13 y 26: Backing-up/Restoring Jenkins y Upgrade Guide.

Referencias concretas consultadas el 2026-10-19: Pipeline Best Practices,
Backing-up/Restoring Jenkins, Plugin Development, Nodes and Processes,
Preparing for Plugin Development y Testing. Esto no constituye una auditoría
de todos los enlaces ni una garantía de compatibilidad entre plugins.
