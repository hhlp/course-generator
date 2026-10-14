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

# Referencias por scope (selección para el generador)

La prioridad de fuentes se aplica por tema: para sintaxis y comportamiento actual de Fedora, prevalecen las páginas man y la documentación de la versión instalada frente al libro de 2020.

## Administración y diagnóstico — bloques 0–16
- Sven Vermeulen, *SELinux System Administration*, 3.ª ed.: base conceptual y administración.
- Fedora SELinux Documentation y páginas man locales: comandos, paquetes y comportamiento de plataforma.
- The SELinux Notebook: contextos, clases, permisos, MLS/MCS y auditoría.

## Desarrollo, módulos y Reference Policy — bloques 17–20
- SELinux Reference Policy: macros, interfaces, templates y estructura de módulos.
- Fedora SELinux Policy: implementación concreta y evolución de políticas distribuidas.
- SELinux Project / SELinux userspace: checkpolicy, checkmodule, semodule_package, semodule.

## Integraciones e internals — bloques 21–23
- Documentación de Fedora, systemd y container-selinux para la versión de laboratorio.
- The SELinux Notebook y código fuente Linux/SELinux userspace para hooks, AVC, SID y policydb.

## CIL y constraints — bloques 27–28
- SELinux Project, documentación CIL y secilc (incluyendo sus manuales).
- The SELinux Notebook: lenguaje de política, constraints y decisiones de acceso.
- Código fuente upstream: semántica exacta de compilación y validación.

## Testing, automatización e ingeniería inversa — bloques 29–31
- SETools (seinfo, sesearch, apol), documentación upstream y man pages.
- Documentación de Ansible y de las colecciones instaladas: verificar nombres y parámetros de módulos antes de utilizarlos.
- Fedora SELinux Policy y repositorios upstream para pruebas de regresión y comparaciones de versiones.

## Proyecto final — bloque 32
- Combinar fuentes de administración, SETools, auditoría, CIL y policy source; citar la procedencia de cada conclusión.

## Regla de trazabilidad
Cada lección debe indicar qué fuente sustenta la explicación, qué se ha comprobado en Fedora y qué depende de la versión. Evitar atribuir comandos o comportamientos modernos al libro cuando no los documente.
