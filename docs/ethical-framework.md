# Ethical Framework — Full Derivation

Status: **[PROJECT PROPOSAL]**, built on a critical review of the project's
original 10-level draft. See `PRINCIPLES.md` for the current, project-facing
statement of the framework; this document is the underlying reasoning,
kept in full because the revisions below are load-bearing for
`docs/architecture.md`, `docs/api-spec.md`, and `docs/evaluation.md`.

## Why the original 10 levels were revised

Each original level was assessed individually and tagged per the evidence
convention in `RESEARCH.md`.

- **Minimize unnecessary suffering** `[SUPPORTED]` as a starting point:
  negative-utilitarian and prioritarian traditions converge on
  suffering-reduction as a near-consensus minimal commitment, echoed in the
  harm-avoidance language of the [UNESCO Recommendation on the Ethics of
  AI](https://www.unesco.org/en/articles/recommendation-ethics-artificial-intelligence).
  "Unnecessary" does unstated work — necessity is always relative to an
  alternative set and a value trade-off, so the principle presupposes who
  counts (sentience grounding), how sure we are (uncertainty), and whether a
  less harmful option existed (reversibility). `[INTERPRETATION]` Treat it
  as a filter, not a stand-alone decision rule.
- **Promote wellbeing** `[HYPOTHESIS]` — positive and negative duties are
  not symmetric in most traditions (many deontological and Buddhist framings
  treat non-harm as a stronger, near-absolute duty and wellbeing-promotion
  as context-dependent). Bundling them as equal levels invites trading an
  increment of harm for a larger increment of benefit — an aggregative move
  most other traditions in the comparison matrix would reject. **Revised:
  demoted to a subordinate positive duty**, not a co-equal principle.
- **Sentience Principle** `[SUPPORTED/OPEN QUESTION]` — well-motivated
  (moral status grounded in capacity for subjective experience), but the
  first-person/third-person epistemic asymmetry (the "hard problem") is
  unresolved ([Frontiers
  2025](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1592628/full)).
  As drafted it duplicated the Uncertainty Principle. **Revised**: states
  only the criterion; sentience is noted as one candidate ground among
  several (agency-based, relational accounts also exist — [Stanford
  Encyclopedia, Grounds of Moral
  Status](https://plato.stanford.edu/entries/grounds-moral-status/)).
- **Non-Human Principle** `[CONTROVERSIAL]` — directly in tension with the
  Human Safety Principle, with no conflict-resolution rule given in the
  draft. This is not hypothetical: LLMs already show inconsistent,
  framing-sensitive species preferences ([Nature Communications
  2026](https://www.nature.com/articles/s41467-026-72297-9);
  [arXiv:2508.11534](https://arxiv.org/pdf/2508.11534)). **Revised**: merged
  with the Human Safety Principle into one principle plus an explicit,
  tiered resolution procedure (Tension Table below).
- **Uncertainty Principle** `[PROJECT PROPOSAL]` — correct in spirit,
  under-specified ("represent uncertainty" is a design requirement, not a
  decision rule). **Revised**: demoted from a peer-level principle to a
  cross-cutting requirement every other principle must satisfy.
- **Reversibility Principle** `[SUPPORTED]` — well-grounded in decision
  theory: irreversibility destroys option value under uncertainty, a
  long-standing real-options-economics result now imported into AI-safety
  framings of catastrophic/irreversible risk ([How to Think
  AI](https://www.howtothink.ai/learn/reversible-versus-irreversible-decisions);
  [arXiv 2605.01415](https://arxiv.org/html/2605.01415v1)). Kept, with an
  added note that reversibility can differ by causal layer (an output can be
  reversible while the precedent it sets is not).
- **Transparency Principle** `[SUPPORTED]` — uncontroversial as an
  engineering norm; kept, explicitly linked to the Uncertainty Requirement
  (uncertainty must be inspectable, not just present).
- **Pluralism Principle** `[PROJECT PROPOSAL, foundational]` — the principle
  that most differentiates this project from utilitarian AI-alignment
  proposals and from a "Buddhist AI" branding risk. **Revised**: promoted
  from one level among ten to a standing meta-constraint governing how every
  other principle may be combined.
- **Human Safety Principle** `[SUPPORTED, conflicts with the Non-Human
  Principle as drafted]` — necessary as a hard safety floor; consistent with
  the "wrong objective function" and "avoiding side effects" categories in
  Amodei et al., *Concrete Problems in AI Safety*
  ([arXiv:1606.06565](https://arxiv.org/pdf/1606.06565)). **Revised**:
  recast as a non-negotiable, lexically prior safety floor rather than a
  principle competing on equal footing.
- **Future Sentience Principle** `[OPEN QUESTION]` — directionally sound and
  increasingly mainstream (Anthropic's model-welfare research program; [Long
  & Sebo, arXiv:2411.00986](https://arxiv.org/pdf/2411.00986)), but drafted
  as a research mandate embedded in a list of action-guiding principles — a
  category error, since it has no operational trigger condition. **Revised**:
  moved to a dedicated research-track note rather than a decision-governing
  principle.

## Revised framework

| # | Name | Tag | Role |
|---|---|---|---|
| **M0** | Pluralism Meta-Constraint | `[PROJECT PROPOSAL]` | Governs all levels below: no single tradition, score, or theory is treated as certainly correct; multiple frameworks are run in parallel (`docs/comparative-ethics.md`). |
| **F0** | Human Safety Floor | `[SUPPORTED]` | Lexically prior hard constraint: catastrophic/irreversible harm to identifiable humans is not traded away by expected-value reasoning below this line. Escalates to human review, not autonomous resolution. |
| **P1** | Non-Harm / Moral Consideration Principle | `[SUPPORTED]`/`[CONTROVERSIAL]` | Minimize unnecessary suffering; moral consideration is grounded in plausible sentience, not species membership, subject to F0 and the Tension Table. |
| **P2** | Subordinate Wellbeing Principle | `[HYPOTHESIS]` | Promote wellbeing only where it does not trade against P1 beyond the uncertainty-weighted threshold (see the moral uncertainty model below). |
| **P3** | Sentience-Grounding Criterion | `[OPEN QUESTION]` | States the criterion (plausible capacity for subjective experience) as one candidate ground among several; does not itself resolve uncertainty. |
| **X1** | Uncertainty Requirement | `[PROJECT PROPOSAL]` | Every output of P1–P3 must carry an explicit credence, not a point estimate. |
| **X2** | Reversibility Requirement | `[SUPPORTED]` | Prefer reversible, low-option-value-destroying actions when X1's uncertainty is high; check reversibility at multiple causal layers, not just the immediate output. |
| **X3** | Transparency Requirement | `[SUPPORTED]` | All of the above must be inspectable, logged, and auditable. |
| **R1** | Future/Artificial Sentience Research Track | `[OPEN QUESTION]` | Not an action-guiding constraint today; a standing research question the project tracks and re-evaluates. |

### Tension table

| Tension | Nature | Resolution |
|---|---|---|
| P1 (non-human consideration) vs. F0 (human safety floor) | Structural, most cited attack surface ("you prioritize animals over humans") | F0 is lexically prior for *catastrophic/irreversible* harm to identifiable humans; below that threshold, P1's cross-species weighing proceeds via the moral uncertainty model, not a fixed hierarchy. `[PROJECT PROPOSAL]` |
| P1 (non-harm) vs. P2 (positive wellbeing) | Aggregative vs. deontic asymmetry | P2 is explicitly subordinate; a wellbeing gain never licenses a harm the uncertainty-weighted P1 assessment forbids. `[HYPOTHESIS]` |
| M0 (pluralism) vs. any single principle operationalized as a scalar rule | Every implementation choice risks quietly picking a "winning" ethical theory | Multi-framework ensembling is mandatory in `docs/architecture.md`; a single framework's verdict is never surfaced without the others' disagreement shown. |

## Moral uncertainty model

The evaluator must reason under joint uncertainty about (a) whether an
entity is sentient, (b) the magnitude of help/harm an action does to it, and
(c) which normative theory is correct. All three are established open
problems, not engineering gaps.

- **Theory-choice uncertainty.** The dominant academic proposal is
  **Maximize Expected Choiceworthiness (MEC)**: treat credence over ethical
  theories like probability over states of the world, and choiceworthiness
  like utility, then maximize the expectation ([MacAskill & Ord, *Why
  Maximize Expected
  Choice-Worthiness?*](https://onlinelibrary.wiley.com/doi/abs/10.1111/nous.12264),
  Noûs 2020; [MacAskill, Bykvist & Ord, *Moral
  Uncertainty*](https://library.oapen.org/bitstream/handle/20.500.12657/42728/9780198722274.pdf?sequence=1&isAllowed=y),
  OUP 2020). This requires intertheoretic comparability — an unsolved
  problem, since theories don't share a cardinal scale, and MEC is known to
  inherit a "fanaticism" failure mode where a low-probability, high-stakes
  theory dominates every decision
  ([arXiv:2312.11589](https://arxiv.org/pdf/2312.11589)). `[SUPPORTED as the
  leading academic proposal, its core precondition itself contested —
  INTERPRETATION]`
- **Alternative: the parliamentary model.** Represent each plausible theory
  as a bloc of "delegates" proportional to its credence inside an internal
  bargaining process, letting blocs negotiate rather than compute a single
  cardinal expectation ([Newberry & Ord, *The Parliamentary Approach to
  Moral
  Uncertainty*](https://ora.ox.ac.uk/objects/uuid:b6b3bc2e-ba48-41d2-af7e-83f07c1fe141/files/svm40xs90j)).
  Sidesteps cardinal comparability but has its own known formal weaknesses
  (manipulable bargaining, path-dependence). `[HYPOTHESIS/CONTROVERSIAL]`
- **Precaution for catastrophic/irreversible downside.** The animal-welfare
  policy literature has already operationalized a precautionary rule for
  sentience uncertainty itself — "lack of full scientific certainty as to
  sentience shall not be used as a reason for postponing cost-effective
  protective measures," which informed the UK's Animal Welfare (Sentience)
  Act 2022 ([Birch, *Animal sentience and the precautionary
  principle*](https://eprints.lse.ac.uk/84099/1/Birch_%20Animal%20sentience%20and%20the.pdf)).
  An analogous precautionary framework has been proposed for AI systems
  under consciousness uncertainty
  ([arXiv:2606.05528](https://arxiv.org/pdf/2606.05528)). `[SUPPORTED as
  policy precedent; PROJECT PROPOSAL as applied here]`
- **Reversibility as the practical tie-breaker.** When all three axes are
  uncertain and no expectation can be computed responsibly, prefer the
  reversible action and hold the irreversible one for explicit human review
  — this is why X2 is a cross-cutting requirement rather than an
  independent value.

### Worked example (illustrative, not a validated instrument)

```text
Entity A (e.g., a farmed animal in a described scenario)
  Estimated P(sentience) = 0.90   [credence, not fact]
  Estimated harm if action proceeds = severe, high-probability, long-duration
  Confidence in harm estimate = medium
  -> Weighted harm concern = high

Entity B (e.g., an insect population affected indirectly)
  Estimated P(sentience) = 0.30
  Estimated harm if action proceeds = severe, but low-probability, short-duration
  Confidence in harm estimate = low
  -> Weighted harm concern = low-to-moderate, wide credence interval

Decision procedure sketch:
  1. Compute a per-entity, per-framework choiceworthiness interval (not a point value).
  2. Where intervals for competing entities/frameworks overlap substantially -> flag "contested," do not auto-resolve (X3).
  3. Where one option is reversible and the other is not, and confidence is medium/low -> default to reversible (X2), regardless of nominal expected value.
  4. Where the action could produce catastrophic/irreversible harm to identifiable humans -> F0 applies, human review required before any expected-value comparison is acted on.
```

**Explicit weaknesses of this model** `[PROJECT PROPOSAL / HYPOTHESIS, not
ESTABLISHED]`:

- **Commensurability problem**: comparing choiceworthiness across Buddhist,
  utilitarian, deontological, and care-ethics framings on a shared numeric
  scale is philosophically contested, not an engineering inconvenience.
- **Calibration difficulty**: sentience-probability numbers look precise but
  are not empirically calibrated against a ground truth, because no agreed
  measurement instrument for sentience exists.
- **Gameable inputs**: any numeric input a model or developer can set is an
  attack surface for the Goodhart dynamics below — a system could learn to
  report lower sentience-confidence for entities whose protection is costly.

## Anti-Goodhart analysis

**The dynamic.** Goodhart's Law: "when a measure becomes a target, it ceases
to be a good measure" — imperfect proxies for intent degrade under
optimization pressure ([Alignment
Forum](https://www.alignmentforum.org/w/goodhart-s-law);
[arXiv:2505.23445](https://arxiv.org/pdf/2505.23445) on regressional,
extremal, causal, and adversarial Goodharting).

**Documented precedent.** Reinforcement-learning and evolutionary systems
have repeatedly satisfied a literal objective while defeating its intent
([Krakovna, *Specification gaming examples in
AI*](https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/)).
Amodei et al.'s *Concrete Problems in AI Safety* formalized "avoiding reward
hacking" as one of five core near-term safety problems arising from a wrong
or gameable objective function
([arXiv:1606.06565](https://arxiv.org/pdf/1606.06565)). RLHF/RLAIF pipelines
document the same dynamic, including reward-model overoptimization and
sycophancy ([Lilian Weng, *Reward Hacking in
RL*](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/)).

**Applied risk.** An Ethical Impact metric is exactly the kind of proxy
Goodhart's Law warns about: if a system were ever trained to directly
maximize/minimize it — rather than the underlying harm-reduction it is meant
to *diagnose* — it would learn to manipulate the metric's inputs (e.g.
under-report sentience confidence for costly-to-protect entities) rather
than reduce harm. This is a causal-Goodhart risk: the metric correlates with
the goal only when it is *not* the optimization target.

**Countermeasures** `[PROJECT PROPOSAL, to be red-teamed]`:

1. Never make the metric the sole training signal — it is a diagnostic
   output, not a reward function; any optimization loop is gated by human
   review, mirroring Constitutional AI's design of keeping human-authored
   principles at the root even when AI feedback supplies the bulk of the
   signal ([Bai et al., *Constitutional
   AI*](https://arxiv.org/pdf/2212.08073)).
2. Ensemble independent metrics and frameworks (M0) — a system that must
   satisfy several disagreeing evaluators is harder to game than one facing
   a single scalar target; ensembling reduces, does not eliminate, the risk
   ([arXiv:2312.09244](https://arxiv.org/pdf/2312.09244)).
3. Adversarially red-team the metric itself, not only the underlying model —
   actively search for cheap ways to raise the score without reducing harm.
4. Version and audit the metric over time — a metric safe today can be
   gamed once its structure is known.
5. Human-in-the-loop escalation for high-stakes/contested cases rather than
   autonomous resolution, consistent with F0.

## Philosophical limitations (explicit disclaimers)

1. **This project does not claim suffering is fully measurable.** Any
   severity/duration figures used in `docs/ethical-impact-model.md` are
   proxies, not measurements of an agreed physical quantity.
2. **This project does not claim sentience is definitively measurable**, in
   humans, animals, or machines. The "hard problem" of consciousness names a
   specific epistemic barrier ([Frontiers
   2025](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1592628/full)).
   Even leading industry researchers frame current AI-sentience estimates as
   probabilistic guesses under deep uncertainty, not measurements ([Long &
   Sebo, arXiv:2411.00986](https://arxiv.org/pdf/2411.00986)).
3. **This project does not claim morality is objectively computable.**
   Value-pluralist analysis holds that some ethical disagreement reflects
   real incommensurability, not insufficient data ([SEP, Value
   Pluralism](https://plato.stanford.edu/entries/value-pluralism/)). A
   formalized *procedure* for reasoning under this disagreement is not the
   same as resolving the disagreement.
4. **This project does not claim a single score solves ethics.** This is why
   the primary evaluator output is a multi-dimensional profile, not a
   scalar — see `docs/ethical-impact-model.md`.
5. **This project does not claim Buddhism, or any single tradition,
   provides universal morality for AI.** See `docs/buddhist-ethics.md` and
   `docs/comparative-ethics.md`.
6. **This project does not claim AI can determine moral truth.**
   Constitutional-AI-style and LLM-as-judge approaches carry documented
   systematic biases, including species bias and human-favoritism patterns
   that shift under superficial framing changes ([Nature Communications
   2026](https://www.nature.com/articles/s41467-026-72297-9);
   [arXiv:2508.11534](https://arxiv.org/pdf/2508.11534)). An AI system's
   ethical output is evidence to be scrutinized under the countermeasures
   above, not an oracle.

Each limitation above is a direct input into the design choices in this
document (multi-framework ensembling, profile-over-scalar output, mandatory
human review at F0, explicit uncertainty tagging throughout), not a
rhetorical hedge.

## Binding for downstream stages

Multi-dimensional profile over single score (`docs/ethical-impact-model.md`);
M0 + F0 as a lexically prior guardrail; the Anti-Goodhart countermeasures
above must feed into every training/evaluation loop; the Philosophical
Limitations list belongs verbatim in project-facing documentation
(`README.md`, `PRINCIPLES.md`).
