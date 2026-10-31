# Local integration tests

These opt-in tests target the current Go API, auth service, and event workers.
Start the complete local stack from `axonpush/server` using its local development
instructions. The SDK test suite does not start servers or seed database tables.

Use a disposable local organization and an unbound API key with the management,
publish, observation, and `content:read` scopes exercised by the tests. Supply credentials in
your shell or secret manager, then run from `packages/python`:

```sh
export AXONPUSH_BASE_URL=http://localhost:3000  # replace with your local API port
# AXONPUSH_API_KEY, AXONPUSH_TENANT_ID, and AXONPUSH_ENVIRONMENT must also be set.
uv sync --extra dev --extra all
uv run pytest -m e2e tests/e2e
```

The URL must resolve by spelling to `localhost` or a loopback IP. Remote targets
and URL userinfo are rejected before authenticated traffic. The fixture creates
a unique app for the run and separate channels per test; teardown deletes only
these resources. Select an existing disposable local environment by its slug;
environment administration requires a browser session, so the API-key test
fixture does not create or change environments. It does not change org selection,
users, grants, API keys, or existing application resources. Webhook CRUD tests use an unreachable
loopback destination and do not test external delivery.

Normal `pytest` and CI exclude this suite. Unit and example smoke tests use mocked
HTTP and do not require credentials. Native OTLP and event-plane compatibility
exporters remain separate supported paths.
