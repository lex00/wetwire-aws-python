"""PropertyTypes for AWS::PCS::Queue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComputeNodeGroupConfiguration(PropertyType):
    compute_node_group_id: str | None = None


@dataclass
class ErrorInfo(PropertyType):
    code: str | None = None
    message: str | None = None


@dataclass
class SlurmConfiguration(PropertyType):
    slurm_custom_settings: list[SlurmCustomSetting] = field(default_factory=list)


@dataclass
class SlurmCustomSetting(PropertyType):
    parameter_name: str | None = None
    parameter_value: str | None = None
