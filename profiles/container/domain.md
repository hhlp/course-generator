# DOMAIN — CONTENEDORES EN PROFUNDIDAD
## Podman + Docker + Buildah + Skopeo

## 1. Propósito

Este dominio define el alcance conceptual y técnico del PATH **CONTENEDORES EN
PROFUNDIDAD — PODMAN + DOCKER + BUILDAH + SKOPEO**.

El objetivo no es enseñar cuatro CLIs independientes. El curso debe construir
un único modelo mental del ecosistema de contenedores Linux y, sobre ese modelo,
explicar qué responsabilidad tiene cada herramienta.

El alumno debe terminar siendo capaz de:

- comprender cómo Linux implementa el aislamiento de contenedores;
- comprender OCI y la interoperabilidad entre herramientas;
- ejecutar y administrar contenedores con Podman y Docker;
- construir imágenes con Podman, Docker y Buildah;
- inspeccionar, copiar y sincronizar imágenes con Skopeo;
- administrar imágenes, registries, storage, volumes y networking;
- utilizar contenedores rootless correctamente;
- integrar Podman con systemd y Quadlet;
- diagnosticar problemas de runtime, red, almacenamiento, permisos, SELinux,
  registries e imágenes;
- comprender qué ocurre internamente por debajo de las CLIs;
- relacionar el stack local con Kubernetes sin convertir este PATH en un curso
  de Kubernetes.

## 2. Modelo central del dominio

El curso debe mantener permanentemente esta relación conceptual:

```text
                         OCI
                          │
             ┌────────────┴────────────┐
             │                         │
          IMÁGENES                 CONTENEDORES
             │                         │
      ┌──────┼──────┐             ┌────┴─────┐
      │      │      │             │          │
   Buildah Skopeo Registry      Podman     Docker
```

Una imagen OCI no pertenece conceptualmente a Podman o a Docker. Las
herramientas pueden producir, transportar, almacenar o ejecutar artefactos
compatibles siempre que respeten los formatos y protocolos correspondientes.

## 3. Fundamentos Linux obligatorios

El dominio incluye los mecanismos Linux que hacen posible un contenedor:

- procesos;
- PID 1;
- señales;
- namespaces;
- PID namespace;
- mount namespace;
- network namespace;
- user namespace;
- IPC namespace;
- UTS namespace;
- cgroup namespace;
- cgroups v2;
- límites de CPU, memoria, PIDs e I/O;
- capabilities;
- seccomp;
- filesystem;
- mounts;
- OverlayFS;
- copy-on-write;
- UID/GID;
- subuid/subgid;
- SELinux.

El curso no debe ocultar estos mecanismos detrás de la CLI.

## 4. OCI

OCI es parte estructural del dominio.

Debe cubrirse:

- Open Container Initiative;
- OCI Image Specification;
- OCI Runtime Specification;
- OCI Distribution Specification;
- image manifest;
- image index;
- image configuration;
- layers;
- blobs;
- media types;
- annotations;
- digests;
- OCI Image Layout;
- OCI archives;
- multi-platform y multi-architecture.

Se debe explicar claramente qué problemas resuelve cada especificación.

## 5. Podman

Podman es uno de los motores principales del PATH y la herramienta preferente
para los laboratorios centrados en Fedora.

Debe cubrirse:

- arquitectura daemonless;
- rootful;
- rootless;
- lifecycle de contenedores;
- imágenes;
- pods;
- volumes;
- networking;
- registries;
- inspect;
- logs;
- events;
- stats;
- exec;
- cp;
- save/load;
- export/import;
- build;
- manifests;
- secrets;
- healthchecks;
- APIs;
- podman system service;
- compatibilidad con Docker API;
- systemd;
- Quadlet;
- integración con SELinux;
- troubleshooting.

## 6. Docker

Docker debe enseñarse con profundidad suficiente para administrar y
diagnosticar entornos reales, no únicamente para traducir comandos de Podman.

Debe cubrirse:

- Docker CLI;
- Docker Engine;
- dockerd;
- Docker API;
- containerd;
- runc;
- lifecycle;
- imágenes;
- volumes;
- networks;
- Dockerfile;
- build;
- Docker Compose;
- daemon.json;
- Docker socket;
- storage drivers;
- logging;
- registries;
- troubleshooting.

La comparación Podman/Docker debe indicar similitudes y diferencias reales.

## 7. Buildah

Buildah debe tratarse como componente de primera clase.

Responsabilidades principales:

- construcción de imágenes;
- working containers;
- construcción con Containerfile/Dockerfile;
- construcción scriptable sin Containerfile;
- mount de rootfs;
- modificación directa;
- commit;
- configuración de metadata;
- rootless builds;
- manifests;
- imágenes multi-arquitectura;
- push;
- interoperabilidad OCI.

