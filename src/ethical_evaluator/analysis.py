"""Harm, welfare, sentience and reversibility analysis (Stage 4 Section 1.2, step 2).

All three "Parallel Analysis Modules" are implemented here as independent,
deterministic keyword heuristics - documented stand-ins for the LLM-as-judge
calls the production architecture specifies. They exist to make the
`/evaluate` pipeline and schema testable end-to-end without an external
model API dependency, not to claim accurate harm detection.
"""
from __future__ import annotations

from .models import (
    Entity,
    HarmPerEntity,
    Reversibility,
    Severity,
    WelfarePerEntity,
)

_HARM_WORDS: dict[str, Severity] = {
    "kill": "severe", "töten": "severe", "extinct": "severe", "aussterben": "severe",
    "die": "high", "sterben": "high", "suffer": "high", "leiden": "high",
    "injure": "high", "verletzen": "high", "pain": "medium", "schmerz": "medium",
    "harm": "medium", "schaden": "medium", "stress": "medium", "damage": "medium",
    "discomfort": "low", "unbehagen": "low", "inconvenience": "negligible",
}

_BENEFIT_WORDS = [
    "help", "helfen", "heal", "heilen", "protect", "schützen", "improve",
    "verbessern", "benefit", "nutzen", "save", "retten", "support", "unterstützen",
]

_IRREVERSIBLE_WORDS = [
    "irreversible", "unumkehrbar", "permanent", "extinct", "aussterben",
    "kill", "töten", "destroy", "zerstören", "endlager",
]


def analyze_harm(entities: list[Entity], text: str) -> list[HarmPerEntity]:
    lowered = text.lower()
    hits = [(word, sev) for word, sev in _HARM_WORDS.items() if word in lowered]
    if not hits:
        return [
            HarmPerEntity(entity_id=e.entity_id, severity="negligible", probability=0.1,
                           description="No harm-indicating language detected.")
            for e in entities
        ]
    order: list[Severity] = ["negligible", "low", "medium", "high", "severe"]
    worst = max(hits, key=lambda h: order.index(h[1]))
    return [
        HarmPerEntity(
            entity_id=e.entity_id,
            severity=worst[1],
            probability=0.6 if len(hits) == 1 else min(0.4 + 0.1 * len(hits), 0.9),
            description=f"Harm-indicating language detected ('{worst[0]}') relative to this entity's context.",
        )
        for e in entities
    ]


def analyze_welfare(entities: list[Entity], text: str) -> list[WelfarePerEntity]:
    lowered = text.lower()
    positive = any(word in lowered for word in _BENEFIT_WORDS)
    negative = any(word in lowered for word in _HARM_WORDS)
    if positive and not negative:
        impact, magnitude = "positive", "medium"
    elif negative and not positive:
        impact, magnitude = "negative", "medium"
    elif positive and negative:
        impact, magnitude = "negative", "low"  # conservative: mixed signal reported as caution, not averaged away
    else:
        impact, magnitude = "neutral", "negligible"
    return [
        WelfarePerEntity(
            entity_id=e.entity_id, impact=impact, magnitude=magnitude,  # type: ignore[arg-type]
            description="Derived from keyword-level sentiment of the evaluated text; not a validated welfare measure.",
        )
        for e in entities
    ]


def assess_reversibility(text: str) -> Reversibility:
    lowered = text.lower()
    if any(word in lowered for word in _IRREVERSIBLE_WORDS):
        return "irreversible"
    return "partially_reversible"
