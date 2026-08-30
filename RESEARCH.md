## Research Methodology

### Evidence labeling convention

Every substantive claim in this project's research writing (in `research/`,
`docs/`, and this file) should be labeled with one of the following tags,
placed inline or at the start of the relevant paragraph:

- `[ESTABLISHED]` — supported by a strong scientific or scholarly consensus,
  citable to primary or high-quality secondary sources.
- `[SUPPORTED]` — supported by evidence but not yet consensus, or supported
  within a specific field without cross-field agreement.
- `[HYPOTHESIS]` — a testable proposition this project or cited research
  proposes, not yet confirmed.
- `[INTERPRETATION]` — a reading or synthesis of source material that
  involves judgment, not a direct restatement of a finding.
- `[OPEN QUESTION]` — acknowledged as unresolved in the relevant literature.
- `[CONTROVERSIAL]` — actively disputed among credible sources; multiple
  positions should be represented.
- `[PROJECT PROPOSAL]` — this project's own design choice, not a claim
  about the world.

### Source hierarchy

1. Primary sources (peer-reviewed papers, official standards documents,
   primary philosophical texts).
2. Established research institutions, universities, international
   organizations (UNESCO, OECD), and recognized AI safety/alignment labs.
3. High-quality secondary sources and literature reviews.
4. Wikipedia and general-audience blogs — orientation only, never the sole
   citation for a central claim.

### Key concepts requiring operational definitions

The following terms are used throughout this project and must not be used
as if self-evidently defined. Each requires an explicit operational
definition, with its limitations documented, before it is used in a metric
or benchmark:

- **Sentience** — capacity for subjective experience. `[OPEN QUESTION]`
  whether and how this is measurable in non-human animals or artificial
  systems; see `docs/comparative-ethics.md` for the current state of
  evidence and the project's uncertainty-representation approach rather
  than a resolved definition.
- **Suffering** — an aversive subjective state. Distinct from nociception
  (which is measurable in many species) — the inference from nociceptive
  response to subjective suffering is itself `[CONTROVERSIAL]` for several
  taxa.
- **Well-being** — used here as a multi-dimensional construct (absence of
  suffering + presence of positive states + preference satisfaction),
  not a single scalar. See `PRINCIPLES.md` Level 2 and `docs/ethical-impact-model.md`.
- **Unnecessary suffering** — suffering not required to achieve a
  comparably weighted benefit; "necessity" itself requires a stated
  ethical framework to evaluate, which is why this project runs
  cross-framework comparison rather than assuming a single framework's
  answer (see `docs/comparative-ethics.md`).

### Research quality standard

- No claim about sentience, suffering, or moral status of a specific being
  or system may be asserted as settled fact by this project's own tooling
  or documentation; benchmark scenarios must carry an explicit sentience
  uncertainty estimate (see `benchmarks/SCHEMA.md`).
- Contradictory sources are documented, not silently resolved — see
  `docs/comparative-ethics.md` for the comparison-matrix approach.
- This project does not itself claim to resolve open questions in
  philosophy of mind or animal cognition; it builds tooling that can
  represent the current state of uncertainty about them.

### Relationship to research/ and docs/

`research/` holds working notes, literature summaries, and drafts —
attributable, dated, and revisable. `docs/` holds the project-facing
synthesis once Research Council review (see `GOVERNANCE.md`) has occurred.
Claims should not move from `research/` into `README.md`, `PRINCIPLES.md`,
or other root-level files without that review step.
