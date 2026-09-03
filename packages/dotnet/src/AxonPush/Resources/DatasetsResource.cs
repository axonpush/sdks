using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class DatasetsResource : ResourceBase
{
    private readonly DatasetControllerClient _datasetControllerClient;

    internal DatasetsResource(AxonPushTransport transport)
        : base(transport)
    {
        _datasetControllerClient = new DatasetControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/datasets</c></summary>
    public Task<DatasetListDto> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/datasets</c></summary>
    public Task<DatasetDto> CreateAsync(CreateDatasetDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/datasets/{datasetId}</c></summary>
    public Task<DatasetDeleteDto> DeleteAsync(string datasetId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.RemoveAsync(datasetId, cancellationToken);

    /// <summary>Get. <c>GET /v2/datasets/{datasetId}</c></summary>
    public Task<DatasetDto> GetAsync(string datasetId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.GetAsync(datasetId, cancellationToken);

    /// <summary>Revisions. <c>GET /v2/datasets/{datasetId}/revisions</c></summary>
    public Task<DatasetRevisionListDto> RevisionsAsync(string datasetId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.RevisionsAsync(datasetId, cancellationToken);

    /// <summary>Create revision. <c>POST /v2/datasets/{datasetId}/revisions</c></summary>
    public Task<DatasetRevisionDto> CreateRevisionAsync(string datasetId, CreateDatasetRevisionDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.CreateRevisionAsync(datasetId, body, cancellationToken);

    /// <summary>From traces. <c>POST /v2/datasets/{datasetId}/revisions/from-traces</c></summary>
    public Task<DatasetRevisionDto> FromTracesAsync(string datasetId, TraceDatasetSelectionDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.FromTracesAsync(datasetId, body, cancellationToken);

    /// <summary>Import revision. <c>POST /v2/datasets/{datasetId}/revisions/import</c></summary>
    public Task<DatasetRevisionDto> ImportRevisionAsync(string datasetId, ImportDatasetRevisionDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.ImportRevisionAsync(datasetId, body, cancellationToken);

    /// <summary>Export revision. <c>GET /v2/datasets/{datasetId}/revisions/{revision}/export/{format}</c></summary>
    public Task<DatasetExportDto> ExportRevisionAsync(string datasetId, Format format, double revision, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.ExportRevisionAsync(datasetId, format, revision, cancellationToken);

    /// <summary>Items. <c>GET /v2/datasets/{datasetId}/revisions/{revision}/items</c></summary>
    public Task<DatasetRevisionItemsDto> ItemsAsync(string datasetId, double revision, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _datasetControllerClient.ItemsAsync(datasetId, revision, cancellationToken);
}
