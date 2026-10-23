# Bibliografía — Terraform

## Bibliografía principal aportada para el curso

### Terraform Cookbook: Recipes for Codifying Infrastructure
**Kerim Satirli, Taylor Dolezal**

Referencia práctica orientada a recetas para codificar infraestructura y resolver problemas reales con Terraform. Se utilizará para workflows de CLI, automatización, state, providers, módulos, integración, operación y patrones reproducibles.

### Terraform in Action
**Scott Winkler**

Referencia práctica y conceptual para comprender Terraform mediante proyectos y patrones reales. Especialmente útil para HCL, recursos, providers, módulos, state, diseño de infraestructura, CLI y automatización.

### Terraform in Depth: Infrastructure as Code with Terraform and OpenTofu
**Robert Hafner**

Referencia avanzada para profundizar en Terraform y OpenTofu: arquitectura, diseño, operación, state, módulos, automatización, prácticas a escala y diferencias entre ambos ecosistemas.

### Terraform: Up & Running
**Yevgeniy Brikman**

Referencia principal para construir una comprensión progresiva y práctica de Infrastructure as Code con Terraform. Útil para fundamentos, workflow, state, módulos, entornos, reutilización, automatización y prácticas de infraestructura mantenible.

## Fuentes normativas y documentación oficial

La documentación oficial tiene prioridad para cualquier comportamiento dependiente de versión, sintaxis exacta, comandos, flags o funcionalidad reciente.

- HashiCorp Terraform Documentation.
- Terraform CLI Documentation y command reference.
- Terraform Language Documentation.
- Terraform Provider Documentation.
- Terraform Registry.
- Terraform Plugin Framework Documentation.
- HCP Terraform Documentation.
- OpenTofu Documentation, para las secciones específicas de OpenTofu y para contrastar divergencias.

## Uso de las fuentes durante el curso

### Principal

Los cuatro libros constituyen la bibliografía pedagógica principal. Se complementan entre sí y una lección no necesita depender exclusivamente de un libro.

### Terraform CLI

Para comandos, subcomandos, opciones globales, flags, variables de entorno, configuración de CLI, formatos JSON, exit codes y comportamiento sensible a versión, la referencia normativa será la documentación oficial actual de Terraform CLI.

Los libros se utilizarán para explicar contexto, workflows, patrones, decisiones de diseño y casos prácticos; la documentación oficial determinará la sintaxis y el comportamiento vigente.

### Normativa

La documentación oficial se utiliza para:

- sintaxis HCL;
- comandos y opciones CLI;
- variables de entorno y CLI configuration;
- comportamiento de state;
- meta-argumentos;
- módulos y providers;
- testing;
- backends;
- funcionalidades sensibles a la versión;
- desarrollo de providers;
- capacidades de HCP Terraform;
- diferencias actuales entre Terraform y OpenTofu.

### Lecturas por nivel

**Fundamentos y nivel intermedio:** Terraform: Up & Running y Terraform in Action.

**Práctica, recetas y resolución de problemas:** Terraform Cookbook: Recipes for Codifying Infrastructure.

**Profundización y nivel avanzado:** Terraform in Depth: Infrastructure as Code with Terraform and OpenTofu.

**Referencia normativa transversal:** documentación oficial de Terraform y, cuando corresponda, OpenTofu y la documentación oficial del provider utilizado.

## Política bibliográfica

- No inventar capítulos, páginas o secciones exactas.
- Solo proporcionar referencias exactas cuando hayan sido verificadas.
- Diferenciar claramente documentación de Terraform Core/CLI de documentación de un provider.
- Verificar comandos, flags y variables de entorno contra la documentación oficial actual antes de enseñarlos como vigentes.
- Marcar comandos legacy, deprecados o desaconsejados y enseñar la alternativa moderna.
- En contenidos sobre AWS, Azure, GCP, Kubernetes u otros providers, consultar también la documentación oficial del provider correspondiente.
- En contenidos Terraform/OpenTofu, verificar las capacidades actuales de ambos proyectos y no asumir compatibilidad absoluta.
- Si un libro describe una versión antigua, conservar su explicación conceptual cuando siga siendo válida y actualizar la parte técnica con documentación oficial.

## Organización por scopes — revisión profunda

