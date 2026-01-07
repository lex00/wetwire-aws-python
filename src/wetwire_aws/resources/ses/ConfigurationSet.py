"""PropertyTypes for AWS::SES::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DashboardOptions(PropertyType):
    engagement_metrics: DslValue[str] | None = None


@dataclass
class DeliveryOptions(PropertyType):
    max_delivery_seconds: DslValue[float] | None = None
    sending_pool_name: DslValue[str] | None = None
    tls_policy: DslValue[str] | None = None


@dataclass
class GuardianOptions(PropertyType):
    optimized_shared_delivery: DslValue[str] | None = None


@dataclass
class ReputationOptions(PropertyType):
    reputation_metrics_enabled: DslValue[bool] | None = None


@dataclass
class SendingOptions(PropertyType):
    sending_enabled: DslValue[bool] | None = None


@dataclass
class SuppressionOptions(PropertyType):
    suppressed_reasons: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TrackingOptions(PropertyType):
    custom_redirect_domain: DslValue[str] | None = None
    https_policy: DslValue[str] | None = None


@dataclass
class VdmOptions(PropertyType):
    dashboard_options: DslValue[DashboardOptions] | None = None
    guardian_options: DslValue[GuardianOptions] | None = None
