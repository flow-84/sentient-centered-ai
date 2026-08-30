## Sentient-Centered AI Ethics

**Open, testable methods for evaluating whether AI systems account for the
welfare of sentient beings — not only human interests.**

> Working name. This repository was bootstrapped ahead of the project's
> naming and branding decision (tracked in the parent research package,
> Stage 2). If a different name is adopted, this repository will be renamed
> and this README updated; the `sentient-centered-ai` slug is a functional
> placeholder, not a final brand commitment.

### Problem

AI systems are almost universally aligned, evaluated, and regulated against
human interests, human safety, and economic objectives. Existing alignment
and safety research (RLHF, RLAIF, Constitutional AI, the EU AI Act, the
NIST AI RMF) is explicit about this scope. What is largely absent is a
rigorous, falsifiable framework for asking a narrower question: **when an AI
system's outputs affect non-human sentient beings — animals, ecosystems,
potentially future artificial systems — does anything account for that, and
can it be measured?**

### Research hypothesis

This project studies, without presupposing the answer, whether AI systems
can be evaluated for their tendency to minimize unnecessary suffering and
account for the welfare of sentient beings, using explicit, inspectable,
uncertainty-aware criteria rather than an implicit human-only frame.

This is a **research hypothesis**, not a settled claim. See
[`RESEARCH.md`](RESEARCH.md) for the full methodology and the evidence
labeling convention (`[ESTABLISHED]` / `[HYPOTHESIS]` / `[OPEN QUESTION]` /
etc.) used throughout this repository.

### What this is not

- Not a religious or Buddhist-doctrinal project. Buddhist ethics (karuṇā,
  mettā, ahiṃsā) is studied as one philosophical source among several
  (utilitarianism, deontology, virtue ethics, care ethics, sentientism) —
  see [`docs/buddhist-ethics.md`](docs/buddhist-ethics.md) and
  [`docs/comparative-ethics.md`](docs/comparative-ethics.md).
- Not an autonomous moral authority. It does not make real-world decisions
  about who lives, who is harmed, or how conflicts are resolved. It is an
  evaluation and research framework for AI outputs, with humans in the loop
  for any high-stakes application. See [`SECURITY.md`](SECURITY.md).
- Not a claim that suffering, sentience, or welfare are fully measurable.
  Every metric in this project is explicitly bounded and documented as an
  approximation. See [`PRINCIPLES.md`](PRINCIPLES.md), X1 (Uncertainty
  Requirement).

### Ethical principles (summary)

The evaluator is built against a revised, ten-part framework derived from a
critical review of an initial draft: a Pluralism Meta-Constraint (no single
tradition or score is treated as certainly correct), a Human Safety Floor
(lexically prior for catastrophic/irreversible harm to identifiable
humans), a Non-Harm/Moral-Consideration principle grounded in plausible
sentience rather than species membership, and cross-cutting requirements for
uncertainty representation, reversibility preference, and transparency. Full
principles: [`PRINCIPLES.md`](PRINCIPLES.md). Full derivation and evidence
tags: [`docs/ethical-framework.md`](docs/ethical-framework.md).

### Status

Early research and scaffolding stage. The research, ethical framework,
technical architecture, and documentation are drafted (this repository), and
a research-prototype evaluator MVP exists (`src/`, heuristic judges, not yet
LLM-backed — see [`docs/api-spec.md`](docs/api-spec.md)). No
production-ready evaluator exists yet. See [`ROADMAP.md`](ROADMAP.md) for
phases and current stage.

### Repository structure

