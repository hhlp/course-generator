from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Any

from .artifacts import (
    artifact_snapshot,
    effective_artifact_plan,
    materialize_artifacts,
    project_context,
    project_root,
    run_validation,
)
from .models import Lesson, Profile
from .output import save_lesson
from .stages import PipelineStages
from .state import ProjectRegistry, StateStore


def audit_passed(audit: dict[str, Any]) -> bool:
    for key in ("verdict", "status", "result"):
        value = audit.get(key)
        if isinstance(value, str):
            return value.strip().upper() == "PASS"
    value = audit.get("pass")
    if isinstance(value, bool):
        return value
    raise ValueError("El auditor no devolvió un veredicto PASS/FAIL reconocible.")


def _teacher_payload(data: dict[str, Any] | None) -> tuple[str, list[dict[str, Any]]]:
    if not isinstance(data, dict):
        raise TypeError("Teacher no devolvió un objeto JSON válido.")
    markdown = data.get("markdown")
    artifacts = data.get("artifacts", [])
    if not isinstance(markdown, str) or not markdown.strip():
        raise ValueError("Teacher no devolvió 'markdown' válido.")
    if not isinstance(artifacts, list):
        raise TypeError("Teacher no devolvió 'artifacts' como array.")
    return markdown.strip(), artifacts


def _prepare_staging(
    output_dir: Path,
    lesson: Lesson,
    artifact_plan: dict[str, Any],
    registry: ProjectRegistry,
) -> tuple[Path, Path | None, Path | None]:
    stage_output = output_dir / ".staging" / lesson.id
    if stage_output.exists():
        shutil.rmtree(stage_output)
    stage_output.mkdir(parents=True, exist_ok=True)

    final_root = project_root(output_dir, lesson, artifact_plan)
    stage_root = project_root(stage_output, lesson, artifact_plan)
    strategy = artifact_plan.get("strategy", "none")

    if strategy == "extends_previous_project":
        project_id = str(artifact_plan.get("project_id") or "")
        registered = registry.project(project_id) if project_id else None
        if registered and isinstance(registered.get("root"), str):
            final_root = Path(registered["root"])
        if final_root is None or not final_root.is_dir():
            raise RuntimeError(
                f"{lesson.id}: extends_previous_project requiere un proyecto registrado existente: {project_id}"
            )
        assert stage_root is not None
        stage_root.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(final_root, stage_root)
    return stage_output, stage_root, final_root


def _commit_project(stage_root: Path | None, final_root: Path | None) -> None:
    if stage_root is None or final_root is None:
        return
    final_root.parent.mkdir(parents=True, exist_ok=True)
    backup = final_root.with_name(final_root.name + ".backup")
    if backup.exists():
        shutil.rmtree(backup)
    if final_root.exists():
        final_root.replace(backup)
    try:
        shutil.copytree(stage_root, final_root)
    except Exception:
        if final_root.exists():
            shutil.rmtree(final_root)
        if backup.exists():
            backup.replace(final_root)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def process_lesson(
    *,
    profile: Profile,
    lesson: Lesson,
    neighbors_text: str,
    stages: PipelineStages,
    state: StateStore,
    registry: ProjectRegistry,
    output_dir: Path,
    force: bool = False,
) -> Path:
    existing_status = state.status(lesson.id)
    if existing_status == "complete" and not force:
        expected = next(output_dir.glob(f"{lesson.id}-*.md"), None)
        if expected and expected.is_file():
            print(f"  ↳ {lesson.id}: ya completada; se omite.")
            return expected

    context = project_context(registry.data)
    state.update(lesson.id, status="planning", title=lesson.title)
    print(f"  1/5 planner   {lesson.id} — {lesson.title}")
    plan_out = stages.planner(profile, lesson, neighbors_text, context)
    plan = plan_out.data or {}
    artifact_plan = effective_artifact_plan(profile, lesson, plan)
    plan["artifacts"] = artifact_plan
    state.update(
        lesson.id,
        status="planned",
        plan=plan,
        planner_response_id=plan_out.raw.response_id,
        planner_usage=plan_out.raw.usage,
    )

    print(f"  2/5 teacher   {lesson.id} [{artifact_plan['strategy']}]")
    teacher_out = stages.teacher(profile, lesson, neighbors_text, plan, context)
    markdown, generated_artifacts = _teacher_payload(teacher_out.data)
    state.update(
        lesson.id,
        status="generated",
        teacher_response_id=teacher_out.raw.response_id,
        teacher_usage=teacher_out.raw.usage,
        artifact_strategy=artifact_plan["strategy"],
        project_id=artifact_plan.get("project_id"),
    )

    stage_output, stage_root, final_root = _prepare_staging(
        output_dir, lesson, artifact_plan, registry
    )
    materialize_artifacts(stage_output, lesson, artifact_plan, generated_artifacts)

    max_repairs = int(os.getenv("OPENAI_MAX_REPAIRS", "2"))
    for attempt in range(max_repairs + 1):
        snapshot = artifact_snapshot(stage_root)
        validation = run_validation(profile, stage_root, artifact_plan)
        print(f"  3/5 validate  {lesson.id}: {validation.get('status')}")

        print(f"  4/5 auditor   {lesson.id} (intento {attempt + 1})")
        audit_out = stages.auditor(
            profile,
            lesson,
            neighbors_text,
            plan,
            markdown,
            snapshot,
            validation,
            context,
        )
        audit = audit_out.data or {}
        state.update(
            lesson.id,
            status="audited",
            audit=audit,
            validation=validation,
            auditor_response_id=audit_out.raw.response_id,
            auditor_usage=audit_out.raw.usage,
            repair_attempts=attempt,
        )
        if audit_passed(audit):
            _commit_project(stage_root, final_root)
            path = save_lesson(output_dir, lesson, markdown)
            project_id = artifact_plan.get("project_id")
            if project_id and final_root is not None:
                final_snapshot = artifact_snapshot(final_root, max_bytes_per_file=0)
                registry.update(
                    str(project_id),
                    strategy=artifact_plan["strategy"],
                    project_type=artifact_plan.get("project_type"),
                    introduced_or_updated_by=lesson.id,
                    root=str(final_root),
                    knowledge_dependencies=artifact_plan.get(
                        "knowledge_dependencies", []
                    ),
                    artifact_dependencies=artifact_plan.get(
                        "artifact_dependencies", []
                    ),
                    files=[x["path"] for x in final_snapshot],
                )
            state.update(lesson.id, status="complete", file=str(path))
            if stage_output.exists():
                shutil.rmtree(stage_output)
            print(f"  ✓ PASS        {path.name}")
            return path

        if attempt >= max_repairs:
            state.update(lesson.id, status="failed", audit=audit)
            raise RuntimeError(
                f"{lesson.id} no superó la auditoría tras {max_repairs} reparaciones. "
                f"Staging conservado en {stage_output}"
            )

        print(f"  5/5 repair    {lesson.id} (reparación {attempt + 1})")
        repair_out = stages.repair(
            profile,
            lesson,
            neighbors_text,
            plan,
            markdown,
            snapshot,
            validation,
            audit,
            context,
        )
        markdown, repaired_artifacts = _teacher_payload(repair_out.data)
        materialize_artifacts(stage_output, lesson, artifact_plan, repaired_artifacts)
        state.update(
            lesson.id,
            status="repaired",
            repair_response_id=repair_out.raw.response_id,
            repair_usage=repair_out.raw.usage,
            repair_attempts=attempt + 1,
        )

    raise AssertionError("flujo inalcanzable")
