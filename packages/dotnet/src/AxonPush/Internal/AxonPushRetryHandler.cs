namespace AxonPush.Internal;

/// <summary>
/// Applies the shared backoff ladder to every request in the pipeline, and
/// records how many attempts it took so a caller can report it.
/// </summary>
internal sealed class AxonPushRetryHandler : DelegatingHandler
{
    internal static readonly HttpRequestOptionsKey<int> AttemptsKey = new("axonpush.attempts");

    private readonly RetryPolicy _retryPolicy;

    public AxonPushRetryHandler(RetryPolicy retryPolicy)
    {
        _retryPolicy = retryPolicy;
    }

    protected override async Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
    {
        var body = await HttpRequestCloning.BufferAsync(request, cancellationToken)
            .ConfigureAwait(false);
        var attempt = 0;

        while (true)
        {
            attempt++;
            var last = attempt >= _retryPolicy.TotalAttempts;
            var attemptRequest = attempt == 1 ? request : HttpRequestCloning.Clone(request, body);
            try
            {
                var response = await base.SendAsync(attemptRequest, cancellationToken)
                    .ConfigureAwait(false);
                if (last || !RetryPolicy.ShouldRetry(response))
                {
                    request.Options.Set(AttemptsKey, attempt);
                    return response;
                }

                var delay = RetryPolicy.ParseRetryAfter(response, RetryPolicy.DelayFor(attempt));
                response.Dispose();
                Discard(attemptRequest, request);
                await Task.Delay(delay, cancellationToken).ConfigureAwait(false);
            }
            catch (Exception exception) when (
                !last && RetryPolicy.ShouldRetry(exception, cancellationToken))
            {
                Discard(attemptRequest, request);
                await Task.Delay(RetryPolicy.DelayFor(attempt), cancellationToken)
                    .ConfigureAwait(false);
            }
        }
    }

    /// <summary>The caller owns the original; only our own copies are ours to dispose.</summary>
    private static void Discard(HttpRequestMessage attempt, HttpRequestMessage original)
    {
        if (!ReferenceEquals(attempt, original))
        {
            attempt.Dispose();
        }
    }
}
