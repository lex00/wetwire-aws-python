"""PropertyTypes for AWS::QuickSight::Folder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourcePermission(PropertyType):
    actions: list[String] = field(default_factory=list)
    principal: str | None = None
