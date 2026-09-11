"""OTel-native telemetry for AxonPush.

The runtime API (``configure_telemetry``, ``TelemetryHandle``, ``genai_span``,
``record_genai_response``, ``record_genai_content``) is defined in
:mod:`axonpush.telemetry.core` and re-exported here. The integration manifest
is always importable regardless of whether the OTel extras are installed.
"""

from __future__ import annotations

from axonpush.telemetry.manifest import (  # noqa: F401
    IntegrationManifest,
    MANIFESTS,
    get_manifest,
    list_manifests,
)

__all__ = [
    "IntegrationManifest",
    "MANIFESTS",
    "get_manifest",
    "list_manifests",
]

# The runtime API depends on the OTel SDK. Keep the import guarded so the
# manifest stays importable when the extras are absent.
try:
    from axonpush.telemetry.core import (  # noqa: F401
        _INSTALLED,
        TelemetryHandle,
        configure_telemetry,
        genai_span,
        record_genai_content,
        record_genai_response,
    )

    __all__ += [
        "TelemetryHandle",
        "configure_telemetry",
        "genai_span",
        "record_genai_content",
        "record_genai_response",
    ]
except ImportError:
    pass
