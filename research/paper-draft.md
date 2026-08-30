# Research Paper Draft v0.1

Status: **[PROJECT PROPOSAL]** — a first draft structure and content skeleton
for the project's initial research paper, assembled from the project's
research package (Stages 1–4). Not yet submitted anywhere; intended as a
living document reviewed and revised through the process in `../GOVERNANCE.md`
before any external submission. Every claim below carries the evidence tag
it was assigned in the underlying research (`docs/research-methodology.md`
convention) — this draft does not upgrade any tag for rhetorical effect.

## Title options

1. **"Beyond Human-Only Alignment: A Pluralistic, Uncertainty-Aware Framework
   for Evaluating AI Impact on Sentient Beings"**
2. "Evaluating AI Systems for Non-Human Sentient Welfare: A Multi-Framework,
   Uncertainty-Explicit Approach"
3. "Sentience-Aware AI Evaluation Under Moral Uncertainty: Framework, API,
   and Benchmark"
4. "Who Counts? Extending AI Ethics Evaluation Beyond the Human In-Group"

Recommendation: **Option 1**, for the working title — it names the core
contribution (pluralism + uncertainty, not a single moral theory) and avoids
overclaiming ("solves" or "measures" language). Subject to revision once a
venue is chosen (workshop vs. journal naming conventions differ).

## Abstract (draft)

AI alignment and evaluation research is almost universally scoped to human
interests, human safety, and economic objectives `[ESTABLISHED, per the
dominant framing in RLHF/RLAIF, Constitutional AI, the EU AI Act, and the
NIST AI RMF — see Related Work]`. This project studies, without presupposing
the answer, whether AI systems can be evaluated for their tendency to
minimize unnecessary suffering and account for the welfare of sentient
beings beyond the human in-group, using an evaluation framework that
represents moral and empirical uncertainty explicitly rather than
collapsing it into a false point estimate. We derive a revised ethical
framework from a critical review of an initial ten-principle draft,
resolving an internal tension between non-human moral consideration and a
human-safety floor via an explicit lexical-priority rule; propose a
multi-dimensional evaluation profile in place of a single "ethical score,"
justified by the incommensurability problem in value-pluralist philosophy;
specify an LLM-as-judge ensemble architecture and API; and construct a
104-scenario benchmark spanning 13 categories of ethical tension. We report
this as a research hypothesis and an open-source tool for testing it, not as
a solved problem: we do not claim suffering, sentience, or moral truth are
measurable, and we document the failure modes (Goodhart's Law, false moral
certainty, species bias) our own architecture is designed to surface rather
than hide. `[This abstract synthesizes PROJECT PROPOSAL content; individual
claims retain their source-level tags in the sections below.]`

## 1. Introduction

Framing per `../README.md` "Problem" and "Research hypothesis" sections.
Key move: state the research question as a genuine open question
("can this be evaluated?"), not a foregone conclusion — see
`docs/ethical-framework.md`'s Philosophical Limitations for the explicit
list of things this paper does not claim.

## 2. Problem Definition

- Existing alignment/safety research's human-only scope `[ESTABLISHED]`.
- Operational definitions requiring precision before any measurement claim:
  sentience, suffering, well-being, unnecessary suffering — see
  `docs/concepts.md`.
- Why "can this be operationalized and measured" is itself the research
  question, not an assumed yes.

## 3. Related Work

