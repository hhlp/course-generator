# RPM PACKAGING EN PROFUNDIDAD — FEDORA

## Dominio

Este PATH estudia RPM desde sus fundamentos hasta el nivel necesario para comprender, construir, analizar, depurar y mantener paquetes dentro del ecosistema Fedora.

RPM no debe estudiarse únicamente como el comando `rpm`. El dominio completo relaciona:

RPM package format → RPM metadata → rpmdb → SPEC → rpmbuild → SRPM → dependencias → transacciones → repositorios → DNF/libdnf5 → libsolv → Mock → Fedora Packaging → COPR → dist-git → Koji → Bodhi.

El objetivo final es comprender el flujo completo:

upstream → source archive → SPEC → SRPM → build reproducible → RPM → validación → review → build infrastructure → actualización → repositorio → instalación.

## 1. Plataforma

La plataforma principal es Fedora Linux. Cuando resulte útil podrán establecerse relaciones con RHEL, CentOS Stream y otras distribuciones basadas en RPM. Las prácticas específicas de Fedora deben distinguirse de las capacidades proporcionadas por RPM upstream.

## 2. Formato RPM, NEVRA y EVR

Debe estudiarse metadata, headers, payload, scripts, dependencias, Provides, metadata de archivos, firmas, checksums, ownership, permisos y configuración.

Se estudiarán Name, Epoch, Version, Release y Architecture, las representaciones NEVRA/NEVR y el modelo EVR. Debe comprenderse la comparación de versiones, incluido el significado de mecanismos como `~` y `^` cuando sean aplicables.

## 3. Herramientas RPM

El PATH cubre `rpm`, `rpmquery`, `rpmverify`, `rpmkeys`, `rpmdb`, `rpm2cpio`, `rpmbuild` y `rpmspec`, además de herramientas relacionadas del ecosistema Fedora.

El alumno debe investigar tanto paquetes instalados como RPM no instalados.

## 4. Consultas y queryformat

Deben estudiarse `rpm -q`, `-qi`, `-ql`, `-qc`, `-qd`, `-qf`, `-qp`, `--requires`, `--provides`, `--whatrequires`, `--whatprovides`, `--scripts`, `--triggers` y `--changelog`, además de queryformat.

No debe limitarse la enseñanza a memorizar opciones: debe explicarse de qué metadata proviene la información y cómo consultarla de forma programática.

## 5. Verificación

Debe estudiarse `rpm -V` y los indicadores S, M, 5, D, L, U, G, T y P, explicando qué metadata se compara y cómo interpretar cada discrepancia.

## 6. rpmdb

Debe estudiarse propósito, contenido, consultas, consistencia, mantenimiento, reconstrucción, corrupción y troubleshooting de rpmdb, distinguiéndola de la metadata de repositorios gestionada por DNF.

## 7. SPEC

Los SPEC son uno de los ejes principales. Deben estudiarse tags como Name, Version, Release, Summary, License, URL, Source, Patch, BuildRequires y Requires, y las secciones `%description`, `%prep`, `%build`, `%install`, `%check`, `%files` y `%changelog`.

También se estudiarán `%package`, `%description` y `%files` para subpackages.

## 8. Sources, Patches y preparación

Debe comprenderse el flujo upstream → source archive → Source → preparación → patches → build. Se estudiarán Source0, Patch, `%setup`, `%autosetup` y los mecanismos modernos recomendados.

Las técnicas históricas deben poder reconocerse, pero se marcarán explícitamente como históricas cuando no sean la práctica moderna recomendada.

## 9. Buildroot

Debe explicarse la relación entre `%install`, `%{buildroot}` y `%files`, diferenciando el buildroot moderno del tag histórico `BuildRoot:`.

## 10. Macros RPM

Las macros se tratarán como un subsistema propio. Se estudiarán macros predefinidas, `%global`, `%define`, macros parametrizadas, expansión, precedencia, evaluación y debugging mediante herramientas como `rpm --eval` y `rpm --showrc`.

## 11. %files y ownership

Debe estudiarse `%dir`, `%doc`, `%license`, `%config`, `%config(noreplace)`, `%attr`, `%defattr`, `%exclude`, globs, directorios, ownership y permisos.

Debe distinguirse claramente instalar algo en `%{buildroot}` de declararlo como perteneciente a un paquete.

## 12. Subpackages

Se estudiará cómo un mismo SRPM genera múltiples RPM binarios, incluyendo patrones como paquete principal, `-devel`, `-libs`, `-doc` y herramientas auxiliares, junto con sus dependencias internas.

## 13. Dependencias

Debe estudiarse BuildRequires, Requires, Provides, Conflicts, Obsoletes, dependencias versionadas, virtual Provides, weak dependencies, rich dependencies y dependencias automáticas.

