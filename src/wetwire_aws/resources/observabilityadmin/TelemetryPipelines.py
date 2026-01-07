"""PropertyTypes for AWS::ObservabilityAdmin::TelemetryPipelines."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class TelemetryPipeline(PropertyType):
    arn: DslValue[str] | None = None
    configuration: DslValue[TelemetryPipelineConfiguration] | None = None
    created_time_stamp: DslValue[float] | None = None
    last_update_time_stamp: DslValue[float] | None = None
    name: DslValue[str] | None = None
    status: DslValue[str] | None = None
    status_reason: DslValue[TelemetryPipelineStatusReason] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class TelemetryPipelineConfiguration(PropertyType):
    body: DslValue[str] | None = None


@dataclass
class TelemetryPipelineStatusReason(PropertyType):
    description: DslValue[str] | None = None
