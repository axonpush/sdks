"""Tests for the telemetry integration manifest.

The manifest is a plain typed data structure with no OTel dependency, so these
run regardless of whether the telemetry runtime API is present.
"""

from __future__ import annotations

import pytest

manifest = pytest.importorskip("axonpush.telemetry.manifest")

IntegrationManifest = manifest.IntegrationManifest
MANIFESTS = manifest.MANIFESTS
get_manifest = manifest.get_manifest
list_manifests = manifest.list_manifests


def test_vercel_ai_manifest_shape():
    m = get_manifest("vercel-ai")
    assert isinstance(m, IntegrationManifest)
    assert m.package == "ai"
    assert m.version_spec == "ai>=0.5,<0.6"
    assert set(m.capabilities) >= {"chat", "tools", "streaming", "usage"}
    assert m.content_capture_default in ("metadata_only", "redacted", "full")
    assert m.content_capture_default == "metadata_only"


def test_setup_snippet_is_copy_paste_ready():
    m = get_manifest("vercel-ai")
    snippet = m.setup_snippet
    assert "configure_telemetry" in snippet
    assert "genai_span" in snippet
    assert "record_genai_response" in snippet
    # snippet must be syntactically valid python
    compile(snippet, "<vercel-ai-snippet>", "exec")


def test_supports_helper_and_listing():
    m = get_manifest("vercel-ai")
    assert m.supports("tools") is True
    assert m.supports("embeddings") is False
    assert m in list_manifests()


def test_unknown_manifest_raises_with_known_keys():
    with pytest.raises(KeyError) as exc:
        get_manifest("does-not-exist")
    assert "vercel-ai" in str(exc.value)


def test_manifest_is_frozen():
    m = get_manifest("vercel-ai")
    with pytest.raises(Exception):
        m.name = "mutated"  # type: ignore[misc]
