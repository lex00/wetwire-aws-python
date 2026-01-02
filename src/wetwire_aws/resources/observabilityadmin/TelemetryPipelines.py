"""PropertyTypes for AWS::ObservabilityAdmin::TelemetryPipelines."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TelemetryPipeline(PropertyType):
    arn: str | None = None
    configuration: TelemetryPipelineConfiguration | None = None
    created_time_stamp: float | None = None
    last_update_time_stamp: float | None = None
    name: str | None = None
    status: str | None = None
    status_reason: TelemetryPipelineStatusReason | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class TelemetryPipelineConfiguration(PropertyType):
    body: str | None = None


@dataclass
class TelemetryPipelineStatusReason(PropertyType):
    description: str | None = None
