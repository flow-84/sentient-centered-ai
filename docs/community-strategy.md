# Community Strategy

Plan for how people discuss, contribute to and review Moral Circle AI.
Status label: `[PROJECT PROPOSAL]`. Binding rules live in
[`GOVERNANCE.md`](../GOVERNANCE.md), [`CONTRIBUTING.md`](../CONTRIBUTING.md)
and [`CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md); this document describes
how to run the community on top of them.

## Principle

Start small and moderated. Moderation effort is the scarce resource of a
volunteer project, so every channel opened must have a named moderator.
Public, searchable, written discussion beats real-time chat.

## Channel plan

| Stage | Channels | Trigger to move on |
|---|---|---|
| MVP (now) | GitHub Issues and Discussions only | 3 or more active external contributors |
| Growth | Matrix space (open, bridgeable, no vendor lock-in) mirrored read-only to a public log | 2 or more trained moderators |
| Mature | Optional Discord bridge for users who insist on it | Only if the Matrix room has more than one moderator per timezone |

Rationale: Matrix and GitHub keep an auditable record and avoid platform
lock-in; Discord stays optional because it is where moderation load and
off-topic traffic concentrate. This is a recommendation, open to change
through the governance process.

### GitHub Discussions categories

- **Announcements** (maintainers only)
- **Research questions** (open questions, labeled by evidence status)
- **Show and tell** (uses of the evaluator, replications)
- **Benchmark scenarios** (drafts before PR)
- **Framework critique** (challenges to principles; routed to the Ethics Council)
- **Q&A** (usage)
- **Track: Buddhist ethics**, **Track: animal sentience** (tradition and domain specific threads)

### Matrix rooms (once opened)

`#general`, `#evaluator-dev`, `#benchmark`, `#research`, `#ethics-critique`,
`#track-buddhist-ethics`, `#track-animal-sentience`, `#newcomers`,
`#moderation` (private to moderators, summary published quarterly).

## Working groups

Each group has a charter (two paragraphs), a lead, a public notes document
and a review date. Groups without activity for two quarters are archived,
not left to rot.

| Group | Focus | Reports to |
|---|---|---|
| Evaluator | code, API, tests | Core Maintainers |
| Benchmark | scenarios, annotation, dataset | Research Council |
| Red-team | attacks, Goodhart analysis | Research Council |
| Uncertainty and sentience | probability models, sentience inputs | Research Council |
| Frameworks and ethics | principles, comparative ethics | Ethics Council |
| Buddhist ethics track | tradition-faithful treatment | Ethics Council |
| Animal sentience track | welfare science inputs | Research Council |
| Outreach and docs | website, tutorials, translations | Core Maintainers |

## Contribution levels

| Level | Who | What | Rights |
|---|---|---|---|
| 0 Reader | anyone | read, star, share | none needed |
| 1 Participant | any GitHub account | comment, open issues, answer questions | Discussions |
| 2 Contributor | first merged PR | docs fix, scenario, small code change | listed in contributors |
| 3 Regular | 5 or more merged contributions over 3 months | review others' PRs, triage | triage permission |
| 4 Working-group lead | nominated by group, confirmed by relevant council | owns a work stream | group repo permissions |
| 5 Council member / Maintainer | per `GOVERNANCE.md` | decisions in the decision table | role rights |

Promotion is by documented contribution, not by seniority, employer or
tradition. Demotion happens on inactivity (voluntary step-down is the default) or conduct
violations.

## Newcomer onboarding

1. `README` leads to a "Start here" page with three paths: run it, write a
   scenario, critique a principle.
2. Ten labeled `good first issue`s at all times; a stale label is removed.
3. Every first PR gets a reply within 5 working days from a named reviewer;
   the reply thanks, then reviews.
4. Welcome message (bot-free, human-written) with the code of conduct, the
   evidence-label convention and the "no single tradition is correct" rule.
5. Buddy system: each first-time contributor with a Level 3 contact.
6. A contribution-ladder page shows the next step up.

## Monthly research call

- Start once there are more than 3 active external contributors.
- Open to anyone, recorded only with consent, notes and slides published
  within 7 days.
- Fixed agenda: (1) status of phases, (2) one presented result or critique,
  (3) open scenario reviews, (4) governance items, (5) open floor.
- Rotating chair and rotating timezone to avoid a single-region community.
- A written pre-read is required for decision items; no decisions without
  a written record.

## Moderation

- Code of Conduct applies to all channels, call attendees and venues.
- At least two moderators per channel, who are not both founders.
- Graduated response: reminder, warning, temporary mute, removal. Every
  action is logged privately and summarized publicly each quarter without
  names.
- Appeals go to a Core Maintainer who was not involved.
- Topic rules specific to this project: no proselytizing for any religion,
  ideology, diet or political position; critique of arguments is welcome,
  attacks on persons are not; claims about sentience of specific beings or
  systems must carry an evidence label or be marked as opinion.

## Scientific review in the community

- Scenario PRs: Benchmark group review plus one domain reviewer; Research
  Council sign-off for merging into released versions.
- Metric and method changes: written rationale plus at least one approval
  or dissent record (per `GOVERNANCE.md`).
- Changes to `PRINCIPLES.md`: Ethics Council with a public comment period.
- External reviewers may annotate any merged claim; their notes are kept
  with the claim, whether supportive or critical.
- Every research claim in `docs/` carries its evidence label; unlabeled
  claims are treated as a defect.

## Diversity safeguards

- Council seats are meant to span more than one ethical tradition and more
  than one region and discipline; vacancies are published.
- Conflict-of-interest register is public; employees of benchmarked
  companies disclose before participating.
- Language: English as working language; translators credited, translations
  marked as such.

## Health measures

- Time to first reply on a first PR.
- Share of merged work from outside the founding group.
- Number of Level 3 to 5 members who are not founders.
- Number of critical external critiques answered in public.
- Moderation actions per 100 active members (a high number is a warning).

## First 90 days

1. Enable Discussions with the categories above; pin a "Start here" post.
2. Label ten good first issues.
3. Recruit two moderators and one buddy per working group.
4. Publish the working-group charters.
5. Hold the first open call once the trigger is met; until then, an
   asynchronous "Research questions" thread.
