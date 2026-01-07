"""PropertyTypes for AWS::IoT::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AbortConfig(PropertyType):
    criteria_list: list[DslValue[AbortCriteria]] = field(default_factory=list)


@dataclass
class AbortCriteria(PropertyType):
    action: DslValue[str] | None = None
    failure_type: DslValue[str] | None = None
    min_number_of_executed_things: DslValue[int] | None = None
    threshold_percentage: DslValue[float] | None = None


@dataclass
class ExponentialRolloutRate(PropertyType):
    base_rate_per_minute: DslValue[int] | None = None
    increment_factor: DslValue[float] | None = None
    rate_increase_criteria: DslValue[RateIncreaseCriteria] | None = None


@dataclass
class JobExecutionsRetryConfig(PropertyType):
    retry_criteria_list: list[DslValue[RetryCriteria]] = field(default_factory=list)


@dataclass
class JobExecutionsRolloutConfig(PropertyType):
    exponential_rollout_rate: DslValue[ExponentialRolloutRate] | None = None
    maximum_per_minute: DslValue[int] | None = None


@dataclass
class MaintenanceWindow(PropertyType):
    duration_in_minutes: DslValue[int] | None = None
    start_time: DslValue[str] | None = None


@dataclass
class PresignedUrlConfig(PropertyType):
    role_arn: DslValue[str] | None = None
    expires_in_sec: DslValue[int] | None = None


@dataclass
class RateIncreaseCriteria(PropertyType):
    number_of_notified_things: DslValue[int] | None = None
    number_of_succeeded_things: DslValue[int] | None = None


@dataclass
class RetryCriteria(PropertyType):
    failure_type: DslValue[str] | None = None
    number_of_retries: DslValue[int] | None = None


@dataclass
class TimeoutConfig(PropertyType):
    in_progress_timeout_in_minutes: DslValue[int] | None = None
