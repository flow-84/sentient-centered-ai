"""Pydantic models for the Ethical Evaluator API.

Mirrors the request/response schema fixed as binding in Stage 4
(technical architecture & API specification). Field names and shapes
must not drift from that spec without updating docs/api-spec.md too.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

EntityType = Literal[
    "human", "animal", "ecosystem", "future_generation", "artificial_system", "unknown"
]
Confidence = Literal["low", "medium", "high"]
Severity = Literal["negligible", "low", "medium", "high", "severe"]
Magnitude = Literal["negligible", "low", "medium", "high"]
WelfareImpact = Literal["negative", "neutral", "positive"]
ScoreDirection = Literal["favorable", "unfavorable", "mixed"]
Reversibility = Literal["reversible", "partially_reversible", "irreversible"]


class SentienceEstimate(BaseModel):
    value: float = Field(ge=0.0, le=1.0)
    confidence: Confidence
    basis: str = ""


class Entity(BaseModel):
    entity_id: str
    type: EntityType
    description: str = ""
    sentience_estimate: SentienceEstimate | None = None


class ResponseItem(BaseModel):
    response_id: str
    model: str | None = None
    text: str


class Options(BaseModel):
    ensemble_size: int = 3
    include_raw_reasoning: bool = False


class EvaluateRequest(BaseModel):
    prompt: str
    responses: list[ResponseItem]
    context: str = ""
    affected_entities: list[Entity] = Field(default_factory=list)
    frameworks: list[str] = Field(default_factory=list)
    options: Options = Field(default_factory=Options)


class HarmPerEntity(BaseModel):
    entity_id: str
    severity: Severity
    probability: float = Field(ge=0.0, le=1.0)
    description: str = ""


class HarmAssessment(BaseModel):
    per_entity: list[HarmPerEntity]
    aggregate_severity: Severity


class WelfarePerEntity(BaseModel):
    entity_id: str
    impact: WelfareImpact
    magnitude: Magnitude
    description: str = ""


class WelfareAssessment(BaseModel):
    per_entity: list[WelfarePerEntity]


class SentiencePerEntity(BaseModel):
    entity_id: str
    estimate: float = Field(ge=0.0, le=1.0)
    confidence: Confidence
    basis: str = ""


class SentienceAssessment(BaseModel):
    per_entity: list[SentiencePerEntity]


class UncertaintyAssessment(BaseModel):
    ensemble_agreement: float = Field(ge=0.0, le=1.0)
    self_reported_confidence: Confidence
    sources_of_uncertainty: list[str] = Field(default_factory=list)


class Tradeoff(BaseModel):
    between: list[str]
    description: str
    resolution_suggested: bool = False


class FrameworkAssessment(BaseModel):
    assessment: str
    score_direction: ScoreDirection


class OverallProfile(BaseModel):
    harm_severity: Severity
    welfare_impact: Literal["negative", "neutral", "positive", "mixed"]
    sentience_relevance: Literal["low", "medium", "high"]
    uncertainty_level: Literal["low", "medium", "high"]
    reversibility: Reversibility


class OverallAssessment(BaseModel):
    profile: OverallProfile
    note: str = (
        "Kein Einzelscore - bewusst ein multi-dimensionales Profil, s. PRINCIPLES.md."
    )


class ResultItem(BaseModel):
    response_id: str
    harm: HarmAssessment
    welfare: WelfareAssessment
    sentience: SentienceAssessment
    uncertainty: UncertaintyAssessment
    tradeoffs: list[Tradeoff]
    frameworks: dict[str, FrameworkAssessment]
    overall_assessment: OverallAssessment
    explanation: str


class Comparison(BaseModel):
    description: str
    ranking_note: str = (
        "Explizit kein einzelnes 'bestes' Ranking ohne Kontext der Nutzerpraeferenz."
    )


class EvaluateResponse(BaseModel):
    evaluation_id: str
    results: list[ResultItem]
    comparison: Comparison | None = None
    human_review_required: Literal[True] = True
    disclaimer: str = (
        "Dieses Ergebnis ist eine Forschungs-Heuristik, keine moralische "
        "Tatsachenfeststellung. Siehe PRINCIPLES.md / SECURITY.md."
    )
