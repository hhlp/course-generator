# BIBLIOGRAFÍA — ANSIBLE 0 → EXPERTO

## 1. Propósito de esta bibliografía

Esta bibliografía acompaña al PATH completo de Ansible desde los fundamentos hasta arquitectura y automatización a escala.

Las fuentes no deben tratarse como equivalentes. Cada una cumple una función concreta dentro del proceso de generación de las lecciones.

El PATH debe combinar:

* fundamentos sólidos;
* comprensión profunda de Ansible Core;
* automatización de Fedora y RHEL;
* automatización de redes;
* containers;
* Kubernetes y OpenShift;
* cloud;
* Infrastructure as Code;
* CI/CD;
* AWX;
* Red Hat Ansible Automation Platform;
* Execution Environments;
* Event-Driven Ansible;
* desarrollo de módulos y plugins;
* testing;
* seguridad;
* rendimiento;
* escalabilidad;
* troubleshooting;
* internals;
* arquitectura de plataformas de automatización.

Los libros proporcionan estructura pedagógica, explicación, ejemplos y profundidad.

La documentación oficial proporciona la referencia técnica autoritativa y actual.

---

# 2. Fuente principal

## Ansible: Up & Running

Editorial: O'Reilly Media.

### Función

Fuente pedagógica principal del PATH.

Debe utilizarse especialmente para construir una comprensión progresiva de Ansible y de su modelo de automatización.

### Áreas principales

* filosofía de Ansible;
* arquitectura general;
* nodo de control;
* managed nodes;
* SSH;
* inventarios;
* grupos;
* variables;
* facts;
* módulos;
* tasks;
* plays;
* playbooks;
* handlers;
* conditionals;
* loops;
* templates;
* Jinja2;
* roles;
* Vault;
* collections;
* reutilización;
* organización de proyectos;
* buenas prácticas;
* troubleshooting básico e intermedio.

### Uso dentro del PATH

Debe actuar como columna vertebral pedagógica durante los bloques fundamentales e intermedios.

No debe considerarse una referencia absoluta sobre comportamiento de versiones modernas.

Cuando su contenido dependa de una versión concreta de Ansible, deberá contrastarse con la documentación oficial actual.

---

# 3. Fuente de profundización

## Mastering Ansible — 4th Edition

Autores:

James Freeman
Jesse Keating

Editorial: Packt.

### Función

Fuente principal para profundización técnica.

Debe utilizarse cuando el PATH pase de enseñar cómo utilizar Ansible a explicar cómo funciona y cómo extenderlo.

### Áreas principales

* arquitectura de Ansible;
* funcionamiento avanzado;
* inventarios complejos;
* variables;
* precedencia;
* ejecución de playbooks;
* estrategias;
* delegación;
* control de ejecución;
* roles avanzados;
* plugins;
* filtros;
* lookups;
* callbacks;
* conexiones;
* módulos;
* Python;
* extensibilidad;
* debugging;
* troubleshooting;
* network automation;
* rendimiento;
* diseño de automatizaciones complejas.

### Uso dentro del PATH

Especialmente importante en los niveles:

intermedio → avanzado → experto.

Debe utilizarse como apoyo para comprender los mecanismos internos detrás de las abstracciones utilizadas por Ansible.

Los detalles dependientes de versiones deben verificarse mediante documentación oficial.

---

# 4. Fuente de automatización en escenarios reales

## Ansible for Real-Life Automation

Autor:

Gineesh Madapparambath

Editorial: Packt.

### Función

Fuente principal para casos de uso reales y automatización aplicada.

Complementa las fuentes conceptuales mostrando cómo combinar componentes de Ansible para resolver problemas de infraestructura reales.

### Áreas principales

* administración de sistemas;
* automatización de infraestructura;
* operaciones;
* redes;
* cloud;
* containers;
* plataformas de containers;
* Kubernetes;
* OpenShift;
* CI/CD;
* integración con otras herramientas;
* escenarios empresariales;
* Red Hat Ansible Automation Platform;
* workflows de automatización.

### Uso dentro del PATH

Debe utilizarse principalmente en:

