"""PropertyTypes for AWS::IoTTwinMaker::Entity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Component(PropertyType):
    component_name: str | None = None
    component_type_id: str | None = None
    defined_in: str | None = None
    description: str | None = None
    properties: dict[str, Property] = field(default_factory=dict)
    property_groups: dict[str, PropertyGroup] = field(default_factory=dict)
    status: Status | None = None


@dataclass
class CompositeComponent(PropertyType):
    component_name: str | None = None
    component_path: str | None = None
    component_type_id: str | None = None
    description: str | None = None
    properties: dict[str, Property] = field(default_factory=dict)
    property_groups: dict[str, PropertyGroup] = field(default_factory=dict)
    status: Status | None = None


@dataclass
class DataType(PropertyType):
    allowed_values: list[DataValue] = field(default_factory=list)
    nested_type: DataType | None = None
    relationship: Relationship | None = None
    type_: str | None = None
    unit_of_measure: str | None = None


@dataclass
class DataValue(PropertyType):
    boolean_value: bool | None = None
    double_value: float | None = None
    expression: str | None = None
    integer_value: int | None = None
    list_value: list[DataValue] = field(default_factory=list)
    long_value: float | None = None
    map_value: dict[str, DataValue] = field(default_factory=dict)
    relationship_value: RelationshipValue | None = None
    string_value: str | None = None


@dataclass
class Definition(PropertyType):
    configuration: dict[str, String] = field(default_factory=dict)
    data_type: DataType | None = None
    default_value: DataValue | None = None
    is_external_id: bool | None = None
    is_final: bool | None = None
    is_imported: bool | None = None
    is_inherited: bool | None = None
    is_required_in_entity: bool | None = None
    is_stored_externally: bool | None = None
    is_time_series: bool | None = None


@dataclass
class Error(PropertyType):
    code: str | None = None
    message: str | None = None


@dataclass
class Property(PropertyType):
    definition: Definition | None = None
    value: DataValue | None = None


@dataclass
class PropertyGroup(PropertyType):
    group_type: str | None = None
    property_names: list[String] = field(default_factory=list)


@dataclass
class Relationship(PropertyType):
    relationship_type: str | None = None
    target_component_type_id: str | None = None


@dataclass
class RelationshipValue(PropertyType):
    target_component_name: str | None = None
    target_entity_id: str | None = None


@dataclass
class Status(PropertyType):
    error: Error | None = None
    state: str | None = None
