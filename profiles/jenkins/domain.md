# Jenkins — Domain (0 → experto en profundidad)

## Propósito
Formar especialistas capaces de instalar, configurar, programar, extender, asegurar, operar y recuperar Jenkins como plataforma de CI/CD en producción.

## Separación de paths
El lenguaje **Groovy** tiene un learning path independiente y revisado en profundidad. Aquí no se repiten sus fundamentos, POO ni metaprogramación general. Se cubren las expresiones mínimas para leer Jenkinsfiles y, en profundidad, las particularidades de Jenkins: Pipeline DSL, CPS, `@NonCPS`, serialización, sandbox, Script Security, Shared Libraries y APIs administrativas.

## Alcance progresivo
1. CI/CD, arquitectura, instalación y operación en Fedora/RHEL.
2. Jobs, SCM, Multibranch y Pipeline declarativo y scripted.
3. Ejecución distribuida, Remoting, agentes, workspaces y colas.
4. Seguridad, credenciales, autenticación/autorización y supply chain.
5. Integración Jenkins con Git, OCI/Podman/Docker, Ansible, Terraform y Kubernetes, sin sustituir sus paths especializados.
6. Observabilidad, logging, diagnóstico, rendimiento, JCasC, Job DSL y GitOps.
7. Groovy aplicado a Jenkins, CPS, Shared Libraries, testing y Jenkins internals.
8. Desarrollo de plugins, REST API, CLI y automatización administrativa.
9. Upgrades, backups, recuperación ante desastres, límites de HA y Platform Engineering.

## Plataforma
Fedora/RHEL, Bash, Git y Java soportado por la versión LTS de Jenkins. Laboratorio aislado sin exposición pública; controles SELinux y firewalld cuando correspondan.

## Profundidad obligatoria
Cada bloque progresa de conceptos a arquitectura, configuración, comandos, archivos y rutas, seguridad, observabilidad, troubleshooting, pruebas, errores frecuentes y laboratorios. Se permiten sublecciones `xx.yy` cuando la complejidad lo requiera. No inventar compatibilidades de plugins o versiones: verificar documentación oficial actual.

## Evidencias y evaluación
Laboratorios reproducibles, Jenkinsfiles versionados, pruebas automatizadas, runbooks, métricas, análisis de incidentes y proyectos integradores. Proyecto final: plataforma reproducible, endurecida, con agentes dinámicos, Shared Library, testing, extensibilidad, observabilidad y restauración verificada.

## Límites
No duplicar cursos de Groovy, Git, contenedores, Kubernetes, Ansible ni Terraform. Enfocar cada integración en configuración, seguridad, ejecución y troubleshooting específicos de Jenkins.
