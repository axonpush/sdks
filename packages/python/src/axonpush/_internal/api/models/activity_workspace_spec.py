from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_workspace_spec_schema_version import ActivityWorkspaceSpecSchemaVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_alert import ActivityAlert
    from ..models.activity_entity_definition import ActivityEntityDefinition
    from ..models.activity_funnel import ActivityFunnel
    from ..models.activity_mapping import ActivityMapping
    from ..models.activity_template_ref import ActivityTemplateRef
    from ..models.activity_widget import ActivityWidget


T = TypeVar("T", bound="ActivityWorkspaceSpec")


@_attrs_define
class ActivityWorkspaceSpec:
    """
    Attributes:
        entities (list[ActivityEntityDefinition] | None):
        mappings (list[ActivityMapping] | None):
        name (str):
        schema_version (ActivityWorkspaceSpecSchemaVersion):
        widgets (list[ActivityWidget] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        alerts (list[ActivityAlert] | None | Unset):
        description (str | Unset):
        funnels (list[ActivityFunnel] | None | Unset):
        template (ActivityTemplateRef | Unset):
    """

    entities: list[ActivityEntityDefinition] | None
    mappings: list[ActivityMapping] | None
    name: str
    schema_version: ActivityWorkspaceSpecSchemaVersion
    widgets: list[ActivityWidget] | None
    schema: str | Unset = UNSET
    alerts: list[ActivityAlert] | None | Unset = UNSET
    description: str | Unset = UNSET
    funnels: list[ActivityFunnel] | None | Unset = UNSET
    template: ActivityTemplateRef | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_alert import ActivityAlert
        from ..models.activity_entity_definition import ActivityEntityDefinition
        from ..models.activity_funnel import ActivityFunnel
        from ..models.activity_mapping import ActivityMapping
        from ..models.activity_template_ref import ActivityTemplateRef
        from ..models.activity_widget import ActivityWidget

        entities: list[dict[str, Any]] | None
        if isinstance(self.entities, list):
            entities = []
            for entities_type_0_item_data in self.entities:
                entities_type_0_item = entities_type_0_item_data.to_dict()
                entities.append(entities_type_0_item)

        else:
            entities = self.entities

        mappings: list[dict[str, Any]] | None
        if isinstance(self.mappings, list):
            mappings = []
            for mappings_type_0_item_data in self.mappings:
                mappings_type_0_item = mappings_type_0_item_data.to_dict()
                mappings.append(mappings_type_0_item)

        else:
            mappings = self.mappings

        name = self.name

        schema_version = self.schema_version.value

        widgets: list[dict[str, Any]] | None
        if isinstance(self.widgets, list):
            widgets = []
            for widgets_type_0_item_data in self.widgets:
                widgets_type_0_item = widgets_type_0_item_data.to_dict()
                widgets.append(widgets_type_0_item)

        else:
            widgets = self.widgets

        schema = self.schema

        alerts: list[dict[str, Any]] | None | Unset
        if isinstance(self.alerts, Unset):
            alerts = UNSET
        elif isinstance(self.alerts, list):
            alerts = []
            for alerts_type_0_item_data in self.alerts:
                alerts_type_0_item = alerts_type_0_item_data.to_dict()
                alerts.append(alerts_type_0_item)

        else:
            alerts = self.alerts

        description = self.description

        funnels: list[dict[str, Any]] | None | Unset
        if isinstance(self.funnels, Unset):
            funnels = UNSET
        elif isinstance(self.funnels, list):
            funnels = []
            for funnels_type_0_item_data in self.funnels:
                funnels_type_0_item = funnels_type_0_item_data.to_dict()
                funnels.append(funnels_type_0_item)

        else:
            funnels = self.funnels

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entities": entities,
                "mappings": mappings,
                "name": name,
                "schemaVersion": schema_version,
                "widgets": widgets,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if description is not UNSET:
            field_dict["description"] = description
        if funnels is not UNSET:
            field_dict["funnels"] = funnels
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_alert import ActivityAlert
        from ..models.activity_entity_definition import ActivityEntityDefinition
        from ..models.activity_funnel import ActivityFunnel
        from ..models.activity_mapping import ActivityMapping
        from ..models.activity_template_ref import ActivityTemplateRef
        from ..models.activity_widget import ActivityWidget

        d = dict(src_dict)

        def _parse_entities(data: object) -> list[ActivityEntityDefinition] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entities_type_0 = []
                _entities_type_0 = data
                for entities_type_0_item_data in _entities_type_0:
                    entities_type_0_item = ActivityEntityDefinition.from_dict(
                        entities_type_0_item_data
                    )

                    entities_type_0.append(entities_type_0_item)

                return entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityEntityDefinition] | None, data)

        entities = _parse_entities(d.pop("entities"))

        def _parse_mappings(data: object) -> list[ActivityMapping] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mappings_type_0 = []
                _mappings_type_0 = data
                for mappings_type_0_item_data in _mappings_type_0:
                    mappings_type_0_item = ActivityMapping.from_dict(mappings_type_0_item_data)

                    mappings_type_0.append(mappings_type_0_item)

                return mappings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityMapping] | None, data)

        mappings = _parse_mappings(d.pop("mappings"))

        name = d.pop("name")

        schema_version = ActivityWorkspaceSpecSchemaVersion(d.pop("schemaVersion"))

        def _parse_widgets(data: object) -> list[ActivityWidget] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                widgets_type_0 = []
                _widgets_type_0 = data
                for widgets_type_0_item_data in _widgets_type_0:
                    widgets_type_0_item = ActivityWidget.from_dict(widgets_type_0_item_data)

                    widgets_type_0.append(widgets_type_0_item)

                return widgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityWidget] | None, data)

        widgets = _parse_widgets(d.pop("widgets"))

        schema = d.pop("$schema", UNSET)

        def _parse_alerts(data: object) -> list[ActivityAlert] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alerts_type_0 = []
                _alerts_type_0 = data
                for alerts_type_0_item_data in _alerts_type_0:
                    alerts_type_0_item = ActivityAlert.from_dict(alerts_type_0_item_data)

                    alerts_type_0.append(alerts_type_0_item)

                return alerts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityAlert] | None | Unset, data)

        alerts = _parse_alerts(d.pop("alerts", UNSET))

        description = d.pop("description", UNSET)

        def _parse_funnels(data: object) -> list[ActivityFunnel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funnels_type_0 = []
                _funnels_type_0 = data
                for funnels_type_0_item_data in _funnels_type_0:
                    funnels_type_0_item = ActivityFunnel.from_dict(funnels_type_0_item_data)

                    funnels_type_0.append(funnels_type_0_item)

                return funnels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityFunnel] | None | Unset, data)

        funnels = _parse_funnels(d.pop("funnels", UNSET))

        _template = d.pop("template", UNSET)
        template: ActivityTemplateRef | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = ActivityTemplateRef.from_dict(_template)

        activity_workspace_spec = cls(
            entities=entities,
            mappings=mappings,
            name=name,
            schema_version=schema_version,
            widgets=widgets,
            schema=schema,
            alerts=alerts,
            description=description,
            funnels=funnels,
            template=template,
        )

        return activity_workspace_spec
