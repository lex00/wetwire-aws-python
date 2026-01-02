"""PropertyTypes for AWS::IoTSiteWise::AssetModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssetModelCompositeModel(PropertyType):
    name: str | None = None
    type_: str | None = None
    composed_asset_model_id: str | None = None
    composite_model_properties: list[AssetModelProperty] = field(default_factory=list)
    description: str | None = None
    external_id: str | None = None
    id: str | None = None
    parent_asset_model_composite_model_external_id: str | None = None
    path: list[String] = field(default_factory=list)


@dataclass
class AssetModelHierarchy(PropertyType):
    child_asset_model_id: str | None = None
    name: str | None = None
    external_id: str | None = None
    id: str | None = None
    logical_id: str | None = None


@dataclass
class AssetModelProperty(PropertyType):
    data_type: str | None = None
    name: str | None = None
    type_: PropertyType | None = None
    data_type_spec: str | None = None
    external_id: str | None = None
    id: str | None = None
    logical_id: str | None = None
    unit: str | None = None


@dataclass
class Attribute(PropertyType):
    default_value: str | None = None


@dataclass
class EnforcedAssetModelInterfacePropertyMapping(PropertyType):
    interface_asset_model_property_external_id: str | None = None
    asset_model_property_external_id: str | None = None
    asset_model_property_logical_id: str | None = None


@dataclass
class EnforcedAssetModelInterfaceRelationship(PropertyType):
    interface_asset_model_id: str | None = None
    property_mappings: list[EnforcedAssetModelInterfacePropertyMapping] = field(
        default_factory=list
    )


@dataclass
class ExpressionVariable(PropertyType):
    name: str | None = None
    value: VariableValue | None = None


@dataclass
class Metric(PropertyType):
    expression: str | None = None
    variables: list[ExpressionVariable] = field(default_factory=list)
    window: MetricWindow | None = None


@dataclass
class MetricWindow(PropertyType):
    tumbling: TumblingWindow | None = None


@dataclass
class PropertyPathDefinition(PropertyType):
    name: str | None = None


@dataclass
class PropertyTypeDefinition(PropertyType):
    type_name: str | None = None
    attribute: Attribute | None = None
    metric: Metric | None = None
    transform: Transform | None = None


@dataclass
class Transform(PropertyType):
    expression: str | None = None
    variables: list[ExpressionVariable] = field(default_factory=list)


@dataclass
class TumblingWindow(PropertyType):
    interval: str | None = None
    offset: str | None = None


@dataclass
class VariableValue(PropertyType):
    hierarchy_external_id: str | None = None
    hierarchy_id: str | None = None
    hierarchy_logical_id: str | None = None
    property_external_id: str | None = None
    property_id: str | None = None
    property_logical_id: str | None = None
    property_path: list[PropertyPathDefinition] = field(default_factory=list)
