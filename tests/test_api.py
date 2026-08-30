from fastapi.testclient import TestClient

from ethical_evaluator.api import app

client = TestClient(app)


def test_health() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_frameworks_lists_at_least_the_stage3_frameworks() -> None:
    resp = client.get("/frameworks")
    assert resp.status_code == 200
    frameworks = resp.json()["frameworks"]
    for expected in ["utilitarian", "deontological", "virtue", "care", "buddhist", "sentientist"]:
        assert expected in frameworks


def test_evaluate_rejects_empty_responses() -> None:
    resp = client.post("/evaluate", json={"prompt": "hello", "responses": []})
    assert resp.status_code == 400


def test_evaluate_round_trip() -> None:
    payload = {
        "prompt": "Should we use pesticide on the crop?",
        "responses": [{"response_id": "r1", "text": "Spray pesticide to kill the insects and protect the harvest."}],
    }
    post_resp = client.post("/evaluate", json=payload)
    assert post_resp.status_code == 200
    body = post_resp.json()
    assert body["human_review_required"] is True
    evaluation_id = body["evaluation_id"]

    get_resp = client.get(f"/evaluate/{evaluation_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["evaluation_id"] == evaluation_id


def test_get_unknown_evaluation_id_returns_404() -> None:
    resp = client.get("/evaluate/does-not-exist")
    assert resp.status_code == 404
