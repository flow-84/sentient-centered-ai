## Roadmap

Roadmap of Moral Circle AI from research to a governed, production-grade
evaluation framework. Every phase lists goal, deliverables, technical tasks,
research tasks, required roles, risks and success criteria. Success criteria
are checkable; a phase is not "done" because time passed.

Evidence labels follow [`RESEARCH.md`](RESEARCH.md). Dates are deliberately
absent: the project is volunteer-driven and phases are gated by criteria, not
by calendar. Status is tracked in the Multica project and in this file.

### Status overview

| Phase | Name | Status |
|---|---|---|
| 0 | Research | done (v0.1 dossier, [`research/research-dossier-stage1.md`](research/research-dossier-stage1.md), Stage 1) |
| 1 | Concept | done (v0.1: question, brand, framework, comparative ethics, Stages 2 to 4) |
| 2 | MVP | prototype done (Ethical Evaluation Layer, Stage 6); hardening open |
| 3 | Benchmark | in progress (12 of 100+ scenarios, schema and validator done) |
| 4 | Open Beta | not started |
| 5 | Research Papers | draft done (`research/paper-draft.md`); submission open |
| 6 | External Validation | not started |
| 7 | Community Governance | structure documented ([`GOVERNANCE.md`](GOVERNANCE.md)); seats unfilled |
| 8 | Production Framework | not started |

Phases overlap. Phase 3 (benchmark growth) and Phase 5 (papers) run in
parallel with Phases 2 and 4. The gates below are the hard ordering.

### Phase 0: Research

- **Goal.** Establish the state of the art and the gap before designing
  anything.
- **Deliverables.** Research dossier with labeled evidence strength; prior-art
  list (including CaML / CompassionML, found in Stage 2); source list.
- **Technical tasks.** Maintain the bibliography in a machine-readable
  format (BibTeX) so papers and docs cite one source of truth.
- **Research tasks.** Literature review across AI ethics, alignment, safety,
  sentience science, moral status, philosophical traditions and regulation
  (EU AI Act, NIST AI RMF, OECD, UNESCO). Re-run the review before every
  paper submission; the field moves fast.
- **Roles.** Research lead, subject-matter reviewers for sentience science
  and moral philosophy.
- **Risks.** Stale or one-sided sources; missed prior art. Mitigation:
  primary sources first, dated entries, open call for missing prior art.
- **Success criteria.** Every central claim in `docs/` traces to a labeled
  source; at least two external readers confirmed no major prior art was
  missed.

### Phase 1: Concept

- **Goal.** Turn the idea into a precise, falsifiable research program.
- **Deliverables.** Research question, nine-part revised principles
  ([`PRINCIPLES.md`](PRINCIPLES.md): M0, F0, P1 to P3, X1 to X3, R1), comparative ethics matrix, candidate
  common ethical core, brand and naming, governance draft.
- **Technical tasks.** None beyond repository scaffolding and CI.
- **Research tasks.** Operationalize sentient, suffering, well-being and
  unnecessary suffering; stress-test the principles in the critical review
  (Stage 8).
- **Roles.** Applied ethicist, philosopher, science communicator.
- **Risks.** Hidden single-tradition bias; overclaiming measurability.
  Mitigation: Pluralism principle, explicit limitations, Ethics Council
  review.
- **Success criteria.** The principles survived the critical review with
  all severity-high weaknesses either fixed or documented as open.

### Phase 2: MVP

- **Goal.** A working Ethical Evaluation Layer: prompt, response, context and
  affected entities in; multi-dimensional assessment out, with uncertainty
  and framework comparison.
- **Deliverables.** `src/` implementation, API per
  [`docs/api-spec.md`](docs/api-spec.md), tests, examples, install guide.
- **Technical tasks.** Replace placeholder heuristics with pluggable
  evaluators (rule-based, LLM-as-judge, ensemble); pin dependencies; add
  type checking and CI gates; add the mandatory human-review flag to every
  response.
- **Research tasks.** Compare evaluator backends on the benchmark;
  document where each fails.
- **Roles.** ML engineer, backend engineer, safety reviewer.
- **Risks.** The score is read as objective morality; the evaluator is
  gamed (Goodhart). Mitigation: multi-dimensional profile instead of one
  score, no single "ethical" verdict, red-team suite in CI.
- **Success criteria.** `pytest`, `ruff`, `mypy` green; the example
  scenarios run end to end from a clean install in the documented steps;
  no response contains a verdict without uncertainty fields.

### Phase 3: Benchmark

- **Goal.** At least 100 scenarios with interest conflicts across species,
  time horizons, reversibility and uncertain sentience.
- **Deliverables.** `benchmarks/scenarios/` (currently 12), schema and
  validator, scenario contribution process, dataset card.
- **Technical tasks.** Scenario validator in CI, coverage report per
  conflict category, versioned dataset releases, optional Hugging Face
  mirror.
- **Research tasks.** Annotation protocol; inter-rater agreement on a
  subset; document that scenarios have no single correct answer, only
  defensible reasoning ranges.
