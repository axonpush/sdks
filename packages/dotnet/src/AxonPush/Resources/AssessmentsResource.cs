using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class AssessmentsResource : ResourceBase
{
    private readonly AssessmentControllerClient _assessmentControllerClient;

    internal AssessmentsResource(AxonPushTransport transport)
        : base(transport)
    {
        _assessmentControllerClient = new AssessmentControllerClient(Http);
    }

    /// <summary>Remove by query. <c>DELETE /v2/traces/{traceId}/assessments</c></summary>
    public Task<AssessmentDeleteResponseDto> RemoveByQueryAsync(string traceId, string assessmentId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _assessmentControllerClient.RemoveByQueryAsync(traceId, assessmentId, cancellationToken);

    /// <summary>List. <c>GET /v2/traces/{traceId}/assessments</c></summary>
    public Task<AssessmentListResponseDto> ListAsync(string traceId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _assessmentControllerClient.ListAsync(traceId, cancellationToken);

    /// <summary>Create. <c>POST /v2/traces/{traceId}/assessments</c></summary>
    public Task<AssessmentDto> CreateAsync(string traceId, CreateAssessmentDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _assessmentControllerClient.CreateAsync(traceId, body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/traces/{traceId}/assessments/{assessmentId}</c></summary>
    public Task<AssessmentDeleteResponseDto> DeleteAsync(string assessmentId, string traceId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _assessmentControllerClient.RemoveAsync(assessmentId, traceId, cancellationToken);
}
