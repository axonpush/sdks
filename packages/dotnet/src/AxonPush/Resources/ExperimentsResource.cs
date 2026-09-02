using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class ExperimentsResource : ResourceBase
{
    private readonly ExperimentControllerClient _experimentControllerClient;

    internal ExperimentsResource(AxonPushTransport transport)
        : base(transport)
    {
        _experimentControllerClient = new ExperimentControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/experiments</c></summary>
    public Task<ExperimentListDto> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/experiments</c></summary>
    public Task<ExperimentDto> CreateAsync(CreateExperimentDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/experiments/{experimentId}</c></summary>
    public Task<ExperimentDeleteDto> DeleteAsync(string experimentId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.RemoveAsync(experimentId, cancellationToken);

    /// <summary>Get. <c>GET /v2/experiments/{experimentId}</c></summary>
    public Task<ExperimentDto> GetAsync(string experimentId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.GetAsync(experimentId, cancellationToken);

    /// <summary>Cancel. <c>POST /v2/experiments/{experimentId}/cancel</c></summary>
    public Task<ExperimentDto> CancelAsync(string experimentId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.CancelAsync(experimentId, cancellationToken);

    /// <summary>Compare. <c>GET /v2/experiments/{experimentId}/compare</c></summary>
    public Task<ExperimentComparisonDto> CompareAsync(string experimentId, string? baselineExperimentId = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.CompareAsync(experimentId, baselineExperimentId, cancellationToken);

    /// <summary>Gate. <c>POST /v2/experiments/{experimentId}/gate</c></summary>
    public Task<ExperimentGateResultDto> GateAsync(string experimentId, ExperimentGateDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.GateAsync(experimentId, body, cancellationToken);

    /// <summary>Results. <c>GET /v2/experiments/{experimentId}/results</c></summary>
    public Task<ExperimentResultListDto> ResultsAsync(string experimentId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.ResultsAsync(experimentId, cancellationToken);

    /// <summary>Submit results. <c>POST /v2/experiments/{experimentId}/results</c></summary>
    public Task<ExperimentDto> SubmitResultsAsync(string experimentId, SubmitLocalExperimentResultsDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.SubmitResultsAsync(experimentId, body, cancellationToken);

    /// <summary>Run. <c>POST /v2/experiments/{experimentId}/run</c></summary>
    public Task<ExperimentDto> RunAsync(string experimentId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _experimentControllerClient.RunAsync(experimentId, cancellationToken);
}
