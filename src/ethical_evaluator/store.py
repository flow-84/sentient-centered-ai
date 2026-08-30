"""In-memory evaluation store.

`GET /evaluate/{evaluation_id}` (Stage 4 Section 5) requires results to be
re-fetchable for reproducibility/audit. A process-local dict is sufficient
for the MVP; docs/tech-stack.md defers PostgreSQL-backed persistence until
an actual multi-process/durability requirement exists, per Rule 14
(no unnecessary complexity).
"""
from __future__ import annotations

from .models import EvaluateResponse

_STORE: dict[str, EvaluateResponse] = {}


def save(response: EvaluateResponse) -> None:
    _STORE[response.evaluation_id] = response


def get(evaluation_id: str) -> EvaluateResponse | None:
    return _STORE.get(evaluation_id)
