"""FastAPI app implementing the Ethical Evaluator API (Stage 4 Section 5)."""
from __future__ import annotations

import uuid

from fastapi import FastAPI, HTTPException

from . import store
from .evaluator import evaluate
from .frameworks import available_frameworks
from .models import EvaluateRequest, EvaluateResponse

app = FastAPI(
    title="Sentient-Centered AI: Ethical Evaluator",
    description=(
        "Research prototype. Produces a multi-dimensional heuristic profile of an "
        "AI interaction, not a moral verdict. See PRINCIPLES.md and SECURITY.md."
    ),
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/frameworks")
def frameworks() -> dict[str, list[str]]:
    return {"frameworks": available_frameworks()}


@app.post("/evaluate", response_model=EvaluateResponse)
def post_evaluate(request: EvaluateRequest) -> EvaluateResponse:
    if not request.responses:
        raise HTTPException(status_code=400, detail="responses must not be empty")
    evaluation_id = str(uuid.uuid4())
    result = evaluate(request, evaluation_id)
    store.save(result)
    return result


@app.get("/evaluate/{evaluation_id}", response_model=EvaluateResponse)
def get_evaluate(evaluation_id: str) -> EvaluateResponse:
    result = store.get(evaluation_id)
    if result is None:
        raise HTTPException(status_code=404, detail="evaluation_id not found")
    return result
