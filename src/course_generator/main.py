from __future__ import annotations

import argparse
from pathlib import Path

from .config_loader import load_profile, load_prompt
from .output import write_index, write_manifest, zip_block
from .parser import neighbors, parse_lessons
from .state import ProjectRegistry, StateStore


def project_root() -> Path:
    # src/course_generator/main.py -> project root
    return Path(__file__).resolve().parents[2]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="course-generator",
        description="Genera cursos técnicos profundos lección por lección.",
    )
    p.add_argument("path", type=Path, help="Archivo bloque-X.txt")
    p.add_argument(
        "--profile",
        required=True,
        help="Nombre del perfil definido en profiles/<nombre>/",
    )
    p.add_argument("--lesson", help="Generar sólo una lección, p. ej. 1.7")
    p.add_argument(
        "--resume", action="store_true", help="Continúa omitiendo lecciones completas"
    )
    p.add_argument(
        "--force", action="store_true", help="Regenera incluso si ya está completa"
    )
    p.add_argument(
        "--dry-run", action="store_true", help="Valida todo sin llamar a la API"
    )
    p.add_argument("--no-zip", action="store_true", help="No comprimir al finalizar")
    p.add_argument(
        "--root", type=Path, help="Raíz del proyecto (normalmente autodetectada)"
    )
    return p


def main() -> None:
    args = build_parser().parse_args()
    root = (args.root or project_root()).resolve()
    source = args.path.resolve()

    profile = load_profile(root, args.profile)
    lessons = parse_lessons(source)
    selected = lessons
    if args.lesson:
        selected = [l for l in lessons if l.id == args.lesson]
        if not selected:
            raise SystemExit(f"No existe la lección {args.lesson} en {source.name}.")

    templates = {
        name: load_prompt(root, name)
        for name in ("planner", "teacher", "auditor", "repair")
    }
    block = selected[0].block
    output_dir = root / "output" / profile.name / f"bloque-{block}"
    state_path = root / "state" / profile.name / f"bloque-{block}.json"

    print(f"Perfil : {profile.name} — {profile.title}")
    print(f"PATH   : {source}")
    print(f"Bloque : {block}")
    print(f"Lecciones seleccionadas: {len(selected)}")

    if args.dry_run:
        print("\nDRY RUN: configuración válida; no se llamará a la API.")
        overrides = (profile.data.get("artifacts") or {}).get("overrides") or {}
        for lesson in selected:
            idx = lessons.index(lesson)
            print(f"  {lesson.id:>6}  {lesson.title}")
            print(
                f"          vecinos: {neighbors(lessons, idx).replace(chr(10), ' | ')}"
            )
            ov = overrides.get(lesson.id) or {}
            if ov:
                print(
                    f"          artefactos: {ov.get('strategy')} / {ov.get('project_id')}"
                )
        return

    from .openai_client import CourseOpenAI
    from .pipeline import process_lesson
    from .stages import PipelineStages

    state = StateStore(state_path, profile.name, str(source))
    registry = ProjectRegistry(
        root / "state" / profile.name / "projects.json", profile.name
    )
    client = CourseOpenAI()
    stages = PipelineStages(client, templates)

    for lesson in selected:
        idx = lessons.index(lesson)
        process_lesson(
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors(lessons, idx),
            stages=stages,
            state=state,
            registry=registry,
            output_dir=output_dir,
            force=args.force,
        )

    write_index(output_dir, profile, lessons)
    write_manifest(output_dir, profile, lessons)

    output_cfg = profile.data.get("output", {})
    should_zip = bool(output_cfg.get("zip_block", True)) and not args.no_zip
    if should_zip:
        target = zip_block(
            output_dir,
            root / "dist" / profile.name,
            f"{profile.name}-bloque-{block}",
        )
        print(f"\nZIP: {target}")
    print("Finalizado.")


if __name__ == "__main__":
    main()
