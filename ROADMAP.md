## Roadmap

### Phase 0 — Research
Literature review across AI ethics/alignment/safety, sentience &
consciousness research, philosophical frameworks (including Buddhist
ethics), and existing AI-ethics standards (EU AI Act, NIST AI RMF, OECD AI
Principles, UNESCO Recommendation). Deliverable: `research/` dossier with
labeled evidence strength per `RESEARCH.md`.

### Phase 1 — Concept
Precise research question, ethical framework draft (`PRINCIPLES.md`),
comparative ethics analysis, common-ethical-core hypothesis. Deliverable:
this repository's founding documents.

### Phase 2 — MVP
Ethical Evaluation Layer: given an AI prompt + response + context, produce
a harm/welfare/sentience/uncertainty/trade-off assessment. Deliverable:
`src/` implementation + `docs/api-spec.md`.

### Phase 3 — Benchmark
At least 100 benchmark scenarios covering human-vs-animal, animal-vs-animal,
short-term-vs-long-term, reversible-vs-irreversible, and uncertain-sentience
conflicts. Deliverable: `benchmarks/` + `benchmarks/SCHEMA.md`.

### Phase 4 — Open Beta
Public release of the evaluator, invite external use and feedback.
Deliverable: tagged release, `docs/` usage guide.

### Phase 5 — Research Papers
First paper draft per `RESEARCH.md` methodology, submitted for external
review or preprint. Deliverable: `research/papers/`.

### Phase 6 — External Validation
Independent replication or critique by external researchers/reviewers not
affiliated with the founding maintainer(s).

### Phase 7 — Community Governance
Research Council and Ethics Council seats filled by contributors beyond the
founding maintainer, per `GOVERNANCE.md`.

### Phase 8 — Production Framework
Hardened, documented, versioned evaluation framework suitable for
integration into third-party AI development pipelines, with the misuse
boundaries in `SECURITY.md` enforced by design (e.g. mandatory
human-in-the-loop flag in the API).

### Current stage

This repository reflects Phase 0/1 scaffolding. The project's parent
research package tracks progress stage-by-stage; see the linked Multica
project for live status.
