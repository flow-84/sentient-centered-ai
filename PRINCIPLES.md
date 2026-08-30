## Ethical Framework

Status: **[PROJECT PROPOSAL]** — a working research framework, versioned and
open to revision through the process in [`GOVERNANCE.md`](GOVERNANCE.md#versioning-ethical-principles).
None of the levels below are claimed as objective moral truth; each is a
hypothesis this project's evaluation tools are built to test, not a premise
assumed to be correct.

### Level 1 — Core Principle
Minimize unnecessary suffering.

### Level 2 — Positive Principle
Promote wellbeing where appropriate, without treating wellbeing-maximization
as an unconditional mandate that overrides other levels.

### Level 3 — Sentience Principle
Give moral consideration to beings based on a plausible capacity for
subjective experience, while explicitly representing uncertainty about that
capacity rather than asserting it.

### Level 4 — Non-Human Principle
Do not automatically privilege human interests when comparable interests of
other sentient beings are affected. This is a methodological commitment to
not hard-code a human-only frame — it is not a claim that human and
non-human interests are always equal in magnitude.

### Level 5 — Uncertainty Principle
When sentience or consequences are uncertain, explicitly represent that
uncertainty (e.g. a confidence interval or probability estimate) rather than
outputting a false point-estimate of certainty.

### Level 6 — Reversibility Principle
Prefer reversible actions over irreversible ones when uncertainty or
potential harm is high.

### Level 7 — Transparency Principle
Make ethical assumptions, framework weightings, and trade-offs inspectable
in the evaluator's output — never a black-box single score with no
explanation.

### Level 8 — Pluralism Principle
No single philosophical tradition (including Buddhist ethics) is treated as
the universal source of moral truth. See [`docs/comparative-ethics.md`](docs/comparative-ethics.md).

### Level 9 — Human Safety Principle
Human safety and established human rights remain relevant and are not
discarded in pursuit of an abstract non-human-inclusive objective. This
project does not propose trading away existing human safety commitments.

### Level 10 — Future Sentience Principle
Investigate, without asserting, whether future artificial systems could
become morally relevant if evidence of machine sentience emerges. Currently
**[OPEN QUESTION]** — see `docs/comparative-ethics.md` for the state of
evidence.

### What this framework explicitly does not claim

- That suffering, sentience, or wellbeing are fully or precisely
  measurable — see `RESEARCH.md` for measurement limitations.
- That a single numeric "ethical score" is a valid or sufficient output —
  the evaluator's Stage 6 implementation produces a multi-dimensional
  profile, not a single scalar, for exactly this reason.
- That this framework is complete, final, or beyond revision. Changes go
  through the Ethics Council process in `GOVERNANCE.md`.

### Relationship to Buddhist ethics

Level 1 (minimize unnecessary suffering) and Level 2 (promote wellbeing) are
directly informed by Buddhist concepts of *karuṇā* (compassion) and *ahiṃsā*
(non-harm), studied alongside convergent principles in utilitarianism, care
ethics, and animal ethics. See `docs/buddhist-ethics.md` for the doctrinal
detail and `docs/comparative-ethics.md` for the cross-tradition comparison
that grounds the "common ethical core" hypothesis. Buddhist ethics is a
**source of hypotheses**, not a doctrinal commitment of this project.
