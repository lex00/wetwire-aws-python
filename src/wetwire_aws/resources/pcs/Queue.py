"""PropertyTypes for AWS::PCS::Queue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComputeNodeGroupConfiguration(PropertyType):
    compute_node_group_id: DslValue[str] | None = None


@dataclass
class ErrorInfo(PropertyType):
    code: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class SlurmConfiguration(PropertyType):
    slurm_custom_settings: list[DslValue[SlurmCustomSetting]] = field(
        default_factory=list
    )


@dataclass
class SlurmCustomSetting(PropertyType):
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None
