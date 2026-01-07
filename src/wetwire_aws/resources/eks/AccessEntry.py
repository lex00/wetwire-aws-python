"""PropertyTypes for AWS::EKS::AccessEntry."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessPolicy(PropertyType):
    access_scope: DslValue[AccessScope] | None = None
    policy_arn: DslValue[str] | None = None


@dataclass
class AccessScope(PropertyType):
    type_: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)
