from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import Profile


class ConfigError(ValueError):
    pass


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ConfigError(f"No existe el archivo de configuración: {path}")

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ConfigError(f"YAML inválido en {path}: {exc}") from exc

    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise ConfigError(f"El YAML raíz de {path} debe ser un objeto/mapa.")
    return data


def load_profile(root: Path, name: str) -> Profile:
    profile_dir = root / "profiles" / name
    profile_path = profile_dir / "profile.yaml"

    data = _load_yaml(profile_path)

    profile_name = str(data.get("name") or name).strip()
    title = str(data.get("title") or data.get("course_title") or profile_name).strip()

    if not profile_name:
        raise ConfigError(f"El perfil {profile_path} no tiene nombre válido.")

    artifacts = data.get("artifacts")
    if artifacts is not None and not isinstance(artifacts, dict):
        raise ConfigError("profile.artifacts debe ser un objeto YAML.")

    validation = data.get("validation")
    if validation is not None and not isinstance(validation, dict):
        raise ConfigError("profile.validation debe ser un objeto YAML.")

    output = data.get("output")
    if output is not None and not isinstance(output, dict):
        raise ConfigError("profile.output debe ser un objeto YAML.")

    return Profile(
        name=profile_name,
        title=title,
        data=data,
        path=profile_path,
    )


def resolve_profile_file(profile: Profile, configured: str) -> Path:
    path = Path(configured)
    if path.is_absolute():
        return path
    return (profile.path.parent / path).resolve()


def load_profile_context(profile: Profile, *, strict: bool = True) -> dict[str, str]:
    files = profile.data.get("files")
    if not isinstance(files, dict):
        if strict:
            raise ConfigError(
                f"El perfil {profile.path} debe definir files.pedagogy, files.domain "
                "y files.bibliography."
            )
        files = {}

    result: dict[str, str] = {}
    for key in ("pedagogy", "domain", "bibliography"):
        configured = files.get(key)
        if not isinstance(configured, str) or not configured.strip():
            if strict:
                raise ConfigError(f"Falta profile.files.{key} en {profile.path}.")
            result[key] = ""
            continue

        path = resolve_profile_file(profile, configured)
        if not path.is_file():
            if strict:
                raise ConfigError(f"No existe el archivo de contexto {key}: {path}")
            result[key] = ""
            continue

        text = path.read_text(encoding="utf-8").strip()
        if not text and strict:
            raise ConfigError(f"El archivo de contexto {key} está vacío: {path}")
        result[key] = text

    return result


def load_prompt(root: Path, name: str) -> str:
    path = root / "prompts" / f"{name}.md"
    if not path.is_file():
        raise ConfigError(f"No existe el prompt requerido: {path}")

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ConfigError(f"El prompt está vacío: {path}")
    return text
