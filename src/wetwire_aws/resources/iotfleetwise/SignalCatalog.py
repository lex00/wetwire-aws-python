"""PropertyTypes for AWS::IoTFleetWise::SignalCatalog."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Actuator(PropertyType):
    data_type: DslValue[str] | None = None
    fully_qualified_name: DslValue[str] | None = None
    allowed_values: list[DslValue[str]] = field(default_factory=list)
    assigned_value: DslValue[str] | None = None
    description: DslValue[str] | None = None
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None
    unit: DslValue[str] | None = None


@dataclass
class Attribute(PropertyType):
    data_type: DslValue[str] | None = None
    fully_qualified_name: DslValue[str] | None = None
    allowed_values: list[DslValue[str]] = field(default_factory=list)
    assigned_value: DslValue[str] | None = None
    default_value: DslValue[str] | None = None
    description: DslValue[str] | None = None
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None
    unit: DslValue[str] | None = None


@dataclass
class Branch(PropertyType):
    fully_qualified_name: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class Node(PropertyType):
    actuator: DslValue[Actuator] | None = None
    attribute: DslValue[Attribute] | None = None
    branch: DslValue[Branch] | None = None
    sensor: DslValue[Sensor] | None = None


@dataclass
class NodeCounts(PropertyType):
    total_actuators: DslValue[float] | None = None
    total_attributes: DslValue[float] | None = None
    total_branches: DslValue[float] | None = None
    total_nodes: DslValue[float] | None = None
    total_sensors: DslValue[float] | None = None


@dataclass
class Sensor(PropertyType):
    data_type: DslValue[str] | None = None
    fully_qualified_name: DslValue[str] | None = None
    allowed_values: list[DslValue[str]] = field(default_factory=list)
    description: DslValue[str] | None = None
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None
    unit: DslValue[str] | None = None
