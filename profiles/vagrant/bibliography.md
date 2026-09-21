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
