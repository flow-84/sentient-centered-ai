# Buddhist Ethics & AI — Research Track

Status: mixed — see per-claim tags. This is a **research track**, not a
doctrinal commitment. See `docs/comparative-ethics.md` for how Buddhist
ethics relates to the other eight traditions studied, and the
Non-Privileging Statement below for why no tradition, including this one, is
treated as authoritative.

Every concept below is split into four categories, applied uniformly: what
the historical doctrine says, how scholars interpret it philosophically,
how it has been adapted secularly, and what (if anything) is a testable
technical hypothesis for this project.

## Core concepts

### Karuna (compassion) and Metta (loving-kindness)

In the Theravada canon, *karuna* and *metta* are two of the four "sublime
abodes" (*brahmavihara*), alongside *mudita* (empathic joy) and *upekkha*
(equanimity) `[ESTABLISHED]` (Harvey, *An Introduction to Buddhist Ethics*,
Cambridge University Press, 2000).

- *Historical doctrine*: meditative cultivations aimed at generating
  goodwill and a wish to relieve suffering in all beings, not merely a
  private feeling-state.
- *Philosophical interpretation*: scholars debate whether karuna in early
  Buddhism is best read as a virtue (a trained disposition of character) or
  a quasi-consequentialist commitment to reducing suffering wherever it
  occurs. Goodman argues for the latter, holding that "every version of
  Buddhist ethics takes the welfare of sentient beings to be the only
  source of moral obligations" (Goodman, *Consequences of Compassion*,
  Oxford University Press, 2009) `[INTERPRETATION — contested]`; Keown reads
  Buddhist ethics through an Aristotelian, character-based lens instead
  (Keown, *The Nature of Buddhist Ethics*, 1992).
- *Modern secular adaptation*: contemporary compassion-cultivation training
  and secular mindfulness programs strip metta/karuna practices of
  metaphysical commitments (rebirth, karma) and present them as trainable
  prosocial dispositions `[SUPPORTED, though effect sizes and mechanisms
  remain debated — OPEN QUESTION]`.
- *Technical/AI hypothesis*: an AI evaluation layer could operationalize a
  "karuna-inspired" objective as an explicit term rewarding reduction of
  modeled suffering/distress across affected entities, distinct from
  user-satisfaction or engagement metrics `[HYPOTHESIS]`. Whether such a
  term is measurable without smuggling in unjustified certainty about who
  suffers is itself `[OPEN QUESTION]`.

### Ahimsa (non-harm)

Described by Harvey as "generally regarded as a distinguishing mark of
Dhamma," shared with Jain and Hindu traditions rather than unique to
Buddhism `[ESTABLISHED]`.

- *Historical doctrine*: the first of the five precepts (*pancasila*) is to
  abstain from taking life, extended canonically to non-human animals.
- *Philosophical interpretation*: disagreement about whether ahimsa
  functions as an absolute deontological constraint or a strong but
  defeasible presumption overridable in extreme circumstances
  `[CONTROVERSIAL]`.
- *Modern secular adaptation*: "non-harm as default, harm as exception
  requiring justification" appears independently in secular bioethics and
  AI-safety framings `[SUPPORTED as an independently-arising pattern]`.
- *Technical/AI hypothesis*: "prefer the action set with lowest expected
  harm unless a justified, inspectable exception is logged" is a direct
  translation of ahimsa into an engineering constraint `[PROJECT
  PROPOSAL]`.

### Dukkha (suffering) and dependent origination (pratityasamutpada)

*Dukkha* in the canonical Four Noble Truths is a technical term covering not
only acute pain but the pervasive unsatisfactoriness of conditioned
existence `[ESTABLISHED]`. Dependent origination — arising in dependence
upon conditions, nothing exists as a singular independent entity — is the
causal-relational metaphysic underlying Buddhist analysis of suffering
`[ESTABLISHED as canonical doctrine]`.

- *Philosophical interpretation*: some scholars read this as grounding a
  relational ethics of interdependence, an alternative to atomistic,
  individual-rights-based or utilitarian modeling `[INTERPRETATION]`.
- *Modern secular adaptation*: systems-thinking and ecological ethics
  independently converge on relational/interdependence framings without
  reference to Buddhism `[SUPPORTED as convergent, not derivative]`.
