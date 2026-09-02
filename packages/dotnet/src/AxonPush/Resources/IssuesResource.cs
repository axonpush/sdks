using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class IssuesResource : ResourceBase
{
    private readonly IssueControllerClient _issueControllerClient;

    internal IssuesResource(AxonPushTransport transport)
        : base(transport)
    {
        _issueControllerClient = new IssueControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/issues</c></summary>
    public Task<System.Collections.Generic.ICollection<IssueResponseDto>> ListAsync(string? severity = null, string? status = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _issueControllerClient.ListAsync(severity, status, cancellationToken);

    /// <summary>Get. <c>GET /v2/issues/{issueId}</c></summary>
    public Task<IssueResponseDto> GetAsync(string issueId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _issueControllerClient.GetAsync(issueId, cancellationToken);

    /// <summary>Update. <c>PATCH /v2/issues/{issueId}</c></summary>
    public Task<IssueResponseDto> UpdateAsync(string issueId, UpdateIssueDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _issueControllerClient.UpdateAsync(issueId, body, cancellationToken);

    /// <summary>Add to dataset. <c>POST /v2/issues/{issueId}/actions/add-to-dataset</c></summary>
    public Task<IssueResponseDto> AddToDatasetAsync(string issueId, AddIssueToDatasetDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _issueControllerClient.AddToDatasetAsync(issueId, body, cancellationToken);

    /// <summary>Merge. <c>POST /v2/issues/{issueId}/merge</c></summary>
    public Task<IssueResponseDto> MergeAsync(string issueId, MergeIssueDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _issueControllerClient.MergeAsync(issueId, body, cancellationToken);

    /// <summary>Occurrences. <c>GET /v2/issues/{issueId}/occurrences</c></summary>
    public Task<System.Collections.Generic.ICollection<IssueOccurrenceResponseDto>> OccurrencesAsync(string issueId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _issueControllerClient.OccurrencesAsync(issueId, cancellationToken);
}
