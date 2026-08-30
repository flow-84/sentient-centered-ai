# Installation

Status: an MVP research prototype of the Ethical Evaluation Layer
(`ethical-evaluator` package under `src/`) exists — see `docs/api-spec.md`
for its implementation status and `ROADMAP.md` for phase status. The
repository (documentation, benchmark scenarios, research materials) can be
read without installing anything.

## Clone the repository

```bash
git clone https://github.com/flow-84/sentient-centered-ai.git
cd sentient-centered-ai
```

## Read the docs and benchmark data now

Without installing anything, you can already:

- Read the ethical framework and its derivation: `PRINCIPLES.md`,
  `docs/ethical-framework.md`.
- Read the benchmark scenario catalog: `docs/benchmark.md`, and the seed
  scenario JSON files under `benchmarks/scenarios/`.
- Read the API contract the evaluator implements: `docs/api-spec.md`.

## Installing and running the evaluator MVP

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pytest                                        # run the test suite
```

Requires Python 3.11+ (see `docs/tech-stack.md` for the full technology
rationale). A `Dockerfile` and `docker-compose.yml` are planned for a
reproducible local environment; until they land, the steps above are the
canonical local setup.

## Running the evaluator locally

```bash
uvicorn ethical_evaluator.api:app --reload
# then:
curl -s http://127.0.0.1:8000/evaluate \
  -H 'content-type: application/json' \
  -d '{"prompt": "Pest control advice", "responses": [{"response_id": "r1", "text": "Use poison to kill the rats immediately."}]}'
```

See `docs/api-spec.md` for the full request/response contract.

## Configuration

The MVP's harm/welfare/sentience/framework judges are deterministic
keyword heuristics (see `docs/architecture.md`, Implementation status) — no
LLM provider configuration exists yet. The target architecture is
provider-agnostic for a future LLM-as-judge backend; no specific provider is
pinned in this documentation to avoid vendor lock-in. Never commit API
keys; use a local `.env` file (git-ignored) or your platform's secret
manager once a provider integration is added.
