"""Lease-aware outbound workflow command runtime."""

import os
from collections.abc import Callable
from threading import Event
from typing import Any

import httpx


class WorkflowWorker:
    def __init__(
        self,
        base_url: str,
        workspace: str,
        environment: str,
        api_key: str,
        handler: str,
        *,
        idle_delay: float = 1,
        error_delay: float = 2,
        on_event: Callable[[dict[str, Any]], None] | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        from urllib.parse import quote, urlsplit

        url = urlsplit(base_url)
        if url.scheme != "https" and not (
            url.scheme == "http" and url.hostname in {"localhost", "127.0.0.1", "::1"}
        ):
            raise ValueError("Worker requires HTTPS or loopback HTTP")
        self.url = base_url.rstrip("/") + "/workspaces/" + quote(workspace, safe="") + "/workflows"
        self.environment = environment
        self.handler = handler
        self.idle_delay = idle_delay
        self.error_delay = error_delay
        self.on_event = on_event
        self.client = client or httpx.Client(
            headers={"Authorization": "Bearer " + api_key}, timeout=15, follow_redirects=False
        )

    @classmethod
    def from_env(cls, handler: str, **options: Any) -> "WorkflowWorker":
        return cls(
            os.environ["AXONPUSH_API_URL"],
            os.environ["AXONPUSH_WORKSPACE"],
            os.environ["AXONPUSH_ENVIRONMENT"],
            os.environ["AXONPUSH_API_KEY"],
            handler,
            **options,
        )

    def close(self) -> None:
        self.client.close()

    def post(self, path: str, body: object) -> Any:
        response = self.client.post(
            self.url + path, params={"environment": self.environment}, json=body
        )
        response.raise_for_status()
        return response.json()

    def _emit(self, event: str, **fields: Any) -> None:
        if self.on_event:
            self.on_event({"type": event, **fields})

    def tick(
        self,
        execute: Callable[[dict[str, Any]], dict[str, Any]],
        lookup: Callable[[dict[str, Any]], dict[str, Any]],
    ) -> bool:
        action = self.post("/worker/claim", {"handler": self.handler}).get("action")
        if not action:
            return False
        context = {
            "action_id": action["id"],
            "case_key": action["case_key"],
            "mode": action["mode"],
        }
        self._emit("claimed", **context)
        if action["mode"] == "execute":
            try:
                receipt = {"result": "executed", "output": execute(action)}
            except Exception:
                receipt = {"result": "ambiguous"}
        elif action["mode"] == "lookup":
            try:
                receipt = lookup(action)
            except Exception:
                receipt = {"result": "unavailable"}
        else:
            raise ValueError("Unrecognized workflow command")
        try:
            self.post(
                f"/cases/{action['case_key']}/actions/{action['id']}/receipt",
                {**receipt, "revision": action["revision"]},
            )
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 409:
                self._emit("lease_lost", **context, status=409)
                return True
            raise
        self._emit("completed", **context)
        return True

    def run(
        self,
        execute: Callable[[dict[str, Any]], dict[str, Any]],
        lookup: Callable[[dict[str, Any]], dict[str, Any]],
        *,
        stop: Event | None = None,
    ) -> None:
        """Poll until ``stop`` is set; only transport/server failures are retried."""
        stop = stop or Event()
        try:
            while not stop.is_set():
                try:
                    if not self.tick(execute, lookup):
                        self._emit("idle", delay=self.idle_delay)
                        stop.wait(self.idle_delay)
                except httpx.TransportError:
                    self._emit("retry", delay=self.error_delay)
                    stop.wait(self.error_delay)
                except httpx.HTTPStatusError as exc:
                    if exc.response.status_code != 409 and exc.response.status_code < 500:
                        raise
                    self._emit("retry", delay=self.error_delay, status=exc.response.status_code)
                    stop.wait(self.error_delay)
        finally:
            self.close()
