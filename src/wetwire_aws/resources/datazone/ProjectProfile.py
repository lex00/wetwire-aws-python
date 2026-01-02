"""PropertyTypes for AWS::DataZone::ProjectProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsAccount(PropertyType):
    aws_account_id: str | None = None


@dataclass
class EnvironmentConfiguration(PropertyType):
    aws_region: Region | None = None
    environment_blueprint_id: str | None = None
    name: str | None = None
    aws_account: AwsAccount | None = None
    configuration_parameters: EnvironmentConfigurationParametersDetails | None = None
    deployment_mode: str | None = None
    deployment_order: float | None = None
    description: str | None = None
    environment_configuration_id: str | None = None


@dataclass
class EnvironmentConfigurationParameter(PropertyType):
    is_editable: bool | None = None
    name: str | None = None
    value: str | None = None


@dataclass
class EnvironmentConfigurationParametersDetails(PropertyType):
    parameter_overrides: list[EnvironmentConfigurationParameter] = field(
        default_factory=list
    )
    resolved_parameters: list[EnvironmentConfigurationParameter] = field(
        default_factory=list
    )
    ssm_path: str | None = None


@dataclass
class Region(PropertyType):
    region_name: str | None = None
