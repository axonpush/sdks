"""Evaluation datasets and their immutable revisions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.datasets import (
    dataset_controller_create as _create_op,
    dataset_controller_create_revision as _create_revision_op,
    dataset_controller_export_revision as _export_revision_op,
    dataset_controller_from_traces as _from_traces_op,
    dataset_controller_get as _get_op,
    dataset_controller_import_revision as _import_revision_op,
    dataset_controller_items as _items_op,
    dataset_controller_list as _list_op,
    dataset_controller_remove as _remove_op,
    dataset_controller_revisions as _revisions_op,
)
from axonpush._internal.api.models import (
    CreateDatasetDto,
    CreateDatasetRevisionDto,
    DatasetDeleteDto,
    DatasetDto,
    DatasetExportDto,
    DatasetListDto,
    DatasetRevisionDto,
    DatasetRevisionItemsDto,
    DatasetRevisionListDto,
    ImportDatasetRevisionDto,
    TraceDatasetSelectionDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Datasets:
    """Evaluation datasets and their immutable revisions."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> DatasetListDto | None:
        """List them all. `GET /v2/datasets`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreateDatasetDto) -> DatasetDto | None:
        """Create one. `POST /v2/datasets`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, dataset_id: str) -> DatasetDeleteDto | None:
        """Delete one. `DELETE /v2/datasets/{datasetId}`"""
        return self._client._invoke(_remove_op, dataset_id=dataset_id)

    def get(self, dataset_id: str) -> DatasetDto | None:
        """Fetch one by id. `GET /v2/datasets/{datasetId}`"""
        return self._client._invoke(_get_op, dataset_id=dataset_id)

    def revisions(self, dataset_id: str) -> DatasetRevisionListDto | None:
        """Revisions. `GET /v2/datasets/{datasetId}/revisions`"""
        return self._client._invoke(_revisions_op, dataset_id=dataset_id)

    def create_revision(
        self, dataset_id: str, body: CreateDatasetRevisionDto
    ) -> DatasetRevisionDto | None:
        """Create revision. `POST /v2/datasets/{datasetId}/revisions`"""
        return self._client._invoke(_create_revision_op, dataset_id=dataset_id, body=body)

    def from_traces(
        self, dataset_id: str, body: TraceDatasetSelectionDto
    ) -> DatasetRevisionDto | None:
        """From traces. `POST /v2/datasets/{datasetId}/revisions/from-traces`"""
        return self._client._invoke(_from_traces_op, dataset_id=dataset_id, body=body)

    def import_revision(
        self, dataset_id: str, body: ImportDatasetRevisionDto
    ) -> DatasetRevisionDto | None:
        """Import revision. `POST /v2/datasets/{datasetId}/revisions/import`"""
        return self._client._invoke(_import_revision_op, dataset_id=dataset_id, body=body)

    def export_revision(
        self, dataset_id: str, format: str, revision: str
    ) -> DatasetExportDto | None:
        """Export revision. `GET /v2/datasets/{datasetId}/revisions/{revision}/export/{format}`"""
        return self._client._invoke(
            _export_revision_op, dataset_id=dataset_id, format=format, revision=revision
        )

    def items(self, dataset_id: str, revision: str) -> DatasetRevisionItemsDto | None:
        """Items. `GET /v2/datasets/{datasetId}/revisions/{revision}/items`"""
        return self._client._invoke(_items_op, dataset_id=dataset_id, revision=revision)


class AsyncDatasets:
    """Async sibling of :class:`Datasets`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> DatasetListDto | None:
        """See :meth:`Datasets.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateDatasetDto) -> DatasetDto | None:
        """See :meth:`Datasets.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, dataset_id: str) -> DatasetDeleteDto | None:
        """See :meth:`Datasets.delete`."""
        return await self._client._invoke(_remove_op, dataset_id=dataset_id)

    async def get(self, dataset_id: str) -> DatasetDto | None:
        """See :meth:`Datasets.get`."""
        return await self._client._invoke(_get_op, dataset_id=dataset_id)

    async def revisions(self, dataset_id: str) -> DatasetRevisionListDto | None:
        """See :meth:`Datasets.revisions`."""
        return await self._client._invoke(_revisions_op, dataset_id=dataset_id)

    async def create_revision(
        self, dataset_id: str, body: CreateDatasetRevisionDto
    ) -> DatasetRevisionDto | None:
        """See :meth:`Datasets.create_revision`."""
        return await self._client._invoke(_create_revision_op, dataset_id=dataset_id, body=body)

    async def from_traces(
        self, dataset_id: str, body: TraceDatasetSelectionDto
    ) -> DatasetRevisionDto | None:
        """See :meth:`Datasets.from_traces`."""
        return await self._client._invoke(_from_traces_op, dataset_id=dataset_id, body=body)

    async def import_revision(
        self, dataset_id: str, body: ImportDatasetRevisionDto
    ) -> DatasetRevisionDto | None:
        """See :meth:`Datasets.import_revision`."""
        return await self._client._invoke(_import_revision_op, dataset_id=dataset_id, body=body)

    async def export_revision(
        self, dataset_id: str, format: str, revision: str
    ) -> DatasetExportDto | None:
        """See :meth:`Datasets.export_revision`."""
        return await self._client._invoke(
            _export_revision_op, dataset_id=dataset_id, format=format, revision=revision
        )

    async def items(self, dataset_id: str, revision: str) -> DatasetRevisionItemsDto | None:
        """See :meth:`Datasets.items`."""
        return await self._client._invoke(_items_op, dataset_id=dataset_id, revision=revision)
