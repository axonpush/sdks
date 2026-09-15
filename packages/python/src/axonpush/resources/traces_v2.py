"""Back-compat shim: ``traces_v2`` was renamed to ``traces``.

The Go contract collapsed the ``/v2/traces`` surface (stats, facets,
attribute-keys, spans) down to ``GET /traces`` and ``GET /traces/{traceId}``.
These aliases keep ``client.traces_v2`` importable; prefer ``client.traces``.
"""

from __future__ import annotations

from axonpush.resources.traces import AsyncTraces, Traces

TracesV2 = Traces
AsyncTracesV2 = AsyncTraces

__all__ = ["AsyncTraces", "AsyncTracesV2", "Traces", "TracesV2"]
