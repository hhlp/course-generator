# BIBLIOGRAPHY — RPM PACKAGING EN PROFUNDIDAD — FEDORA

## 1. RPM upstream

### RPM Documentation

Fuente técnica principal para comportamiento y capacidades de RPM.

Usar especialmente para:

- formato RPM y headers
- rpm y rpmquery
- rpmbuild y rpmspec
- SPEC
- macros
- dependencies y dependency generators
- rich dependencies
- scriptlets y triggers
- transacciones
- firmas
- internals

Prioridad: MUY ALTA.

### RPM source code

Referencia definitiva cuando sea necesario investigar detalles internos no suficientemente descritos en documentación de usuario.

Áreas especialmente útiles:

- macro engine
- package/header handling
- rpmdb
- transactions
- dependency handling
- signatures
- build subsystem

Debe emplearse selectivamente en los niveles avanzados.

## 2. Fedora Packaging Guidelines

Referencia normativa principal para paquetes destinados a Fedora.

Usar para:

- naming y versioning
- Release/Epoch
- dependencies
- file ownership
- macros
- scriptlets
- libraries y devel packages
- documentation y licenses
- filesystem layout
- packaging practices

Prioridad: MUY ALTA.

La documentación upstream de RPM explica principalmente qué puede hacer RPM; las Fedora Packaging Guidelines determinan las prácticas aceptadas o recomendadas en Fedora.

## 3. Fedora Package Maintainer Docs

Referencia principal para el workflow real del mantenedor Fedora.

Áreas:

- package lifecycle
- package review
- dist-git
- branches
- fedpkg
- builds
- updates
- mantenimiento

Prioridad: MUY ALTA.

## 4. Fedora Package Review

Usar la documentación oficial del proceso para estudiar requisitos de nuevos paquetes, review requests, SPEC/SRPM, rpmlint, builds de prueba y cumplimiento de las Packaging Guidelines.

## 5. dist-git y fedpkg

Usar documentación oficial de Fedora para repositories, branches, SPEC, sources, patches, fedpkg y workflow de builds. Relacionar siempre esta capa con Koji y Bodhi.

## 6. Mock

La documentación oficial de Mock es la referencia principal para:

- buildroots
- configuraciones
- builds de SRPM
- entornos limpios
- instalación de BuildRequires
- reproducibilidad
- debugging

Debe utilizarse para demostrar por qué un paquete necesita construirse correctamente fuera del entorno del desarrollador.

## 7. rpmlint

Usar documentación oficial de rpmlint para análisis de SPEC y RPM, checks, warnings y errors. Interpretar los diagnósticos junto con las Fedora Packaging Guidelines.

## 8. COPR

La documentación de Fedora COPR se utilizará para projects, builds, chroots, repositories, SRPM, resultados de build y pruebas de paquetes.

Debe explicarse la diferencia entre COPR y Koji.

## 9. Koji

La documentación oficial de Koji será la referencia principal para:

- builds
- tasks
- tags
- targets
- buildroots
- packages
- NVR
- inheritance
- builders

En los bloques avanzados podrá complementarse con el código fuente.

## 10. Bodhi

Usar documentación oficial de Bodhi para:

- updates
- builds
- testing
- stable updates
- update lifecycle
- integración con Koji

## 11. DNF y libdnf5

Usar documentación oficial de DNF/libdnf5 para comprender la capa superior a RPM:

- repositorios
- metadata
- selección de paquetes
- dependency resolution
- transactions

Debe evitarse atribuir a RPM operaciones realizadas por DNF, libdnf5 o libsolv.

## 12. libsolv

Usar documentación y código fuente de libsolv para los bloques avanzados sobre:

- Pool
- Repo
- Solvable
- Reldep
- jobs
- dependency rules
- SAT
- UNSAT
- solution selection

Prioridad: ALTA en los bloques dedicados al solver.

## 13. createrepo_c

Referencia para repository metadata, repodata, creación y regeneración de repositorios.

Debe utilizarse directamente en laboratorios de repositorios RPM.

## 14. Documentación general de Fedora

Utilizar como referencia para integración del packaging con Fedora, especialmente DNF, repositorios, package management, claves, seguridad e infraestructura.

## 15. Manual pages

Las páginas man instaladas en Fedora son fuentes primarias de consulta.

Especialmente:

- `man rpm`
- `man rpmbuild`
- `man rpmspec`

Además deben utilizarse `--help`, `rpm --eval` y `rpm --showrc` para investigar el comportamiento real de las herramientas instaladas.

## 16. Inspección práctica del sistema

El propio Fedora constituye una fuente experimental.

Usar, entre otros:

- `rpm -q`
- `rpm -qi`
- `rpm -ql`
- `rpm -qf`
- `rpm --requires`
- `rpm --provides`
- `rpm --scripts`
- `rpm --triggers`
- `rpm -V`
- `rpm --eval`
- `rpm --showrc`

Los resultados deben correlacionarse con la documentación.