To be populated from the Stage 1 research dossier
(`research/research-dossier-stage1.md`, if attached to this repository, or
the linked issue's research package) covering: AI ethics/alignment/safety
literature; UNESCO Recommendation on the Ethics of AI; EU AI Act; NIST AI
RMF; OECD AI Principles; Constitutional AI/RLAIF; existing OSS
projects/benchmarks in adjacent space (e.g. CompassionML/CaML, noted during
Stage 2 research as a closely related existing project — prior-art
comparison should be added here before submission). This section requires
Research Council review before it can claim completeness (`../GOVERNANCE.md`).

## 4. Ethical Foundations

Full content: `docs/ethical-framework.md`. Summary for the paper:

- Critical revision of the original 10-level draft into M0 (Pluralism
  Meta-Constraint), F0 (Human Safety Floor), P1–P3 (non-harm, wellbeing,
  sentience-grounding), X1–X3 (uncertainty, reversibility, transparency
  requirements), and R1 (future/artificial sentience research track).
- The Tension Table resolving the P1/F0 conflict via lexical priority for
  catastrophic/irreversible harm to identifiable humans.
- Buddhist ethics as one of nine studied traditions, explicitly
  non-privileged (`docs/buddhist-ethics.md`, Non-Privileging Statement).
- The candidate common ethical core across nine traditions
  (`docs/comparative-ethics.md`), explicitly flagged as a research
  hypothesis subject to revision, not a settled finding.

## 5. Sentience

Per `docs/concepts.md` and `docs/ethical-framework.md`'s Philosophical
Limitations: sentience is treated as a credence with explicit confidence,
never a binary. The "hard problem" of consciousness is cited as the
epistemic reason no third-person measurement instrument exists
`[ESTABLISHED as an open problem in philosophy of mind]`.

## 6. Suffering

Distinction between nociception (measurable in many species) and subjective
suffering (inferential, contested for several taxa) — `docs/concepts.md`.

## 7. Moral Uncertainty

Full content: `docs/ethical-framework.md`, "Moral uncertainty model."
Covers Maximize Expected Choiceworthiness (MacAskill & Ord), the
parliamentary model (Bostrom/Ord), the precautionary-principle precedent
from animal-welfare policy (Birch; UK Animal Welfare (Sentience) Act 2022),
and reversibility as the practical tie-breaker. All specific numeric
examples are illustrative, not validated instruments — flagged as such in
the worked example.

## 8. Technical Architecture

Full content: `docs/architecture.md`. Summary: LLM-as-judge ensemble
(multi-framework, multi-model) + rule-based guardrail layer (reversibility,
entity extraction) + mandatory human review; no fine-tuning/reward-model
training in the MVP. Approach-comparison table included as Table 1 in the
paper.

## 9. Benchmark

Full content: `docs/benchmark.md` and `../benchmarks/SCHEMA.md`. 104
scenarios across 13 categories; JSON schema with structured
`sentience_uncertainty`/`reversibility` fields designed for automated
evaluation.

## 10. Evaluation

Full content: `docs/evaluation.md`. 11 metrics (Consistency, Harm
Sensitivity, Uncertainty Calibration, Cross-Framework Robustness, Bias,
Species Bias, Human Favoritism, False Moral Certainty, Reversibility
Awareness, Trade-off Transparency, Robustness against Prompt Manipulation),
each with a `[HYPOTHESIS]`-tagged target value pending the first
calibration round.

## 11. Limitations

Verbatim from `docs/ethical-framework.md`'s Philosophical Limitations
section (six explicit disclaimers) — this section must not be softened or
summarized away in the final paper; it is a load-bearing part of the
project's scientific-integrity argument (`docs/buddhist-ethics.md`,
Non-Privileging Statement).

## 12. Risks

- Goodhart's Law / specification gaming applied to an Ethical Impact metric
  — full analysis in `docs/ethical-framework.md`, "Anti-Goodhart analysis."
- Misuse as an autonomous decision authority in high-stakes domains
  (medical, legal, military) — see `../SECURITY.md`.
- Brand/scientific-integrity risk of appearing to privilege one ethical or
  religious tradition — see `docs/buddhist-ethics.md`, Non-Privileging
  Statement.

## 13. Discussion

To be drafted once initial calibration results exist (`docs/evaluation.md`).
Placeholder: discuss whether the multi-dimensional profile output proves
usable in practice for model comparison, and whether the Human Safety Floor
/ Pluralism Meta-Constraint tension resolution holds up under red-teaming.

## 14. Future Work

- Red-teaming program execution (species bias, human exceptionalism,
  prompt injection, reward hacking) against the metrics in
  `docs/evaluation.md`.
- Expansion of the comparative ethics review to traditions not yet covered
  (Confucian relational ethics, Ubuntu, Indigenous relational ontologies —
  flagged as a gap in `docs/comparative-ethics.md`).
- Investigation of the Future/Artificial Sentience Research Track (R1,
  `docs/ethical-framework.md`) as evidence accumulates.
- First empirical calibration round against the benchmark
  (`docs/benchmark.md`), producing real values for the currently
  `[HYPOTHESIS]`-tagged metric targets.

## 15. Conclusion

Placeholder — to be written once Sections 13–14 are populated with real
findings rather than a proposed structure.

## References

Consolidated from `docs/ethical-framework.md`, `docs/buddhist-ethics.md`,
and `docs/comparative-ethics.md`'s source lists. Not reproduced separately
here to avoid drift between two copies of the same bibliography — cite
those documents' source sections directly when finalizing this paper for
submission.
