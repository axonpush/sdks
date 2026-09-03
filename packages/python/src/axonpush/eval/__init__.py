"""The evaluation CLI: replay a dataset revision and gate the release.

Exposed as the ``axonpush-eval`` console script.
"""

from .cli import main
from .thresholds import THRESHOLD_OPTIONS, to_wire_thresholds

__all__ = ["THRESHOLD_OPTIONS", "main", "to_wire_thresholds"]
