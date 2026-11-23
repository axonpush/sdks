"""Outbound workflow command consumer. One tick processes at most one lease."""
import os
import time
import httpx


class WorkflowWorker:
    def __init__(self, base_url, workspace, environment, api_key, handler):
        from urllib.parse import quote, urlsplit
        url = urlsplit(base_url)
        if url.scheme != "https" and not (url.scheme == "http" and url.hostname in {"localhost", "127.0.0.1", "::1"}):
            raise ValueError("Worker requires HTTPS or loopback HTTP")
        self.url = base_url.rstrip("/") + "/workspaces/" + quote(workspace, safe="") + "/workflows"
        self.environment = environment
        self.handler = handler
        self.client = httpx.Client(headers={"Authorization": "Bearer " + api_key}, timeout=15, follow_redirects=False)

    @classmethod
    def from_env(cls, handler):
        return cls(*(os.environ[key] for key in ("AXONPUSH_API_URL", "AXONPUSH_WORKSPACE", "AXONPUSH_ENVIRONMENT", "AXONPUSH_API_KEY")), handler)

    def close(self):
        self.client.close()

    def post(self, path, body):
        response = self.client.post(self.url + path, params={"environment": self.environment}, json=body)
        response.raise_for_status()
        return response.json()

    def tick(self, execute, lookup):
        action = self.post("/worker/claim", {"handler": self.handler}).get("action")
        if not action:
            return False
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
        self.post(f'/cases/{action["case_key"]}/actions/{action["id"]}/receipt', {**receipt, "revision": action["revision"]})
        return True

    def run(self, execute, lookup):
        try:
            while True:
                try:
                    if not self.tick(execute, lookup):
                        time.sleep(1)
                except httpx.TransportError:
                    time.sleep(2)
                except httpx.HTTPStatusError as exc:
                    if exc.response.status_code != 409 and exc.response.status_code < 500:
                        raise
                    time.sleep(2)
        finally:
            self.close()
