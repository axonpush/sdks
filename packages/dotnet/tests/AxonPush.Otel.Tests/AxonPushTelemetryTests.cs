using System.Diagnostics;
using System.IO.Compression;
using System.Net;
using System.Text;
using AxonPush.Otel.Telemetry;
using Xunit;

namespace AxonPush.Otel.Tests;

/// <summary>
/// Exercises the OTel-native telemetry path against a mock OTLP/HTTP receiver, mirroring the
/// Python SDK's telemetry test: it asserts the exporter posts to <c>/v1/traces</c> with the
/// AxonPush headers and that the exported protobuf carries the <c>gen_ai.*</c> attributes.
/// </summary>
public sealed class AxonPushTelemetryTests
{
    [Fact]
    public async Task ExportsGenAiSpan_WithHeadersAndAttributes()
    {
        using var receiver = new MockOtlpReceiver();
        receiver.Start();

        var source = new ActivitySource("axonpush");
        using var handle = AxonPushTelemetry.ConfigureTelemetry(o =>
        {
            o.BaseUrl = receiver.BaseUrl;
            o.ApiKey = "test-key-123";
            o.ChannelId = "chan-abc";
            o.ServiceName = "telemetry-test";
            o.Environment = "test";
            o.ServiceVersion = "9.9.9";
            o.ContentCapture = ContentCaptureMode.Full;
        });

        using (var activity = GenAi.StartSpan(source, operation: "chat", requestModel: "gpt-4o", system: "openai"))
        {
            Assert.NotNull(activity);
            GenAi.RecordResponse(
                activity,
                responseModel: "gpt-4o",
                inputTokens: 12,
                outputTokens: 48,
                cacheWriteTokens: 7);
            GenAi.RecordContent(
                activity,
                prompt: "hello world",
                completion: "hi there",
                handle: handle);
        }

        Assert.True(handle.Flush(5000), "telemetry flush timed out");

        var request = await receiver.WaitForRequestAsync(TimeSpan.FromSeconds(5));

        Assert.Equal("/v1/traces", request.Path);
        Assert.Equal("test-key-123", request.Headers["X-API-Key"]);
        Assert.Equal("chan-abc", request.Headers["X-Axonpush-Channel"]);
        Assert.Contains("application/x-protobuf", request.ContentType);

        // OTLP protobuf embeds attribute keys and string values as UTF-8; assert on the wire bytes.
        var body = Encoding.UTF8.GetString(request.Body);
        Assert.Contains("gen_ai.operation.name", body);
        Assert.Contains("gen_ai.request.model", body);
        Assert.Contains("gen_ai.system", body);
        Assert.Contains("gen_ai.response.model", body);
        Assert.Contains("gen_ai.usage.input_tokens", body);
        Assert.Contains("gen_ai.usage.output_tokens", body);
        Assert.Contains("gen_ai.usage.cache_write_input_tokens", body);
        Assert.Contains("gen_ai.content.prompt", body);
        Assert.Contains("gen_ai.content.completion", body);
        Assert.Contains("telemetry-test", body); // service.name resource attribute
    }

    [Fact]
    public void RecordContent_MetadataOnly_EmitsNoEvents()
    {
        var source = new ActivitySource("axonpush.metadata-test");
        using var listener = new ActivityListener
        {
            ShouldListenTo = s => s.Name == source.Name,
            Sample = (ref ActivityCreationOptions<ActivityContext> _) => ActivitySamplingResult.AllDataAndRecorded,
        };
        ActivitySource.AddActivityListener(listener);

        using var activity = GenAi.StartSpan(source, operation: "chat", requestModel: "gpt-4o");
        Assert.NotNull(activity);
        GenAi.RecordContent(
            activity,
            prompt: "secret prompt",
            completion: "secret completion",
            contentCapture: ContentCaptureMode.MetadataOnly);

        Assert.Empty(activity.Events);
    }

