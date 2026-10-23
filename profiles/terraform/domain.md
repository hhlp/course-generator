# Dominio — Terraform

## Propósito

Este curso enseña Terraform desde cero hasta un nivel experto, tratando Terraform como una tecnología independiente de AWS, Azure o Google Cloud. Los proveedores cloud aparecen después de dominar Terraform Core, HCL, providers, state, módulos, backends, testing, seguridad y automatización.

## Plataforma de referencia

- Linux como entorno principal.
- Git para control de versiones.
- Terraform CLI como interfaz operativa principal, desde workflow básico hasta automatización, diagnóstico y CI/CD.
- HCL como lenguaje de configuración.
- Providers locales al principio para no convertir un cloud concreto en prerrequisito.
- Ansible como herramienta complementaria de configuration management.
- AWS, Azure, Google Cloud, Kubernetes y otros providers como especializaciones posteriores.
- OpenTofu como implementación relacionada que debe comprenderse y compararse técnicamente.

## Alcance obligatorio

El curso debe cubrir en profundidad:

- Infrastructure as Code.
- Modelo declarativo, desired state, convergencia e idempotencia.
- Terraform Core y arquitectura Core/provider.
- Terraform CLI en profundidad: comandos, subcomandos, opciones globales, flags, variables de entorno y configuración de CLI.
- Automatización de Terraform CLI: exit codes, planes guardados, JSON, ejecución no interactiva y CI/CD.
- HCL: sintaxis, tipos, expresiones, funciones y evaluación.
- Providers, resources y data sources.
- Dependency graph.
- Plan, apply, destroy y lifecycle.
- Terraform state y operaciones sobre state.
- Importación y adopción de infraestructura existente.
- Refactoring mediante moved/removed blocks cuando corresponda.
- Módulos, composición y diseño de interfaces.
- Backends, remote state y locking.
- Workspaces y estrategias multi-entorno.
- Terraform + Ansible.
- Testing, validación, linting y calidad.
- Seguridad, secretos y supply chain.
- CI/CD.
- Ejecución remota y colaboración.
- Terraform a escala, gobernanza y Policy as Code.
- Troubleshooting.
- Internals de Terraform.
- Desarrollo de providers.
- Terraform y OpenTofu.
- Aplicación posterior a AWS, Azure, GCP, Kubernetes y otros providers.
- Patrones y antipatrones.
- Proyecto final integrador.

## Principios pedagógicos del dominio

1. Terraform se aprende antes que un proveedor cloud específico.
2. AWS, Azure y GCP no deben presentarse como prerrequisitos.
3. Cada concepto debe distinguir entre comportamiento de Terraform Core y comportamiento específico del provider.
4. State debe tratarse como uno de los conceptos centrales del curso, no como un detalle secundario.
5. Los ejemplos deben progresar desde infraestructura local y segura hacia escenarios remotos y cloud.
6. Terraform y Ansible deben enseñarse como herramientas complementarias, evitando usar provisioners como sustituto general de configuration management.
7. Los ejemplos deben explicar qué cambia en configuration, state y remote infrastructure.
8. Se debe enseñar a leer un plan antes de aplicar cambios.
9. Los laboratorios deben incluir errores, drift, importación, refactoring y recuperación.
10. Los contenidos sensibles a versión deben verificarse contra documentación oficial antes de afirmar sintaxis o comportamiento exactos.
11. La CLI debe enseñarse primero como workflow operativo y después como interfaz automatizable para scripts y CI/CD.
12. Los comandos legacy o de uso desaconsejado deben identificarse como tales y acompañarse de la alternativa moderna.

## Límites

- El curso no es un curso completo de AWS, Azure o GCP.
- No convertir el aprendizaje en memorización de recursos de un provider.
- No almacenar credenciales reales ni secretos en ejemplos.
- No asumir que `sensitive` elimina secretos del state.
- No presentar `terraform destroy` como mecanismo de rollback.
- No abusar de `-target`, provisioners, workspaces o `depends_on`.
- No enseñar multi-cloud como objetivo por sí mismo; debe justificarse por requisitos.
- No confundir provisioning con configuration management.
- No tratar OpenTofu y Terraform como idénticos cuando una funcionalidad diverja.

## Resultado esperado

Al finalizar, el estudiante debe dominar Terraform CLI de forma interactiva y automatizada; diseñar, implementar, probar, versionar, asegurar, automatizar, mantener, diagnosticar y evolucionar infraestructura gestionada con Terraform; comprender el state y el grafo de dependencias; construir módulos; integrar Terraform con Ansible y CI/CD; adoptar infraestructura existente; y trasladar estos conocimientos a distintos providers sin depender conceptualmente de un cloud concreto.

