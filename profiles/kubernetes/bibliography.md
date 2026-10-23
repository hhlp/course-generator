# Bibliografía — Kubernetes 0 → Experto

## Principal

### Kubernetes Documentation
Kubernetes upstream documentation.

Uso:
- referencia principal durante todo el PATH
- API
- workloads
- scheduling
- networking
- storage
- security
- administration
- cluster architecture
- troubleshooting
- version-specific behavior

### Kubernetes: Up and Running
Kelsey Hightower, Brendan Burns, Joe Beda.

Uso:
- fundamentos
- modelo mental
- aplicaciones
- objetos principales
- arquitectura y operación


### kubectl Documentation and Command Reference
Kubernetes upstream documentation.

Uso:
- sintaxis y estructura de kubectl
- get, describe, explain y events
- create, apply, replace, patch, edit y delete
- rollout, scale y autoscale
- logs, exec, attach, cp, debug y port-forward
- JSONPath, custom-columns, selectors y sort-by
- kubeconfig y contexts
- auth can-i e impersonation
- cordon, uncordon, drain, taint y label
- proxy, raw API access y dry-run
- shell completion, scripting y troubleshooting

## Administración y operación

### Kubernetes: The Hard Way
Kelsey Hightower.

Uso:
- comprensión profunda de bootstrap
- PKI
- control plane
- kubelet
- networking
- componentes individuales

No debe emplearse como receta única de instalación, sino como laboratorio de comprensión arquitectónica.

### Certified Kubernetes Administrator (CKA) Study Guide
Benjamin Muschko.

Uso:
- consolidación práctica del bloque CKA
- ejercicios
- administración
- troubleshooting

### Kubernetes in Action
Marko Lukša.

Uso:
- explicación profunda de recursos
- workloads
- networking
- storage
- funcionamiento del cluster

## Desarrollo

### Certified Kubernetes Application Developer (CKAD) Study Guide
Benjamin Muschko.

Uso:
- preparación del hito CKAD
- ejercicios prácticos
- configuración
- workloads
- services
- troubleshooting de aplicaciones

### Kubernetes Patterns
Bilgin Ibryam, Roland Huß.

Uso:
- patrones de aplicaciones cloud-native
- sidecars
- configuración
- lifecycle
- controllers
- operadores
- diseño

## Seguridad

### Kubernetes Security
Liz Rice, Michael Hausenblas.

Uso:
- seguridad de clusters
- workloads
- runtime
- RBAC
- supply chain
- network security

### Hacking Kubernetes
Andrew Martin, Michael Hausenblas.

Uso:
- threat modeling
- hardening
- análisis defensivo
- comprensión de vectores de ataque para mejorar seguridad

### CIS Kubernetes Benchmark

Uso:
- baseline de hardening
- auditoría de configuración
- bloque CKS

### NSA/CISA Kubernetes Hardening Guidance

Uso:
- hardening defensivo
- aislamiento
- autenticación
- autorización
- networking
- logging

## Cloud Native y certificaciones base

### CNCF KCNA Curriculum / Exam Domains

Uso:
- verificar cobertura del hito KCNA

### CNCF KCSA Curriculum / Exam Domains

Uso:
- verificar cobertura del hito KCSA

### CNCF Cloud Native Landscape

Uso:
- comprender el ecosistema CNCF
- mapear herramientas y categorías

## Networking

### Kubernetes Networking and CNI documentation

Uso:
- networking model
- Services
- EndpointSlices
- NetworkPolicy
- CNI

### CNI Specification

Uso:
- internals de networking
- plugins
- ADD/DEL/CHECK
- IPAM

### CoreDNS Documentation

Uso:
- DNS
- Corefile
- plugins
- troubleshooting

### Gateway API Documentation

Uso:
- GatewayClass
- Gateway
- Routes
- evolución de Ingress

### Cilium Documentation

Uso:
- eBPF
- networking avanzado
- policy
- observabilidad

## Storage

### CSI Specification

Uso:
- internals de storage
- Node y Controller services
- provisioning
- attach
- mount
- snapshots
- expansion

### Kubernetes CSI Documentation

Uso:
- integración CSI con Kubernetes

## Runtime y contenedores

### OCI Specifications

Incluye:
- Image Specification
- Runtime Specification
- Distribution Specification

Uso:
- fundamentos de imágenes
- runtime
- registries

### containerd Documentation

