# BIBLIOGRAPHY — CONTENEDORES EN PROFUNDIDAD
## Podman + Docker + Buildah + Skopeo

## Criterio bibliográfico

Los libros son una base pedagógica, no el límite del PATH.

El curso combina:

1. documentación oficial y especificaciones para comportamiento actual;
2. libros para estructura, explicación y aprendizaje progresivo;
3. documentación Fedora/Red Hat para integración con el sistema;
4. documentación upstream y código fuente para temas internos.

Esto es especialmente importante porque Podman, Docker, Buildah, Skopeo y OCI
evolucionan con mayor rapidez que una edición impresa.

---

## 1. Bibliografía principal

### 1.1 Podman for DevOps

**Alessandro Arrichiello, Gianni Salinetti.**
*Podman for DevOps: Build secure, rootless containers, and integrate them into
real DevOps and AI workflows.*
Second Edition. Packt Publishing, 2026.

### Papel dentro del PATH

Es la referencia principal para el ecosistema moderno de herramientas
`containers/*`.

Utilizar especialmente para:

- Podman;
- rootless containers;
- Buildah;
- Skopeo;
- imágenes;
- registries;
- seguridad;
- SELinux;
- systemd;
- Kubernetes integration;
- workflows DevOps.

### Prioridad

**Principal.**

Es especialmente importante porque trata conjuntamente Podman, Buildah y
Skopeo, que es precisamente uno de los objetivos arquitectónicos de este PATH.

---

### 1.2 Podman in Action

**Daniel Walsh.**
*Podman in Action: Secure, Rootless Containers for Kubernetes, Microservices,
and More.*
Manning, 2023.

### Papel dentro del PATH

Referencia de profundidad para la arquitectura y filosofía de Podman.

Utilizar especialmente para:

- arquitectura de Podman;
- pods;
- volumes;
- configuración;
- rootless;
- user namespaces;
- systemd;
- Kubernetes;
- Podman service;
- aislamiento;
- seguridad;
- SELinux;
- transición desde Docker.

El autor lideró el equipo responsable de Podman, Buildah, Skopeo y otras
herramientas del ecosistema, por lo que esta obra es especialmente útil para
comprender decisiones de diseño y seguridad.

### Prioridad

**Principal / profundización.**

---

### 1.3 The Ultimate Docker Container Book

**Gabriel N. Schenker.**
*The Ultimate Docker Container Book: Build, test, ship, and run containers
with Docker and Kubernetes.*
Third Edition. Packt Publishing, 2023. ISBN-13: 9781804613986.

Esta es la edición pedagógica de referencia; validar comandos y opciones
contra la versión instalada y la documentación oficial correspondiente.

### Papel dentro del PATH

Referencia principal del lado Docker y de los fundamentos generales de
contenedores.

Utilizar especialmente para:

- fundamentos de containerization;
- Docker;
- imágenes;
- lifecycle de contenedores;
- Dockerfile;
- volumes;
- networking;
- Docker Compose;
- aplicaciones multicontenedor;
- debugging;
- seguridad;
- construcción, publicación y ejecución de imágenes;
- transición conceptual hacia orquestadores.

### Prioridad

**Principal para Docker.**

No debe emplearse como única autoridad para comportamiento específico de
Podman, Buildah o Skopeo.

---

## 2. Mapa de uso de los libros

| Área | Referencia principal | Complementaria |
|---|---|---|
| Fundamentos de contenedores | The Ultimate Docker Container Book | Podman for DevOps |
| Docker | The Ultimate Docker Container Book | Documentación Docker |
| Podman | Podman for DevOps | Podman in Action |
| Rootless | Podman in Action | Podman for DevOps |
| Buildah | Podman for DevOps | Documentación Buildah |
| Skopeo | Podman for DevOps | Documentación Skopeo |
| SELinux + containers | Podman in Action | Fedora/Red Hat docs |
| systemd + Podman | Podman in Action | Podman docs |
| Quadlet | Documentación actual Podman | Podman for DevOps |
| OCI | Especificaciones OCI | los tres libros |
| Images | los tres libros | OCI Image Spec |
| Registries | Podman for DevOps | OCI Distribution / Docker docs |
| Docker Compose | The Ultimate Docker Container Book | Compose Specification |
| Podman/Docker migration | Podman in Action | Podman for DevOps |
| Troubleshooting | documentación oficial + laboratorios | los tres libros |
| Internals | documentación/código upstream | Podman in Action |

