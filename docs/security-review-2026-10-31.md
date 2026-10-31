# SDK security review — 2026-10-31

This review covers SDK-owned HTTP transports, credential redirects, retry safety,
input handling and the resolved dependency graphs. It does not certify arbitrary
host applications or every version allowed by optional dependency ranges.
Package versions remain TypeScript 0.0.12, Python 0.0.19 and .NET 0.0.6.

## Fixed credential redirects

AxonPush sends credentials in custom headers. Standard HTTP redirect handling
can retain these headers even when it removes `Authorization`. Real loopback
servers reproduced TypeScript forwarding credentials through 301, 302, 303, 307
and 308 responses before the fix.

- TypeScript's transport interceptor now forces manual redirect handling, even
  when a low-level request passes `redirect: "follow"`. Redirect responses are
  terminal API errors rather than requests to a second endpoint.
- SDK-owned .NET HTTP clients disable automatic redirects. Python HTTPX clients
  explicitly retain their existing no-redirect default.
- Native Python OTLP export uses a requests session with a zero redirect limit;
  native .NET OTLP export supplies an HTTP client with redirects disabled.
- The official TypeScript OTLP exporter already refuses redirects; a real
  collector regression test now verifies this boundary.

Tests cover synthetic API keys/public tokens and check that redirect destinations
receive no requests. They make no production calls. The .NET constructor taking
an injected `HttpClient` remains caller-owned: its handler must set
`AllowAutoRedirect = false`. The SDK cannot inspect or modify that handler.
Configure canonical API URLs instead of relying on endpoint redirects.

## Retry and parsing review

Existing regression suites exercise total invocation deadlines, cancellation,
per-client credentials, stable publish deduplication, bounded queues, redacted
content and refusal to retry non-idempotent mutations. Those suites passed after
these changes. Generated path serialization and the scoped server guards remain
in place; the SDK does not treat discovery results as authorization.

## Dependency audit results

Audits were run with `bun audit --json`, `pip-audit` against the installed Python
3.13 all-extras environment and separately against the exported locked base
requirements, and `dotnet list packages/dotnet/AxonPush.slnx package --vulnerable
--include-transitive`. These are advisory-database checks, not exploitability
proofs. Duplicate Python advisory records are counted separately by the tool.

- All seven .NET projects: no reported vulnerable packages after updating
  Semantic Kernel to 1.71.0 and its required logging abstraction dependency.
- Python base SDK: no reported vulnerable packages in the locked base graph.
- TypeScript: two remaining optional OpenTelemetry 1.x dependency advisories,
  down from nine affected package names. Mastra/MCP, test tooling and the
  generator's js-yaml dependency were updated. The YAML override stays on major
  version 4 and generated TypeScript output is unchanged.
- Python all extras and development tools: eight advisory records in three
  packages, down from 266 records in 32 packages. Available compatible patches
  were installed, including the HTTP stack, OTel, framework integrations and
  supporting parsers. The remaining packages are described below.

## Remaining compatibility and upstream limitations

1. Optional TypeScript OTel 1.x peers contain the
   [baggage allocation advisory](https://github.com/advisories/GHSA-8988-4f7v-96qf)
   and [Jaeger extraction advisory](https://github.com/advisories/GHSA-45rx-2jwx-cxfr).
   Fixes require OTel 2.8/2.9 or later. OTel 2 removes the `addSpanProcessor` API
   used to attach to an application's existing provider, so silently upgrading
   would break that supported integration. AxonPush does not install an inbound
   propagator or select Jaeger. Hosts using these peers should keep inbound header
   limits and avoid the affected Jaeger propagator. An OTel 2 provider-attachment
   API migration remains separate work.
2. Optional CrewAI dependencies include ChromaDB 1.5.9 and diskcache 5.6.3. The
   audit reports no patched versions for the four ChromaDB advisories
   ([code injection](https://github.com/advisories/GHSA-f4j7-r4q5-qw2c),
   [CVE-2026-45833](https://github.com/advisories/GHSA-36p7-vc44-83pf),
   [CVE-2026-45831](https://github.com/advisories/GHSA-xph7-9rjv-w5fr),
   [CVE-2026-45830](https://github.com/advisories/GHSA-2wm9-hf6c-p5cr)) or
   [diskcache's unsafe deserialization](https://github.com/advisories/GHSA-w8v5-vhqr-4h9v).
   The SDK callback integration does not start a ChromaDB server or read diskcache
   files. Host applications must not expose affected ChromaDB server operations
   to untrusted callers and must keep cache directories trusted. Installing only
   the needed extras avoids pulling in unused framework dependencies.
3. Development-only openapi-python-client 0.28.3 has an
   [untrusted-schema code-generation advisory](https://github.com/advisories/GHSA-5293-mq8x-g3xj).
   The fixed 0.29.1 generator was tested, but emits Python 3.11-only `typing.Self`,
   `StrEnum` and changed datetime parsing, incompatible with this SDK's Python
   3.10 support. The generator is explicitly capped below 0.29. Code generation
   must consume the reviewed, vendored AxonPush contract; do not generate/import
   code from untrusted schemas. This tool is not a runtime package dependency.

The all-extras audit above reflects Python 3.13. Resolver branches for older
supported interpreters can select different third-party versions; this report
is not a claim that every optional dependency combination is vulnerability-free.

## Verification

- TypeScript: full Vitest suite, `tsc --noEmit`, production build, publint,
  Biome, generated-client determinism and operation/resource parity.
- Python: full non-live pytest suite, strict mypy, Ruff checks and formatting.
- .NET: all three test assemblies, including loopback event and OTLP redirect
  tests; dependency audit covers the sample as well.
- Package version, contract digest and generated-facade checks pass.

Live backend end-to-end tests and production penetration tests were not part of
this local SDK review. No credentials or deployment configuration were copied
into these notes.
