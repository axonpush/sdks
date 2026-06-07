using System.Globalization;
using System.Net;

namespace AxonPush.Internal;

internal sealed class RetryPolicy
{
    private static readonly TimeSpan[] DefaultDelays =
    [
        TimeSpan.FromMilliseconds(250),
        TimeSpan.FromMilliseconds(500),
        TimeSpan.FromSeconds(1),
        TimeSpan.FromSeconds(2),
        TimeSpan.FromSeconds(4),
    ];

    private readonly int _maxRetries;

    public RetryPolicy(int maxRetries)
    {
        _maxRetries = maxRetries;
    }

    /// <summary>Total attempts including the initial try.</summary>
    public int TotalAttempts => _maxRetries + 1;

    /// <summary>
    /// Returns the delay before the given retry attempt. Retry index is 1-based:
    /// 1 = the first retry, 2 = the second, and so on.
    /// </summary>
    public static TimeSpan DelayFor(int retryIndex)
    {
        if (retryIndex <= 0)
        {
            return TimeSpan.Zero;
        }

        var idx = Math.Min(retryIndex - 1, DefaultDelays.Length - 1);
        return DefaultDelays[idx];
    }

    public static bool ShouldRetry(HttpResponseMessage response)
    {
        var code = (int)response.StatusCode;
        if (response.StatusCode == HttpStatusCode.RequestTimeout) return true;
        if (response.StatusCode == (HttpStatusCode)429) return true;
        return code >= 500 && code < 600;
    }

    public static bool ShouldRetry(Exception exception, CancellationToken userCancellation)
    {
        if (exception is HttpRequestException) return true;
        if (exception is TaskCanceledException && !userCancellation.IsCancellationRequested) return true;
        return false;
    }

    public static TimeSpan ParseRetryAfter(HttpResponseMessage response, TimeSpan fallback)
    {
        var retryAfter = response.Headers.RetryAfter;
        if (retryAfter is null)
        {
            return fallback;
        }

        if (retryAfter.Delta is { } delta && delta > TimeSpan.Zero)
        {
            return delta;
        }

        if (retryAfter.Date is { } when)
        {
            var diff = when - DateTimeOffset.UtcNow;
            return diff > TimeSpan.Zero ? diff : fallback;
        }

        return fallback;
    }
}
