# Bibliografía — Vagrant sobre Fedora/KVM

## Principal

### Vagrant: Up and Running
Mitchell Hashimoto.

Fuente principal para los fundamentos conceptuales de Vagrant, Vagrantfile, boxes, provisioning, networking, workflows y filosofía de entornos reproducibles.

Debe utilizarse como fundamento histórico y conceptual. Debido a la evolución de Vagrant y sus providers, los detalles operativos deben contrastarse con documentación oficial actual.

### Pro Vagrant
Wlodzimierz Gajda.

Fuente de profundización para workflows, automatización, configuración avanzada y utilización profesional de Vagrant.

Al igual que la obra anterior, debe complementarse con documentación vigente.

## Documentación oficial y normativa técnica

### HashiCorp Vagrant Documentation
Referencia prioritaria para sintaxis, comandos, Vagrantfile, boxes, provisioners, synced folders, networking, plugins y comportamiento de versiones actuales.

### vagrant-libvirt Documentation
Referencia prioritaria para cualquier configuración específica del provider libvirt.

Debe prevalecer sobre ejemplos antiguos diseñados para VirtualBox u otros providers.

### libvirt Documentation
Referencia para domains, networks, storage pools, volumes, XML, drivers, seguridad y arquitectura de libvirt.

### QEMU Documentation
Referencia para conceptos y comportamiento de QEMU relevantes al provider libvirt.

### Fedora Documentation
Referencia para configuración del host Fedora, virtualización, SELinux, firewalld, networking y administración del sistema.

### Linux kernel KVM documentation
Referencia para arquitectura y capacidades KVM cuando se estudie la capa de virtualización.

## Herramientas relacionadas

### HashiCorp Packer Documentation
Referencia para construcción reproducible de imágenes y generación del artefacto utilizado posteriormente como base de una box.

### Ansible Documentation
Referencia para los provisioners Ansible, inventories, SSH, roles e idempotencia.

### Terraform / OpenTofu Documentation
Utilizar únicamente para delimitar Infrastructure as Code frente al objetivo de Vagrant y evitar solapamientos entre cursos.

## Política de referencias

Los libros proporcionan estructura conceptual y profundidad.

La documentación oficial actual tiene prioridad para:
- comandos;
- opciones;
- configuración;
- compatibilidad;
- comportamiento de providers;
- arquitectura actual de libvirt;
- requisitos de Fedora;
- características que hayan cambiado desde la publicación de los libros.

No inventar números de página, capítulos, secciones ni URLs.

Las referencias exactas de una lección solo deben incluirse cuando hayan sido verificadas.

## Jerarquía

1. Documentación oficial actual para comportamiento técnico vigente.
2. Vagrant: Up and Running para fundamentos.
3. Pro Vagrant para profundización.
4. Documentación de Fedora/libvirt/QEMU/KVM para las capas inferiores.
5. Packer y Ansible para las integraciones correspondientes.

## Mapa de referencias por scope

| Scope y bloques | Referencia prioritaria | Apoyo |
| --- | --- | --- |
| Fundamentos y CLI (0, 2, 4, 5) | HashiCorp Vagrant Documentation | Vagrant: Up and Running; Pro Vagrant |
| KVM/libvirt y provider (1, 12) | vagrant-libvirt Documentation; libvirt Documentation | Fedora Documentation; QEMU Documentation; Linux kernel KVM documentation |
| Boxes y distribución (3, 14) | HashiCorp Vagrant Documentation; vagrant-libvirt Documentation | Fedora Documentation; Packer Documentation |
| Networking y storage (6, 7, 8, 13) | libvirt Documentation; vagrant-libvirt Documentation | QEMU Documentation; Fedora Documentation |
| Provisioning, multi-machine y Ansible (9, 10, 11) | HashiCorp Vagrant Documentation; Ansible Documentation | Pro Vagrant |
| Packer e imágenes (15) | HashiCorp Packer Documentation | Fedora Documentation; Vagrant Documentation |
| Plugins, Ruby e internals (16, 17, 24) | HashiCorp Vagrant Documentation y código fuente de Vagrant | Pro Vagrant |
| Seguridad, troubleshooting, rendimiento (18, 19, 20) | Fedora Documentation; libvirt Documentation; QEMU Documentation | vagrant-libvirt Documentation; Linux kernel KVM documentation |
| Equipo, CI/CD, integración y proyecto (21–23, 25) | Vagrant, Ansible y Packer Documentation | Pro Vagrant; Terraform/OpenTofu Documentation solo como comparación |

## Reglas de uso en lecciones

- Identificar el scope y citar primero la documentación de la capa que controla la función.
- Indicar cuándo una opción depende de la versión de Vagrant, vagrant-libvirt, libvirt, QEMU o Fedora.
- No extrapolar ejemplos de VirtualBox a libvirt sin verificar equivalencia.
- Para internals, recurrir al código fuente y tests de la versión estudiada, sin inventar rutas internas.
- Mantener los dos libros como apoyo conceptual y práctico; la documentación vigente manda en la sintaxis.

## Enlaces de referencia

- Vagrant: https://developer.hashicorp.com/vagrant/docs
- Vagrantfile y orden de carga:
  https://developer.hashicorp.com/vagrant/docs/vagrantfile
- Actualización de boxes:
  https://developer.hashicorp.com/vagrant/docs/cli/box
- Provisioners y run:
  https://developer.hashicorp.com/vagrant/docs/provisioning/basic_usage
- vagrant-libvirt:
  https://vagrant-libvirt.github.io/vagrant-libvirt/
- Configuración del provider:
  https://vagrant-libvirt.github.io/vagrant-libvirt/configuration.html
- Código y configuración del provider:
  https://github.com/vagrant-libvirt/vagrant-libvirt
- libvirt: https://libvirt.org/docs.html
- QEMU: https://www.qemu.org/docs/master/
- qemu-img y advertencias sobre imágenes activas:
  https://www.qemu.org/docs/master/tools/qemu-img.html
- Fedora: https://docs.fedoraproject.org/
- KVM: https://docs.kernel.org/virt/kvm/index.html
- Packer: https://developer.hashicorp.com/packer/docs
- Ansible: https://docs.ansible.com/
- Terraform: https://developer.hashicorp.com/terraform/docs
- OpenTofu: https://opentofu.org/docs/

## Versiones y trazabilidad de las fuentes

Registrar la versión instalada de cada herramienta al iniciar el laboratorio.
Para opciones del provider, enlazar la documentación de esa versión o un tag
concreto de su repositorio; las ramas main/master son referencias móviles.
Las páginas QEMU master tampoco sustituyen el manual de la versión instalada.
No presentar una combinación Fedora/Vagrant/plugin como probada sin ejecutar
su laboratorio y conservar los resultados. Verificar la disponibilidad real de
boxes y servicios de publicación al generar cada lección.

## Correspondencia de bloques revisada

- Bloque 4: Ruby mínimo y Vagrantfile para una máquina.
- Bloque 10: entornos multi-machine y topologías.
- Bloque 11: integración Ansible sobre máquinas ya definidas.
- Bloque 17: Ruby avanzado aplicado al DSL y refactorización.

Los dos libros originales siguen siendo las fuentes conceptuales principales.
