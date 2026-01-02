"""PropertyTypes for AWS::AppStream::AppBlockBuilder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessEndpoint(PropertyType):
    endpoint_type: str | None = None
    vpce_id: str | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