## 17. SPEC reales de Fedora

Los SPEC mantenidos por Fedora son ejemplos esenciales para estudiar macros, subpackages, BuildRequires, Sources, Patches, fases de build, `%files` y patrones reales.

No sustituyen las Packaging Guidelines: un paquete existente puede contener decisiones históricas, excepciones o deuda técnica.

## 18. Código fuente de componentes relacionados

Para internals pueden consultarse selectivamente:

- RPM
- libsolv
- libdnf5
- DNF
- Mock
- Koji
- Bodhi
- createrepo_c

El objetivo es comprender arquitectura y comportamiento, no transformar todo el PATH en un curso de desarrollo de estas herramientas.

## 19. Jerarquía de fuentes

Para comportamiento de RPM:

1. RPM upstream documentation.
2. Manual pages de la versión instalada.
3. Código fuente RPM.
4. Experimentación controlada.

Para política de Fedora Packaging:

1. Fedora Packaging Guidelines.
2. Fedora Package Maintainer documentation.
3. Documentación de Fedora Infrastructure.
4. Paquetes y SPEC reales de Fedora.

Para resolución de dependencias:

1. libsolv documentation.
2. libsolv source code.
3. libdnf5/DNF documentation.
4. Experimentación con repositorios reales.

Para infraestructura:

1. Documentación oficial del proyecto correspondiente.
2. Documentación Fedora.
3. Código fuente cuando sea necesario profundizar.

## 20. Fuentes históricas y prácticas obsoletas

RPM posee una historia extensa y numerosos SPEC públicos contienen técnicas antiguas.

Deben reconocerse y marcarse explícitamente cuando aparezcan, incluyendo ejemplos como el tag histórico `BuildRoot:`, construcciones SPEC antiguas, macros reemplazadas por alternativas modernas y scriptlets evitables mediante mecanismos actuales.

Comprender una práctica histórica no implica recomendarla.

## 21. Política bibliográfica

No generar una lección importante basándose ciegamente en una única fuente.

Cuando exista conflicto entre documentación genérica antigua y las prácticas actuales de Fedora, dar prioridad a la documentación actual de Fedora para política de packaging.

Para comportamiento interno de RPM, priorizar RPM upstream.

Combinar documentación con experimentación real en Fedora.

Objetivo:

precisión técnica + prácticas actuales + profundidad + comprensión interna + experiencia práctica.


## 22. Referencias adicionales organizadas por scope

| Scope | Referencias prioritarias | Uso |
|---|---|---|
| RPM formato e internals (0, 2, 3) | RPM upstream docs, código RPM, man rpm | Cabeceras, rpmdb, transacciones, firma |
| SPEC y macros (1) | RPM upstream manual, Fedora Packaging Guidelines | BuildRequires dinámicos, macros y subpackages |
| DNF5 y repositorios (4) | DNF5/libdnf5 docs, createrepo_c, libsolv | Repositorios, políticas, SAT/UNSAT |
| Integración Fedora (5) | Fedora Packaging Guidelines, systemd packaging docs, SELinux docs | Servicios, bibliotecas, seguridad |
| Calidad y seguridad (6) | Fedora Packaging Guidelines, reproducible-builds.org, SPDX specification | Reproducibilidad, licencias, SBOM |
| Workflow (7) | Fedora Package Maintainer docs, Packit docs, COPR, Koji, Bodhi | CI/CD, builds y publicación |
| Diagnóstico (8) | Mock docs, rpmlint, rpminspect, libsolv docs | Análisis de errores y logs |
| Proyecto final (9) | Todas las fuentes anteriores y SPEC reales de Fedora | Validación de extremo a extremo |

### Referencias complementarias por ecosistema

- Fedora Python Packaging Guidelines y macros pyproject: paquetes Python.
- Fedora Rust Packaging Guidelines y herramientas Cargo: paquetes Rust.
- Fedora Go Packaging Guidelines: paquetes Go.
- Fedora C/C++ Packaging Guidelines y políticas de bibliotecas: ELF, ABI, SONAME y subpackages devel.
- Fedora systemd Packaging Guidelines y documentación systemd: servicios, presets, tmpfiles y sysusers.
- Documentación oficial de Packit: integración CI y COPR.
- Documentación oficial de SPDX: expresión de licencias y metadatos.

**Nota de vigencia:** las opciones, macros y políticas cambian entre versiones. Consultar documentación correspondiente a la versión de Fedora y RPM usada en cada laboratorio.


## 23. Enlaces oficiales y correspondencia con el PATH

Este índice concreta las fuentes citadas en las secciones anteriores.
Seleccionar la rama documental correspondiente a la versión del laboratorio;
una documentación de RPM 6 no demuestra disponibilidad en RPM 4.