- **Roles.** Benchmark curator, domain experts (animal welfare, ecology,
  Buddhist ethics, human rights), annotators.
- **Risks.** Contributor bias skews categories; scenarios leak into
  training data. Mitigation: category quotas, held-out private split,
  contributor diversity checks.
- **Success criteria.** 100 or more valid scenarios; no category below its
  quota; agreement statistics published, including bad numbers.

### Phase 4: Open Beta

- **Goal.** External people use the evaluator and tell us where it breaks.
- **Deliverables.** Tagged pre-release (`v0.x`), PyPI package, hosted docs,
  public issue triage, beta feedback report.
- **Technical tasks.** Packaging, semantic versioning, rate-limited
  reference API for local use, documented threat model, telemetry off by
  default.
- **Research tasks.** Collect failure cases; run the first experiments
  from the planned experiment list (to be added under `research/experiments/`;
  each with hypothesis, dataset, method, metrics, expected result and failure
  conditions).
- **Roles.** Maintainers, release manager, community manager.
- **Risks.** Misuse in high-risk settings; reputational damage from a bad
  output screenshot. Mitigation: the misuse boundaries in
  [`SECURITY.md`](SECURITY.md), visible disclaimers, human-in-the-loop flag
  required.
- **Success criteria.** At least 10 external users outside the founding
  group file issues or scenarios; no critical security finding open.

### Phase 5: Research Papers

- **Goal.** Peer-visible, citable research output.
- **Deliverables.** Preprint (arXiv) from `research/paper-draft.md`, a
  benchmark dataset paper, replication package.
- **Technical tasks.** Reproducibility scripts, fixed seeds, archived
  releases (Zenodo DOI).
- **Research tasks.** Run the first ten experiments with preregistered
  hypotheses and failure conditions; report negative results.
- **Roles.** Research lead, statistician, external co-reviewers.
- **Risks.** Overclaiming; selective reporting. Mitigation: preregistration
  in the repository, labels per `RESEARCH.md`.
- **Success criteria.** Preprint public; replication package runs from a
  clean checkout; at least one submission to a workshop or journal.

### Phase 6: External Validation

- **Goal.** People who do not depend on the project judge it.
- **Deliverables.** Independent replication or critique reports, published
  as received, plus our response.
- **Technical tasks.** Support for third-party evaluators and datasets;
  stable API for replication.
- **Research tasks.** Invite critique from sentience science, AI safety,
  philosophy and Buddhist studies; commission at least one adversarial
  review.
- **Roles.** External reviewers (no merge rights), Research Council.
- **Risks.** Reviewers are all friendly; negative findings are ignored.
  Mitigation: recruit named critics, publish unedited reports.
- **Success criteria.** At least two independent reports, one of them
  critical, published; every severity-high finding has a tracked response.

### Phase 7: Community Governance

- **Goal.** The project no longer depends on its founders.
- **Deliverables.** Seated Research Council and Ethics Council, rotation
  rules, conflict-of-interest register, decision log in `docs/decisions/`.
- **Technical tasks.** Repository permissions aligned to roles; release
  process that does not need a single person.
- **Research tasks.** Review the principles through the council process
  and publish version 1.0 of `PRINCIPLES.md` or a reasoned decision not to.
- **Roles.** Two or more Core Maintainers, council members across more than
  one tradition.
- **Risks.** Capture by a single group; governance without participants.
  Mitigation: tradition-diversity requirement, term limits, public votes.
- **Success criteria.** Both councils seated with members who are not
  founding maintainers; one principle change completed through the full
  documented process.

### Phase 8: Production Framework

- **Goal.** A stable, versioned framework other teams can integrate without
  contacting us.
- **Deliverables.** `v1.0` release, long-term support policy, integration
  guides, audit log format, deprecation policy.
- **Technical tasks.** Backward-compatible API, benchmark versioning,
  signed releases, SBOM, performance budget.
- **Research tasks.** Longitudinal drift study of evaluator results across
  model generations; annual review of the ethical core.
- **Roles.** Release manager, security engineer, maintainers, councils.
- **Risks.** Use as an autonomous decision authority in high-risk domains.
  Mitigation: mandatory human-in-the-loop flag enforced by the API, refusal
  paths for the use cases excluded in `SECURITY.md`.
- **Success criteria.** Two independent integrations in use; security
  review passed; no unresolved severity-high weakness from the critical
  review.

### Gates

1. Phase 4 starts only when Phase 2 success criteria and the Phase 3 first
   milestone (50 valid scenarios) are met.
2. Phase 5 submission requires the preregistered experiments to be run, not
   described.
3. Phase 8 requires Phase 6 and Phase 7 criteria, not only engineering
   readiness.

### Current stage

The repository reflects the output of planning Stages 1 to 8 (research,
brand, framework, architecture, repository, prototype, documentation,
critical review). Website content, marketing and community plans are in
[`docs/website-structure.md`](docs/website-structure.md),
[`docs/marketing-strategy.md`](docs/marketing-strategy.md) and
[`docs/community-strategy.md`](docs/community-strategy.md). No website has
been deployed; publishing is a maintainer decision.
