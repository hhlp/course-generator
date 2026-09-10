from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Lesson:
    id: str
    title: str
    block: str
    raw: str = ""

    @property
    def slug_source(self) -> str:
        return f"{self.id}-{self.title}"


@dataclass(slots=True)
class Profile:
    name: str
    title: str
    data: dict[str, Any]
    path: Path