| Bloques | Fuente oficial | Secciones o uso |
|---|---|---|
| 0–3 | [RPM Documentation](https://rpm.org/documentation.html) | Elegir versión; formato, macros, dependencias y transacciones |
| 1–2 | [RPM SPEC, rama 4.20](https://rpm.org/docs/4.20.x/manual/spec.html) | Tags, fases, intérpretes, %files y scriptlets; referencia versionada |
| 0–3 | [Manuales RPM, rama 6.0](https://rpm.org/docs/6.0.x/man/) | Consultas, rpmkeys, rpmsign, rpmlua y extracción; contrastar versión |
| 2–3 | [rpmdeps](https://rpm.org/docs/6.0.x/man/rpmdeps.1) | Generación de dependencias a partir de archivos; ubicación y límites |
| 3 | [rpmgraph](https://rpm.org/docs/6.0.x/man/rpmgraph.1) | Grafo de ordenación en DOT; alcance distinto de un solver de repositorios |
| 1, 5–7 | [Fedora Packaging Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/) | SPEC, configuración, ownership y política Fedora |
| 2, 5 | [Fedora Scriptlets](https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/) | Scriptlets, macros y mecanismos de integración |
| 1, 7 | [rpmautospec](https://docs.pagure.org/fedora-infra.rpmautospec/) | %autorelease, %autochangelog y relación con Git |
| 1, 6–8 | [Mock](https://rpm-software-management.github.io/mock/) | Configuración, chroots, logs, aislamiento y límites |
| 2, 4, 8–9 | [libsolv upstream](https://github.com/openSUSE/libsolv) | doc/, examples/ y test/: API C, testsolv, reglas y transacciones |
| 4, 8 | [DNF5](https://dnf5.readthedocs.io/en/stable/) | CLI, configuración y diferencias frente a DNF4 |
| 4, 8 | [Historial DNF5](https://dnf5.readthedocs.io/en/stable/commands/history.8.html) | Operaciones disponibles y semántica del historial |
| 4 | [libdnf5](https://dnf5.readthedocs.io/en/stable/) | API, repositorios, consultas y resolución; secciones Library y Tutorials |
| 4 | [createrepo_c](https://github.com/rpm-software-management/createrepo_c) | repodata, compresión y actualización de metadata |
| 6, 8 | [rpmlint](https://github.com/rpm-software-management/rpmlint) | Diagnósticos, configuración y checks |
| 6, 8 | [rpminspect](https://github.com/rpminspect/rpminspect) | Inspección y comparación de builds |
| 6 | [Reproducible Builds](https://reproducible-builds.org/docs/) | Entradas, SOURCE_DATE_EPOCH y causas de no determinismo |
| 6 | [SPDX Specifications](https://spdx.dev/use/specifications/) | Expresiones de licencia y SBOM; seleccionar versión |
| 7 | [Fedora Package Maintainers](https://docs.fedoraproject.org/en-US/package-maintainers/) | fedpkg, dist-git, revisión y mantenimiento |
| 7 | [Proceso para nuevos contribuidores](https://docs.fedoraproject.org/en-US/package-maintainers/New_Package_Process_for_New_Contributors/) | Acceso, review y requisitos del itinerario oficial |
| 7 | [COPR](https://docs.pagure.org/copr.copr/) | Proyectos, builds, chroots y repositorios propios |
| 7 | [Koji](https://docs.pagure.org/koji/) | Tags, targets, tareas, builds y logs |
| 7 | [Bodhi](https://bodhi.readthedocs.io/en/stable/) | Ciclo de actualizaciones e interacción con Koji |
| 7 | [Packit](https://packit.dev/docs/) | Configuración, trabajos y automatización de pruebas/builds |

### Fuentes para las lagunas cubiertas en esta revisión

- 1.86–1.89: manual SPEC de RPM y Guidelines de Fedora para %ghost,
  %verify, restricciones de arquitectura y dependencias ISA.
- 1.90–1.92 y 6.16: documentación RPM de archivos de configuración y
  Guidelines Fedora; confirmar con la matriz de pruebas del laboratorio.
- 1.93–1.95 y 7.15: documentación rpmautospec; inspeccionar el SRPM generado.
- 1.96–1.97: manual SPEC, macros RPM y Scriptlets Fedora para intérpretes y
  momentos de expansión.
- 2.113 y S1–S5: documentación y ejemplos de la API C de libsolv;
  comprobar firmas y disponibilidad contra la versión instalada.
- 6.15: documentación Mock y Reproducible Builds; no inferir reproducibilidad
  únicamente porque el build se ejecuta dentro de un chroot.

### Registro de consulta y límites

Revisión: 2026-10-21. Se contrastaron específicamente el manual SPEC RPM,
los manuales upstream rpmdeps/rpmgraph, la documentación Mock y las
referencias de Fedora sobre rpmautospec. El sitio Fedora Docs devolvió una
barrera de acceso automatizado en la comprobación directa de Guidelines y
Scriptlets; se conservan sus URL canónicas, sin afirmar una verificación
completa de cada política actual. El resto de enlaces es un índice de
referencias oficiales para consultar por versión, no una certificación de
que todos sus contenidos se hayan auditado en esta revisión.
