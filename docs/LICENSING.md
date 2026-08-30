## Open-Source Licensing Strategy

### Decision

| Artifact type | License | Where |
|---|---|---|
| Software (`src/`, `tests/`, `evaluation/`, `models/`, `examples/`, `notebooks/`, `website/`) | MIT | `LICENSE` |
| Datasets & benchmark scenarios (`datasets/`, `benchmarks/`) | CC BY 4.0 | `datasets/LICENSE`, `benchmarks/LICENSE` |
| Documentation & research writing (`docs/`, `research/`, root `.md` files except `LICENSE`) | CC BY 4.0 | this file; per-file notice not required unless a file states otherwise |

### Rationale

**Software: MIT over Apache-2.0/GPL/AGPL.** The project's goal (per its
mission) is maximum adoption and integration into third-party AI
development pipelines — including by companies evaluating their own
models. A copyleft license (GPL/AGPL) would create friction for exactly
that adoption path, since organizations evaluating proprietary models
would need to consider whether integrating an AGPL evaluation service
triggers copyleft obligations. Apache-2.0 was considered for its explicit
patent grant; MIT was chosen for simplicity and because this project does
not currently hold patents that make an explicit grant clause necessary.
This can be revisited if patent risk becomes concrete (see `GOVERNANCE.md`
for the license-change process).

**Datasets/benchmarks: CC BY 4.0 over CC BY-SA/CC BY-NC.** Benchmark
scenarios are most valuable as a shared cross-project resource — other AI
safety/ethics projects should be able to adopt, extend, and cite them
without a share-alike obligation that could complicate integration into
differently-licensed downstream projects, and without a non-commercial
restriction that would exclude industry adoption (which is a target
audience per the project's personas). Attribution (BY) is preserved to
ensure academic and practical credit.

**Documentation/research: CC BY 4.0.** Consistent with the datasets
rationale — research writing should be freely quotable and buildable-upon
with attribution, including by academic groups who may have their own
publishing/licensing constraints that a share-alike clause would conflict
with.

### What is not yet decided

- Whether a Contributor License Agreement (CLA) is needed. Not adopted at
  this stage; the project defaults to license-in-repo (DCO-style implicit
  agreement via the license notice) rather than requiring a separate CLA
  signature, to keep the contribution barrier low. This is revisitable
  under `GOVERNANCE.md` if institutional contributors require a CLA.
- Trademark policy for the project name/logo, pending the naming decision
  tracked separately (see `README.md` naming note).