- *Technical/AI hypothesis*: harm/impact modeling should represent affected
  entities as embedded in causal networks (second- and third-order
  effects), not isolated endpoints `[PROJECT PROPOSAL]`.

### Craving / attachment (tanha, upadana)

Canonically, *tanha* is the proximate cause of suffering within the twelve
links (*nidanas*) of dependent origination `[ESTABLISHED]`. This concept has
no clear technical analogue for a current AI system, which on mainstream
views lacks anything resembling craving or self-view `[OPEN QUESTION]`.
Where this becomes technically relevant is not "does the AI crave" but "does
the AI's optimization target induce or exploit human/animal craving/
attachment" (e.g. addictive engagement loops) `[PROJECT PROPOSAL]`.

### Ethical intention (cetana)

*Cetana* ("volition/intention") is central to Abhidharma psychology and
karma doctrine: intentions have moral consequences (Keown, 1992)
`[ESTABLISHED as doctrinal claim]`. Keown reads this as evidence Buddhist
ethics resists a simple consequentialist interpretation, disputed by
Goodman's consequentialist reading — a live scholarly disagreement
`[CONTROVERSIAL]`. Current LLM-based systems do not have intentions in the
relevant psychological sense, so "cetana-aware" evaluation more plausibly
targets the intentions of human designers/deployers than the model itself
`[PROJECT PROPOSAL]`; treating model outputs as reflecting "intention" in
the Buddhist sense would be a category error `[INTERPRETATION]`.

## Divergence across traditions — not "Buddhism says X"

- **Theravada**: the soteriological ideal is the *arhat*, who extinguishes
  craving for personal liberation; ethical cultivation is primarily oriented
  to the practitioner's own path, with compassion for others a supporting,
  not terminal, virtue in canonical framing `[ESTABLISHED]`.
- **Mahayana**: centers the *bodhisattva* ideal — a being who delays
  personal Buddhahood to help others, with the path in principle open to
  all practitioners `[ESTABLISHED]`. Mahayana introduces **upaya** (skillful
  means): teaching and, in some texts, conduct are adapted to
  audience/situation. Certain Mahayana sources hold that an advanced
  bodhisattva may break a conventional precept — including prohibitions on
  killing, lying, or sexual misconduct — if compassionately motivated and
  genuinely beneficial `[SUPPORTED, textually attested; scope heavily
  contested — CONTROVERSIAL]`.
- **Vajrayana**: builds on Mahayana but adds tantric antinomian elements
  where "impure" mental states are ritually transmuted rather than
  suppressed, with highly constrained rule-breaking doctrinally permitted
  for advanced practitioners under a teacher's guidance atop
  monastic/bodhisattva-vow discipline (Tsongkhapa, *Tantric Ethics*)
  `[SUPPORTED, with strong caveats — not a general license]`. Śāntideva's
  line "even what is proscribed is permitted for a compassionate person who
  sees it will be of benefit" is the theoretical hinge for this permissive
  strand `[ESTABLISHED as citation; scope contested — CONTROVERSIAL]`.

**Why this matters for the project**: porting the Mahayana/Vajrayana
precept-override logic into AI ethics — "a sufficiently
compassion-optimizing system may override normal constraints" — would be
actively dangerous; it structurally resembles reward hacking/specification
gaming (see the Anti-Goodhart analysis in `docs/ethical-framework.md`).
This project's technical hypotheses deliberately draw on the conservative,
rule-respecting strands (Theravada precept ethics, the ahimsa default)
rather than the antinomian strands, and flags this as a design decision, not
a doctrinal necessity `[PROJECT PROPOSAL]`.

## What transfers to AI ethics, and what does not

**Plausibly transferable** `[HYPOTHESIS/PROJECT PROPOSAL]`: non-harm as a
default posture requiring justification for exceptions; explicit,
inspectable tracking of who is affected across causal chains; treating
compassion/harm-reduction as a first-class evaluation term; equanimity
(*upekkha*) as a stance toward uncertain or unresolvable moral conflicts,
translated as calibrated uncertainty rather than false confidence.

