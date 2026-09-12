from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from .config_loader import resolve_profile_file
from .models import Lesson, Profile
from .stages import PipelineStages, render_stage_instructions


def context_checks(profile: Profile, templates: dict[str, str]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    files = profile.data.get("files") or {}
    if not isinstance(files, dict):
        files = {}

    for key in ("pedagogy", "domain", "bibliography"):
        configured = files.get(key)
        if not isinstance(configured, str) or not configured.strip():
            checks.append({"name": key, "status": "MISSING", "path": None})
            continue
        path = resolve_profile_file(profile, configured)
        checks.append(
            {
                "name": key,
                "status": "OK"
                if path.is_file() and path.stat().st_size > 0
                else "MISSING",
                "path": str(path),
            }
        )

    for name in ("planner", "teacher", "auditor", "repair"):
        checks.append(
            {
                "name": f"prompt:{name}",
                "status": "OK" if templates.get(name, "").strip() else "MISSING",
                "path": None,
            }
        )
    return checks


def planner_preview(
    profile: Profile,
    lesson: Lesson,
    neighbors_text: str,
    templates: dict[str, str],
    prompt_context: dict[str, str],
    context: str,
) -> dict[str, Any]:
    payload = PipelineStages.planner_payload(profile, lesson, neighbors_text, context)
    instructions = render_stage_instructions(
        templates["planner"],
        prompt_context=prompt_context,
        profile=profile,
        lesson=lesson,
        neighbors_text=neighbors_text,
        context=context,
    )
    return {
        "stage": "planner",
        "instructions": instructions,
        "input": json.dumps(payload, ensure_ascii=False, indent=2),
        "payload": payload,
    }


def inspection_data(
    *,
    profile: Profile,
    source: Path,
    lessons_count: int,
    lesson: Lesson,
    neighbors_text: str,
    templates: dict[str, str],
    prompt_context: dict[str, str],
    context: str,
    neighbor_radius: int,
) -> dict[str, Any]:
    load_dotenv()
    preview = planner_preview(
        profile,
        lesson,
        neighbors_text,
        templates,
        prompt_context,
        context,
    )
    return {
        "profile": {
            "name": profile.name,
            "title": profile.title,
            "source": str(profile.path),
        },
        "path": str(source),
        "lessons": lessons_count,
        "lesson": {
            "id": lesson.id,
            "title": lesson.title,
            "block": lesson.block,
        },
        "neighbors": {
            "radius": neighbor_radius,
            "text": neighbors_text,
        },
        "context_checks": context_checks(profile, templates),
        "context_sizes": {key: len(value) for key, value in prompt_context.items()},
        "openai": {
            "model": os.getenv("OPENAI_MODEL", "gpt-6-astra"),
            "reasoning_effort": os.getenv("OPENAI_REASONING_EFFORT", "high"),
            "max_output_tokens": os.getenv("OPENAI_MAX_OUTPUT_TOKENS", "50000"),
            "store": os.getenv("OPENAI_STORE_RESPONSES", "false"),
        },
        "stages": {
            "planner": {"status": "MATERIALIZED"},
            "teacher": {
                "status": "NOT MATERIALIZED",
                "reason": "requires planner output",
            },
            "auditor": {
                "status": "NOT MATERIALIZED",
                "reason": "requires teacher output and validation",
            },
            "repair": {
                "status": "NOT MATERIALIZED",
                "reason": "requires audit failure",
            },
        },
        "planner": preview,
    }


def render_inspection(data: dict[str, Any]) -> str:
    lines = [
        "INSPECTION",
        "=" * 72,
        f"Profile : {data['profile']['name']} — {data['profile']['title']}",
        f"Source  : {data['profile']['source']}",
        f"PATH    : {data['path']}",
        f"Lessons : {data['lessons']}",
        f"Lesson  : {data['lesson']['id']} — {data['lesson']['title']}",
        f"Block   : {data['lesson']['block']}",
        f"Radius  : {data['neighbors']['radius']}",
        "",
        "CONTEXT",
    ]
    for check in data["context_checks"]:
        suffix = f" — {check['path']}" if check["path"] else ""
        size = ""
        if check["name"] in data.get("context_sizes", {}):
            size = f" ({data['context_sizes'][check['name']]} chars)"
        lines.append(f"  {check['status']:<7} {check['name']}{size}{suffix}")

    lines.extend(
        [
            "",
            "OPENAI",
            f"  model             = {data['openai']['model']}",
            f"  reasoning_effort  = {data['openai']['reasoning_effort']}",
            f"  max_output_tokens = {data['openai']['max_output_tokens']}",
            f"  store             = {data['openai']['store']}",
            "",
            "STAGES",
        ]
    )
    for name, stage in data["stages"].items():
        reason = f" — {stage['reason']}" if "reason" in stage else ""
        lines.append(f"  {name:<8} {stage['status']}{reason}")
    return "\n".join(lines) + "\n"


def render_prompt(preview: dict[str, Any]) -> str:
    return (
        "PLANNER — INSTRUCTIONS\n"
        + "=" * 72
        + "\n"
        + preview["instructions"]
        + "\n\nPLANNER — INPUT\n"
        + "=" * 72
        + "\n"
        + preview["input"]
        + "\n"
    )
