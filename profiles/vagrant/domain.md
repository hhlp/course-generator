# Dominio — Vagrant sobre Fedora/KVM

## Propósito

Este curso enseña Vagrant desde cero hasta un nivel experto usando Fedora como host y KVM/QEMU + libvirt como plataforma de virtualización principal.

El objetivo no es aprender únicamente comandos de Vagrant. El estudiante debe comprender la relación entre Vagrant, vagrant-libvirt, libvirt, QEMU, KVM, networking, almacenamiento, Fedora, SELinux, firewalld, Ansible y Packer, y ser capaz de construir laboratorios reproducibles y diagnosticarlos.

## Alcance principal

- Fedora como sistema host.
- Linux/Fedora como guest preferente.
- KVM/QEMU como virtualización.
- libvirt como capa de gestión.
- vagrant-libvirt como provider principal.
- Vagrantfile y Ruby DSL.
- Boxes y su ciclo de vida.
- Networking y storage.
- Synced folders.
- Provisioning.
- Ansible como herramienta principal de configuración.
- Entornos multi-machine.
- Snapshots.
- Creación y mantenimiento de boxes.
- Packer para Image as Code.
- Seguridad.
- Troubleshooting.
- Rendimiento.
- Automatización y CI/CD.
- Internals de Vagrant.

## Fuera de foco

VirtualBox, VMware, Hyper-V y otros providers pueden mencionarse para explicar conceptos o diferencias, pero no deben convertirse en plataformas paralelas del curso.

El curso no debe duplicar un curso completo de:
- Ansible.
- Terraform/OpenTofu.
- Packer.
- Ruby.
- libvirt.
- administración Fedora.

Debe enseñar únicamente la profundidad necesaria para utilizar esas tecnologías correctamente dentro del dominio Vagrant.

## Modelo conceptual

Vagrant no es el hipervisor.

Vagrant -> provider vagrant-libvirt -> libvirt -> QEMU/KVM -> VM

La separación debe mantenerse durante todo el curso.

## Integración con otras herramientas

Packer:
Construye imágenes reproducibles y boxes.

Vagrant:
Crea y controla entornos de máquinas virtuales reproducibles, especialmente laboratorios y entornos de desarrollo.

Ansible:
Configura el sistema operativo y los servicios dentro de las máquinas.

Terraform/OpenTofu:
Gestiona infraestructura declarativa. Debe compararse con Vagrant para aclarar responsabilidades, no enseñarse de nuevo en profundidad.

## Enfoque Fedora

Los ejemplos deben favorecer herramientas y prácticas actuales de Fedora:
- dnf
- systemd
- journalctl
- NetworkManager
- firewalld
- nftables cuando sea relevante
- SELinux
- KVM/QEMU
- libvirt
- virsh

No asumir comandos o arquitecturas históricas cuando hayan sido sustituidos en Fedora/libvirt modernos.

## Laboratorios

Los laboratorios deben ser reproducibles, destruibles y reconstruibles.

La progresión recomendada es:
1. Una VM.
2. Configuración del Vagrantfile.
3. Networking.
4. Storage.
5. Provisioning.
6. Ansible.
7. Multi-machine.
8. Box propia.
9. Packer.
10. Proyecto final integrado.

## Proyecto final

Construir un laboratorio Fedora multi-machine sobre KVM/libvirt administrado por Vagrant y configurado mediante Ansible.

Debe demostrar:
- Vagrantfile mantenible.
- configuración del provider libvirt.
- varias VMs.
- redes.
- almacenamiento.
- provisioning idempotente.
- SELinux.
- firewalld.
- snapshots.
- logging.
- troubleshooting.
- tests.
- documentación.
- destrucción y reconstrucción reproducibles.

Como extensión, la imagen base se construirá con Packer.

## Criterio de nivel experto

El estudiante alcanza el nivel experto cuando puede explicar y diagnosticar cada capa:

Vagrant
↓
vagrant-libvirt
↓
libvirt
↓
QEMU/KVM
↓
kernel/Fedora

y puede determinar en qué capa se origina un problema sin tratar Vagrant como una caja negra.
