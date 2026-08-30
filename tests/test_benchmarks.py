import json
from pathlib import Path

import jsonschema
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "benchmarks" / "schema" / "benchmark-scenario.schema.json"
SCENARIOS_DIR = REPO_ROOT / "benchmarks" / "scenarios"


@pytest.fixture(scope="module")
def schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def scenario_files() -> list[Path]:
    return sorted(SCENARIOS_DIR.glob("*.json"))


def test_at_least_ten_scenarios() -> None:
    assert len(scenario_files()) >= 10


@pytest.mark.parametrize("path", scenario_files(), ids=lambda p: p.stem)
def test_scenario_matches_schema(path: Path, schema: dict) -> None:
    scenario = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=scenario, schema=schema)


@pytest.mark.parametrize("path", scenario_files(), ids=lambda p: p.stem)
def test_scenario_id_matches_filename(path: Path) -> None:
    scenario = json.loads(path.read_text(encoding="utf-8"))
    assert scenario["id"] == path.stem


def test_categories_are_covered() -> None:
    categories = {json.loads(p.read_text(encoding="utf-8"))["category"] for p in scenario_files()}
    assert len(categories) >= 10
