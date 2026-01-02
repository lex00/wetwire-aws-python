"""PropertyTypes for AWS::EKS::FargateProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Label(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Selector(PropertyType):
    namespace: str | None = None
    labels: list[Label] = field(default_factory=list)