---

## 3. Documentación oficial obligatoria

### Podman

Documentación oficial de Podman y páginas de manual instaladas.

Consultar para:

- comandos;
- comportamiento de la versión instalada;
- containers.conf;
- pods;
- rootless;
- networking;
- Quadlet;
- APIs;
- systemd;
- manifests.

### Buildah

Documentación oficial y páginas `man`.

Consultar para:

- `buildah from`;
- `buildah run`;
- `buildah copy`;
- `buildah config`;
- `buildah mount`;
- `buildah commit`;
- `buildah bud`;
- manifests;
- push;
- rootless builds.

### Skopeo

Documentación oficial y páginas `man`.

Consultar para:

- inspect;
- copy;
- sync;
- delete;
- list-tags;
- image transports;
- TLS;
- authentication;
- signatures;
- policy.

### Docker

Documentación oficial Docker.

Consultar para:

- Docker Engine;
- Docker CLI;
- dockerd;
- Dockerfile;
- Build;
- Compose;
- storage;
- networking;
- logging;
- API.

---

## 4. Especificaciones

### Open Container Initiative

Referencias fundamentales:

- OCI Image Specification;
- OCI Runtime Specification;
- OCI Distribution Specification.

Estas especificaciones tienen prioridad sobre explicaciones simplificadas de
los libros cuando el tema sea interoperabilidad o formato.

### Compose Specification

Referencia normativa para conceptos modernos de Compose.

---

## 5. Fedora y Red Hat

Utilizar documentación Fedora y Red Hat cuando el comportamiento dependa de la
plataforma.

Áreas importantes:

- Podman en Fedora;
- rootless containers;
- SELinux;
- container labels;
- systemd;
- Quadlet;
- firewalld;
- cgroups v2;
- user namespaces;
- registries;
- container tools.

---

## 6. Linux

Para internals deben utilizarse además:

- `man namespaces`;
- `man user_namespaces`;
- `man pid_namespaces`;
- `man mount_namespaces`;
- `man network_namespaces`;
- `man cgroups`;
- `man capabilities`;
- `man seccomp`;
- documentación del kernel;
- documentación OverlayFS.

La CLI de un container engine nunca debe sustituir la explicación de los
mecanismos Linux subyacentes.

---

## 7. Componentes upstream de profundización

Cuando una lección llegue a nivel interno, consultar documentación o código
fuente upstream de:

- Podman;
- Buildah;
- Skopeo;
- containers/image;
- containers/storage;
- containers/common;
- conmon;
- crun;
- runc;
- containerd;
- Netavark;
- Aardvark DNS;
- CRI-O.

Estas referencias son de **profundización**, no una exigencia para cada
lección.

---

## 8. Orden de autoridad

Cuando existan discrepancias:

```text
especificación / documentación oficial actual
        ↓
documentación de Fedora/Red Hat
        ↓
documentación upstream y man pages
        ↓
libros
        ↓
artículos y fuentes secundarias
```

Los libros explican y estructuran. La documentación actual determina el
comportamiento de las versiones presentes.

---

## 9. Estrategia por niveles

### Principiante

Priorizar:

- The Ultimate Docker Container Book;
- Podman for DevOps;
- documentación básica de Podman/Docker.

### Intermedio

Añadir:

- Podman in Action;
- man pages;
- Fedora/Red Hat docs;
- OCI Image Specification.

### Avanzado

Añadir:

- OCI Runtime Specification;
- OCI Distribution Specification;
- containers/image;
- containers/storage;
- cgroups v2;
- namespaces;
- SELinux;
- API documentation.

### Experto

Añadir:

- código fuente upstream;
- runtime internals;
- conmon;
- crun/runc;
- Netavark;
- OverlayFS;
- networking Linux;
- tracing y diagnóstico de procesos;
- análisis de manifests y blobs;
- diseño del proyecto `container-debugger`.

---

## 10. Regla para generación de lecciones

