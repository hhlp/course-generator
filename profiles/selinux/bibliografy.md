# Bibliografía — SELinux en profundidad

## Bibliografía principal

### SELinux System Administration, Third Edition

Autor: Sven Vermeulen
Editorial: Packt Publishing
Edición: Third Edition
Año: 2020
ISBN: 9781800201477

Rol dentro del PATH:

PRINCIPAL

Este libro constituye la referencia bibliográfica principal del PATH
SELinux en profundidad.

Se utilizará principalmente para:

- fundamentos de SELinux
- Mandatory Access Control
- Linux Security Modules
- security contexts
- SELinux users
- roles
- types
- domains
- Type Enforcement
- RBAC
- MLS
- MCS
- políticas SELinux
- gestión de políticas
- administración de usuarios
- administración de aplicaciones
- integración con servicios
- networking
- troubleshooting
- auditoría
- administración práctica de SELinux

El libro debe utilizarse como guía conceptual y administrativa.

El PATH no debe limitarse a la estructura ni profundidad del libro.


# Documentación principal de plataforma

## Fedora SELinux Documentation

Rol:

PLATAFORMA / IMPLEMENTACIÓN

Debe utilizarse para adaptar los conceptos del libro al entorno Fedora.

Prioridad especialmente alta para:

- paquetes
- comandos disponibles
- políticas distribuidas por Fedora
- targeted policy
- selinux-policy
- selinux-policy-targeted
- policycoreutils
- policycoreutils-python-utils
- setools-console
- setroubleshoot
- audit
- systemd
- RPM
- actualizaciones de políticas
- particularidades de Fedora


# Referencia upstream

## SELinux Project

Rol:

REFERENCIA UPSTREAM

Utilizar para estudiar:

- arquitectura SELinux
- userspace
- libselinux
- libsepol
- libsemanage
- policycoreutils
- checkpolicy
- secilc
- semodule
- semanage
- herramientas internas
- interfaces
- evolución del proyecto


## The SELinux Notebook

Proyecto: SELinuxProject

Rol:

PROFUNDIZACIÓN / INTERNALS / REFERENCIA

Debe utilizarse especialmente para:

- arquitectura interna
- Linux Security Modules
- SELinux kernel components
- Access Vector Cache
- security server
- object managers
- security identifiers
- contexts
- object classes
- permissions
- policy language
- binary policy
- policy stores
- policy configuration
- Reference Policy
- CIL
- networking
- filesystem labeling
- usuarios y roles
- MLS/MCS
- internals


# Política Fedora

## Fedora SELinux Policy

Rol:

IMPLEMENTACIÓN REAL

Debe utilizarse para estudiar políticas reales utilizadas por Fedora.

Especialmente importante para:

- tipos
- dominios
- atributos
- interfaces
- file contexts
- port contexts
- booleans
- transitions
- allow rules
- dontaudit
- neverallow
- módulos
- macros
- interfaces
- ejemplos reales


# Reference Policy

## SELinux Reference Policy

Rol:

PROFUNDIZACIÓN

Utilizar para comprender:

- arquitectura de políticas
- módulos
- interfaces
- templates
- attributes
- domains
- file types
- network types
- policy abstractions
- construcción de políticas
- organización del source tree


# Manual pages

Las páginas man forman parte de la bibliografía obligatoria del PATH.

Consultar según la lección:

selinux(8)
sestatus(8)
getenforce(8)
setenforce(8)
semanage(8)
semodule(8)
semodule_package(8)
restorecon(8)
setfiles(8)
chcon(1)
matchpathcon(8)
seinfo(1)
sesearch(1)
ausearch(8)
aureport(8)
audit2why(1)
audit2allow(1)
sepolicy(8)
checkpolicy(8)
checkmodule(8)
secilc(8)
selinux_config(5)
file_contexts(5)
semanage.conf(5)

Las páginas man instaladas en Fedora tienen prioridad para determinar
la sintaxis exacta disponible en el sistema utilizado en los
laboratorios.


# Código fuente

Cuando el PATH alcance internals debe consultarse directamente:

- SELinux userspace
- Linux kernel
- SELinux policy
- Reference Policy

El código fuente se utilizará para comprender implementación y no
solamente comportamiento observable.


# Orden de prioridad

Para cada lección:

1. SELinux System Administration, Third Edition
2. documentación Fedora
3. páginas man del sistema Fedora
4. SELinux Project
5. SELinux Notebook
6. Fedora SELinux Policy
7. Reference Policy
8. código fuente cuando corresponda


# Regla de actualidad

El libro principal es una referencia conceptual, no una especificación
de la versión actual.

Cuando exista una diferencia entre el libro y Fedora actual:

- explicar el comportamiento histórico cuando sea relevante
- utilizar el comportamiento actual de Fedora para los laboratorios
- señalar cambios importantes
- utilizar documentación upstream para resolver diferencias


# Filosofía bibliográfica

El PATH debe enseñar a investigar SELinux sin depender de memorizar
configuraciones para servicios concretos.

El estudiante debe aprender dónde encontrar:

- contexts
- types
- domains
- attributes
- roles
- users
- booleans
- ports
- object classes
- permissions
- interfaces
- transitions
- policy rules
- file-context definitions
- módulos instalados

El objetivo final es poder investigar una política SELinux desconocida.
