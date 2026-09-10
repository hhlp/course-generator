from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from .models import Lesson, Profile
from .openai_client import CourseOpenAI, StructuredResult


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


@dataclass(slots=True)
class PipelineStages:
    client: CourseOpenAI
    templates: dict[str, str]

    def _call(self, name: str, payload: dict[str, Any]) -> StructuredResult:
        template = self.templates.get(name)
        if not template:
            raise ValueError(f"No existe template para la etapa {name!r}.")
        return self.client.json_call(
            instructions=template,
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

    def planner(
        self,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        context: str,
    ) -> StructuredResult:
        payload = self._base(profile, lesson, neighbors_text, context)
        payload["required_output"] = {
            "type": "object",
            "description": "Plan de la lección.",
            "must_include": ["artifacts"],
        }
        return self._call("planner", payload)

    def teacher(
        self,
        profile: Profile,
        lesson: Lesson,
        neighbors_text: str,
        plan: dict[str, Any],
        context: str,
    ) -> StructuredResult:
        payload = self._base(profile, lesson, neighbors_text, context)
        payload["plan"] = plan
        payload["required_output"] = {
            "markdown": "Lección completa en Markdown.",
            "artifacts": [
                {"path": "ruta/relativa", "content": "contenido completo del archivo"}
            ],
        }
        return self._call("teacher", payload)

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
        payload = self._base(profile, lesson, neighbors_text, context)
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
        return self._call("auditor", payload)

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
        payload = self._base(profile, lesson, neighbors_text, context)
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
        return self._call("repair", payload)
