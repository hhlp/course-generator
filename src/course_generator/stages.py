from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from .models import Lesson, Profile

if TYPE_CHECKING:
    from .openai_client import CourseOpenAI, StructuredResult


_PLACEHOLDER_RE = re.compile(r"\{\{([A-Z_]+)\}\}")


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


def _render_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)

    unresolved = sorted(set(_PLACEHOLDER_RE.findall(rendered)))
    if unresolved:
        joined = ", ".join(unresolved)
        raise ValueError(f"Prompt con placeholders sin resolver: {joined}")
    return rendered


def render_stage_instructions(
    template: str,
    *,
    prompt_context: dict[str, str],
    profile: Profile,
    lesson: Lesson,
    neighbors_text: str,
    context: str,
    extra: dict[str, str] | None = None,
) -> str:
    values = {
        "PEDAGOGY": prompt_context["pedagogy"],
        "PROFILE": _json(
            {
                "name": profile.name,
                "title": profile.title,
                "config": profile.data,
            }
        ),
        "DOMAIN": prompt_context["domain"],
        "BIBLIOGRAPHY": prompt_context["bibliography"],
        "LESSON_ID": lesson.id,
        "LESSON_TITLE": lesson.title,
        "NEIGHBORS": neighbors_text,
        "PROJECT_CONTEXT": context,
    }
    if extra:
        values.update(extra)
    return _render_template(template, values)


@dataclass(slots=True)
class PipelineStages:
    client: CourseOpenAI
    templates: dict[str, str]
    prompt_context: dict[str, str]

    def render_instructions(
        self,
        name: str,
        *,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        context: str,
        extra: dict[str, str] | None = None,
    ) -> str:
        template = self.templates.get(name)
        if not template:
            raise ValueError(f"No existe template para la etapa {name!r}.")
        return render_stage_instructions(
            template,
            prompt_context=self.prompt_context,
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors_text,
            context=context,
            extra=extra,
        )

    def _call(
        self,
        name: str,
        payload: dict[str, Any],
        *,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        context: str,
        extra: dict[str, str] | None = None,
    ) -> StructuredResult:
        instructions = self.render_instructions(
            name,
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors_text,
            context=context,
            extra=extra,
        )
        return self.client.json_call(
            instructions=instructions,
            input_text=_json(payload),
        )

    @staticmethod
    def _base(
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        context: str,
    ) -> dict[str, Any]:
        return {
            "profile": {
                "name": profile.name,
                "title": profile.title,
                "config": profile.data,
            },
            "lesson": {
                "id": lesson.id,
                "title": lesson.title,
                "block": lesson.block,
            },
            "neighbors": neighbors_text,
            "project_context": context,
        }

    @classmethod
    def planner_payload(
        cls,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        context: str,
    ) -> dict[str, Any]:
        payload = cls._base(profile, lesson, neighbors_text, context)
        payload["required_output"] = {
            "type": "object",
            "description": "Plan de la lección.",
            "must_include": ["artifacts"],
        }
        return payload

    @classmethod
    def teacher_payload(
        cls,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        context: str,
    ) -> dict[str, Any]:
        payload = cls._base(profile, lesson, neighbors_text, context)
        payload["plan"] = plan
        payload["required_output"] = {
            "markdown": "Lección completa en Markdown.",
            "artifacts": [
                {"path": "ruta/relativa", "content": "contenido completo del archivo"}
            ],
        }
        return payload

    @classmethod
    def auditor_payload(
        cls,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        markdown: str,
        snapshot: list[dict[str, Any]],
        validation: dict[str, Any],
        context: str,
    ) -> dict[str, Any]:
        payload = cls._base(profile, lesson, neighbors_text, context)
        payload.update(
            {
                "plan": plan,
                "markdown": markdown,
                "artifact_snapshot": snapshot,
                "validation": validation,
                "required_output": {
                    "verdict": "PASS o FAIL",
                    "issues": [],
                },
            }
        )
        return payload

    @classmethod
    def repair_payload(
        cls,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        markdown: str,
        snapshot: list[dict[str, Any]],
        validation: dict[str, Any],
        audit: dict[str, Any],
        context: str,
    ) -> dict[str, Any]:
        payload = cls._base(profile, lesson, neighbors_text, context)
        payload.update(
            {
                "plan": plan,
                "markdown": markdown,
                "artifact_snapshot": snapshot,
                "validation": validation,
                "audit": audit,
                "required_output": {
                    "markdown": "Lección completa reparada en Markdown.",
                    "artifacts": [
                        {
                            "path": "ruta/relativa",
                            "content": "contenido completo reparado",
                        }
                    ],
                },
            }
        )
        return payload

    def planner(
        self,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        context: str,
    ) -> StructuredResult:
        payload = self.planner_payload(profile, lesson, neighbors_text, context)
        return self._call(
            "planner",
            payload,
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors_text,
            context=context,
        )

    def teacher(
        self,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        context: str,
    ) -> StructuredResult:
        payload = self.teacher_payload(profile, lesson, neighbors_text, plan, context)
        return self._call(
            "teacher",
            payload,
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors_text,
            context=context,
            extra={"PLAN_JSON": _json(plan)},
        )

    def auditor(
        self,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        markdown: str,
        snapshot: list[dict[str, Any]],
        validation: dict[str, Any],
        context: str,
    ) -> StructuredResult:
        payload = self.auditor_payload(
            profile,
            lesson,
            neighbors_text,
            plan,
            markdown,
            snapshot,
            validation,
            context,
        )
        return self._call(
            "auditor",
            payload,
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors_text,
            context=context,
            extra={
                "PLAN_JSON": _json(plan),
                "LESSON_MARKDOWN": markdown,
                "ARTIFACTS_JSON": _json(snapshot),
                "VALIDATION_JSON": _json(validation),
            },
        )

    def repair(
        self,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        markdown: str,
        snapshot: list[dict[str, Any]],
        validation: dict[str, Any],
        audit: dict[str, Any],
        context: str,
    ) -> StructuredResult:
        payload = self.repair_payload(
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
        return self._call(
            "repair",
            payload,
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors_text,
            context=context,
            extra={
                "PLAN_JSON": _json(plan),
                "LESSON_MARKDOWN": markdown,
                "ARTIFACTS_JSON": _json(snapshot),
                "VALIDATION_JSON": _json(validation),
                "AUDIT_JSON": _json(audit),
            },
        )