## Profundidad adicional obligatoria — versión ampliada

- Conservar los 30 bloques y sus identificadores; precisar títulos y añadir lecciones cuando resuelvan lagunas. El bloque 24 integra el tronco y 29.19–29.20 cierran los itinerarios.
- Para cada tema: fundamentos, arquitectura, sintaxis, semántica, ejemplos ejecutables, resultados esperados, seguridad, errores frecuentes, diagnóstico, recuperación y límites.
- Distinguir Terraform Core, provider, HCP Terraform y OpenTofu; verificar disponibilidad y versión de cada capacidad antes de enseñar comandos.
- Profundizar en cty, parsing HCL, grafo, RPC, plan modifiers, state lineage/serial, deposed instances y recuperación.
- Enseñar Terraform Stacks con condiciones de disponibilidad, evitando asumir que funciona en cualquier instalación local.
- Enseñar recursos efímeros y write-only arguments solo cuando la versión de Terraform y el provider los soporten.
- Priorizar laboratorios seguros en Fedora/RHEL, KVM/libvirt, cloud-init y Ansible con red privada.
- Evitar credenciales reales, destrucciones accidentales y operaciones de state sin snapshot, revisión y runbook.
- Incluir testing de módulos y providers, seguridad de pipelines, gobernanza, contratos y migraciones.
- Evaluar objetivos por milestones y proyecto integrador final.

## Laboratorios y evidencias

Cada lección práctica debe explicar prerrequisitos, topología, versiones, archivos, comandos, resultados esperados, pruebas de idempotencia, fallos reproducibles, limpieza y criterios de aceptación.

Los laboratorios que necesiten HCP Terraform, clouds u otros servicios externos se marcarán opcionales, con alternativa local cuando sea viable.

## Progresión revisada y dependencias

La numeración identifica contenido y conserva referencias existentes. El bloque 1
es una referencia transversal: no se exige dominar sus 60 lecciones al comenzar.
El generador debe explicar los prerrequisitos en cada lección; esta ruta pedagógica
no modifica automáticamente el orden de ejecución del programa.

| Etapa | Contenido | Evidencia para avanzar |
|---|---|---|
| Inicio | 0 y primera pasada de 1: 1.1–1.7 y 1.9–1.14 | Crear terraform_data, leer plan, repetir apply y limpiar |
| Lenguaje | 2–3; consultar 1.15–1.18 | Configuración tipada con entradas, locals y outputs |
| Modelo | 4–5 y 6 | Explicar dependencias, unknowns, reemplazos y provider |
| Operación | 7 y 8, salvo 8.7 y 8.16 | Importar y recuperar un objeto sin módulos anidados |
| Composición | 9; retomar 8.7 y 8.16 | Refactoring con módulos sin destrucción imprevista |
| Colaboración | 10–12 | Backend con locking, entornos e inventario Ansible |
| Calidad | 13–15; retomar 9.23 y completar 1 | Tests negativos, secretos protegidos y pipeline revisable |
| Operación avanzada | 17–18 y 23; 16 si se usa HCP | Diagnóstico, gobernanza y decisiones justificadas |
| Integración | 24 | Proyecto del tronco verificable con alternativa local |
| Especialización | Itinerarios siguientes | Evidencias específicas y defensa 29.19 o 29.20 |

La migración de backend de 1.8 se difiere al bloque 10. Segunda pasada de CLI:
consultar 1.19–1.46 al llegar a su bloque conceptual.
Tercera pasada: consolidar 1.47–1.60 después del bloque 15. Los comandos de
recuperación y modificación de state se ejecutan después del bloque 7, sobre
copias desechables. 1.51 y 1.52 remiten a 25 y 8 para prácticas completas.
En el bloque 5, los aliases entre módulos se introducen visualmente; la práctica
completa de 5.11 y 5.20 se retoma con 9.10 y 9.27.
En 4.14 y 4.23 se enseñan condiciones en recursos; las de outputs se retoman
con módulos y testing. No exigir mocks antes de explicar terraform test.

| Itinerario | Secuencia y prerrequisitos | Cierre |
|---|---|---|
| Local Fedora/RHEL | Tronco; 22.13 y 22.17–22.18 como consulta; 29; 27 después de 7, 10 y 18 | 29.19 amplía 24.21 |
| Plataforma empresarial | Tronco, 17, 27 y 28; 16 cuando proceda | 29.20 con contratos, políticas y recuperación |
| Stacks | 9–11, 16–17 y 25; acceso HCP para ejecución | 29.20 con componentes y deployments |
| Core y providers | 19, prerrequisitos Go, 20 y 26 | 29.20 con provider y pruebas de aceptación |
| Cloud | Tronco y secciones elegidas de 22; fundamentos del cloud seleccionado | 29.20 con presupuesto y limpieza |
| OpenTofu | Tronco, 21 y matriz de compatibilidad independiente | Comparación ensayada sobre copias |

