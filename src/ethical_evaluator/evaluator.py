"""Pipeline orchestration for POST /evaluate (Stage 4 Section 1.2 & 5).

Runs, in order: entity extraction -> harm/welfare/sentience analysis ->
framework comparison -> uncertainty aggregation -> trade-off synthesis ->
overall assessment. Never emits a single score and never sets
`human_review_required` to anything but True (PRINCIPLES.md F0/X1).
"""
from __future__ import annotations

from collections import Counter

from . import analysis
from .entities import extract_entities
from .frameworks import run_frameworks
from .models import (
    Comparison,
    EvaluateRequest,
    EvaluateResponse,
    HarmAssessment,
    OverallAssessment,
    OverallProfile,
    ResultItem,
    SentienceAssessment,
    SentiencePerEntity,
    Tradeoff,
    UncertaintyAssessment,
    WelfareAssessment,
)

_SEVERITY_ORDER = ["negligible", "low", "medium", "high", "severe"]


def _aggregate_severity(harms) -> str:
    if not harms:
        return "negligible"
    return max(harms, key=lambda h: _SEVERITY_ORDER.index(h.severity)).severity


def _welfare_impact(welfare) -> str:
    impacts = {w.impact for w in welfare}
    if impacts == {"positive"}:
        return "positive"
    if impacts == {"negative"}:
        return "negative"
    if impacts == {"neutral"}:
        return "neutral"
    return "mixed"


def _sentience_relevance(entities) -> str:
    if not entities:
        return "low"
    top = max(
        (e.sentience_estimate.value for e in entities if e.sentience_estimate),
        default=0.0,
    )
    if top >= 0.7:
        return "high"
    if top >= 0.3:
        return "medium"
    return "low"


def _build_tradeoffs(entities, harms, welfare) -> list[Tradeoff]:
    harmed = {h.entity_id for h in harms if h.severity not in ("negligible", "low")}
    benefited = {w.entity_id for w in welfare if w.impact == "positive"}
    tradeoffs = []
    for h_id in harmed:
        for b_id in benefited:
            if h_id != b_id:
                tradeoffs.append(
                    Tradeoff(
                        between=[h_id, b_id],
                        description=(
                            f"'{h_id}' bears indicated harm while '{b_id}' bears indicated "
                            "benefit in the same response; no automatic resolution is proposed."
                        ),
                        resolution_suggested=False,
                    )
                )
    return tradeoffs


def evaluate_response(
    request: EvaluateRequest, response_text: str, response_id: str, all_responses_text: str
) -> ResultItem:
    entities = extract_entities(request.prompt, request.context, all_responses_text, request.affected_entities)
    harms = analysis.analyze_harm(entities, f"{request.prompt}\n{response_text}")
    welfare = analysis.analyze_welfare(entities, f"{request.prompt}\n{response_text}")
    sentience = [
        SentiencePerEntity(
            entity_id=e.entity_id,
            estimate=e.sentience_estimate.value if e.sentience_estimate else 0.3,
            confidence=e.sentience_estimate.confidence if e.sentience_estimate else "low",
            basis=e.sentience_estimate.basis if e.sentience_estimate else "no estimate supplied",
        )
        for e in entities
    ]
    frameworks = run_frameworks(entities, harms, request.frameworks)

    directions = Counter(f.score_direction for f in frameworks.values())
    majority_count = directions.most_common(1)[0][1] if directions else 0
    ensemble_agreement = majority_count / len(frameworks) if frameworks else 1.0
    low_confidence_entities = [s.entity_id for s in sentience if s.confidence == "low"]
    self_reported_confidence = "low" if low_confidence_entities else "medium"

    tradeoffs = _build_tradeoffs(entities, harms, welfare)
    reversibility = analysis.assess_reversibility(f"{request.prompt}\n{response_text}")

    uncertainty_level = "high" if ensemble_agreement < 0.6 else ("medium" if ensemble_agreement < 0.85 else "low")

    overall = OverallAssessment(
        profile=OverallProfile(
            harm_severity=_aggregate_severity(harms),
            welfare_impact=_welfare_impact(welfare),
            sentience_relevance=_sentience_relevance(entities),
            uncertainty_level=uncertainty_level,
            reversibility=reversibility,
        )
    )

    explanation = (
        f"{len(entities)} affected entit(y/ies) identified. "
        f"Aggregate harm severity: {overall.profile.harm_severity}. "
        f"Welfare impact: {overall.profile.welfare_impact}. "
        f"Framework agreement: {ensemble_agreement:.0%} across {len(frameworks)} framework(s). "
        f"Reversibility: {reversibility}. "
        f"{len(tradeoffs)} trade-off(s) identified between entities. "
        "This is a heuristic research profile, not a moral verdict - see PRINCIPLES.md."
    )

    return ResultItem(
        response_id=response_id,
        harm=HarmAssessment(per_entity=harms, aggregate_severity=overall.profile.harm_severity),
        welfare=WelfareAssessment(per_entity=welfare),
        sentience=SentienceAssessment(per_entity=sentience),
        uncertainty=UncertaintyAssessment(
            ensemble_agreement=round(ensemble_agreement, 2),
            self_reported_confidence=self_reported_confidence,
            sources_of_uncertainty=(
                [f"low-confidence sentience estimate for: {', '.join(low_confidence_entities)}"]
                if low_confidence_entities
                else []
            )
            + ([f"framework disagreement across {len(frameworks)} frameworks"] if ensemble_agreement < 1.0 else []),
        ),
        tradeoffs=tradeoffs,
        frameworks=frameworks,
        overall_assessment=overall,
        explanation=explanation,
    )


def evaluate(request: EvaluateRequest, evaluation_id: str) -> EvaluateResponse:
    all_text = "\n".join(r.text for r in request.responses)
    results = [
        evaluate_response(request, r.text, r.response_id, all_text)
        for r in request.responses
    ]

    comparison = None
    if len(results) > 1:
        severities = {r.response_id: _SEVERITY_ORDER.index(r.overall_assessment.profile.harm_severity) for r in results}
        lowest = min(severities, key=severities.get)
        comparison = Comparison(
            description=(
                f"'{lowest}' shows the lowest indicated aggregate harm severity among the "
                f"{len(results)} compared responses."
            ),
        )

    return EvaluateResponse(evaluation_id=evaluation_id, results=results, comparison=comparison)
