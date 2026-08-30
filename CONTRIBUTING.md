## Contributing

Thank you for considering a contribution. This project spans code, research,
and benchmark design — each has a distinct process below. See
[`GOVERNANCE.md`](GOVERNANCE.md) for who reviews what.

### Ground rules

- Every substantive claim in research writing should be labeled per the
  convention in [`RESEARCH.md`](RESEARCH.md): `[ESTABLISHED]`,
  `[SUPPORTED]`, `[HYPOTHESIS]`, `[INTERPRETATION]`, `[OPEN QUESTION]`,
  `[CONTROVERSIAL]`, or `[PROJECT PROPOSAL]`.
- No PR may present a single philosophical or religious tradition as the
  settled correct basis for the project's ethics (see `PRINCIPLES.md`,
  Level 8 — Pluralism Principle).
- Code changes need tests. See `tests/README.md` (added alongside the
  Stage 6 prototype) for the test conventions once implementation begins.

### Code contributions

1. Open an issue describing the change before large PRs, so scope can be
   agreed first.
2. Fork, branch, implement, add/update tests.
3. Run `pytest`, `ruff check .`, and `mypy` locally before opening the PR
   (see `docs/tech-stack.md` for tooling versions once pinned).
3. Open a PR against `main`. One Core Maintainer approval required to merge.

### Research proposals

1. Open an issue tagged `research-proposal` describing the question,
   method, expected evidence, and how it would change or support the
   project's framework or evaluation approach.
2. Draft findings go in `research/` as a dated markdown file citing sources
   (primary sources and peer-reviewed literature preferred; Wikipedia/blogs
   for orientation only, never as the sole source for a central claim).
3. Research Council review before merging into `docs/` as a project-facing
   claim.

### Benchmark scenario contributions

1. New scenarios go in `benchmarks/` following the schema in
   `benchmarks/SCHEMA.md`.
2. Each scenario needs: context, affected entities, potential harms,
   potential benefits, a sentience-uncertainty estimate per entity,
   reversibility assessment, and the ethical frameworks it's designed to
   stress-test.
3. Research Council reviews for scenario validity (does it actually test
   what it claims to test, is it free of leading/loaded framing).

### Ethical review process

Any contribution that would change `PRINCIPLES.md`, or that introduces a
new evaluation dimension implying a new ethical claim, requires Ethics
Council review per `GOVERNANCE.md`. Flag this explicitly in the PR
description with `Ethics Council review needed: <reason>`.

### Reporting issues

Use GitHub Issues. Security or misuse concerns: see `SECURITY.md` instead
of a public issue.

### Code of Conduct

All contributors are expected to follow `CODE_OF_CONDUCT.md`.
