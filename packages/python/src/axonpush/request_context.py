"""Client-owned customer identity. Profile updates remain explicit identify calls."""

from __future__ import annotations
from contextvars import ContextVar
from copy import deepcopy
from types import SimpleNamespace
from typing import Any, Mapping
from axonpush._internal.api.models import FactsInputBody
from axonpush._tracing import TraceContext, current_trace, set_current_trace, _clear_current_trace

_current: ContextVar[dict[object, dict[str, Any]]] = ContextVar(
    "axonpush_customer_context", default={}
)


def current_context(owner: object) -> dict[str, Any] | None:
    try:
        return _current.get().get(owner)
    except TypeError:
        # Protocol-compatible integration clients need not be hashable.
        return None


def attributes(context: Mapping[str, Any] | None) -> dict[str, Any]:
    if context is None:
        return {}
    subjects = dict(context.get("subjects") or {})
    result: dict[str, Any] = {
        "axonpush.workspace_id": context["workspace_id"],
        "deployment.environment.name": context["environment"],
    }
    if subjects:
        result["telemetry.subjects"] = subjects
    if subjects.get("user"):
        result["user.id"] = subjects["user"]
    if context.get("request_id"):
        result["axonpush.request_id"] = context["request_id"]
    if context.get("session_id"):
        result["session.id"] = context["session_id"]
    return result


def merge_subjects(
    explicit: Mapping[str, str] | None, defaults: Mapping[str, str] | None
) -> dict[str, str]:
    if explicit is not None and not isinstance(explicit, Mapping):
        raise ValueError("Invalid subject map")
    result = dict(defaults or {})
    for kind, id in (explicit or {}).items():
        if (
            not isinstance(kind, str)
            or not kind.strip()
            or not isinstance(id, str)
            or not id.strip()
        ):
            raise ValueError("Invalid subject map")
        if kind in result and result[kind] != id:
            raise ValueError(f"Conflicting subject: {kind}")
        result[kind] = id
    return result


def capture_event(owner: object, params: dict[str, Any]) -> dict[str, Any]:
    c = current_context(owner)
    if c is None:
        return params
    if params.get("environment") and params["environment"] != c["environment"]:
        raise ValueError("Request environment mismatch")
    payload = params.get("payload") or {}
    for bag in (params.get("metadata") or {}, payload, payload.get("attributes") or {}):
        if not isinstance(bag, Mapping):
            continue
        merge_subjects(bag.get("telemetry.subjects"), c.get("subjects"))
        for key in ("user.id", "enduser.id", "userId"):
            if (
                key in bag
                and c.get("subjects", {}).get("user")
                and bag[key] != c["subjects"]["user"]
            ):
                raise ValueError("Conflicting user identity")
        if "axonpush.workspace_id" in bag and bag["axonpush.workspace_id"] != c["workspace_id"]:
            raise ValueError("Request workspace mismatch")
    explicit = dict(params.get("metadata") or {})
    subjects = merge_subjects(explicit.get("telemetry.subjects"), c.get("subjects"))
    if explicit.get("user.id") and subjects.get("user") and explicit["user.id"] != subjects["user"]:
        raise ValueError("Conflicting user identity")
    metadata = {**attributes(c), **explicit, "telemetry.subjects": subjects}
    return {
        **params,
        "trace_id": params.get("trace_id") or c.get("trace_id"),
        "environment": c["environment"],
        "metadata": deepcopy(metadata),
    }


def observation(owner: object, workspace_id: str, params: Mapping[str, Any]) -> dict[str, Any]:
    c = current_context(owner)
    if c is None:
        return dict(params)
    if workspace_id != c["workspace_id"] or (
        params.get("environment") and params["environment"] != c["environment"]
    ):
        raise ValueError("Request workspace/environment mismatch")
    mapped = dict(params)
    bindings = c.get("bindings", {}).get(params["event"], {})
    for category in ("refs", "attributes"):
        explicit = dict(params.get(category) or {})
        for field, kind in bindings.get(category, {}).items():
            id = c.get("subjects", {}).get(kind)
            if id is None:
                continue
            if field in explicit and explicit[field] != id:
                raise ValueError(f"Conflicting subject binding: {field}")
            explicit[field] = id
        mapped[category] = explicit
    mapped["environment"] = c["environment"]
    return mapped


