"""PropertyTypes for AWS::Backup::Framework."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ControlInputParameter(PropertyType):
    parameter_name: str | None = None
    parameter_value: str | None = None


@dataclass
class ControlScope(PropertyType):
    compliance_resource_ids: list[String] = field(default_factory=list)
    compliance_resource_types: list[String] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)


@dataclass
class FrameworkControl(PropertyType):
    control_name: str | None = None
    control_input_parameters: list[ControlInputParameter] = field(default_factory=list)
    control_scope: ControlScope | None = None
