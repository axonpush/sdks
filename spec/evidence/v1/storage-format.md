# Evidence storage format v1

This versioned format is implemented by the archive codec, transactional writer,
external subject-key authority and ledger APIs. Enable archives through the
retention API after configuring a compatible locked archive, separate unversioned
key authority, private master key and trusted RFC 3161 authority. Never bypass
activation checks by editing `org_retention.enabled` directly.

## Immutable bytes

An hour can have multiple bounded parts. Each database commit covers at most 500
events, keeping the transaction below DSQL's write-set limits. The codec accepts
at most 5,000 rows and 32 MiB of unencrypted data per part; an individual record
is at most 8 MiB. The source query also bounds estimated decoded bytes to 16 MiB,
including a conservative allowance for serialization copies; a single large row
is admitted for explicit validation. Hydration stops at a 32 MiB prefix, whose
membership alone is committed. Remaining records continue in another part.
No event is eligible
for expiry merely because a different event from its hour was sealed.

Each attempt writes `meta.parquet`, `content.parquet` and `manifest.json` to a
fresh random prefix. Parquet compression uses zstd. Customer fields, including
event IDs, user IDs, names, attributes and other metadata, live inside AES-256-GCM
records. The clear metadata contains only pinned region, ordinal, server ingest
timestamp, opaque key reference and ciphertext digest. AAD binds tenant, region, schema, hour,
ordinal, timestamp and key reference. Every encryption uses a fresh nonce.

When archive content capture is disabled, the record excludes inline payloads,
compressed payloads and spilled payload bodies. The normal ingest capture and
redaction policy still applies before a record reaches the archive writer.

For a metadata row `m` and encrypted body `c`, the Merkle leaf is
`SHA256(0x00 || JCS(m) || SHA256(c))`. Internal nodes follow RFC 6962:
`SHA256(0x01 || left || right)`. JCS uses the RFC 8785 library; trees and proofs
use transparency-dev's implementation. Ordinals follow ingest time then event
ID. They are local to the part. No decryption keys are required to verify them.

The manifest binds tenant, pinned region, part root, count, period, sequence, predecessor hash,
exact object keys and version IDs, file checksums and lengths, lock mode,
retention date and seal time. `sealHash` is omitted from its own preimage by
replacing it with an empty string. The seal hash is
`SHA256("axonpush:evidence:seal:v1\0" || JCS(manifest-with-empty-sealHash))`.

The S3 adapter validates bucket region, enabled versioning and Object Lock. Each
write uses `If-None-Match: *`, a SHA-256 transport checksum and explicit object
retention. It checks the returned version's actual retention, downloads all
three objects, and verifies the complete bundle before producing a candidate.
The archive writer has no delete or governance-bypass permission.

## Local object-storage tests

`bash scripts/test-objectstorage.sh` starts a disposable RustFS 1.0.4 container
with loopback networking, synthetic credentials and temporary in-memory volumes.
It supports Podman or Docker (`CONTAINER_CLI=docker` selects Docker). The script
stops its own container on exit; it never uses an existing bucket or production
AWS credentials. `RUSTFS_TEST_IMAGE` can select a newer candidate for testing.

The integration test exercises actual version-pinned uploads/downloads,
conditional creation, governance and compliance retention, legal holds,
permanent key replacement with ETag checks, and Merkle verification after key
erasure. The direct test requires an explicit loopback `RUSTFS_TEST_ENDPOINT`
and dedicated `RUSTFS_TEST_ACCESS_KEY`/`RUSTFS_TEST_SECRET_KEY`.

RustFS omits the region header on `HeadBucket`. Both storage adapters therefore
fall back to `GetBucketLocation` and compare its result with the configured
region; they never assume that a reachable bucket has the right region. These
tests establish the listed local S3 behaviors, not AWS IAM, KMS or billing
behavior. RustFS is a local testing dependency, not a production storage change.

## Commit and deletion

One transaction validates current policy and each selected row's privacy
revision, advances the tenant head, inserts the seal and segment, writes the
entire membership batch and wakes retention. The tenant guard serializes this
with erasure and organization deletion. Unrelated new ingest does not invalidate
an already uploaded, closed-hour batch. Privacy edits increment
`events.archive_revision`; future privacy mutation paths must do the same.

