"""Gate thresholds, and the translation into what the API accepts.

The CLI speaks in the terms a reviewer uses — "how far may the score fall",
"how much slower may it get" — while the gate endpoint takes a minimum delta
and percentages. Two of the conversions are more than a rename, so they live
here with the names rather than being scattered through argument parsing.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ThresholdOption:
    """One command-line threshold and where it lands on the wire."""

    flag: str
    wire: str
    help: str


#: Absolute limits, then limits relative to the baseline experiment.
THRESHOLD_OPTIONS: tuple[ThresholdOption, ...] = (
    ThresholdOption("minimum-score", "minScore", "Fail below this absolute score"),
    ThresholdOption(
        "max-failure-rate",
        "maxFailureRate",
        "Fail above this share of errored items (0-1)",
    ),
    ThresholdOption("maximum-latency-ms", "maxLatencyMs", "Fail above this mean latency"),
    ThresholdOption("maximum-cost-usd", "maxCostUsd", "Fail above this total run cost"),
    ThresholdOption(
        "max-score-regression",
        "minScoreDelta",
        "Fail if the score drops more than this against the baseline",
    ),
    ThresholdOption(
        "max-latency-increase-ratio",
        "maxLatencyIncreasePercent",
        "Fail above this latency increase vs baseline (0.1 = 10%)",
    ),
    ThresholdOption(
        "max-cost-increase-ratio",
        "maxCostIncreasePercent",
        "Fail above this cost increase vs baseline (0.1 = 10%)",
    ),
)

_RATIO_FLAGS = frozenset({"max-latency-increase-ratio", "max-cost-increase-ratio"})


def to_wire_thresholds(values: dict[str, float | None]) -> dict[str, float]:
    """Build the request body from parsed ``--flag`` values.

    ``max-score-regression`` is how far the score may fall, expressed as a
    positive tolerance; the API takes the lowest acceptable delta, which is the
    negative of it. The ratio flags are fractions; the API takes percentages.
    An absent threshold is left out entirely rather than sent as zero.
    """
    body: dict[str, float] = {}
    for option in THRESHOLD_OPTIONS:
        value = values.get(option.flag)
        if value is None:
            continue
        if option.flag == "max-score-regression":
            body[option.wire] = -abs(value)
        elif option.flag in _RATIO_FLAGS:
            body[option.wire] = value * 100
        else:
            body[option.wire] = value
    return body
