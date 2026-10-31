# Caller operation discovery

`GET /capabilities` remains deployment metadata: feature flags, license state and the scope catalogue. `GET /capabilities/operations` returns decisions for the authenticated caller. It is not a replacement for authorization on each request.

The discovery response contains `registryRevision` and `operations`. Each entry has an `operationId`, `availability` (`allowed`, `denied` or `conditional`), and an optional machine-readable reason. `conditional` means the particular resource still needs authorization. A missing entry or failed discovery is `unknown`, never an access grant.

The SDKs do not cache caller discovery. Fetch a new snapshot after changing identity, organization, permissions or grants. `registryRevision` identifies the operation catalogue, not a user's permission version. A previous `allowed` result cannot guarantee a later call: permissions may have changed, or resource checks may reject it.

```ts
import { operationAvailability } from "@axonpush/sdk";
const snapshot = await client.capabilities.operations();
const availability = operationAvailability(snapshot, "alerts.list");
```

```python
from axonpush import operation_availability
snapshot = client.capabilities.operations()
availability = operation_availability(snapshot, "alerts.list")
# Async clients expose await client.capabilities.operations().
```

```csharp
using AxonPush.Operations;
var snapshot = await client.Capabilities.OperationsAsync();
var availability = snapshot.GetAvailability("alerts.list");
```

Normal SDK error behavior is preserved. A configured fail-open transport may return `null`/`None`; the helper maps that to `unknown`. Authentication errors still follow the transport's existing error policy. Applications that catch errors must discard the previous snapshot instead of reusing a cached permission decision.

Generated SDK methods remain stable across callers. Discovery does not remove methods from a client or grant access locally. The server remains authoritative for scope, membership, bindings and resource access.
