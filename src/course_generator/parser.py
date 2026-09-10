from __future__ import annotations

import re
from pathlib import Path

from .models import Lesson

LESSON_RE = re.compile(r"^\s*(?P<id>\d+\.\d+)\s*(?:[-—–:]\s*)?(?P<title>.+?)\s*$")


class PathParseError(ValueError):
    pass


def parse_lessons(path: Path) -> list[Lesson]:
    if not path.is_file():
        raise PathParseError(f"No existe el PATH: {path}")

    lessons: list[Lesson] = []
    seen: set[str] = set()

    for lineno, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw.strip()
        if not line:
            continue

        # Elimina decoración típica de árboles.
        cleaned = re.sub(r"^[│├└─\s]+", "", line).strip()
        match = LESSON_RE.match(cleaned)
        if not match:
            continue

        lesson_id = match.group("id")
        title = match.group("title").strip()
        if not title:
            raise PathParseError(f"{path}:{lineno}: lección sin título: {raw!r}")

        if lesson_id in seen:
            raise PathParseError(f"{path}:{lineno}: lección duplicada: {lesson_id}")

        block = lesson_id.split(".", 1)[0]
        lessons.append(Lesson(id=lesson_id, title=title, block=block, raw=raw))
        seen.add(lesson_id)

    if not lessons:
        raise PathParseError(f"No se encontraron lecciones con formato X.Y en {path}")

    blocks = {lesson.block for lesson in lessons}
    if len(blocks) != 1:
        raise PathParseError(
            f"{path} contiene múltiples bloques ({', '.join(sorted(blocks))}); "
            "cada archivo bloque-X.txt debe contener un único bloque."
        )

    return lessons


def neighbors(lessons: list[Lesson], index: int, radius: int = 2) -> str:
    if not 0 <= index < len(lessons):
        raise IndexError(index)

    lines: list[str] = []

    start = max(0, index - radius)
    end = min(len(lessons), index + radius + 1)

    for i in range(start, end):
        lesson = lessons[i]
        marker = "ACTUAL" if i == index else ("ANTERIOR" if i < index else "SIGUIENTE")
        lines.append(f"{marker}: {lesson.id} — {lesson.title}")

    return "\n".join(lines)
