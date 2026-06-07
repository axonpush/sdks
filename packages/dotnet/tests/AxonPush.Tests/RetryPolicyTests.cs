using System.Net;
using AxonPush.Internal;
using Xunit;

namespace AxonPush.Tests;

public class RetryPolicyTests
{
    [Fact]
    public void DelayFor_FollowsBackoffSchedule()
    {
        Assert.Equal(TimeSpan.Zero, RetryPolicy.DelayFor(0));
        Assert.Equal(TimeSpan.FromMilliseconds(250), RetryPolicy.DelayFor(1));
        Assert.Equal(TimeSpan.FromMilliseconds(500), RetryPolicy.DelayFor(2));
        Assert.Equal(TimeSpan.FromSeconds(1), RetryPolicy.DelayFor(3));
        Assert.Equal(TimeSpan.FromSeconds(2), RetryPolicy.DelayFor(4));
        Assert.Equal(TimeSpan.FromSeconds(4), RetryPolicy.DelayFor(5));
        Assert.Equal(TimeSpan.FromSeconds(4), RetryPolicy.DelayFor(99));
    }

    [Theory]
    [InlineData(HttpStatusCode.RequestTimeout, true)]
    [InlineData((HttpStatusCode)429, true)]
    [InlineData(HttpStatusCode.InternalServerError, true)]
    [InlineData(HttpStatusCode.BadGateway, true)]
    [InlineData(HttpStatusCode.BadRequest, false)]
    [InlineData(HttpStatusCode.Unauthorized, false)]
    [InlineData(HttpStatusCode.Forbidden, false)]
    public void ShouldRetry_HttpResponse_MatchesPolicy(HttpStatusCode status, bool expected)
    {
        using var response = new HttpResponseMessage(status);
        Assert.Equal(expected, RetryPolicy.ShouldRetry(response));
    }

    [Fact]
    public void ShouldRetry_HttpRequestException_IsRetryable()
    {
        Assert.True(RetryPolicy.ShouldRetry(new HttpRequestException(), CancellationToken.None));
    }

    [Fact]
    public void ShouldRetry_TaskCanceled_RetryableWhenUserHasNotCancelled()
    {
        Assert.True(RetryPolicy.ShouldRetry(new TaskCanceledException(), CancellationToken.None));
    }

    [Fact]
    public void ShouldRetry_TaskCanceled_NotRetryableWhenUserCancelled()
    {
        using var cts = new CancellationTokenSource();
        cts.Cancel();
        Assert.False(RetryPolicy.ShouldRetry(new TaskCanceledException(), cts.Token));
    }

    [Fact]
    public void ParseRetryAfter_PrefersHeaderDelta()
    {
        using var response = new HttpResponseMessage(HttpStatusCode.TooManyRequests);
        response.Headers.RetryAfter = new System.Net.Http.Headers.RetryConditionHeaderValue(TimeSpan.FromSeconds(7));
        var result = RetryPolicy.ParseRetryAfter(response, fallback: TimeSpan.FromSeconds(1));
        Assert.Equal(TimeSpan.FromSeconds(7), result);
    }

    [Fact]
    public void ParseRetryAfter_FallsBackWhenHeaderMissing()
    {
        using var response = new HttpResponseMessage(HttpStatusCode.TooManyRequests);
        var fallback = TimeSpan.FromMilliseconds(123);
        Assert.Equal(fallback, RetryPolicy.ParseRetryAfter(response, fallback));
    }
}
