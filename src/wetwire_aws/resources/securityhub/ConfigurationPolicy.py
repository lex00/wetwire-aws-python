"""PropertyTypes for AWS::SecurityHub::ConfigurationPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ParameterConfiguration(PropertyType):
    value_type: str | None = None
    value: ParameterValue | None = None


@dataclass
class ParameterValue(PropertyType):
    boolean: bool | None = None
    double: float | None = None
    enum: str | None = None
    enum_list: list[String] = field(default_factory=list)
    integer: int | None = None
    integer_list: list[Integer] = field(default_factory=list)
    string: str | None = None
    string_list: list[String] = field(default_factory=list)


@dataclass
class Policy(PropertyType):
    security_hub: SecurityHubPolicy | None = None


@dataclass
class SecurityControlCustomParameter(PropertyType):
    parameters: dict[str, ParameterConfiguration] = field(default_factory=dict)
    security_control_id: str | None = None


@dataclass
class SecurityControlsConfiguration(PropertyType):
    disabled_security_control_identifiers: list[String] = field(default_factory=list)
    enabled_security_control_identifiers: list[String] = field(default_factory=list)
    security_control_custom_parameters: list[SecurityControlCustomParameter] = field(
        default_factory=list
    )


@dataclass
class SecurityHubPolicy(PropertyType):
    enabled_standard_identifiers: list[String] = field(default_factory=list)
    security_controls_configuration: SecurityControlsConfiguration | None = None
    service_enabled: bool | None = None
