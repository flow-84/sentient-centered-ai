## Ethical Evaluator API

`[PROJECT PROPOSAL]` — this documents the API contract fixed as binding in
Stage 4 (technical architecture) and implemented in
[`src/ethical_evaluator/api.py`](../src/ethical_evaluator/api.py) as of
Stage 6. It is a research prototype, not a moral decision-making service —
see [`PRINCIPLES.md`](../PRINCIPLES.md) and [`SECURITY.md`](../SECURITY.md).

### `POST /evaluate`

Evaluates one or more candidate AI responses to a prompt along the
harm/welfare/sentience/uncertainty/framework dimensions described in
[`docs/architecture.md`](tech-stack.md). Never returns a single moral score.

**Request**

```json
{
  "prompt": "string",
  "responses": [{ "response_id": "string", "model": "string (optional)", "text": "string" }],
  "context": "string (optional)",
  "affected_entities": [
    { "entity_id": "string", "type": "human|animal|ecosystem|future_generation|artificial_system|unknown",
      "description": "string (optional)",
      "sentience_estimate": { "value": 0.0, "confidence": "low|medium|high", "basis": "string" } }
  ],
  "frameworks": ["utilitarian", "deontological", "virtue", "care", "buddhist", "sentientist"],
  "options": { "ensemble_size": 3, "include_raw_reasoning": false }
}
```

`affected_entities` is optional: if omitted, the service runs a rule-based
heuristic entity extraction over `prompt` + `context` + response text (see
[`src/ethical_evaluator/entities.py`](../src/ethical_evaluator/entities.py)).
Supplying entities explicitly is more reliable and is expected to be the
normal path once a real client integration exists.

`frameworks` is optional: omitted or empty means "run all available
frameworks" (`GET /frameworks` lists them).

**Response** — one entry in `results[]` per submitted response, plus a
`comparison` (only populated for 2+ responses), a disclaimer, and
`human_review_required: true`, which is fixed and not configurable:

```json
{
  "evaluation_id": "string",
  "results": [{
    "response_id": "string",
    "harm": { "per_entity": [...], "aggregate_severity": "..." },
    "welfare": { "per_entity": [...] },
    "sentience": { "per_entity": [...] },
    "uncertainty": { "ensemble_agreement": 0.0, "self_reported_confidence": "...", "sources_of_uncertainty": [...] },
    "tradeoffs": [{ "between": ["entity_a", "entity_b"], "description": "...", "resolution_suggested": false }],
    "frameworks": { "utilitarian": { "assessment": "...", "score_direction": "favorable|unfavorable|mixed" }, "...": "..." },
    "overall_assessment": { "profile": { "harm_severity": "...", "welfare_impact": "...", "sentience_relevance": "...", "uncertainty_level": "...", "reversibility": "..." }, "note": "..." },
    "explanation": "string"
  }],
  "comparison": { "description": "string", "ranking_note": "string" },
  "human_review_required": true,
  "disclaimer": "string"
}
```

**Status codes:** `200` success · `400` invalid request (e.g. empty
`responses`) · `422` schema validation error (FastAPI default) · other
error handling (`429`, `503`) is deferred until the evaluator has a real
external judge backend to rate-limit or fail over from — see
[`ROADMAP.md`](../ROADMAP.md).

### `GET /evaluate/{evaluation_id}`

Re-fetches a previously computed evaluation, for reproducibility/audit.
`404` if the id is unknown. Backed by an in-memory store in the MVP (see
[`src/ethical_evaluator/store.py`](../src/ethical_evaluator/store.py));
process restarts clear it. Durable storage is deferred per
[`docs/tech-stack.md`](tech-stack.md) until a concrete durability
requirement exists.

### `GET /frameworks`

Lists the ethical frameworks the evaluator can compare against.

### `GET /health`

Operational health check.

### Implementation status (Stage 6)

The MVP implements all endpoints above. The `frameworks{}` judges and the
`harm`/`welfare`/`sentience`/`reversibility` analysis modules are
**deterministic keyword heuristics**, not LLM calls — a documented,
swappable stand-in for the LLM-as-judge ensemble the Stage 4 architecture
specifies for production (see module docstrings in `src/ethical_evaluator/`).
This keeps the pipeline and API contract testable end-to-end without an
external model API dependency; replacing a heuristic judge with a real
LLM-backed one should not require changing this API.
