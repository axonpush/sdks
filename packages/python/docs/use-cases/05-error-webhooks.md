# Notify operators about lifecycle incidents

`activity.incidents` records stateful operational failures and recoveries. Configure an existing alert rule with `metric: lifecycle_open`, `operator: gte` and `threshold: 1`, an authorized app/environment, and an email or webhook destination. Optional `service: operation | journey | pipeline` restricts the incident entity. Incidents deduplicate while open; alert delivery retains its cooldown.

Inspect the active alert schema before creating a rule:

```python
from axonpush import AxonPush
from axonpush.resources.alerts import CreateAlertRuleInput

with AxonPush() as client:
    rule = client.alerts.create(CreateAlertRuleInput.from_dict({
        "name": "Operational incidents",
        "metric": "lifecycle_open",
        "operator": "gte",
        "threshold": 1,
        "destinationType": "email",
        "destination": "operator@example.test",
        "appId": "authorized-app-id",
        "environmentId": "authorized-environment-id",
        "service": "pipeline",
    }))
```

The example destination and IDs are synthetic placeholders. Create a destination only when authorized. An ordinary authentication challenge, human decision wait or idle agent is not automatically an incident. Rules notify operators and perform no hiring actions.

Event webhooks are a separate channel-level fan-out mechanism: `webhooks.create_endpoint` returns `endpoint_id` and a one-time `raw_secret`; `webhooks.deliveries(endpoint_id)` inspects attempts. Keep the signing secret in a secret store and verify signatures using the [shared fixture](../../../../contract/fixtures/webhook-signature.json). Do not print payloads or raw response bodies in operational logs.

See [export failures](07-production-error-handling.md) and the [shared operations contract](../../../../AGENT_OPERATIONS.md).
