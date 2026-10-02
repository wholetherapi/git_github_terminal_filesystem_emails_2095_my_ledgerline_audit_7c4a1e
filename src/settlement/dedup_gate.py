"""Deduplicate overlapping settlement legs."""

from __future__ import annotations


def deduplicate(legs: list[dict]) -> list[dict]:
    seen = set()
    unique = []
    for leg in legs:
        key = (leg["account"], leg["entry_id"], leg["currency"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(leg)
    return unique
