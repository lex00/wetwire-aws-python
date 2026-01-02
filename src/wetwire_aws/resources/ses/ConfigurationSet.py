"""PropertyTypes for AWS::SES::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DashboardOptions(PropertyType):
    engagement_metrics: str | None = None


@dataclass
class DeliveryOptions(PropertyType):
    max_delivery_seconds: float | None = None
    sending_pool_name: str | None = None
    tls_policy: str | None = None


@dataclass
class GuardianOptions(PropertyType):
    optimized_shared_delivery: str | None = None


@dataclass
class ReputationOptions(PropertyType):
    reputation_metrics_enabled: bool | None = None


@dataclass
class SendingOptions(PropertyType):
    sending_enabled: bool | None = None


@dataclass
class SuppressionOptions(PropertyType):
    suppressed_reasons: list[String] = field(default_factory=list)


@dataclass
class TrackingOptions(PropertyType):
    custom_redirect_domain: str | None = None
    https_policy: str | None = None


@dataclass
class VdmOptions(PropertyType):
    dashboard_options: DashboardOptions | None = None
    guardian_options: GuardianOptions | None = None