Debe mostrarse la relación entre Buildah y Podman sin presentarlos como
sinónimos.

## 8. Skopeo

Skopeo debe tratarse como componente de primera clase.

Debe cubrirse:

- inspección remota de imágenes;
- manifests;
- config;
- raw manifests;
- tags;
- copia de imágenes;
- sincronización;
- eliminación cuando el transport lo permita;
- autenticación;
- TLS;
- signatures/policy;
- multi-arch;
- air-gapped workflows;
- migración entre registries.

Transports relevantes:

- docker://
- containers-storage:
- oci:
- dir:
- docker-archive:
- oci-archive:

Debe quedar claro que Skopeo trabaja con imágenes sin necesidad de ejecutar un
contenedor.

## 9. Stack containers/*

El PATH debe profundizar en el ecosistema compartido por las herramientas de
containers:

- containers/image;
- containers/storage;
- containers/common;
- conmon;
- crun;
- runc;
- Netavark;
- Aardvark DNS.

Debe enseñarse cuándo cada componente aparece en el flujo real.

## 10. Imágenes

Deben cubrirse en profundidad:

- layers;
- blobs;
- manifests;
- config;
- history;
- tags;
- digests;
- image IDs;
- metadata;
- labels;
- build cache;
- multi-stage builds;
- minimal images;
- scratch;
- reproducibilidad;
- SBOM;
- provenance;
- firmas;
- multi-architecture.

Regla conceptual obligatoria:

**tag != identidad inmutable**

Los digests deben utilizarse para enseñar identidad de contenido.

## 11. Registries

Debe cubrirse:

- registry;
- repository;
- namespace;
- tag;
- digest;
- pull;
- push;
- login/logout;
- auth files;
- TLS;
- certificados;
- mirrors;
- short-name resolution;
- fully qualified image names;
- registry policies;
- private registries;
- copia registry-to-registry.

Quay y Docker Hub pueden utilizarse como ejemplos, sin convertir el curso en
formación específica de un proveedor.

## 12. Storage

Debe incluir:

- containers/storage;
- graphroot;
- runroot;
- OverlayFS;
- writable layer;
- copy-on-write;
- volumes;
- named volumes;
- bind mounts;
- tmpfs;
- ownership;
- UID/GID mappings;
- rootful/rootless storage;
- SELinux :z y :Z;
- Docker storage;
- Podman storage;
- diagnóstico de espacio y mounts.

## 13. Networking

Debe incluir:

- network namespaces;
- veth;
- bridge;
- NAT;
- port forwarding;
- DNS;
- host networking;
- rootless networking;
- Netavark;
- Aardvark DNS;
- Docker networking;
- Podman networking;
- IPv4;
- IPv6;
- firewalld;
- nftables.

El alumno debe poder seguir conceptualmente un paquete desde el host hasta el
contenedor y viceversa.

## 14. Rootless

Rootless es un tema central, especialmente con Podman.

Debe cubrirse:

- user namespaces;
- UID/GID mappings;
- /etc/subuid;
- /etc/subgid;
- newuidmap/newgidmap;
- storage rootless;
- networking rootless;
- puertos;
- mounts;
- capabilities;
- SELinux;
- límites y diferencias con rootful.

## 15. Seguridad

Debe tratarse como parte transversal del PATH:

- principio de mínimo privilegio;
- rootless;
- capabilities;
- seccomp;
- SELinux;
- read-only rootfs;
- no-new-privileges;
- secrets;
- privileged;
- devices;
- image provenance;
- signatures;
- digest pinning;
- SBOM;
- supply-chain security.

No se debe recomendar deshabilitar SELinux como solución normal.

## 16. systemd y Quadlet

Fedora hace especialmente importante esta integración.

Debe cubrirse:

- unidades systemd;
- servicios de usuario;
- lingering;
- dependencias;
- restart policies;
- journal;
- Quadlet;
- .container;
- .volume;
- .network;
- .pod;
- rootless + systemd.

Quadlet debe ser el enfoque moderno principal para integración Podman/systemd.

## 17. Build files

El dominio incluye:

- Containerfile;
- Dockerfile;
- FROM;
- RUN;
- COPY;
- ADD;
- ARG;
- ENV;
- WORKDIR;
- USER;
- CMD;
- ENTRYPOINT;
- EXPOSE;
- VOLUME;
- LABEL;
- HEALTHCHECK;
- build contexts;
- ignore files;
- multi-stage;
- cache;
- secrets;
- platform builds.

## 18. Compose

Debe cubrirse la Compose Specification y su uso con Docker y Podman.

No se debe asumir compatibilidad perfecta entre implementaciones.

## 19. APIs y automatización

Debe incluir:

- Docker API;
- Docker socket;
- Podman API;
- podman system service;
- Docker-compatible Podman API;
- REST;
- Unix sockets;
- JSON;
- jq;
- shell scripting;
- Buildah automation;
- Skopeo automation;
- CI/CD.

