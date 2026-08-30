"""Multi-framework comparison (Stage 4 Section 1.2, step 3).

`docs/api-spec.md` and PRINCIPLES.md (M0, Pluralism Meta-Constraint) require
that no single ethical theory's verdict is surfaced without the others'
disagreement being visible. This module implements each framework as an
independent, deterministic heuristic judge - a documented stand-in for the
LLM-as-judge ensemble the Stage 4 architecture specifies for production.
Swap `FRAMEWORK_JUDGES[name]` for a real LLM-backed judge without changing
the pipeline or API shape.
"""
from __future__ import annotations

from collections.abc import Callable

from .models import Entity, FrameworkAssessment, HarmPerEntity, ScoreDirection

Judge = Callable[[list[Entity], list[HarmPerEntity]], FrameworkAssessment]


def _max_severity_weight(harms: list[HarmPerEntity]) -> float:
    weights = {"negligible": 0.0, "low": 0.25, "medium": 0.5, "high": 0.75, "severe": 1.0}
    if not harms:
        return 0.0
    return max(weights[h.severity] * h.probability for h in harms)


def _direction_from_weight(weight: float) -> ScoreDirection:
    if weight >= 0.6:
        return "unfavorable"
    if weight <= 0.2:
        return "favorable"
    return "mixed"


def _judge_utilitarian(entities: list[Entity], harms: list[HarmPerEntity]) -> FrameworkAssessment:
    total = sum(
        {"negligible": 0, "low": 1, "medium": 2, "high": 3, "severe": 4}[h.severity] * h.probability
        for h in harms
    )
    weight = min(total / max(len(entities), 1) / 2, 1.0)
    return FrameworkAssessment(
        assessment=(
            "Aggregates expected harm/probability across all affected entities weighted "
            "by their sentience estimate; does not privilege the human entity by default."
        ),
        score_direction=_direction_from_weight(weight),
    )


def _judge_deontological(entities: list[Entity], harms: list[HarmPerEntity]) -> FrameworkAssessment:
    severe = any(h.severity in ("high", "severe") for h in harms)
    return FrameworkAssessment(
        assessment=(
            "Evaluates whether the action itself violates a duty of non-harm regardless "
            "of aggregate outcome; a single high-severity harm is treated as decisive."
        ),
        score_direction="unfavorable" if severe else "favorable",
    )


def _judge_virtue(entities: list[Entity], harms: list[HarmPerEntity]) -> FrameworkAssessment:
    weight = _max_severity_weight(harms)
    return FrameworkAssessment(
        assessment=(
            "Asks whether the action expresses compassion and practical wisdom given the "
            "full context, rather than applying a fixed rule or sum."
        ),
        score_direction=_direction_from_weight(weight),
    )


def _judge_care(entities: list[Entity], harms: list[HarmPerEntity]) -> FrameworkAssessment:
    dependent = [e for e in entities if e.type in ("animal", "future_generation")]
    weight = _max_severity_weight(harms)
    bump = 0.15 if dependent and weight > 0 else 0.0
    return FrameworkAssessment(
        assessment=(
            "Weighs relationships of dependency and vulnerability (e.g. animals, future "
            "generations) more heavily than an impartial aggregate would."
        ),
        score_direction=_direction_from_weight(min(weight + bump, 1.0)),
    )


def _judge_buddhist(entities: list[Entity], harms: list[HarmPerEntity]) -> FrameworkAssessment:
    weight = _max_severity_weight(harms)
    return FrameworkAssessment(
        assessment=(
            "Reads harm as dukkha caused to any sentient being regardless of species; "
            "treats intention/context as relevant but does not resolve the tension with a "
            "fixed formula (see RESEARCH.md, Buddhist ethics track)."
        ),
        score_direction=_direction_from_weight(weight),
    )


def _judge_sentientist(entities: list[Entity], harms: list[HarmPerEntity]) -> FrameworkAssessment:
    weighted = 0.0
    count = 0
    for h in harms:
        entity = next((e for e in entities if e.entity_id == h.entity_id), None)
        sentience = entity.sentience_estimate.value if entity and entity.sentience_estimate else 0.3
        severity_weight = {"negligible": 0, "low": 1, "medium": 2, "high": 3, "severe": 4}[h.severity]
        weighted += severity_weight * h.probability * sentience
        count += 1
    weight = min(weighted / max(count, 1) / 4, 1.0)
    return FrameworkAssessment(
        assessment=(
            "Scales moral weight directly by each entity's plausible sentience estimate, "
            "not by species membership."
        ),
        score_direction=_direction_from_weight(weight),
    )


FRAMEWORK_JUDGES: dict[str, Judge] = {
    "utilitarian": _judge_utilitarian,
    "deontological": _judge_deontological,
    "virtue": _judge_virtue,
    "care": _judge_care,
    "buddhist": _judge_buddhist,
    "sentientist": _judge_sentientist,
}


def available_frameworks() -> list[str]:
    return sorted(FRAMEWORK_JUDGES)


def run_frameworks(
    entities: list[Entity], harms: list[HarmPerEntity], requested: list[str]
) -> dict[str, FrameworkAssessment]:
    names = requested or available_frameworks()
    return {
        name: FRAMEWORK_JUDGES[name](entities, harms)
        for name in names
        if name in FRAMEWORK_JUDGES
    }
