# SemanticKernelChat

A console chat REPL that runs Microsoft Semantic Kernel against Azure OpenAI (or vanilla OpenAI), with one inline kernel function (`GetTime`), and forwards every Semantic Kernel `Activity` to AxonPush via the OpenTelemetry exporter in this repo.

## Prerequisites

- .NET 8 SDK or later.
- An AxonPush API key, tenant id, and channel id.
- Either an Azure OpenAI deployment or an OpenAI API key.

## Run

Set the required environment variables, then run from the repository root:

```bash
dotnet run --project samples/SemanticKernelChat
```

Type prompts at the `>` cursor. An empty line exits.

## Environment variables

| Variable | Required | Notes |
| --- | --- | --- |
| `AXONPUSH_API_KEY` | yes | AxonPush API key. |
| `AXONPUSH_TENANT_ID` | yes | AxonPush tenant id. |
| `AXONPUSH_CHANNEL_ID` | yes | Channel that should receive the spans. |
| `AXONPUSH_ENVIRONMENT` | no | Defaults to `development`. |
| `AZURE_OPENAI_ENDPOINT` | yes (Azure path) | e.g. `https://my-resource.openai.azure.com/`. |
| `AZURE_OPENAI_API_KEY` | yes (Azure path) | Azure OpenAI key. |
| `AZURE_OPENAI_DEPLOYMENT` | no | Defaults to `gpt-4o-mini`. |
| `OPENAI_API_KEY` | yes (OpenAI path) | OpenAI key. |
| `OPENAI_MODEL` | no | Defaults to `gpt-4o-mini`. |

The sample defaults to Azure OpenAI. To use vanilla OpenAI instead, pass `--Backend OpenAI` on the command line or set `Backend=OpenAI` in your environment.

## What you should see in AxonPush

Within a few seconds of each prompt, the channel you configured will receive `app.span` events with names like:

- `chat.completions <deployment>` from the SK Azure OpenAI connector.
- `Kernel.InvokeAsync` from the kernel function dispatcher.
- `GetTime` from the inline kernel function.

Each span carries the `gen_ai.*` semantic-convention attributes (model, token usage, finish reason). Enable sensitive-data export by setting `enableSensitiveData: true` on `AddAxonPushTelemetry` if you also want the raw prompts and completions as span events.

## Fail-open behaviour

If AxonPush is unreachable, the sample keeps responding to prompts and logs an `AxonPush publish failed` warning to the console. Set `AXONPUSH_FAIL_OPEN=false` to make publish errors throw.
