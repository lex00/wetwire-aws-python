"""PropertyTypes for AWS::IoT::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AbortConfig(PropertyType):
    criteria_list: list[AbortCriteria] = field(default_factory=list)


@dataclass
class AbortCriteria(PropertyType):
    action: str | None = None
    failure_type: str | None = None
    min_number_of_executed_things: int | None = None
    threshold_percentage: float | None = None


@dataclass
class ExponentialRolloutRate(PropertyType):
    base_rate_per_minute: int | None = None
    increment_factor: float | None = None
    rate_increase_criteria: RateIncreaseCriteria | None = None


@dataclass
class JobExecutionsRetryConfig(PropertyType):
    retry_criteria_list: list[RetryCriteria] = field(default_factory=list)


@dataclass
class JobExecutionsRolloutConfig(PropertyType):
    exponential_rollout_rate: ExponentialRolloutRate | None = None
    maximum_per_minute: int | None = None


@dataclass
class MaintenanceWindow(PropertyType):
    duration_in_minutes: int | None = None
    start_time: str | None = None


@dataclass
class PresignedUrlConfig(PropertyType):
    role_arn: str | None = None
    expires_in_sec: int | None = None


@dataclass
class RateIncreaseCriteria(PropertyType):
    number_of_notified_things: int | None = None
    number_of_succeeded_things: int | None = None


@dataclass
class RetryCriteria(PropertyType):
    failure_type: str | None = None
    number_of_retries: int | None = None


@dataclass
class TimeoutConfig(PropertyType):
    in_progress_timeout_in_minutes: int | None = None
