"""PropertyTypes for AWS::IoTSiteWise::Portal."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Alarms(PropertyType):
    alarm_role_arn: str | None = None
    notification_lambda_arn: str | None = None


@dataclass
class PortalTypeEntry(PropertyType):
    portal_tools: list[String] = field(default_factory=list)
