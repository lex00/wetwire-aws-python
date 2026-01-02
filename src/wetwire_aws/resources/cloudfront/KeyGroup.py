"""PropertyTypes for AWS::CloudFront::KeyGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class KeyGroupConfig(PropertyType):
    items: list[String] = field(default_factory=list)
    name: str | None = None
    comment: str | None = None
