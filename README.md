# Course Generator

Generador genérico de cursos técnicos profundos, lección por lección y por bloques.

- Idea inspirada por : hhlp
- Asistida por       : ChatGPT (Bloques/Python/API)
- Testeado por       : hhlp

## Arquitectura

```text
PATH/bloque-X.txt
    ↓
PLANNER
    ↓
TEACHER
    ├── lesson Markdown
    └── artifacts/proyecto cuando corresponda
    ↓
materialización en staging
    ↓
validación local opcional
    ↓
AUDITOR
    ├── PASS → commit + guardar .md
    └── FAIL → REPAIR → validar → auditar
```

La pedagogía y el motor son comunes. Cada dominio vive en `profiles/<perfil>/`.

## Artefactos

Estrategias:

- `none`
- `standalone_artifacts`
- `standalone_project`
- `extends_previous_project`
- `final_integrator_project`

Se distinguen explícitamente:

- `knowledge_dependencies`: conocimientos anteriores necesarios;
- `artifact_dependencies`: archivos/proyectos anteriores que deben reutilizarse.

Los proyectos aprobados se registran globalmente por perfil en:

```text
state/<perfil>/projects.json
```

Esto permite continuidad incluso entre bloques cuando se declare `extends_previous_project`.

## C++

El perfil C++ declara como proyectos independientes:

```text
1.41  proyecto final PPP3         → standalone_project
3.30  proyecto C++17              → standalone_project
4.44  proyecto C++23              → standalone_project
5.29  proyecto generic library    → standalone_project
6.36  proyecto concurrente        → standalone_project
8.26  proyecto C++23 completo     → final_integrator_project
```

No reutilizan código entre sí. Sí pueden depender de conocimientos de bloques anteriores.

Los proyectos C++ se validan, cuando CMake/CTest estén disponibles, con configure → build → tests. El build temporal no entra en el ZIP.

## Instalación con uv

```bash
uv sync
cp .env.example .env
```

Configura `OPENAI_API_KEY` en `.env`.

## Comandos

Validar parser/config sin API:

```bash
uv run course-generator \
    paths/cpp/bloque-1.txt \
    --profile cpp \
    --lesson 1.7 \
    --dry-run
```

Generar una lección:

```bash
uv run course-generator paths/bloque-1.txt --profile cpp --lesson 1.7
```

Generar un proyecto final concreto:

```bash
uv run course-generator paths/bloque-1.txt --profile cpp --lesson 1.41
```

Generar el bloque:

```bash
uv run course-generator paths/bloque-1.txt --profile cpp
```

Regenerar:

```bash
uv run course-generator paths/bloque-1.txt --profile cpp --lesson 1.41 --force
```

## Salida

```text
output/cpp/bloque-1/
├── 1.1-....md
├── ...
├── 1.41-proyecto-final-ppp3.md
├── projects/
│   └── proyecto-final-ppp3/
│       ├── README.md
│       ├── CMakeLists.txt
│       ├── src/
│       └── tests/
├── INDEX.md
└── MANIFEST.md
```

Los artefactos se generan primero bajo `.staging/`; sólo se publican en `projects/` cuando la auditoría termina en PASS.


## Tipos de proyecto

El generador distingue dos intenciones pedagógicas:

- **Proyecto integrador** (`project_type: integrator`): construir algo coherente aplicando conjuntamente conocimientos previos.
- **Mini-debugger / proyecto diagnóstico** (`project_type: diagnostic`, normalmente `strategy: diagnostic_project`): observar el funcionamiento interno, correlacionar evidencia y practicar troubleshooting.

No se exige un proyecto por bloque. Los proyectos aparecen sólo cuando el PATH, el perfil o el planner justifican su valor pedagógico.
