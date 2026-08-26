using Microsoft.Extensions.Logging;

namespace AxonPush.Internal;

internal static partial class AxonPushTransportLogs
{
    [LoggerMessage(EventId = 1000, Level = LogLevel.Warning,
        Message = "AxonPush publish failed; fail-open is on so the call returns without throwing.")]
    public static partial void PublishFailedFailOpen(ILogger logger, Exception exception);
}
