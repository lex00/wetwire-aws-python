"""PropertyTypes for AWS::CloudFront::MonitoringSubscription."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MonitoringSubscription(PropertyType):
    realtime_metrics_subscription_config: RealtimeMetricsSubscriptionConfig | None = (
        None
    )


@dataclass
class RealtimeMetricsSubscriptionConfig(PropertyType):
    realtime_metrics_subscription_status: str | None = None
