// Back-compat shim: the pre-Go `client.tracesV2` accessor. The `/v2/traces`
// surface collapsed to `GET /traces` and `GET /traces/{traceId}`, so this just
// re-exports the current traces resource. Prefer `client.traces`.
// @deprecated Use the `traces` resource via `client.traces`.
export { TracesV2Resource } from "./traces.js";
