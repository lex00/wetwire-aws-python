"""PropertyTypes for AWS::EKS::FargateProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Label(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Selector(PropertyType):
    namespace: DslValue[str] | None = None
    labels: list[DslValue[Label]] = field(default_factory=list)
