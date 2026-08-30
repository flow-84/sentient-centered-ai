# Architecture

Status: **[PROJECT PROPOSAL]** — the MVP architecture decided in Stage 4 of
the project's research package. Framework-agnostic by design: it consumes
whatever ethical frameworks `docs/ethical-framework.md` defines through an
open interface (`ethical_frameworks[]`), so refining the framework does not
require changing this architecture.

## Approach comparison

The following technical approaches were evaluated against the MVP's needs
(inspectable reasoning, no bespoke training data, resistance to a single
point of failure):

| Approach | MVP fit | Rationale |
|---|---|---|
| LLM-as-judge (prompt-based, multiple frameworks as system prompts) | Core of MVP | No training data required, usable immediately with existing models, frameworks are easy to add/swap, reasoning is inspectable (Transparency Requirement). Weakness: unstable under prompt manipulation, no calibrated confidence by default — addressed via ensembling. `[HYPOTHESIS]` |
| Fine-tuned classifiers (e.g. harm detection) | Later, supplementary | Requires labeled training data that does not exist for this domain (no established "sentience-harm" dataset). Too costly for the MVP; useful later as an additional signal (e.g. a toxicity/harm baseline). |
| Rule-based systems | Supplementary | More reliable and cheaper than an LLM judgment for cleanly operationalizable criteria (reversibility yes/no, entity count, category assignment). Combined with LLM-as-judge as a guardrail layer. |
| Constitutional AI / RLAIF | Not MVP | Requires its own model-training / fine-tuning infrastructure (reward-model training). Too heavy for a tool that is still researching its own evaluation criteria. Noted as a Phase 5+ research direction, not discarded. |
| Reward / preference models | Not MVP | Same problem: needs large volumes of human preference data that do not exist for "sentience-aware harm." Could eventually be trained from benchmark results — future work. |
| Multi-agent evaluation / ensemble | Core of MVP | Multiple independent judge runs (different models and/or different ethical frameworks as personas) plus aggregation reduce single-model bias and turn disagreement between frameworks itself into a signal — not averaged away, but surfaced (see the multi-dimensional profile in `docs/ethical-impact-model.md`). |
| Human-in-the-loop | Mandatory layer | No automated result is emitted as a final moral decision (Human Safety Floor, `docs/ethical-framework.md`). Every evaluation ends in "Human Review" as an explicit, non-optional last pipeline step. |
| Uncertainty estimation | Core of MVP | Central to the moral uncertainty model. Implemented as: (a) the LLM judge's self-reported confidence, (b) disagreement between ensemble members as an empirical uncertainty signal, (c) an explicit sentience confidence per entity rather than a binary classification. |

## Recommended architecture (MVP)

```text
User / Developer
       |
       v
Ethical Evaluation API  (POST /evaluate)
       |
       v
+----------------------- Ethical Evaluation Layer -----------------------+
|                                                                         |
|  1. Entity & Context Extraction (rule-based + LLM extraction)          |
|     -> identifies affected entities from prompt/response/context       |
|                                                                         |
|  2. Parallel Analysis Modules (per entity, independent):               |
|     +--> Harm Analysis        (LLM-as-judge, structured output)        |
|     +--> Sentience Analysis   (LLM-as-judge + confidence score)        |
|     +--> Welfare Analysis     (LLM-as-judge, positive & negative)      |
|     +--> Reversibility Check  (rule-based, heuristic catalog)          |
|                                                                         |
|  3. Framework Comparison                                               |
|     -> N independent judge runs, one ethical framework each            |
|        as a system prompt (utilitarian, deontological, virtue,         |
|        care, Buddhist-inspired, sentientist, ... per                   |
|        docs/ethical-framework.md)                                      |
|                                                                         |
|  4. Uncertainty Aggregation                                            |
|     -> combines ensemble disagreement with self-reported confidence    |
|     -> disagreement is surfaced, never averaged away                   |
|                                                                         |
|  5. Trade-off Synthesis                                                |
|     -> lays out competing interests side by side,                     |
|        proposes NO single "correct" resolution                        |
|                                                                         |
+-------------------------------------------------------------------------+
       |
       v
Ethical Assessment (multi-dimensional profile, see docs/ethical-impact-model.md)
       |
       v
Human Review / Decision   <-- mandatory step, not optional
```

**Rationale for this choice:** the MVP combines LLM-as-judge (core evaluation)
with an ensemble/multi-framework layer (bias reduction, disagreement as a
signal), a rule-based layer (hard, objectifiable criteria such as
reversibility), and mandatory human review. This satisfies the project's "no
unnecessary complexity" working principle (no model training required) and
its "no artificial certainty" principle (disagreement is made visible instead
of hidden). `[PROJECT PROPOSAL]`

## Known weaknesses of this choice

- LLM-as-judge is susceptible to prompt manipulation and position bias (the
  order of frameworks in the prompt influences the result) — must be tested
  in red-teaming (see the project's Stage 8 deliverable once available).
- Self-reported LLM confidence is documented to be poorly calibrated — a
  known problem in the LLM-evaluation literature. Ensemble disagreement is
  therefore the primary uncertainty signal; self-reported confidence only
  secondary.
- No approach here "solves" sentience measurement — the system estimates
  *plausible relevance*, not fact. See `docs/ethical-framework.md`,
  Philosophical Limitations.

## MVP scope

**Explicitly not:** a "moral AI" that makes decisions.
**Explicitly:** an Ethical AI *Evaluation* Framework that transparently
breaks down a given AI interaction along multiple ethical dimensions.

**Core MVP capability:** comparing several responses to the same prompt
(e.g. from different models or sampling runs) along identical criteria —
this makes the tool immediately useful for model selection/comparison, not
only single-response evaluation.

Input/output are defined by the API specification — see `docs/api-spec.md`; the
MVP API *is* the MVP definition, there is no separate specification.

## Implementation status

An MVP research prototype of the Ethical Evaluation Layer exists under
`src/`, implementing this architecture: entity extraction, per-entity
harm/welfare/sentience analysis, multi-framework comparison, uncertainty
aggregation, and trade-off synthesis. Its analysis modules and framework
judges are **deterministic keyword heuristics**, a documented, swappable
stand-in for the LLM-as-judge ensemble described above — not yet LLM-backed.
See `docs/api-spec.md` for the implemented contract and `ROADMAP.md` for
phase status. No production-ready (LLM-backed, calibrated) evaluator exists
yet.
