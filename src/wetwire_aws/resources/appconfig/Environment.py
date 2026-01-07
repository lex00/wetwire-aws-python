"""PropertyTypes for AWS::AppConfig::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Monitor(PropertyType):
    alarm_arn: DslValue[str] | None = None
    alarm_role_arn: DslValue[str] | None = None
