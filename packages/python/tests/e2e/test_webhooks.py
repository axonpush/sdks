import pytest

from axonpush._internal.api.models import CreateEndpointOutputBody
from axonpush.models import WebhookEndpoint

pytestmark = pytest.mark.e2e


class TestWebhooks:
    def test_create_endpoint(self, client, channel):
        endpoint = client.webhooks.create_endpoint(
            url="http://127.0.0.1:1/webhook",
            channel_id=channel.channel_id,
            event_types=["agent.tool_call.start"],
            description="test endpoint",
        )
        assert isinstance(endpoint, CreateEndpointOutputBody)
        assert endpoint.url == "http://127.0.0.1:1/webhook"
        assert endpoint.channel_id == channel.channel_id
        client.webhooks.delete_endpoint(endpoint.endpoint_id)

    def test_list_endpoints(self, client, channel):
        ep = client.webhooks.create_endpoint(
            url="http://127.0.0.1:1/hook-list",
            channel_id=channel.channel_id,
        )
        endpoints = client.webhooks.list_endpoints(channel.channel_id)
        assert isinstance(endpoints, list)
        assert all(isinstance(e, WebhookEndpoint) for e in endpoints)
        ids = [e.endpoint_id for e in endpoints]
        assert ep.endpoint_id in ids
        client.webhooks.delete_endpoint(ep.endpoint_id)

    def test_deliveries(self, client, channel):
        ep = client.webhooks.create_endpoint(
            url="http://127.0.0.1:1/hook-deliveries",
            channel_id=channel.channel_id,
        )
        deliveries = client.webhooks.deliveries(ep.endpoint_id)
        assert isinstance(deliveries, list)
        client.webhooks.delete_endpoint(ep.endpoint_id)

    def test_delete_endpoint(self, client, channel):
        ep = client.webhooks.create_endpoint(
            url="http://127.0.0.1:1/hook-delete",
            channel_id=channel.channel_id,
        )
        client.webhooks.delete_endpoint(ep.endpoint_id)
        endpoints = client.webhooks.list_endpoints(channel.channel_id)
        removed = [e for e in endpoints if e.endpoint_id == ep.endpoint_id]
        assert len(removed) == 1
        assert removed[0].active is False
