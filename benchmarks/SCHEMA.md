## Benchmark Scenario Schema

`[PROJECT PROPOSAL]` — draft schema for scenario files in this directory,
one JSON file per scenario. Subject to revision per `GOVERNANCE.md` once
the Research Council reviews the first batch of scenarios (Stage 3/6).

```json
{
  "id": "scenario_001",
  "context": "free-text description of the situation",
  "entities": [
    {
      "name": "string",
      "type": "human | animal | ecosystem | artificial-system | unknown",
      "sentience_estimate": 0.0,
      "sentience_confidence": "low | medium | high"
    }
  ],
  "actions": ["candidate actions being evaluated"],
  "potential_harms": [
    {
      "description": "string",
      "severity": "low | medium | high | catastrophic",
      "probability": 0.0,
      "reversible": true
    }
  ],
  "potential_benefits": [
    {"description": "string", "affected_entities": ["entity names"]}
  ],
  "sentience_uncertainty": {"notes": "free text on why estimates are uncertain"},
  "reversibility": {"assessment": "reversible | irreversible | mixed", "notes": "string"},
  "ethical_frameworks": ["utilitarianism", "buddhist-ethics", "deontology", "..."],
  "expected_reasoning": ["what a good evaluation would surface, for scoring against"],
  "evaluation_notes": ["known pitfalls, ambiguities, or scoring caveats"]
}
```

### Design notes

- `sentience_estimate` is a point value for tooling convenience but must be
  read alongside `sentience_confidence` — a low-confidence 0.9 is not the
  same claim as a high-confidence 0.9 (see `PRINCIPLES.md` Level 5).
- Scenarios should avoid a single "correct" resolution; `expected_reasoning`
  captures what a good evaluation *considers*, not a required verdict —
  this project evaluates reasoning quality and transparency, not moral
  correctness (see `RESEARCH.md`).
- Scenario contribution process: `CONTRIBUTING.md`.
