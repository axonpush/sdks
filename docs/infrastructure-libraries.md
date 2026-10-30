# SDK infrastructure libraries

Package versions are unchanged; this work does not publish any SDK.

TypeScript uses p-retry 7 and p-queue 9, preserving Node 20+ support. Python uses
Tenacity 9; .NET uses Polly 8. maxRetries still means additional attempts. Delays
include jitter with a 250ms base and 4s cap. Retry-After is respected within the
invocation budget. Event publishing generates a UUID once before retries when
no dedup key was supplied. Automatic retries are restricted to GET/HEAD reads and event/observation writes with stable identities; other mutations run once. Libraries cannot make other mutations idempotent.

The configured timeout covers an invocation including retries and response body.
TypeScript and async Python cancel at the total deadline. .NET passes a linked
deadline token through Polly and HttpClient, including injected clients. Sync
Python uses remaining-budget HTTPX timeouts and checks the absolute deadline
while reading response chunks. Cancellation is cooperative: a socket read may
return at its inactivity timeout before the next deadline checkpoint. No orphan
helper thread is created. Caller cancellation is never converted into fail-open.

Retry counts must be nonnegative integers; timeouts must be finite and
positive. TypeScript validates with Zod; Python uses existing Pydantic. Transport
calls copy rather than mutate caller argument objects.

TypeScript synchronous submit with overflowPolicy="block" is deprecated and now
drops newest when full. submitAsync(params,{signal}) resolves true when admitted,
false when closed or waiting capacity is full, and rejects caller cancellation
while awaiting admission. Queue and waiter capacities each equal queueSize;
in-flight capacity is concurrency. Close drains within its budget, cancels active
work and counts abandoned records. Sync Python close retains a live worker handle
until its current bounded IO returns; async workers are canceled and awaited.

OTel registrations are scoped to provider identity and share the actual processor.
The final handle's shutdown releases registration, permitting reinitialization.
Conflicting credentials on one provider/endpoint/channel raise an explicit error.

Existing capture-policy paths use 256 Unicode code points for redacted previews,
further bounded by maxContentLength. The suffix is outside that content budget.
Secret-key redaction is independent. Truncating a preview is not a guarantee that
arbitrary secrets embedded inside a string have been removed.