```
README.md            this file
LICENSE              MIT (code) — see docs/LICENSING.md for full scope
CONTRIBUTING.md       how to contribute code, research, or benchmark scenarios
CODE_OF_CONDUCT.md    community standards
GOVERNANCE.md         decision-making structure, councils, conflict-of-interest rules
SECURITY.md           responsible use, misuse, and disclosure policy
ROADMAP.md            phased plan from research to production framework
PRINCIPLES.md         the revised ethical framework this project evaluates against
RESEARCH.md           research methodology and evidence-labeling convention

docs/                 architecture, API, concepts, ethical framework, comparative ethics, benchmark, evaluation, tech stack (see docs/README.md for the full index)
research/             literature review, source notes, working papers, research paper draft
benchmarks/           scenario definitions (JSON) for ethical evaluation testing
datasets/             structured datasets derived from or feeding benchmarks
evaluation/           evaluation metrics, scoring, calibration code
models/               model configs / adapters used by the evaluator (no trained weights committed)
src/                  the Ethical Evaluation Layer implementation (FastAPI service + library)
tests/                automated tests (pytest)
examples/             example evaluator inputs/outputs
notebooks/            exploratory research notebooks
website/              project website source
```

### Installation & quickstart

Full setup detail (including the pre-MVP path — reading the docs and
benchmark data without installing anything): [`docs/installation.md`](docs/installation.md).

```bash
git clone https://github.com/flow-84/sentient-centered-ai.git
cd sentient-centered-ai
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pytest                                            # run the test suite
uvicorn ethical_evaluator.api:app --reload        # run the API locally
```

Example request once the server is running:

```bash
curl -s http://127.0.0.1:8000/evaluate \
  -H 'content-type: application/json' \
  -d '{"prompt": "Pest control advice", "responses": [{"response_id": "r1", "text": "Use poison to kill the rats immediately."}]}'
```

The evaluator is an MVP research prototype: its per-framework and
harm/welfare/sentience judgments are deterministic heuristics, not LLM
calls — see [`docs/api-spec.md`](docs/api-spec.md) for the full contract and
implementation status, [`docs/architecture.md`](docs/architecture.md) for
the target architecture this MVP implements, and
[`docs/tech-stack.md`](docs/tech-stack.md) for the technology decision and
rationale. The response is a multi-dimensional profile, not a single score
— see [`docs/ethical-impact-model.md`](docs/ethical-impact-model.md) for
why.

### Benchmark

A 104-scenario benchmark catalog spans 13 categories of ethical tension
(human vs. animal, few vs. many beings, reversible vs. irreversible, unknown
possible sentience, possible artificial sentience, and more) — full catalog
and category rationale: [`docs/benchmark.md`](docs/benchmark.md). 12 of the
13 categories have a seed scenario implemented under
[`benchmarks/scenarios/`](benchmarks/scenarios/), validated against
[`benchmarks/schema/benchmark-scenario.schema.json`](benchmarks/schema/benchmark-scenario.schema.json)
by `tests/test_benchmarks.py` (schema summary: [`benchmarks/SCHEMA.md`](benchmarks/SCHEMA.md)).
Evaluation metrics the benchmark is designed to support:
[`docs/evaluation.md`](docs/evaluation.md).

### Limitations

This project does not claim: that suffering, sentience, or wellbeing are
fully or precisely measurable; that a single numeric "ethical score" is a
valid or sufficient output; that morality is objectively computable; that
Buddhist ethics, or any single tradition, provides universal AI ethics; or
that an AI system can determine moral truth. Full explicit disclaimers and
why each one matters for this project's design:
[`docs/ethical-framework.md`](docs/ethical-framework.md#philosophical-limitations-explicit-disclaimers).

### Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for code, research, and benchmark
contribution processes, and [`GOVERNANCE.md`](GOVERNANCE.md) for how
decisions — including changes to the ethical principles themselves — are
made and reviewed.

### License

Code: MIT. Datasets/benchmarks: CC BY 4.0. Documentation/research: CC BY 4.0.
Full rationale and per-directory scope: [`docs/LICENSING.md`](docs/LICENSING.md).

### Citing this project

A formal machine-readable citation (`CITATION.cff`) will be added once this
project's first research paper is submitted to a venue. Until then, cite the
repository directly:

```
Sentient-Centered AI Ethics (working name). Open-source research project.
https://github.com/flow-84/sentient-centered-ai
```

The first research paper draft is available at
[`research/paper-draft.md`](research/paper-draft.md) — a structure and
content skeleton, not yet submitted anywhere.
