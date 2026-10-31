using AxonPush.Operations;
using Polly;
using Polly.Retry;
using System.Diagnostics;
using System.Net;
using System.Net.Http.Json;
using System.Reflection;
using AxonPush.Events;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace AxonPush.Internal;

/// <summary>
/// Inner HTTP machinery used by <see cref="EventsResource"/>. Owns the retry loop, header stamping,
/// JSON serialisation, and fail-open logic.
/// </summary>
internal sealed class AxonPushTransport : IDisposable
{
    /// <summary>
    /// Publish route, singular. This read "events" and 404ed against
    /// <c>GET /events/search</c>, the only route on that plural path.
    /// ContractTests asserts it against contract/openapi.sdk.json.
    /// </summary>
    internal const string EventsPath = "event";

    private static readonly string UserAgent =
        $"axonpush-dotnet/{typeof(AxonPushTransport).Assembly.GetName().Version?.ToString(3) ?? "0.0.0"}";

    private readonly HttpClient _httpClient;
    private readonly bool _ownsHttpClient;
    private readonly AxonPushOptions _options;
    private readonly ILogger<AxonPushTransport> _logger;

    public AxonPushTransport(AxonPushOptions options, HttpClient? injectedClient, ILoggerFactory? loggerFactory)
    {
        options.Validate();
        _options = options;
        _logger = (loggerFactory ?? NullLoggerFactory.Instance).CreateLogger<AxonPushTransport>();

        if (injectedClient is not null)
        {
            _httpClient = injectedClient;
            _ownsHttpClient = false;
        }
        else
        {
            // Redirect handlers preserve custom API-key headers. Never send them to
            // a redirect target; callers must configure the canonical API URL.
            _httpClient = new HttpClient(new HttpClientHandler { AllowAutoRedirect = false })
            {
                BaseAddress = options.BaseUrl,
                Timeout = options.Timeout,
            };
            _ownsHttpClient = true;
        }

        if (_httpClient.BaseAddress is null)
        {
            _httpClient.BaseAddress = options.BaseUrl;
        }
    }

    private async Task<(HttpResponseMessage Response, int Attempts)> SendWithRetryAsync(
        Func<HttpRequestMessage> create, bool retrySafe, CancellationToken userCancellation)
    {
        using var budget = CancellationTokenSource.CreateLinkedTokenSource(userCancellation);
        budget.CancelAfter(_options.Timeout);
        var attempts = 0;
        var pipeline = new ResiliencePipelineBuilder<HttpResponseMessage>()
            .AddRetry(new RetryStrategyOptions<HttpResponseMessage>
            {
                MaxRetryAttempts = Math.Max(1, _options.MaxRetries),
                Delay = TimeSpan.FromMilliseconds(250),
                MaxDelay = TimeSpan.FromSeconds(4),
                BackoffType = DelayBackoffType.Exponential,
                UseJitter = true,
                ShouldHandle = args => ValueTask.FromResult(retrySafe && _options.MaxRetries > 0 &&
                    (args.Outcome.Result is { } response ? RetryPolicy.ShouldRetry(response) :
                    args.Outcome.Exception is { } ex && RetryPolicy.ShouldRetry(ex, budget.Token))),
                DelayGenerator = args => ValueTask.FromResult<TimeSpan?>(args.Outcome.Result is { } response && response.Headers.RetryAfter is not null
                    ? RetryPolicy.ParseRetryAfter(response, TimeSpan.Zero) : null),
                OnRetry = args => { args.Outcome.Result?.Dispose(); return default; },
            }).Build();
        try
        {
            var result = await pipeline.ExecuteAsync(async token =>
            {
                attempts++;
                using var message = create();
                StampHeaders(message);
                return await _httpClient.SendAsync(message, token).ConfigureAwait(false);
            }, budget.Token).ConfigureAwait(false);
            return (result, attempts);
        }
        catch (OperationCanceledException) when (!userCancellation.IsCancellationRequested)
        {
            throw new AxonPushException("AxonPush invocation timed out.") { Data = { ["AxonPush.Attempts"] = attempts } };
        }
        catch (Exception ex) { ex.Data["AxonPush.Attempts"] = attempts; throw; }
    }

    public async Task<PublishResult> PostEventAsync(PublishRequest request, CancellationToken userCancellation)
    {
        request = request with { DedupKey = string.IsNullOrEmpty(request.DedupKey) ? Guid.NewGuid().ToString() : request.DedupKey };
        var attempts = 0;
        try
        {
            var result = await SendWithRetryAsync(() =>
            {
                var message = new HttpRequestMessage(HttpMethod.Post, EventsPath) { Content = JsonContent.Create(request, options: AxonPushJsonOptions.Default) };
                if (!string.IsNullOrWhiteSpace(request.Environment)) message.Headers.Add("X-Axonpush-Environment", request.Environment);
                return message;
            }, true, userCancellation).ConfigureAwait(false);
            attempts = result.Attempts;
            using var response = result.Response;
            if (response.IsSuccessStatusCode) return PublishResult.Ok(response.StatusCode, attempts);
            return HandleFailure(new AxonPushException($"AxonPush publish failed with {(int)response.StatusCode} {response.ReasonPhrase}.")
            { StatusCode = response.StatusCode, ResponseBody = await ReadBodyAsync(response).ConfigureAwait(false) }, attempts);
        }
        catch (OperationCanceledException) when (userCancellation.IsCancellationRequested) { throw; }
        catch (AxonPushException ex) { return HandleFailure(ex, ex.Data["AxonPush.Attempts"] as int? ?? attempts); }
        catch (Exception ex) { return HandleFailure(new AxonPushException("AxonPush publish failed.", ex), ex.Data["AxonPush.Attempts"] as int? ?? attempts); }
    }

