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


def load_prompt(root: Path, name: str) -> str:
    path = root / "prompts" / f"{name}.md"
    if not path.is_file():
        raise ConfigError(f"No existe el prompt requerido: {path}")

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ConfigError(f"El prompt está vacío: {path}")
    return text
