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

## Contrato entre paths y prerrequisitos
Groovy es un path independiente: consultar allí sintaxis, POO y metaprogramación.
Los bloques 4, 14, 15 y 16 aplican ese lenguaje al runtime y las APIs de Jenkins.
Antes del bloque 21 se requiere Java y Maven básicos: las sublecciones 21.2.1–21.2.4
son un puente de entrada, no un curso completo de Java.

## Orden y profundidad de los temas recurrentes
| Tema | Entrada | Profundización y diferencia |
| --- | --- | --- |
| CPS | 3.6.1–3.6.3: modelo mínimo | 15: transformación, persistencia y diagnóstico |
| Agentes | 6: configurar y operar | 24: canales, scheduling y fallos de Remoting |
| JCasC | 13: reconstrucción inicial | 22: pruebas, drift y límites de reconciliación |
| Testing | 16: contrato unitario de librerías | 23: integración, CPS, permisos y reinicios |
| Recuperación | 13: primera restauración | 26: consistencia, staging, migración y RPO/RTO |
| Seguridad | 7: controles básicos | 19: threat model y verificación de supply chain |
| Administración | 17: modelo de objetos y scripts | 25: cliente API/CLI seguro e idempotente |

Cada reaparición debe citar el bloque previo, reutilizar sus artefactos y añadir
un escenario nuevo. Evitar repetir explicaciones y laboratorios introductorios.

## Precisiones técnicas obligatorias
- Groovy del Pipeline se ejecuta en el controller; sh ejecuta comandos en el
  nodo asignado. Leer archivos con APIs Java/Groovy no equivale a usar steps
  de workspace. Demostrar la diferencia sin efectuar builds en el controller.
- @NonCPS no es un mecanismo de aislamiento ni mueve trabajo a los agentes.
  No llamar steps de Pipeline desde métodos @NonCPS.
- Reservar Jenkins.get() y APIs de administración para contextos autorizados.
  No enseñar su acceso directo desde Jenkinsfile como patrón de orquestación.
- Distinguir núcleo, plugins y comandos externos. Registrar el plugin que
  proporciona cada step adicional y comprobar requisitos antes del laboratorio.
- Los tests con mocks no prueban por sí solos CPS, sandbox o comportamiento
  real de plugins. Verificar esos contratos en una instancia de prueba.
- No suponer equivalencia entre Docker Pipeline y Podman; verificar el modo
  de integración utilizado y documentar sus límites.

## Aceptación común de laboratorios
Cada laboratorio identifica prerrequisitos, archivos, comandos, versión probada,
resultado esperado y verificación reproducible. Debe incluir al menos un fallo
controlado, diagnóstico con evidencias y limpieza o recuperación del entorno.
Usar secretos ficticios. Registrar el resultado observado; no declarar como
probado un comando o escenario que solo se haya diseñado.

## Evidencia mínima por bloque
| Bloque | Resultado verificable |
| --- | --- |
| 0 | Entorno aislado y comprobación de herramientas y conectividad |
| 1 | Servicio operativo, TLS y diagnóstico de un fallo de arranque |
| 2 | Job versionado en su configuración, trigger y retención comprobados |
| 3 | Pipeline con éxito, error, cancelación y limpieza comprobables |
| 4 | Jenkinsfile explicado con quoting seguro y parámetros controlados |
| 5 | Multibranch con política documentada para PR de fork |
| 6 | Ejecución en agente y diagnóstico de desconexión |
| 7 | Pruebas de acceso permitido y denegado; secretos ficticios protegidos |
| 8 | Tests publicados y artefacto relacionado con commit y checksum |
| 9 | Imagen OCI construida, publicada y verificada por digest |
| 10 | Plan revisable, aprobación y control de cambios concurrentes |
| 11 | Agente efímero y diagnóstico de un pod que no inicia |
| 12 | Alerta comprobada y runbook basado en evidencia de un incidente |
| 13 | Reconstrucción inicial desde configuración y backup |
| 14 | Refactorización con lógica pura separada de steps |
| 15 | Fallo de serialización corregido y reanudación demostrada |
| 16 | Librería versionada con contrato y pruebas unitarias |
| 17 | Inspección administrativa con acceso restringido y trazabilidad |
| 18 | Promoción del mismo artefacto y recuperación ante fallo |
| 19 | Threat model y verificaciones de firma, SBOM y provenance |
| 20 | Medición antes/después bajo carga reproducible |
| 21 | Plugin compilado con pruebas funcionales y de permisos |
| 22 | Provisioning probado y diferencias de configuración documentadas |
| 23 | Suite que distingue mocks, integración y reinicios reales |
| 24 | Fallo de canal o agente diagnosticado con logs correlacionados |
| 25 | Cliente API/CLI que trata permisos, cola, errores y cancelaciones |
| 26 | Restauración aislada con tiempos y pérdida de datos medidos |
| 27 | Dossier reproducible y defensa técnica de todos los criterios finales |

## Rúbrica del proyecto final
Aceptar solo cuando: la configuración permite reconstruir la plataforma; el
pipeline construye y prueba en agentes; la promoción conserva la identidad del
artefacto; las pruebas negativas verifican permisos y secretos ficticios; los
fallos de agente y reinicios tienen resultados registrados; y una restauración
independiente demuestra los objetivos RPO/RTO definidos para el laboratorio.
Cada criterio debe enlazar evidencia versionada y un procedimiento repetible.

## Interpretación del perfil
Las claves pedagógicas expresan requisitos del curso. Su presencia en YAML no
demuestra que course-generator las implemente: verificar su consumo en el código
antes de atribuirles controles automáticos. Resolver files.pedagogy según la
estructura real del repositorio, sin asumir que existe junto a estos entregables.
