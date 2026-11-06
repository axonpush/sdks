# Evidence format v1

This MIT-licensed specification describes passive SDK evidence and sealed archive
parts. The server OpenAPI contract remains authoritative for HTTP operations.

- `event.schema.json`: TypeScript publish-envelope names. Python/.NET helpers
  serialize the same identifiers and payload fields. Additional transport fields
  remain permitted. `sdk_reported` actors are customer assertions.
- `manifest.schema.json`: immutable segment commitment. Validation also requires
  canonical JSON, an exact UTC hour, distinct immutable object versions, retention
  after sealing, and the independently pinned seal described in `storage-format.md`.
- `storage-format.md`: canonicalization, encryption, RFC 6962 proof and RFC 3161
  checkpoint verification, limits and trust boundaries.

Identifiers are `agent.task.start`, `agent.task.end`, `oversight.decision`,
`policy.denied`, and `notice.shown`. Management changes, suspension and resume are
server-recorded events; clients cannot turn an asserted human actor into an
authenticated dashboard approval by setting metadata.

Use `axonpush verify-evidence --manifest manifest.json --meta meta.parquet
--content content.parquet --expected-seal <independent-checkpoint>`. Optional
`--proof-ordinal` emits a proof. For packs use `axonpush verify-pack --json
pack.json --pdf pack.pdf --expected-key <separately-trusted-issuer-key>`.
A document and the hash/key it contains cannot authenticate themselves. Neither
a valid signature nor observed evidence certifies legal compliance or complete
capture. Capture policies may deliberately omit goals, reasons and other content.

The production dashboard also verifies downloaded proofs locally in the browser.
Format changes requiring different hash preimages or cryptographic interpretation
require a new schema version; do not silently redefine v1.
