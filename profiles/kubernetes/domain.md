# Domain — Kubernetes 0 → Experto

## Propósito

Este dominio define un itinerario completo para aprender Kubernetes desde cero hasta un nivel experto de ingeniería, operación, seguridad, extensibilidad e internals.

El PATH incorpora como hitos explícitos las cinco credenciales principales del programa Kubestronaut:

- KCNA — Kubernetes and Cloud Native Associate
- KCSA — Kubernetes and Cloud Security Associate
- CKAD — Certified Kubernetes Application Developer
- CKA — Certified Kubernetes Administrator
- CKS — Certified Kubernetes Security Specialist
- Kubestronaut — hito alcanzado al obtener y mantener las cinco credenciales requeridas por el programa

Las certificaciones son hitos de validación, no el límite del contenido. Después del hito Kubestronaut, el PATH continúa hacia Kubernetes avanzado, producción, arquitectura, internals, platform engineering y operación de clusters complejos.

## Alcance

El dominio cubre:

- Linux necesario para comprender Kubernetes.
- Contenedores, OCI, containerd, runc y CRI.
- Fundamentos cloud-native y ecosistema CNCF.
- Arquitectura Kubernetes.
- kubectl CLI de básico a avanzado, incluyendo consulta, creación, gestión declarativa, rollout, debugging, RBAC, kubeconfig, administración de nodos, API, JSONPath, selectors, scripting y troubleshooting.
- Workloads.
- Scheduling.
- Configuración y Secrets.
- Networking.
- Storage.
- Observabilidad.
- Seguridad.
- Instalación y administración.
- kubeadm.
- etcd.
- kubelet.
- kube-apiserver.
- kube-scheduler.
- kube-controller-manager.
- kube-proxy.
- CoreDNS.
- CNI.
- CSI.
- Gateway API.
- RBAC.
- Pod Security Standards.
- NetworkPolicy.
- Admission control.
- Supply-chain security.
- Runtime security.
- Troubleshooting.
- High availability.
- Disaster recovery.
- Upgrades.
- Autoscaling.
- Performance.
- Multi-tenancy.
- Multi-cluster.
- Cluster API.
- GitOps.
- Helm.
- Kustomize.
- Operators.
- CRDs.
- Controllers.
- Service mesh.
- Policy as Code.
- Workload identity.
- Secrets management.
- Platform Engineering.
- Crossplane.
- FinOps.
- eBPF.
- Kubernetes internals.
- Kubernetes source code.
- KEPs.
- Conformance.
- Arquitectura empresarial.
- Proyecto final experto.

## Enfoque pedagógico

Cada lección debe comenzar obligatoriamente con:

## 🎯 OBJETIVO

El desarrollo debe ser completo, progresivo, técnico y didáctico. No debe limitarse a una definición breve o un resumen superficial.

Cuando aporten valor deben incluirse:

- 🧪 Laboratorio / ejemplos
- ⚠️ Errores frecuentes
- 💡 Idea importante

Cada lección debe terminar obligatoriamente con:

## 🧠 QUÉ DEBES RECORDAR

La sección final debe condensar entre 3 y 7 ideas clave de la lección. No debe repetir literalmente el objetivo.

## Filosofía del PATH

El PATH sigue una progresión:

fundamentos → cloud native → Kubernetes básico → seguridad básica → KCNA → KCSA → desarrollo → CKAD → administración → CKA → seguridad avanzada → CKS → Kubestronaut → Kubernetes avanzado → producción → internals → arquitectura experta.

Las certificaciones se utilizan como checkpoints. El contenido no debe deformarse para limitarse exclusivamente al blueprint de examen.

## Profundidad esperada

### Nivel inicial

El alumno debe entender conceptos y poder ejecutar operaciones básicas con seguridad.

### Nivel intermedio

El alumno debe administrar aplicaciones y clusters, comprender dependencias entre componentes y solucionar fallos comunes.

### Nivel avanzado

El alumno debe diseñar, asegurar, escalar, actualizar, observar y recuperar clusters de producción.

