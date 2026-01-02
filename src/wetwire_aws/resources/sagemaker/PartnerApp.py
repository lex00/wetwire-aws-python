"""PropertyTypes for AWS::SageMaker::PartnerApp."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PartnerAppConfig(PropertyType):
    admin_users: list[String] = field(default_factory=list)
    arguments: dict[str, String] = field(default_factory=dict)


@dataclass
class PartnerAppMaintenanceConfig(PropertyType):
    maintenance_window_start: str | None = None
