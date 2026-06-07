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
    private static readonly string UserAgent =
        $"axonpush-dotnet/{typeof(AxonPushTransport).Assembly.GetName().Version?.ToString(3) ?? "0.0.0"}";

    private readonly HttpClient _httpClient;
    private readonly bool _ownsHttpClient;
    private readonly AxonPushOptions _options;
    private readonly RetryPolicy _retryPolicy;
    private readonly ILogger<AxonPushTransport> _logger;

    public AxonPushTransport(AxonPushOptions options, HttpClient? injectedClient, ILoggerFactory? loggerFactory)
    {
        options.Validate();
        _options = options;
        _retryPolicy = new RetryPolicy(options.MaxRetries);
        _logger = (loggerFactory ?? NullLoggerFactory.Instance).CreateLogger<AxonPushTransport>();

        if (injectedClient is not null)
        {
            _httpClient = injectedClient;
            _ownsHttpClient = false;
        }
        else
        {
            _httpClient = new HttpClient
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

    public async Task<PublishResult> PostEventAsync(PublishRequest request, CancellationToken userCancellation)
    {
        var attempt = 0;
        Exception? lastException = null;
        HttpStatusCode? lastStatus = null;
        string? lastError = null;

        while (attempt < _retryPolicy.TotalAttempts)
        {
            attempt++;
            try
            {
                using var message = new HttpRequestMessage(HttpMethod.Post, "events")
                {
                    Content = JsonContent.Create(request, options: AxonPushJsonOptions.Default),
                };
                StampHeaders(message);

                using var response = await _httpClient.SendAsync(message, userCancellation).ConfigureAwait(false);
                if (response.IsSuccessStatusCode)
                {
                    return PublishResult.Ok(response.StatusCode, attempt);
                }

                lastStatus = response.StatusCode;
                lastError = await ReadBodyAsync(response).ConfigureAwait(false);

                if (!RetryPolicy.ShouldRetry(response) || attempt >= _retryPolicy.TotalAttempts)
                {
                    return HandleFailure(
                        new AxonPushException($"AxonPush publish failed with {(int)response.StatusCode} {response.ReasonPhrase}.")
                        {
                            StatusCode = response.StatusCode,
                            ResponseBody = lastError,
                        },
                        attempt);
                }

                var delay = RetryPolicy.ParseRetryAfter(response, RetryPolicy.DelayFor(attempt));
                await Task.Delay(delay, userCancellation).ConfigureAwait(false);
            }
            catch (OperationCanceledException) when (userCancellation.IsCancellationRequested)
            {
                throw;
            }
            catch (Exception ex) when (RetryPolicy.ShouldRetry(ex, userCancellation))
            {
                lastException = ex;
                lastError = ex.Message;
                if (attempt >= _retryPolicy.TotalAttempts)
                {
                    return HandleFailure(new AxonPushException("AxonPush publish failed after retries.", ex), attempt);
                }

                var delay = RetryPolicy.DelayFor(attempt);
                await Task.Delay(delay, userCancellation).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                return HandleFailure(new AxonPushException("AxonPush publish failed.", ex), attempt);
            }
        }

        return HandleFailure(
            new AxonPushException(lastError ?? "AxonPush publish failed.", lastException ?? new InvalidOperationException("retries exhausted")),
            attempt);
    }

    private void StampHeaders(HttpRequestMessage message)
    {
        if (!message.Headers.Contains("X-API-Key") && !string.IsNullOrWhiteSpace(_options.ApiKey))
        {
            message.Headers.Add("X-API-Key", _options.ApiKey);
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