### Nivel experto

El alumno debe comprender internals, APIs, controllers, scheduler, kubelet, runtimes, CNI, CSI, etcd, código fuente, trade-offs arquitectónicos y diseño de plataformas.

## Entorno principal

Se prioriza Linux como sistema anfitrión.

Los ejemplos pueden usar:

- kubeadm
- kind
- minikube
- k3d cuando resulte útil para laboratorios
- clusters gestionados únicamente cuando sirvan para explicar conceptos portables

No se debe convertir el PATH en formación específica de un único proveedor cloud.

## Kubernetes upstream primero

La documentación upstream y las especificaciones oficiales son la fuente técnica principal.

Cuando una capacidad dependa de versión, estado alpha/beta/stable, feature gate o implementación concreta, la lección debe indicarlo explícitamente.

## Certificaciones

### KCNA

Debe quedar cubierto el conocimiento fundamental de Kubernetes, cloud native, contenedores, networking, storage, observabilidad y ecosistema CNCF.

### KCSA

Debe quedar cubierta la seguridad base de cloud native, contenedores y Kubernetes.

### CKAD

Debe quedar cubierta la creación, configuración, exposición, observación y troubleshooting de aplicaciones sobre Kubernetes.

### CKA

Debe quedar cubierta la instalación, operación, networking, storage, mantenimiento y troubleshooting de clusters.

### CKS

Debe quedar cubierta la seguridad avanzada de cluster, workloads, supply chain y runtime.

CKS requiere mantener un CKA válido para obtener la certificación.

### Kubestronaut

Se trata como hito de competencias certificadas, no como punto final del itinerario.

## Laboratorios

Los laboratorios deben favorecer el aprendizaje práctico.

Siempre que sea razonable deben incluir:

- manifests YAML
- kubectl y su CLI de básico a avanzado
- inspección directa de recursos
- logs
- events
- troubleshooting
- herramientas Linux
- crictl
- containerd
- tcpdump
- ss
- ip
- nft
- conntrack
- nsenter
- etcdctl

Los laboratorios avanzados deben incluir fallos deliberados y recuperación.

## Seguridad

El contenido de seguridad debe enseñar defensa y administración legítima:

- hardening
- least privilege
- RBAC
- Pod Security
- NetworkPolicy
- admission
- supply chain
- runtime security
- audit
- incident response
- forensics defensivo

## Observabilidad

El PATH debe enseñar los conceptos fundamentales y la integración de Kubernetes con:

- Prometheus
- Grafana
- Loki
- OpenTelemetry
- logs
- metrics
- traces
- events

Los productos de observabilidad pueden tener PATHs independientes; aquí se estudian desde la perspectiva de Kubernetes.

## Networking

Se debe pasar de la abstracción Kubernetes al dataplane real:

Service → EndpointSlice → kube-proxy o dataplane equivalente → Linux networking → CNI → routing/overlay/eBPF.

## Storage

Se debe pasar de PVC y StorageClass hasta CSI, provisioning, attach, mount, snapshots, topology y troubleshooting.

## Internals

El tramo experto debe explicar cómo funciona Kubernetes internamente.

Debe incluir:

- request lifecycle
- apiserver
- API machinery
- etcd
- controllers
- informers
- workqueues
- scheduler
- kubelet
- CRI
- container runtime
- CNI
- CSI
- source code
- KEPs

## Proyecto final

El proyecto final debe exigir diseñar y operar una plataforma Kubernetes completa.

Debe integrar:

- HA
- networking
- storage
- security
- identity
- policy
- GitOps
- observability
- backup
- DR
- upgrades
- autoscaling
- multi-tenancy
- troubleshooting
- documentación
- decisiones arquitectónicas y trade-offs

## Resultado esperado

Al finalizar el PATH el alumno debe estar preparado no solo para afrontar KCNA, KCSA, CKAD, CKA y CKS, sino también para operar Kubernetes en producción, diseñar plataformas internas, comprender los componentes internos y continuar hacia contribución upstream o arquitectura especializada.
