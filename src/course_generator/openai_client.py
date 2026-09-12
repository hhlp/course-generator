from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, cast

from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)
from openai.types import ReasoningEffort


@dataclass(slots=True)
class RawCall:
    response_id: str | None
    usage: dict[str, Any]


@dataclass(slots=True)
class StructuredResult:
    data: dict[str, Any] | None
    raw: RawCall


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default

    value = raw.strip().lower()
    if value in {"1", "true", "yes", "on"}:
        return True
    if value in {"0", "false", "no", "off"}:
        return False

    raise ValueError(
        f"{name} debe ser true/false, 1/0, yes/no u on/off; recibido: {raw!r}"
    )


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default

    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} debe ser un entero; recibido: {raw!r}") from exc

    if value <= 0:
        raise ValueError(f"{name} debe ser > 0; recibido: {value}")

    return value


class OpenAIRequestError(RuntimeError):
    """Error de API presentado sin exponer detalles internos del SDK."""


def _api_error_code(exc: APIStatusError) -> str | None:
    body = getattr(exc, "body", None)
    if not isinstance(body, dict):
        return None
    error = body.get("error")
    if isinstance(error, dict):
        code = error.get("code")
        return code if isinstance(code, str) else None
    code = body.get("code")
    return code if isinstance(code, str) else None


def _friendly_api_error(exc: Exception) -> OpenAIRequestError:
    if isinstance(exc, AuthenticationError):
        return OpenAIRequestError(
            "OPENAI: autenticación rechazada. Comprueba OPENAI_API_KEY."
        )
    if isinstance(exc, RateLimitError):
        code = _api_error_code(exc)
        if code == "credit_balance_exhausted":
            return OpenAIRequestError(
                "OPENAI: saldo de API agotado. Añade créditos antes de realizar "
                "una generación real. Puedes usar --dry-run sin consumir API."
            )
        if code == "insufficient_quota":
            return OpenAIRequestError(
                "OPENAI: cuota o créditos insuficientes. Revisa la facturación "
                "de la API. Puedes usar --dry-run sin consumir API."
            )
        return OpenAIRequestError(
            "OPENAI: límite temporal de solicitudes alcanzado. "
            "Espera y vuelve a intentarlo."
        )
    if isinstance(exc, APITimeoutError):
        return OpenAIRequestError(
            "OPENAI: la solicitud agotó el tiempo de espera. Vuelve a intentarlo."
        )
    if isinstance(exc, APIConnectionError):
        return OpenAIRequestError(
            "OPENAI: no se pudo conectar con la API. Comprueba la red."
        )
    if isinstance(exc, APIStatusError):
        status = getattr(exc, "status_code", None)
        if isinstance(status, int) and status >= 500:
            return OpenAIRequestError(
                f"OPENAI: error temporal del servicio (HTTP {status}). "
                "Vuelve a intentarlo más tarde."
            )
        return OpenAIRequestError(
            f"OPENAI: la API rechazó la solicitud (HTTP {status})."
        )
    return OpenAIRequestError(f"OPENAI: error inesperado: {exc}")


class CourseOpenAI:
    def __init__(self) -> None:
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Falta OPENAI_API_KEY. Configúrala en el entorno o en .env."
            )

        self.client = OpenAI(api_key=api_key)

        self.model = os.getenv("OPENAI_MODEL", "gpt-6-astra").strip()
        raw_effort = os.getenv("OPENAI_REASONING_EFFORT", "high").strip().lower()
        self.max_output_tokens = _env_int("OPENAI_MAX_OUTPUT_TOKENS", 50_000)
        self.store = _env_bool("OPENAI_STORE_RESPONSES", False)

        valid_efforts = {"low", "medium", "high", "xhigh", "max"}
        if self.model == "gpt-6-astra" and raw_effort not in valid_efforts:
            raise ValueError(
                "OPENAI_REASONING_EFFORT no válido para gpt-6-astra. "
                f"Valores admitidos: {', '.join(sorted(valid_efforts))}. "
                f"Recibido: {raw_effort!r}"
            )

        self.reasoning_effort = cast(ReasoningEffort, raw_effort)

        if self.model == "gpt-6-astra" and self.max_output_tokens > 128_000:
            raise ValueError(
                "OPENAI_MAX_OUTPUT_TOKENS supera el máximo publicado de "
                "128000 para gpt-6-astra."
            )

    @staticmethod
    def _usage_dict(response: Any) -> dict[str, Any]:
        usage = getattr(response, "usage", None)

        if usage is None:
            return {}

        if hasattr(usage, "model_dump"):
            return usage.model_dump()

        if isinstance(usage, dict):
            return usage

        return {"value": str(usage)}

    @staticmethod
    def _extract_text(response: Any) -> str:
        text = getattr(response, "output_text", None)
        if isinstance(text, str) and text.strip():
            return text.strip()

        output = getattr(response, "output", None) or []
        chunks: list[str] = []

        for item in output:
            content = getattr(item, "content", None) or []

            for part in content:
                value = getattr(part, "text", None)
                if isinstance(value, str):
                    chunks.append(value)

        return "\n".join(chunks).strip()

    @staticmethod
    def _strip_json_fence(text: str) -> str:
        cleaned = text.strip()

        if not cleaned.startswith("```"):
            return cleaned

        lines = cleaned.splitlines()

        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        return "\n".join(lines).strip()

    def json_call(
        self,
        *,
        instructions: str,
        input_text: str,
    ) -> StructuredResult:
        try:
            response = self.client.responses.create(
                model=self.model,
                instructions=instructions,
                input=input_text,
                reasoning={
                    "effort": self.reasoning_effort,
                },
                max_output_tokens=self.max_output_tokens,
                store=self.store,
            )
        except (
            AuthenticationError,
            RateLimitError,
            APITimeoutError,
            APIConnectionError,
            APIStatusError,
        ) as exc:
            raise _friendly_api_error(exc) from None

        text = self._extract_text(response)

        if not text:
            status = getattr(response, "status", None)
            incomplete = getattr(response, "incomplete_details", None)
            raise RuntimeError(
                "La API no devolvió texto. "
                f"status={status!r}, incomplete_details={incomplete!r}"
            )

        cleaned = self._strip_json_fence(text)

        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "La etapa esperaba JSON válido pero la API devolvió "
                "contenido no parseable.\n"
                f"Primeros 2000 caracteres:\n{cleaned[:2000]}"
            ) from exc

        if not isinstance(data, dict):
            raise TypeError("La etapa esperaba un objeto JSON en la raíz.")

        raw = RawCall(
            response_id=getattr(response, "id", None),
            usage=self._usage_dict(response),
        )

        return StructuredResult(
            data=data,
            raw=raw,
        )
