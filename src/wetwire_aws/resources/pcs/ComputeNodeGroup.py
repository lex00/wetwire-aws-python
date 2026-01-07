"""PropertyTypes for AWS::PCS::ComputeNodeGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomLaunchTemplate(PropertyType):
    version: DslValue[str] | None = None
    template_id: DslValue[str] | None = None


@dataclass
class ErrorInfo(PropertyType):
    code: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class InstanceConfig(PropertyType):
    instance_type: DslValue[str] | None = None


@dataclass
class ScalingConfiguration(PropertyType):
    max_instance_count: DslValue[int] | None = None
    min_instance_count: DslValue[int] | None = None


@dataclass
class SlurmConfiguration(PropertyType):
    slurm_custom_settings: list[DslValue[SlurmCustomSetting]] = field(
        default_factory=list
    )


@dataclass
class SlurmCustomSetting(PropertyType):
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None


@dataclass
class SpotOptions(PropertyType):
    allocation_strategy: DslValue[str] | None = None
