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

## Flujo de trabajo del PATH

El generador distingue entre dos tipos de archivo de aprendizaje:

```text
initial.txt
    ↓
revisión del learning path completo
    ↓
--dry-run / --inspect / --show-prompt
    ↓
separación por bloques
    ↓
bloque-0.txt
bloque-1.txt
bloque-2.txt
...
    ↓
generación real
```

`initial.txt` puede contener múltiples bloques y está pensado para diseñar, revisar e inspeccionar
el learning path completo antes de dividirlo. En modo `--dry-run` el parser permite este formato
multi-bloque.

La generación real conserva una regla más estricta: cada `bloque-X.txt` debe contener un único
bloque. Esto evita mezclar estados, salidas, manifests y ZIP de bloques diferentes.

## Separar `initial.txt` por bloques

La separación de un PATH maestro está integrada directamente en la CLI de `course-generator`.
No requiere `--profile`, porque esta operación sólo analiza la estructura del PATH y no carga
perfil, prompts ni API.

Antes de escribir archivos, validar el PATH completo:

```bash
uv run course-generator \
    paths/regex/initial.txt \
    --split-blocks \
    --check-lessons \
    --dry-run
```

`--split-blocks` detecta las cabeceras `0.`, `1.`, `2.`... y prepara un archivo independiente por
bloque. `--check-lessons` exige además numeración continua dentro de cada bloque:

```text
X.1
X.2
X.3
...
```

Si el `dry-run` es correcto, generar los bloques:

```bash
uv run course-generator \
    paths/regex/initial.txt \
    --profile regex \
    --split-blocks \
    --check-lessons
```

El resultado será:

```text
paths/regex/
├── initial.txt
├── bloque-0.txt
├── bloque-1.txt
├── bloque-2.txt
└── ...
```

Por seguridad, la CLI no sobrescribe `bloque-X.txt` existentes. Para regenerarlos
deliberadamente:

```bash
uv run course-generator \
    paths/regex/initial.txt \
    --profile regex
    --split-blocks \
    --check-lessons \
    --force
```

También puede utilizarse otro directorio:

```bash
uv run course-generator \
    paths/regex/initial.txt \
    --profile regex
    --split-blocks \
    --check-lessons \
    --output-dir /tmp/regex-blocks
```

La separación valida:

- cabeceras de bloque duplicadas;
- lecciones situadas bajo un bloque incorrecto;
- bloques intermedios ausentes;
- numeración continua de lecciones con `--check-lessons`;
- sobrescrituras accidentales.

El flujo recomendado queda así:

```text
initial.txt
    ↓
revisión global
    ↓
--split-blocks --check-lessons --dry-run
    ↓
--split-blocks --check-lessons
    ↓
bloque-0.txt ... bloque-N.txt
    ↓
--dry-run / --inspect sobre lecciones representativas
    ↓
generación real
```

la interfaz recomendada es ahora `course-generator --split-blocks`.

## Inspección y dry-run

`--dry-run` resuelve y valida el contexto sin llamar a la API de OpenAI. Puede combinarse con las
opciones de inspección:

```text
--dry-run
--show-prompt
--inspect
--save-prompt FILE
--save-inspect FILE
--dump-json
--validate-context
--neighbor-radius N
```

Funciones principales:

- `--dry-run`: valida y materializa la inspección sin realizar llamadas a la API.
- `--show-prompt`: muestra las instrucciones y el input/payload que recibiría la etapa materializable.
- `--inspect`: muestra cómo se ha construido el contexto y la procedencia de sus componentes.
- `--save-prompt FILE`: guarda el prompt inspeccionado en un archivo.
- `--save-inspect FILE`: guarda el informe de inspección.
- `--dump-json`: muestra la representación estructurada del payload.
- `--validate-context`: comprueba que el contexto requerido pueda resolverse correctamente.
- `--neighbor-radius N`: modifica el radio de lecciones vecinas utilizado durante la inspección.

En un `dry-run`, las etapas que dependen de resultados todavía inexistentes no se inventan. Por
ejemplo, `teacher` requiere la salida del planner, `auditor` requiere la salida del teacher y la
validación, y `repair` requiere además un fallo de auditoría.

Ejemplo de inspección de un PATH maestro todavía no separado:

```bash
uv run course-generator \
    paths/regex/initial.txt \
    --profile regex \
    --lesson 0.1 \
    --dry-run \
    --validate-context \
    --inspect \
    --show-prompt \
    --dump-json \
    --save-prompt /tmp/regex-0.1.prompt.txt \
    --save-inspect /tmp/regex-0.1.inspect.txt
```

La presencia de `--dry-run` garantiza que esta operación no llama a la API.

También puede hacerse una validación mínima de un bloque ya separado:

```bash
uv run course-generator \
    paths/cpp/bloque-1.txt \
    --profile cpp \
    --lesson 1.7 \
    --dry-run
```

## Comandos de generación

Generar una lección:

```bash
uv run course-generator paths/cpp/bloque-1.txt --profile cpp --lesson 1.7
```

Generar un proyecto final concreto:

```bash
uv run course-generator paths/cpp/bloque-1.txt --profile cpp --lesson 1.41
```

Generar el bloque:

```bash
uv run course-generator paths/cpp/bloque-1.txt --profile cpp
```

Regenerar:

```bash
uv run course-generator paths/cpp/bloque-1.txt --profile cpp --lesson 1.41 --force
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

## Test

```
uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest
```