Los conceptos de todos los bloques pertenecen al alcance. La ejecución de cada
especialización depende del itinerario. Go no es requisito del tronco; sí de
20 y 26. HCP y cloud público no son requisitos del itinerario local. La alternativa
local de Stacks enseña coordinación entre root modules, sin afirmar equivalencia
funcional con HCP Stacks. Los hitos son evaluaciones internas, no certificaciones.

## Seguridad y precisión desde el inicio

- Laboratorio 0: terraform_data integrado, sin provider descargable, API externa
  ni credenciales. Después se añaden providers locales con versiones fijadas.
- Introducir .gitignore, permisos y datos ficticios en 0.18, antes de crear state.
  Versionar .terraform.lock.hcl y excluir state, planes y credenciales.
- Introducir riesgos de lectura de planes en 0 y 6; 14 desarrolla su modelo de
  amenazas. Un saved plan aplicado no solicita confirmación interactiva.
- sensitive oculta ciertas salidas; no elimina secretos de state ni de planes.
  ephemeral y write-only tienen contextos y soporte específicos; no protegen
  copias en cloud-init, herramientas externas, inventarios o logs.
- terraform_remote_state expone outputs en HCL pero requiere permisos de lectura
  del snapshot. Publicar datos necesarios mediante un canal con permisos propios.
- El lock file fija providers, no versiones de módulos remotos. Fijar módulos
  mediante versión exacta o referencia Git inmutable según su tipo de fuente.
- check produce advertencias durante plan/apply; no sustituye controles
  bloqueantes. En terraform test un check fallido hace fallar la prueba salvo
  expectativa válida. expect_failures se limita a condiciones personalizadas.
- refresh y taint están deprecados; untaint sigue documentado para retirar una
  marca tras diagnóstico. No atribuir la misma deprecación a los tres comandos.
- Nunca hacer force-unlock sin descartar una operación activa. Un snapshot del
  state no restaura los datos de aplicaciones; la recuperación exige ambos planes.
- La red privada del laboratorio puede permitir salida controlada para instalar
  dependencias; no exige puertos entrantes públicos. Air-gap es un caso separado.

## Contratos de generación y validación

Para cada bloque: declarar conocimientos previos, práctica mínima y ampliación.
Las repeticiones deben aumentar la exigencia: introducción, operación,
diagnóstico e internals. Referenciar la lección anterior y evitar repetirla.

Cada entrega sensible a versión registra fecha, versión exacta de Core, provider,
backend, plataforma y URL normativa. required_version expresa compatibilidad;
el entorno de laboratorio fija además la versión exacta instalada. No afirmar que
una versión mínima equivale a soporte universal del provider.

Los comandos de validation del perfil son la base para root modules .tf. Ejecutar
cada fixture en su directorio. Los child modules requieren un root de prueba;
aliases y credenciales deben estar resueltos cuando correspondan. init puede
descargar dependencias y ejecutar plugins: usar código confiable y aislamiento.
fmt/validate no prueban acceso real a APIs ni convergencia. Añadir plan y test solo
cuando el laboratorio lo permita. Go usa sus controles propios; Stacks, su CLI;
no afirmar que terraform validate verifica esos artefactos.

La ruta files.pedagogy se conserva del perfil recibido. Al integrar en el repositorio,
comprobar su resolución con el cargador real: el archivo compartido no está en
estos adjuntos. Mantener los nombres domain.md y bibliography.md junto al perfil.
Las claves quality documentan intención; su presencia no demuestra que el
generador ejecute cada control. Comprobar el código antes de atribuirles efectos.

## Criterios de cierre

24.21: repositorio reproducible, módulos, backend privado con locking, inventario
Ansible, pruebas, revisión de plan, adopción y refactoring sin destrucción no
prevista. Se puede realizar sin HCP, cloud público ni desarrollo de providers.

29.19: ampliar el proyecto con varias VM, cloud-init, SSH, roles Ansible, segundo
plan sin cambios, fallo de configuración recuperable y simulación de pérdida de
state con RPO/RTO medidos. Comprobar restauración de infraestructura y datos por
separado. 29.20 cierra itinerarios alternativos mediante una rúbrica equivalente.
Un laboratorio con criterios de producción no acredita un entorno productivo real.
