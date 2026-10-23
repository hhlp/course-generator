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
6. Multi-machine.
7. Ansible sobre varias máquinas.
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

## Profundidad operativa exigida

Cada tema operativo debe explicar concepto, arquitectura, prerrequisitos, instalación o preparación, configuración, comandos con opciones explicadas, verificación, errores frecuentes, logs, seguridad, recuperación y laboratorio reproducible. La profundidad de libvirt/QEMU/KVM se limita a la necesaria para entender, configurar y diagnosticar Vagrant.

### Compatibilidad y límites del provider

No asumir que toda característica de libvirt está expuesta por vagrant-libvirt. Distinguir explícitamente soporte de Vagrant, soporte del plugin, soporte de libvirt/QEMU y capacidades del host/guest. Contrastar ejemplos con documentación actual y explicar alternativas cuando no exista soporte.

### Diagnóstico por capas

Aplicar hipótesis → captura de evidencia → localización de capa → corrección mínima → validación → prueba de regresión. Incluir VAGRANT_LOG, vagrant ssh-config, virsh, journalctl, logs QEMU, ip, bridge, tcpdump, nft y auditoría SELinux cuando corresponda. No presuponer nombres de servicios libvirt idénticos entre versiones.

### Seguridad y reproducibilidad

Preferir aislamiento y redes privadas, proteger secretos y claves, verificar origen e integridad de boxes y plugins, y advertir antes de destroy, cambios de disco o snapshots. Los laboratorios deben reconstruirse a partir de configuración versionada y artefactos identificados, sin depender de ediciones manuales persistentes en XML.

### Criterios de evaluación

Cada bloque operativo incluye al menos un laboratorio con requisitos, comandos, resultados esperados, verificación, errores deliberados y limpieza. Los bloques avanzados incluyen pruebas de recuperación. El proyecto final exige arranque desde cero, conectividad entre nodos, provisioning idempotente, tests, logs, medidas básicas de rendimiento y destrucción completa sin recursos huérfanos.

## Prerrequisitos y progresión revisada

El bloque 4 introduce el Ruby mínimo antes de utilizar arrays, hashes, bloques
e iteraciones en el Vagrantfile. El bloque 17 profundiza en evaluación del DSL,
alcance y refactorización, con la experiencia previa de los laboratorios.

El bloque 10 enseña entornos multi-machine; el bloque 11 aplica Ansible a esas
máquinas. No exigir configuración distribuida antes de enseñar config.vm.define.
Cada bloque desarrolla primero los conceptos y termina con sus laboratorios.

## Contrato de laboratorios y evaluación

Es obligatorio al menos un laboratorio por bloque operativo. Las lecciones
operativas incluyen práctica o una fase verificable del laboratorio del bloque;
las lecciones puramente conceptuales pueden utilizar ejemplos razonados.
No exigir repetir un despliegue completo en cada lección conceptual.

Cada laboratorio declara prerrequisitos, recursos, versiones, acciones,
resultados esperados, criterios de aceptación, diagnóstico y limpieza.
Los escenarios avanzados incorporan fallos deliberados y recuperación.

## Precisiones operativas

- Diferenciar la red de gestión del provider de las redes de datos del proyecto.
  Explicar su papel en descubrimiento de IP y SSH antes de depurar conectividad.
- Diferenciar bridge Linux y macvtap y comprobar sus restricciones de conexión.
- Actualizar una box no modifica las máquinas existentes. Enseñar una recreación
  controlada, identificando primero los datos que deben conservarse.
- No modificar imágenes activas mediante qemu-img. Explicar qué operaciones
  requieren VM apagada y cuándo debe utilizarse la gestión de discos de libvirt.
- Distinguir el metadata.json incluido en la box del catálogo JSON que publica
  versiones, providers, arquitecturas, URLs y checksums.
- Definir reproducibilidad como reconstrucción verificable con entradas
  identificadas y criterios de equivalencia. No prometer igualdad binaria por
  utilizar Packer: requiere controlar también fuentes, paquetes y otras entradas.

## Integración con course-generator

Los nombres finales son initial.txt, profile.yaml, domain.md y bibliography.md.
La referencia ../../config/pedagogy.md conserva la configuración recibida y debe
resolverse según las reglas del cargador y la ubicación real del perfil en el
repositorio. No inferir la compatibilidad del cargador solo por validar YAML.
