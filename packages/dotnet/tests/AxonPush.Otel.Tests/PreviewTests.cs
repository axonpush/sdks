using AxonPush.Otel.Internal;
using AxonPush.Otel.Telemetry;
using Xunit;

namespace AxonPush.Otel.Tests;

public class PreviewTests
{
    [Fact]
    public void RedactedPreviewUsesUnicodeCodepoints()
    {
        var input = new Dictionary<string, object?> { ["prompt"] = string.Concat(Enumerable.Repeat("😀", 300)) };
        var output = Assert.IsType<Dictionary<string, object?>>(TelemetryRedactor.Redact(input, ContentCaptureMode.Redacted, Array.Empty<string>(), 4096));
        Assert.Equal(string.Concat(Enumerable.Repeat("😀", 256)) + "…[REDACTED_PREVIEW]", output["prompt"]);
    }
}
