"""PropertyTypes for AWS::PCS::ComputeNodeGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomLaunchTemplate(PropertyType):
    version: str | None = None
    template_id: str | None = None


@dataclass
class ErrorInfo(PropertyType):
    code: str | None = None
    message: str | None = None


@dataclass
class InstanceConfig(PropertyType):
    instance_type: str | None = None


@dataclass
class ScalingConfiguration(PropertyType):
    max_instance_count: int | None = None
    min_instance_count: int | None = None


@dataclass
class SlurmConfiguration(PropertyType):
    slurm_custom_settings: list[SlurmCustomSetting] = field(default_factory=list)


@dataclass
class SlurmCustomSetting(PropertyType):
    parameter_name: str | None = None
    parameter_value: str | None = None


@dataclass
class SpotOptions(PropertyType):
    allocation_strategy: str | None = None
