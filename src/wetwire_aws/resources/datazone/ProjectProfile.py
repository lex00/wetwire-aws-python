"""PropertyTypes for AWS::DataZone::ProjectProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsAccount(PropertyType):
    aws_account_id: DslValue[str] | None = None


@dataclass
class EnvironmentConfiguration(PropertyType):
    aws_region: DslValue[Region] | None = None
    environment_blueprint_id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    aws_account: DslValue[AwsAccount] | None = None
    configuration_parameters: (
        DslValue[EnvironmentConfigurationParametersDetails] | None
    ) = None
    deployment_mode: DslValue[str] | None = None
    deployment_order: DslValue[float] | None = None
    description: DslValue[str] | None = None
    environment_configuration_id: DslValue[str] | None = None


@dataclass
class EnvironmentConfigurationParameter(PropertyType):
    is_editable: DslValue[bool] | None = None
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EnvironmentConfigurationParametersDetails(PropertyType):
    parameter_overrides: list[DslValue[EnvironmentConfigurationParameter]] = field(
        default_factory=list
    )
    resolved_parameters: list[DslValue[EnvironmentConfigurationParameter]] = field(
        default_factory=list
    )
    ssm_path: DslValue[str] | None = None


@dataclass
class Region(PropertyType):
    region_name: DslValue[str] | None = None
