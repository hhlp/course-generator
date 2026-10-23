# RPM PACKAGING EN PROFUNDIDAD — FEDORA

## Dominio

Este PATH estudia RPM desde sus fundamentos hasta el nivel necesario para comprender, construir, analizar, depurar y mantener paquetes dentro del ecosistema Fedora.

RPM no debe estudiarse únicamente como el comando `rpm`. El dominio completo relaciona:

RPM package format → RPM metadata → rpmdb → SPEC → rpmbuild → SRPM → dependencias → transacciones → repositorios → DNF/libdnf5 → libsolv → Mock → Fedora Packaging → COPR → dist-git → Koji → Bodhi.

El objetivo final es comprender el flujo completo:

upstream → source archive → SPEC → SRPM → build limpio → RPM → validación → review → build infrastructure → actualización → repositorio → instalación.

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

Mock se estudiará como herramienta de construcción en entornos limpios con aislamiento. Su uso por sí solo no demuestra hermeticidad ni reproducibilidad bit a bit. Debe comprenderse por qué compilar correctamente en la máquina del desarrollador no demuestra que las BuildRequires estén completas.

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

Base común: upstream → SPEC → Sources/Patches → SRPM → Mock → RPM → validación.

Itinerario COPR: paquete validado → proyecto COPR → build → repositorio propio.

Itinerario Fedora oficial: paquete validado → Package Review → acceso autorizado a dist-git → Koji → actualización mediante Bodhi cuando corresponda a la rama → repositorios Fedora.

COPR puede ayudar a realizar pruebas, pero no es un paso obligatorio de la incorporación oficial. Los laboratorios deben simular los pasos para los que el alumno no disponga de permisos y señalar cuáles se han ejecutado realmente.

El objetivo no es simplemente ejecutar `rpmbuild`, sino comprender el ecosistema RPM/Fedora como un sistema completo y poder diagnosticar cada frontera del proceso.


## 36. Ampliación avanzada por bloques (revisión)

Conservar los bloques 0–9 y todas las lecciones anteriores. Los apartados X.900.n existentes se conservan y se integran en el orden pedagógico de su bloque. La numeración identifica contenido; no determina por sí sola la secuencia de estudio. Esta revisión incorpora las lagunas en sus secciones temáticas, sin crear otra capa de ampliaciones.

- **0:** compatibilidad RPM 4/6, formato y payload.
- **1:** SPEC avanzado, buildrequires dinámicos y empaquetado por lenguaje.
- **2:** librpm, dependency generators, transacciones y solver.
- **3:** consultas programáticas, rpmdb SQLite y firma.
- **4:** DNF5/libdnf5, publicación y confianza en repositorios.
- **5:** integración completa con systemd, SELinux, bibliotecas y módulos kernel.
- **6:** ABI, seguridad de la cadena de suministro, SBOM y reproducibilidad.
- **7:** Packit, CI/CD, COPR, mantenimiento y gating.
- **8:** metodología de diagnóstico basada en evidencias y logs.
- **9:** proyecto integrador, publicación, regresión y documentación.

## 37. Criterios de competencia verificables

Cada bloque deberá incluir explicación de mecanismos internos, comandos reales en Fedora, salidas esperadas (marcadas como ilustrativas cuando proceda), verificación, errores frecuentes, procedimientos de diagnóstico y laboratorio. Distinguir comportamiento de RPM upstream, política Fedora y funciones de DNF5/libdnf5/libsolv. Verificar macros y opciones contra la versión instalada antes de presentarlas como universales.

El proyecto final exige SPEC, SRPM, RPM binario, pruebas en Mock, inspección de dependencias, repositorio firmado de laboratorio, pruebas de instalación/actualización/eliminación y evidencias de troubleshooting.


## 38. Orden de estudio y clasificación de entradas

Los identificadores originales son estables. Un encabezado agrupa contenido;
un subtema desarrolla una competencia; una tarea de proyecto describe un paso
de implementación. No convertir automáticamente cada línea numerada en una
lección independiente. Los títulos de comandos aislados se desarrollan junto
con su propósito, semántica, ejemplo, resultado y verificación.

Orden recomendado para la ruta de packaging:

1. Bloque 0: fundamentos y primera inspección de paquetes.
2. Bloque 1: primer SPEC, construcción y ciclo básico de prueba. Adelantar
   3.1–3.6 para consultar y verificar sus artefactos. Introducir Mock con 1.98;
   6.12 y 7.2 amplían después el mismo procedimiento.
3. Bloque 2: transacciones y dependencias; estudiar el solver conceptualmente
   y usar ejemplos preparados de testsolv. Diferir toda implementación 2.112.
4. Bloques 3 y 4: consultas avanzadas, repositorios y DNF5. Integrar aquí las
   ampliaciones X.900 correspondientes antes de sus laboratorios finales.
5. Bloques 5 y 6: integración, calidad y pruebas de actualización. Retomar las
   macros por lenguaje de 1.900 con los prerrequisitos de cada ecosistema.
