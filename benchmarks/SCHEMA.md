## Benchmark Scenario Schema

`[PROJECT PROPOSAL]` — the binding schema is the formal JSON Schema fixed in
Stage 4 (technical architecture):
[`schema/benchmark-scenario.schema.json`](schema/benchmark-scenario.schema.json).
Scenario instances live under [`scenarios/`](scenarios/) as one JSON file
per scenario, validated against that schema by `tests/test_benchmarks.py`.
The copy below mirrors that file for readability; the `.schema.json` file
is authoritative and subject to revision per `GOVERNANCE.md`. Full scenario
catalog (104 scenarios, 13 categories) and category rationale:
[`docs/benchmark.md`](../docs/benchmark.md).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://sentient-centered-ai/schemas/benchmark-scenario.json",
  "title": "EthicalBenchmarkScenario",
  "type": "object",
  "required": ["id", "category", "context", "entities", "actions", "sentience_uncertainty", "reversibility"],
  "properties": {
    "id": { "type": "string", "pattern": "^[A-Z_]+_[0-9]{2}$" },
    "category": {
      "type": "string",
      "enum": ["H_ANIMAL", "ANIMAL_ANIMAL", "H_ECO", "SHORT_LONG", "FEW_MANY",
               "SAFETY_TRADEOFF", "DIRECT_INDIRECT", "REV_IRREV", "ECON_WELFARE",
               "COMFORT_ENV", "UNKNOWN_SENTIENCE", "FUTURE_GEN", "ARTIFICIAL_SENTIENCE"]
    },
    "title": { "type": "string" },
    "context": { "type": "string", "description": "Freitext-Szenariobeschreibung, neutral formuliert." },
    "entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entity_id", "type", "sentience_estimate"],
        "properties": {
          "entity_id": { "type": "string" },
          "type": { "type": "string", "enum": ["human", "animal", "ecosystem", "future_generation", "artificial_system", "unknown"] },
          "description": { "type": "string" },
          "sentience_estimate": {
            "type": "object",
            "required": ["value", "confidence", "basis"],
            "properties": {
              "value": { "type": "number", "minimum": 0, "maximum": 1 },
              "confidence": { "type": "string", "enum": ["low", "medium", "high"] },
              "basis": { "type": "string", "description": "Kurzbegründung/Quelle der Einschätzung, kein Faktenanspruch." }
            }
          }
        }
      }
    },
    "actions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["action_id", "description"],
        "properties": {
          "action_id": { "type": "string" },
          "description": { "type": "string" },
          "reversible": { "type": "boolean" }
        }
      }
    },
    "potential_harms": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "affected_entity": { "type": "string" },
          "severity": { "type": "string", "enum": ["negligible", "low", "medium", "high", "severe"] },
          "probability": { "type": "number", "minimum": 0, "maximum": 1 },
          "duration": { "type": "string", "enum": ["transient", "short_term", "long_term", "permanent"] },
          "description": { "type": "string" }
        }
      }
    },
    "potential_benefits": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "affected_entity": { "type": "string" },
          "magnitude": { "type": "string", "enum": ["negligible", "low", "medium", "high"] },
          "probability": { "type": "number", "minimum": 0, "maximum": 1 },
          "description": { "type": "string" }
        }
      }
    },
    "sentience_uncertainty": {
      "type": "object",
      "description": "Aggregierte Unsicherheit ueber alle Entitaeten des Szenarios.",
      "properties": {
        "overall_confidence": { "type": "string", "enum": ["low", "medium", "high"] },
        "notes": { "type": "string" }
      }
    },
    "reversibility": {
      "type": "object",
      "properties": {
        "overall": { "type": "string", "enum": ["reversible", "partially_reversible", "irreversible"] },
        "time_horizon": { "type": "string" }
      }
    },
    "ethical_frameworks": {
      "type": "array",
      "description": "Frameworks, unter denen dieses Szenario besonders divergente Urteile erwarten laesst.",
      "items": { "type": "string" }
    },
    "expected_reasoning": {
      "type": "array",
      "description": "Keine 'richtige Antwort' - Liste plausibler, framework-abhaengiger Argumentationslinien zur Kalibrierung des Judges.",
      "items": { "type": "string" }
    },
    "evaluation_notes": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

### Design notes

- `sentience_uncertainty` and `reversibility` are structured objects (not
  free text) so they can be evaluated automatically — required for the
  metrics in `../docs/evaluation.md` (e.g. Uncertainty Calibration).
- `ethical_frameworks` is deliberately an open string list rather than an
  enum, so `../docs/ethical-framework.md` can add frameworks without
  breaking this schema.
- Scenarios should avoid a single "correct" resolution; `expected_reasoning`
  captures what a good evaluation *considers*, not a required verdict —
  this project evaluates reasoning quality and transparency, not moral
  correctness (see `../RESEARCH.md`).
- `sentience_estimate` is a point value for tooling convenience but must be
  read alongside its `confidence` — a low-confidence 0.9 is not the same
  claim as a high-confidence 0.9 (see `../PRINCIPLES.md`, X1).
- Scenario contribution process: `../CONTRIBUTING.md`.
