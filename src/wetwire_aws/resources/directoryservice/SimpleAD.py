"""PropertyTypes for AWS::DirectoryService::SimpleAD."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class VpcSettings(PropertyType):
    subnet_ids: list[String] = field(default_factory=list)
    vpc_id: str | None = None
