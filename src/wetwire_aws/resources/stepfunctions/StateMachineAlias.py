"""PropertyTypes for AWS::StepFunctions::StateMachineAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeploymentPreference(PropertyType):
    state_machine_version_arn: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    alarms: list[DslValue[str]] = field(default_factory=list)
    interval: DslValue[int] | None = None
    percentage: DslValue[int] | None = None


@dataclass
class RoutingConfigurationVersion(PropertyType):
    state_machine_version_arn: DslValue[str] | None = None
    weight: DslValue[int] | None = None
