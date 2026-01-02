"""PropertyTypes for AWS::AppConfig::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Monitor(PropertyType):
    alarm_arn: str | None = None
    alarm_role_arn: str | None = None
