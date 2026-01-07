"""PropertyTypes for AWS::Backup::Framework."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ControlInputParameter(PropertyType):
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None


@dataclass
class ControlScope(PropertyType):
    compliance_resource_ids: list[DslValue[str]] = field(default_factory=list)
    compliance_resource_types: list[DslValue[str]] = field(default_factory=list)
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class FrameworkControl(PropertyType):
    control_name: DslValue[str] | None = None
    control_input_parameters: list[DslValue[ControlInputParameter]] = field(
        default_factory=list
    )
    control_scope: DslValue[ControlScope] | None = None
