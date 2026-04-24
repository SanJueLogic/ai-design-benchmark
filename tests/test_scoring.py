"""Tests for tools/scoring.py"""

import sys
import os
import csv
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

from scoring import aggregate, load_votes, SKIP_VOTES


PRODUCT_MAP = {"1": "ProductA", "2": "ProductB", "3": "ProductC"}


def make_rows(entries):
    """Helper: build vote row dicts from (scene, task, question, vote) tuples."""
    return [
        {"scene": s, "evaluator": "E01", "role": "Design", "task": t, "question": q, "vote": v}
        for s, t, q, v in entries
    ]


def test_simple_winner():
    """One product wins all 5 questions for one task — should have 100% win rate."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "1"),
        ("SceneA", "T-001", "Q2", "1"),
        ("SceneA", "T-001", "Q3", "1"),
        ("SceneA", "T-001", "Q4", "1"),
        ("SceneA", "T-001", "Q5", "1"),
    ])
    results = aggregate(rows, PRODUCT_MAP)
    scene_results = {r["product"]: r for r in results if r["scene"] == "SceneA"}
    assert scene_results["ProductA"]["tasks_won"] == 1
    assert scene_results["ProductB"]["tasks_won"] == 0
    assert scene_results["ProductC"]["tasks_won"] == 0
    assert scene_results["ProductA"]["win_rate"] == "100.0%"


def test_skip_votes_excluded():
    """Votes of '5' (about the same) and '6' (not relevant) must not be counted."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "5"),  # skip
        ("SceneA", "T-001", "Q2", "6"),  # skip
        ("SceneA", "T-001", "Q3", "2"),  # ProductB wins
        ("SceneA", "T-001", "Q4", "2"),
        ("SceneA", "T-001", "Q5", "2"),
    ])
    results = aggregate(rows, PRODUCT_MAP)
    scene_results = {r["product"]: r for r in results if r["scene"] == "SceneA"}
    assert scene_results["ProductB"]["tasks_won"] == 1
    assert scene_results["ProductA"]["tasks_won"] == 0


def test_known_csv_reproduces_numbers():
    """Loading the bundled raw-votes.csv must reproduce the published Round 1 numbers."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "results", "round-1", "raw-votes.csv")
    if not os.path.exists(csv_path):
        return  # skip if CSV not present (e.g. partial clone)

    real_map = {"1": "Lovart", "2": "Roboneo", "3": "即梦"}
    rows = load_votes(csv_path)
    assert len(rows) == 3645, f"Expected 3645 vote rows, got {len(rows)}"

    results = aggregate(rows, real_map)
    totals = {r["product"]: r for r in results if r["scene"] == "[Total]"}

    lovart_rate = float(totals["Lovart"]["win_rate"].strip("%"))
    assert 54 < lovart_rate < 58, f"Lovart overall win rate out of expected range: {lovart_rate}%"


def test_tie_handling():
    """When two products tie on question wins, both should be recorded as task winners."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "1"),  # ProductA
        ("SceneA", "T-001", "Q2", "1"),  # ProductA
        ("SceneA", "T-001", "Q3", "2"),  # ProductB
        ("SceneA", "T-001", "Q4", "2"),  # ProductB
        ("SceneA", "T-001", "Q5", "3"),  # ProductC — irrelevant to tie
    ])
    results = aggregate(rows, PRODUCT_MAP)
    scene_results = {r["product"]: r for r in results if r["scene"] == "SceneA"}
    # ProductA and ProductB both won 2 questions — both should get credit
    assert scene_results["ProductA"]["tasks_won"] == 1
    assert scene_results["ProductB"]["tasks_won"] == 1
    assert scene_results["ProductC"]["tasks_won"] == 0


def test_write_and_read_results(tmp_path):
    """write_results should produce a readable CSV with correct columns."""
    from scoring import write_results
    rows = make_rows([("S", "T-001", "Q1", "1")])
    results = aggregate(rows, PRODUCT_MAP)
    out = str(tmp_path / "out.csv")
    write_results(results, out)
    with open(out, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows_out = list(reader)
    assert all("scene" in r and "win_rate" in r for r in rows_out)
