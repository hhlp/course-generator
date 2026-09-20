# Bibliografía — Terraform

## Bibliografía principal aportada para el curso

### Terraform: Up & Running
**Yevgeniy Brikman**

Referencia principal para construir una comprensión progresiva y práctica de Infrastructure as Code con Terraform. Útil para fundamentos, state, módulos, entornos, reutilización, workflows y prácticas de infraestructura mantenible.

### Terraform in Action
**Scott Winkler**

Referencia práctica para comprender Terraform mediante proyectos y patrones reales. Especialmente útil para HCL, recursos, providers, módulos, state, diseño de infraestructura y automatización.

### Terraform Cookbook: Recipes for Codifying Infrastructure
**Kerim Satirli, Taylor Dolezal**

Referencia orientada a recetas y resolución de problemas. Se utilizará principalmente como fuente de patrones prácticos, técnicas operativas, automatización, workflows y casos que complementen la explicación conceptual.

### Terraform in Depth: Infrastructure as Code with Terraform and OpenTofu
**Robert Hafner**

Referencia avanzada para profundizar en diseño, operación, state, módulos, arquitectura, prácticas a escala y la relación entre Terraform y OpenTofu.

## Fuentes normativas y documentación oficial

La documentación oficial debe tener prioridad para cualquier comportamiento dependiente de versión, sintaxis exacta o funcionalidad reciente.

- HashiCorp Terraform Documentation.
- Terraform Language Documentation.
- Terraform CLI Documentation.
- Terraform Provider Documentation.
- Terraform Registry.
- Terraform Plugin Framework Documentation.
- HCP Terraform Documentation.
- OpenTofu Documentation, para las secciones específicas de OpenTofu y para contrastar divergencias.

## Uso de las fuentes durante el curso

### Principal

Los cuatro libros constituyen la bibliografía pedagógica principal. No es necesario que una lección dependa exclusivamente de un libro.

### Normativa

La documentación oficial se utiliza para:

- sintaxis HCL;
- comandos y opciones CLI;
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

**Práctica y resolución de problemas:** Terraform Cookbook.

**Profundización y nivel avanzado:** Terraform in Depth, complementado siempre por documentación oficial actual cuando el comportamiento pueda haber cambiado.

## Política bibliográfica

- No inventar capítulos, páginas o secciones exactas.
- Solo proporcionar referencias exactas cuando hayan sido verificadas.
- Diferenciar claramente documentación de Terraform de documentación de un provider.
- En contenidos sobre AWS, Azure, GCP, Kubernetes u otros providers, consultar también la documentación oficial del provider correspondiente.
- En contenidos Terraform/OpenTofu, verificar las capacidades actuales de ambos proyectos y no asumir compatibilidad absoluta.
- Si un libro describe una versión antigua, conservar su explicación conceptual cuando siga siendo válida y actualizar la parte técnica con documentación oficial.
