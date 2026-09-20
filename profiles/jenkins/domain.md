# Jenkins — Domain

## Propósito

Este dominio define un curso progresivo de Jenkins desde fundamentos hasta diseño, operación y desarrollo avanzado de plataformas CI/CD.

El curso no presupone un lenguaje de programación concreto. Introduce primero el Groovy necesario para Jenkins Pipeline y, en la etapa avanzada, estudia Groovy en profundidad antes de abordar CPS, Shared Libraries e internals de Jenkins.

## Alcance

- Fundamentos de CI/CD y Pipeline as Code.
- Instalación y administración de Jenkins sobre Linux.
- Jobs, builds, artifacts, triggers y plugins.
- Jenkinsfile, Declarative Pipeline y Scripted Pipeline.
- Groovy esencial y Groovy avanzado.
- Controller, agents, executors y ejecución distribuida.
- Git, webhooks, Multibranch Pipeline y repositorios.
- Credentials, autorización, Sandbox y Script Security.
- Testing, quality gates y gestión de artefactos.
- Docker/Podman, Ansible, Terraform y Kubernetes.
- JCasC, REST API, backups, upgrades y recuperación.
- Observabilidad, troubleshooting, rendimiento y escalabilidad.
- Jenkins Pipeline CPS, serialización y @NonCPS.
- Shared Libraries y diseño de DSLs.
- Jenkins object model y automatización administrativa.
- Seguridad de CI/CD y software supply chain.
- Proyecto final de plataforma Jenkins.

## Plataforma principal

La plataforma de laboratorio será Linux, con preferencia por Fedora/RHEL cuando no exista una razón pedagógica para utilizar otra distribución.

## Enfoque de Groovy

El aprendizaje de Groovy se divide deliberadamente en tres capas:

1. Groovy esencial para comprender y escribir Jenkinsfiles.
2. Groovy como lenguaje en profundidad: objetos, closures, colecciones, metaprogramación y DSLs.
3. Groovy bajo Jenkins Pipeline: CPS, persistencia, serialización, Sandbox, Shared Libraries y restricciones específicas del motor de Pipeline.

El objetivo es evitar que el estudiante confunda Groovy convencional con el modelo de ejecución de Jenkins Pipeline.

## Límites y separación con otros cursos

Este curso integra Docker/Podman, Ansible, Terraform y Kubernetes desde el punto de vista de su uso con Jenkins, pero no sustituye cursos especializados de esas tecnologías.

Git se estudia únicamente hasta el nivel necesario para SCM, Multibranch Pipeline y estrategias CI/CD.

Groovy sí recibe tratamiento profundo porque constituye una base directa para Scripted Pipeline, Shared Libraries, DSLs y automatización interna de Jenkins.

## Resultado esperado

Al finalizar, el estudiante debe poder instalar, asegurar, administrar y diagnosticar Jenkins; diseñar pipelines mantenibles; crear Shared Libraries; comprender los problemas derivados de CPS; integrar herramientas DevOps; automatizar la configuración; y diseñar una plataforma CI/CD escalable y observable.
