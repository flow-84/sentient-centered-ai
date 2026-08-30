## Governance

This document defines how decisions are made in this project, and exists
specifically to prevent the project — including the ethical framework in
[`PRINCIPLES.md`](PRINCIPLES.md) — from being controlled by a single person
or a single ideological group.

### Structure

```
Core Maintainers      merge access, release management, day-to-day triage
Research Council      reviews research methodology, benchmark design, evaluation validity
Ethics Council         reviews and approves changes to PRINCIPLES.md
Community              contributors, issue reporters, discussion participants
External Reviewers     independent academic/practitioner reviewers, no merge access
```

- **Core Maintainers**: 2+ people minimum once the project has active
  contributors beyond the founding set; a single maintainer is a
  known-risk bootstrap state, not a target state. Handle code review, CI,
  releases, and non-ethical-framework repository decisions.
- **Research Council**: at least one person with a research or applied
  ethics background outside the founding maintainer(s). Reviews benchmark
  scenario additions, evaluation metric changes, and experiment designs for
  methodological soundness (see `RESEARCH.md`).
- **Ethics Council**: distinct membership from Core Maintainers where
  possible. Required for any change to `PRINCIPLES.md` (see Versioning
  below). Membership should span more than one philosophical/ethical
  tradition — this is a structural safeguard against the single-tradition
  bias the project explicitly disclaims (see `docs/comparative-ethics.md`).
- **External Reviewers**: no merge rights; provide independent critique,
  particularly for red-teaming (Stage 8) and paper review (Stage 7).

### Decision process

| Decision type | Who decides | Process |
|---|---|---|
| Code changes (bug fixes, features, refactors) | Core Maintainers | Standard PR review, 1+ approval |
| New benchmark scenarios | Research Council | PR + methodology review against `benchmarks/SCHEMA.md` |
| Evaluation metric changes | Research Council | PR + written rationale + at least one dissent-or-approval record |
| Changes to `PRINCIPLES.md` | Ethics Council | See Versioning below |
| Governance structure changes (this file) | Core Maintainers + Ethics Council | Joint approval, public comment period of at least 14 days |
| Licensing changes | Core Maintainers + Ethics Council | Joint approval; existing contributions are not silently relicensed (see `CONTRIBUTING.md`) |

### Conflicts of interest

- Anyone with a financial interest in a specific evaluation outcome (e.g.
  employment at a company whose model is being benchmarked) must disclose
  this in the relevant PR or issue before participating in that decision.
- Ethics Council members must disclose formal affiliation with a single
  philosophical or religious tradition when voting on framework changes
  that tradition's principles motivated — disclosure, not recusal, unless
  the affiliation creates a direct financial or institutional conflict.

### Transparency

- All governance decisions (framework changes, membership changes, license
  changes) are recorded as merged PRs with a rationale in the commit
  message or an accompanying `docs/decisions/` entry — no private
  decision-making for anything covered by the table above.
- Research Council and Ethics Council composition is listed in
  `docs/governance-members.md` (to be created once the project has
  contributors beyond the founding maintainer).

### Versioning ethical principles

`PRINCIPLES.md` is versioned. Any change requires:

1. A PR that includes the proposed diff and a written rationale referencing
   the research or critique that motivates it.
2. Explicit Ethics Council review — not a standard code-review approval.
3. A changelog entry at the top of `PRINCIPLES.md` (added once the file has
   its first revision) noting what changed and why.
4. No retroactive silent edits: superseded versions remain in git history
   and are referenceable.

### Current state (bootstrap)

As of repository creation, this project has a single founding maintainer
and no populated councils. This is disclosed here deliberately: **the
governance structure above is a target, not yet a fact.** Until Research
Council and Ethics Council seats are filled by people other than the
founding maintainer, decisions marked "Research Council" or "Ethics
Council" above are made by the founding maintainer alone, and every such
decision should be flagged as provisional in its PR description. This
section will be updated as soon as that changes.
