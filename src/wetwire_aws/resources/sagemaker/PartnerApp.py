"""PropertyTypes for AWS::SageMaker::PartnerApp."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PartnerAppConfig(PropertyType):
    admin_users: list[DslValue[str]] = field(default_factory=list)
    arguments: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class PartnerAppMaintenanceConfig(PropertyType):
    maintenance_window_start: DslValue[str] | None = None
