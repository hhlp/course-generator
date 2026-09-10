from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


class StateStore:
    def __init__(self, path: Path, profile: str, source: str) -> None:
        self.path = path
        self.profile = profile
        self.source = source
        self.data = self._load()
        self.data.setdefault("profile", profile)
        self.data.setdefault("source", source)
        self.data.setdefault("lessons", {})

    def _load(self) -> dict[str, Any]:
        if not self.path.is_file():
            return {}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"State JSON inválido en {self.path}: {exc}") from exc
        if not isinstance(data, dict):
            raise TypeError(
                f"State inválido en {self.path}: la raíz debe ser un objeto."
            )
        return data

    def save(self) -> None:
        _atomic_write_json(self.path, self.data)

    def status(self, lesson_id: str) -> str | None:
        entry = self.data.get("lessons", {}).get(lesson_id, {})
        if isinstance(entry, dict):
            value = entry.get("status")
            return str(value) if value is not None else None
        return None

    def update(self, lesson_id: str, **values: Any) -> None:
        lessons = self.data.setdefault("lessons", {})
        entry = lessons.setdefault(lesson_id, {})
        if not isinstance(entry, dict):
            entry = {}
            lessons[lesson_id] = entry
        entry.update(values)
        self.save()


class ProjectRegistry:
    def __init__(self, path: Path, profile: str) -> None:
        self.path = path
        self.profile = profile
        self.data = self._load()
        self.data.setdefault("profile", profile)
        self.data.setdefault("projects", {})

    def _load(self) -> dict[str, Any]:
        if not self.path.is_file():
            return {}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Registry JSON inválido en {self.path}: {exc}") from exc
        if not isinstance(data, dict):
            raise TypeError(
                f"Registry inválido en {self.path}: la raíz debe ser un objeto."
            )
        return data

    def save(self) -> None:
        _atomic_write_json(self.path, self.data)

    def project(self, project_id: str) -> dict[str, Any] | None:
        value = self.data.get("projects", {}).get(project_id)
        return value if isinstance(value, dict) else None

    def update(self, project_id: str, **values: Any) -> None:
        projects = self.data.setdefault("projects", {})
        entry = projects.setdefault(project_id, {})
        if not isinstance(entry, dict):
            entry = {}
            projects[project_id] = entry
        entry.update(values)
        self.save()