## 20. Kubernetes como frontera del dominio

El curso debe explicar:

- OCI;
- CRI;
- containerd;
- CRI-O;
- runc;
- crun;
- pods;
- imágenes y registries;
- relación conceptual de Podman pods con Kubernetes;
- generación/consumo de YAML cuando proceda.

No debe desarrollar administración Kubernetes profunda. Esa materia pertenece
al PATH específico de Kubernetes.

## 21. Troubleshooting

Todo el PATH debe formar una metodología de diagnóstico.

Orden recomendado:

```text
síntoma
→ identificar capa
→ obtener evidencia
→ formular hipótesis
→ realizar prueba
→ corregir
→ verificar
```

Capas mínimas:

- CLI;
- engine;
- runtime;
- proceso;
- namespace;
- cgroup;
- storage;
- filesystem;
- mount;
- networking;
- DNS;
- registry;
- image manifest;
- UID/GID;
- capabilities;
- seccomp;
- SELinux;
- systemd.

Herramientas de diagnóstico relevantes:

- podman inspect;
- docker inspect;
- buildah inspect;
- skopeo inspect;
- ps;
- lsns;
- nsenter;
- findmnt;
- ip;
- ss;
- nft;
- systemctl;
- journalctl;
- ausearch;
- jq.

## 22. Relación con otros PATH del proyecto

Este PATH debe reutilizar y conectar conocimientos con:

- Linux/Fedora;
- systemd;
- SELinux;
- firewalld;
- networking;
- Bash/Zsh;
- RPM;
- Git;
- CI/CD;
- Kubernetes.

No debe duplicar innecesariamente esos cursos, pero sí aplicar sus conceptos al
mundo de los contenedores.

## 23. Resultado final esperado

Al terminar, el alumno no debe limitarse a saber:

```bash
podman run ...
docker run ...
```

Debe poder responder preguntas como:

- ¿qué proceso real existe en el host?;
- ¿qué namespaces utiliza?;
- ¿en qué cgroup está?;
- ¿qué runtime lo creó?;
- ¿qué UID tiene dentro y fuera?;
- ¿qué mounts utiliza?;
- ¿qué labels SELinux tiene?;
- ¿cómo llega un paquete de red al contenedor?;
- ¿qué layer introdujo un archivo?;
- ¿qué manifest y digest se descargaron?;
- ¿cómo copiar esa imagen sin ejecutarla?;
- ¿cómo reconstruirla sin Docker?;
- ¿por qué funciona en Docker y falla en Podman?;
- ¿cómo convertirla en un servicio systemd?;
- ¿cómo diagnosticar todo el flujo de forma reproducible?

Ese nivel de comprensión define el nivel **experto** de este dominio.

## 24. Ampliación experta — bloques 40–52

Los bloques 0–39 se conservan íntegros. Los laboratorios integrales de 38 y 39 son una primera implementación; el bloque 52 constituye la entrega experta del entorno local; el bloque 61 completa la entrega con Swarm, sin sustituir las prácticas anteriores.

