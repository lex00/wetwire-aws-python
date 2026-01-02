"""PropertyTypes for AWS::SNS::Topic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoggingConfig(PropertyType):
    protocol: str | None = None
    failure_feedback_role_arn: str | None = None
    success_feedback_role_arn: str | None = None
    success_feedback_sample_rate: str | None = None


@dataclass
class Subscription(PropertyType):
    endpoint: str | None = None
    protocol: str | None = None