6. Bloque 7: mantenimiento y los dos itinerarios de publicación.
7. Bloque 8: diagnóstico con escenarios reproducibles y evidencias.
8. Bloque 9: integración y aceptación, reutilizando los artefactos anteriores.

La especialización en implementación C/libsolv comienza tras el bloque 4.
No bloquear el aprendizaje básico de empaquetado por desconocer C. Para
completar el nivel experto de internals y el proyecto C sí se exige superar
2.113 antes del hito S1.

## 39. Un único mini-solver-debugger con cinco hitos

2.112.1–2.112.300 son tareas del mismo proyecto, no 300 lecciones autónomas.
2.112 permanece en su ubicación por trazabilidad y se consulta por hitos.
9.15 y 9.16 cierran ese proyecto; no inician una segunda implementación.

| Hito | Tareas conservadas | Momento | Evidencia de aceptación |
|---|---|---|---|
| S1 | 2.112.1–2.112.38 | Tras bloque 4 y 2.113 | CLI mínima; universo artificial; SAT y UNSAT; limpieza de recursos |
| S2 | 2.112.39–2.112.132 | Tras S1 y prácticas de repositorios del bloque 4 | Carga de RPM/repodata; repositorio instalado; consultas; transacción prevista |
| S3 | 2.112.133–2.112.199 | Tras bloque 6 y S2 | Análisis mediante herramientas RPM; SRPM; build limpio; comparación de dependencias |
| S4 | 2.112.200–2.112.250 | Tras bloque 8 y S3 | Casos diagnosticados; testcases; comparación controlada con DNF y testsolv |
| S5 | 2.112.251–2.112.300 | Durante bloque 9 y tras S4 | Arquitectura modular; pruebas de regresión; salida JSON; documentación y v1.0 |

Cada hito agrupa sus tareas en sesiones de diseño, implementación, diagnóstico
y verificación. Las opciones CLI se implementan juntas cuando comparten
competencia; cada opción no justifica una lección aislada. El código de cada
hito es la base del siguiente.

La resolución calcula una transacción prevista. El proyecto no necesita
ejecutar instalaciones privilegiadas: las pruebas reales se realizan con
DNF/RPM en el laboratorio preparado. No exigir una traza interna idéntica a
DNF: deben controlarse repositorios, arquitectura, estado instalado, jobs y
políticas antes de comparar resultados.

## 40. Configuración, SPEC y shells

Desarrollar explícitamente 1.86–1.97 y validar en 6.16: %ghost, %verify,
%{?_isa}, ExclusiveArch, ExcludeArch, .rpmnew y .rpmsave. La matriz de pruebas
debe cruzar %config frente a %config(noreplace), archivo local intacto o
modificado y configuración upstream igual o distinta, registrando el resultado
observado en cada combinación. Distinguir conservación de configuración,
persistencia de datos del servicio y reversión del conjunto de paquetes.

Zsh es la shell interactiva del alumno y de sus funciones auxiliares. No
transferir sus opciones, sintaxis ni configuración al SPEC. Explicar el
intérprete de cada fase de build y de cada scriptlet, sus dependencias y sus
posibles alternativas según RPM y la política Fedora. Separar expansión de
macros RPM, expansión shell y ejecución de Lua.

El análisis de SPEC debe delegar en rpmspec o las interfaces de RPM. No usar
expresiones regulares para reimplementar el parser completo ni inferir todas
las dependencias automáticas desde el texto fuente. La metadata final del
RPM construido es la referencia para sus Requires y Provides efectivos.

## 41. Reproducibilidad y vigencia técnica

Un entorno limpio facilita detectar BuildRequires ausentes. Aislamiento
describe qué separa el entorno del host. Hermeticidad exige controlar las
entradas externas. Reproducibilidad requiere comparar reconstrucciones con
entradas documentadas. Son propiedades diferentes y deben probarse por
separado; Mock no las garantiza todas automáticamente.

Registrar distribución, arquitectura, versiones RPM/DNF5/Mock, macros,
repositorios y NEVRA de dependencias. Separar la comparación del contenido
de las diferencias introducidas al firmar o publicar artefactos.

rpmdeps y rpmgraph son herramientas documentadas upstream; comprobar paquete
proveedor y ruta antes de concluir que no están disponibles. rpmdeps upstream
no es el proyecto externo homónimo; rpmgraph representa relaciones de
ordenación y no sustituye la resolución SAT de repositorios completos.

rpmautospec se estudia explícitamente en 1.93–1.95 y 7.15. El alumno debe
inspeccionar el Release y changelog generados y relacionarlos con Git.
No presentar las funciones recientes de RPM, las opciones DNF4 o los comandos
DNF5 como intercambiables sin comprobar la versión del laboratorio.

Los campos adicionales de profile.yaml son metadatos pedagógicos. Su mera
presencia no demuestra que course-generator los interprete; estas reglas se
mantienen también aquí para que el generador disponga de instrucciones de
dominio explícitas. La comprobación de integración requiere ejecutar el
generador en el repositorio del usuario.
