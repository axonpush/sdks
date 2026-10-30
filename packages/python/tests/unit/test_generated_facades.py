"""Compatibility facades stay aligned with the installed OpenAPI generator output."""

from __future__ import annotations

import ast
import importlib
import inspect
import textwrap

import pytest

from axonpush.resources.analytics import Analytics, AsyncAnalytics

RESOURCES = (
    "alerts",
    "analytics",
    "apps",
    "capabilities",
    "channels",
    "environments",
    "errors",
    "organizations",
    "traces",
    "webhooks",
)


@pytest.mark.parametrize("resource", RESOURCES)
def test_generated_facades_expose_all_operation_parameters(resource):
    module = importlib.import_module(f"axonpush.resources.{resource}")
    classes = [
        c
        for _, c in inspect.getmembers(module, inspect.isclass)
        if c.__module__ == module.__name__ and not c.__name__.startswith("Async")
    ]
    for cls in classes:
        sibling = getattr(module, "Async" + cls.__name__)
        for name, method in inspect.getmembers(cls, inspect.isfunction):
            if name.startswith("_"):
                continue
            assert inspect.signature(method) == inspect.signature(getattr(sibling, name))
            tree = ast.parse(textwrap.dedent(inspect.getsource(method)))
            calls = [
                node
                for node in ast.walk(tree)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "_invoke"
            ]
            for call in calls:
                operation = getattr(module, call.args[0].id)
                expected = set(inspect.signature(operation._get_kwargs).parameters) - {
                    "client",
                    "body",
                }
                assert expected <= set(inspect.signature(method).parameters), (
                    resource,
                    name,
                    expected,
                )


class SerializeClient:
    def _invoke(self, operation, /, **kwargs):
        kwargs.pop("_coerce", None)
        return operation._get_kwargs(**kwargs)


class AsyncSerializeClient:
    async def _invoke(self, operation, /, **kwargs):
        return SerializeClient()._invoke(operation, **kwargs)


def test_analytics_filters_and_string_enums_serialize_to_wire_names():
    result = Analytics(SerializeClient()).breakdown(
        dimension="tag",
        tag_key="tier",
        model="synthetic",
        filter_tag_key="region",
        filter_tag_value="eu",
    )
    assert result["params"] == {
        "dimension": "tag",
        "tagKey": "tier",
        "model": "synthetic",
        "filterTagKey": "region",
        "filterTagValue": "eu",
    }
    with pytest.raises(ValueError):
        Analytics(SerializeClient()).breakdown(dimension="invalid-enum")


@pytest.mark.asyncio
async def test_async_analytics_filters_use_same_generated_serializer():
    result = await AsyncAnalytics(AsyncSerializeClient()).timeseries(
        bucket="hour", model="synthetic", filter_tag_key="tier", filter_tag_value="paid"
    )
    assert result["params"] == {
        "bucket": "hour",
        "model": "synthetic",
        "filterTagKey": "tier",
        "filterTagValue": "paid",
    }
