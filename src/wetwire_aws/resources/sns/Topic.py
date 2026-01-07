"""PropertyTypes for AWS::SNS::Topic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoggingConfig(PropertyType):
    protocol: DslValue[str] | None = None
    failure_feedback_role_arn: DslValue[str] | None = None
    success_feedback_role_arn: DslValue[str] | None = None
    success_feedback_sample_rate: DslValue[str] | None = None


@dataclass
class Subscription(PropertyType):
    endpoint: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
