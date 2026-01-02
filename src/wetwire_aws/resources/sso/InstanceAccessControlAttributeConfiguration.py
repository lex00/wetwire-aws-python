"""PropertyTypes for AWS::SSO::InstanceAccessControlAttributeConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessControlAttribute(PropertyType):
    key: str | None = None
    value: AccessControlAttributeValue | None = None


@dataclass
class AccessControlAttributeValue(PropertyType):
    source: list[String] = field(default_factory=list)
