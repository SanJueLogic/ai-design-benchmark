"""Tests for tools/confidence.py"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

from scoring import aggregate
from confidence import compute_scene_confidence, bootstrap_overall_ci


PRODUCT_MAP = {"1": "ProductA", "2": "ProductB", "3": "ProductC"}


def make_rows(entries):
    return [
        {"scene": s, "evaluator": "E01", "role": "Design", "task": t, "question": q, "vote": v}
        for s, t, q, v in entries
    ]


def test_confidence_high():
    """A gap ≥ 20% should produce ✅ High confidence."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "1"),
        ("SceneA", "T-001", "Q2", "1"),
        ("SceneA", "T-001", "Q3", "1"),
        ("SceneA", "T-001", "Q4", "1"),
        ("SceneA", "T-002", "Q1", "2"),
        ("SceneA", "T-003", "Q1", "1"),
        ("SceneA", "T-004", "Q1", "1"),
        ("SceneA", "T-005", "Q1", "1"),
    ])
    results = aggregate(rows, PRODUCT_MAP)
    conf = compute_scene_confidence(results)
    assert len(conf) == 1
    assert "High" in conf[0]["confidence"]


def test_confidence_low():
    """A gap < 10% should produce ❌ Low confidence."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "1"),
        ("SceneA", "T-002", "Q1", "2"),
    ])
    results = aggregate(rows, PRODUCT_MAP)
    conf = compute_scene_confidence(results)
    assert "Low" in conf[0]["confidence"]


def test_bootstrap_ci_order():
    """Bootstrap CI lo must be ≤ mean ≤ hi for all products."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "1"),
        ("SceneA", "T-001", "Q2", "1"),
        ("SceneA", "T-002", "Q1", "2"),
        ("SceneA", "T-002", "Q2", "2"),
        ("SceneA", "T-003", "Q1", "3"),
    ])
    ci = bootstrap_overall_ci(rows, PRODUCT_MAP, n_iter=200, seed=0)
    for prod, vals in ci.items():
        assert vals["lo"] <= vals["mean"] <= vals["hi"], f"{prod}: CI bounds out of order {vals}"


def test_bootstrap_reproducible():
    """Same seed must produce the same CI values across two calls."""
    rows = make_rows([
        ("SceneA", "T-001", "Q1", "1"),
        ("SceneA", "T-002", "Q1", "2"),
    ])
    ci1 = bootstrap_overall_ci(rows, PRODUCT_MAP, n_iter=100, seed=42)
    ci2 = bootstrap_overall_ci(rows, PRODUCT_MAP, n_iter=100, seed=42)
    for prod in ci1:
        assert ci1[prod]["mean"] == ci2[prod]["mean"]
        assert ci1[prod]["lo"] == ci2[prod]["lo"]
        assert ci1[prod]["hi"] == ci2[prod]["hi"]
