"""Local workflow tooling. Evaluation is delegated to the pinned Go executable."""

from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
from importlib.resources import files
from pathlib import Path
from typing import Any

from axonpush._internal.api.models import FactsInputBody as PublishWorkflowFacts
from axonpush._internal.api.models import Input as WorkflowInput

__all__ = ["run", "resolve_binary", "PublishWorkflowFacts", "WorkflowInput", "COMPILER_VERSION"]

COMPILER_VERSION = "0.1.1"


def main() -> int:
    """Forward CLI arguments, streams and exit status to the native workflow tool."""
    return subprocess.call([resolve_binary(), *sys.argv[1:]])


def resolve_binary() -> str:
    """Resolve the bundled platform binary, with an explicit env override."""
    override = os.environ.get("AXONPUSH_WORKFLOW_BINARY")
    if override and Path(override).is_file():
        return str(Path(override).resolve())
    system = {"Windows": "windows", "Darwin": "darwin", "Linux": "linux"}.get(
        platform.system(), platform.system().lower()
    )
    machine = {"x86_64": "amd64", "AMD64": "amd64", "aarch64": "arm64"}.get(
        platform.machine(), platform.machine().lower()
    )
    name = "axonpush.exe" if system == "windows" else "axonpush"
    resource = files("axonpush").joinpath("bin").joinpath(f"{system}-{machine}").joinpath(name)
    if resource.is_file():
        return str(resource)
    raise ValueError(f"No workflow compiler for {system}-{machine}; set AXONPUSH_WORKFLOW_BINARY")


def run(*arguments: str, binary: str | None = None, timeout: float = 30) -> Any:
    """Run a local command without a shell; no model or server calls are made.

    Supply AXONPUSH_WORKFLOW_BINARY or an explicit path to a verified release
    binary. Publishing is deliberately excluded from this offline helper.
    """
    if not arguments or arguments[0] not in {
        "init",
        "validate",
        "generate",
        "test",
        "action-test",
        "diff",
    }:
        raise ValueError("Expected init, validate, generate, test, action-test or diff")
    executable = binary or resolve_binary()
    if not Path(executable).is_file():
        raise ValueError("Workflow compiler executable does not exist")
    executable = str(Path(executable).resolve())
    version = subprocess.run(
        [executable, "workflow", "version"],
        capture_output=True,
        text=True,
        check=True,
        timeout=timeout,
    )
    if json.loads(version.stdout).get("version") != COMPILER_VERSION:
        raise ValueError(f"Workflow compiler {COMPILER_VERSION} is required")
    result = subprocess.run(
        [executable, "workflow", *arguments],
        capture_output=True,
        text=True,
        check=True,
        timeout=timeout,
    )
    return json.loads(result.stdout) if result.stdout.strip() else None