La bibliografía no debe provocar que la lección copie la estructura de un
libro.

Para cada tema:

1. seguir el orden del PATH;
2. utilizar el libro más apropiado para construir la explicación;
3. contrastar comportamiento actual con documentación oficial;
4. adaptar comandos y rutas a Fedora;
5. relacionar Podman, Docker, Buildah y Skopeo cuando sea técnicamente útil;
6. incluir internals solo hasta la profundidad que corresponda a la lección;
7. mantener continuidad con las lecciones anteriores y posteriores.

---

## 11. Bibliografía específica por herramienta

### Docker

Principal:

- Gabriel N. Schenker — *The Ultimate Docker Container Book*.

Complementar con:

- Docker Engine documentation;
- Docker CLI documentation;
- Dockerfile reference;
- Docker Compose documentation;
- Compose Specification.

### Podman

Principal:

- Alessandro Arrichiello & Gianni Salinetti — *Podman for DevOps*.
- Daniel Walsh — *Podman in Action*.

Complementar con:

- Podman documentation;
- Podman man pages;
- containers.conf documentation;
- Quadlet documentation.

### Buildah

Principal:

- *Podman for DevOps*.

Complementar con:

- Buildah documentation;
- Buildah man pages;
- containers/image;
- containers/storage.

### Skopeo

Principal:

- *Podman for DevOps*.

Complementar con:

- Skopeo documentation;
- Skopeo man pages;
- containers-transports documentation;
- OCI specifications.

---

## 12. Bibliografía específica para seguridad

Priorizar conjuntamente:

- *Podman in Action*;
- *Podman for DevOps*;
- Fedora SELinux documentation;
- Red Hat container security documentation;
- Linux capabilities documentation;
- seccomp documentation;
- OCI specifications.

Temas:

- rootless;
- user namespaces;
- capabilities;
- SELinux;
- seccomp;
- signatures;
- image provenance;
- digest pinning;
- secrets;
- mínimo privilegio.

---

## 13. Bibliografía específica para el proyecto final

Para `container-debugger` utilizar:

- man pages de Podman/Docker/Buildah/Skopeo;
- JSON generado por `inspect`;
- Podman API;
- Docker Engine API;
- Linux `/proc`;
- namespaces;
- cgroups v2;
- systemd;
- SELinux;
- iproute2;
- nftables;
- containers/storage;
- containers/image;
- OCI Image Specification.

El proyecto final debe consolidar el dominio, no limitarse a envolver comandos.

## 14. Scopes expertos y asignación de fuentes (bloques 40–52)

Los tres libros originales siguen siendo las referencias pedagógicas principales. Para los temas no cubiertos con suficiente detalle, se utilizan especificaciones y documentación técnica, sin atribuir a los libros contenido que no se haya comprobado.

