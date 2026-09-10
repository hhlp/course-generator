from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from .models import Lesson, Profile
from .output import slugify

VALID_STRATEGIES = {
    "none",
    "standalone_artifacts",
    "standalone_project",
    "extends_previous_project",
    "diagnostic_project",
    "final_integrator_project",
}


class ArtifactError(ValueError):
    pass


@dataclass(slots=True)
class MaterializedArtifacts:
    strategy: str
    project_id: str | None
    root: Path | None
    files: list[Path]


def _safe_relpath(value: str) -> Path:
    posix = PurePosixPath(value)
    if posix.is_absolute() or ".." in posix.parts or not posix.parts:
        raise ArtifactError(f"Ruta de artefacto insegura: {value!r}")
    return Path(*posix.parts)


def profile_override(profile: Profile, lesson: Lesson) -> dict[str, Any]:
    artifacts = profile.data.get("artifacts", {}) or {}
    overrides = artifacts.get("overrides", {}) or {}
    raw = overrides.get(lesson.id, {}) or {}
    if not isinstance(raw, dict):
        raise ArtifactError(f"artifacts.overrides.{lesson.id} debe ser un objeto YAML.")
    return raw


def effective_artifact_plan(
    profile: Profile, lesson: Lesson, plan: dict[str, Any]
) -> dict[str, Any]:
    declared = plan.get("artifacts", {}) or {}
    if not isinstance(declared, dict):
        declared = {}
    override = profile_override(profile, lesson)

    result = dict(declared)
    # Las decisiones explícitas del perfil tienen prioridad sobre la inferencia del planner.
    for key, value in override.items():
        result[key] = value

    strategy = str(result.get("strategy") or "none")
    if strategy not in VALID_STRATEGIES:
        raise ArtifactError(f"Estrategia de artefactos no válida: {strategy}")
    result["strategy"] = strategy

    if strategy != "none" and not result.get("project_id"):
        result["project_id"] = f"{lesson.id}-{slugify(lesson.title)}"

    result.setdefault("knowledge_dependencies", [])
    result.setdefault("artifact_dependencies", [])
    result.setdefault("required_files", [])
    project_type = result.get("project_type")
    if project_type is not None:
        project_type = str(project_type)
        if project_type not in {"integrator", "diagnostic"}:
            raise ArtifactError(f"project_type no válido: {project_type}")
        result["project_type"] = project_type
    elif strategy == "diagnostic_project":
        result["project_type"] = "diagnostic"
    elif strategy in {"standalone_project", "final_integrator_project"}:
        result["project_type"] = "integrator"
    else:
        result["project_type"] = None

    if strategy == "diagnostic_project" and result["project_type"] != "diagnostic":
        raise ArtifactError("diagnostic_project requiere project_type: diagnostic")

    result.setdefault(
        "validation_required",
        strategy
        in {
            "standalone_project",
            "extends_previous_project",
            "diagnostic_project",
            "final_integrator_project",
        },
    )
    return result


def project_context(state_data: dict[str, Any], output_dir: Path | None = None) -> str:
    projects = state_data.get("projects", {}) or {}
    if not projects:
        return "No hay proyectos ni artefactos acumulados todavía en este bloque."
    enriched: dict[str, Any] = {}
    for project_id, entry in projects.items():
        item = dict(entry) if isinstance(entry, dict) else {"value": entry}
        if output_dir is not None:
            root_value = item.get("root")
            if isinstance(root_value, str):
                root = Path(root_value)
                if not root.is_absolute():
                    root = output_dir / root
                if root.is_dir():
                    item["snapshot"] = artifact_snapshot(
                        root, max_bytes_per_file=50_000
                    )
        enriched[project_id] = item
    return json.dumps(enriched, ensure_ascii=False, indent=2)


def project_root(
    output_dir: Path, lesson: Lesson, artifact_plan: dict[str, Any]
) -> Path | None:
    strategy = artifact_plan.get("strategy", "none")
    if strategy == "none":
        return None
    project_id = str(
        artifact_plan.get("project_id") or f"{lesson.id}-{slugify(lesson.title)}"
    )
    return output_dir / "projects" / slugify(project_id)