* laboratorios;
* escenarios de producción;
* integración entre tecnologías;
* ejercicios acumulativos;
* proyectos;
* automatización multiinfraestructura.

Debe ayudar a evitar que el aprendizaje quede limitado a ejemplos artificiales de playbooks.

---

# 5. Fuente práctica avanzada

## Practical Ansible — 2nd Edition

### Función

Fuente de implementación práctica, laboratorios y automatización operacional.

Debe utilizarse como complemento práctico de Ansible: Up & Running y Mastering Ansible.

### Áreas de interés

* configuración de entornos;
* inventarios;
* playbooks;
* roles;
* reutilización;
* automatización práctica;
* Vault;
* collections;
* testing;
* desarrollo;
* troubleshooting;
* automatización cloud;
* containers;
* AWX;
* Ansible Automation Controller;
* Execution Environments;
* operación de plataformas de automatización.

### Uso dentro del PATH

Especialmente útil para:

* laboratorios;
* ejercicios prácticos;
* testing;
* automatización reproducible;
* AWX;
* Automation Controller;
* Execution Environments;
* transición desde Ansible Core hacia plataformas empresariales.

---

# 6. Documentación oficial de Ansible

## Ansible Community Documentation

La documentación oficial de Ansible constituye la referencia técnica primaria para Ansible Core y el ecosistema comunitario.

### Consultar especialmente

* ansible-core;
* ansible;
* ansible-playbook;
* ansible-config;
* ansible-inventory;
* ansible-doc;
* ansible-galaxy;
* ansible-vault;
* ansible-console;
* configuración;
* inventarios;
* variables;
* precedence rules;
* playbooks;
* roles;
* collections;
* modules;
* plugins;
* filters;
* lookups;
* callbacks;
* connection plugins;
* strategy plugins;
* become plugins;
* inventory plugins;
* module development;
* plugin development;
* Python API cuando corresponda;
* testing;
* porting guides;
* changelogs.

### Regla

Debe comprobarse la documentación correspondiente a la versión estudiada siempre que el comportamiento pueda haber cambiado entre versiones.

---

# 7. Red Hat Ansible Automation Platform

## Red Hat Ansible Automation Platform Documentation

Fuente autoritativa para los componentes empresariales de Red Hat Ansible Automation Platform.

### Áreas principales

* arquitectura de AAP;
* Automation Controller;
* Automation Hub;
* Private Automation Hub;
* Execution Environments;
* automation execution;
* ansible-navigator;
* credentials;
* inventories;
* projects;
* organizations;
* teams;
* RBAC;
* workflows;
* job templates;
* scheduling;
* APIs;
* webhooks;
* authentication;
* logging;
* auditing;
* scaling;
* clustering;
* high availability;
* disaster recovery;
* seguridad;
* administración;
* upgrades;
* troubleshooting.

Debe utilizarse también para estudiar la arquitectura empresarial de una plataforma de automatización.

---

# 8. Event-Driven Ansible

Para Event-Driven Ansible deben priorizarse las fuentes oficiales actuales del proyecto y de Red Hat Ansible Automation Platform.

### Áreas principales

* Event-Driven Automation;
* ansible-rulebook;
* rulebooks;
* events;
* sources;
* rules;
* conditions;
* actions;
* event sources;
* decision environments;
* Event-Driven Ansible Controller;
* integración con sistemas externos;
* observabilidad;
* automatización reactiva;
* remediation;
* event-driven operations.

Debido a la rápida evolución de esta área, la documentación oficial tiene prioridad especialmente alta.

---

# 9. Ansible Builder y Execution Environments

Debe utilizarse documentación oficial para estudiar:

* Execution Environments;
* imágenes OCI;
* ansible-builder;
* execution-environment.yml;
* dependencias Python;
* dependencias del sistema;
* collections;
* ansible-core;
* ansible-runner;
* construcción de imágenes;
* publicación;
* registries;
* reproducibilidad;
* versionado;
* seguridad;
* supply chain;
* integración con AAP.

Execution Environments deben tratarse como parte fundamental del Ansible moderno y no como un añadido opcional.

---

# 10. Ansible Navigator

