# Course Generator

Generador de cursos técnicos **de cero a experto**, organizado por *learning paths*, bloques y lecciones. Permite validar el itinerario completo, inspeccionar el contexto y generar progresivamente materiales técnicos con planificación, auditoría y reparación.

- **Idea y pruebas:** hhlp.
- **Asistencia:** ChatGPT (contenidos, Python y API).

> **Bibliografía:** los libros citados son referencias; no se distribuyen con el proyecto. La documentación oficial de cada tecnología es la fuente primaria.

## Contenidos

- [Cómo funciona](#cómo-funciona)
- [Instalación](#instalación)
- [Estructura de los PATHs](#estructura-de-los-paths)
- [Catálogo de Learning Paths](#catálogo-de-learning-paths)
- [Validación de perfiles](#validación-de-perfiles)
- [Flujo recomendado](#flujo-recomendado)
- [CLI y comandos](#cli-y-comandos)
- [Artefactos y proyectos](#artefactos-y-proyectos)
- [Comprobación y buenas prácticas](#comprobación-y-buenas-prácticas)

## Cómo funciona

```text
PATH / bloque-X.txt
        │
        ▼
     PLANNER
        ▼
     TEACHER ──► Lección Markdown + artefactos
        │
        ▼
   Validación local (cuando corresponda)
        │
        ▼
     AUDITOR
      ├── PASS ──► Guardar resultados
      └── FAIL ──► REPAIR ──► Validar y auditar
```

El motor separa la **lógica común** de los **perfiles específicos** de cada disciplina. Las dependencias de conocimientos y las dependencias de proyectos se modelan por separado.

## Instalación

Requisitos: Python 3.12 o superior, `uv` y una clave API válida para generación real.

```bash
git clone https://github.com/hhlp/course-generator.git
cd course-generator
uv sync
cp .env.example .env
```

Configura `OPENAI_API_KEY` en `.env` y, cuando corresponda, los parámetros del modelo. No incluyas secretos en commits. Las comprobaciones `--dry-run` no consumen créditos de la API.

## Estructura de los PATHs

```text
paths/<dominio>/
├── initial.txt             # Itinerario maestro
├── bloque-0.txt            # Generado al dividir el maestro
├── bloque-1.txt
└── ...

profiles/<dominio>/
├── profile.yaml            # Parámetros pedagógicos y de generación
├── domain.md               # Contexto y alcance técnico
└── bibliography.md         # Referencias documentales
```

No todos los directorios tienen idéntica estructura: existen rutas anidadas, especialmente `paths/english/{A2,B2,C2}` y `paths/tcp/design`. Los nombres de `paths/` y `profiles/` no siempre coinciden uno a uno (por ejemplo, inglés emplea perfiles anidados).

### Profundidad pedagógica

Cada PATH se diseña para avanzar desde los fundamentos hasta escenarios avanzados, prestando atención —según el dominio— a teoría, instalación, configuración, funcionamiento interno, pruebas, laboratorios, seguridad, observabilidad, rendimiento, diagnóstico, resolución de fallos y proyectos integradores. La existencia de un PATH revisado no implica que todas sus lecciones Markdown se hayan generado o auditado.

## Catálogo de Learning Paths

Inventario comprobado en la rama `main` el **23 de octubre de 2026**. Se han localizado **72 itinerarios `initial.txt`** en **48 directorios raíz**. Las rutas anidadas se muestran explícitamente; el inventario no demuestra por sí solo que se hayan generado o auditado todas las lecciones. La revisión curricular con GPT-6.1-sol (Medium) y la comprobación de estilo YAML mediante `yamllint` han sido comunicadas por el mantenedor.

### Agile y Product Management

| Learning Path | Directorio |
|---|---|
| [Scrum Master](https://github.com/hhlp/course-generator/tree/main/paths/sm) | `sm` |
| [Product Owner](https://github.com/hhlp/course-generator/tree/main/paths/po) | `po` |
| [kanban](https://github.com/hhlp/course-generator/tree/main/paths/kanban) | `kanban` |

### Linux, administración, seguridad y servicios

| Learning Path | Directorio |
|---|---|
| [1.- TIME](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/1.-%20TIME) | `rhcsa/1.- TIME` |
| [10. MAIL](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/10.%20MAIL) | `rhcsa/10. MAIL` |
| [11. VPN](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/11.%20VPN) | `rhcsa/11. VPN` |
| [2. DNS](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/2.%20DNS) | `rhcsa/2. DNS` |
| [3. DHCP](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/3.%20DHCP) | `rhcsa/3. DHCP` |
| [4. DHCP + DNS INTEGRATION](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/4.%20DHCP%20%2B%20DNS%20INTEGRATION) | `rhcsa/4. DHCP + DNS INTEGRATION` |
| [5.- IAM](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/5.-%20IAM) | `rhcsa/5.- IAM` |
| [6.- STORAGE SERVICE](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/6.-%20STORAGE%20SERVICE) | `rhcsa/6.- STORAGE SERVICE` |
| [8.- WEB SERVER](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/8.-%20WEB%20SERVER) | `rhcsa/8.- WEB SERVER` |
| [9. PROXY](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa/9.%20PROXY) | `rhcsa/9. PROXY` |
| [RHCSA y servicios](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa) | `rhcsa` |
| [bash-zsh](https://github.com/hhlp/course-generator/tree/main/paths/bash-zsh) | `bash-zsh` |
| [coreutils](https://github.com/hhlp/course-generator/tree/main/paths/coreutils) | `coreutils` |
| [grep](https://github.com/hhlp/course-generator/tree/main/paths/grep) | `grep` |
| [sed](https://github.com/hhlp/course-generator/tree/main/paths/sed) | `sed` |
| [awk](https://github.com/hhlp/course-generator/tree/main/paths/awk) | `awk` |
| [regex](https://github.com/hhlp/course-generator/tree/main/paths/regex) | `regex` |
| [systemd](https://github.com/hhlp/course-generator/tree/main/paths/systemd) | `systemd` |
| [openssh-watchdog](https://github.com/hhlp/course-generator/tree/main/paths/openssh-watchdog) | `openssh-watchdog` |
| [selinux](https://github.com/hhlp/course-generator/tree/main/paths/selinux) | `selinux` |
| [firewalld](https://github.com/hhlp/course-generator/tree/main/paths/firewalld) | `firewalld` |
| [rpm](https://github.com/hhlp/course-generator/tree/main/paths/rpm) | `rpm` |
| [git](https://github.com/hhlp/course-generator/tree/main/paths/git) | `git` |
| [gpg](https://github.com/hhlp/course-generator/tree/main/paths/gpg) | `gpg` |
| [vpn](https://github.com/hhlp/course-generator/tree/main/paths/vpn) | `vpn` |

### Programación

| Learning Path | Directorio |
|---|---|
| [python](https://github.com/hhlp/course-generator/tree/main/paths/python) | `python` |
| [cpp](https://github.com/hhlp/course-generator/tree/main/paths/cpp) | `cpp` |
| [rust](https://github.com/hhlp/course-generator/tree/main/paths/rust) | `rust` |
| [java](https://github.com/hhlp/course-generator/tree/main/paths/java) | `java` |
| [go](https://github.com/hhlp/course-generator/tree/main/paths/go) | `go` |
| [javascript](https://github.com/hhlp/course-generator/tree/main/paths/javascript) | `javascript` |
| [typescript](https://github.com/hhlp/course-generator/tree/main/paths/typescript) | `typescript` |
| [groovy](https://github.com/hhlp/course-generator/tree/main/paths/groovy) | `groovy` |

### Fundamentos y redes

| Learning Path | Directorio |
|---|---|
| [algebra](https://github.com/hhlp/course-generator/tree/main/paths/algebra) | `algebra` |
| [big-o](https://github.com/hhlp/course-generator/tree/main/paths/big-o) | `big-o` |
| [design](https://github.com/hhlp/course-generator/tree/main/paths/tcp/design) | `tcp/design` |
| [TCP/IP y diseño de redes](https://github.com/hhlp/course-generator/tree/main/paths/tcp) | `tcp` |

### DevOps y plataformas

| Learning Path | Directorio |
|---|---|
| [ansible](https://github.com/hhlp/course-generator/tree/main/paths/ansible) | `ansible` |
| [terraform](https://github.com/hhlp/course-generator/tree/main/paths/terraform) | `terraform` |
| [jenkins](https://github.com/hhlp/course-generator/tree/main/paths/jenkins) | `jenkins` |
| [container](https://github.com/hhlp/course-generator/tree/main/paths/container) | `container` |
| [kubernetes](https://github.com/hhlp/course-generator/tree/main/paths/kubernetes) | `kubernetes` |
| [vagrant](https://github.com/hhlp/course-generator/tree/main/paths/vagrant) | `vagrant` |

### Bases de datos

| Learning Path | Directorio |
|---|---|
| [Diseño de bases de datos](https://github.com/hhlp/course-generator/tree/main/paths/dd) | `dd` |
| [sql](https://github.com/hhlp/course-generator/tree/main/paths/sql) | `sql` |
| [Administración de bases de datos](https://github.com/hhlp/course-generator/tree/main/paths/dba) | `dba` |
| [dba](https://github.com/hhlp/course-generator/tree/main/paths/mongodb/dba) | `mongodb/dba` |
| [sql](https://github.com/hhlp/course-generator/tree/main/paths/mongodb/sql) | `mongodb/sql` |

### Observabilidad y logging

| Learning Path | Directorio |
|---|---|
| [prometheus](https://github.com/hhlp/course-generator/tree/main/paths/prometheus) | `prometheus` |
| [grafana](https://github.com/hhlp/course-generator/tree/main/paths/grafana) | `grafana` |
| [1.- logging](https://github.com/hhlp/course-generator/tree/main/paths/log/1.-%20logging) | `log/1.- logging` |
| [2.- nagios](https://github.com/hhlp/course-generator/tree/main/paths/log/2.-%20nagios) | `log/2.- nagios` |
| [3.- zabixx](https://github.com/hhlp/course-generator/tree/main/paths/log/3.-%20zabixx) | `log/3.- zabixx` |
| [4.- Elastic](https://github.com/hhlp/course-generator/tree/main/paths/log/4.-%20Elastic) | `log/4.- Elastic` |
| [5.- opensearch](https://github.com/hhlp/course-generator/tree/main/paths/log/5.-%20opensearch) | `log/5.- opensearch` |
| [6.- opentelemetry / cpp](https://github.com/hhlp/course-generator/tree/main/paths/log/6.-%20opentelemetry/cpp) | `log/6.- opentelemetry/cpp` |
| [6.- opentelemetry / go](https://github.com/hhlp/course-generator/tree/main/paths/log/6.-%20opentelemetry/go) | `log/6.- opentelemetry/go` |
| [6.- opentelemetry](https://github.com/hhlp/course-generator/tree/main/paths/log/6.-%20opentelemetry) | `log/6.- opentelemetry` |
| [6.- opentelemetry / java](https://github.com/hhlp/course-generator/tree/main/paths/log/6.-%20opentelemetry/java) | `log/6.- opentelemetry/java` |
| [6.- opentelemetry / javascript](https://github.com/hhlp/course-generator/tree/main/paths/log/6.-%20opentelemetry/javascript) | `log/6.- opentelemetry/javascript` |
| [6.- opentelemetry / python](https://github.com/hhlp/course-generator/tree/main/paths/log/6.-%20opentelemetry/python) | `log/6.- opentelemetry/python` |

### Ciencia de datos y Python

| Learning Path | Directorio |
|---|---|
| [numpy](https://github.com/hhlp/course-generator/tree/main/paths/numpy) | `numpy` |
| [pandas](https://github.com/hhlp/course-generator/tree/main/paths/pandas) | `pandas` |
| [graficos](https://github.com/hhlp/course-generator/tree/main/paths/graficos) | `graficos` |
| [Python para ingeniería de redes](https://github.com/hhlp/course-generator/tree/main/paths/python%20for%20ne) | `python for ne` |

### Documentación e idiomas

| Learning Path | Directorio |
|---|---|
| [latex](https://github.com/hhlp/course-generator/tree/main/paths/latex) | `latex` |
| [A2](https://github.com/hhlp/course-generator/tree/main/paths/english/A2) | `english/A2` |
| [B2](https://github.com/hhlp/course-generator/tree/main/paths/english/B2) | `english/B2` |
| [C2](https://github.com/hhlp/course-generator/tree/main/paths/english/C2) | `english/C2` |

### Relaciones entre rutas

- **Regex** y **Big O** son rutas transversales; cada lenguaje puede aplicar sus conceptos sin duplicar íntegramente los fundamentos.
- **TCP/IP** y **diseño IPv4/IPv6** están diferenciados mediante `tcp` y `tcp/design`.
- Los servicios de **RHCSA** se organizan en rutas anidadas, con IAM como proveedor central de identidad cuando corresponda.
- **OpenTelemetry** tiene una ruta general y especializaciones independientes para Python, C++, Go, Java y JavaScript.
- **MongoDB** distingue consultas y administración; **SQL**, **diseño** y **DBA** mantienen alcances diferentes.

## Validación de perfiles

Los `profile.yaml` han superado la comprobación de estilo con
`yamllint`, según la validación del mantenedor:

```bash
uv run --with yamllint yamllint -c .yamllint profiles/
```

La rama de validación añade comprobaciones **offline** adicionales.
No requiere `OPENAI_API_KEY` ni consume créditos:

```bash
# Comprobar todos los perfiles, incluidos los anidados
uv run course-generator --validate-profiles

# Comprobar un perfil concreto
uv run course-generator \
  --validate-profile profiles/ansible/profile.yaml

# Enumerar todas las rutas de claves de cada YAML
uv run course-generator --validate-profiles --profile-items

# Informe JSON para automatización
uv run course-generator --validate-profiles --profiles-json
```

La validación reutiliza `load_profile()` y
`load_profile_context(strict=True)`: verifica que el perfil se puede
cargar, las estructuras ya tipadas por el cargador y la existencia
y contenido no vacío de los archivos de contexto
(`pedagogy`, `domain`, `bibliography`).
El proceso devuelve código 1 si hay errores y 0 si todos pasan.

**Alcance:** los parámetros pedagógicos arbitrarios se incorporan
completos al contexto del modelo. Por ello, una clave desconocida
no se considera automáticamente un error, y esta comprobación
**no certifica** que cada campo tenga un consumidor específico ni
que todas las lecciones se hayan generado y auditado. Para ello
harían falta reglas de esquema y pruebas adicionales.

## Flujo recomendado

**Revisa un PATH cada vez**, valida la estructura antes de realizar llamadas a la API y genera progresivamente las lecciones para poder auditar su calidad y controlar el gasto.

```text
initial.txt + profile.yaml + domain.md + bibliography.md
                      │
                      ▼
     Revisión pedagógica y técnica
                      │
                      ▼
     --validate-profiles (sin API)
                      │
                      ▼
 --split-blocks --check-lessons --dry-run
                      │
                      ▼
       --split-blocks --check-lessons
                      │
                      ▼
  bloque-0.txt ... bloque-N.txt
                      │
                      ▼
 --dry-run --validate-context --inspect
                      │
                      ▼
    Generación por bloque / lección
                      │
                      ▼
        Revisión + tests + commit
```

### 1. Validar sin generar ni gastar créditos

```bash
uv run course-generator \
  paths/python/initial.txt \
  --profile python \
  --split-blocks \
  --check-lessons \
  --dry-run
```

### 2. Separar en bloques

```bash
uv run course-generator \
  paths/python/initial.txt \
  --profile python \
  --split-blocks \
  --check-lessons
```

Por defecto, no se sobrescriben bloques existentes. Usa `--force` **únicamente** cuando quieras reemplazarlos deliberadamente.

### 3. Inspeccionar antes de generar

```bash
uv run course-generator \
  paths/python/bloque-0.txt \
  --profile python \
  --lesson 0.1 \
  --dry-run \
  --validate-context \
  --inspect \
  --show-prompt
```

### 4. Generar y continuar

```bash
# Generar un bloque
uv run course-generator paths/python/bloque-0.txt --profile python

# Trabajar sobre una lección concreta
uv run course-generator paths/python/bloque-0.txt --profile python --lesson 0.1

# Reanudar según el estado guardado
uv run course-generator paths/python/bloque-0.txt --profile python --resume
```

La generación real utiliza la API. Comprueba antes los límites, los créditos y el estado de las salidas.

## CLI y comandos

```text
course-generator [-h] [--profile PROFILE]
                 [--validate-profiles] [--validate-profile FILE]
                 [--profile-items] [--profiles-json]
                 [--lesson LESSON] [--resume] [--force] [--dry-run]
                 [--show-prompt] [--inspect]
                 [--save-prompt FILE] [--save-inspect FILE]
                 [--dump-json] [--validate-context]
                 [--neighbor-radius N] [--split-blocks]
                 [--check-lessons] [--no-zip] [--root ROOT]
                 [path]
```

`path` y `--profile` son obligatorios para generación, pero no para
validación independiente de perfiles.

| Opción                                        | Propósito                                         |
|-----------------------------------------------|---------------------------------------------------|
| `--profile`                                   | Selecciona el perfil al generar.                  |
| `--validate-profiles`                         | Valida todos los perfiles sin API.                |
| `--validate-profile FILE`                     | Valida un perfil concreto sin API.                |
| `--profile-items`                             | Lista las rutas de claves encontradas.            |
| `--profiles-json`                            | Produce un informe JSON.                         |
| `--split-blocks`                              | Divide `initial.txt` en archivos de bloque.       |
| `--check-lessons`                             | Comprueba continuidad de numeración.              |
| `--dry-run`                                   | Valida/inspecciona sin llamar a la API.           |
| `--validate-context`                          | Comprueba resolución del contexto.                |
| `--inspect` y `--show-prompt`                 | Explican el contexto y el prompt.                 |
| `--save-prompt FILE`, `--save-inspect FILE`   | Guardan informes de inspección.                   |
| `--dump-json`                                 | Expone el payload estructurado.                   |
| `--neighbor-radius N`                         | Ajusta el contexto de lecciones vecinas.          |
| `--lesson X.Y`                                | Selecciona una lección.                           |
| `--resume`                                    | Continúa desde el estado registrado.              |
| `--force`                                     | Fuerza repetición/sobrescritura cuando proceda.   |
| `--no-zip`                                    | Deshabilita el ZIP de salida.                     |
| `--root ROOT`                                 | Especifica la raíz de trabajo.                    |

Consulta también la ayuda instalada para confirmar opciones en tu versión:

```bash
uv run course-generator --help
```

## Artefactos y proyectos

El motor admite estrategias de artefactos:

- `none`: lección sin artefactos independientes.
- `standalone_artifacts`: archivos independientes.
- `standalone_project`: proyecto independiente.
- `extends_previous_project`: ampliación de un proyecto anterior.
- `final_integrator_project`: integración final.

Distingue `knowledge_dependencies` (conocimientos previos) y `artifact_dependencies` (artefactos que deben reutilizarse). El registro de proyectos se mantiene por perfil en `state/<perfil>/projects.json`.

En C++, determinados proyectos se definen como independientes; si están disponibles, CMake y CTest permiten validar configuración, compilación y pruebas.

## Comprobación y buenas prácticas

1. Revisar **`initial.txt`**, **`profile.yaml`**, **`domain.md`** y **`bibliography.md`** juntos antes de iniciar la generación.
2. Conservar la numeración continua `X.1`, `X.2`, `X.3`, etc., y los bloques `0.`, `1.`, `2.` sin saltos.
3. No duplicar cursos transversales: referenciar Regex, Big O y otros fundamentos cuando corresponda.
4. Hacer primero `--dry-run` y `--check-lessons`, y después generar lecciones/bloques de manera incremental.
5. Validar ejemplos, entornos y proyectos con pruebas prácticas adecuadas al dominio.
6. Versionar cambios una vez comprobados y revisar salidas antes de gastar más créditos.

---

Repositorio: **[hhlp/course-generator](https://github.com/hhlp/course-generator)**.

_Inventario verificado en GitHub el 23 de octubre de 2026. La revisión de contenidos y la validación de perfiles no equivalen a la auditoría de las lecciones generadas._

## Test

``` bash
uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest
```