class RequestScope:
    """Use with sync or async clients; scoped operations retain their normal await behavior."""

    def __init__(
        self,
        owner: Any,
        *,
        workspace_id: str,
        environment: str,
        subjects: Mapping[str, str] | None = None,
        request_id: str | None = None,
        trace_id: str | None = None,
        session_id: str | None = None,
        bindings: Mapping[str, Any] | None = None,
    ):
        if not workspace_id.strip() or not environment.strip():
            raise ValueError("Request context requires workspace_id and environment")
        if len(subjects or {}) > 32:
            raise ValueError("At most 32 subjects are supported")
        for kind, id in (subjects or {}).items():
            if (
                not kind.strip()
                or len(kind) > 80
                or not isinstance(id, str)
                or not id.strip()
                or len(id) > 200
            ):
                raise ValueError("Subjects require nonempty entity types and opaque IDs")
        self._owner = owner
        self._context = deepcopy(
            dict(
                workspace_id=workspace_id,
                environment=environment,
                subjects=dict(subjects or {}),
                request_id=request_id,
                trace_id=trace_id,
                session_id=session_id,
                bindings=dict(bindings or {}),
            )
        )
        self.workflows = SimpleNamespace(facts=self.facts)
        self.events = SimpleNamespace(publish=self.publish_event)
        self._token: Any = None

    def __enter__(self) -> RequestScope:
        if self._token is not None:
            raise RuntimeError("Create a fresh scope for each invocation")
        trace = (
            TraceContext(self._context.get("trace_id"))
            if self._context.get("trace_id")
            else (current_trace() or TraceContext())
        )
        self._trace_token = set_current_trace(trace)
        self._context["trace_id"] = trace.w3c_trace_id()
        self._token = _current.set({**_current.get(), self._owner: self._context})
        return self

    def __exit__(self, *args: Any) -> None:
        _current.reset(self._token)
        _clear_current_trace(self._trace_token)
        self._token = None

    async def __aenter__(self) -> RequestScope:
        return self.__enter__()

    async def __aexit__(self, *args: Any) -> None:
        self.__exit__(*args)

    def capture(self) -> dict[str, Any]:
        return deepcopy(self._context)

    def _require_active(self) -> None:
        if current_context(self._owner) is not self._context:
            raise RuntimeError(
                "Use scoped operations inside their with_context block; capture and restore context for jobs"
            )

    def publish_event(self, *args: Any, **kwargs: Any) -> Any:
        self._require_active()
        return self._owner.events.publish(*args, **kwargs)

    def observe(self, event: str, **kwargs: Any) -> Any:
        self._require_active()
        return self._owner.observe(self._context["workspace_id"], event, **kwargs)

    def facts(self, workflow: str, input: Mapping[str, Any]) -> Any:
        self._require_active()
        body = deepcopy(dict(input))
        for fact in body.get("facts", []):
            if self._context.get("trace_id"):
                fact.setdefault("trace_id", self._context["trace_id"])
        body["subjects"] = merge_subjects(body.get("subjects"), self._context.get("subjects"))
        return self._owner.workflows.facts(
            self._context["workspace_id"],
            FactsInputBody.from_dict({"workflow": workflow, "input": body}),
            {"environment": self._context["environment"]},
        )

    def annotate_span(self, span: Any) -> None:
        import json

        for key, value in attributes(self._context).items():
            span.set_attribute(key, json.dumps(value) if isinstance(value, dict) else value)
