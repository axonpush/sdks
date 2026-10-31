"""Bounded reads of synthetic event content through the audited public API."""

from tenacity import retry, retry_if_result, stop_after_delay, wait_fixed


def _not_projected(events):
    return not events


@retry(stop=stop_after_delay(10), wait=wait_fixed(0.1), retry=retry_if_result(_not_projected))
def read_events(client, channel_id):
    page = client.events.search(channel_id=channel_id, limit=50)
    assert page is not None
    assert all(event.content_state == "not_loaded" for event in (page.events or []))
    return (
        [client.telemetry.content(event.event_id) for event in (page.events or [])] if page else []
    )


@retry(stop=stop_after_delay(10), wait=wait_fixed(0.1), retry=retry_if_result(_not_projected))
async def read_events_async(client, channel_id):
    page = await client.events.search(channel_id=channel_id, limit=50)
    assert page is not None
    assert all(event.content_state == "not_loaded" for event in (page.events or []))
    return (
        [await client.telemetry.content(event.event_id) for event in (page.events or [])]
        if page
        else []
    )