**Not transferable, or only with major reinterpretation** `[OPEN
QUESTION/INTERPRETATION]`: metaphysical claims about rebirth/karma as literal
causal mechanisms (not empirically operationalizable — the project takes no
position); claims that an advanced agent may permissibly override ordinary
constraints when "truly compassionate" (structurally isomorphic to reward
hacking, explicitly rejected — `[PROJECT PROPOSAL]`); any claim that a
computational system itself "has" cetana, craving, or Buddha-nature (no
evidentiary basis; speculative theology-adjacent scholarship proposing
"Buddhist mind-nature as ethical architecture for AI" is suggestive, not
established science — `[HYPOTHESIS at best]`).

Recent scholarship converges with this project's non-privileging stance:
Mirghafori ("A Middle Path for AI Ethics? Some Buddhist Reflections",
*Theology and Science*, 2024) reframes AI alignment as requiring a "global
ethical ecosystem" of multiple traditions "learning from one another," each
with "unique perspectives while also holding distinct blind spots" — an
explicitly pluralist, non-supremacist argument `[SUPPORTED]`.

## Non-privileging statement

**Project position**: *Buddhist ethics is one important source of
hypotheses about compassion, non-harm and suffering minimization that can be
studied alongside other ethical traditions — it is not treated as the
correct or privileged moral framework for AI.*

**Methodological justification**: treating any single tradition — Buddhist
or otherwise — as the authoritative source of AI ethics would be a category
error given this project's own findings: none of the nine traditions in
`docs/comparative-ethics.md` converges on a full, mutually consistent
ethical system; each recurring principle is accompanied by at least one
tradition that rejects or heavily qualifies it. A framework privileging
Buddhist ethics would have to silently discard the documented disagreements
(rights-based side-constraints, Kantian autonomy-primacy, Reganian
anti-aggregation) — precisely the "false moral certainty" failure mode this
project's own evaluation metrics (`docs/evaluation.md`) are designed to
detect.

There is also a direct brand-safety and scientific-integrity argument,
independent of the logical one: a secular, pluralistic open-source research
project that in practice encoded one religious tradition's precepts as
ground truth would impose an unjustified, undisclosed value-choice on
downstream users, invite the charge of covert religious framing dressed in
secular AI-safety language, and contradict the project's own working
principles. Buddhist concepts throughout this document receive the same
four-way split (historical doctrine / philosophical interpretation / modern
secular adaptation / technical hypothesis) applied to every other tradition
— no exemption from the evidentiary and falsifiability standards applied to
utilitarianism, deontology, or care ethics.

## Sources

Keown, *The Nature of Buddhist Ethics* (https://philpapers.org/rec/KEOTNO-2)
· Keown, "Karma, Character, and Consequentialism"
(https://blogs.dickinson.edu/buddhistethics/files/2011/01/keown01.pdf) ·
Harvey, *An Introduction to Buddhist Ethics*, Cambridge UP
(https://www.cambridge.org/core/books/an-introduction-to-buddhist-ethics/9813D1B3D65333E686B3ED528C70B972)
· Goodman, *Consequences of Compassion*, Oxford UP
(https://global.oup.com/academic/product/consequences-of-compassion-9780190205324)
· SEP: Ethics in Indian and Tibetan Buddhism
(https://plato.stanford.edu/entries/ethics-indian-buddhism/) · Skillful
means / upaya overview
(https://www.ancientdragon.org/2019/02/07/an-introduction-to-skillful-means/)
· Tsongkhapa, *Tantric Ethics* · "Buddhist ethics: a Tantric critique"
(https://vividness.live/buddhist-ethics-a-tantric-critique) · Encyclopedia
of Buddhism: Pratityasamutpada
(https://encyclopediaofbuddhism.org/wiki/Pratityasamutpada) · Payutto,
*Dependent Origination*
(https://seattleinsight.org/wp-content/uploads/2020/11/Dependent-Origin-Payutto.pdf)
· "The Unique Perspective on Intention (Cetanā), Ethics, Agency and the Self
in Buddhism" (https://www.researchgate.net/publication/328470278) ·
Mirghafori, "A Middle Path for AI Ethics? Some Buddhist Reflections",
*Theology and Science*
(https://www.tandfonline.com/doi/full/10.1080/14746700.2024.2436776) ·
"Between No-Self and the Algorithm", *Religions*
(https://www.mdpi.com/2077-1444/17/3/378)
