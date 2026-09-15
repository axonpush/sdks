import uuid

import pytest

from axonpush.exceptions import NotFoundError
from axonpush.models import Channel

pytestmark = pytest.mark.e2e


class TestChannels:
    def test_create_channel(self, client, backend):
        name = f"test-ch-{uuid.uuid4().hex[:8]}"
        ch = client.channels.create(backend.app_id, name)
        assert isinstance(ch, Channel)
        assert ch.name == name
        assert ch.channel_id is not None
        client.channels.delete(backend.app_id, ch.channel_id)

    def test_get_channel(self, client, channel, backend):
        fetched = client.channels.get(backend.app_id, channel.channel_id)
        assert fetched.channel_id == channel.channel_id
        assert fetched.name == channel.name

    def test_delete_channel(self, client, backend):
        name = f"test-ch-{uuid.uuid4().hex[:8]}"
        ch = client.channels.create(backend.app_id, name)
        client.channels.delete(backend.app_id, ch.channel_id)
        with pytest.raises((NotFoundError, Exception)):
            client.channels.get(backend.app_id, ch.channel_id)
