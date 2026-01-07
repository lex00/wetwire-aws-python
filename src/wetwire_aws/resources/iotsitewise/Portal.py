"""PropertyTypes for AWS::IoTSiteWise::Portal."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Alarms(PropertyType):
    alarm_role_arn: DslValue[str] | None = None
    notification_lambda_arn: DslValue[str] | None = None


@dataclass
class PortalTypeEntry(PropertyType):
    portal_tools: list[DslValue[str]] = field(default_factory=list)
