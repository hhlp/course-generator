from __future__ import annotations

import argparse
import json
from pathlib import Path

from .artifacts import project_context
from .config_loader import load_profile, load_profile_context, load_prompt
from .inspection import inspection_data, render_inspection, render_prompt
from .openai_client import OpenAIRequestError
from .output import write_index, write_manifest, zip_block
from .parser import PathParseError, neighbors, parse_lessons, split_initial
from .stages import PipelineStages
from .state import ProjectRegistry, StateStore


def project_root() -> Path:
    # src/course_generator/main.py -> project root
    return Path(__file__).resolve().parents[2]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="course-generator",
        description="Genera cursos técnicos profundos lección por lección.",
    )
    p.add_argument("path", type=Path, help="Archivo PATH/bloque-X.txt")
    p.add_argument(
        "--profile",
        required=True,
        help="Nombre del perfil definido en profiles/<nombre>/",
    )
    p.add_argument("--lesson", help="Generar sólo una lección, p. ej. 1.7 o 1.7.2")
    p.add_argument(
        "--resume", action="store_true", help="Continúa omitiendo lecciones completas"
    )
    p.add_argument(
        "--force", action="store_true", help="Regenera incluso si ya está completa"
    )
    p.add_argument(
        "--dry-run", action="store_true", help="Valida todo sin llamar a la API"
    )
    p.add_argument(
        "--show-prompt",
        action="store_true",
        help="Muestra instructions e input exactos del planner",
    )
    p.add_argument(
        "--inspect",
        action="store_true",
        help="Muestra cómo se ha resuelto el contexto y las etapas",
    )
    p.add_argument(
        "--save-prompt",
        type=Path,
        metavar="FILE",
        help="Guarda el prompt materializado del planner",
    )
    p.add_argument(
        "--save-inspect",
        type=Path,
        metavar="FILE",
        help="Guarda el informe de inspección",
    )
    p.add_argument(
        "--dump-json",
        action="store_true",
        help="Muestra el payload JSON estructurado del planner",
    )
    p.add_argument(
        "--validate-context",
        action="store_true",
        help="Falla si falta un archivo de contexto o prompt requerido",
    )
    p.add_argument(
        "--neighbor-radius",
        type=int,
        default=2,
        metavar="N",
        help="Número de lecciones vecinas por lado (default: 2)",
    )
    p.add_argument(
        "--split-blocks",
        action="store_true",
        help="Separa initial.txt en bloque-X.txt",
    )
    p.add_argument(
        "--check-lessons",
        action="store_true",
        help="Comprueba numeración jerárquica continua X.Y[.Z...] al separar bloques",
    )
    p.add_argument("--no-zip", action="store_true", help="No comprimir al finalizar")
    p.add_argument(
        "--root", type=Path, help="Raíz del proyecto (normalmente autodetectada)"
    )
    return p


def _write_text(path: Path, text: str) -> None:
    path = path.expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"Guardado: {path}")


def _main() -> None:
    args = build_parser().parse_args()
    if args.neighbor_radius < 0:
        raise SystemExit("--neighbor-radius debe ser >= 0.")

    root = (args.root or project_root()).resolve()
    source = args.path.resolve()

    profile = load_profile(root, args.profile)

    if args.check_lessons and not args.split_blocks:
        raise SystemExit("--check-lessons requiere --split-blocks.")

    if args.split_blocks:
        split_initial(
            source,
            source.parent,
            check_lessons=args.check_lessons,
            dry_run=args.dry_run,
            force=args.force,
        )
        return

    lessons = parse_lessons(source, require_single_block=not args.dry_run)
    selected = lessons
    if args.lesson:
        selected = [lesson for lesson in lessons if lesson.id == args.lesson]
        if not selected:
            raise SystemExit(f"No existe la lección {args.lesson} en {source.name}.")

    templates = {
        name: load_prompt(root, name)
        for name in ("planner", "teacher", "auditor", "repair")
    }
    prompt_context = load_profile_context(profile, strict=not args.dry_run)

    block = selected[0].block
    output_dir = root / "output" / profile.name / f"bloque-{block}"
    state_path = root / "state" / profile.name / f"bloque-{block}.json"
    registry = ProjectRegistry(
        root / "state" / profile.name / "projects.json", profile.name
    )
    context = project_context(registry.data)

    print(f"Perfil : {profile.name} — {profile.title}")
    print(f"PATH   : {source}")
    print(f"Bloque : {block}")
    print(f"Lecciones seleccionadas: {len(selected)}")

    inspection_requested = any(
        (
            args.show_prompt,
            args.inspect,
            args.save_prompt is not None,
            args.save_inspect is not None,
            args.dump_json,
            args.validate_context,
        )
    )

    if inspection_requested and len(selected) != 1:
        raise SystemExit(
            "Las opciones de inspección requieren una única lección; usa --lesson X.Y[.Z...]."
        )

    if inspection_requested:
        lesson = selected[0]
        idx = lessons.index(lesson)
        neighbors_text = neighbors(lessons, idx, radius=args.neighbor_radius)
        data = inspection_data(
            profile=profile,
            source=source,
            lessons_count=len(lessons),
            lesson=lesson,
            neighbors_text=neighbors_text,
            templates=templates,
            prompt_context=prompt_context,
            context=context,
            neighbor_radius=args.neighbor_radius,
        )
        inspect_text = render_inspection(data)
        prompt_text = render_prompt(data["planner"])

        if args.inspect:
            print("\n" + inspect_text, end="")
        if args.show_prompt:
            print("\n" + prompt_text, end="")
        if args.dump_json:
            print("\nPLANNER — PAYLOAD JSON")
            print("=" * 72)
            print(json.dumps(data["planner"]["payload"], ensure_ascii=False, indent=2))
        if args.save_prompt:
            _write_text(args.save_prompt, prompt_text)
        if args.save_inspect:
            _write_text(args.save_inspect, inspect_text)
        if args.validate_context:
            failures = [
                check for check in data["context_checks"] if check["status"] != "OK"
            ]
            if failures:
                names = ", ".join(check["name"] for check in failures)
                raise SystemExit(f"Contexto inválido; faltan: {names}")
            print("Contexto: OK")

    if args.dry_run:
        print("\nDRY RUN: configuración válida; no se llamará a la API.")
        overrides = (profile.data.get("artifacts") or {}).get("overrides") or {}
        for lesson in selected:
            idx = lessons.index(lesson)
            neighbor_text = neighbors(lessons, idx, radius=args.neighbor_radius)
            print(f"  {lesson.id:>6}  {lesson.title}")
            print(f"          vecinos: {neighbor_text.replace(chr(10), ' | ')}")
            override = overrides.get(lesson.id) or {}
            if override:
                print(
                    "          artefactos: "
                    f"{override.get('strategy')} / {override.get('project_id')}"
                )
        return

    from .openai_client import CourseOpenAI
    from .pipeline import process_lesson

    state = StateStore(state_path, profile.name, str(source))
    client = CourseOpenAI()
    stages = PipelineStages(client, templates, prompt_context)

    for lesson in selected:
        idx = lessons.index(lesson)
        process_lesson(
            profile=profile,
            lesson=lesson,
            neighbors_text=neighbors(lessons, idx, radius=args.neighbor_radius),
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


def main() -> None:
    try:
        _main()
    except (PathParseError, OpenAIRequestError) as exc:
        raise SystemExit(f"ERROR: {exc}") from None


if __name__ == "__main__":
    main()