| Scope | Bibliografía pedagógica | Documentación normativa complementaria |
|---|---|---|
| IaC, HCL y CLI | Terraform: Up & Running; Terraform in Action | Terraform Language y Terraform CLI |
| Providers, módulos y state | Terraform in Action; Terraform Cookbook | Terraform Registry, provider docs, backends y state |
| Testing, seguridad y automatización | Terraform Cookbook; Terraform in Depth | Terraform test, security y HCP Terraform |
| Internals y desarrollo de providers | Terraform in Depth | Terraform Plugin Framework, protocolo y código fuente |
| Escalabilidad y Stacks | Terraform in Depth; Terraform: Up & Running | Terraform Stacks y HCP Terraform, según versión y edición |
| Terraform y OpenTofu | Terraform in Depth | Documentación oficial de ambos proyectos |
| Infraestructura local y on-premises | Terraform Cookbook; Terraform in Action | Documentación del provider libvirt elegido, libvirt, KVM y Ansible |

## Política de actualización técnica

- Verificar versiones mínimas y disponibilidad real de Terraform Stacks, terraform query, recursos efímeros, argumentos write-only y demás capacidades recientes.
- No asumir que todos los providers admiten funciones, operaciones write-only, importación o recursos efímeros.
- Separar documentación de Core, providers, HCP Terraform y OpenTofu.
- Registrar fecha de verificación y URL oficial al desarrollar cada lección sensible a versión.
- No atribuir capítulos específicos a libros sin comprobar su índice o texto.

## Referencias verificadas para esta revisión — 2026-10-19

- [CLI modules: requisito >= 1.10](https://developer.hashicorp.com/terraform/cli/commands/modules).
- [CLI query y descubrimiento](https://developer.hashicorp.com/terraform/cli/commands/query).
- [Importación masiva y list blocks](https://developer.hashicorp.com/terraform/language/import/bulk).
- [CLI Stacks](https://developer.hashicorp.com/terraform/cli/commands/stacks).
- [Datos sensibles, ephemeral y write-only](https://developer.hashicorp.com/terraform/language/manage-sensitive-data).
- [Check: advertencias en plan/apply](https://developer.hashicorp.com/terraform/language/block/check).
- [Terraform test y expect_failures](https://developer.hashicorp.com/terraform/language/tests).
- [Mocks de providers](https://developer.hashicorp.com/terraform/language/tests/mocking).
- [Permisos de terraform_remote_state](https://developer.hashicorp.com/terraform/language/state/remote-state-data).
- [Lock file: providers y límites para módulos](https://developer.hashicorp.com/terraform/language/files/dependency-lock).
- [untaint y recuperación](https://developer.hashicorp.com/terraform/cli/commands/untaint).
- [state replace-provider](https://developer.hashicorp.com/terraform/cli/commands/state/replace-provider).
- [Resource identities en state](https://developer.hashicorp.com/terraform/cli/commands/state/identities).
- [Actions y extensión de CRUD](https://developer.hashicorp.com/terraform/language/invoke-actions).

## Matriz técnica de referencia

| Capacidad | Umbral confirmado o regla de uso |
|---|---|
| terraform modules | Terraform 1.10 o posterior |
| Variables/outputs de módulos hijos efímeros y bloques ephemeral | Core 1.10 o posterior; recursos según provider |
| Argumentos write-only | Core 1.11 o posterior y soporte del recurso |
| query, list y resource identity | Verificar la versión exacta de Core y el soporte de cada provider |
| Actions y action_trigger | Verificar Core, schema y disponibilidad de actions en el provider |
| Stacks | Verificar CLI/plugin, acceso HCP y capacidades disponibles para la cuenta |

Estos umbrales no fijan la versión universal del curso. Cada laboratorio mantiene
su matriz exacta y debe volver a verificar las páginas al generarse. No se exige
la versión más reciente ni se incorporan release candidates por defecto.

Los cuatro libros aportados se conservan como fuentes pedagógicas. No se han
verificado sus ediciones, índices completos ni cobertura de funciones recientes;
los títulos no constituyen evidencia de soporte técnico actual. En internals,
Stacks, APIs de providers y acciones prevalecen documentación y código oficiales.
Para OpenTofu, Fedora/RHEL, libvirt y Ansible verificar las fuentes oficiales de
la versión elegida al desarrollar cada laboratorio; esta revisión no certifica
una combinación concreta de esas plataformas.
