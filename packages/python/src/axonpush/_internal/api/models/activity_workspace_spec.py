from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_alert import ActivityAlert
    from ..models.activity_attribute import ActivityAttribute
    from ..models.activity_entity_definition import ActivityEntityDefinition
    from ..models.activity_funnel import ActivityFunnel
    from ..models.activity_template_ref import ActivityTemplateRef
    from ..models.activity_view import ActivityView


T = TypeVar("T", bound="ActivityWorkspaceSpec")


@_attrs_define
class ActivityWorkspaceSpec:
    """
    Attributes:
        name (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        alerts (list[ActivityAlert] | None | Unset):
        attributes (list[ActivityAttribute] | None | Unset):
        description (str | Unset):
        entities (list[ActivityEntityDefinition] | None | Unset):
        funnels (list[ActivityFunnel] | None | Unset):
        heartbeat (str | Unset): Event name the source emits as a liveness heartbeat; its attributes are shown as source
            health
        schema_version (int | Unset):
        template (ActivityTemplateRef | Unset):
        views (list[ActivityView] | None | Unset):
    """

    name: str
    schema: str | Unset = UNSET
    alerts: list[ActivityAlert] | None | Unset = UNSET
    attributes: list[ActivityAttribute] | None | Unset = UNSET
    description: str | Unset = UNSET
    entities: list[ActivityEntityDefinition] | None | Unset = UNSET
    funnels: list[ActivityFunnel] | None | Unset = UNSET
    heartbeat: str | Unset = UNSET
    schema_version: int | Unset = UNSET
    template: ActivityTemplateRef | Unset = UNSET
    views: list[ActivityView] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_alert import ActivityAlert
        from ..models.activity_attribute import ActivityAttribute
        from ..models.activity_entity_definition import ActivityEntityDefinition
        from ..models.activity_funnel import ActivityFunnel
        from ..models.activity_template_ref import ActivityTemplateRef
        from ..models.activity_view import ActivityView

        name = self.name

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

        attributes: list[dict[str, Any]] | None | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, list):
            attributes = []
            for attributes_type_0_item_data in self.attributes:
                attributes_type_0_item = attributes_type_0_item_data.to_dict()
                attributes.append(attributes_type_0_item)

        else:
            attributes = self.attributes

        description = self.description

        entities: list[dict[str, Any]] | None | Unset
        if isinstance(self.entities, Unset):
            entities = UNSET
        elif isinstance(self.entities, list):
            entities = []
            for entities_type_0_item_data in self.entities:
                entities_type_0_item = entities_type_0_item_data.to_dict()
                entities.append(entities_type_0_item)

        else:
            entities = self.entities

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

        heartbeat = self.heartbeat

        schema_version = self.schema_version

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        views: list[dict[str, Any]] | None | Unset
        if isinstance(self.views, Unset):
            views = UNSET
        elif isinstance(self.views, list):
            views = []
            for views_type_0_item_data in self.views:
                views_type_0_item = views_type_0_item_data.to_dict()
                views.append(views_type_0_item)

        else:
            views = self.views

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if description is not UNSET:
            field_dict["description"] = description
        if entities is not UNSET:
            field_dict["entities"] = entities
        if funnels is not UNSET:
            field_dict["funnels"] = funnels
        if heartbeat is not UNSET:
            field_dict["heartbeat"] = heartbeat
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version
        if template is not UNSET:
            field_dict["template"] = template
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_alert import ActivityAlert
        from ..models.activity_attribute import ActivityAttribute
        from ..models.activity_entity_definition import ActivityEntityDefinition
        from ..models.activity_funnel import ActivityFunnel
        from ..models.activity_template_ref import ActivityTemplateRef
        from ..models.activity_view import ActivityView

        d = dict(src_dict)
        name = d.pop("name")

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

        def _parse_attributes(data: object) -> list[ActivityAttribute] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attributes_type_0 = []
                _attributes_type_0 = data
                for attributes_type_0_item_data in _attributes_type_0:
                    attributes_type_0_item = ActivityAttribute.from_dict(
                        attributes_type_0_item_data
                    )

                    attributes_type_0.append(attributes_type_0_item)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityAttribute] | None | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        description = d.pop("description", UNSET)

        def _parse_entities(data: object) -> list[ActivityEntityDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(list[ActivityEntityDefinition] | None | Unset, data)

        entities = _parse_entities(d.pop("entities", UNSET))

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

        heartbeat = d.pop("heartbeat", UNSET)

        schema_version = d.pop("schemaVersion", UNSET)

        _template = d.pop("template", UNSET)
        template: ActivityTemplateRef | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = ActivityTemplateRef.from_dict(_template)

        def _parse_views(data: object) -> list[ActivityView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                views_type_0 = []
                _views_type_0 = data
                for views_type_0_item_data in _views_type_0:
                    views_type_0_item = ActivityView.from_dict(views_type_0_item_data)

                    views_type_0.append(views_type_0_item)

                return views_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityView] | None | Unset, data)

        views = _parse_views(d.pop("views", UNSET))

        activity_workspace_spec = cls(
            name=name,
            schema=schema,
            alerts=alerts,
            attributes=attributes,
            description=description,
            entities=entities,
            funnels=funnels,
            heartbeat=heartbeat,
            schema_version=schema_version,
            template=template,
            views=views,
        )

        return activity_workspace_spec
