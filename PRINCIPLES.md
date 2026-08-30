## Ethical Framework

Status: **[PROJECT PROPOSAL]** — a working research framework, versioned and
open to revision through the process in [`GOVERNANCE.md`](GOVERNANCE.md#versioning-ethical-principles).
None of the principles below are claimed as objective moral truth; each is a
hypothesis this project's evaluation tools are built to test, not a premise
assumed to be correct.

This is the **revised** framework, produced by a critical review of an
initial 10-level draft (kept, with the full derivation and per-principle
evidence tags, in
[`docs/ethical-framework.md`](docs/ethical-framework.md)). The review found
two structural problems in the original draft — an unresolved conflict
between non-human moral consideration and human safety, and principles that
mixed action-guiding rules with cross-cutting requirements and research
mandates — and restructured the framework accordingly.

### M0 — Pluralism Meta-Constraint
Governs every principle below: no single tradition, score, or theory is
treated as certainly correct; multiple ethical frameworks are run in
parallel and their disagreement is surfaced, not silently resolved. See
[`docs/comparative-ethics.md`](docs/comparative-ethics.md).

### F0 — Human Safety Floor
A lexically prior, non-negotiable constraint: catastrophic or irreversible
harm to identifiable humans is not traded away by expected-value reasoning.
Escalates to human review, not autonomous resolution.

### P1 — Non-Harm / Moral Consideration Principle
Minimize unnecessary suffering. Moral consideration is grounded in
plausible sentience, not species membership — subject to F0 and the
explicit conflict-resolution rule in
[`docs/ethical-framework.md`](docs/ethical-framework.md#tension-table). This
is a methodological commitment to not hard-code a human-only frame — it is
not a claim that human and non-human interests are always equal in
magnitude.

### P2 — Subordinate Wellbeing Principle
Promote wellbeing only where it does not trade against P1 beyond the
uncertainty-weighted threshold in the moral uncertainty model
([`docs/ethical-framework.md`](docs/ethical-framework.md)) — wellbeing
promotion does not override the non-harm principle.

### P3 — Sentience-Grounding Criterion
Give moral consideration to beings based on a plausible capacity for
subjective experience, stated as one candidate ground among several
(agency-based and relational accounts also exist). Does not itself resolve
uncertainty about that capacity — see X1.

### X1 — Uncertainty Requirement
When sentience or consequences are uncertain, every evaluation must carry
an explicit credence, not a point estimate presented as certain.

### X2 — Reversibility Requirement
Prefer reversible actions over irreversible ones when uncertainty or
potential harm is high; check reversibility at multiple causal layers, not
just the immediate output.

### X3 — Transparency Requirement
Make ethical assumptions, framework weightings, and trade-offs inspectable
in the evaluator's output — never a black-box single score with no
explanation.

### R1 — Future/Artificial Sentience Research Track
Investigate, without asserting, whether future artificial systems could
become morally relevant if evidence of machine sentience emerges. Currently
**[OPEN QUESTION]**, tracked as a standing research question rather than an
action-guiding principle — see
[`docs/ethical-framework.md`](docs/ethical-framework.md) for why this was
demoted from the original draft's "Level 10" and
[`docs/comparative-ethics.md`](docs/comparative-ethics.md) for the state of
evidence.

### The central tension, made explicit

P1 (non-human moral consideration) and F0 (human safety floor) are in
structural tension — the most common objection this project expects
("you prioritize animals over humans"). The resolution: F0 is lexically
prior for *catastrophic/irreversible* harm to identifiable humans; below
that threshold, P1's cross-species weighing proceeds via the moral
uncertainty model, not a fixed hierarchy. Full tension table:
[`docs/ethical-framework.md`](docs/ethical-framework.md#tension-table).

### What this framework explicitly does not claim

- That suffering, sentience, or wellbeing are fully or precisely
  measurable — see `RESEARCH.md` for measurement limitations.
- That a single numeric "ethical score" is a valid or sufficient output —
  the evaluator produces a multi-dimensional profile, not a single scalar,
  for exactly this reason. See
  [`docs/ethical-impact-model.md`](docs/ethical-impact-model.md).
- That this framework is complete, final, or beyond revision. Changes go
  through the Ethics Council process in `GOVERNANCE.md`.

### Relationship to Buddhist ethics

P1 (non-harm) and P2 (wellbeing) are directly informed by Buddhist concepts
of *karuṇā* (compassion) and *ahiṃsā* (non-harm), studied alongside
convergent principles in utilitarianism, care ethics, and animal ethics. See
[`docs/buddhist-ethics.md`](docs/buddhist-ethics.md) for the doctrinal
detail and [`docs/comparative-ethics.md`](docs/comparative-ethics.md) for
the cross-tradition comparison that grounds the "common ethical core"
hypothesis. Buddhist ethics is a **source of hypotheses**, not a doctrinal
commitment of this project — see `docs/buddhist-ethics.md`'s
Non-Privileging Statement.