    /// <summary>Typed control-plane operations never fail open.</summary>
    public async Task<TResponse?> SendAsync<TResponse>(HttpMethod method, string path, object? body, CancellationToken userCancellation) where TResponse : class
    {
        try
        {
            var result = await SendWithRetryAsync(() => new HttpRequestMessage(method, path)
            { Content = body is null ? null : JsonContent.Create(body, body.GetType(), options: AxonPushJsonOptions.Default) }, method == HttpMethod.Get || method == HttpMethod.Head ||
                (method == HttpMethod.Post && path.StartsWith("workspaces/", StringComparison.Ordinal) && path.EndsWith("/observations", StringComparison.Ordinal) && body is WorkspaceIngestInputBody batch && batch.Observations is not null && batch.Observations.All(item => !string.IsNullOrEmpty(item.SourceEventId))), userCancellation).ConfigureAwait(false);
            using var response = result.Response;
            if (!response.IsSuccessStatusCode) throw new AxonPushException($"AxonPush request to {path} failed with {(int)response.StatusCode} {response.ReasonPhrase}.")
            { StatusCode = response.StatusCode, ResponseBody = await ReadBodyAsync(response).ConfigureAwait(false) };
            if (response.StatusCode == HttpStatusCode.NoContent) return null;
            return await response.Content.ReadFromJsonAsync<TResponse>(AxonPushJsonOptions.Default, userCancellation).ConfigureAwait(false);
        }
        catch (OperationCanceledException) when (userCancellation.IsCancellationRequested) { throw; }
        catch (AxonPushException) { throw; }
        catch (Exception ex) { throw new AxonPushException($"AxonPush request to {path} failed.", ex); }
    }

    /// <summary>Observation acceptance fails open on connection failure when configured.</summary>
    public async Task<TResponse?> SendObservationAsync<TResponse>(
        HttpMethod method, string path, object? body, CancellationToken cancellationToken)
        where TResponse : class
    {
        try
        {
            return await SendAsync<TResponse>(method, path, body, cancellationToken).ConfigureAwait(false);
        }
        catch (AxonPushException ex) when (_options.FailOpen && ex.StatusCode is null)
        {
            AxonPushTransportLogs.PublishFailedFailOpen(_logger, ex);
            return null;
        }
    }

    private void StampHeaders(HttpRequestMessage message)
    {
        if (!string.IsNullOrWhiteSpace(_options.ApiKey))
        {
            // pt_ public ingest tokens go on X-Public-Token; ak_ API keys on x-axonpush-api-key.
            var authHeader = _options.ApiKey!.StartsWith("pt_", StringComparison.Ordinal)
                ? "X-Public-Token"
                : "x-axonpush-api-key";
            if (!message.Headers.Contains(authHeader))
            {
                message.Headers.Add(authHeader, _options.ApiKey);
            }
        }

        if (!message.Headers.Contains("x-tenant-id") && !string.IsNullOrWhiteSpace(_options.TenantId))
        {
            message.Headers.Add("x-tenant-id", _options.TenantId);
        }

        if (!string.IsNullOrWhiteSpace(_options.Environment) && !message.Headers.Contains("X-Axonpush-Environment"))
        {
            message.Headers.Add("X-Axonpush-Environment", _options.Environment);
        }

        var current = Activity.Current;
        if (current is not null && current.TraceId != default && !message.Headers.Contains("X-Axonpush-Trace-Id"))
        {
            message.Headers.Add("X-Axonpush-Trace-Id", current.TraceId.ToHexString());
        }

        if (message.Headers.UserAgent.Count == 0)
        {
            message.Headers.TryAddWithoutValidation("User-Agent", UserAgent);
        }
    }

    private PublishResult HandleFailure(AxonPushException ex, int attempts)
    {
        if (_options.FailOpen)
        {
            AxonPushTransportLogs.PublishFailedFailOpen(_logger, ex);
            return PublishResult.Failed(ex.Message, ex.StatusCode, attempts);
        }

        throw ex;
    }

    private static async Task<string?> ReadBodyAsync(HttpResponseMessage response)
    {
        try
        {
            return await response.Content.ReadAsStringAsync().ConfigureAwait(false);
        }
        catch (Exception)
        {
            return null;
        }
    }

    public void Dispose()
    {
        if (_ownsHttpClient)
        {
            _httpClient.Dispose();
        }
    }
}
