"""Disposable example resources, using the current app-scoped channel API.

An existing AXONPUSH_CHANNEL_ID is reused without creating or deleting resources.
Otherwise contextlib cleans up only resources created by this example, including
when the example raises. Set AXONPUSH_APP_ID to create a channel in an existing app.
"""

from collections.abc import AsyncIterator, Iterator
from contextlib import AsyncExitStack, ExitStack, asynccontextmanager, contextmanager

from axonpush import AsyncAxonPush, AxonPush
from config import APP_ID, CHANNEL_ID


@contextmanager
def example_channel(client: AxonPush) -> Iterator[str]:
    if CHANNEL_ID:
        yield CHANNEL_ID
        return
    with ExitStack() as cleanup:
        app_id = APP_ID
        if not app_id:
            app = client.apps.create(name="sdk-example")
            if app is None:
                raise RuntimeError("Could not create the example app")
            app_id = app.app_id
            cleanup.callback(client.apps.delete, app_id)
        channel = client.channels.create(app_id=app_id, name="sdk-example")
        if channel is None:
            raise RuntimeError("Could not create the example channel")
        cleanup.callback(client.channels.delete, app_id, channel.channel_id)
        yield channel.channel_id


@asynccontextmanager
async def async_example_channel(client: AsyncAxonPush) -> AsyncIterator[str]:
    if CHANNEL_ID:
        yield CHANNEL_ID
        return
    async with AsyncExitStack() as cleanup:
        app_id = APP_ID
        if not app_id:
            app = await client.apps.create(name="sdk-example")
            if app is None:
                raise RuntimeError("Could not create the example app")
            app_id = app.app_id
            cleanup.push_async_callback(client.apps.delete, app_id)
        channel = await client.channels.create(app_id=app_id, name="sdk-example")
        if channel is None:
            raise RuntimeError("Could not create the example channel")
        cleanup.push_async_callback(client.channels.delete, app_id, channel.channel_id)
        yield channel.channel_id
