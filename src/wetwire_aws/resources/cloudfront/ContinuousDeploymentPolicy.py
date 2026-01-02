"""PropertyTypes for AWS::CloudFront::ContinuousDeploymentPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ContinuousDeploymentPolicyConfig(PropertyType):
    enabled: bool | None = None
    staging_distribution_dns_names: list[String] = field(default_factory=list)
    single_header_policy_config: SingleHeaderPolicyConfig | None = None
    single_weight_policy_config: SingleWeightPolicyConfig | None = None
    traffic_config: TrafficConfig | None = None
    type_: str | None = None


@dataclass
class SessionStickinessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_ttl": "IdleTTL",
        "maximum_ttl": "MaximumTTL",
    }

    idle_ttl: int | None = None
    maximum_ttl: int | None = None


@dataclass
class SingleHeaderConfig(PropertyType):
    header: str | None = None
    value: str | None = None


@dataclass
class SingleHeaderPolicyConfig(PropertyType):
    header: str | None = None
    value: str | None = None


@dataclass
class SingleWeightConfig(PropertyType):
    weight: float | None = None
    session_stickiness_config: SessionStickinessConfig | None = None


@dataclass
class SingleWeightPolicyConfig(PropertyType):
    weight: float | None = None
    session_stickiness_config: SessionStickinessConfig | None = None


@dataclass
class TrafficConfig(PropertyType):
    type_: str | None = None
    single_header_config: SingleHeaderConfig | None = None
    single_weight_config: SingleWeightConfig | None = None