def materialize_artifacts(
    output_dir: Path,
    lesson: Lesson,
    artifact_plan: dict[str, Any],
    artifacts: list[dict[str, Any]],
) -> MaterializedArtifacts:
    strategy = str(artifact_plan.get("strategy", "none"))
    project_id = artifact_plan.get("project_id")
    root = project_root(output_dir, lesson, artifact_plan)

    if strategy == "none":
        if artifacts:
            raise ArtifactError(
                "La estrategia 'none' no puede devolver archivos de artefacto."
            )
        return MaterializedArtifacts(strategy, None, None, [])

    if root is None:
        raise ArtifactError("No se pudo determinar el directorio del proyecto.")
    root.mkdir(parents=True, exist_ok=True)

    # standalone_project/final_integrator_project parten de cero en --force o primera creación.
    # No borramos automáticamente aquí para no destruir trabajo previo; el pipeline controla force.
    written: list[Path] = []
    for item in artifacts:
        if not isinstance(item, dict):
            raise ArtifactError("Cada artefacto debe ser un objeto JSON.")
        rel = _safe_relpath(str(item.get("path") or ""))
        content = item.get("content")
        if not isinstance(content, str):
            raise ArtifactError(f"El artefacto {rel} no contiene texto válido.")
        target = (root / rel).resolve()
        if root.resolve() not in target.parents and target != root.resolve():
            raise ArtifactError(f"Ruta fuera del proyecto: {rel}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.rstrip() + "\n", encoding="utf-8")
        written.append(target)

    # Los archivos requeridos se auditan después. No abortamos aquí para dar a REPAIR
    # la oportunidad de corregir omisiones del primer borrador.
    return MaterializedArtifacts(strategy, str(project_id), root, written)


def artifact_snapshot(
    root: Path | None, *, max_bytes_per_file: int = 200_000
) -> list[dict[str, Any]]:
    if root is None or not root.is_dir():
        return []
    result: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "build" in path.parts:
            continue
        rel = path.relative_to(root).as_posix()
        size = path.stat().st_size
        item: dict[str, Any] = {"path": rel, "size": size}
        if size <= max_bytes_per_file:
            try:
                item["content"] = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                item["content"] = "<binary>"
        else:
            item["content"] = f"<omitted: {size} bytes>"
        result.append(item)
    return result


def run_validation(
    profile: Profile, root: Path | None, artifact_plan: dict[str, Any]
) -> dict[str, Any]:
    validation = profile.data.get("validation", {}) or {}
    if root is None or not artifact_plan.get("validation_required", False):
        return {
            "status": "SKIPPED",
            "reason": "validation_not_required",
            "commands": [],
        }
    if not bool(validation.get("enabled", False)):
        return {
            "status": "SKIPPED",
            "reason": "profile_validation_disabled",
            "commands": [],
        }

    commands = validation.get("commands", []) or []
    results: list[dict[str, Any]] = []
    overall = "PASS"
    timeout = int(validation.get("timeout_seconds", 120))

    for command in commands:
        if isinstance(command, str):
            import shlex

            argv = shlex.split(command)
        elif isinstance(command, list) and all(isinstance(x, str) for x in command):
            argv = command
        else:
            results.append({"command": command, "status": "INVALID"})
            overall = "FAIL"
            continue
        if not argv:
            continue
        if shutil.which(argv[0]) is None:
            results.append(
                {"command": argv, "status": "SKIPPED", "reason": "command_not_found"}
            )
            if bool(validation.get("require_tools", False)):
                overall = "FAIL"
            continue
        proc = subprocess.run(
            argv,
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        result = {
            "command": argv,
            "returncode": proc.returncode,
            "status": "PASS" if proc.returncode == 0 else "FAIL",
            "output": proc.stdout[-12000:],
        }
        results.append(result)
        if proc.returncode != 0:
            overall = "FAIL"
            if bool(validation.get("stop_on_failure", True)):
                break
    return {"status": overall, "commands": results}
