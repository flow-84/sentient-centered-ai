# Research Methodology

This document expands on the evidence-labeling convention and source
hierarchy defined in `RESEARCH.md` (read that file first — it is the
canonical, project-facing statement). This document adds the operational
detail relevant to contributors doing research work for this project.

## Handling contradictory sources

When sources disagree on a factual or scholarly matter:

1. Compare the sources directly rather than picking one silently.
2. Weigh recency — a 2026 finding supersedes a 2015 finding on a fast-moving
   empirical question (e.g. LLM bias measurement), but not necessarily on a
   settled philosophical debate.
3. Prefer the primary source over a secondary summary when they diverge.
4. Document the conflict explicitly in the writing (e.g. "`[CONTROVERSIAL]`
   — X argues A, Y argues B") rather than resolving it by omission. See
   `docs/comparative-ethics.md` and `docs/buddhist-ethics.md` for examples
   of this applied to genuine scholarly disagreement (e.g. Goodman's
   consequentialist reading of Buddhist ethics vs. Keown's virtue-ethics
   reading).

## Why research/ and docs/ are separate

`research/` holds working notes, literature summaries, and drafts —
attributable, dated, and revisable. `docs/` holds the project-facing
synthesis once Research Council review (`GOVERNANCE.md`) has occurred.
Claims do not move from `research/` into `README.md`, `PRINCIPLES.md`, or
other root-level files without that review step. This is not bureaucratic
overhead — it is the mechanism that keeps a single contributor's unreviewed
literature read from silently becoming a project-endorsed claim.

## Applying the moral-uncertainty standard to research writing itself

The project's stance on moral uncertainty (`docs/ethical-framework.md`) is
not only a technical design choice for the evaluator — it is also the
standard this project's own research writing is held to. A claim about
which ethical theory is "correct," or which philosophical tradition should
ground the evaluator, would violate the Pluralism Meta-Constraint (M0) if
asserted as settled. This is why `docs/comparative-ethics.md` and
`docs/buddhist-ethics.md` present a matrix and per-tradition analysis rather
than a ranked recommendation.

## Currency of research

Research must reflect the state of the field at the time it is conducted.
When citing benchmarks, standards, or regulatory developments (e.g. the EU
AI Act, NIST AI RMF, UNESCO Recommendation), check for amendments or
successor documents before citing a version as current — regulatory and
benchmark landscape in AI governance changes quickly. If a source's
publication date is more than roughly two years old at the time of writing,
verify it is still the current authoritative version rather than assuming
it, especially for anything with regulatory or platform-specific content.

## What research writing must never claim

Per `docs/ethical-framework.md`'s Philosophical Limitations section, no
document in this repository claims: that suffering or sentience are fully
measurable; that morality is objectively computable; that Buddhism or any
single tradition provides universal AI ethics; or that this project's
evaluator can determine moral truth rather than produce an inspectable,
falsifiable research heuristic. Any PR introducing language that implies
otherwise should be flagged in review (`CONTRIBUTING.md`, ethical review
process).
