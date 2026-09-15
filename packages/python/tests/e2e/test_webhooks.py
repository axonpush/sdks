import pytest

from axonpush._internal.api.models import CreateEndpointOutputBody
from axonpush.models import WebhookEndpoint

pytestmark = pytest.mark.e2e


class TestWebhooks:
    def test_create_endpoint(self, client, channel):
        endpoint = client.webhooks.create_endpoint(
            url="https://example.com/webhook",
            channel_id=channel.channel_id,
            event_types=["agent.tool_call.start"],
            description="test endpoint",
        )
        assert isinstance(endpoint, CreateEndpointOutputBody)
        assert endpoint.url == "https://example.com/webhook"
        assert endpoint.channel_id == channel.channel_id
        client.webhooks.delete_endpoint(endpoint.endpoint_id)

    def test_list_endpoints(self, client, channel):
        ep = client.webhooks.create_endpoint(
            url="https://example.com/hook-list",
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
            url="https://example.com/hook-deliveries",
            channel_id=channel.channel_id,
        )
        deliveries = client.webhooks.deliveries(ep.endpoint_id)
        assert isinstance(deliveries, list)
        client.webhooks.delete_endpoint(ep.endpoint_id)

    def test_delete_endpoint(self, client, channel):
        ep = client.webhooks.create_endpoint(
            url="https://example.com/hook-delete",
            channel_id=channel.channel_id,
        )
        client.webhooks.delete_endpoint(ep.endpoint_id)
        endpoints = client.webhooks.list_endpoints(channel.channel_id)
        ids = [e.endpoint_id for e in endpoints]
        assert ep.endpoint_id not in ids
