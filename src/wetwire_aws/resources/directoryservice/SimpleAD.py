"""PropertyTypes for AWS::DirectoryService::SimpleAD."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class VpcSettings(PropertyType):
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    vpc_id: DslValue[str] | None = None
