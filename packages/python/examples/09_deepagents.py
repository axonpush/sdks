"""09 — LangChain Deep Agents integration.

``AxonPushDeepAgentHandler`` traces planning steps, sub-agent delegation,
filesystem ops, LLM calls, and tool calls produced by ``deepagents``.

Run::

    uv sync --extra deepagents
    uv run examples/09_deepagents.py

Set ``OPENAI_API_KEY`` to actually run the agent; otherwise the script
just prints the wiring pattern.
"""

import sys

from config import BASE_URL, ENVIRONMENT, OPENAI_API_KEY, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402

try:
    from axonpush.integrations.deepagents import AxonPushDeepAgentHandler
except ImportError:
    print("Install Deep Agents integration: uv sync --extra deepagents")
    sys.exit(1)


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        handler = AxonPushDeepAgentHandler(
            client,
            channel_id,
            agent_id="deep-agent",
            metadata={"model": "gpt-4o"},
        )
        print(f"Handler ready (channel={channel_id})\n")

        if OPENAI_API_KEY:
            try:
                from deepagents import create_deep_agent

                agent = create_deep_agent(
                    tools=[],
                    system_prompt="You are a helpful assistant. Be concise.",
                )
                print("Running Deep Agent with AxonPush tracing...")
                result = agent.invoke(
                    {"messages": [{"role": "user", "content": "What is 2 + 2?"}]},
                    config={"callbacks": [handler]},
                )
                print(f"Result: {result['messages'][-1].content}\n")
            except Exception as exc:
                print(f"Deep Agent execution error: {exc}\n")
        else:
            print("OPENAI_API_KEY not set — pattern only:")
            print("  agent = create_deep_agent(tools=[...], system_prompt='...')")
            print("  agent.invoke({'messages': [...]}, config={'callbacks': [handler]})\n")

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None and (listing.events or []):
            print(f"Events published ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name}")
        else:
            print("No events published (set OPENAI_API_KEY to run the agent).")


if __name__ == "__main__":
    main()
