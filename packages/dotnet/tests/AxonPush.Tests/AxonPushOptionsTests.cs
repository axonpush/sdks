using Microsoft.Extensions.Configuration;
using Xunit;

namespace AxonPush.Tests;

public class AxonPushOptionsTests
{
    [Fact]
    public void FromEnvironment_AppliesAllKnownKeys()
    {
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(new Dictionary<string, string?>
            {
                ["AXONPUSH_API_KEY"] = "ak_test",
                ["AXONPUSH_TENANT_ID"] = "tenant",
                ["AXONPUSH_BASE_URL"] = "https://example.test/",
                ["AXONPUSH_ENVIRONMENT"] = "staging",
                ["AXONPUSH_TIMEOUT"] = "5",
                ["AXONPUSH_MAX_RETRIES"] = "2",
                ["AXONPUSH_FAIL_OPEN"] = "false",
            })
            .Build();

        var options = AxonPushOptions.FromEnvironment(config);

        Assert.Equal("ak_test", options.ApiKey);
        Assert.Equal("tenant", options.TenantId);
        Assert.Equal(new Uri("https://example.test/"), options.BaseUrl);
        Assert.Equal("staging", options.Environment);
        Assert.Equal(TimeSpan.FromSeconds(5), options.Timeout);
        Assert.Equal(2, options.MaxRetries);
        Assert.False(options.FailOpen);
    }

    [Fact]
    public void Validate_RequiresApiKeyAndTenant()
    {
        var options = new AxonPushOptions { ApiKey = "ak", TenantId = "t" };
        var exception = Record.Exception(() => options.Validate());
        Assert.Null(exception);

        var missingKey = new AxonPushOptions { TenantId = "t" };
        Assert.Throws<InvalidOperationException>(() => missingKey.Validate());

        var missingTenant = new AxonPushOptions { ApiKey = "k" };
        Assert.Throws<InvalidOperationException>(() => missingTenant.Validate());
    }
}
