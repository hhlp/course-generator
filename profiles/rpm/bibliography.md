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
