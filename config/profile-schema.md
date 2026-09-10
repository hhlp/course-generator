# ESQUEMA DE UN PERFIL

Cada dominio vive en `profiles/<nombre>/` y contiene:

- `profile.yaml` — metadatos y reglas declarativas;
- `domain.md` — conocimiento, alcance, herramientas y reglas específicas;
- `bibliography.md` — bibliografía/documentación del dominio.

El motor no contiene conocimiento específico de C++, systemd, SELinux, firewalld, OpenSSH o RPM.

## Artefactos y proyectos

Un perfil puede declarar:

```yaml
artifacts:
  enabled: true
  default_strategy: auto

  project_policy:
    integrator_projects: auto
    diagnostic_projects: auto
    require_project_for_every_block: false

  overrides:
    "X.Y":
      strategy: standalone_project
      project_type: integrator
      project_id: nombre-estable
      knowledge_dependencies: ["bloque-X"]
      artifact_dependencies: []
      required_files:
        - README.md
      validation_required: true
```

Estrategias soportadas:

- `none` — sólo Markdown y ejemplos embebidos;
- `standalone_artifacts` — archivos auxiliares independientes;
- `standalone_project` — proyecto nuevo y autocontenido;
- `extends_previous_project` — continúa físicamente un proyecto registrado;
- `diagnostic_project` — mini-debugger/herramienta de observación y troubleshooting;
- `final_integrator_project` — proyecto final autocontenido que integra conocimientos previos.

Tipos de proyecto:

- `integrator` — construir y aplicar conjuntamente conocimientos previos;
- `diagnostic` — observar estado interno, correlacionar evidencia, explicar causas y diagnosticar.

Regla conceptual:

> Los proyectos integradores enseñan a construir. Los mini-debuggers enseñan a observar, explicar y diagnosticar.

No se obliga a que cada bloque o perfil tenga ambos tipos. Un proyecto sólo debe aparecer cuando el PATH, el perfil o el planner puedan justificar su valor pedagógico.

`diagnostic_project` implica `project_type: diagnostic`. `standalone_project` y `final_integrator_project` usan normalmente `project_type: integrator`, salvo una configuración explícita compatible.

`knowledge_dependencies` y `artifact_dependencies` son conceptos distintos. Conocer material anterior no implica reutilizar su código.

Los overrides del perfil tienen prioridad sobre la inferencia del planner.

## Validación local

```yaml
validation:
  enabled: true
  require_tools: false
  stop_on_failure: true
  timeout_seconds: 180
  commands:
    - [cmake, -S, ., -B, build]
    - [cmake, --build, build]
```

Los comandos se ejecutan en el directorio raíz del proyecto generado. Si `require_tools` es falso, una herramienta ausente produce `SKIPPED`; un comando disponible que termina con código distinto de cero produce `FAIL`.
