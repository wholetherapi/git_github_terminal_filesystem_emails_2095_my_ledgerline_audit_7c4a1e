"""FX rate refresh helpers for the nightly rollup."""

from __future__ import annotations


def refresh(rates: dict[str, float], fresh: dict[str, float]) -> dict[str, float]:
    merged = dict(rates)
    merged.update(fresh)
    return merged