La documentación oficial de ansible-navigator debe utilizarse para:

* ejecución de playbooks;
* Execution Environments;
* inventories;
* collections;
* configuración;
* artefactos;
* introspección;
* troubleshooting;
* transición desde herramientas tradicionales de CLI hacia workflows basados en Execution Environments.

---

# 11. Ansible Runner

Consultar documentación oficial y código del proyecto cuando el PATH estudie:

* ansible-runner;
* ejecución programática;
* artifacts;
* events;
* callbacks;
* integración con aplicaciones;
* ejecución aislada;
* Execution Environments;
* APIs;
* integración con plataformas superiores.

Debe relacionarse conceptualmente con Automation Controller y otras plataformas que ejecutan automatizaciones.

---

# 12. Ansible Collections

La documentación oficial y Ansible Galaxy deben utilizarse para estudiar:

* namespaces;
* collections;
* modules;
* plugins;
* roles;
* dependencies;
* galaxy.yml;
* MANIFEST.json;
* versionado;
* distribución;
* publicación;
* instalación;
* documentación;
* testing;
* desarrollo de collections.

Las collections deben tratarse como unidad fundamental de distribución de contenido Ansible moderno.

---

# 13. Fedora y RHEL

Para automatización de sistemas deben utilizarse también:

## Fedora Documentation

Para:

* Fedora;
* systemd;
* firewalld;
* SELinux;
* NetworkManager;
* DNF;
* almacenamiento;
* usuarios;
* servicios;
* containers;
* Podman.

## Red Hat Enterprise Linux Documentation

Fuente principal para automatización específica de RHEL.

Especialmente:

* system roles;
* SELinux;
* firewalld;
* systemd;
* NetworkManager;
* storage;
* LVM;
* Stratis;
* users;
* security;
* Podman;
* software management;
* repositories;
* administración empresarial.

Ansible no debe enseñarse aislado del sistema que está automatizando.

---

# 14. Red Hat System Roles

Consultar documentación oficial de RHEL y de la colección correspondiente.

Debe utilizarse para estudiar:

* Linux System Roles;
* automatización soportada por Red Hat;
* networking;
* storage;
* firewall;
* SELinux;
* timesync;
* logging;
* certificates;
* kernel settings;
* SSH;
* Podman;
* otras funciones disponibles según versión.

Debe compararse la utilización de System Roles con el desarrollo manual de roles propios.

---

# 15. Network Automation

Cuando el PATH llegue a automatización de redes deben utilizarse las collections y documentación oficial de los fabricantes correspondientes.

Estudiar conceptualmente:

* network_cli;
* httpapi;
* NETCONF;
* RESTCONF;
* APIs;
* network resource modules;
* facts;
* configuración declarativa;
* backup;
* diff;
* validation;
* idempotencia;
* inventories de red;
* credenciales;
* seguridad;
* troubleshooting.

No debe asumirse que administrar dispositivos de red funciona igual que administrar hosts Linux mediante SSH.

---

# 16. Containers

Para containers deben utilizarse fuentes oficiales de:

* Podman;
* Buildah;
* Skopeo;
* OCI;
* container registries;
* collections Ansible relacionadas.

El PATH debe relacionar Ansible con:

* lifecycle de containers;
* imágenes;
* registries;
* networks;
* volumes;
* pods;
* secrets;
* systemd;
* Quadlet cuando corresponda;
* construcción de imágenes;
* despliegue;
* actualización;
* automatización reproducible.

Fedora/RHEL y tecnologías compatibles con su ecosistema constituyen la plataforma Linux principal del PATH.

---

# 17. Kubernetes y OpenShift

Utilizar documentación oficial de:

* Kubernetes;
* Red Hat OpenShift;
* collections de Ansible correspondientes;
* Operator SDK cuando corresponda.

Estudiar:

* API Kubernetes;
* recursos;
* manifests;
* namespaces;
* authentication;
* RBAC;
* deployments;
* services;
* ConfigMaps;
* Secrets;
* operators;
* automatización de clusters;
* automatización de aplicaciones;
* integración Ansible/Kubernetes.

