"""PropertyTypes for AWS::CloudFront::ContinuousDeploymentPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ContinuousDeploymentPolicyConfig(PropertyType):
    enabled: DslValue[bool] | None = None
    staging_distribution_dns_names: list[DslValue[str]] = field(default_factory=list)
    single_header_policy_config: DslValue[SingleHeaderPolicyConfig] | None = None
    single_weight_policy_config: DslValue[SingleWeightPolicyConfig] | None = None
    traffic_config: DslValue[TrafficConfig] | None = None
    type_: DslValue[str] | None = None


@dataclass
class SessionStickinessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_ttl": "IdleTTL",
        "maximum_ttl": "MaximumTTL",
    }

    idle_ttl: DslValue[int] | None = None
    maximum_ttl: DslValue[int] | None = None


@dataclass
class SingleHeaderConfig(PropertyType):
    header: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SingleHeaderPolicyConfig(PropertyType):
    header: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SingleWeightConfig(PropertyType):
    weight: DslValue[float] | None = None
    session_stickiness_config: DslValue[SessionStickinessConfig] | None = None


@dataclass
class SingleWeightPolicyConfig(PropertyType):
    weight: DslValue[float] | None = None
    session_stickiness_config: DslValue[SessionStickinessConfig] | None = None


@dataclass
class TrafficConfig(PropertyType):
    type_: DslValue[str] | None = None
    single_header_config: DslValue[SingleHeaderConfig] | None = None
    single_weight_config: DslValue[SingleWeightConfig] | None = None
