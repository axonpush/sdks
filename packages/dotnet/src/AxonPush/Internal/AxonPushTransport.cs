using System.Net.Http.Json;
using AxonPush.Events;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace AxonPush.Internal;

/// <summary>
/// Owns the HTTP pipeline every resource shares: header stamping and the retry
/// ladder live in delegating handlers, so the generated API clients behave the
/// same as the events path without either restating the logic.
///
/// Fail-open stays here, and only on the events path. A gate that passes
/// because the API was unreachable is worse than no gate.
/// </summary>
internal sealed class AxonPushTransport : IDisposable
{
    /// <summary>
    /// Publish route, singular. This read "events" and 404ed against
    /// <c>GET /events/search</c>, the only route on that plural path.
    /// ContractTests asserts it against contract/openapi.sdk.json.
    /// </summary>
    internal const string EventsPath = "event";

    private readonly bool _ownsHttpClient;
    private readonly AxonPushOptions _options;
    private readonly ILogger<AxonPushTransport> _logger;

    public AxonPushTransport(
        AxonPushOptions options,
        HttpClient? injectedClient,
        ILoggerFactory? loggerFactory)
    {
        options.Validate();
        _options = options;
        _logger = (loggerFactory ?? NullLoggerFactory.Instance).CreateLogger<AxonPushTransport>();

        // An injected client is a test seam or a caller-managed pool. Either way
        // it becomes the terminal hop of our pipeline rather than replacing it,
        // so headers and retries apply in both cases.
        HttpMessageHandler terminal = injectedClient is null
            ? new HttpClientHandler()
            : new ForwardingHandler(injectedClient);

        HttpClient = new HttpClient(
            new AxonPushRetryHandler(new RetryPolicy(options.MaxRetries))
            {
                InnerHandler = new AxonPushHeaderHandler(options) { InnerHandler = terminal },
            })
        {
            BaseAddress = injectedClient?.BaseAddress ?? options.BaseUrl,
            Timeout = options.Timeout,
        };
        _ownsHttpClient = true;
    }

    /// <summary>The pipeline the generated API clients are constructed over.</summary>
    public HttpClient HttpClient { get; }

    public async Task<PublishResult> PostEventAsync(
        PublishRequest request,
        CancellationToken userCancellation)
    {
        using var message = new HttpRequestMessage(HttpMethod.Post, EventsPath)
        {
            Content = JsonContent.Create(request, options: AxonPushJsonOptions.Default),
        };

        try
        {
            using var response = await HttpClient.SendAsync(message, userCancellation)
                .ConfigureAwait(false);
            var attempts = Attempts(message);
            if (response.IsSuccessStatusCode)
            {
                return PublishResult.Ok(response.StatusCode, attempts);
            }

            return HandleFailure(
                new AxonPushException(
                    $"AxonPush publish failed with {(int)response.StatusCode} {response.ReasonPhrase}.")
                {
                    StatusCode = response.StatusCode,
                    ResponseBody = await ReadBodyAsync(response).ConfigureAwait(false),
                },
                attempts);
        }
        catch (OperationCanceledException) when (userCancellation.IsCancellationRequested)
        {
            throw;
        }
        catch (AxonPushException)
        {
            throw;
        }
        catch (Exception exception)
        {
            return HandleFailure(
                new AxonPushException("AxonPush publish failed.", exception),
                Attempts(message));
        }
    }

    private static int Attempts(HttpRequestMessage message) =>
        message.Options.TryGetValue(AxonPushRetryHandler.AttemptsKey, out var attempts)
            ? attempts
            : 1;

    private PublishResult HandleFailure(AxonPushException exception, int attempts)
    {
        if (_options.FailOpen)
        {
            AxonPushTransportLogs.PublishFailedFailOpen(_logger, exception);
            return PublishResult.Failed(exception.Message, exception.StatusCode, attempts);
        }

        throw exception;
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
            HttpClient.Dispose();
        }
    }
}

/// <summary>Terminates our pipeline in a caller-supplied client.</summary>
internal sealed class ForwardingHandler : HttpMessageHandler
{
    private readonly HttpClient _inner;

    public ForwardingHandler(HttpClient inner)
    {
        _inner = inner;
    }

    protected override async Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
    {
        // Our pipeline has already sent this message, and a message may only be
        // sent once. The caller's client needs its own copy.
        var body = await HttpRequestCloning.BufferAsync(request, cancellationToken)
            .ConfigureAwait(false);
        var forwarded = HttpRequestCloning.Clone(request, body);
        return await _inner.SendAsync(forwarded, cancellationToken).ConfigureAwait(false);
    }
}
