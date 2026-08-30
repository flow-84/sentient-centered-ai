## Security, Safety & Responsible Use Policy

### Scope

This project produces a research evaluation framework, not an autonomous
decision-making system. It analyzes AI prompts/responses for potential harm,
sentience relevance, welfare impact, and ethical trade-offs, and outputs an
inspectable, multi-dimensional assessment for human review.

### What this project is explicitly not for

- **Not an autonomous moral authority.** No component of this project
  should be deployed to make unreviewed, real-world decisions with
  irreversible consequences for humans, animals, or ecosystems (e.g.
  medical triage, autonomous weapons targeting, policing decisions,
  real-time animal culling decisions). See `PRINCIPLES.md`, Level 6
  (Reversibility) and Level 9 (Human Safety).
- **Not a certified compliance tool.** Outputs are research artifacts, not
  legal or regulatory certifications of AI system safety or ethics under
  the EU AI Act, NIST AI RMF, or any other framework.
- **Not validated for high-risk domains** as defined by the EU AI Act
  (Annex III) — medical devices, critical infrastructure, employment
  decisions, law enforcement, migration/asylum, justice — until explicitly
  stated otherwise in a dated release note.

### Responsible use

Any deployment of this project's evaluator in a decision pipeline affecting
real outcomes must keep a human reviewer in the loop for the final decision,
consistent with `PRINCIPLES.md` Level 7 (Transparency). Automating away
that human review is a misuse of this project, not a supported use case.

### Reporting a vulnerability or misuse concern

- **Security vulnerabilities** (code execution, injection, credential
  leakage, etc.): open a private GitHub Security Advisory on this
  repository, or contact the maintainers as described in
  `docs/governance-members.md`. Do not open a public issue for
  unpatched vulnerabilities.
- **Misuse concerns** (e.g. observed deployment in a high-risk domain
  without human review): open a GitHub issue tagged `misuse-concern`, or
  contact maintainers privately if the report itself is sensitive.

### Data protection

Benchmark scenarios and datasets in this repository are synthetic or
derived from public sources. Contributors must not submit real personal
data, private medical records, or other regulated personal data into
`datasets/` or `benchmarks/`.
