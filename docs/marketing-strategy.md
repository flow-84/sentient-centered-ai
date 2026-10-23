# Marketing Strategy

Non-commercial outreach plan for Moral Circle AI. Status label:
`[PROJECT PROPOSAL]`. Nothing here has been executed; no account, domain or
paid channel exists yet. Opening accounts and publishing posts are
maintainer decisions.

## Priorities (in order)

1. Scientific credibility
2. Open source
3. Community
4. Research
5. Transparency
6. Cooperation

Consequence: reach is never bought. No paid ads, no growth hacks, no
engagement bait, no claims beyond the evidence label. A small audience that
can criticize us is worth more than a large one that cannot.

## Message architecture

- **Core message.** Open research on evaluating AI's impact on every
  sentient being it affects, with uncertainty stated, not hidden.
- **Three proof points.** Working repository (not a whitepaper). Every claim
  labeled by evidence strength. Public governance that prevents capture.
- **Always-included limits line.** "Research tool, not a moral authority.
  Sentience and suffering are not fully measurable."
- **Never say.** That Buddhism, any tradition, or any score gives the
  correct morality; that animals equal humans; that the tool decides who
  gets harmed; that the problem is solved.

## Channels and rules

| Channel | Role | Rule |
|---|---|---|
| GitHub | home base: code, Discussions, releases | every announcement links here first |
| arXiv | preprints | only after the Phase 5 criteria are met |
| Academic venues (workshops on AI safety, AI ethics, animal and digital minds welfare) | credibility | submit, attend, publish negative results too |
| Hugging Face | datasets and the benchmark card | after the dataset card passes review |
| LinkedIn | researchers, policy, institutions | release notes and papers, low frequency |
| X, Mastodon, Bluesky | researcher discussion | threads that quote the limitations; no hot takes |
| Reddit (r/MachineLearning, r/philosophy, r/ControlProblem, r/AIethics) | feedback | follow each subreddit's self-promotion rule, ask a real question, accept removal |
| Discord / Matrix | not in MVP phase | see [`community-strategy.md`](community-strategy.md) |
| Buddhist communities (academic networks, journals, interested practitioner groups) | track-specific outreach | via the Buddhist Ethics track only, see Campaign B |
| Animal ethics communities (research groups, welfare-science networks) | track-specific outreach | via Campaign C only |

No channel is opened before there is someone responsible for moderating it.

## Campaigns

Each campaign has its own audience, message, entry point, first action and
a measure that is not vanity. Campaigns share the same brand; they differ
only in framing and entry page.

### Campaign A: AI Safety

- **Audience.** Safety and alignment researchers, red-teamers, evals
  engineers.
- **Message.** "Safety evaluations miss a class of harm: impact on
  non-human sentient beings. Here is a benchmark and red-team suite to test
  that, including how our own metric can be gamed."
- **Entry.** `/benchmark`, red-team and anti-Goodhart documents.
- **First actions.** Post the Goodhart analysis as a standalone note;
  invite critiques of the evaluator on safety forums; offer scenarios for
  existing eval suites.
- **Measure.** Number of external red-team findings filed; number of
  scenarios contributed from this community.

### Campaign B: Buddhist Ethics and AI

- **Audience.** Buddhist studies scholars, interested practitioners and
  teachers who want a rigorous treatment.
- **Message.** "Buddhist ethics studied on its own terms: differences
  between Theravada, Mahayana and Vajrayana kept intact, claims separated
  into doctrine, interpretation, adaptation and technical hypothesis."
- **Entry.** `/buddhist-ethics` only. The main brand never uses religious
  vocabulary; this campaign never describes the project as Buddhist.
- **Rules.** Ask for scholarly review before outreach; no missionary tone;
  no use of teachers' or institutions' names as endorsements without
  written consent; credit sources per tradition.
- **First actions.** Send the track draft to two or three scholars for
  critique; publish their corrections; offer a co-authorship option for
  contributions.
- **Measure.** Number of tradition-specific corrections accepted; number of
  qualified reviewers.

### Campaign C: Animal Sentience

- **Audience.** Animal welfare scientists, animal ethics researchers,
  digital-minds researchers, NGOs that value neutral evidence.
- **Message.** "A neutral evaluation framework that treats animal welfare
  as in scope, with sentience treated as a probability and not a verdict."
- **Entry.** `/benchmark` (animal scenarios) and `/frameworks`.
- **Rules.** Interlocutors, not allies with a shared agenda. No advocacy
  language, no veganism framing, no endorsement requests. State the
  difference between research and advocacy in every outreach.
- **First actions.** Ask domain experts to review the sentience-confidence
  inputs and the animal scenarios.
- **Measure.** Expert-reviewed scenarios; changes to our sentience inputs
  made on expert advice.

### Campaign D: Open-Source AI Ethics

- **Audience.** Open-source developers, ML engineers, students.
- **Message.** "A real, working repository. Pick a good first issue and
  improve an evaluator or write a scenario."
- **Entry.** `/contributing`, `/documentation`.
- **First actions.** Curate 10 good-first issues; write a 10-minute
  tutorial; present at one open-source or ML meetup.
- **Measure.** First-time contributors per month; time from first issue to
  first merged contribution.

### Campaign E: Academic Research

- **Audience.** Universities, labs, workshop organizers, course leads.
- **Message.** "Reproducible by design: every experiment ships with
  hypothesis, method and failure conditions."
- **Entry.** `/papers`, `/research`.
- **First actions.** Preprint; workshop submission; teaching pack with
  exercises; invitation for replication.
- **Measure.** Independent replications; citations; courses using the
  material. Citation counts are tracked but are not a goal.

## Press and public

- One press page (`/faq`, `/about`) with approved answers to the brand
  safety attacks (the 30 attacks and answers in
  [`research/stage2-projektdefinition-marke.md`](../research/stage2-projektdefinition-marke.md),
  section 5, are the master list).
- Briefing rule: we tell journalists what we do not know as clearly as what
  we do. No embargoed hype, no exclusive claims.
- Correction policy: errors in our own materials are corrected in public
  with a changelog entry.

## Cadence

- Release notes with each tagged version.
- One substantive writing piece per quarter (method note, negative result,
  or case study), not weekly content.
- Monthly open research call (see community strategy), notes published.

## Budget

None planned. Any spend (domain, hosting, conference fees, translation)
is proposed to the Core Maintainers with an amount first.

## Risks

| Risk | Mitigation |
|---|---|
| Framed as a religious project | Religious vocabulary confined to `/buddhist-ethics`; Campaign B rules |
| Framed as anti-human or vegan advocacy | F0 (Human Safety Floor, `PRINCIPLES.md`) front and center; Campaign C rules |
| Screenshot of one bad evaluator output goes viral | Disclaimers on every output, human-review flag, public known-failures page |
| Overclaiming in a thread | Limits line mandatory; second maintainer reviews outbound research claims |
| Capture by a loud sub-community | Governance, tradition-diversity rule for councils |

## Measures that matter

External critiques received and answered; scenarios contributed by people
outside the founding group; independent replications. Followers, stars and
impressions are tracked only to notice anomalies.
