"""PropertyTypes for AWS::Athena::CapacityReservation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityAssignment(PropertyType):
    workgroup_names: list[String] = field(default_factory=list)


@dataclass
class CapacityAssignmentConfiguration(PropertyType):
    capacity_assignments: list[CapacityAssignment] = field(default_factory=list)