Uso:
- runtime internals
- CRI
- snapshots
- content store
- plugins

### CRI API / Kubernetes CRI documentation

Uso:
- kubelet-runtime interaction
- pod sandbox
- lifecycle de containers

## etcd

### etcd Documentation

Uso:
- operaciones
- backup
- restore
- compaction
- defragmentation
- TLS
- clustering

### Raft Paper
Diego Ongaro, John Ousterhout.

Uso:
- consenso
- leader election
- replicación
- fundamentos de etcd

## Extensibilidad y operadores

### Kubebuilder Book

Uso:
- CRDs
- controllers
- controller-runtime
- webhooks
- operators

### Operator SDK Documentation

Uso:
- desarrollo de operadores
- patrones de reconciliación

### Programming Kubernetes
Michael Hausenblas, Stefan Schimanski.

Uso:
- API machinery
- CRDs
- controllers
- extensibilidad
- client-go

## API e internals

### Kubernetes API Concepts documentation

Uso:
- resourceVersion
- watch
- patch
- Server-Side Apply
- API groups
- versioning

### Kubernetes source code
Repositorio `kubernetes/kubernetes`.

Uso:
- tramo experto
- apiserver
- controllers
- scheduler
- kubelet
- tests
- build

### Kubernetes Enhancement Proposals

Uso:
- evolución del proyecto
- lifecycle de features
- design rationale
- feature gates

## GitOps y packaging

### Learning Helm: Managing Apps on Kubernetes
Matt Butcher, Matt Farina y Josh Dolitsky.
O’Reilly Media, 2021.

Referencia editorial: https://www.oreilly.com/library/view/learning-helm/9781492083641/

Uso:
- introducción operativa a Helm antes del hito CKA
- comprensión de charts, values y releases
- instalación, actualización, historial y rollback
- creación de charts y templates en el bloque 53

El libro explica Helm 3. Contrastar comandos, opciones, plugins y comportamiento
con la documentación oficial de la versión objetivo, especialmente al usar Helm 4.

### Helm Documentation

Uso:
- charts
- templates
- dependencies
- lifecycle de releases

### Kustomize Documentation

Uso:
- bases
- overlays
- patching
- configuración por entorno

### Argo CD Documentation

Uso:
- GitOps
- synchronization
- health
- progressive delivery

### Flux Documentation

Uso:
- GitOps
- reconciliation
- source controllers
- automation

## Policy as Code

### Open Policy Agent Documentation

Uso:
- políticas
- Rego
- integración con Kubernetes

### Gatekeeper Documentation

Uso:
- admission policy
- constraints
- templates

### Kyverno Documentation

Uso:
- validation
- mutation
- generation
- image verification

### CEL / Kubernetes ValidatingAdmissionPolicy Documentation

Uso:
- políticas nativas
- validación declarativa

## Observabilidad

### Prometheus Documentation

Uso:
- métricas Kubernetes
- scraping
- alerting

### kube-state-metrics Documentation

Uso:
- métricas de estado de objetos Kubernetes

### OpenTelemetry Documentation

Uso:
- logs
- metrics
- traces
- instrumentación y collector

### Grafana Documentation

Uso:
- dashboards y visualización

### Loki Documentation

Uso:
- logging agregado

## Supply chain

### Sigstore Documentation

Uso:
- firmas
- provenance
- cosign
- Rekor
- Fulcio

### SLSA Specification

Uso:
- supply-chain security
- provenance
- niveles de madurez

### SPDX y CycloneDX

Uso:
- SBOM

## Platform Engineering

### Material sobre Platform Engineering en Kubernetes
Categoría temática, no referencia a un libro concreto. Consultar documentación y literatura actual de CNCF y proyectos relevantes.

Uso:
- internal developer platforms
- self-service
- golden paths
- gobernanza
- developer experience

### Backstage Documentation

Uso:
- catálogo
- portal de desarrolladores
- platform engineering

### Crossplane Documentation

Uso:
- control planes de infraestructura
- compositions
- managed resources

## Multi-cluster y lifecycle

### Cluster API Book / Documentation

Uso:
- lifecycle declarativo
- Machine
- MachineDeployment
- providers
- ClusterClass

## Backup y recuperación

### Velero Documentation

Uso:
- backup
- restore
- migration
- disaster recovery

## Conformance

### CNCF Kubernetes Conformance

Uso:
- conformidad
- portabilidad
- validación de distribuciones

