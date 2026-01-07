"""PropertyTypes for AWS::IoTTwinMaker::Entity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Component(PropertyType):
    component_name: DslValue[str] | None = None
    component_type_id: DslValue[str] | None = None
    defined_in: DslValue[str] | None = None
    description: DslValue[str] | None = None
    properties: dict[str, DslValue[Property]] = field(default_factory=dict)
    property_groups: dict[str, DslValue[PropertyGroup]] = field(default_factory=dict)
    status: DslValue[Status] | None = None


@dataclass
class CompositeComponent(PropertyType):
    component_name: DslValue[str] | None = None
    component_path: DslValue[str] | None = None
    component_type_id: DslValue[str] | None = None
    description: DslValue[str] | None = None
    properties: dict[str, DslValue[Property]] = field(default_factory=dict)
    property_groups: dict[str, DslValue[PropertyGroup]] = field(default_factory=dict)
    status: DslValue[Status] | None = None


@dataclass
class DataType(PropertyType):
    allowed_values: list[DslValue[DataValue]] = field(default_factory=list)
    nested_type: DslValue[DataType] | None = None
    relationship: DslValue[Relationship] | None = None
    type_: DslValue[str] | None = None
    unit_of_measure: DslValue[str] | None = None


@dataclass
class DataValue(PropertyType):
    boolean_value: DslValue[bool] | None = None
    double_value: DslValue[float] | None = None
    expression: DslValue[str] | None = None
    integer_value: DslValue[int] | None = None
    list_value: list[DslValue[DataValue]] = field(default_factory=list)
    long_value: DslValue[float] | None = None
    map_value: dict[str, DslValue[DataValue]] = field(default_factory=dict)
    relationship_value: DslValue[RelationshipValue] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class Definition(PropertyType):
    configuration: dict[str, DslValue[str]] = field(default_factory=dict)
    data_type: DslValue[DataType] | None = None
    default_value: DslValue[DataValue] | None = None
    is_external_id: DslValue[bool] | None = None
    is_final: DslValue[bool] | None = None
    is_imported: DslValue[bool] | None = None
    is_inherited: DslValue[bool] | None = None
    is_required_in_entity: DslValue[bool] | None = None
    is_stored_externally: DslValue[bool] | None = None
    is_time_series: DslValue[bool] | None = None


@dataclass
class Error(PropertyType):
    code: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class Property(PropertyType):
    definition: DslValue[Definition] | None = None
    value: DslValue[DataValue] | None = None


@dataclass
class PropertyGroup(PropertyType):
    group_type: DslValue[str] | None = None
    property_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Relationship(PropertyType):
    relationship_type: DslValue[str] | None = None
    target_component_type_id: DslValue[str] | None = None


@dataclass
class RelationshipValue(PropertyType):
    target_component_name: DslValue[str] | None = None
    target_entity_id: DslValue[str] | None = None


@dataclass
class Status(PropertyType):
    error: DslValue[Error] | None = None
    state: DslValue[str] | None = None
