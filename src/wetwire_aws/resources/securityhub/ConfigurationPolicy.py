"""PropertyTypes for AWS::SecurityHub::ConfigurationPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ParameterConfiguration(PropertyType):
    value_type: DslValue[str] | None = None
    value: DslValue[ParameterValue] | None = None


@dataclass
class ParameterValue(PropertyType):
    boolean: DslValue[bool] | None = None
    double: DslValue[float] | None = None
    enum: DslValue[str] | None = None
    enum_list: list[DslValue[str]] = field(default_factory=list)
    integer: DslValue[int] | None = None
    integer_list: list[DslValue[int]] = field(default_factory=list)
    string: DslValue[str] | None = None
    string_list: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Policy(PropertyType):
    security_hub: DslValue[SecurityHubPolicy] | None = None


@dataclass
class SecurityControlCustomParameter(PropertyType):
    parameters: dict[str, DslValue[ParameterConfiguration]] = field(
        default_factory=dict
    )
    security_control_id: DslValue[str] | None = None


@dataclass
class SecurityControlsConfiguration(PropertyType):
    disabled_security_control_identifiers: list[DslValue[str]] = field(
        default_factory=list
    )
    enabled_security_control_identifiers: list[DslValue[str]] = field(
        default_factory=list
    )
    security_control_custom_parameters: list[
        DslValue[SecurityControlCustomParameter]
    ] = field(default_factory=list)


@dataclass
class SecurityHubPolicy(PropertyType):
    enabled_standard_identifiers: list[DslValue[str]] = field(default_factory=list)
    security_controls_configuration: DslValue[SecurityControlsConfiguration] | None = (
        None
    )
    service_enabled: DslValue[bool] | None = None
