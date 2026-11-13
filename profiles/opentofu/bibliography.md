# Bibliografía — OpenTofu

## Fuentes primarias

Referencia curricular OpenTofu 1.13. Verificar el parche exacto instalado y
consultar la versión correspondiente antes de preparar prácticas.

| Tema | Fuente |
| --- | --- |
| Instalación y comprobación de la versión | [Instalación](https://opentofu.org/docs/intro/install/) |
| CLI y subcomandos | [Referencia CLI](https://opentofu.org/docs/cli/commands/) |
| Configuración de la CLI y precedencia | [Archivo de configuración](https://opentofu.org/docs/cli/config/config-file/), [variables de entorno](https://opentofu.org/docs/cli/config/environment-variables/) |
| HCL, .tf y .tofu | [Lenguaje](https://opentofu.org/docs/language/), [archivos y directorios](https://opentofu.org/docs/language/files/) |
| Providers y módulos | [Configuración de providers](https://opentofu.org/docs/language/providers/configuration/), [fuentes de módulos](https://opentofu.org/docs/language/modules/sources/), [Registry](https://registry.opentofu.org/) |
| Suministro | [Bloqueo de providers](https://opentofu.org/docs/cli/commands/providers/lock/), [integración OCI](https://opentofu.org/docs/cli/oci_registries/) |
| Importación y state | [Importación](https://opentofu.org/docs/language/import/), [CLI de state](https://opentofu.org/docs/cli/state/) |
| Backends y cifrado | [Backend S3](https://opentofu.org/docs/language/settings/backends/s3/), [cifrado de state y planes](https://opentofu.org/docs/language/state/encryption/) |
| Testing | [Comando test y lenguaje de pruebas](https://opentofu.org/docs/cli/commands/test/) |
| Migración | [Guía de migración](https://opentofu.org/docs/intro/migration/migration-guide/), [configuraciones interdependientes](https://opentofu.org/docs/v1.13/intro/migration/multiple-configurations/) |
| Internals | [Formato JSON](https://opentofu.org/docs/v1.13/internals/json-format/), [código fuente](https://github.com/opentofu/opentofu) |
| Evolución de versiones | [OpenTofu 1.13](https://opentofu.org/blog/opentofu-1-13-0/), [releases](https://github.com/opentofu/opentofu/releases) |
| Contraste con Terraform | [Terraform CLI](https://developer.hashicorp.com/terraform/cli), [lenguaje Terraform](https://developer.hashicorp.com/terraform/language) |
| Laboratorios on-premises | [Provider libvirt](https://github.com/dmacvicar/terraform-provider-libvirt), [libvirt](https://libvirt.org/docs.html), [cloud-init](https://cloudinit.readthedocs.io/), [Ansible](https://docs.ansible.com/) |

## Lecturas complementarias

- Robert Hafner, *Terraform in Depth: Infrastructure as Code with Terraform
  and OpenTofu*. Arquitectura, diseño y contrastes de los dos motores.
- Yevgeniy Brikman, *Terraform: Up & Running*. Patrones de IaC, módulos,
  reutilización y trabajo en equipo. Verificar los ejemplos con OpenTofu
  antes de asignarlos como práctica.
- Documentación y changelog de cada provider y backend utilizado. Registrar
  la versión junto al enlace que justifica el esquema o comportamiento.

## Criterio de selección

Usar una lectura principal con sección concreta por lección y una fuente
normativa del comando, esquema o protocolo cuando corresponda. Los libros
aportan contexto y patrones. Las referencias de cada versión determinan la
sintaxis y las garantías que se enseñan. Para ejercicios de compatibilidad,
consultar ambos motores y documentar el resultado observado por separado.