If object I/O or validation fails, no membership is published. An interrupted
attempt may leave encrypted, locked orphan objects until their retention expires.
Retries use a fresh prefix. A database commit retry for the same candidate is
idempotent. Enabled tenants' hot expiry requires that event's membership, segment
and seal; an unsealed backlog does not arm an idle polling deadline. Newly
committed membership wakes expiry again.

PostgreSQL contains no subject decryption keys. The implemented `keyvault`
authority stores wrapped random subject keys in a separate, private, unversioned
S3 bucket. Opaque HMAC references hide identifiers. HKDF derives a record's key
from every declared subject key, plus an organization key. An environment-scoped
erase removes its exact key; an app-wide erase removes a key shared by that
subject's environments. Subject-less records additionally use a per-day key.
Destroying the organization key prevents all record decryption for that tenant.

Each erasure permanently replaces a single key object with a tombstone using
its ETag and `If-Match`. Creation uses `If-None-Match`, so neither a concurrent
writer nor a retry can recreate a destroyed key. The authority rejects enabled
or suspended versioning, checks the current state on every resolve, batches
shared subjects, clears transient key buffers and never caches plaintext keys
across requests. A restored PostgreSQL backup contains only the recipe reference;
it cannot reconstruct a destroyed random subject key using the master alone.

The key bucket is deliberately excluded from ordinary backup/rollback workflows.
Customer-created copies of key material remain recoverable by that customer.
Restoring hot PostgreSQL content requires revocation reconciliation before
serving traffic. The runtime checks the external generation even when the restored
backup has no retention-policy row. A mismatch blocks ordinary reads/writes and
protected deliveries while bounded durable work scrubs revoked rows/projections.
Status and job recovery remain available. Replayed ingestion is checked again:
revoked entries are discarded independently within mixed batches. An organization
key tombstone is permanent; SQL restore cannot resurrect that organization. Keys can only cover subjects declared in telemetry;
undeclared personal references cannot be found by an identifier erasure request.

## Independent verification

Build `go build ./cmd/evidence-verify`, or use a newly built portable executable:

```sh
axonpush verify-evidence \
  --manifest manifest.json --meta meta.parquet --content content.parquet \
  --expected-seal "$CHECKPOINT_SEAL" --proof-ordinal 0
```

The command makes no network/database calls and needs no decryption key. The
expected seal must come from an independently retained checkpoint. A manifest
and its own hash only detect corruption; they do not establish operator honesty.

The RFC 3161 adapter timestamps `SHA256(raw-32-byte-seal-hash)`. It uses a random
nonce, requests the signer certificate, refuses redirects and plaintext HTTP,
and validates the response imprint, nonce, time, CMS signature and certificate
chain against explicit trust roots. The signer must have the dedicated critical
timestamp EKU. Saved responses can also be verified offline with
`--tsa-response`, `--tsa-roots` and `--tsa-nonce`. This establishes trust under the
configured PKI, without claiming qualified/eIDAS status or online revocation
validation. Daily checkpoints are scheduled from committed archive work, with no recurring
empty-tenant scan. Storage or TSA failures remain explicit job failures; they do
not produce a successful independent anchor.

## Infrastructure and costs

The CDK adds a retained, private Object Lock bucket with versioning, TLS and
AWS-managed KMS SSE, plus the separate unversioned key bucket. Client encryption is independent of SSE; a configured
customer KMS key can also be supplied to the S3 adapter. The template creates no
new scheduled polling, provisioned compute, inventory job or customer-managed
KMS key. Two retained Secrets Manager seeds separately protect key authority and
pack signing; these have a provider storage charge even when compute is idle. There has been no deployment or live AWS cost measurement.

Objects carry a 30/180/365/2555-day retention tag. Expiration never bypasses an
active Object Lock or legal hold. Only parts over 128 KiB in longer tiers
transition to Standard-IA at day 30 and Glacier Instant Retrieval at day 90;
only the seven-year tier reaches Deep Archive at day 365. This avoids small-file
transition overhead and unnecessary minimum-duration charges for short tiers.
Deep Archive retrieval uses the explicit segment restore job before synchronous
verification can read those objects. Retention and legal holds never grant a
restore or verify worker permission to delete locked archive versions.

These choices follow [S3 Object Lock lifecycle semantics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html)
and [S3 transition constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html).

The timestamp dependency requires Go 1.27; builds now pin Go 1.27.3 and
golangci-lint 2.15.0 rather than weakening parser/security dependencies.
