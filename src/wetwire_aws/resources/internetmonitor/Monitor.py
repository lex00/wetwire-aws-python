"""PropertyTypes for AWS::InternetMonitor::Monitor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HealthEventsConfig(PropertyType):
    availability_local_health_events_config: LocalHealthEventsConfig | None = None
    availability_score_threshold: float | None = None
    performance_local_health_events_config: LocalHealthEventsConfig | None = None
    performance_score_threshold: float | None = None


@dataclass
class InternetMeasurementsLogDelivery(PropertyType):
    s3_config: S3Config | None = None


@dataclass
class LocalHealthEventsConfig(PropertyType):
    health_score_threshold: float | None = None
    min_traffic_impact: float | None = None
    status: str | None = None


@dataclass
class S3Config(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None
    log_delivery_status: str | None = None
