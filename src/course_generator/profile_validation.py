from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .config_loader import ConfigError, load_profile, load_profile_context


def _walk(value: Any, prefix: str = "") -> list[str]:
    result: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            name = f"{prefix}.{key}" if prefix else str(key)
            result.append(name)
            result.extend(_walk(child, name))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            result.extend(_walk(child, f"{prefix}[{index}]"))
    return result


def validate_profiles(
    root: Path,
    target: Path | None = None,
    *,
    show_items: bool = False,
    json_output: bool = False,
) -> int:
    profiles_root = root / "profiles"
    paths = [target.resolve()] if target else sorted(
        profiles_root.rglob("profile.yaml")
    )
    results: list[dict[str, Any]] = []
    for path in paths:
        errors: list[str] = []
        warnings: list[str] = []
        items: list[str] = []
        try:
            relative = path.relative_to(profiles_root.resolve())
            if relative.name != "profile.yaml":
                raise ConfigError("El archivo debe llamarse profile.yaml")
            name = relative.parent.as_posix()
            profile = load_profile(root, name)
            items = _walk(profile.data)
            load_profile_context(profile, strict=True)
            # The complete config is passed to model prompts; unknown
            # keys are not necessarily errors or unused parameters.
            for key in ("artifacts", "validation", "output"):
                value = profile.data.get(key)
                if value is not None and not isinstance(value, dict):
                    errors.append(f"{key} debe ser un mapa YAML")
        except (ConfigError, OSError, UnicodeError, yaml.YAMLError,
                ValueError) as exc:
            errors.append(str(exc))
        results.append({
            "path": str(path),
            "status": "FAIL" if errors else "PASS",
            "items": items,
            "errors": errors,
            "warnings": warnings,
        })
    if not paths:
        results.append({
            "path": str(profiles_root),
            "status": "FAIL",
            "items": [],
            "errors": ["No se encontraron profile.yaml"],
            "warnings": [],
        })
    if json_output:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(f"[{result['status']}] {result['path']} "
                  f"({len(result['items'])} rutas de claves)")
            for error in result["errors"]:
                print(f"  ERROR: {error}")
            if show_items:
                for item in result["items"]:
                    print(f"  {item}")
        passed = sum(r["status"] == "PASS" for r in results)
        print(f"Perfiles: {len(results)} | PASS: {passed} | "
              f"FAIL: {len(results) - passed}")
    return int(any(r["status"] == "FAIL" for r in results))