Las rich dependencies incluirán `and`, `or`, `if`, `unless`, `with` y `without`.

## 14. Generación automática de dependencias

Debe explicarse conceptualmente la relación archivos → generadores → Provides/Requires y analizar ejemplos reales cuando corresponda.

## 15. Scriptlets

Se estudiarán `%pretrans`, `%pre`, `%post`, `%preun`, `%postun` y `%posttrans`, incluyendo `$1`, orden, entorno, exit status, errores y relación con la transacción.

## 16. Triggers

Debe estudiarse triggers, file triggers y transaction file triggers, explicando qué problemas resuelven y cuándo evitan scriptlets repetidos.

## 17. Transacciones

El alumno debe comprender instalación, actualización, downgrade y eliminación como operaciones transaccionales y relacionarlas con dependencias, scriptlets, triggers y rpmdb.

## 18. RPM frente a DNF

Debe mantenerse una separación clara. RPM administra paquetes y su base local; DNF/libdnf5 añade repositorios, selección, descarga y resolución de dependencias a un nivel superior.

## 19. libsolv y solver

El PATH profundiza hasta Pool, Repo, Solvable, Reldep, jobs, reglas, SAT, UNSAT y backtracking. El objetivo es comprender cómo un solver determina una solución válida y poder investigar casos reales mediante herramientas y APIs de libsolv.

## 20. SRPM

Debe comprenderse la diferencia entre RPM binario y Source RPM, qué contiene un SRPM, cómo inspeccionarlo y cómo reconstruir paquetes a partir de él.

## 21. rpmbuild

Se estudiarán `rpmbuild -ba`, `-bb`, `-bs`, las fases de construcción, árbol de trabajo y relación con las secciones SPEC.

## 22. rpmlint

Debe utilizarse como herramienta de análisis, interpretando cada diagnóstico en contexto y contrastándolo con las Packaging Guidelines en lugar de tratar su salida mecánicamente.

## 23. Mock

Mock se estudiará como herramienta de builds aislados y reproducibles. Debe comprenderse por qué compilar correctamente en la máquina del desarrollador no demuestra que las BuildRequires estén completas.

## 24. Fedora Packaging Guidelines

Constituyen una referencia normativa fundamental. Debe distinguirse siempre entre lo que RPM técnicamente permite y lo que Fedora recomienda o exige para sus paquetes.

## 25. Fedora Package Review

Debe comprenderse el flujo SPEC → SRPM → rpmlint → Mock → guidelines → review y las responsabilidades asociadas al proceso.

## 26. COPR

COPR se estudiará para builds y repositorios fuera de la infraestructura oficial principal de Fedora, comprendiendo su posición y diferencias frente a Koji.

## 27. dist-git y fedpkg

Debe estudiarse el modelo Fedora dist-git y su relación con Git, SPEC, sources, patches, branches, releases y `fedpkg`.

## 28. Koji

Debe comprenderse build, task, target, tag, buildroot, package y NVR, relacionando Koji con dist-git, Mock y la infraestructura de Fedora.

## 29. Bodhi

Debe estudiarse su papel en el ciclo de actualizaciones de Fedora y el flujo desde un build hasta su distribución como actualización.

## 30. Repositorios RPM

Debe estudiarse repository metadata, repodata, `createrepo_c`, configuración de repositorios, publicación y consumo. El alumno construirá repositorios de laboratorio.

## 31. Firmas y confianza

Se estudiarán `rpmkeys`, `rpm -K`, `rpm --checksig`, OpenPGP/GPG, firmas de paquetes, claves y trust, distinguiendo integridad de autenticidad.

## 32. Troubleshooting

Cada bloque debe desarrollar capacidad de diagnóstico: SPEC, macros, dependencias, scriptlets, transacciones, rpmdb, builds, Mock, metadata de repositorios, firmas, Koji y Bodhi.

## 33. Internals

En niveles avanzados se estudiarán RPM headers, payload, rpmdb, macro engine, dependency generators, transactions, scriptlets y signatures con suficiente profundidad para razonar sobre el comportamiento interno.

## 34. Automatización

Las herramientas auxiliares favorecerán scripts modulares y reutilizables. En el entorno del curso se priorizarán funciones Zsh integrables en una configuración modular.

## 35. Proyecto final

Todo el conocimiento debe converger en el workflow:

upstream → SPEC → Sources/Patches → SRPM → Mock → rpmlint → review → COPR → dist-git → Koji → Bodhi → repository.

El objetivo no es simplemente ejecutar `rpmbuild`, sino comprender el ecosistema RPM/Fedora como un sistema completo y poder diagnosticar cada frontera del proceso.
