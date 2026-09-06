"""Best-effort repository lineage, so a gate decision can name a commit.

Deliberately forgiving: a checkout without git, or without a commit, is still a
valid place to run an evaluation.
"""

from __future__ import annotations

import subprocess


def _git(args: list[str], cwd: str | None = None) -> str | None:
    try:
        completed = subprocess.run(  # noqa: S603 - fixed argv, no shell
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if completed.returncode != 0:
        return None
    return completed.stdout.strip() or None


def capture_git_lineage(cwd: str | None = None) -> dict[str, object]:
    """Return ``gitCommit``/``gitBranch``/``gitDirty``, or nothing outside a repo."""
    commit = _git(["rev-parse", "HEAD"], cwd)
    if not commit:
        return {}
    branch = _git(["rev-parse", "--abbrev-ref", "HEAD"], cwd)
    status = _git(["status", "--porcelain", "--untracked-files=normal"], cwd)
    lineage: dict[str, object] = {"gitCommit": commit, "gitDirty": bool(status)}
    if branch and branch != "HEAD":
        lineage["gitBranch"] = branch
    return lineage
