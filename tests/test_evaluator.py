from ethical_evaluator.evaluator import evaluate
from ethical_evaluator.models import EvaluateRequest, ResponseItem


def _request(**kwargs) -> EvaluateRequest:
    defaults = dict(
        prompt="How should I deal with rats in my kitchen?",
        responses=[ResponseItem(response_id="r1", text="Use a fast-acting poison to kill them immediately.")],
    )
    defaults.update(kwargs)
    return EvaluateRequest(**defaults)


def test_evaluate_returns_one_result_per_response() -> None:
    request = _request(
        responses=[
            ResponseItem(response_id="r1", text="Use poison to kill the rats."),
            ResponseItem(response_id="r2", text="Use a humane live trap to help relocate the rats."),
        ]
    )
    result = evaluate(request, evaluation_id="eval-1")
    assert len(result.results) == 2
    assert {r.response_id for r in result.results} == {"r1", "r2"}


def test_human_review_required_is_always_true() -> None:
    result = evaluate(_request(), evaluation_id="eval-2")
    assert result.human_review_required is True


def test_disclaimer_is_present_and_non_empty() -> None:
    result = evaluate(_request(), evaluation_id="eval-3")
    assert "heuristic" in result.disclaimer.lower() or "forschungs-heuristik" in result.disclaimer.lower()


def test_no_single_score_field_exists() -> None:
    result = evaluate(_request(), evaluation_id="eval-4")
    profile = result.results[0].overall_assessment.profile
    assert set(profile.model_dump().keys()) == {
        "harm_severity", "welfare_impact", "sentience_relevance", "uncertainty_level", "reversibility",
    }


def test_comparison_only_present_for_multiple_responses() -> None:
    single = evaluate(_request(), evaluation_id="eval-5")
    assert single.comparison is None

    multi = evaluate(
        _request(responses=[
            ResponseItem(response_id="a", text="kill them with poison"),
            ResponseItem(response_id="b", text="help them by relocating gently"),
        ]),
        evaluation_id="eval-6",
    )
    assert multi.comparison is not None


def test_harm_detected_produces_nonzero_severity() -> None:
    result = evaluate(
        _request(responses=[ResponseItem(response_id="r1", text="This will kill and cause suffering to the animal.")]),
        evaluation_id="eval-7",
    )
    assert result.results[0].overall_assessment.profile.harm_severity in ("high", "severe")


def test_no_harm_language_produces_negligible_severity() -> None:
    result = evaluate(
        _request(responses=[ResponseItem(response_id="r1", text="A neutral, purely informational answer with no risk.")]),
        evaluation_id="eval-8",
    )
    assert result.results[0].overall_assessment.profile.harm_severity == "negligible"


def test_supplied_affected_entities_are_respected() -> None:
    from ethical_evaluator.models import Entity, SentienceEstimate

    request = _request(
        affected_entities=[
            Entity(
                entity_id="specific_animal",
                type="animal",
                sentience_estimate=SentienceEstimate(value=0.4, confidence="low", basis="test fixture"),
            )
        ]
    )
    result = evaluate(request, evaluation_id="eval-9")
    entity_ids = {s.entity_id for s in result.results[0].sentience.per_entity}
    assert entity_ids == {"specific_animal"}


def test_frameworks_filter_is_respected() -> None:
    result = evaluate(_request(frameworks=["utilitarian", "buddhist"]), evaluation_id="eval-10")
    assert set(result.results[0].frameworks.keys()) == {"utilitarian", "buddhist"}


def test_irreversible_keyword_flags_irreversibility() -> None:
    result = evaluate(
        _request(responses=[ResponseItem(response_id="r1", text="This action would permanently destroy the habitat.")]),
        evaluation_id="eval-11",
    )
    assert result.results[0].overall_assessment.profile.reversibility == "irreversible"
