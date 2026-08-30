# Ethical Impact Model

Status: **[PROJECT PROPOSAL]**. Three candidate formulations for an "Ethical
Impact Score," each built from: potential harm, severity, probability,
duration, number of affected beings, sentience confidence, reversibility,
alternative options, potential benefit, and uncertainty.

## Candidate A — Weighted linear sum

```
Score = w1·Severity + w2·Probability + w3·Duration + w4·log(N_affected)
      + w5·SentienceConfidence − w6·Reversibility − w7·AlternativesAvailable
      − w8·Benefit + w9·Uncertainty_penalty
```

**Failure modes:** the weights (`w1…w9`) are themselves value judgments
smuggled into a number that looks objective; linear sums let a large gain on
one dimension silently offset a severe harm on another (the P1/P2
aggregation risk in `docs/ethical-framework.md`); easy to reverse-engineer
and game once the weights are known (see the Anti-Goodhart analysis).

## Candidate B — Multiplicative / gated formulation

```
Score = Severity × Probability × N_affected × (1 − Reversibility) × SentienceConfidence
```

with a hard **veto gate**: if the Human Safety Floor (F0) triggers, the
score is not computed at all — the case routes to human review.

**Failure modes:** a zero in any factor (e.g. fully reversible) zeroes the
whole score, which can hide a real but reversible harm that is still
ethically significant; multiplicative forms resist compensatory gaming
better than linear sums but are harder to interpret and audit (conflicts
with the Transparency Requirement, X3).

## Candidate C — Lexicographic / profile ordering (no single number)

Rank dimensions in a fixed priority order (e.g. irreversible catastrophic
harm to any plausible-sentience being > reversible severe harm > reversible
moderate harm...) and only move to the next-priority dimension when the
current one is tied. Output is an ordered **profile**, not a scalar:
`{harm_profile, benefit_profile, uncertainty_profile,
framework_disagreement_profile}`.

**Failure modes:** lexicographic orderings are brittle at ties and require
someone to fix the priority order in advance, which is itself a contestable
ethical choice — this relocates, rather than removes, the value-laden
weighting problem; harder to use directly as a training signal.

## Which one does this project use?

A single scalar necessarily performs an aggregation across dimensions the
philosophical literature treats as **incommensurable** — value pluralism
holds that in many cases there is no objective ordering across conflicting
values, and any forced ranking is either ad hoc or not truth-tracking ([SEP,
Value Pluralism](https://plato.stanford.edu/entries/value-pluralism/); [Ruth
Chang, *Value
Pluralism*](http://fas-philosophy.rutgers.edu/chang/valuepluralismsubmittedupdate.pdf)).
Given that the Pluralism Meta-Constraint (M0, `docs/ethical-framework.md`)
is a foundational commitment, choosing Candidate A or B as the *sole* output
would itself violate M0 — it would silently pick a resolution to the
aggregation problem and present it as the system's answer.

**Conclusion: this project adopts a multi-dimensional profile (Candidate
C's structure) as the primary output, with a scalar rendering (Candidate A
or B) computed only as one diagnostic view among several, always shown
alongside the disaggregated profile and never as the sole surfaced number.**
`[PROJECT PROPOSAL]` This directly serves the Anti-Goodhart goal in
`docs/ethical-framework.md`: a profile without a single optimization target
is structurally harder to game than a scalar reward. The API's
`overall_assessment.profile` object in `docs/api-spec.md` is the technical
realization of this decision.
