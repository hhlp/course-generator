from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .models import Lesson

LESSON_RE = re.compile(r"^\s*(?P<id>\d+(?:\.\d+)+)\s*(?:[-—–:]\s*)?(?P<title>.+?)\s*$")
BLOCK_RE = re.compile(r"^\s*(?P<block>\d+)\.\s+(?P<title>.+?)\s*$")


@dataclass(slots=True)
class PathBlock:
    number: int
    lines: list[str]


class PathParseError(ValueError):
    pass


def parse_lessons(path: Path, *, require_single_block: bool = True) -> list[Lesson]:
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
        raise PathParseError(
            f"No se encontraron lecciones con formato X.Y[.Z...] en {path}"
        )

    blocks = {lesson.block for lesson in lessons}
    if require_single_block and len(blocks) != 1:
        raise PathParseError(
            f"{path} contiene múltiples bloques ({', '.join(sorted(blocks))}); "
            "cada archivo bloque-X.txt debe contener un único bloque para generación."
        )

    return lessons


def parse_blocks(path: Path) -> list[PathBlock]:
    """Parsea un PATH maestro conservando cada bloque completo."""
    if not path.is_file():
        raise PathParseError(f"No existe el PATH: {path}")

    blocks: list[PathBlock] = []
    current: PathBlock | None = None
    seen_blocks: set[int] = set()

    for lineno, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw.rstrip()
        block_match = BLOCK_RE.match(line)
        lesson_match = LESSON_RE.match(line.strip())

        if block_match and not lesson_match:
            block_number = int(block_match.group("block"))
            if block_number in seen_blocks:
                raise PathParseError(
                    f"{path}:{lineno}: bloque duplicado: {block_number}"
                )
            current = PathBlock(number=block_number, lines=[line])
            blocks.append(current)
            seen_blocks.add(block_number)
            continue

        if lesson_match:
            lesson_block = int(lesson_match.group("id").split(".", 1)[0])
            if current is None:
                raise PathParseError(
                    f"{path}:{lineno}: la lección {lesson_match.group('id')} "
                    "aparece antes de cualquier cabecera de bloque."
                )
            if lesson_block != current.number:
                raise PathParseError(
                    f"{path}:{lineno}: la lección {lesson_match.group('id')} "
                    f"pertenece al bloque {lesson_block}, pero la cabecera activa "
                    f"es {current.number}."
                )
            current.lines.append(line)
            continue

        if current is not None:
            current.lines.append(line)
        elif line.strip():
            raise PathParseError(
                f"{path}:{lineno}: contenido antes del primer bloque: {line!r}"
            )

    if not blocks:
        raise PathParseError(f"No se encontraron cabeceras de bloque X. en {path}")

    numbers = [block.number for block in blocks]
    expected = list(range(numbers[0], numbers[-1] + 1))
    if numbers != expected:
        missing = sorted(set(expected) - set(numbers))
        raise PathParseError(
            "La numeración de bloques no es continua. "
            f"Encontrados: {numbers}; faltan: {missing}"
        )

    return blocks


def validate_block_lessons(block: PathBlock) -> None:
    """Comprueba numeración jerárquica continua entre hermanos.

    Admite X.Y, X.Y.Z, X.Y.Z.W, ... y valida cada nivel
    independientemente. Por ejemplo, 7.13, 7.14, 7.14.1,
    7.14.2, 7.15 es válido.
    """
    lesson_ids: list[tuple[int, ...]] = []

    for line in block.lines:
        match = LESSON_RE.match(line.strip())
        if not match:
            continue

        parts = tuple(int(part) for part in match.group("id").split("."))
        if parts[0] == block.number:
            lesson_ids.append(parts)

    if not lesson_ids:
        raise PathParseError(f"El bloque {block.number} no contiene lecciones.")

    siblings: dict[tuple[int, ...], list[int]] = {}
    for parts in lesson_ids:
        parent = parts[:-1]
        siblings.setdefault(parent, []).append(parts[-1])

    for parent, numbers in siblings.items():
        expected = list(range(1, numbers[-1] + 1))
        if numbers != expected:
            parent_id = ".".join(str(part) for part in parent)
            raise PathParseError(
                f"Bloque {block.number}: numeración no continua bajo {parent_id}. "
                f"Encontrada: {numbers}; esperada: {expected}"
            )


def render_block(block: PathBlock) -> str:
    """Serializa un bloque eliminando sólo líneas vacías finales."""
    lines = block.lines[:]
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) + "\n"


def split_initial(
    source: Path,
    output_dir: Path,
    *,
    check_lessons: bool = False,
    dry_run: bool = False,
    force: bool = False,
) -> list[Path]:
    """Separa initial.txt en bloque-X.txt y devuelve los destinos."""
    blocks = parse_blocks(source)

    if check_lessons:
        for block in blocks:
            validate_block_lessons(block)

    targets = [output_dir / f"bloque-{block.number}.txt" for block in blocks]
    conflicts = [target for target in targets if target.exists()]

    if conflicts and not force and not dry_run:
        formatted = "\n".join(f"  - {path}" for path in conflicts)
        raise PathParseError(
            "Ya existen archivos de bloque. Usa --force para sobrescribirlos:\n"
            f"{formatted}"
        )

    print(f"Source : {source}")
    print(f"Output : {output_dir}")
    print(f"Blocks : {len(blocks)}")
    print()

    for block, target in zip(blocks, targets, strict=True):
        lesson_count = sum(1 for line in block.lines if LESSON_RE.match(line.strip()))
        action = "WOULD WRITE" if dry_run else "WRITE"
        print(f"{action:11} {target.name} ({lesson_count} lecciones)")

    if dry_run:
        print("\nDRY RUN: no se escribió ningún archivo.")
        return targets

    output_dir.mkdir(parents=True, exist_ok=True)
    for block, target in zip(blocks, targets, strict=True):
        target.write_text(render_block(block), encoding="utf-8")

    print(f"\nOK: {len(blocks)} bloques generados.")
    return targets


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
