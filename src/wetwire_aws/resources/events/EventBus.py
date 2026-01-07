"""PropertyTypes for AWS::Events::EventBus."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeadLetterConfig(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class LogConfig(PropertyType):
    include_detail: DslValue[str] | None = None
    level: DslValue[str] | None = None
