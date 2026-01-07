"""PropertyTypes for AWS::SSO::InstanceAccessControlAttributeConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessControlAttribute(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[AccessControlAttributeValue] | None = None


@dataclass
class AccessControlAttributeValue(PropertyType):
    source: list[DslValue[str]] = field(default_factory=list)
