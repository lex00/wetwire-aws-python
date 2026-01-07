"""PropertyTypes for AWS::InternetMonitor::Monitor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HealthEventsConfig(PropertyType):
    availability_local_health_events_config: (
        DslValue[LocalHealthEventsConfig] | None
    ) = None
    availability_score_threshold: DslValue[float] | None = None
    performance_local_health_events_config: DslValue[LocalHealthEventsConfig] | None = (
        None
    )
    performance_score_threshold: DslValue[float] | None = None


@dataclass
class InternetMeasurementsLogDelivery(PropertyType):
    s3_config: DslValue[S3Config] | None = None


@dataclass
class LocalHealthEventsConfig(PropertyType):
    health_score_threshold: DslValue[float] | None = None
    min_traffic_impact: DslValue[float] | None = None
    status: DslValue[str] | None = None


@dataclass
class S3Config(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    log_delivery_status: DslValue[str] | None = None
