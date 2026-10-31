"""13 — Print capture.

Some agent frameworks emit free-form output via ``print()`` rather than
through a structured logger. ``setup_print_capture()`` patches
``sys.stdout`` / ``sys.stderr`` with a tee that (a) still writes to the
original console and (b) forwards each completed line to AxonPush as an
``agent.log`` event.

Run::

    uv run examples/13_print_capture.py
"""

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402
from axonpush.integrations.print_capture import setup_print_capture  # noqa: E402


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        # Print the header BEFORE patching so it doesn't get captured.
        print(f"channel={channel_id}\n")

        handle = setup_print_capture(
            client,
            channel_id,
            agent_id="demo-agent",
            service_name="my-agent",
        )
        try:
            print("agent starting up")
            print("step 1: loaded tools = ['web_search', 'calculator']")
            print("step 2: calling model")
            print("step 3: parsing response")
            print("agent done")
            handle.flush(timeout=5.0)
        finally:
            handle.unpatch()

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None:
            print(f"\nEvents captured ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name} (event_id={ev.event_id})")
            # Payload reads are separate and audited: client.telemetry.content(event_id)
            # requires content:read; search returns metadata only.


if __name__ == "__main__":
    main()
