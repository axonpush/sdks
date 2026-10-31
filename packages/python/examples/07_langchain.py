"""07 — LangChain integration.

``AxonPushCallbackHandler`` is a LangChain ``BaseCallbackHandler`` that
publishes one AxonPush event per chain / LLM / tool callback. The shape
follows OpenTelemetry conventions, so it lines up with anything else you
ship to an OTel-compatible backend.

Run::

    uv sync --extra langchain
    uv run examples/07_langchain.py

Set ``OPENAI_API_KEY`` to actually exercise the chain; without it the
script just prints the wiring pattern.
"""

import sys

from config import BASE_URL, ENVIRONMENT, OPENAI_API_KEY, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402

try:
    from axonpush.integrations.langchain import AxonPushCallbackHandler
except ImportError:
    print("Install LangChain integration: uv sync --extra langchain")
    sys.exit(1)


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        handler = AxonPushCallbackHandler(
            client,
            channel_id,
            agent_id="langchain-agent",
            metadata={"model": "gpt-4o-mini"},
        )
        print(f"Handler ready (channel={channel_id}, agent=langchain-agent)\n")

        if OPENAI_API_KEY:
            try:
                from langchain_core.prompts import ChatPromptTemplate
                from importlib import import_module

                ChatOpenAI = import_module("langchain_openai").ChatOpenAI

                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
                prompt = ChatPromptTemplate.from_messages(
                    [
                        ("system", "You are a helpful assistant. Be concise."),
                        ("human", "{question}"),
                    ]
                )
                chain = prompt | llm

                print("Invoking chain with AxonPush tracing...")
                result = chain.invoke(
                    {"question": "What is life in one sentence?"},
                    config={"callbacks": [handler]},
                )
                print(f"Result: {result.content}\n")
            except Exception as exc:
                print(f"LangChain execution error: {exc}\n")
        else:
            print("OPENAI_API_KEY not set — pattern only:")
            print("  chain.invoke(input, config={'callbacks': [handler]})\n")

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None and (listing.events or []):
            print(f"Events published ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name}")
        else:
            print("No events published (set OPENAI_API_KEY to run the chain).")


if __name__ == "__main__":
    main()
