from __future__ import annotations

import json
import re
import shutil
from collections.abc import Iterable
from pathlib import Path

from .models import Lesson, Profile


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = (
        text.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ü", "u")
        .replace("ñ", "n")
    )
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "lesson"


def lesson_filename(lesson: Lesson) -> str:
    return f"{lesson.id}-{slugify(lesson.title)}.md"


def save_lesson(output_dir: Path, lesson: Lesson, markdown: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / lesson_filename(lesson)
    path.write_text(markdown.rstrip() + "\n", encoding="utf-8")
    return path


def write_index(output_dir: Path, profile: Profile, lessons: Iterable[Lesson]) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    lessons = list(lessons)

    lines = [
        f"# {profile.title}",
        "",
        f"Perfil: `{profile.name}`",
        "",
        "## Lecciones",
        "",
    ]

    for lesson in lessons:
        filename = lesson_filename(lesson)
        status = "✓" if (output_dir / filename).is_file() else "○"
        lines.append(f"- {status} [{lesson.id} — {lesson.title}]({filename})")

    path = output_dir / "README.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def write_manifest(
    output_dir: Path, profile: Profile, lessons: Iterable[Lesson]
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    lessons = list(lessons)
    payload = {
        "profile": profile.name,
        "title": profile.title,
        "lessons": [
            {
                "id": lesson.id,
                "title": lesson.title,
                "file": lesson_filename(lesson),
                "generated": (output_dir / lesson_filename(lesson)).is_file(),
            }
            for lesson in lessons
        ],
    }
    path = output_dir / "manifest.json"
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def zip_block(output_dir: Path, dist_dir: Path, archive_name: str) -> Path:
    if not output_dir.is_dir():
        raise FileNotFoundError(f"No existe el directorio de salida: {output_dir}")
    dist_dir.mkdir(parents=True, exist_ok=True)
    base = dist_dir / archive_name
    archive = shutil.make_archive(
        str(base),
        "zip",
        root_dir=output_dir.parent,
        base_dir=output_dir.name,
    )
    return Path(archive)