Debe explicarse claramente cuándo utilizar Ansible y cuándo utilizar mecanismos declarativos nativos de Kubernetes.

---

# 18. Cloud

Cuando el PATH estudie cloud, utilizar documentación oficial del proveedor y de las collections Ansible correspondientes.

Debe cubrirse conceptualmente:

* autenticación;
* credentials;
* APIs;
* provisioning;
* compute;
* networking;
* storage;
* IAM;
* inventories dinámicos;
* tags;
* secrets;
* idempotencia;
* lifecycle;
* teardown;
* seguridad;
* costes;
* testing;
* troubleshooting.

El objetivo no es convertir el PATH en un curso completo de cada proveedor cloud, sino enseñar cómo Ansible interactúa correctamente con ellos.

---

# 19. Infrastructure as Code

Para IaC deben utilizarse fuentes oficiales de las herramientas que se integren con Ansible.

Debe estudiarse la relación entre:

Ansible → configuration management

Terraform/OpenTofu → provisioning declarativo

Kubernetes → desired-state orchestration

Git → control de versiones

CI/CD → automatización del ciclo de entrega

Ansible no debe presentarse como sustituto universal de todas las herramientas IaC.

---

# 20. CI/CD y GitOps

Consultar documentación oficial de las plataformas utilizadas cuando corresponda.

Áreas:

* Git;
* repositories;
* branching;
* pull/merge requests;
* pipelines;
* linting;
* testing;
* ansible-lint;
* Molecule;
* CI;
* deployment;
* secrets;
* artifacts;
* Execution Environments;
* registries;
* promotion;
* rollback;
* GitOps;
* policy enforcement.

---

# 21. Testing y calidad

Utilizar documentación oficial de:

* ansible-lint;
* Molecule;
* pytest cuando corresponda;
* ansible-test;
* testing de collections.

Estudiar:

* syntax checks;
* linting;
* unit testing;
* integration testing;
* scenario testing;
* idempotence testing;
* molecule scenarios;
* test matrices;
* CI;
* regression testing;
* collection testing.

La automatización debe tratarse como software y, por tanto, debe probarse.

---

# 22. Desarrollo de módulos y plugins

Las fuentes principales deben ser la documentación para desarrolladores de Ansible y el código fuente de ansible-core.

Estudiar:

* Python;
* arquitectura de módulos;
* AnsibleModule;
* argument_spec;
* return values;
* check mode;
* diff mode;
* idempotencia;
* error handling;
* module_utils;
* plugins;
* callbacks;
* filters;
* lookups;
* inventory plugins;
* connection plugins;
* strategy plugins;
* documentation fragments;
* testing;
* ansible-test.

En nivel experto debe utilizarse directamente el código fuente de ansible-core cuando sea necesario comprender el comportamiento interno.

---

# 23. Código fuente

## ansible-core source code

Fuente de profundización para el nivel experto.

Debe consultarse cuando sea necesario estudiar:

* arquitectura interna;
* plugin loader;
* inventory manager;
* variable manager;
* task execution;
* strategies;
* connection handling;
* templating;
* collections loader;
* module execution;
* serialization;
* multiprocessing;
* callbacks;
* errors;
* internals.

No es necesario estudiar todo el código fuente de manera lineal.

Debe utilizarse selectivamente para conectar conceptos del PATH con su implementación real.

---

# 24. Seguridad

La seguridad debe contrastarse con documentación oficial de:

* Ansible;
* Red Hat;
* Fedora;
* RHEL;
* OpenSSH;
* SELinux;
* container security;
* Kubernetes/OpenShift;
* proveedores cloud.

Áreas:

* Vault;
* secrets;
* credentials;
* privilege escalation;
* become;
* SSH;
* RBAC;
* least privilege;
* Execution Environments;
* supply chain;
* signed content;
* Automation Hub;
* private repositories;
* tokens;
* API credentials;
* auditing;
* logging;
* isolation.

---

# 25. Escalabilidad y arquitectura empresarial

Para niveles experto y arquitecto utilizar prioritariamente documentación oficial de Red Hat Ansible Automation Platform.

Estudiar:

