"""PropertyTypes for AWS::EKS::AccessEntry."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessPolicy(PropertyType):
    access_scope: AccessScope | None = None
    policy_arn: str | None = None


@dataclass
class AccessScope(PropertyType):
    type_: str | None = None
    namespaces: list[String] = field(default_factory=list)