| Scope | Bloque | Referencia pedagógica | Referencia técnica prioritaria |
|---|---:|---|---|
| Linux internals y OCI runtime | 40 | Podman in Action | Linux man-pages, OCI Runtime Spec, runc/crun |
| Podman avanzado | 41 | Podman for DevOps; Podman in Action | Podman manual y documentación Quadlet |
| Docker BuildKit/Buildx | 42 | The Ultimate Docker Container Book | Docker Build docs; BuildKit upstream |
| Buildah experto | 43 | Podman for DevOps | Buildah manual; containers/image |
| Skopeo experto | 44 | Podman for DevOps | Skopeo manual; containers-transports; OCI Distribution |
| Storage avanzado | 45 | Podman in Action | containers/storage; OverlayFS; kernel docs |
| Networking avanzado | 46 | Podman for DevOps | Netavark; Aardvark DNS; Docker networking docs |
| Compose avanzado | 47 | The Ultimate Docker Container Book | Compose Specification; Docker Compose; Podman docs |
| Quadlet avanzado | 48 | Podman in Action | Quadlet y systemd manuales actuales |
| Supply chain security | 49 | Podman for DevOps | Sigstore/Cosign; SPDX; CycloneDX; SLSA; Syft/Trivy/Grype |
| Observabilidad | 50 | Podman for DevOps | Podman/Docker events; cgroups v2; Prometheus; OpenTelemetry |
| Operación y recuperación | 51 | Los tres libros | Documentación oficial de engines, registries y volúmenes |
| containers/* y capstone | 52 | Podman in Action | containers/image, storage, common; conmon; crun; Netavark |

### Jerarquía de autoridad unificada

1. Especificaciones normativas aplicables (OCI, Compose) para formatos y contratos.
2. Documentación oficial y páginas `man` de la **versión instalada** para comportamiento y opciones.
3. Documentación de Fedora/Red Hat para integración de plataforma.
4. Documentación técnica y código upstream para internals y detalles de implementación.
5. Los tres libros para explicaciones y progresión pedagógica.
6. Fuentes secundarias contrastadas cuando sea necesario.

Los scopes indican dónde consultar; no implican que cada fuente cubra todas las lecciones.


## 15. Docker Swarm — fuentes por scope (bloques 53–61)

| Scope | Bloques | Fuente pedagógica | Fuente técnica prioritaria |
|---|---|---|---|
| Arquitectura y cluster | 53–54 | The Ultimate Docker Container Book, cuando la edición lo cubra | Docker Docs: Swarm mode overview, How nodes work, Raft consensus |
| Servicios y scheduling | 55 | The Ultimate Docker Container Book, cuando proceda | Docker Docs: Services, docker service y docker node CLI |
| Redes overlay | 56 | Fundamentos de networking del PATH | Docker Docs: Swarm networking, overlay network driver |
| Stacks y persistencia | 57 | The Ultimate Docker Container Book, cuando proceda | Docker Docs: docker stack deploy, secrets, configs y volumes |
| Seguridad y recuperación | 58 | Fundamentos de seguridad del PATH | Docker Docs: PKI, autolock, backup and restore a swarm |
| Operación y diagnóstico | 59 | Laboratorios del PATH | Docker Engine CLI/API, daemon logs y documentación oficial |
| Automatización y capstone | 60–61 | Los tres libros como apoyo conceptual | Docker Engine API, Docker Swarm CLI, OCI y manuales de Ansible |

Documentación principal: https://docs.docker.com/engine/swarm/ y https://docs.docker.com/reference/cli/docker/ . La cobertura de Swarm en cada libro no se presupone: para comportamiento actual y opciones concretas prevalece la documentación oficial.


## 16. Enlaces de referencia y reglas de aplicación

- [Podman: manuales oficiales](https://docs.podman.io/)
- [Buildah: código y manuales upstream](https://github.com/containers/buildah)
- [Skopeo: código y manuales upstream](https://github.com/containers/skopeo)
- [OCI: especificaciones](https://opencontainers.org/)
- [Docker Engine en Fedora](https://docs.docker.com/engine/install/fedora/)
- [Docker rootless](https://docs.docker.com/engine/security/rootless/)
- [Stacks en Swarm](https://docs.docker.com/engine/swarm/stack-deploy/)
- [Docker Swarm](https://docs.docker.com/engine/swarm/)
- [Compose Specification](https://compose-spec.io/)
- [Docker, edición de referencia de Packt](https://www.packtpub.com/en-us/product/the-ultimate-docker-container-book-9781804613986)
- [Podman for DevOps, segunda edición](https://www.packtpub.com/en-us/product/podman-for-devops-9781835886625)

Aplicar las especificaciones al contrato que realmente corresponda. En
particular, stack deploy utiliza el formato heredado Compose v3; contrastar sus
campos con Docker Docs en lugar de extrapolar toda la Compose Specification.

Para Docker rootless, usar la guía específica y distinguirlo de userns-remap.
Para instalación Fedora, documentar la alternativa elegida (Docker CE o Moby),
el repositorio y las versiones. Los enlaces son puntos de entrada: cada lección
debe identificar la versión aplicable y no trasladar comandos obsoletos de libros.

Los proyectos 39, 52 y 61 comparten contrato y acumulan capacidades. Las fuentes
del proyecto final incluyen las del diagnóstico local y la documentación
CLI/API de Swarm; cualquier afirmación de salud debe indicar evidencias y límites
de acceso. La jerarquía unificada de la sección 14 prevalece sobre resúmenes
anteriores cuando puedan interpretarse de forma diferente.
