"""PropertyTypes for AWS::QuickSight::Folder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResourcePermission(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[str] | None = None
