# DOMAIN --- ANSIBLE DE CERO A EXPERTO

## Alcance

Curso integral de Ansible con Fedora/RHEL como plataforma de sistemas.
No incluye administración de Windows. Cubre ansible-core, automatización
RHEL, networking, Podman/Buildah/Skopeo, Kubernetes/OpenShift, cloud,
IaC, CI/CD, testing, AWX, Red Hat Ansible Automation Platform, Execution
Environments, Event-Driven Ansible, desarrollo de módulos/plugins,
internals, seguridad, escala, gobernanza y arquitectura.

## Hito RHCE / Ansible

El bloque 16 es un checkpoint explícito. Todo lo anterior construye las
competencias de Ansible y administración automatizada de RHEL necesarias
para alcanzar ese nivel. No convierte el curso en una preparación
limitada al examen: desde el bloque 17 el recorrido continúa mucho más
allá de RHCE hacia Ansible/AAP profesional y arquitectura empresarial.

## Plataforma

Control node y managed Linux nodes: Fedora/RHEL. Windows queda fuera de
alcance. Las áreas de red usan las collections y transportes apropiados.
Containers se centra en Podman, Buildah, Skopeo y OCI. Orquestación
cubre Kubernetes/OpenShift. Enterprise cubre AWX/AAP.

## Estructura pedagógica

Cada lección comienza con `🎯 OBJETIVO`, desarrolla el tema con
profundidad y enfoque práctico, incluye `🧪 Laboratorio/ejemplos`,
`⚠️ Errores frecuentes` y `💡 Idea importante` cuando aporten valor, y
termina con `🧠 QUÉ DEBES RECORDAR` con 3--7 ideas esenciales.

## Profundidad

No producir simples resúmenes. Explicar qué hace cada mecanismo, cómo
funciona, cómo se configura, cómo se valida, cómo falla, cómo se
diagnostica y sus implicaciones de seguridad, mantenibilidad,
idempotencia, reproducibilidad y escala.

## Resultado

El alumno debe poder diseñar, implementar, probar, securizar, operar,
diagnosticar y gobernar una plataforma Ansible/AAP profesional.


## Contrato de profundidad reforzado

Las lecciones técnicas deben explicar prerrequisitos, mecanismo interno, sintaxis y parámetros, configuración, ejecución, validación, fallos habituales, diagnóstico, seguridad, idempotencia y mantenimiento. No sustituir estos apartados por enumeraciones superficiales. En cada laboratorio especificar plataforma, versiones, inventario, archivos, comandos, resultados esperados, verificación, repetición idempotente y limpieza o reversión.

Los contenidos puramente conceptuales pueden reemplazar el laboratorio por un análisis guiado, una comparación verificable o un experimento reproducible. No inventar resultados de ejecución. Distinguir explícitamente comportamiento demostrado, documentación y supuestos.

## Alcance y especialización

El PATH enseña cómo automatizar sistemas Fedora/RHEL, redes, containers, Kubernetes/OpenShift y proveedores cloud mediante Ansible; no reemplaza los PATH independientes de cada tecnología. Mantener Windows excluido. Explicar regex solo como aplicación de filtros de Ansible, no como curso de teoría regex.

## Hito RHCE y evaluación

El bloque 16 es un hito pedagógico, no una garantía de aprobar una certificación. Contrastarlo con los objetivos oficiales vigentes para la versión del examen. Incorporar simulacros de configuración y troubleshooting, criterios de aceptación, evidencias y pruebas de idempotencia.

## Laboratorios avanzados y proyecto final

En AWX/AAP, redes, EDA, EE y cloud exigir, cuando sea viable, instalación o preparación, configuración, validación, diagnóstico y recuperación. Si una tecnología requiere licencias o recursos externos, proporcionar alternativa de laboratorio y declarar limitaciones. El proyecto final debe incluir pruebas de aceptación automatizadas, matriz de compatibilidad, recuperación de fallos y documentación de evidencias.
