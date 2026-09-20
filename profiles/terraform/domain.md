# Dominio — Terraform

## Propósito

Este curso enseña Terraform desde cero hasta un nivel experto, tratando Terraform como una tecnología independiente de AWS, Azure o Google Cloud. Los proveedores cloud aparecen después de dominar Terraform Core, HCL, providers, state, módulos, backends, testing, seguridad y automatización.

## Plataforma de referencia

- Linux como entorno principal.
- Git para control de versiones.
- Terraform CLI.
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
- Patrones y antipatrónes.
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

Al finalizar, el estudiante debe poder diseñar, implementar, probar, versionar, asegurar, automatizar, mantener, diagnosticar y evolucionar infraestructura gestionada con Terraform; comprender el state y el grafo de dependencias; construir módulos; integrar Terraform con Ansible y CI/CD; adoptar infraestructura existente; y trasladar estos conocimientos a distintos providers sin depender conceptualmente de un cloud concreto.