* control plane;
* execution plane;
* execution nodes;
* hop nodes;
* instance groups;
* mesh;
* Receptor;
* Automation Controller;
* Automation Hub;
* Event-Driven Ansible;
* Execution Environments;
* capacity;
* scheduling;
* scaling;
* HA;
* topology;
* observability;
* disaster recovery;
* governance;
* RBAC;
* lifecycle management.

---

# 26. Orden recomendado de utilización

### Nivel inicial

1. Ansible: Up & Running.
2. Documentación oficial de Ansible.
3. Practical Ansible, 2nd Edition.

### Nivel intermedio

1. Ansible: Up & Running.
2. Mastering Ansible, 4th Edition.
3. Practical Ansible, 2nd Edition.
4. Ansible for Real-Life Automation.
5. Documentación oficial.

### Nivel avanzado

1. Mastering Ansible, 4th Edition.
2. Ansible for Real-Life Automation.
3. Practical Ansible, 2nd Edition.
4. Documentación oficial de Ansible.
5. Documentación específica de las tecnologías automatizadas.

### Nivel experto

1. Documentación oficial.
2. Código fuente de ansible-core.
3. Documentación de desarrollo de Ansible.
4. Red Hat Ansible Automation Platform.
5. Documentación de las collections.
6. Documentación de las tecnologías integradas.
7. Libros como apoyo conceptual y pedagógico.

---

# 27. Regla de autoridad de las fuentes

Cuando varias fuentes proporcionen información diferente, utilizar este orden de prioridad:

1. comportamiento real verificable de la versión utilizada;
2. documentación oficial correspondiente a esa versión;
3. documentación oficial del proyecto;
4. documentación oficial de Red Hat cuando se trate de RHEL/AAP;
5. código fuente;
6. documentación de collections y proveedores;
7. libros recientes;
8. libros correspondientes a versiones anteriores;
9. otras fuentes secundarias.

Un libro nunca debe utilizarse para forzar un comportamiento perteneciente a una versión antigua sobre una versión moderna.

---

# 28. Regla de actualización

Ansible, sus collections y Red Hat Ansible Automation Platform evolucionan continuamente.

Antes de generar contenido sensible a versiones deben comprobarse especialmente:

* comandos;
* opciones;
* configuración;
* nombres de plugins;
* módulos;
* collections;
* APIs;
* componentes de AAP;
* Execution Environments;
* ansible-builder;
* ansible-navigator;
* Event-Driven Ansible;
* características deprecated;
* características eliminadas;
* requisitos de Python;
* compatibilidad con Fedora/RHEL.

No presentar características obsoletas como prácticas actuales.

Cuando resulte pedagógicamente útil explicar una característica histórica, debe identificarse explícitamente como histórica, deprecated o eliminada.

---

# 29. Principio pedagógico

La bibliografía no define por sí sola el alcance del PATH.

Los libros son fuentes de apoyo.

El PATH define el conocimiento que debe adquirirse.

Una lección no debe reducir su profundidad porque un determinado libro trate superficialmente el tema.

Cuando los libros no sean suficientes deberán utilizarse:

* documentación oficial;
* documentación técnica del proyecto;
* código fuente;
* especificaciones;
* documentación de APIs;
* documentación de proveedores;
* experimentación práctica.

---

# 30. Objetivo final

La bibliografía debe permitir progresar desde:

automatización básica

→ inventarios

→ módulos

→ playbooks

→ variables

→ Jinja2

→ roles

→ collections

→ testing

→ Fedora/RHEL

→ redes

→ containers

→ Kubernetes/OpenShift

→ cloud

→ IaC

→ CI/CD

→ AWX

→ Red Hat Ansible Automation Platform

→ Execution Environments

→ Event-Driven Ansible

→ desarrollo de módulos/plugins

→ seguridad

→ troubleshooting

→ rendimiento

→ escalabilidad

→ internals

→ arquitectura

→ gobernanza

→ plataforma empresarial de automatización.

El objetivo final no es únicamente aprender a escribir playbooks.

El objetivo es comprender, diseñar, desarrollar, operar, depurar, asegurar y escalar plataformas completas de automatización basadas en Ansible.
