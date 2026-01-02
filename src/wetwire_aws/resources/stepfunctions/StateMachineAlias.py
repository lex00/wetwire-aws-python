"""PropertyTypes for AWS::StepFunctions::StateMachineAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeploymentPreference(PropertyType):
    state_machine_version_arn: str | None = None
    type_: str | None = None
    alarms: list[String] = field(default_factory=list)
    interval: int | None = None
    percentage: int | None = None


@dataclass
class RoutingConfigurationVersion(PropertyType):
    state_machine_version_arn: str | None = None
    weight: int | None = None
