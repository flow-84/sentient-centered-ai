# Development

Status: describes the development workflow for the Ethical Evaluation
Layer (`ethical-evaluator` package, `src/`). See `docs/tech-stack.md` for
the full technology decision and rationale, and `CONTRIBUTING.md` for the
contribution process (code, research, and benchmark scenarios each have a
distinct path).

## Local setup

See `docs/installation.md` for environment setup. In short: Python 3.11+,
`pip install -r requirements-dev.txt && pip install -e .`, `pytest` before
opening a PR.

## Project layout

```
src/                    the ethical-evaluator package (FastAPI service + library, MVP implementation)
tests/                  automated tests (pytest)
benchmarks/scenarios/   scenario definitions (JSON), one file per scenario
benchmarks/schema/      authoritative JSON Schema for scenario files (see benchmarks/SCHEMA.md)
evaluation/             evaluation metrics, scoring, calibration code (docs/evaluation.md)
models/                 model configs / adapters used by the evaluator (no trained weights committed)
```

## Testing

- `pytest` is the test runner (`pytest -q` in CI). Every code change needs
  tests — no PR merges code without corresponding test coverage.
- Benchmark-driven tests (validating scenarios in `benchmarks/scenarios/`
  against `benchmarks/schema/benchmark-scenario.schema.json`, and
  evaluating the evaluator against them) are the primary correctness signal
  for evaluation logic, since there is no single "correct" moral answer to
  assert against (see `benchmarks/SCHEMA.md`'s design notes) — tests assert
  schema conformance, metric behavior (`docs/evaluation.md`), and
  regression-freedom, not moral correctness.

## Linting and types

**Ruff** and **mypy** are the chosen tools (see `docs/tech-stack.md`) but
are not yet wired into CI — currently only `pytest` runs
(`.github/workflows/ci.yml`). Adding lint/type-check enforcement to CI is
open work, not yet done; run them locally in the meantime if installed.

## CI

GitHub Actions runs `pytest -q` on every push to `main` and on every PR
(`.github/workflows/ci.yml`). A PR with failing CI does not merge.

## Adding a new ethical framework to the evaluator

New frameworks (beyond the ones already discussed in
`docs/comparative-ethics.md`) are added as an entry in the open
`ethical_frameworks` list (`docs/api-spec.md`, `benchmarks/SCHEMA.md`) plus a
system-prompt persona for the LLM-as-judge ensemble (`docs/architecture.md`).
This requires Research Council review per `GOVERNANCE.md`, since it changes
what the evaluator claims to compare against — flag it in the PR per
`CONTRIBUTING.md`'s ethical review process.

## Adding a new benchmark scenario

Follow `benchmarks/SCHEMA.md` and the contribution steps in
`CONTRIBUTING.md`. New scenarios should target a category in
`docs/benchmark.md`'s catalog, or propose a new category with justification
for why the existing 13 don't cover it.
