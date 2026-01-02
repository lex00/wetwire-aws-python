"""PropertyTypes for AWS::Events::EventBus."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeadLetterConfig(PropertyType):
    arn: str | None = None


@dataclass
class LogConfig(PropertyType):
    include_detail: str | None = None
    level: str | None = None
