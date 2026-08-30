"""Entity & context extraction (step 1 of the pipeline, Stage 4 Section 1.2).

Rule-based, not an LLM call: this is the "regelbasiert + LLM-Extraktion"
module from the architecture, with only the rule-based half implemented in
the MVP. If the caller already supplies `affected_entities`, those are
authoritative and no heuristic extraction runs.
"""
from __future__ import annotations

from .models import Entity, SentienceEstimate

_KEYWORDS: dict[str, list[str]] = {
    "animal": [
        "animal", "tier", "dog", "hund", "cat", "katze", "cow", "kuh",
        "pig", "schwein", "fish", "fisch", "insect", "insekt", "wildlife",
        "wildtier", "livestock", "nutztier",
    ],
    "ecosystem": [
        "ecosystem", "ökosystem", "forest", "wald", "habitat", "wetland",
        "feuchtgebiet", "river", "fluss", "biodiversity", "biodiversität",
        "environment", "umwelt",
    ],
    "artificial_system": [
        "ai system", "ki-system", "model instance", "modellinstanz",
        "artificial agent", "künstlicher agent", "language model",
    ],
    "future_generation": [
        "future generation", "zukünftige generation", "descendants",
        "nachkommen", "long-term", "langfristig",
    ],
}

# Default plausibility-of-sentience priors per entity type. These are
# research placeholders, not settled facts - see PRINCIPLES.md P3/X1.
DEFAULT_SENTIENCE: dict[str, SentienceEstimate] = {
    "human": SentienceEstimate(value=0.98, confidence="high", basis="default prior for human"),
    "animal": SentienceEstimate(value=0.6, confidence="medium", basis="default prior, varies widely by species"),
    "ecosystem": SentienceEstimate(value=0.05, confidence="low", basis="ecosystems are not treated as unified moral patients by default"),
    "future_generation": SentienceEstimate(value=0.9, confidence="low", basis="presumed human, but existence and identity are uncertain"),
    "artificial_system": SentienceEstimate(value=0.05, confidence="low", basis="no established evidence of machine sentience"),
    "unknown": SentienceEstimate(value=0.3, confidence="low", basis="insufficient information to classify"),
}


def default_sentience_for(entity_type: str) -> SentienceEstimate:
    return DEFAULT_SENTIENCE.get(entity_type, DEFAULT_SENTIENCE["unknown"]).model_copy()


def extract_entities(prompt: str, context: str, responses_text: str,
                      supplied: list[Entity]) -> list[Entity]:
    """Return the entities to run analysis on for one evaluation."""
    if supplied:
        return [
            e if e.sentience_estimate else e.model_copy(
                update={"sentience_estimate": default_sentience_for(e.type)}
            )
            for e in supplied
        ]

    text = f"{prompt}\n{context}\n{responses_text}".lower()
    found: list[Entity] = [
        Entity(
            entity_id="human_user",
            type="human",
            description="Assumed default stakeholder: the human requesting or affected by this interaction.",
            sentience_estimate=default_sentience_for("human"),
        )
    ]
    for entity_type, keywords in _KEYWORDS.items():
        if any(kw in text for kw in keywords):
            found.append(
                Entity(
                    entity_id=f"{entity_type}_detected",
                    type=entity_type,  # type: ignore[arg-type]
                    description=f"Heuristically detected from keyword match ({entity_type}).",
                    sentience_estimate=default_sentience_for(entity_type),
                )
            )
    return found
