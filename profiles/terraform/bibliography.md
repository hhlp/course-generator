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
