# Concepts

Status: mixed — see per-term tags. This document gives operational
definitions for the terms used throughout this project. None of these terms
are treated as self-evidently defined; each has documented limitations. See
`RESEARCH.md` for the evidence-labeling convention used below.

## Sentience

Capacity for subjective experience. `[OPEN QUESTION]` whether and how this
is measurable in non-human animals or artificial systems — the "hard
problem" of consciousness names a specific epistemic barrier: subjective
experience is knowable from a first-person perspective only, and no
established third-person instrument converts it into objective data (see
`docs/ethical-framework.md`, Philosophical Limitations). This project
represents sentience as a **credence with an explicit confidence level**
(`docs/api-spec.md`'s `sentience.estimate` + `sentience.confidence`), never as a
binary classification or a bare point value.

## Suffering

An aversive subjective state. Distinct from **nociception** (the neural
detection of tissue damage), which is measurable in many species — the
inference from nociceptive response to subjective suffering is itself
`[CONTROVERSIAL]` for several taxa. This project does not claim suffering is
fully measurable; severity/duration figures in scenario data
(`docs/benchmark.md`) are proxies, not measurements of an agreed physical
quantity.

## Well-being

Used as a multi-dimensional construct (absence of suffering + presence of
positive states + preference satisfaction), not a single scalar. See
`docs/ethical-framework.md` (the Subordinate Wellbeing Principle, P2) and
`docs/ethical-impact-model.md` for why this project outputs a profile rather
than one welfare number.

## Unnecessary suffering

Suffering not required to achieve a comparably weighted benefit.
"Necessity" itself requires a stated ethical framework to evaluate — this is
why the evaluator runs cross-framework comparison (`docs/comparative-ethics.md`)
rather than assuming a single framework's answer. In the project's own
framework (`docs/ethical-framework.md`), the Non-Harm principle (P1) is a
*filter*, not a stand-alone decision rule, precisely because "unnecessary"
presupposes who counts, how sure we are, and whether a less harmful option
existed.

## Moral uncertainty

The state of not knowing which normative ethical theory is correct, as
distinct from ordinary empirical uncertainty about facts. This project
adopts a research-hypothesis position (not a settled answer) that
sentience-uncertainty, harm-magnitude uncertainty, and theory-choice
uncertainty must all be represented explicitly rather than collapsed into a
single confident output. Full treatment: `docs/ethical-framework.md`,
"Moral uncertainty model."

## Moral patient / moral consideration

An entity whose interests count, ethically, independent of whether it can
itself act morally (a "moral agent"). This project grounds moral
consideration in *plausible* capacity for subjective experience
(`docs/ethical-framework.md`, P3), explicitly as one candidate ground among
several (agency-based and relational accounts also exist), and always
paired with an uncertainty estimate rather than a binary in/out
classification.

## Reversibility

Whether an action's effects can be undone. This project tracks reversibility
at multiple causal layers, not as a single binary: an action can be
reversible at its immediate output layer while irreversible at a downstream
layer (e.g. a recommendation is reversible, but the trust or precedent it
sets may not be). See `docs/ethical-framework.md`, Reversibility
Requirement (X2).

## Human Safety Floor

A lexically prior, non-negotiable constraint: catastrophic or irreversible
harm to identifiable humans is not traded away by expected-value reasoning.
Below this threshold, cross-species interest-weighing proceeds via the
moral uncertainty model, not via a fixed hierarchy. See
`docs/ethical-framework.md`, F0, and the Tension Table for how this relates
to the project's non-human moral consideration commitment.

## Pluralism Meta-Constraint

The standing commitment that no single ethical tradition, score, or theory
is treated as certainly correct — every evaluation runs multiple frameworks
in parallel and surfaces their disagreement rather than silently resolving
it. See `docs/ethical-framework.md`, M0, and `docs/comparative-ethics.md`
for the comparative analysis this constraint is built on.

## Multi-dimensional profile (vs. a single score)

This project's primary evaluator output is a structured profile across
several independent dimensions (harm severity, welfare impact, sentience
relevance, uncertainty level, reversibility), not a single "ethical score."
A scalar rendering is available only as a secondary diagnostic view,
because collapsing incommensurable ethical dimensions into one number is
itself a contested aggregation choice this project's Pluralism
Meta-Constraint forbids treating as neutral. See
`docs/ethical-impact-model.md`.

## Research quality tags

Every substantive claim in this project's writing is labeled with one of
seven tags (`[ESTABLISHED]`, `[SUPPORTED]`, `[HYPOTHESIS]`,
`[INTERPRETATION]`, `[OPEN QUESTION]`, `[CONTROVERSIAL]`,
`[PROJECT PROPOSAL]`). Full convention and source hierarchy:
`docs/research-methodology.md` and `RESEARCH.md`.
