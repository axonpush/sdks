using System.ComponentModel;
using System.Globalization;
using AxonPush;
using AxonPush.SemanticKernel;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using OpenTelemetry.Trace;

#pragma warning disable SKEXP0001

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration.AddEnvironmentVariables();
builder.Configuration.AddUserSecrets<Program>(optional: true);
builder.Configuration.AddCommandLine(args);

var backend = (builder.Configuration["Backend"] ?? "AzureOpenAI").Trim();
var axonPushApiKey = Required(builder.Configuration, "AXONPUSH_API_KEY");
var axonPushTenantId = Required(builder.Configuration, "AXONPUSH_TENANT_ID");
var axonPushChannelId = Required(builder.Configuration, "AXONPUSH_CHANNEL_ID");
var axonPushEnvironment = builder.Configuration["AXONPUSH_ENVIRONMENT"]
    ?? builder.Configuration["AxonPush:Environment"]
    ?? "development";

var kernelBuilder = builder.Services.AddKernel();

if (backend.Equals("OpenAI", StringComparison.OrdinalIgnoreCase))
{
    var apiKey = Required(builder.Configuration, "OPENAI_API_KEY");
    var model = builder.Configuration["OPENAI_MODEL"]
        ?? builder.Configuration["OpenAI:Model"]
        ?? "gpt-4o-mini";
    kernelBuilder.AddOpenAIChatCompletion(model, apiKey);
    Console.WriteLine($"[SemanticKernelChat] Using OpenAI model '{model}'.");
}
else
{
    var endpoint = Required(builder.Configuration, "AZURE_OPENAI_ENDPOINT");
    var apiKey = Required(builder.Configuration, "AZURE_OPENAI_API_KEY");
    var deployment = builder.Configuration["AZURE_OPENAI_DEPLOYMENT"]
        ?? builder.Configuration["AzureOpenAI:Deployment"]
        ?? "gpt-4o-mini";
    kernelBuilder.AddAzureOpenAIChatCompletion(deployment, endpoint, apiKey);
    Console.WriteLine($"[SemanticKernelChat] Using Azure OpenAI deployment '{deployment}' at {endpoint}.");
}

kernelBuilder.Plugins.AddFromType<TimePlugin>();

kernelBuilder.AddAxonPushTelemetry(
    client =>
    {
        client.ApiKey = axonPushApiKey;
        client.TenantId = axonPushTenantId;
        client.Environment = axonPushEnvironment;
    },
    exporter =>
    {
        exporter.ChannelId = axonPushChannelId;
        exporter.ServiceName = "semantic-kernel-chat";
        exporter.Environment = axonPushEnvironment;
    });

builder.Services.AddLogging(logging => logging.SetMinimumLevel(LogLevel.Warning));

using var host = builder.Build();
_ = host.Services.GetRequiredService<TracerProvider>();

var kernel = host.Services.GetRequiredService<Kernel>();
var chat = kernel.GetRequiredService<IChatCompletionService>();
var execution = new OpenAIPromptExecutionSettings
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto(),
};

var history = new ChatHistory("You are a concise assistant. If asked for the current time, call the GetTime function.");

Console.WriteLine("Type a prompt and press enter. Empty line exits.");
while (true)
{
    Console.Write("> ");
    var line = Console.ReadLine();
    if (string.IsNullOrWhiteSpace(line))
    {
        break;
    }

    history.AddUserMessage(line);
    var response = await chat.GetChatMessageContentAsync(history, execution, kernel).ConfigureAwait(false);
    history.Add(response);
    Console.WriteLine(response.Content);
}

Console.WriteLine("Flushing telemetry...");
await host.StopAsync().ConfigureAwait(false);
Console.WriteLine("Done.");

#pragma warning restore SKEXP0001

static string Required(IConfiguration configuration, string key)
{
    var value = configuration[key];
    if (string.IsNullOrWhiteSpace(value))
    {
        throw new InvalidOperationException($"Missing required configuration value '{key}'. Set it via env var or user secrets.");
    }
    return value;
}

internal sealed class TimePlugin
{
    [KernelFunction("GetTime")]
    [Description("Returns the current UTC time as an ISO 8601 string.")]
#pragma warning disable CA1822
    public string GetTime() => DateTimeOffset.UtcNow.ToString("o", CultureInfo.InvariantCulture);
#pragma warning restore CA1822
}
