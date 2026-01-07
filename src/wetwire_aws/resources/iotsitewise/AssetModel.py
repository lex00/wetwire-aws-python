"""PropertyTypes for AWS::IoTSiteWise::AssetModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssetModelCompositeModel(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    composed_asset_model_id: DslValue[str] | None = None
    composite_model_properties: list[DslValue[AssetModelProperty]] = field(
        default_factory=list
    )
    description: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    id: DslValue[str] | None = None
    parent_asset_model_composite_model_external_id: DslValue[str] | None = None
    path: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AssetModelHierarchy(PropertyType):
    child_asset_model_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    id: DslValue[str] | None = None
    logical_id: DslValue[str] | None = None


@dataclass
class AssetModelProperty(PropertyType):
    data_type: DslValue[str] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[PropertyType] | None = None
    data_type_spec: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    id: DslValue[str] | None = None
    logical_id: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class Attribute(PropertyType):
    default_value: DslValue[str] | None = None


@dataclass
class EnforcedAssetModelInterfacePropertyMapping(PropertyType):
    interface_asset_model_property_external_id: DslValue[str] | None = None
    asset_model_property_external_id: DslValue[str] | None = None
    asset_model_property_logical_id: DslValue[str] | None = None


@dataclass
class EnforcedAssetModelInterfaceRelationship(PropertyType):
    interface_asset_model_id: DslValue[str] | None = None
    property_mappings: list[DslValue[EnforcedAssetModelInterfacePropertyMapping]] = (
        field(default_factory=list)
    )


@dataclass
class ExpressionVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[VariableValue] | None = None


@dataclass
class Metric(PropertyType):
    expression: DslValue[str] | None = None
    variables: list[DslValue[ExpressionVariable]] = field(default_factory=list)
    window: DslValue[MetricWindow] | None = None


@dataclass
class MetricWindow(PropertyType):
    tumbling: DslValue[TumblingWindow] | None = None


@dataclass
class PropertyPathDefinition(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class PropertyTypeDefinition(PropertyType):
    type_name: DslValue[str] | None = None
    attribute: DslValue[Attribute] | None = None
    metric: DslValue[Metric] | None = None
    transform: DslValue[Transform] | None = None


@dataclass
class Transform(PropertyType):
    expression: DslValue[str] | None = None
    variables: list[DslValue[ExpressionVariable]] = field(default_factory=list)


@dataclass
class TumblingWindow(PropertyType):
    interval: DslValue[str] | None = None
    offset: DslValue[str] | None = None


@dataclass
class VariableValue(PropertyType):
    hierarchy_external_id: DslValue[str] | None = None
    hierarchy_id: DslValue[str] | None = None
    hierarchy_logical_id: DslValue[str] | None = None
    property_external_id: DslValue[str] | None = None
    property_id: DslValue[str] | None = None
    property_logical_id: DslValue[str] | None = None
    property_path: list[DslValue[PropertyPathDefinition]] = field(default_factory=list)
