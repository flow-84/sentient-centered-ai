## Technology Stack

`[PROJECT PROPOSAL]` — the following stack is proposed for the Ethical
Evaluation Layer MVP (Phase 2). Chosen for simplicity and to avoid
unnecessary complexity, per the project's working principles.

### Backend / API

- **Python 3.11+** — dominant language for both the AI/ML tooling this
  project evaluates and the evaluation logic itself; keeps contributor
  onboarding low-friction for the target audience (AI/ML researchers and
  engineers).
- **FastAPI** — async-capable, typed, auto-generates OpenAPI schema
  matching `docs/api-spec.md` (Stage 4 deliverable), minimal boilerplate.
- **Pydantic** — request/response validation and the typed data models for
  the evaluator's structured output (harm/welfare/sentience/uncertainty
  profile).

### Data

- **PostgreSQL** — relational storage for benchmark scenarios, evaluation
  runs, and results. Chosen over a NoSQL store because benchmark data is
  structured and relational (scenarios, entities, evaluations, frameworks)
  and benefits from referential integrity and SQL querying for research
  analysis.
- **Vector database: not adopted by default.** No current MVP requirement
  involves semantic search over embeddings at a scale that justifies the
  added operational complexity. If a future evaluation method needs
  similarity search (e.g. finding similar past scenarios), add pgvector as
  a Postgres extension rather than a separate service — avoids a second
  piece of infrastructure for a need that isn't established yet.

### ML / evaluation

- **Hugging Face (transformers, datasets)** — for any evaluator component
  that uses open models (e.g. classifier-based harm detection), and for
  publishing benchmark datasets in a format the broader research community
  already knows how to consume.
- **PyTorch** — backend for any locally-run models, consistent with the
  Hugging Face ecosystem choice.
- **LLM-as-judge** (via API or self-hosted) is expected to be one evaluation
  method among several (see Stage 4 architecture options); no specific
  provider is pinned here to avoid vendor lock-in in this document —
  provider choice belongs in `src/` configuration, not this doc.

### Quality tooling

- **pytest** — test runner.
- **Ruff** — linting and formatting (replaces separate flake8/black/isort
  tooling with one fast tool).
- **mypy** — static type checking, enforced given Pydantic's typed models.

### Infrastructure

- **Docker** — reproducible local dev and deployment environment.
- **GitHub Actions** — CI: lint, type-check, test on every PR.

### Frontend (website/, later)

Not pinned yet — deferred to Stage 9 (Website & Community Strategy), which
owns the website's own technology decision separately from the evaluator
backend.

### Explicitly deferred / not adopted

- No message queue, no Kubernetes manifest, no microservice split at MVP
  stage — a single FastAPI service is sufficient for the evaluation
  workload described in Phase 2, and premature infrastructure would slow
  down the research iteration this project needs most right now.
