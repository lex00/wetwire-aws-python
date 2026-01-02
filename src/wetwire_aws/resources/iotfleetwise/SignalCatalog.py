"""PropertyTypes for AWS::IoTFleetWise::SignalCatalog."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Actuator(PropertyType):
    data_type: str | None = None
    fully_qualified_name: str | None = None
    allowed_values: list[String] = field(default_factory=list)
    assigned_value: str | None = None
    description: str | None = None
    max: float | None = None
    min: float | None = None
    unit: str | None = None


@dataclass
class Attribute(PropertyType):
    data_type: str | None = None
    fully_qualified_name: str | None = None
    allowed_values: list[String] = field(default_factory=list)
    assigned_value: str | None = None
    default_value: str | None = None
    description: str | None = None
    max: float | None = None
    min: float | None = None
    unit: str | None = None


@dataclass
class Branch(PropertyType):
    fully_qualified_name: str | None = None
    description: str | None = None


@dataclass
class Node(PropertyType):
    actuator: Actuator | None = None
    attribute: Attribute | None = None
    branch: Branch | None = None
    sensor: Sensor | None = None


@dataclass
class NodeCounts(PropertyType):
    total_actuators: float | None = None
    total_attributes: float | None = None
    total_branches: float | None = None
    total_nodes: float | None = None
    total_sensors: float | None = None


@dataclass
class Sensor(PropertyType):
    data_type: str | None = None
    fully_qualified_name: str | None = None
    allowed_values: list[String] = field(default_factory=list)
    description: str | None = None
    max: float | None = None
    min: float | None = None
    unit: str | None = None