### Sonobuoy Documentation

Uso:
- ejecución de pruebas de conformance

## Lectura por etapas

### Fundamentos → KCNA
- Kubernetes Documentation
- Kubernetes: Up and Running
- CNCF KCNA domains
- CNCF Landscape
- OCI specifications

### Seguridad base → KCSA
- Kubernetes Security
- KCSA domains
- CIS Benchmark
- NSA/CISA guidance

### Desarrollo → CKAD
- CKAD Study Guide
- Kubernetes Patterns
- Kubernetes in Action
- Kubernetes Documentation

### Administración → CKA
- Learning Helm: Managing Apps on Kubernetes
- Helm y Kustomize: documentación oficial versionada
- CKA Study Guide
- Kubernetes: The Hard Way
- Kubernetes in Action
- etcd docs
- CNI docs
- CSI docs

### Seguridad avanzada → CKS
- Kubernetes Security
- Hacking Kubernetes
- CIS Benchmark
- Sigstore
- OPA/Gatekeeper/Kyverno
- Falco documentation

### Después de Kubestronaut
- Learning Helm: profundización en charts y templates
- Programming Kubernetes
- Kubebuilder Book
- Kubernetes source
- KEPs
- CNI specification
- CSI specification
- containerd documentation
- etcd internals
- Gateway API
- Cluster API
- GitOps tooling
- eBPF/Cilium
- Platform Engineering material

## Criterio de uso

La bibliografía no reemplaza la documentación upstream.

Cuando exista discrepancia entre un libro y el comportamiento actual de Kubernetes, prevalecen:

1. documentación upstream de la versión estudiada
2. especificación oficial correspondiente
3. KEP aprobado
4. código fuente
5. documentación del proyecto CNCF implicado

Los libros se emplean para explicación, estructura mental y práctica; las fuentes upstream determinan el comportamiento técnico vigente.

## Referencias complementarias — profundización

### Kubernetes Dynamic Resource Allocation
Documentación upstream y KEPs de DRA; estudiar ResourceClaim, controladores, drivers y estado de la API por versión.

### Kubernetes Dual-stack IPv4/IPv6
Documentación upstream de dual-stack Services y networking; contrastar soporte del CNI seleccionado.

### Kubernetes API Priority and Fairness
Documentación upstream para FlowSchema, PriorityLevelConfiguration y métricas del API server.

### Kubernetes Testing / controller-runtime envtest
Documentación de sigs.k8s.io/controller-runtime y del framework e2e de Kubernetes para pruebas de reconciliación y compatibilidad.

### Helm — documentación versionada
Consultar guías oficiales de Helm 3 y Helm 4 según la versión objetivo; verificar cambios en CLI, plugins, charts y compatibilidad.

### Kubernetes Production Best Practices y SRE
Documentación oficial de Kubernetes sobre administración, upgrades, alta disponibilidad y disaster recovery; Google SRE Workbook como referencia complementaria de SLI/SLO, alertas e incidentes.

### Kubernetes Authentication / OIDC
Documentación oficial sobre autenticación, tokens de ServiceAccount, OIDC y autorización RBAC.

## Enlaces primarios para verificación y preparación

- Kubernetes: https://kubernetes.io/docs/
- Referencia kubectl: https://kubernetes.io/docs/reference/kubectl/
- Currículos oficiales versionados: https://github.com/cncf/curriculum
- CKA: https://www.cncf.io/training/certification/cka/
- CKAD: https://www.cncf.io/training/certification/ckad/
- CKS y prerrequisito CKA: https://www.cncf.io/training/certification/cks/
- Helm: https://helm.sh/docs/
- Kustomize: https://kubectl.docs.kubernetes.io/references/kustomize/
- etcd y recuperación: https://etcd.io/docs/
- Kubebuilder: https://book.kubebuilder.io/
- Go y puente para controllers: https://go.dev/doc/
- Gateway API: https://gateway-api.sigs.k8s.io/
- CRI/containerd: https://containerd.io/docs/
- CNI: https://www.cni.dev/docs/
- CSI: https://github.com/container-storage-interface/spec

Para cada libro, registrar la edición realmente consultada antes de generar
lecciones que dependan de ella. Las entradas sin edición identifican una obra,
no presuponen una edición concreta ni garantizan actualidad técnica.
Para currículos y documentación viva, registrar fecha y revisión o versión.