- **Bloque 40 — Linux Container Internals y OCI Runtime:** 21 lecciones de profundización y laboratorios.
- **Bloque 41 — Podman — administración avanzada:** 21 lecciones de profundización y laboratorios.
- **Bloque 42 — Docker BuildKit y Buildx — experto:** 21 lecciones de profundización y laboratorios.
- **Bloque 43 — Buildah — workflows expertos:** 20 lecciones de profundización y laboratorios.
- **Bloque 44 — Skopeo — workflows expertos:** 21 lecciones de profundización y laboratorios.
- **Bloque 45 — Storage avanzado y persistencia:** 20 lecciones de profundización y laboratorios.
- **Bloque 46 — Networking avanzado de contenedores:** 20 lecciones de profundización y laboratorios.
- **Bloque 47 — Compose avanzado y portabilidad:** 20 lecciones de profundización y laboratorios.
- **Bloque 48 — Quadlet y systemd — avanzado:** 21 lecciones de profundización y laboratorios.
- **Bloque 49 — Seguridad de la cadena de suministro:** 22 lecciones de profundización y laboratorios.
- **Bloque 50 — Observabilidad y diagnóstico avanzado:** 21 lecciones de profundización y laboratorios.
- **Bloque 51 — Operación, mantenimiento y recuperación:** 21 lecciones de profundización y laboratorios.
- **Bloque 52 — Internals containers/* y proyecto experto integrador:** 23 lecciones de profundización y laboratorios.

### Requisitos verificables del nivel experto

- Inspeccionar namespaces, cgroups, UID/GID, mounts y procesos reales, distinguiendo runtime y engine.
- Construir, firmar, inspeccionar, copiar y ejecutar una imagen OCI, verificando digests y plataformas.
- Administrar contenedores rootless, servicios Quadlet, redes y volúmenes en Fedora sin desactivar SELinux.
- Diagnosticar problemas con evidencias reproducibles: logs, eventos, syscalls, métricas, paquetes y manifiestos.
- Ejecutar backups, restauraciones y cambios de versión con comprobación de integridad.
- Implementar `container-debugger` en modo de solo lectura, con informes JSON y pruebas.

### Límites y coordinación con otros PATH

Kubernetes, systemd, SELinux, redes, Bash, CI/CD y observabilidad se aplican a contenedores, sin repetir sus cursos generales. Las funciones opcionales y los flags dependen de versiones instaladas; cada lección debe comprobar compatibilidad con `--help`, `man` y documentación upstream.


## 25. Docker Swarm — ampliación multinodo (bloques 53–61)

Docker Swarm se incorpora como materia principal de orquestación integrada en Docker Engine, sin confundirlo con Docker Compose, Podman pods, Quadlet o Kubernetes. Cubrir arquitectura manager/worker, Raft/quorum, PKI/mTLS, servicios y tareas, scheduling, redes overlay/VXLAN, ingress y DNS, stacks, secrets/configs, volúmenes distribuidos, seguridad, observabilidad, alta disponibilidad, recuperación y automatización.

Se exigen laboratorios Fedora multinodo con verificación de puertos, firewalld, SELinux, tolerancia a fallos, actualizaciones, rollback, backups y troubleshooting basado en evidencias. Swarm no debe presentarse como equivalente funcional a Kubernetes ni como solución de almacenamiento distribuido. Las capacidades y flags se validarán contra la versión instalada de Docker Engine.

Los bloques 0–52 permanecen intactos. El bloque 61 amplía el proyecto container-debugger para diagnosticar servicios, tareas, nodos, redes y quorum, sin sustituir el proyecto original.


## 26. Progresión, instalación y límites de implementación

Los 62 bloques se mantienen. Las lecciones nuevas se añaden al final de sus
bloques; las anteriores conservan identificador y título. Los temas recurrentes
se desarrollan por resultados: fundamentos identifica y ejecuta; avanzado
configura y diagnostica; experto justifica, mide y recupera. Cada lección debe
explicitar lo que reutiliza y la capacidad nueva que aporta.

### Instalación y Docker rootless

Distinguir Docker CE del repositorio oficial y Moby distribuido por Fedora.
Inventariar paquetes, repositorios, runtimes y plugins antes de instalar;
resolver conflictos según la transacción real de DNF. No asumir que el paquete
`docker` identifica siempre la misma implementación. Comprobar si `podman-docker`
proporciona la CLI y verificar sockets, contexto y endpoint antes de operar.

Docker rootless requiere una práctica propia: mapeos subordinados,
`dockerd-rootless-setuptool.sh`, servicio systemd de usuario, linger, contexto
rootless y socket de usuario. Comparar con Podman rootless y con `userns-remap`:
en este último el daemon sigue siendo rootful. Registrar limitaciones de red,
recursos y almacenamiento de la versión instalada. El laboratorio Swarm debe
validar separadamente sus requisitos de engine, privilegios y overlay.

### Compose y Swarm stacks

`docker stack deploy` utiliza el formato heredado Compose v3; la Compose
Specification moderna no constituye una garantía de compatibilidad con stacks.
Comparar campos soportados, rechazados e ignorados y revisar los avisos del CLI.
Construir y publicar imágenes antes del despliegue del stack; verificar acceso
al registry desde todos los nodos y la identidad del contenido desplegado.

### Hitos y aceptación del proyecto

| Hito | Entrega | Evidencia mínima |
|---|---|---|
| 39 | Diagnóstico base local | Engine/contexto, JSON válido, PID, namespaces, cgroup, mounts y red |
| 52 | Diagnóstico experto local | Flujo de imagen por digest/plataforma, fallos inyectados y restauración |
| 61 | Diagnóstico final con Swarm | Nodos, servicios, tareas, redes, managers y pruebas de recuperación |

El bloque 39 debe incluir un contrato JSON versionado e informe humano;
el 52 conserva ese contrato y amplía adaptadores; el 61 añade Swarm sin romper
los resultados locales. Todos exigen evidencias sanitizadas, estados explícitos
para permisos insuficientes y documentación de reproducción. El informe no debe
exportar credenciales, variables sensibles, tokens ni contenido de secrets.

El modo de diagnóstico es de solo lectura. Los comandos correctivos se
presentan como propuestas documentadas y se ejecutan aparte en el laboratorio.
La salud y el quorum se describen según el punto de observación: distinguir
estado local, información del manager, datos obsoletos y evidencias inaccesibles.
Las pruebas de recuperación deben demostrar integridad de datos además de
arranque del servicio. El bloque 61 es la entrega final del PATH completo.