    [Fact]
    public void RecordContent_Redacted_StripsSecretKeys()
    {
        var source = new ActivitySource("axonpush.redact-test");
        using var listener = new ActivityListener
        {
            ShouldListenTo = s => s.Name == source.Name,
            Sample = (ref ActivityCreationOptions<ActivityContext> _) => ActivitySamplingResult.AllDataAndRecorded,
        };
        ActivitySource.AddActivityListener(listener);

        using var activity = GenAi.StartSpan(source, operation: "chat", requestModel: "gpt-4o");
        Assert.NotNull(activity);
        var payload = new Dictionary<string, object?>
        {
            ["text"] = "keep me",
            ["api_key"] = "sk-should-be-stripped",
        };
        GenAi.RecordContent(activity, prompt: payload, contentCapture: ContentCaptureMode.Full);

        var evt = Assert.Single(activity.Events);
        Assert.Equal("gen_ai.content.prompt", evt.Name);
        var tags = evt.Tags.ToDictionary(t => t.Key, t => t.Value);
        // The nested prompt dict is JSON-flattened under the "prompt" key.
        var promptJson = Assert.IsType<string>(tags["prompt"]);
        Assert.Contains("keep me", promptJson);
        Assert.Contains("[REDACTED]", promptJson);
        Assert.DoesNotContain("sk-should-be-stripped", promptJson);
    }
}

/// <summary>Minimal in-process OTLP/HTTP receiver backed by <see cref="HttpListener"/>.</summary>
internal sealed class MockOtlpReceiver : IDisposable
{
    private readonly HttpListener _listener = new();
    private readonly TaskCompletionSource<CapturedRequest> _received =
        new(TaskCreationOptions.RunContinuationsAsynchronously);
    private readonly int _port;

    public MockOtlpReceiver()
    {
        _port = GetFreePort();
        _listener.Prefixes.Add($"http://127.0.0.1:{_port}/");
    }

    public string BaseUrl => $"http://127.0.0.1:{_port}";

    public void Start()
    {
        _listener.Start();
        _ = Task.Run(AcceptLoop);
    }

    public async Task<CapturedRequest> WaitForRequestAsync(TimeSpan timeout)
    {
        var completed = await Task.WhenAny(_received.Task, Task.Delay(timeout));
        if (completed != _received.Task)
        {
            throw new TimeoutException("Mock OTLP receiver did not receive a request in time.");
        }
        return await _received.Task;
    }

    private async Task AcceptLoop()
    {
        try
        {
            var context = await _listener.GetContextAsync();
            var request = context.Request;

            byte[] body;
            using (var ms = new MemoryStream())
            {
                await request.InputStream.CopyToAsync(ms);
                body = ms.ToArray();
            }

            if (string.Equals(request.Headers["Content-Encoding"], "gzip", StringComparison.OrdinalIgnoreCase))
            {
                body = Decompress(body);
            }

            var headers = new Dictionary<string, string?>(StringComparer.OrdinalIgnoreCase);
            foreach (string key in request.Headers.AllKeys!)
            {
                headers[key] = request.Headers[key];
            }

            _received.TrySetResult(new CapturedRequest(
                request.Url!.AbsolutePath,
                request.ContentType ?? string.Empty,
                headers,
                body));

            // A valid empty ExportTraceServiceResponse is zero bytes; 200 with empty body is fine.
            context.Response.StatusCode = 200;
            context.Response.ContentType = "application/x-protobuf";
            context.Response.Close();
        }
        catch (Exception ex)
        {
            _received.TrySetException(ex);
        }
    }

    private static byte[] Decompress(byte[] data)
    {
        using var input = new MemoryStream(data);
        using var gzip = new GZipStream(input, CompressionMode.Decompress);
        using var output = new MemoryStream();
        gzip.CopyTo(output);
        return output.ToArray();
    }

    private static int GetFreePort()
    {
        var l = new System.Net.Sockets.TcpListener(IPAddress.Loopback, 0);
        l.Start();
        var port = ((IPEndPoint)l.LocalEndpoint).Port;
        l.Stop();
        return port;
    }

    public void Dispose()
    {
        if (_listener.IsListening)
        {
            _listener.Stop();
        }
        ((IDisposable)_listener).Dispose();
    }
}

internal sealed record CapturedRequest(
    string Path,
    string ContentType,
    IReadOnlyDictionary<string, string?> Headers,
    byte[] Body);
