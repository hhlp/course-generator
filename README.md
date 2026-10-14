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

El siguiente índice refleja los directorios **comprobados en `paths/` de la rama `main` el 14 de octubre de 2026**. Son **48 directorios raíz**; `english/A2`, `english/B2`, `english/C2` y `tcp/design` son subrutas que también se muestran para facilitar la navegación. Una materia puede relacionarse con varias áreas sin duplicarse en este índice.

### Agile y Product Management

| Learning Path | Directorio |
|---|---|
| [Scrum Master](https://github.com/hhlp/course-generator/tree/main/paths/sm) | `sm` |
| [Product Owner](https://github.com/hhlp/course-generator/tree/main/paths/po) | `po` |
| [Kanban](https://github.com/hhlp/course-generator/tree/main/paths/kanban) | `kanban` |

### Linux, administración y seguridad

| Learning Path | Directorio |
|---|---|
| [RHCSA](https://github.com/hhlp/course-generator/tree/main/paths/rhcsa) | `rhcsa` |
| [Bash / Zsh](https://github.com/hhlp/course-generator/tree/main/paths/bash-zsh) | `bash-zsh` |
| [GNU Coreutils](https://github.com/hhlp/course-generator/tree/main/paths/coreutils) | `coreutils` |
| [grep / ripgrep](https://github.com/hhlp/course-generator/tree/main/paths/grep) | `grep` |
| [sed](https://github.com/hhlp/course-generator/tree/main/paths/sed) | `sed` |
| [AWK](https://github.com/hhlp/course-generator/tree/main/paths/awk) | `awk` |
| [Expresiones regulares](https://github.com/hhlp/course-generator/tree/main/paths/regex) | `regex` |
| [systemd](https://github.com/hhlp/course-generator/tree/main/paths/systemd) | `systemd` |
| [OpenSSH / Watchdog](https://github.com/hhlp/course-generator/tree/main/paths/openssh-watchdog) | `openssh-watchdog` |
| [SELinux](https://github.com/hhlp/course-generator/tree/main/paths/selinux) | `selinux` |
| [firewalld](https://github.com/hhlp/course-generator/tree/main/paths/firewalld) | `firewalld` |
| [RPM Packaging](https://github.com/hhlp/course-generator/tree/main/paths/rpm) | `rpm` |
| [Git](https://github.com/hhlp/course-generator/tree/main/paths/git) | `git` |
| [GPG / OpenPGP](https://github.com/hhlp/course-generator/tree/main/paths/gpg) | `gpg` |

### Programación

| Learning Path | Directorio |
|---|---|
| [Python](https://github.com/hhlp/course-generator/tree/main/paths/python) | `python` |
| [C++](https://github.com/hhlp/course-generator/tree/main/paths/cpp) | `cpp` |
| [Rust](https://github.com/hhlp/course-generator/tree/main/paths/rust) | `rust` |
| [Java](https://github.com/hhlp/course-generator/tree/main/paths/java) | `java` |
| [Go](https://github.com/hhlp/course-generator/tree/main/paths/go) | `go` |
| [JavaScript](https://github.com/hhlp/course-generator/tree/main/paths/javascript) | `javascript` |
| [TypeScript](https://github.com/hhlp/course-generator/tree/main/paths/typescript) | `typescript` |
| [Groovy](https://github.com/hhlp/course-generator/tree/main/paths/groovy) | `groovy` |

### Fundamentos y redes

| Learning Path | Directorio |
|---|---|
| [Álgebra booleana](https://github.com/hhlp/course-generator/tree/main/paths/algebra) | `algebra` |
| [Complejidad algorítmica / Big O](https://github.com/hhlp/course-generator/tree/main/paths/big-o) | `big-o` |
| [TCP/IP](https://github.com/hhlp/course-generator/tree/main/paths/tcp) | `tcp` |
| [Diseño IPv4 / IPv6 y subnetting](https://github.com/hhlp/course-generator/tree/main/paths/tcp/design) | `tcp/design` |
| [VPN / OpenVPN / WireGuard](https://github.com/hhlp/course-generator/tree/main/paths/vpn) | `vpn` |

### DevOps, automatización y plataformas

| Learning Path | Directorio |
|---|---|
| [Ansible](https://github.com/hhlp/course-generator/tree/main/paths/ansible) | `ansible` |
| [Terraform](https://github.com/hhlp/course-generator/tree/main/paths/terraform) | `terraform` |
| [Jenkins](https://github.com/hhlp/course-generator/tree/main/paths/jenkins) | `jenkins` |
| [Contenedores / Docker / Podman / Swarm](https://github.com/hhlp/course-generator/tree/main/paths/container) | `container` |
| [Kubernetes](https://github.com/hhlp/course-generator/tree/main/paths/kubernetes) | `kubernetes` |
| [Vagrant](https://github.com/hhlp/course-generator/tree/main/paths/vagrant) | `vagrant` |

### Bases de datos

| Learning Path | Directorio |
|---|---|
| [Diseño de bases de datos](https://github.com/hhlp/course-generator/tree/main/paths/dd) | `dd` |
| [SQL](https://github.com/hhlp/course-generator/tree/main/paths/sql) | `sql` |
| [Administración de bases de datos](https://github.com/hhlp/course-generator/tree/main/paths/dba) | `dba` |

### Observabilidad y logging

| Learning Path | Directorio |
|---|---|
| [Prometheus](https://github.com/hhlp/course-generator/tree/main/paths/prometheus) | `prometheus` |
| [Grafana](https://github.com/hhlp/course-generator/tree/main/paths/grafana) | `grafana` |
| [Linux Logging](https://github.com/hhlp/course-generator/tree/main/paths/log) | `log` |

### Ciencia de datos y Python

| Learning Path | Directorio |
|---|---|
| [NumPy](https://github.com/hhlp/course-generator/tree/main/paths/numpy) | `numpy` |
| [Pandas](https://github.com/hhlp/course-generator/tree/main/paths/pandas) | `pandas` |
| [Gráficos / visualización](https://github.com/hhlp/course-generator/tree/main/paths/graficos) | `graficos` |
| [Python for Network Engineers](https://github.com/hhlp/course-generator/tree/main/paths/python%20for%20ne) | `python for ne` |

### Documentación e idiomas

| Learning Path | Directorio |
|---|---|
| [LaTeX](https://github.com/hhlp/course-generator/tree/main/paths/latex) | `latex` |
| [Inglés A2](https://github.com/hhlp/course-generator/tree/main/paths/english/A2) | `english/A2` |
| [Inglés B2](https://github.com/hhlp/course-generator/tree/main/paths/english/B2) | `english/B2` |
| [Inglés C2](https://github.com/hhlp/course-generator/tree/main/paths/english/C2) | `english/C2` |

### Relaciones entre rutas

- **Regex** es una materia propia; Python, JavaScript, Java, Rust y otros lenguajes pueden trabajar sus APIs y particularidades sin repetir el curso completo de expresiones regulares.
- **Big O** aporta los fundamentos generales de complejidad; las implementaciones y el análisis de estructuras y algoritmos se contextualizan en cada lenguaje.
- **TCP/IP** y **diseño IPv4/IPv6** están diferenciados; la planificación de direccionamiento y subnetting se desarrolla en `tcp/design`.
- **Groovy** tiene PATH propio y es un conocimiento útil para Jenkins Pipeline.
- **Git** y **GPG** son rutas separadas pero complementarias en control de versiones y firma.
- **SQL**, **diseño de bases de datos** y **DBA** mantienen alcances distintos.

## Flujo recomendado

**Revisa un PATH cada vez**, valida la estructura antes de realizar llamadas a la API y genera progresivamente las lecciones para poder auditar su calidad y controlar el gasto.

```text
initial.txt + profile.yaml + domain.md + bibliography.md
                      │
                      ▼
     Revisión pedagógica y técnica
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
course-generator [-h] --profile PROFILE
                 [--lesson LESSON] [--resume] [--force] [--dry-run]
                 [--show-prompt] [--inspect]
                 [--save-prompt FILE] [--save-inspect FILE]
                 [--dump-json] [--validate-context]
                 [--neighbor-radius N] [--split-blocks]
                 [--check-lessons] [--no-zip] [--root ROOT]
                 path
```

| Opción                                        | Propósito                                         |
|-----------------------------------------------|---------------------------------------------------|
| `--profile`                                   | Selecciona el perfil; es obligatorio.             |
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

_Catálogo actualizado a partir de los directorios disponibles en GitHub; el estado de publicación de contenido generado, perfiles y validación individual de cada PATH puede variar._

## Test

``` bash
uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest
```
