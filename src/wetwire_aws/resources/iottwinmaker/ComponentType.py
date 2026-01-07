"""PropertyTypes for AWS::IoTTwinMaker::ComponentType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CompositeComponentType(PropertyType):
    component_type_id: DslValue[str] | None = None


@dataclass
class DataConnector(PropertyType):
    is_native: DslValue[bool] | None = None
    lambda_: DslValue[LambdaFunction] | None = None


@dataclass
class DataType(PropertyType):
    type_: DslValue[str] | None = None
    allowed_values: list[DslValue[DataValue]] = field(default_factory=list)
    nested_type: DslValue[DataType] | None = None
    relationship: DslValue[Relationship] | None = None
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
class Error(PropertyType):
    code: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class Function(PropertyType):
    implemented_by: DslValue[DataConnector] | None = None
    required_properties: list[DslValue[str]] = field(default_factory=list)
    scope: DslValue[str] | None = None


@dataclass
class LambdaFunction(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class PropertyDefinition(PropertyType):
    configurations: dict[str, DslValue[str]] = field(default_factory=dict)
    data_type: DslValue[DataType] | None = None
    default_value: DslValue[DataValue] | None = None
    is_external_id: DslValue[bool] | None = None
    is_required_in_entity: DslValue[bool] | None = None
    is_stored_externally: DslValue[bool] | None = None
    is_time_series: DslValue[bool] | None = None


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
